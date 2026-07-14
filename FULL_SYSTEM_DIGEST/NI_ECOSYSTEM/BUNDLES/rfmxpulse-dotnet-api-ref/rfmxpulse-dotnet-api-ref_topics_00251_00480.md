# NI DOCUMENT BUNDLE: rfmxpulse-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxpulse-dotnet-api-ref start=251 end=480 -->
<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemeasurementpointreference.html language=enus -->
## TOPIC 00251: RFmxPulseMXPulseMeasurementPointReference Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemeasurementpointreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemeasurementpointreference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseMeasurementPointReferenceMembersNameValueDe

### RFmxPulseMXPulseMeasurementPointReference Enumeration

Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseMeasurementPointReference

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rise | 0 | The measurement point is defined in reference to the rising edge. |
| Center | 1 | The measurement point is defined in reference to the center of the pulse. |
| Fall | 2 | The measurement point is defined in reference to the falling edge. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsamplitudedeviationunit.html language=enus -->
## TOPIC 00252: RFmxPulseMXPulseMetricsAmplitudeDeviationUnit Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsamplitudedeviationunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsamplitudedeviationunit.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseMetricsAmplitudeDeviationUnitMembersNameValueDescriptionPercentage0Amplitude deviation results are

### RFmxPulseMXPulseMetricsAmplitudeDeviationUnit Enumeration

Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseMetricsAmplitudeDeviationUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Percentage | 0 | Amplitude deviation results are returned as a percentage. |
| dB | 1 | Amplitude deviation results are returned in dB. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsenabled.html language=enus -->
## TOPIC 00253: RFmxPulseMXPulseMetricsEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pulse metrics results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseMetricsEnabledMembersNameValueDescriptionFalse0Pulse Metric results computation is disabled. True1Pulse Metric results computation is enabled.

### RFmxPulseMXPulseMetricsEnabled Enumeration

Specifies whether to enable pulse metrics results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseMetricsEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Pulse Metric results computation is disabled. |
| True | 1 | Pulse Metric results computation is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html language=enus -->
## TOPIC 00254: RFmxPulseMXPulseModulationType Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseModulationTypeMembersNameValueDescriptionCW0Continous wave where the frequency remains constant over pulse ON duration.

### RFmxPulseMXPulseModulationType Enumeration

Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| CW | 0 | Continous wave where the frequency remains constant over pulse ON duration. |
| LinearFM | 1 | Frequency varies linearly within pulse ON duration. |
| TriangularFM | 2 | Frequency varies with two lienar FM chirps with opposite slopes within pulse ON duration. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html language=enus -->
## TOPIC 00255: RFmxPulseMXPulseMultipleMeasurementPointsEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseMult

### RFmxPulseMXPulseMultipleMeasurementPointsEnabled Enumeration

Specifies whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseMultipleMeasurementPointsEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Multiple Measurement Points related computation is disabled. |
| True | 1 | Multiple Measurement Points related computation is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchacquiredamplitudetrace__string-double-out-ref-ref-ref.html language=enus -->
## TOPIC 00256: FetchAcquiredAmplitudeTrace(string, double, out double, ref float[], ref int[], ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchacquiredamplitudetrace__string-double-out-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchacquiredamplitudetrace__string-double-out-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the PulseAcquisitionTraceSelect method to select all pulses or the subset of acquired pulses. When you set the SegmentedAcquisitionEnabled method to False, returns a single e

### FetchAcquiredAmplitudeTrace(string, double, out double, ref float[], ref int[], ref double[])

Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to select all pulses or the subset of acquired pulses. When you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html), returns a single element in the Start Indices and Start Time Stamp array.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchAcquiredAmplitudeTrace(string selectorString, double timeout, out double sampleDuration, ref float[] amplitude, ref int[] startIndex, ref double[] startTimeStamp)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| sampleDuration | out double | Upon return, contains the sample duration, in seconds. |
| amplitude | ref float[] | Upon return, contains the trace of amplitude measured in units specified by PulseAmplitudeTraceUnit method. |
| startIndex | ref int[] | Upon return, contains the array of sample indices for the start of each segment. |
| startTimeStamp | ref double[] | Upon return, contains the array of timestamps of each segment start, in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchamplitudetrace__string-double-ref.html language=enus -->
## TOPIC 00257: FetchAmplitudeTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchamplitudetrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchamplitudetrace__string-double-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude trace of the selected pulse.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchAmplitudeTrace(string selectorString, double timeout, ref AnalogWaveform< float > amplitude)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of th

### FetchAmplitudeTrace(string, double, ref AnalogWaveform< float >)

Fetches the amplitude trace of the selected pulse.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchAmplitudeTrace(string selectorString, double timeout, ref AnalogWaveform< float > amplitude)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| amplitude | ref AnalogWaveform< float > | Upon return, contains the trace of amplitude measured in units specified by PulseAmplitudeTraceUnit method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchburstintrapulsestabilitytrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00258: FetchBurstIntrapulseStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchburstintrapulsestabilitytrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchburstintrapulsestabilitytrace__string-double-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points.(br/) SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchBurstIntrapulseStabilityTrace(string selectorString, double timeout, ref AnalogWaveform<

### FetchBurstIntrapulseStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points.(br/)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchBurstIntrapulseStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > intrapulseAverageAmplitudeStability, ref AnalogWaveform< float > intrapulseAveragePhaseStability, ref AnalogWaveform< float > intrapulseAverageTotalStability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| intrapulseAverageAmplitudeStability | ref AnalogWaveform< float > | Upon return, contains the intrapulse average amplitude stability trace at multiple measurement points. This value is expressed in dB. |
| intrapulseAveragePhaseStability | ref AnalogWaveform< float > | Upon return, contains the intrapulse average phase stability trace at multiple measurement points. This value is expressed in dB. |
| intrapulseAverageTotalStability | ref AnalogWaveform< float > | Upon return, contains the intrapulse average total stability trace at multiple measurement points. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchburstselectedpositionstabilitytrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00259: FetchBurstSelectedPositionStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchburstselectedpositionstabilitytrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchburstselectedpositionstabilitytrace__string-double-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the burst stability trace of the selected position.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchBurstSelectedPositionStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > pulseAmplitudeStability, ref AnalogWaveform< float > pulsePhaseStability,

### FetchBurstSelectedPositionStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the burst stability trace of the selected position.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchBurstSelectedPositionStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > pulseAmplitudeStability, ref AnalogWaveform< float > pulsePhaseStability, ref AnalogWaveform< float > pulseTotalStability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pulseAmplitudeStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse amplitude stability, in dB. |
| pulsePhaseStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse phase stability, in dB. |
| pulseTotalStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse total stability, in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchfrequencytrace__string-double-ref.html language=enus -->
## TOPIC 00260: FetchFrequencyTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchfrequencytrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchfrequencytrace__string-double-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency trace of the selected pulse.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchFrequencyTrace(string selectorString, double timeout, ref AnalogWaveform< float > frequency)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of th

### FetchFrequencyTrace(string, double, ref AnalogWaveform< float >)

Fetches the frequency trace of the selected pulse.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchFrequencyTrace(string selectorString, double timeout, ref AnalogWaveform< float > frequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| frequency | ref AnalogWaveform< float > | Upon return, contains the trace of frequency, in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchintrapulsestabilitytrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00261: FetchIntrapulseStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchintrapulsestabilitytrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchintrapulsestabilitytrace__string-double-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position.(br/) SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchIntrapulseStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > intrapulseAmplitudeStability,

### FetchIntrapulseStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position.(br/)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchIntrapulseStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > intrapulseAmplitudeStability, ref AnalogWaveform< float > intrapulsePhaseStability, ref AnalogWaveform< float > intrapulseTotalStability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| intrapulseAmplitudeStability | ref AnalogWaveform< float > | Upon return, contains the intrapulse amplitude stability trace at multiple measurement points. This value is expressed in dB. |
| intrapulsePhaseStability | ref AnalogWaveform< float > | Upon return, contains the intrapulse phase stability trace at multiple measurement points. This value is expressed in dB. |
| intrapulseTotalStability | ref AnalogWaveform< float > | Upon return, contains the intrapulse total stability trace at multiple measurement points. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchiqtrace__string-double-ref.html language=enus -->
## TOPIC 00262: FetchIQTrace(string, double, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchiqtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchiqtrace__string-double-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the IQ trace of the selected pulse.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchIQTrace(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > IQData)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result

### FetchIQTrace(string, double, ref ComplexWaveform< ComplexSingle >)

Fetches the IQ trace of the selected pulse.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchIQTrace(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > IQData)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| IQData | ref ComplexWaveform< ComplexSingle > | Upon return, contains the trace of IQ data in time domain. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchmultiplemeasurementpointsstabilitytrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00263: FetchMultipleMeasurementPointsStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchmultiplemeasurementpointsstabilitytrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchmultiplemeasurementpointsstabilitytrace__string-double-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the multiple measurement points stability trace.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchMultipleMeasurementPointsStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > pulseAverageAmplitudeStability, ref AnalogWaveform< float > pulseAverage

### FetchMultipleMeasurementPointsStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the multiple measurement points stability trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchMultipleMeasurementPointsStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > pulseAverageAmplitudeStability, ref AnalogWaveform< float > pulseAveragePhaseStability, ref AnalogWaveform< float > pulseAverageTotalStability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pulseAverageAmplitudeStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse average amplitude stability for multiple measurement points, in dB. |
| pulseAveragePhaseStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse average phase stability for multiple measurement points, in dB. |
| pulseAverageTotalStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse average total stability for multiple measurement points, in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchphasewrappedtrace__string-double-ref.html language=enus -->
## TOPIC 00264: FetchPhaseWrappedTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchphasewrappedtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchphasewrappedtrace__string-double-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the wrapped phase trace of the selected pulse.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchPhaseWrappedTrace(string selectorString, double timeout, ref AnalogWaveform< float > wrappedPhase)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string compri

### FetchPhaseWrappedTrace(string, double, ref AnalogWaveform< float >)

Fetches the wrapped phase trace of the selected pulse.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchPhaseWrappedTrace(string selectorString, double timeout, ref AnalogWaveform< float > wrappedPhase)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| wrappedPhase | ref AnalogWaveform< float > | Upon return, contains the trace of wrapped phase, in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchpulsetopulsestabilitytrace__string-double-ref-ref-ref-ref.html language=enus -->
## TOPIC 00265: FetchPulseToPulseStabilityTrace(string, double, ref int[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchpulsetopulsestabilitytrace__string-double-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchpulsetopulsestabilitytrace__string-double-ref-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the pulse to pulse stability trace.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchPulseToPulseStabilityTrace(string selectorString, double timeout, ref int[] pulseIndex, ref double[] pulseToPulseAmplitudeStability, ref double[] pulseToPulsePhaseStability, ref double[] pulse

### FetchPulseToPulseStabilityTrace(string, double, ref int[], ref double[], ref double[], ref double[])

Fetches the pulse to pulse stability trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchPulseToPulseStabilityTrace(string selectorString, double timeout, ref int[] pulseIndex, ref double[] pulseToPulseAmplitudeStability, ref double[] pulseToPulsePhaseStability, ref double[] pulseToPulseTotalStability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pulseIndex | ref int[] | Upon return, contains the pulse index. |
| pulseToPulseAmplitudeStability | ref double[] | Upon return, contains the trace of pulse to pulse amplitude stability, in dB. |
| pulseToPulsePhaseStability | ref double[] | Upon return, contains the trace of pulse to pulse phase stability, in dB. |
| pulseToPulseTotalStability | ref double[] | Upon return, contains the trace of pulse to pulse total stability, in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchstabilitytrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00266: FetchStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchstabilitytrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchstabilitytrace__string-double-ref-ref-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stability trace of the selected pulse.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > pulseAmplitudeStability, ref AnalogWaveform< float > pulsePhaseStability, ref AnalogWaveform< float > p

### FetchStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the stability trace of the selected pulse.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchStabilityTrace(string selectorString, double timeout, ref AnalogWaveform< float > pulseAmplitudeStability, ref AnalogWaveform< float > pulsePhaseStability, ref AnalogWaveform< float > pulseTotalStability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pulseAmplitudeStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse amplitude stability, in dB. |
| pulsePhaseStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse phase stability, in dB. |
| pulseTotalStability | ref AnalogWaveform< float > | Upon return, contains the trace of pulse total stability, in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchtimesidelobetrace__string-double-ref.html language=enus -->
## TOPIC 00267: FetchTimeSidelobeTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchtimesidelobetrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-fetchtimesidelobetrace__string-double-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the time sidelobe trace for the selected pulse. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int FetchTimeSidelobeTrace(string selectorString, double timeout, ref AnalogWaveform< float > timeSidelobe)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comp

### FetchTimeSidelobeTrace(string, double, ref AnalogWaveform< float >)

Fetches the time sidelobe trace for the selected pulse.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int FetchTimeSidelobeTrace(string selectorString, double timeout, ref AnalogWaveform< float > timeSidelobe)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| timeSidelobe | ref AnalogWaveform< float > | Upon return, contains the trace of correlated magnitude, in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestability__string-ref.html language=enus -->
## TOPIC 00268: GetAmplitudeStability(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestability__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestability__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeStability(string selectorString, ref double[] value)RemarksThis method g

### GetAmplitudeStability(string, ref double[])

Gets the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeStability(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsAmplitudeStability](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitymaximum__string-out.html language=enus -->
## TOPIC 00269: GetAmplitudeStabilityMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum amplitude stability across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeStabilityMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAmplitudeStabilityMaximum

### GetAmplitudeStabilityMaximum(string, out double)

Gets the maximum amplitude stability across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeStabilityMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAmplitudeStabilityMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum amplitude stability across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitymean__string-out.html language=enus -->
## TOPIC 00270: GetAmplitudeStabilityMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the amplitude stability values across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeStabilityMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAmplitudeStability

### GetAmplitudeStabilityMean(string, out double)

Gets the mean of the amplitude stability values across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeStabilityMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAmplitudeStabilityMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the amplitude stability values across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilityminimum__string-out.html language=enus -->
## TOPIC 00271: GetAmplitudeStabilityMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilityminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilityminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum amplitude stability across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeStabilityMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAmplitudeStabilityMinimum

### GetAmplitudeStabilityMinimum(string, out double)

Gets the minimum amplitude stability across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeStabilityMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAmplitudeStabilityMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum amplitude stability across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitystandarddeviation__string-out.html language=enus -->
## TOPIC 00272: GetAmplitudeStabilityStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getamplitudestabilitystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the amplitude stability standard deviation across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeStabilityStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAmpli

### GetAmplitudeStabilityStandardDeviation(string, out double)

Gets the amplitude stability standard deviation across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeStabilityStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAmplitudeStabilityStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the amplitude stability standard deviation across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageamplitudestability__string-out.html language=enus -->
## TOPIC 00273: GetAverageAmplitudeStability(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageamplitudestability__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageamplitudestability__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average amplitude stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the amplitude over the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageAmplitudeStability(string selectorString, out double

### GetAverageAmplitudeStability(string, out double)

Gets the average amplitude stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the amplitude over the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageAmplitudeStability(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageAmplitudeStability](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average amplitude stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the amplitude over the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequency__string-ref.html language=enus -->
## TOPIC 00274: GetAverageFrequency(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequency__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average frequencie for all measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageFrequency(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsAverageFrequency attribute.ParametersNameType

### GetAverageFrequency(string, ref double[])

Gets the average frequencie for all measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageFrequency(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsAverageFrequency](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the average frequencie for all measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencymaximum__string-out.html language=enus -->
## TOPIC 00275: GetAverageFrequencyMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum average frequency across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageFrequencyMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverageFrequencyMaximum attrib

### GetAverageFrequencyMaximum(string, out double)

Gets the maximum average frequency across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageFrequencyMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageFrequencyMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum average frequency across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencymean__string-out.html language=enus -->
## TOPIC 00276: GetAverageFrequencyMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the average frequency across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageFrequencyMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverageFrequencyMean attribut

### GetAverageFrequencyMean(string, out double)

Gets the mean of the average frequency across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageFrequencyMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageFrequencyMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the average frequency across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencyminimum__string-out.html language=enus -->
## TOPIC 00277: GetAverageFrequencyMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencyminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencyminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum average frequency across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageFrequencyMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverageFrequencyMinimum attrib

### GetAverageFrequencyMinimum(string, out double)

Gets the minimum average frequency across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageFrequencyMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageFrequencyMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum average frequency across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencystandarddeviation__string-out.html language=enus -->
## TOPIC 00278: GetAverageFrequencyStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragefrequencystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageFrequencyStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAv

### GetAverageFrequencyStandardDeviation(string, out double)

Gets the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageFrequencyStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageFrequencyStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevel__string-ref.html language=enus -->
## TOPIC 00279: GetAverageLevel(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevel__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevel__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power levels during the pulse period for all measured pulses. The values are expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageLevel(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsAverageLevel attribut

### GetAverageLevel(string, ref double[])

Gets the average power levels during the pulse period for all measured pulses. The values are expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageLevel(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsAverageLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the average power levels during the pulse period for all measured pulses. The values are expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelmaximum__string-out.html language=enus -->
## TOPIC 00280: GetAverageLevelMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageLevelMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverage

### GetAverageLevelMaximum(string, out double)

Gets the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageLevelMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageLevelMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelmean__string-out.html language=enus -->
## TOPIC 00281: GetAverageLevelMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageLevelMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAvera

### GetAverageLevelMean(string, out double)

Gets the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageLevelMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageLevelMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelminimum__string-out.html language=enus -->
## TOPIC 00282: GetAverageLevelMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageLevelMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverage

### GetAverageLevelMinimum(string, out double)

Gets the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageLevelMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageLevelMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelstandarddeviation__string-out.html language=enus -->
## TOPIC 00283: GetAverageLevelStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragelevelstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageLevelStandardDeviation(string selectorString, out double value)RemarksThis method gets the

### GetAverageLevelStandardDeviation(string, out double)

Gets the standard deviation of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageLevelStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageLevelStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevel__string-ref.html language=enus -->
## TOPIC 00284: GetAverageOnLevel(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevel__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevel__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power levels during the ON duration for all measured pulses. The values are expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageOnLevel(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsAverageOnLevel attri

### GetAverageOnLevel(string, ref double[])

Gets the average power levels during the ON duration for all measured pulses. The values are expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageOnLevel(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsAverageOnLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the average power levels during the ON duration for all measured pulses. The values are expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelmaximum__string-out.html language=enus -->
## TOPIC 00285: GetAverageOnLevelMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageOnLevelMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverag

### GetAverageOnLevelMaximum(string, out double)

Gets the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageOnLevelMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageOnLevelMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelmean__string-out.html language=enus -->
## TOPIC 00286: GetAverageOnLevelMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageOnLevelMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAver

### GetAverageOnLevelMean(string, out double)

Gets the mean of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageOnLevelMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageOnLevelMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelminimum__string-out.html language=enus -->
## TOPIC 00287: GetAverageOnLevelMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageOnLevelMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverag

### GetAverageOnLevelMinimum(string, out double)

Gets the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageOnLevelMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageOnLevelMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelstandarddeviation__string-out.html language=enus -->
## TOPIC 00288: GetAverageOnLevelStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaverageonlevelstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageOnLevelStandardDeviation(string selectorString, out double value)RemarksThis method gets th

### GetAverageOnLevelStandardDeviation(string, out double)

Gets the standard deviation of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageOnLevelStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageOnLevelStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephase__string-ref.html language=enus -->
## TOPIC 00289: GetAveragePhase(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephase__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephase__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average phase for all measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAveragePhase(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsAveragePhase attribute.ParametersNameTypeDescript

### GetAveragePhase(string, ref double[])

Gets the average phase for all measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAveragePhase(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsAveragePhase](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the average phase for all measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasemaximum__string-out.html language=enus -->
## TOPIC 00290: GetAveragePhaseMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum average phase across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAveragePhaseMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAveragePhaseMaximum attribute.Par

### GetAveragePhaseMaximum(string, out double)

Gets the maximum average phase across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAveragePhaseMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAveragePhaseMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum average phase across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasemean__string-out.html language=enus -->
## TOPIC 00291: GetAveragePhaseMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the average phase across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAveragePhaseMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAveragePhaseMean attribute.Param

### GetAveragePhaseMean(string, out double)

Gets the mean of the average phase across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAveragePhaseMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAveragePhaseMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the average phase across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephaseminimum__string-out.html language=enus -->
## TOPIC 00292: GetAveragePhaseMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephaseminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephaseminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum average phase across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAveragePhaseMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAveragePhaseMinimum attribute.Par

### GetAveragePhaseMinimum(string, out double)

Gets the minimum average phase across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAveragePhaseMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAveragePhaseMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum average phase across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasestability__string-out.html language=enus -->
## TOPIC 00293: GetAveragePhaseStability(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasestability__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasestability__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average phase stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the phase over the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAveragePhaseStability(string selectorString, out double value)Remar

### GetAveragePhaseStability(string, out double)

Gets the average phase stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the phase over the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAveragePhaseStability(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAveragePhaseStability](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average phase stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the phase over the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasestandarddeviation__string-out.html language=enus -->
## TOPIC 00294: GetAveragePhaseStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragephasestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the average phase across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAveragePhaseStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAvera

### GetAveragePhaseStandardDeviation(string, out double)

Gets the standard deviation of the average phase across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAveragePhaseStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAveragePhaseStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the average phase across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragetotalstability__string-out.html language=enus -->
## TOPIC 00295: GetAverageTotalStability(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragetotalstability__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getaveragetotalstability__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average total stability over measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAverageTotalStability(string selectorString, out double value)RemarksThis method gets the value of PulseResultsAverageTotalStability attribute.Paramete

### GetAverageTotalStability(string, out double)

Gets the average total stability over measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAverageTotalStability(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsAverageTotalStability](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average total stability over measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevel__string-ref.html language=enus -->
## TOPIC 00296: GetBaseLevel(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevel__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevel__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the base levels for all measured pulses. The values are expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetBaseLevel(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsBaseLevel attribute.ParametersNameTypeDescriptionselector

### GetBaseLevel(string, ref double[])

Gets the base levels for all measured pulses. The values are expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetBaseLevel(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsBaseLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the base levels for all measured pulses. The values are expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelmaximum__string-out.html language=enus -->
## TOPIC 00297: GetBaseLevelMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum base level across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetBaseLevelMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsBaseLevelMaximum attribute.ParametersNameTy

### GetBaseLevelMaximum(string, out double)

Gets the maximum base level across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetBaseLevelMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsBaseLevelMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum base level across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelmean__string-out.html language=enus -->
## TOPIC 00298: GetBaseLevelMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the base levels across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetBaseLevelMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsBaseLevelMean attribute.ParametersNameTyp

### GetBaseLevelMean(string, out double)

Gets the mean of the base levels across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetBaseLevelMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsBaseLevelMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the base levels across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelminimum__string-out.html language=enus -->
## TOPIC 00299: GetBaseLevelMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum base level across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetBaseLevelMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsBaseLevelMinimum attribute.ParametersNameTy

### GetBaseLevelMinimum(string, out double)

Gets the minimum base level across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetBaseLevelMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsBaseLevelMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum base level across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelstandarddeviation__string-out.html language=enus -->
## TOPIC 00300: GetBaseLevelStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getbaselevelstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the base levels across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetBaseLevelStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsBaseLevelStand

### GetBaseLevelStandardDeviation(string, out double)

Gets the standard deviation of the base levels across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetBaseLevelStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsBaseLevelStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the base levels across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getburstindex__string-ref.html language=enus -->
## TOPIC 00301: GetBurstIndex(string, ref int[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getburstindex__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getburstindex__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the burst indices of all the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetBurstIndex(string selectorString, ref int[] value)RemarksThis method gets the value of PulseResultsBurstIndex attribute.ParametersNameTypeDescriptionselectorStringstringSpecifies the res

### GetBurstIndex(string, ref int[])

Gets the burst indices of all the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetBurstIndex(string selectorString, ref int[] value)

#### Remarks

This method gets the value of [PulseResultsBurstIndex](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref int[] | Upon return, contains the burst indices of all the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroop__string-ref.html language=enus -->
## TOPIC 00302: GetDroop(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroop__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroop__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeD

### GetDroop(string, ref double[])

Gets the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDroop(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsDroop](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopmaximum__string-out.html language=enus -->
## TOPIC 00303: GetDroopMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDroopMaximum(string selector

### GetDroopMaximum(string, out double)

Gets the maximum of droop values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDroopMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDroopMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopmean__string-out.html language=enus -->
## TOPIC 00304: GetDroopMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDroopMean(string selectorSt

### GetDroopMean(string, out double)

Gets the mean of the droop values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDroopMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDroopMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopminimum__string-out.html language=enus -->
## TOPIC 00305: GetDroopMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDroopMinimum(string selector

### GetDroopMinimum(string, out double)

Gets the minimum of droop values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDroopMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDroopMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopstandarddeviation__string-out.html language=enus -->
## TOPIC 00306: GetDroopStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdroopstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDroopStandard

### GetDroopStandardDeviation(string, out double)

Gets the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDroopStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDroopStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycycle__string-ref.html language=enus -->
## TOPIC 00307: GetDutyCycle(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycycle__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycycle__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDutyCycle(string selectorString, ref double[] value)RemarksThis method gets th

### GetDutyCycle(string, ref double[])

Gets the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDutyCycle(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsDutyCycle](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclemaximum__string-out.html language=enus -->
## TOPIC 00308: GetDutyCycleMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum duty cycle across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDutyCycleMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsDutyCycleMaximum attribute.Paramet

### GetDutyCycleMaximum(string, out double)

Gets the maximum duty cycle across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDutyCycleMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDutyCycleMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum duty cycle across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclemean__string-out.html language=enus -->
## TOPIC 00309: GetDutyCycleMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDutyCycleMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsDutyCycleMean attribute.Parame

### GetDutyCycleMean(string, out double)

Gets the mean of duty cycle values across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDutyCycleMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDutyCycleMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycycleminimum__string-out.html language=enus -->
## TOPIC 00310: GetDutyCycleMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycycleminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycycleminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum duty cycle across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDutyCycleMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsDutyCycleMinimum attribute.Paramet

### GetDutyCycleMinimum(string, out double)

Gets the minimum duty cycle across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDutyCycleMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDutyCycleMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum duty cycle across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclestandarddeviation__string-out.html language=enus -->
## TOPIC 00311: GetDutyCycleStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getdutycyclestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDutyCycleStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsDut

### GetDutyCycleStandardDeviation(string, out double)

Gets the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDutyCycleStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsDutyCycleStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalledge__string-ref.html language=enus -->
## TOPIC 00312: GetFallEdge(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalledge__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalledge__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFallEdge(string selectorString, ref double[] value)RemarksThi

### GetFallEdge(string, ref double[])

Gets the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFallEdge(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFallEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltime__string-ref.html language=enus -->
## TOPIC 00313: GetFallTime(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltime__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltime__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFallTime(string selectorString, ref double[] value)Re

### GetFallTime(string, ref double[])

Gets the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFallTime(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFallTime](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimemaximum__string-out.html language=enus -->
## TOPIC 00314: GetFallTimeMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum fall time across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFallTimeMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFallTimeMaximum attribute.ParametersNameT

### GetFallTimeMaximum(string, out double)

Gets the maximum fall time across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFallTimeMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFallTimeMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum fall time across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimemean__string-out.html language=enus -->
## TOPIC 00315: GetFallTimeMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the fall time values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFallTimeMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFallTimeMean attribute.Parameters

### GetFallTimeMean(string, out double)

Gets the mean of the fall time values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFallTimeMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFallTimeMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the fall time values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimeminimum__string-out.html language=enus -->
## TOPIC 00316: GetFallTimeMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimeminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimeminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum fall time across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFallTimeMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFallTimeMinimum attribute.ParametersNameT

### GetFallTimeMinimum(string, out double)

Gets the minimum fall time across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFallTimeMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFallTimeMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum fall time across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimestandarddeviation__string-out.html language=enus -->
## TOPIC 00317: GetFallTimeStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfalltimestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFallTimeStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFallTi

### GetFallTimeStandardDeviation(string, out double)

Gets the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFallTimeStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFallTimeStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2__string-ref.html language=enus -->
## TOPIC 00318: GetFMChirpRate2(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz/us.This result is valid only for trian

### GetFMChirpRate2(string, ref double[])

Gets the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRate2(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRate2](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2maximum__string-out.html language=enus -->
## TOPIC 00319: GetFMChirpRate2Maximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2maximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRate2Maximum(string selectorString, out double value)RemarksThis method get

### GetFMChirpRate2Maximum(string, out double)

Gets the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRate2Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRate2Maximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2mean__string-out.html language=enus -->
## TOPIC 00320: GetFMChirpRate2Mean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2mean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2mean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRate2Mean(string selectorString, out double value)RemarksThis method g

### GetFMChirpRate2Mean(string, out double)

Gets the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRate2Mean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRate2Mean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2minimum__string-out.html language=enus -->
## TOPIC 00321: GetFMChirpRate2Minimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2minimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2minimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRate2Minimum(string selectorString, out double value)RemarksThis method get

### GetFMChirpRate2Minimum(string, out double)

Gets the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRate2Minimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRate2Minimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2standarddeviation__string-out.html language=enus -->
## TOPIC 00322: GetFMChirpRate2StandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2standarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate2standarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRate2StandardDeviation(string selectorString, out double

### GetFMChirpRate2StandardDeviation(string, out double)

Gets the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRate2StandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRate2StandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate__string-ref.html language=enus -->
## TOPIC 00323: GetFMChirpRate(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprate__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for each pulse. This value is expressed in Hz/us.This result is valid for linear FM and triangular

### GetFMChirpRate(string, ref double[])

Gets the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for each pulse. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRate(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRate](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for each pulse. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratemaximum__string-out.html language=enus -->
## TOPIC 00324: GetFMChirpRateMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRateMaximum(string selectorString, out double value)RemarksThis method ge

### GetFMChirpRateMaximum(string, out double)

Gets the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRateMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRateMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratemean__string-out.html language=enus -->
## TOPIC 00325: GetFMChirpRateMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRateMean(string selectorString, out double value)RemarksThis method

### GetFMChirpRateMean(string, out double)

Gets the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRateMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRateMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprateminimum__string-out.html language=enus -->
## TOPIC 00326: GetFMChirpRateMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprateminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirprateminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRateMinimum(string selectorString, out double value)RemarksThis method ge

### GetFMChirpRateMinimum(string, out double)

Gets the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRateMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRateMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratestandarddeviation__string-out.html language=enus -->
## TOPIC 00327: GetFMChirpRateStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpratestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpRateStandardDeviation(string selectorString, out doubl

### GetFMChirpRateStandardDeviation(string, out double)

Gets the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpRateStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpRateStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2__string-ref.html language=enus -->
## TOPIC 00328: GetFMChirpStartFrequency2(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular F

### GetFMChirpStartFrequency2(string, ref double[])

Gets the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequency2(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequency2](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2maximum__string-out.html language=enus -->
## TOPIC 00329: GetFMChirpStartFrequency2Maximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2maximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequency2Maximum(string selectorString, out double value)RemarksThi

### GetFMChirpStartFrequency2Maximum(string, out double)

Gets the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequency2Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequency2Maximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2mean__string-out.html language=enus -->
## TOPIC 00330: GetFMChirpStartFrequency2Mean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2mean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2mean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequency2Mean(string selectorString, out double value)RemarksT

### GetFMChirpStartFrequency2Mean(string, out double)

Gets the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequency2Mean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequency2Mean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2minimum__string-out.html language=enus -->
## TOPIC 00331: GetFMChirpStartFrequency2Minimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2minimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2minimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequency2Minimum(string selectorString, out double value)RemarksThi

### GetFMChirpStartFrequency2Minimum(string, out double)

Gets the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequency2Minimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequency2Minimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2standarddeviation__string-out.html language=enus -->
## TOPIC 00332: GetFMChirpStartFrequency2StandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2standarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency2standarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequency2StandardDeviation(string selectorString, out d

### GetFMChirpStartFrequency2StandardDeviation(string, out double)

Gets the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequency2StandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequency2StandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency__string-ref.html language=enus -->
## TOPIC 00333: GetFMChirpStartFrequency(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequency__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and trian

### GetFMChirpStartFrequency(string, ref double[])

Gets the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequency(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequency](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencymaximum__string-out.html language=enus -->
## TOPIC 00334: GetFMChirpStartFrequencyMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequencyMaximum(string selectorString, out double value)Rem

### GetFMChirpStartFrequencyMaximum(string, out double)

Gets the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequencyMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequencyMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencymean__string-out.html language=enus -->
## TOPIC 00335: GetFMChirpStartFrequencyMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequencyMean(string selectorString, out double value)R

### GetFMChirpStartFrequencyMean(string, out double)

Gets the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequencyMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequencyMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencyminimum__string-out.html language=enus -->
## TOPIC 00336: GetFMChirpStartFrequencyMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencyminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencyminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequencyMinimum(string selectorString, out double value)Rem

### GetFMChirpStartFrequencyMinimum(string, out double)

Gets the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequencyMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequencyMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencystandarddeviation__string-out.html language=enus -->
## TOPIC 00337: GetFMChirpStartFrequencyStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstartfrequencystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStartFrequencyStandardDeviation(string selectorString

### GetFMChirpStartFrequencyStandardDeviation(string, out double)

Gets the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStartFrequencyStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStartFrequencyStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2__string-ref.html language=enus -->
## TOPIC 00338: GetFMChirpStopFrequency2(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM

### GetFMChirpStopFrequency2(string, ref double[])

Gets the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequency2(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequency2](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2maximum__string-out.html language=enus -->
## TOPIC 00339: GetFMChirpStopFrequency2Maximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2maximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequency2Maximum(string selectorString, out double value)RemarksThis

### GetFMChirpStopFrequency2Maximum(string, out double)

Gets the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequency2Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequency2Maximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2mean__string-out.html language=enus -->
## TOPIC 00340: GetFMChirpStopFrequency2Mean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2mean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2mean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequency2Mean(string selectorString, out double value)RemarksThi

### GetFMChirpStopFrequency2Mean(string, out double)

Gets the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequency2Mean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequency2Mean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2minimum__string-out.html language=enus -->
## TOPIC 00341: GetFMChirpStopFrequency2Minimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2minimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2minimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequency2Minimum(string selectorString, out double value)RemarksThis

### GetFMChirpStopFrequency2Minimum(string, out double)

Gets the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequency2Minimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequency2Minimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2standarddeviation__string-out.html language=enus -->
## TOPIC 00342: GetFMChirpStopFrequency2StandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2standarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency2standarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequency2StandardDeviation(string selectorString, out dou

### GetFMChirpStopFrequency2StandardDeviation(string, out double)

Gets the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequency2StandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequency2StandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency__string-ref.html language=enus -->
## TOPIC 00343: GetFMChirpStopFrequency(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequency__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triang

### GetFMChirpStopFrequency(string, ref double[])

Gets the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequency(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequency](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencymaximum__string-out.html language=enus -->
## TOPIC 00344: GetFMChirpStopFrequencyMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequencyMaximum(string selectorString, out double value)Remar

### GetFMChirpStopFrequencyMaximum(string, out double)

Gets the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequencyMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequencyMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencymean__string-out.html language=enus -->
## TOPIC 00345: GetFMChirpStopFrequencyMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequencyMean(string selectorString, out double value)Rem

### GetFMChirpStopFrequencyMean(string, out double)

Gets the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequencyMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequencyMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencyminimum__string-out.html language=enus -->
## TOPIC 00346: GetFMChirpStopFrequencyMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencyminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencyminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequencyMinimum(string selectorString, out double value)Remar

### GetFMChirpStopFrequencyMinimum(string, out double)

Gets the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequencyMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequencyMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencystandarddeviation__string-out.html language=enus -->
## TOPIC 00347: GetFMChirpStopFrequencyStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfmchirpstopfrequencystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFMChirpStopFrequencyStandardDeviation(string selectorString,

### GetFMChirpStopFrequencyStandardDeviation(string, out double)

Gets the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFMChirpStopFrequencyStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFMChirpStopFrequencyStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviation__string-ref.html language=enus -->
## TOPIC 00348: GetFrequencyDeviation(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviation__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviation__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak-to-peak frequency deviation for all measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyDeviation(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsFrequencyDeviation attribute.

### GetFrequencyDeviation(string, ref double[])

Gets the peak-to-peak frequency deviation for all measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyDeviation(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFrequencyDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak-to-peak frequency deviation for all measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationmaximum__string-out.html language=enus -->
## TOPIC 00349: GetFrequencyDeviationMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyDeviationMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyDeviatio

### GetFrequencyDeviationMaximum(string, out double)

Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyDeviationMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyDeviationMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationmean__string-out.html language=enus -->
## TOPIC 00350: GetFrequencyDeviationMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyDeviationMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyDeviati

### GetFrequencyDeviationMean(string, out double)

Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyDeviationMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyDeviationMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationminimum__string-out.html language=enus -->
## TOPIC 00351: GetFrequencyDeviationMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyDeviationMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyDevi

### GetFrequencyDeviationMinimum(string, out double)

Gets the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyDeviationMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyDeviationMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationstandarddeviation__string-out.html language=enus -->
## TOPIC 00352: GetFrequencyDeviationStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencydeviationstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyDeviationStandardDeviation(string selectorString, out double value)RemarksThis method gets the value

### GetFrequencyDeviationStandardDeviation(string, out double)

Gets the standard deviation of the peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyDeviationStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyDeviationStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeak__string-ref.html language=enus -->
## TOPIC 00353: GetFrequencyErrorPeak(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeak__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeak__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak frequency error for all measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorPeak(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsFrequencyErrorPeak attribute.ParametersNa

### GetFrequencyErrorPeak(string, ref double[])

Gets the peak frequency error for all measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorPeak(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorPeak](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak frequency error for all measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeaklocation__string-ref.html language=enus -->
## TOPIC 00354: GetFrequencyErrorPeakLocation(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeaklocation__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeaklocation__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorPeakLocation(string selectorString, ref double[] value)RemarksThis method gets the value of Pulse

### GetFrequencyErrorPeakLocation(string, ref double[])

Gets the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorPeakLocation(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorPeakLocation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakmaximum__string-out.html language=enus -->
## TOPIC 00355: GetFrequencyErrorPeakMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorPeakMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyErrorPeakMaximum

### GetFrequencyErrorPeakMaximum(string, out double)

Gets the maximum peak frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorPeakMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorPeakMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakmean__string-out.html language=enus -->
## TOPIC 00356: GetFrequencyErrorPeakMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorPeakMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyErrorPeakMean a

### GetFrequencyErrorPeakMean(string, out double)

Gets the mean of the peak frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorPeakMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorPeakMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakminimum__string-out.html language=enus -->
## TOPIC 00357: GetFrequencyErrorPeakMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorPeakMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyErrorPeakMinimum

### GetFrequencyErrorPeakMinimum(string, out double)

Gets the minimum peak frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorPeakMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorPeakMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakstandarddeviation__string-out.html language=enus -->
## TOPIC 00358: GetFrequencyErrorPeakStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorpeakstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorPeakStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResu

### GetFrequencyErrorPeakStandardDeviation(string, out double)

Gets the standard deviation of the peak frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorPeakStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorPeakStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrms__string-ref.html language=enus -->
## TOPIC 00359: GetFrequencyErrorRms(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrms__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrms__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS frequency error for all measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorRms(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsFrequencyErrorRms attribute.ParametersNameT

### GetFrequencyErrorRms(string, ref double[])

Gets the RMS frequency error for all measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorRms(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorRms](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the RMS frequency error for all measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsmaximum__string-out.html language=enus -->
## TOPIC 00360: GetFrequencyErrorRmsMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum RMS frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorRmsMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyErrorRmsMaximum at

### GetFrequencyErrorRmsMaximum(string, out double)

Gets the maximum RMS frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorRmsMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorRmsMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum RMS frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsmean__string-out.html language=enus -->
## TOPIC 00361: GetFrequencyErrorRmsMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorRmsMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyErrorRmsMean attr

### GetFrequencyErrorRmsMean(string, out double)

Gets the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorRmsMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorRmsMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsminimum__string-out.html language=enus -->
## TOPIC 00362: GetFrequencyErrorRmsMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum RMS frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorRmsMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsFrequencyErrorRmsMinimum at

### GetFrequencyErrorRmsMinimum(string, out double)

Gets the minimum RMS frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorRmsMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorRmsMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum RMS frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsstandarddeviation__string-out.html language=enus -->
## TOPIC 00363: GetFrequencyErrorRmsStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getfrequencyerrorrmsstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyErrorRmsStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResult

### GetFrequencyErrorRmsStandardDeviation(string, out double)

Gets the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyErrorRmsStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsFrequencyErrorRmsStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershoot__string-ref.html language=enus -->
## TOPIC 00364: GetOvershoot(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershoot__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershoot__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the overshoot values computed for all measured pulses. The overshoot value is defined as the ratio of height of the local peak after a rising edge to the pulse amplitude. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDevia

### GetOvershoot(string, ref double[])

Gets the overshoot values computed for all measured pulses. The overshoot value is defined as the ratio of height of the local peak after a rising edge to the pulse amplitude. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetOvershoot(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsOvershoot](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the overshoot values computed for all measured pulses. The overshoot value is defined as the ratio of height of the local peak after a rising edge to the pulse amplitude. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootmaximum__string-out.html language=enus -->
## TOPIC 00365: GetOvershootMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetOvershootMaximum(string

### GetOvershootMaximum(string, out double)

Gets the maximum of overshoot values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetOvershootMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsOvershootMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootmean__string-out.html language=enus -->
## TOPIC 00366: GetOvershootMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetOvershootMean(string se

### GetOvershootMean(string, out double)

Gets the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetOvershootMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsOvershootMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootminimum__string-out.html language=enus -->
## TOPIC 00367: GetOvershootMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetOvershootMinimum(string

### GetOvershootMinimum(string, out double)

Gets the minimum of overshoot values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetOvershootMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsOvershootMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootstandarddeviation__string-out.html language=enus -->
## TOPIC 00368: GetOvershootStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getovershootstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetOvershoot

### GetOvershootStandardDeviation(string, out double)

Gets the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetOvershootStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsOvershootStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevel__string-ref.html language=enus -->
## TOPIC 00369: GetPeakLevel(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevel__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevel__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPeakLevel(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsPeakLevel attribute.Paramet

### GetPeakLevel(string, ref double[])

Gets the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPeakLevel(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPeakLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelmaximum__string-out.html language=enus -->
## TOPIC 00370: GetPeakLevelMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPeakLevelMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPeakLevelMaxi

### GetPeakLevelMaximum(string, out double)

Gets the maximum peak power level during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPeakLevelMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPeakLevelMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelmean__string-out.html language=enus -->
## TOPIC 00371: GetPeakLevelMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPeakLevelMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPeakLevelMe

### GetPeakLevelMean(string, out double)

Gets the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPeakLevelMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPeakLevelMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelminimum__string-out.html language=enus -->
## TOPIC 00372: GetPeakLevelMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPeakLevelMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPeakLevelMini

### GetPeakLevelMinimum(string, out double)

Gets the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPeakLevelMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPeakLevelMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelstandarddeviation__string-out.html language=enus -->
## TOPIC 00373: GetPeakLevelStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpeaklevelstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPeakLevelStandardDeviation(string selectorString, out double value)RemarksThis method gets the value

### GetPeakLevelStandardDeviation(string, out double)

Gets the standard deviation of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPeakLevelStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPeakLevelStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviation__string-ref.html language=enus -->
## TOPIC 00374: GetPhaseDeviation(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviation__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviation__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseDeviation(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsPhaseDeviation attribute.Paramet

### GetPhaseDeviation(string, ref double[])

Gets the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseDeviation(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPhaseDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationmaximum__string-out.html language=enus -->
## TOPIC 00375: GetPhaseDeviationMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseDeviationMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseDeviationMa

### GetPhaseDeviationMaximum(string, out double)

Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseDeviationMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseDeviationMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationmean__string-out.html language=enus -->
## TOPIC 00376: GetPhaseDeviationMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseDeviationMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseDeviationM

### GetPhaseDeviationMean(string, out double)

Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseDeviationMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseDeviationMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationminimum__string-out.html language=enus -->
## TOPIC 00377: GetPhaseDeviationMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseDeviationMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseDeviationMi

### GetPhaseDeviationMinimum(string, out double)

Gets the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseDeviationMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseDeviationMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationstandarddeviation__string-out.html language=enus -->
## TOPIC 00378: GetPhaseDeviationStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasedeviationstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseDeviationStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of

### GetPhaseDeviationStandardDeviation(string, out double)

Gets the standard deviation of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseDeviationStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseDeviationStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeak__string-ref.html language=enus -->
## TOPIC 00379: GetPhaseErrorPeak(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeak__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeak__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak phase error for all measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorPeak(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsPhaseErrorPeak attribute.ParametersNameTypeD

### GetPhaseErrorPeak(string, ref double[])

Gets the peak phase error for all measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorPeak(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorPeak](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak phase error for all measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeaklocation__string-ref.html language=enus -->
## TOPIC 00380: GetPhaseErrorPeakLocation(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeaklocation__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeaklocation__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorPeakLocation(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResults

### GetPhaseErrorPeakLocation(string, ref double[])

Gets the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorPeakLocation(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorPeakLocation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakmaximum__string-out.html language=enus -->
## TOPIC 00381: GetPhaseErrorPeakMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorPeakMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseErrorPeakMaximum attrib

### GetPhaseErrorPeakMaximum(string, out double)

Gets the maximum peak phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorPeakMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorPeakMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakmean__string-out.html language=enus -->
## TOPIC 00382: GetPhaseErrorPeakMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorPeakMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseErrorPeakMean attribut

### GetPhaseErrorPeakMean(string, out double)

Gets the mean of the peak phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorPeakMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorPeakMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakminimum__string-out.html language=enus -->
## TOPIC 00383: GetPhaseErrorPeakMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorPeakMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseErrorPeakMinimum attrib

### GetPhaseErrorPeakMinimum(string, out double)

Gets the minimum peak phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorPeakMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorPeakMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakstandarddeviation__string-out.html language=enus -->
## TOPIC 00384: GetPhaseErrorPeakStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorpeakstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorPeakStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResults

### GetPhaseErrorPeakStandardDeviation(string, out double)

Gets the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorPeakStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorPeakStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrms__string-ref.html language=enus -->
## TOPIC 00385: GetPhaseErrorRms(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrms__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrms__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS phase error for all measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorRms(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsPhaseErrorRms attribute.ParametersNameTypeDesc

### GetPhaseErrorRms(string, ref double[])

Gets the RMS phase error for all measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorRms(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorRms](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the RMS phase error for all measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsmaximum__string-out.html language=enus -->
## TOPIC 00386: GetPhaseErrorRmsMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum RMS phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorRmsMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseErrorRmsMaximum attribute

### GetPhaseErrorRmsMaximum(string, out double)

Gets the maximum RMS phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorRmsMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorRmsMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum RMS phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsmean__string-out.html language=enus -->
## TOPIC 00387: GetPhaseErrorRmsMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorRmsMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseErrorRmsMean attribute.P

### GetPhaseErrorRmsMean(string, out double)

Gets the mean of the RMS phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorRmsMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorRmsMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the RMS phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsminimum__string-out.html language=enus -->
## TOPIC 00388: GetPhaseErrorRmsMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum RMS phase error across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorRmsMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseErrorRmsMinimum attribute

### GetPhaseErrorRmsMinimum(string, out double)

Gets the minimum RMS phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorRmsMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorRmsMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum RMS phase error across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsstandarddeviation__string-out.html language=enus -->
## TOPIC 00389: GetPhaseErrorRmsStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphaseerrorrmsstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the RMS phase errors across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseErrorRmsStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsP

### GetPhaseErrorRmsStandardDeviation(string, out double)

Gets the standard deviation of the RMS phase errors across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseErrorRmsStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseErrorRmsStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the RMS phase errors across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestability__string-ref.html language=enus -->
## TOPIC 00390: GetPhaseStability(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestability__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestability__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the phase stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of phase from the reference. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseStability(string selectorString, ref double[] value)RemarksThis method gets the valu

### GetPhaseStability(string, ref double[])

Gets the phase stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of phase from the reference.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseStability(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPhaseStability](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the phase stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of phase from the reference. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitymaximum__string-out.html language=enus -->
## TOPIC 00391: GetPhaseStabilityMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum phase stability across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseStabilityMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseStabilityMaximum attribute.Pa

### GetPhaseStabilityMaximum(string, out double)

Gets the maximum phase stability across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseStabilityMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseStabilityMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum phase stability across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitymean__string-out.html language=enus -->
## TOPIC 00392: GetPhaseStabilityMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the phase stability values across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseStabilityMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseStabilityMean attribu

### GetPhaseStabilityMean(string, out double)

Gets the mean of the phase stability values across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseStabilityMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseStabilityMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the phase stability values across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilityminimum__string-out.html language=enus -->
## TOPIC 00393: GetPhaseStabilityMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilityminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilityminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum phase stability across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseStabilityMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseStabilityMinimum attribute.Pa

### GetPhaseStabilityMinimum(string, out double)

Gets the minimum phase stability across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseStabilityMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseStabilityMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum phase stability across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitystandarddeviation__string-out.html language=enus -->
## TOPIC 00394: GetPhaseStabilityStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getphasestabilitystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the phase stability standard deviation across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPhaseStabilityStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPhaseStabilit

### GetPhaseStabilityStandardDeviation(string, out double)

Gets the phase stability standard deviation across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPhaseStabilityStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPhaseStabilityStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the phase stability standard deviation across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsecount__string-out.html language=enus -->
## TOPIC 00395: GetPulseCount(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsecount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsecount__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measured pulse count. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseCount(string selectorString, out int value)RemarksThis method gets the value of PulseResultsPulseCount attribute.ParametersNameTypeDescriptionselectorStringstringSpecifies the result name. Example: ""

### GetPulseCount(string, out int)

Gets the measured pulse count.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseCount(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseResultsPulseCount](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the measured pulse count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffduration__string-ref.html language=enus -->
## TOPIC 00396: GetPulseOffDuration(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffduration__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffduration__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseOffDu

### GetPulseOffDuration(string, ref double[])

Gets the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseOffDuration(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPulseOffDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationmaximum__string-out.html language=enus -->
## TOPIC 00397: GetPulseOffDurationMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum OFF duration across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseOffDurationMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseOffDurationMaximum attrib

### GetPulseOffDurationMaximum(string, out double)

Gets the maximum OFF duration across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseOffDurationMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseOffDurationMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum OFF duration across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationmean__string-out.html language=enus -->
## TOPIC 00398: GetPulseOffDurationMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the OFF duration values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseOffDurationMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseOffDurationMean a

### GetPulseOffDurationMean(string, out double)

Gets the mean of the OFF duration values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseOffDurationMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseOffDurationMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the OFF duration values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationminimum__string-out.html language=enus -->
## TOPIC 00399: GetPulseOffDurationMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum OFF duration across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseOffDurationMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseOffDurationMinimum attrib

### GetPulseOffDurationMinimum(string, out double)

Gets the minimum OFF duration across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseOffDurationMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseOffDurationMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum OFF duration across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationstandarddeviation__string-out.html language=enus -->
## TOPIC 00400: GetPulseOffDurationStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulseoffdurationstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseOffDurationStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResult

### GetPulseOffDurationStandardDeviation(string, out double)

Gets the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseOffDurationStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseOffDurationStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsepositionindex__string-ref.html language=enus -->
## TOPIC 00401: GetPulsePositionIndex(string, ref int[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsepositionindex__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsepositionindex__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the position indices of all the measured pulses within a burst. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulsePositionIndex(string selectorString, ref int[] value)RemarksThis method gets the value of PulseResultsPulsePositionIndex attribute.ParametersNameTypeDescriptionsel

### GetPulsePositionIndex(string, ref int[])

Gets the position indices of all the measured pulses within a burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulsePositionIndex(string selectorString, ref int[] value)

#### Remarks

This method gets the value of [PulseResultsPulsePositionIndex](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref int[] | Upon return, contains the position indices of all the measured pulses within a burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitioninterval__string-ref.html language=enus -->
## TOPIC 00402: GetPulseRepetitionInterval(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitioninterval__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitioninterval__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds. SyntaxNamespace: Nati

### GetPulseRepetitionInterval(string, ref double[])

Gets the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseRepetitionInterval(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPulseRepetitionInterval](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalmaximum__string-out.html language=enus -->
## TOPIC 00403: GetPulseRepetitionIntervalMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum pulse period across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseRepetitionIntervalMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseRepetitionInterval

### GetPulseRepetitionIntervalMaximum(string, out double)

Gets the maximum pulse period across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseRepetitionIntervalMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseRepetitionIntervalMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum pulse period across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalmean__string-out.html language=enus -->
## TOPIC 00404: GetPulseRepetitionIntervalMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of pulse period values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseRepetitionIntervalMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseRepetitionInte

### GetPulseRepetitionIntervalMean(string, out double)

Gets the mean of pulse period values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseRepetitionIntervalMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseRepetitionIntervalMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of pulse period values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalminimum__string-out.html language=enus -->
## TOPIC 00405: GetPulseRepetitionIntervalMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum pulse period across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseRepetitionIntervalMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseRepetitionInterval

### GetPulseRepetitionIntervalMinimum(string, out double)

Gets the minimum pulse period across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseRepetitionIntervalMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseRepetitionIntervalMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum pulse period across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalstandarddeviation__string-out.html language=enus -->
## TOPIC 00406: GetPulseRepetitionIntervalStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulserepetitionintervalstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseRepetitionIntervalStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of Puls

### GetPulseRepetitionIntervalStandardDeviation(string, out double)

Gets the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseRepetitionIntervalStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseRepetitionIntervalStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifference__string-ref.html language=enus -->
## TOPIC 00407: GetPulseToPulseFrequencyDifference(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifference__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifference__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulseFrequencyDifference(string selectorString, ref double[] value)RemarksThis method gets the value of P

### GetPulseToPulseFrequencyDifference(string, ref double[])

Gets the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulseFrequencyDifference(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulseFrequencyDifference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencemaximum__string-out.html language=enus -->
## TOPIC 00408: GetPulseToPulseFrequencyDifferenceMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulseFrequencyDifferenceMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResu

### GetPulseToPulseFrequencyDifferenceMaximum(string, out double)

Gets the maximum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulseFrequencyDifferenceMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulseFrequencyDifferenceMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencemean__string-out.html language=enus -->
## TOPIC 00409: GetPulseToPulseFrequencyDifferenceMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulseFrequencyDifferenceMean(string selectorString, out double value)RemarksThis method gets the value of PulseRes

### GetPulseToPulseFrequencyDifferenceMean(string, out double)

Gets the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulseFrequencyDifferenceMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulseFrequencyDifferenceMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferenceminimum__string-out.html language=enus -->
## TOPIC 00410: GetPulseToPulseFrequencyDifferenceMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferenceminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferenceminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulseFrequencyDifferenceMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResu

### GetPulseToPulseFrequencyDifferenceMinimum(string, out double)

Gets the minimum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulseFrequencyDifferenceMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulseFrequencyDifferenceMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencestandarddeviation__string-out.html language=enus -->
## TOPIC 00411: GetPulseToPulseFrequencyDifferenceStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsefrequencydifferencestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulseFrequencyDifferenceStandardDeviation(string selectorString, out double value)RemarksThis method

### GetPulseToPulseFrequencyDifferenceStandardDeviation(string, out double)

Gets the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulseFrequencyDifferenceStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulseFrequencyDifferenceStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifference__string-ref.html language=enus -->
## TOPIC 00412: GetPulseToPulsePhaseDifference(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifference__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifference__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulsePhaseDifference(string selectorString, ref double[] value)RemarksThis method gets the value of PulseRes

### GetPulseToPulsePhaseDifference(string, ref double[])

Gets the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulsePhaseDifference(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulsePhaseDifference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencemaximum__string-out.html language=enus -->
## TOPIC 00413: GetPulseToPulsePhaseDifferenceMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulsePhaseDifferenceMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResults

### GetPulseToPulsePhaseDifferenceMaximum(string, out double)

Gets the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulsePhaseDifferenceMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulsePhaseDifferenceMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencemean__string-out.html language=enus -->
## TOPIC 00414: GetPulseToPulsePhaseDifferenceMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulsePhaseDifferenceMean(string selectorString, out double value)RemarksThis method gets the value of PulseResult

### GetPulseToPulsePhaseDifferenceMean(string, out double)

Gets the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulsePhaseDifferenceMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulsePhaseDifferenceMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferenceminimum__string-out.html language=enus -->
## TOPIC 00415: GetPulseToPulsePhaseDifferenceMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferenceminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferenceminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulsePhaseDifferenceMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResults

### GetPulseToPulsePhaseDifferenceMinimum(string, out double)

Gets the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulsePhaseDifferenceMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulsePhaseDifferenceMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencestandarddeviation__string-out.html language=enus -->
## TOPIC 00416: GetPulseToPulsePhaseDifferenceStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsetopulsephasedifferencestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseToPulsePhaseDifferenceStandardDeviation(string selectorString, out double value)RemarksThis method ge

### GetPulseToPulsePhaseDifferenceStandardDeviation(string, out double)

Gets the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseToPulsePhaseDifferenceStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseToPulsePhaseDifferenceStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidth__string-ref.html language=enus -->
## TOPIC 00417: GetPulseWidth(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidth__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidth__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseWidth(string s

### GetPulseWidth(string, ref double[])

Gets the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseWidth(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsPulseWidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthmaximum__string-out.html language=enus -->
## TOPIC 00418: GetPulseWidthMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum ON duration across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseWidthMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseWidthMaximum attribute.Parameter

### GetPulseWidthMaximum(string, out double)

Gets the maximum ON duration across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseWidthMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseWidthMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum ON duration across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthmean__string-out.html language=enus -->
## TOPIC 00419: GetPulseWidthMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the ON duration values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseWidthMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseWidthMean attribute.Para

### GetPulseWidthMean(string, out double)

Gets the mean of the ON duration values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseWidthMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseWidthMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the ON duration values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthminimum__string-out.html language=enus -->
## TOPIC 00420: GetPulseWidthMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum ON duration across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseWidthMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseWidthMinimum attribute.Parameter

### GetPulseWidthMinimum(string, out double)

Gets the minimum ON duration across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseWidthMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseWidthMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum ON duration across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthstandarddeviation__string-out.html language=enus -->
## TOPIC 00421: GetPulseWidthStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getpulsewidthstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetPulseWidthStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsPulseW

### GetPulseWidthStandardDeviation(string, out double)

Gets the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetPulseWidthStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsPulseWidthStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripple__string-ref.html language=enus -->
## TOPIC 00422: GetRipple(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripple__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripple__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) meth

### GetRipple(string, ref double[])

Gets the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRipple(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsRipple](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplemaximum__string-out.html language=enus -->
## TOPIC 00423: GetRippleMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRippleMaximum(string select

### GetRippleMaximum(string, out double)

Gets the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRippleMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRippleMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplemean__string-out.html language=enus -->
## TOPIC 00424: GetRippleMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRippleMean(string selector

### GetRippleMean(string, out double)

Gets the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRippleMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRippleMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrippleminimum__string-out.html language=enus -->
## TOPIC 00425: GetRippleMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrippleminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrippleminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRippleMinimum(string select

### GetRippleMinimum(string, out double)

Gets the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRippleMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRippleMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplestandarddeviation__string-out.html language=enus -->
## TOPIC 00426: GetRippleStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getripplestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRippleStanda

### GetRippleStandardDeviation(string, out double)

Gets the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by [SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRippleStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRippleStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getriseedge__string-ref.html language=enus -->
## TOPIC 00427: GetRiseEdge(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getriseedge__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getriseedge__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRiseEdge(string selectorString, ref double[] value)RemarksThis

### GetRiseEdge(string, ref double[])

Gets the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRiseEdge(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsRiseEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetime__string-ref.html language=enus -->
## TOPIC 00428: GetRiseTime(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetime__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetime__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRiseTime(string selectorString, ref double[] value)Remark

### GetRiseTime(string, ref double[])

Gets the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRiseTime(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsRiseTime](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimemaximum__string-out.html language=enus -->
## TOPIC 00429: GetRiseTimeMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimemaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimemaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum rise time across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRiseTimeMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsRiseTimeMaximum attribute.ParametersNameT

### GetRiseTimeMaximum(string, out double)

Gets the maximum rise time across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRiseTimeMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRiseTimeMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum rise time across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimemean__string-out.html language=enus -->
## TOPIC 00430: GetRiseTimeMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimemean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the rise time values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRiseTimeMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsRiseTimeMean attribute.Parameters

### GetRiseTimeMean(string, out double)

Gets the mean of the rise time values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRiseTimeMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRiseTimeMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the rise time values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimeminimum__string-out.html language=enus -->
## TOPIC 00431: GetRiseTimeMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimeminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimeminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum rise time across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRiseTimeMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsRiseTimeMinimum attribute.ParametersNameT

### GetRiseTimeMinimum(string, out double)

Gets the minimum rise time across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRiseTimeMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRiseTimeMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum rise time across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimestandarddeviation__string-out.html language=enus -->
## TOPIC 00432: GetRiseTimeStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimestandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-getrisetimestandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetRiseTimeStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsRiseTi

### GetRiseTimeStandardDeviation(string, out double)

Gets the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetRiseTimeStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsRiseTimeStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratio__string-ref.html language=enus -->
## TOPIC 00433: GetTimeSidelobeCompressionRatio(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratio__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratio__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeCompressionRatio(string selectorString, ref double[] value)

### GetTimeSidelobeCompressionRatio(string, ref double[])

Gets the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeCompressionRatio(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeCompressionRatio](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiomaximum__string-out.html language=enus -->
## TOPIC 00434: GetTimeSidelobeCompressionRatioMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiomaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiomaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum compression ratio across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeCompressionRatioMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSide

### GetTimeSidelobeCompressionRatioMaximum(string, out double)

Gets the maximum compression ratio across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeCompressionRatioMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeCompressionRatioMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum compression ratio across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiomean__string-out.html language=enus -->
## TOPIC 00435: GetTimeSidelobeCompressionRatioMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiomean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiomean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeCompressionRatioMean(string selectorString, out double value)RemarksThis method gets the value of PulseResults

### GetTimeSidelobeCompressionRatioMean(string, out double)

Gets the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeCompressionRatioMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeCompressionRatioMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiominimum__string-out.html language=enus -->
## TOPIC 00436: GetTimeSidelobeCompressionRatioMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiominimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiominimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum compression ratio across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeCompressionRatioMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSide

### GetTimeSidelobeCompressionRatioMinimum(string, out double)

Gets the minimum compression ratio across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeCompressionRatioMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeCompressionRatioMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum compression ratio across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiostandarddeviation__string-out.html language=enus -->
## TOPIC 00437: GetTimeSidelobeCompressionRatioStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiostandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobecompressionratiostandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeCompressionRatioStandardDeviation(string selectorString, out double value)RemarksThis method get

### GetTimeSidelobeCompressionRatioStandardDeviation(string, out double)

Gets the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeCompressionRatioStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeCompressionRatioStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelay__string-ref.html language=enus -->
## TOPIC 00438: GetTimeSidelobeDelay(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelay__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelay__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeDelay(string selectorString, ref double[] valu

### GetTimeSidelobeDelay(string, ref double[])

Gets the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeDelay(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeDelay](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaymaximum__string-out.html language=enus -->
## TOPIC 00439: GetTimeSidelobeDelayMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeDelayMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobeDelayMaximum at

### GetTimeSidelobeDelayMaximum(string, out double)

Gets the maximum sidelobe delay across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeDelayMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeDelayMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaymean__string-out.html language=enus -->
## TOPIC 00440: GetTimeSidelobeDelayMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeDelayMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobeDelayMe

### GetTimeSidelobeDelayMean(string, out double)

Gets the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeDelayMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeDelayMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelayminimum__string-out.html language=enus -->
## TOPIC 00441: GetTimeSidelobeDelayMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelayminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelayminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeDelayMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobeDelayMinimum at

### GetTimeSidelobeDelayMinimum(string, out double)

Gets the minimum sidelobe delay across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeDelayMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeDelayMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaystandarddeviation__string-out.html language=enus -->
## TOPIC 00442: GetTimeSidelobeDelayStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobedelaystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeDelayStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of Puls

### GetTimeSidelobeDelayStandardDeviation(string, out double)

Gets the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeDelayStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeDelayStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidth__string-ref.html language=enus -->
## TOPIC 00443: GetTimeSidelobeMainlobeWidth(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidth__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidth__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeMainlobeWidth(string selectorString, ref double[] value)RemarksThis method get

### GetTimeSidelobeMainlobeWidth(string, ref double[])

Gets the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeMainlobeWidth(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeMainlobeWidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthmaximum__string-out.html language=enus -->
## TOPIC 00444: GetTimeSidelobeMainlobeWidthMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum mainlobe width across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeMainlobeWidthMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobeMainlob

### GetTimeSidelobeMainlobeWidthMaximum(string, out double)

Gets the maximum mainlobe width across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeMainlobeWidthMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeMainlobeWidthMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum mainlobe width across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthmean__string-out.html language=enus -->
## TOPIC 00445: GetTimeSidelobeMainlobeWidthMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeMainlobeWidthMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelob

### GetTimeSidelobeMainlobeWidthMean(string, out double)

Gets the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeMainlobeWidthMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeMainlobeWidthMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthminimum__string-out.html language=enus -->
## TOPIC 00446: GetTimeSidelobeMainlobeWidthMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum mainlobe width across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeMainlobeWidthMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobeMainlob

### GetTimeSidelobeMainlobeWidthMinimum(string, out double)

Gets the minimum mainlobe width across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeMainlobeWidthMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeMainlobeWidthMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum mainlobe width across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthstandarddeviation__string-out.html language=enus -->
## TOPIC 00447: GetTimeSidelobeMainlobeWidthStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobemainlobewidthstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeMainlobeWidthStandardDeviation(string selectorString, out double value)RemarksThis method gets the value

### GetTimeSidelobeMainlobeWidthStandardDeviation(string, out double)

Gets the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeMainlobeWidthStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobeMainlobeWidthStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelation__string-ref.html language=enus -->
## TOPIC 00448: GetTimeSidelobePeakCorrelation(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelation__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelation__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakCorrelation(stri

### GetTimeSidelobePeakCorrelation(string, ref double[])

Gets the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakCorrelation(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakCorrelation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationmaximum__string-out.html language=enus -->
## TOPIC 00449: GetTimeSidelobePeakCorrelationMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak correlation across the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakCorrelationMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobePeakCorrelationMaximum attribute.Parame

### GetTimeSidelobePeakCorrelationMaximum(string, out double)

Gets the maximum peak correlation across the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakCorrelationMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakCorrelationMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak correlation across the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationmean__string-out.html language=enus -->
## TOPIC 00450: GetTimeSidelobePeakCorrelationMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak correlation values across the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakCorrelationMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobePeakCorrelationMean attribute.P

### GetTimeSidelobePeakCorrelationMean(string, out double)

Gets the mean of the peak correlation values across the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakCorrelationMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakCorrelationMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak correlation values across the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationminimum__string-out.html language=enus -->
## TOPIC 00451: GetTimeSidelobePeakCorrelationMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak correlation across the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakCorrelationMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobePeakCorrelationMinimum attribute.Parame

### GetTimeSidelobePeakCorrelationMinimum(string, out double)

Gets the minimum peak correlation across the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakCorrelationMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakCorrelationMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak correlation across the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationstandarddeviation__string-out.html language=enus -->
## TOPIC 00452: GetTimeSidelobePeakCorrelationStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeakcorrelationstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak correlation values across the measured pulses. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakCorrelationStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobePeak

### GetTimeSidelobePeakCorrelationStandardDeviation(string, out double)

Gets the standard deviation of the peak correlation values across the measured pulses.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakCorrelationStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakCorrelationStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak correlation values across the measured pulses. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevel__string-ref.html language=enus -->
## TOPIC 00453: GetTimeSidelobePeakSidelobeLevel(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevel__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevel__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakSidelobeLevel(string selectorString, ref doubl

### GetTimeSidelobePeakSidelobeLevel(string, ref double[])

Gets the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakSidelobeLevel(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakSidelobeLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelmaximum__string-out.html language=enus -->
## TOPIC 00454: GetTimeSidelobePeakSidelobeLevelMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakSidelobeLevelMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelo

### GetTimeSidelobePeakSidelobeLevelMaximum(string, out double)

Gets the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakSidelobeLevelMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakSidelobeLevelMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelmean__string-out.html language=enus -->
## TOPIC 00455: GetTimeSidelobePeakSidelobeLevelMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakSidelobeLevelMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSid

### GetTimeSidelobePeakSidelobeLevelMean(string, out double)

Gets the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakSidelobeLevelMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakSidelobeLevelMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelminimum__string-out.html language=enus -->
## TOPIC 00456: GetTimeSidelobePeakSidelobeLevelMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakSidelobeLevelMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTimeSidelobePea

### GetTimeSidelobePeakSidelobeLevelMinimum(string, out double)

Gets the minimum peak sidelobe level across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakSidelobeLevelMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakSidelobeLevelMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelstandarddeviation__string-out.html language=enus -->
## TOPIC 00457: GetTimeSidelobePeakSidelobeLevelStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettimesidelobepeaksidelobelevelstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobePeakSidelobeLevelStandardDeviation(string selectorString, out double value)RemarksThis method gets the v

### GetTimeSidelobePeakSidelobeLevelStandardDeviation(string, out double)

Gets the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobePeakSidelobeLevelStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTimeSidelobePeakSidelobeLevelStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevel__string-ref.html language=enus -->
## TOPIC 00458: GetTopLevel(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevel__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevel__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the top levels for all measured pulses. The values are expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTopLevel(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsTopLevel attribute.ParametersNameTypeDescriptionselectorStr

### GetTopLevel(string, ref double[])

Gets the top levels for all measured pulses. The values are expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTopLevel(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTopLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the top levels for all measured pulses. The values are expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelmaximum__string-out.html language=enus -->
## TOPIC 00459: GetTopLevelMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelmaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum top level across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTopLevelMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTopLevelMaximum attribute.ParametersNameTypeD

### GetTopLevelMaximum(string, out double)

Gets the maximum top level across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTopLevelMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTopLevelMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum top level across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelmean__string-out.html language=enus -->
## TOPIC 00460: GetTopLevelMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelmean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the top levels across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTopLevelMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTopLevelMean attribute.ParametersNameTypeDe

### GetTopLevelMean(string, out double)

Gets the mean of the top levels across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTopLevelMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTopLevelMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the top levels across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelminimum__string-out.html language=enus -->
## TOPIC 00461: GetTopLevelMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum top level across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTopLevelMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTopLevelMinimum attribute.ParametersNameTypeD

### GetTopLevelMinimum(string, out double)

Gets the minimum top level across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTopLevelMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTopLevelMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum top level across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelstandarddeviation__string-out.html language=enus -->
## TOPIC 00462: GetTopLevelStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettoplevelstandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the standard deviation of the top levels across the measured pulses. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTopLevelStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTopLevelStandard

### GetTopLevelStandardDeviation(string, out double)

Gets the standard deviation of the top levels across the measured pulses. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTopLevelStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTopLevelStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the standard deviation of the top levels across the measured pulses. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstability__string-ref.html language=enus -->
## TOPIC 00463: GetTotalStability(string, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstability__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstability__string-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total stability of the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTotalStability(string selectorString, ref double[] value)RemarksThis method gets the value of PulseResultsTotalStability attribute.ParametersNameTypeDescript

### GetTotalStability(string, ref double[])

Gets the total stability of the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTotalStability(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [PulseResultsTotalStability](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | ref double[] | Upon return, contains the total stability of the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitymaximum__string-out.html language=enus -->
## TOPIC 00464: GetTotalStabilityMaximum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitymaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitymaximum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum total stability across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTotalStabilityMaximum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTotalStabilityMaximum attribute.Pa

### GetTotalStabilityMaximum(string, out double)

Gets the maximum total stability across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTotalStabilityMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTotalStabilityMaximum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum total stability across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitymean__string-out.html language=enus -->
## TOPIC 00465: GetTotalStabilityMean(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitymean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitymean__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the total stability values across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTotalStabilityMean(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTotalStabilityMean attribu

### GetTotalStabilityMean(string, out double)

Gets the mean of the total stability values across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTotalStabilityMean(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTotalStabilityMean](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the total stability values across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilityminimum__string-out.html language=enus -->
## TOPIC 00466: GetTotalStabilityMinimum(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilityminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilityminimum__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum total stability across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTotalStabilityMinimum(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTotalStabilityMinimum attribute.Pa

### GetTotalStabilityMinimum(string, out double)

Gets the minimum total stability across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTotalStabilityMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTotalStabilityMinimum](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the minimum total stability across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitystandarddeviation__string-out.html language=enus -->
## TOPIC 00467: GetTotalStabilityStandardDeviation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitystandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults-gettotalstabilitystandarddeviation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total stability standard deviation across the measured pulses. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTotalStabilityStandardDeviation(string selectorString, out double value)RemarksThis method gets the value of PulseResultsTotalStabilit

### GetTotalStabilityStandardDeviation(string, out double)

Gets the total stability standard deviation across the measured pulses. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTotalStabilityStandardDeviation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseResultsTotalStabilityStandardDeviation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the total stability standard deviation across the measured pulses. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseResults Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults.html language=enus -->
## TOPIC 00468: RFmxPulseMXPulseResults Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the Pulse measurement results. Derives fromRFmxPulseMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic class RFmxPulseMXPulseResults : RFmxPulseMXSubObjectMethodsNameDescriptionFetchAcquiredAmplitudeTrace(string, double, out double, ref float[], ref

### RFmxPulseMXPulseResults Class

Provides methods to fetch and read the Pulse measurement results.

#### Derives from

- RFmxPulseMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public class RFmxPulseMXPulseResults : RFmxPulseMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchAcquiredAmplitudeTrace(string, double, out double, ref float[], ref int[], ref double[]) | Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the PulseAcquisitionTraceSelect method to select all pulses or the subset of acquired pulses. When you set the SegmentedAcquisitionEnabled method to False, returns a single element in the Start Indices and Start Time Stamp array. |
| FetchAmplitudeTrace(string, double, ref AnalogWaveform< float >) | Fetches the amplitude trace of the selected pulse. |
| FetchBurstIntrapulseStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points.(br/) |
| FetchBurstSelectedPositionStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the burst stability trace of the selected position. |
| FetchFrequencyTrace(string, double, ref AnalogWaveform< float >) | Fetches the frequency trace of the selected pulse. |
| FetchIntrapulseStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position.(br/) |
| FetchIQTrace(string, double, ref ComplexWaveform< ComplexSingle >) | Fetches the IQ trace of the selected pulse. |
| FetchMultipleMeasurementPointsStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the multiple measurement points stability trace. |
| FetchPhaseWrappedTrace(string, double, ref AnalogWaveform< float >) | Fetches the wrapped phase trace of the selected pulse. |
| FetchPulseToPulseStabilityTrace(string, double, ref int[], ref double[], ref double[], ref double[]) | Fetches the pulse to pulse stability trace. |
| FetchStabilityTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the stability trace of the selected pulse. |
| FetchTimeSidelobeTrace(string, double, ref AnalogWaveform< float >) | Fetches the time sidelobe trace for the selected pulse. |
| GetAmplitudeStability(string, ref double[]) | Gets the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference. |
| GetAmplitudeStabilityMaximum(string, out double) | Gets the maximum amplitude stability across the measured pulses. This value is expressed in dB. |
| GetAmplitudeStabilityMean(string, out double) | Gets the mean of the amplitude stability values across the measured pulses. This value is expressed in dB. |
| GetAmplitudeStabilityMinimum(string, out double) | Gets the minimum amplitude stability across the measured pulses. This value is expressed in dB. |
| GetAmplitudeStabilityStandardDeviation(string, out double) | Gets the amplitude stability standard deviation across the measured pulses. This value is expressed in dB. |
| GetAverageAmplitudeStability(string, out double) | Gets the average amplitude stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the amplitude over the measured pulses. |
| GetAverageFrequency(string, ref double[]) | Gets the average frequencie for all measured pulses. This value is expressed in Hz. |
| GetAverageFrequencyMaximum(string, out double) | Gets the maximum average frequency across the measured pulses. This value is expressed in Hz. |
| GetAverageFrequencyMean(string, out double) | Gets the mean of the average frequency across the measured pulses. This value is expressed in Hz. |
| GetAverageFrequencyMinimum(string, out double) | Gets the minimum average frequency across the measured pulses. This value is expressed in Hz. |
| GetAverageFrequencyStandardDeviation(string, out double) | Gets the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz. |
| GetAverageLevel(string, ref double[]) | Gets the average power levels during the pulse period for all measured pulses. The values are expressed in dBm. |
| GetAverageLevelMaximum(string, out double) | Gets the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetAverageLevelMean(string, out double) | Gets the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetAverageLevelMinimum(string, out double) | Gets the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetAverageLevelStandardDeviation(string, out double) | Gets the standard deviation of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetAverageOnLevel(string, ref double[]) | Gets the average power levels during the ON duration for all measured pulses. The values are expressed in dBm. |
| GetAverageOnLevelMaximum(string, out double) | Gets the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm. |
| GetAverageOnLevelMean(string, out double) | Gets the mean of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. |
| GetAverageOnLevelMinimum(string, out double) | Gets the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm. |
| GetAverageOnLevelStandardDeviation(string, out double) | Gets the standard deviation of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. |
| GetAveragePhase(string, ref double[]) | Gets the average phase for all measured pulses. This value is expressed in degrees. |
| GetAveragePhaseMaximum(string, out double) | Gets the maximum average phase across the measured pulses. This value is expressed in degrees. |
| GetAveragePhaseMean(string, out double) | Gets the mean of the average phase across the measured pulses. This value is expressed in degrees. |
| GetAveragePhaseMinimum(string, out double) | Gets the minimum average phase across the measured pulses. This value is expressed in degrees. |
| GetAveragePhaseStability(string, out double) | Gets the average phase stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the phase over the measured pulses. |
| GetAveragePhaseStandardDeviation(string, out double) | Gets the standard deviation of the average phase across the measured pulses. This value is expressed in degrees. |
| GetAverageTotalStability(string, out double) | Gets the average total stability over measured pulses. This value is expressed in dB. |
| GetBaseLevel(string, ref double[]) | Gets the base levels for all measured pulses. The values are expressed in dBm. |
| GetBaseLevelMaximum(string, out double) | Gets the maximum base level across the measured pulses. This value is expressed in dBm. |
| GetBaseLevelMean(string, out double) | Gets the mean of the base levels across the measured pulses. This value is expressed in dBm. |
| GetBaseLevelMinimum(string, out double) | Gets the minimum base level across the measured pulses. This value is expressed in dBm. |
| GetBaseLevelStandardDeviation(string, out double) | Gets the standard deviation of the base levels across the measured pulses. This value is expressed in dBm. |
| GetBurstIndex(string, ref int[]) | Gets the burst indices of all the measured pulses. |
| GetDroop(string, ref double[]) | Gets the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetDroopMaximum(string, out double) | Gets the maximum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetDroopMean(string, out double) | Gets the mean of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetDroopMinimum(string, out double) | Gets the minimum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetDroopStandardDeviation(string, out double) | Gets the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetDutyCycle(string, ref double[]) | Gets the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. |
| GetDutyCycleMaximum(string, out double) | Gets the maximum duty cycle across the measured pulses. This value is expressed as a percentage. |
| GetDutyCycleMean(string, out double) | Gets the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. |
| GetDutyCycleMinimum(string, out double) | Gets the minimum duty cycle across the measured pulses. This value is expressed as a percentage. |
| GetDutyCycleStandardDeviation(string, out double) | Gets the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage. |
| GetFallEdge(string, ref double[]) | Gets the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. |
| GetFallTime(string, ref double[]) | Gets the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. |
| GetFallTimeMaximum(string, out double) | Gets the maximum fall time across the measured pulses. This value is expressed in seconds. |
| GetFallTimeMean(string, out double) | Gets the mean of the fall time values across the measured pulses. This value is expressed in seconds. |
| GetFallTimeMinimum(string, out double) | Gets the minimum fall time across the measured pulses. This value is expressed in seconds. |
| GetFallTimeStandardDeviation(string, out double) | Gets the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds. |
| GetFMChirpRate(string, ref double[]) | Gets the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for each pulse. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpRate2(string, ref double[]) | Gets the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| GetFMChirpRate2Maximum(string, out double) | Gets the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| GetFMChirpRate2Mean(string, out double) | Gets the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| GetFMChirpRate2Minimum(string, out double) | Gets the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| GetFMChirpRate2StandardDeviation(string, out double) | Gets the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| GetFMChirpRateMaximum(string, out double) | Gets the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpRateMean(string, out double) | Gets the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpRateMinimum(string, out double) | Gets the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpRateStandardDeviation(string, out double) | Gets the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStartFrequency(string, ref double[]) | Gets the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStartFrequency2(string, ref double[]) | Gets the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStartFrequency2Maximum(string, out double) | Gets the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStartFrequency2Mean(string, out double) | Gets the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStartFrequency2Minimum(string, out double) | Gets the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStartFrequency2StandardDeviation(string, out double) | Gets the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStartFrequencyMaximum(string, out double) | Gets the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStartFrequencyMean(string, out double) | Gets the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStartFrequencyMinimum(string, out double) | Gets the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStartFrequencyStandardDeviation(string, out double) | Gets the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStopFrequency(string, ref double[]) | Gets the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStopFrequency2(string, ref double[]) | Gets the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStopFrequency2Maximum(string, out double) | Gets the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStopFrequency2Mean(string, out double) | Gets the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStopFrequency2Minimum(string, out double) | Gets the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStopFrequency2StandardDeviation(string, out double) | Gets the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| GetFMChirpStopFrequencyMaximum(string, out double) | Gets the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStopFrequencyMean(string, out double) | Gets the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStopFrequencyMinimum(string, out double) | Gets the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFMChirpStopFrequencyStandardDeviation(string, out double) | Gets the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| GetFrequencyDeviation(string, ref double[]) | Gets the peak-to-peak frequency deviation for all measured pulses. This value is expressed in Hz. |
| GetFrequencyDeviationMaximum(string, out double) | Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. |
| GetFrequencyDeviationMean(string, out double) | Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. |
| GetFrequencyDeviationMinimum(string, out double) | Gets the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. |
| GetFrequencyDeviationStandardDeviation(string, out double) | Gets the standard deviation of the peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorPeak(string, ref double[]) | Gets the peak frequency error for all measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorPeakLocation(string, ref double[]) | Gets the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds. |
| GetFrequencyErrorPeakMaximum(string, out double) | Gets the maximum peak frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorPeakMean(string, out double) | Gets the mean of the peak frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorPeakMinimum(string, out double) | Gets the minimum peak frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorPeakStandardDeviation(string, out double) | Gets the standard deviation of the peak frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorRms(string, ref double[]) | Gets the RMS frequency error for all measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorRmsMaximum(string, out double) | Gets the maximum RMS frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorRmsMean(string, out double) | Gets the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorRmsMinimum(string, out double) | Gets the minimum RMS frequency error across the measured pulses. This value is expressed in Hz. |
| GetFrequencyErrorRmsStandardDeviation(string, out double) | Gets the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz. |
| GetOvershoot(string, ref double[]) | Gets the overshoot values computed for all measured pulses. The overshoot value is defined as the ratio of height of the local peak after a rising edge to the pulse amplitude. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetOvershootMaximum(string, out double) | Gets the maximum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetOvershootMean(string, out double) | Gets the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetOvershootMinimum(string, out double) | Gets the minimum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetOvershootStandardDeviation(string, out double) | Gets the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetPeakLevel(string, ref double[]) | Gets the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm. |
| GetPeakLevelMaximum(string, out double) | Gets the maximum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetPeakLevelMean(string, out double) | Gets the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetPeakLevelMinimum(string, out double) | Gets the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetPeakLevelStandardDeviation(string, out double) | Gets the standard deviation of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| GetPhaseDeviation(string, ref double[]) | Gets the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees. |
| GetPhaseDeviationMaximum(string, out double) | Gets the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| GetPhaseDeviationMean(string, out double) | Gets the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| GetPhaseDeviationMinimum(string, out double) | Gets the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| GetPhaseDeviationStandardDeviation(string, out double) | Gets the standard deviation of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorPeak(string, ref double[]) | Gets the peak phase error for all measured pulses. This value is expressed in degrees. |
| GetPhaseErrorPeakLocation(string, ref double[]) | Gets the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds. |
| GetPhaseErrorPeakMaximum(string, out double) | Gets the maximum peak phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorPeakMean(string, out double) | Gets the mean of the peak phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorPeakMinimum(string, out double) | Gets the minimum peak phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorPeakStandardDeviation(string, out double) | Gets the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorRms(string, ref double[]) | Gets the RMS phase error for all measured pulses. This value is expressed in degrees. |
| GetPhaseErrorRmsMaximum(string, out double) | Gets the maximum RMS phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorRmsMean(string, out double) | Gets the mean of the RMS phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorRmsMinimum(string, out double) | Gets the minimum RMS phase error across the measured pulses. This value is expressed in degrees. |
| GetPhaseErrorRmsStandardDeviation(string, out double) | Gets the standard deviation of the RMS phase errors across the measured pulses. This value is expressed in degrees. |
| GetPhaseStability(string, ref double[]) | Gets the phase stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of phase from the reference. |
| GetPhaseStabilityMaximum(string, out double) | Gets the maximum phase stability across the measured pulses. This value is expressed in dB. |
| GetPhaseStabilityMean(string, out double) | Gets the mean of the phase stability values across the measured pulses. This value is expressed in dB. |
| GetPhaseStabilityMinimum(string, out double) | Gets the minimum phase stability across the measured pulses. This value is expressed in dB. |
| GetPhaseStabilityStandardDeviation(string, out double) | Gets the phase stability standard deviation across the measured pulses. This value is expressed in dB. |
| GetPulseCount(string, out int) | Gets the measured pulse count. |
| GetPulseOffDuration(string, ref double[]) | Gets the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds. |
| GetPulseOffDurationMaximum(string, out double) | Gets the maximum OFF duration across the measured pulses. This value is expressed in seconds. |
| GetPulseOffDurationMean(string, out double) | Gets the mean of the OFF duration values across the measured pulses. This value is expressed in seconds. |
| GetPulseOffDurationMinimum(string, out double) | Gets the minimum OFF duration across the measured pulses. This value is expressed in seconds. |
| GetPulseOffDurationStandardDeviation(string, out double) | Gets the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. |
| GetPulsePositionIndex(string, ref int[]) | Gets the position indices of all the measured pulses within a burst. |
| GetPulseRepetitionInterval(string, ref double[]) | Gets the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds. |
| GetPulseRepetitionIntervalMaximum(string, out double) | Gets the maximum pulse period across the measured pulses. This value is expressed in seconds. |
| GetPulseRepetitionIntervalMean(string, out double) | Gets the mean of pulse period values across the measured pulses. This value is expressed in seconds. |
| GetPulseRepetitionIntervalMinimum(string, out double) | Gets the minimum pulse period across the measured pulses. This value is expressed in seconds. |
| GetPulseRepetitionIntervalStandardDeviation(string, out double) | Gets the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. |
| GetPulseToPulseFrequencyDifference(string, ref double[]) | Gets the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz. |
| GetPulseToPulseFrequencyDifferenceMaximum(string, out double) | Gets the maximum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| GetPulseToPulseFrequencyDifferenceMean(string, out double) | Gets the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| GetPulseToPulseFrequencyDifferenceMinimum(string, out double) | Gets the minimum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| GetPulseToPulseFrequencyDifferenceStandardDeviation(string, out double) | Gets the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| GetPulseToPulsePhaseDifference(string, ref double[]) | Gets the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees. |
| GetPulseToPulsePhaseDifferenceMaximum(string, out double) | Gets the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| GetPulseToPulsePhaseDifferenceMean(string, out double) | Gets the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| GetPulseToPulsePhaseDifferenceMinimum(string, out double) | Gets the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| GetPulseToPulsePhaseDifferenceStandardDeviation(string, out double) | Gets the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| GetPulseWidth(string, ref double[]) | Gets the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds. |
| GetPulseWidthMaximum(string, out double) | Gets the maximum ON duration across the measured pulses. This value is expressed in seconds. |
| GetPulseWidthMean(string, out double) | Gets the mean of the ON duration values across the measured pulses. This value is expressed in seconds. |
| GetPulseWidthMinimum(string, out double) | Gets the minimum ON duration across the measured pulses. This value is expressed in seconds. |
| GetPulseWidthStandardDeviation(string, out double) | Gets the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds. |
| GetRipple(string, ref double[]) | Gets the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetRippleMaximum(string, out double) | Gets the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetRippleMean(string, out double) | Gets the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetRippleMinimum(string, out double) | Gets the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetRippleStandardDeviation(string, out double) | Gets the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| GetRiseEdge(string, ref double[]) | Gets the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds. |
| GetRiseTime(string, ref double[]) | Gets the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds. |
| GetRiseTimeMaximum(string, out double) | Gets the maximum rise time across the measured pulses. This value is expressed in seconds. |
| GetRiseTimeMean(string, out double) | Gets the mean of the rise time values across the measured pulses. This value is expressed in seconds. |
| GetRiseTimeMinimum(string, out double) | Gets the minimum rise time across the measured pulses. This value is expressed in seconds. |
| GetRiseTimeStandardDeviation(string, out double) | Gets the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeCompressionRatio(string, ref double[]) | Gets the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. |
| GetTimeSidelobeCompressionRatioMaximum(string, out double) | Gets the maximum compression ratio across the measured pulses. This value is expressed as a percentage. |
| GetTimeSidelobeCompressionRatioMean(string, out double) | Gets the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage. |
| GetTimeSidelobeCompressionRatioMinimum(string, out double) | Gets the minimum compression ratio across the measured pulses. This value is expressed as a percentage. |
| GetTimeSidelobeCompressionRatioStandardDeviation(string, out double) | Gets the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage. |
| GetTimeSidelobeDelay(string, ref double[]) | Gets the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. |
| GetTimeSidelobeDelayMaximum(string, out double) | Gets the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeDelayMean(string, out double) | Gets the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeDelayMinimum(string, out double) | Gets the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeDelayStandardDeviation(string, out double) | Gets the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeMainlobeWidth(string, ref double[]) | Gets the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds. |
| GetTimeSidelobeMainlobeWidthMaximum(string, out double) | Gets the maximum mainlobe width across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeMainlobeWidthMean(string, out double) | Gets the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeMainlobeWidthMinimum(string, out double) | Gets the minimum mainlobe width across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobeMainlobeWidthStandardDeviation(string, out double) | Gets the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobePeakCorrelation(string, ref double[]) | Gets the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1. |
| GetTimeSidelobePeakCorrelationMaximum(string, out double) | Gets the maximum peak correlation across the measured pulses. |
| GetTimeSidelobePeakCorrelationMean(string, out double) | Gets the mean of the peak correlation values across the measured pulses. |
| GetTimeSidelobePeakCorrelationMinimum(string, out double) | Gets the minimum peak correlation across the measured pulses. |
| GetTimeSidelobePeakCorrelationStandardDeviation(string, out double) | Gets the standard deviation of the peak correlation values across the measured pulses. |
| GetTimeSidelobePeakSidelobeLevel(string, ref double[]) | Gets the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. |
| GetTimeSidelobePeakSidelobeLevelMaximum(string, out double) | Gets the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds. |
| GetTimeSidelobePeakSidelobeLevelMean(string, out double) | Gets the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |
| GetTimeSidelobePeakSidelobeLevelMinimum(string, out double) | Gets the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. |
| GetTimeSidelobePeakSidelobeLevelStandardDeviation(string, out double) | Gets the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |
| GetTopLevel(string, ref double[]) | Gets the top levels for all measured pulses. The values are expressed in dBm. |
| GetTopLevelMaximum(string, out double) | Gets the maximum top level across the measured pulses. This value is expressed in dBm. |
| GetTopLevelMean(string, out double) | Gets the mean of the top levels across the measured pulses. This value is expressed in dBm. |
| GetTopLevelMinimum(string, out double) | Gets the minimum top level across the measured pulses. This value is expressed in dBm. |
| GetTopLevelStandardDeviation(string, out double) | Gets the standard deviation of the top levels across the measured pulses. This value is expressed in dBm. |
| GetTotalStability(string, ref double[]) | Gets the total stability of the measured pulses. This value is expressed in dB. |
| GetTotalStabilityMaximum(string, out double) | Gets the maximum total stability across the measured pulses. This value is expressed in dB. |
| GetTotalStabilityMean(string, out double) | Gets the mean of the total stability values across the measured pulses. This value is expressed in dB. |
| GetTotalStabilityMinimum(string, out double) | Gets the minimum total stability across the measured pulses. This value is expressed in dB. |
| GetTotalStabilityStandardDeviation(string, out double) | Gets the total stability standard deviation across the measured pulses. This value is expressed in dB. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityenabled.html language=enus -->
## TOPIC 00469: RFmxPulseMXPulseStabilityEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pulse stability results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseStabilityEnabledMembersNameValueDescriptionFalse0Pulse Stability results computation is disabled. True1Pulse Stability results computation is enabled.

### RFmxPulseMXPulseStabilityEnabled Enumeration

Specifies whether to enable pulse stability results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseStabilityEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Pulse Stability results computation is disabled. |
| True | 1 | Pulse Stability results computation is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html language=enus -->
## TOPIC 00470: RFmxPulseMXPulseStabilityFrequencyErrorCompensation Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseM

### RFmxPulseMXPulseStabilityFrequencyErrorCompensation Enumeration

Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseStabilityFrequencyErrorCompensation

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | Frequency error compensation is disabled. |
| On | 1 | Frequency error compensation is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobeenabled.html language=enus -->
## TOPIC 00471: RFmxPulseMXPulseTimeSidelobeEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobeenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pulse time sidelobe results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseTimeSidelobeEnabledMembersNameValueDescriptionFalse0Pulse Time Sidelobe results computation is disabled. True1Pulse Time Sidelobe results computation is e

### RFmxPulseMXPulseTimeSidelobeEnabled Enumeration

Specifies whether to enable pulse time sidelobe results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseTimeSidelobeEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Pulse Time Sidelobe results computation is disabled. |
| True | 1 | Pulse Time Sidelobe results computation is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html language=enus -->
## TOPIC 00472: RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseTimeSidelobeKeepOutTimeAutoMembersNameValueDescriptionFalse0Keep out time computation is set to manual specifified b

### RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto Enumeration

Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Keep out time computation is set to manual specifified by Pulse Time Sidelobe Keep Out Time (s) method. |
| True | 1 | Keep out time computation is set to automatic, determined mainlobe 3dB width is used. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobereferencewindowtype.html language=enus -->
## TOPIC 00473: RFmxPulseMXPulseTimeSidelobeReferenceWindowType Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobereferencewindowtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobereferencewindowtype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseTimeSidelobeReferenceWindowTypeMembersNameValueDescriptionNone0Indicates no windowing. FlatTop1I

### RFmxPulseMXPulseTimeSidelobeReferenceWindowType Enumeration

Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseTimeSidelobeReferenceWindowType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Indicates no windowing. |
| FlatTop | 1 | Indicates Flat Top window type. |
| Hanning | 2 | Indicates Hanning window type. |
| Hamming | 3 | Indicates Hamming window type. |
| Gaussian | 4 | Indicates Gaussian window type. |
| Blackman | 5 | Indicates Blackman window type. |
| DolphChebyshev | 6 | Indicates Chebyshev window type. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetracerangeauto.html language=enus -->
## TOPIC 00474: RFmxPulseMXPulseTraceRangeAuto Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetracerangeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetracerangeauto.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseTraceRangeAutoMembersNameValueDescriptionFalse0Trace range computation is set to manual. True1Trace range is au

### RFmxPulseMXPulseTraceRangeAuto Enumeration

Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseTraceRangeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Trace range computation is set to manual. |
| True | 1 | Trace range is automatically computed according to the pulse width. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetracerangereference.html language=enus -->
## TOPIC 00475: RFmxPulseMXPulseTraceRangeReference Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetracerangereference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetracerangereference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseTraceRangeReferenceMembersNameValueDescriptionRise0Trace range is defined

### RFmxPulseMXPulseTraceRangeReference Enumeration

Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseTraceRangeReference

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rise | 0 | Trace range is defined in reference to the rising edge. |
| Center | 1 | Trace range is defined in reference to the center of the pulse. |
| Fall | 2 | Trace range is defined in reference to the falling edge. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html language=enus -->
## TOPIC 00476: RFmxPulseMXSegmentedAcquisitionEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXSegmentedAcquisitionEnabledMembersNameValueDescriptionFalse0Segmented acquisition is disabled. True1Segmented acqu

### RFmxPulseMXSegmentedAcquisitionEnabled Enumeration

Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXSegmentedAcquisitionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Segmented acquisition is disabled. |
| True | 1 | Segmented acquisition is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxsubobject.html language=enus -->
## TOPIC 00477: RFmxPulseMXSubObject Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxsubobject.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxsubobject.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents members that are common to all sub-object of RFmxPulseMX classes. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic class RFmxPulseMXSubObjectThread SafetyAny public static members of this type are thread safe. Any instance members are not guaranteed to be thread saf

### RFmxPulseMXSubObject Class

Represents members that are common to all sub-object of RFmxPulseMX classes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public class RFmxPulseMXSubObject

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00478: RFmxPulseMXTriggerMinimumQuietTimeMode Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggerminimumquiettimemode.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXTriggerMinimumQuietTimeModeMembersNameValueDescriptionManual0The minimum quiet time for triggering is the value of the TriggerMinimumQuietTim

### RFmxPulseMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXTriggerMinimumQuietTimeMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the TriggerMinimumQuietTimeDuration method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html language=enus -->
## TOPIC 00479: RFmxPulseMXTriggerType Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXTriggerTypeMembersNameValueDescriptionNone0No Reference Trigger is configured. DigitalEdge1The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is spe

### RFmxPulseMXTriggerType Enumeration

Specifies the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the DigitalEdgeTriggerSource method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQPowerEdgeTriggerSlope method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx.html language=enus -->
## TOPIC 00480: NationalInstruments.RFmx.PulseMX

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxPulseMXDefines a root class which is used to identify and control PULSE signal configuration. RFmxPulseMXConstantsSpecifies constants for I/O terminals. RFmxPulseMXPulseRepresents the Pulse measurement. RFmxPulseMXPulseConfigurationProvides methods to configure the Pulse me

### NationalInstruments.RFmx.PulseMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxPulseMX | Defines a root class which is used to identify and control PULSE signal configuration. |
| RFmxPulseMXConstants | Specifies constants for I/O terminals. |
| RFmxPulseMXPulse | Represents the Pulse measurement. |
| RFmxPulseMXPulseConfiguration | Provides methods to configure the Pulse measurement. |
| RFmxPulseMXPulseResults | Provides methods to fetch and read the Pulse measurement results. |
| RFmxPulseMXSubObject | Represents members that are common to all sub-object of RFmxPulseMX classes. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxPulseMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| RFmxPulseMXIQPowerEdgeTriggerLevelType | Specifies the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |
| RFmxPulseMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |
| RFmxPulseMXMaximumPulseCountEnabled | Specifies whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| RFmxPulseMXMeasurementFilterType | Specifies the demodulation filter type to be used in the measurements. |
| RFmxPulseMXMeasurementTypes | Specifies the type of measurement. |
| RFmxPulseMXMultiburstEnabled | Specifies whether to enable pulse measurements on the multiple burst transmission. |
| RFmxPulseMXPropertyId | Specifies all the attribute identifiers. |
| RFmxPulseMXPulseAcquisitionTraceSelect | Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. |
| RFmxPulseMXPulseAmplitudeLevelDomain | Specifies whether voltage or power to be used as domain for pulse measurements. |
| RFmxPulseMXPulseAmplitudeTraceUnit | Specifies the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace. |
| RFmxPulseMXPulseCWFrequencyOffsetAuto | Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| RFmxPulseMXPulseDetectionReference | Specifies the reference used for SetDetectionThreshold(string, double) method. |
| RFmxPulseMXPulseDroopCompensationEnabled | Specifies whether to compensate the droop detected in pulse level when applying thresholds. |
| RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference | Specifies the reference used for the measurement range in phase/frequency deviation and error measurements. |
| RFmxPulseMXPulseLevelComputationMethod | Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |
| RFmxPulseMXPulseMeasurementPointReference | Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |
| RFmxPulseMXPulseMetricsAmplitudeDeviationUnit | Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |
| RFmxPulseMXPulseMetricsEnabled | Specifies whether to enable pulse metrics results computation. |
| RFmxPulseMXPulseModulationType | Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |
| RFmxPulseMXPulseMultipleMeasurementPointsEnabled | Specifies whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |
| RFmxPulseMXPulseStabilityEnabled | Specifies whether to enable pulse stability results computation. |
| RFmxPulseMXPulseStabilityFrequencyErrorCompensation | Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |
| RFmxPulseMXPulseTimeSidelobeEnabled | Specifies whether to enable pulse time sidelobe results computation. |
| RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto | Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual. |
| RFmxPulseMXPulseTimeSidelobeReferenceWindowType | Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |
| RFmxPulseMXPulseTraceRangeAuto | Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you. |
| RFmxPulseMXPulseTraceRangeReference | Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |
| RFmxPulseMXSegmentedAcquisitionEnabled | Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |
| RFmxPulseMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxPulseMXTriggerType | Specifies the trigger type. |

#### Delegates

None
