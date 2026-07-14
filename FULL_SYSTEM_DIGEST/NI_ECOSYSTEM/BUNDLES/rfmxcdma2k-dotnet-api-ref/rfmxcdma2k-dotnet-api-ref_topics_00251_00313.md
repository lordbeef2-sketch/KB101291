# NI DOCUMENT BUNDLE: rfmxcdma2k-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxcdma2k-dotnet-api-ref start=251 end=313 -->
<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults.html language=enus -->
## TOPIC 00251: RFmxCdma2kMXSemResults Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SEM measurement results. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSemResults : RFmxCdma2kMXSubObjectMethodsNameDescriptionFetchCarrierAbsoluteIntegratedPower(string, double, out double)Returns t

### RFmxCdma2kMXSemResults Class

Provides methods to fetch and read the SEM measurement results.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSemResults : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchCarrierAbsoluteIntegratedPower(string, double, out double) | Returns the absolute carrier integrated power of the SEM measurement. |
| FetchLowerOffsetMargin(string, double, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchLowerOffsetMarginArray(string, double, ref RFmxCdma2kMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns the array of measurement status and margins from the limit line measured in the lower offset segments. |
| FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the lower offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns the arrays of lower offset segment power measurements. |
| FetchMeasurementStatus(string, double, out RFmxCdma2kMXSemMeasurementStatus) | Returns the SEM measurement status. |
| FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >) | Returns the spectrum used for the SEM measurement. |
| FetchUpperOffsetMargin(string, double, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchUpperOffsetMarginArray(string, double, ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns the measurement status and margin from the limit line measured in the upper offset segments. |
| FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the upper offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns the arrays of upper offset segment power measurements. |
| GetCarrierAbsoluteIntegratedPower(string, out double) | Gets the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. |
| GetLowerOffsetAbsoluteIntegratedPower(string, out double) | Gets the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetAbsolutePeakPower(string, out double) | Gets the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetMargin(string, out double) | Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetMarginAbsolutePower(string, out double) | Gets the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetMarginFrequency(string, out double) | Gets the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetMarginRelativePower(string, out double) | Gets the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetMeasurementStatus(string, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus) | Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetRelativeIntegratedPower(string, out double) | Gets the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| GetLowerOffsetRelativePeakPower(string, out double) | Gets the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| GetMeasurementStatus(string, out RFmxCdma2kMXSemMeasurementStatus) | Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. |
| GetUpperOffsetAbsoluteIntegratedPower(string, out double) | Gets the power measured in the upper (positive) offset segment. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetAbsolutePeakPower(string, out double) | Gets the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetMargin(string, out double) | Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetMarginAbsolutePower(string, out double) | Gets the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetMarginFrequency(string, out double) | Gets the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetMarginRelativePower(string, out double) | Gets the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetMeasurementStatus(string, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus) | Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetRelativeIntegratedPower(string, out double) | Gets the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| GetUpperOffsetRelativePeakPower(string, out double) | Gets the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html language=enus -->
## TOPIC 00252: RFmxCdma2kMXSemSweepTimeAuto Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The meas

### RFmxCdma2kMXSemSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses the default sweep time, 0.001667 seconds. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemupperoffsetmeasurementstatus.html language=enus -->
## TOPIC 00253: RFmxCdma2kMXSemUpperOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemupperoffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemupperoffsetmeasurementstatus.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemUpperOffsetMeasurementStatusMembersNameValueDescriptionFail0The lowe

### RFmxCdma2kMXSemUpperOffsetMeasurementStatus Enumeration

Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemUpperOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The lower offset segment measurement fails according to the measurement limits specified by this standard. |
| Pass | 1 | The lower offset segment measurement passes according to the measurement limits specified by this standard. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase-configuration.html language=enus -->
## TOPIC 00254: Configuration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase-configuration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSlotPhaseConfiguration Configuration { get; }

### Configuration

Gets the [RFmxCdma2kMXSlotPhaseConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration.html) instance that provides methods to configure the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSlotPhaseConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration.html) Configuration { get; }

Parent topic:

RFmxCdma2kMXSlotPhase Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase-results.html language=enus -->
## TOPIC 00255: Results

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase-results.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSlotPhaseResults Results { get; }

### Results

Gets the [RFmxCdma2kMXSlotPhaseResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults.html) instance that provides methods to fetch and read the SlotPhase measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSlotPhaseResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults.html) Results { get; }

Parent topic:

RFmxCdma2kMXSlotPhase Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase.html language=enus -->
## TOPIC 00256: RFmxCdma2kMXSlotPhase Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SlotPhase measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSlotPhase : RFmxCdma2kMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxCdma2kMXSlotPhaseConfiguration instance that provides methods to confi

### RFmxCdma2kMXSlotPhase Class

Represents the SlotPhase measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSlotPhase : RFmxCdma2kMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxCdma2kMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. |
| Results | Gets the RFmxCdma2kMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxslotphasesynchronizationmode-int-int.html language=enus -->
## TOPIC 00257: ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPhaseSynchronizationMode, int, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxslotphasesynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxslotphasesynchronizationmode-int-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronizationMode, measurementOffset, and measurementLength parameters of the SlotPhase measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXSlotPhaseSynchronizationMode synchronizationMod

### ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPhaseSynchronizationMode, int, int)

Configures the *synchronizationMode*, *measurementOffset*, and *measurementLength* parameters of the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXSlotPhaseSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxCdma2kMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the synchronizationMode parameter. |
| measurementLength | int | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00258: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseAllTracesEnabled attribute.The

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00259: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescripti

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00260: GetMeasurementLength(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPhaseMeasurementLength attribute.The default value is 16.P

### GetMeasurementLength(string, out int)

Gets the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00261: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetM

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotphasesynchronizationmode.html) method. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getreceivefilterenabled__string-out.html language=enus -->
## TOPIC 00262: GetReceiveFilterEnabled(string, out RFmxCdma2kMXSlotPhaseReceiveFilterEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getreceivefilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getreceivefilterenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetReceiveFilterEnabled(string selectorString, out RFmxCdma2kMXSlotPhaseReceiveFil

### GetReceiveFilterEnabled(string, out RFmxCdma2kMXSlotPhaseReceiveFilterEnabled)

Gets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetReceiveFilterEnabled(string selectorString, out RFmxCdma2kMXSlotPhaseReceiveFilterEnabled value)

#### Remarks

This method gets the value of [SlotPhaseReceiveFilterEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasereceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSlotPhaseReceiveFilterEnabled | Upon return, contains whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00263: GetSpectrumInverted(string, out RFmxCdma2kMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSpectrumInverted(string selectorString, out RFmxCdma2kMXSlotPhaseSpectrumInverted value)RemarksThis method gets the value of SlotPhaseSpectrumInverted attribute.The default value is F

### GetSpectrumInverted(string, out RFmxCdma2kMXSlotPhaseSpectrumInverted)

Gets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSpectrumInverted(string selectorString, out RFmxCdma2kMXSlotPhaseSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSlotPhaseSpectrumInverted | Upon return, contains whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getsynchronizationmode__string-out.html language=enus -->
## TOPIC 00264: GetSynchronizationMode(string, out RFmxCdma2kMXSlotPhaseSynchronizationMode)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getsynchronizationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-getsynchronizationmode__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSynchronizationMode(string selectorString, out RFmxCdma2kMXSlotPhaseSynchronizationMode value)RemarksThis method gets the value of SlotPhaseSynchronizationMode a

### GetSynchronizationMode(string, out RFmxCdma2kMXSlotPhaseSynchronizationMode)

Gets whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSynchronizationMode(string selectorString, out RFmxCdma2kMXSlotPhaseSynchronizationMode value)

#### Remarks

This method gets the value of [SlotPhaseSynchronizationMode](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasesynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSlotPhaseSynchronizationMode | Upon return, contains whether the measurement is performed from the frame or slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-gettransientduration__string-out.html language=enus -->
## TOPIC 00265: GetTransientDuration(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-gettransientduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-gettransientduration__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetTransientDuration(string selectorString, out double value)RemarksThis method gets the value of SlotPhaseTransie

### GetTransientDuration(string, out double)

Gets the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetTransientDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [SlotPhaseTransientDuration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0. The valid values are 0 to 0.0002, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00266: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPhaseAllTracesEnabled attribute.The def

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00267: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPhaseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionse

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00268: SetMeasurementLength(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of SlotPhaseMeasurementLength attribute.The default value is 16.Param

### SetMeasurementLength(string, int)

Sets the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00269: SetMeasurementOffset(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetM

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotphasesynchronizationmode.html) method. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setreceivefilterenabled__string-rfmxcdma2kmxslotphasereceivefilterenabled.html language=enus -->
## TOPIC 00270: SetReceiveFilterEnabled(string, RFmxCdma2kMXSlotPhaseReceiveFilterEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setreceivefilterenabled__string-rfmxcdma2kmxslotphasereceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setreceivefilterenabled__string-rfmxcdma2kmxslotphasereceivefilterenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetReceiveFilterEnabled(string selectorString, RFmxCdma2kMXSlotPhaseReceiveFilterE

### SetReceiveFilterEnabled(string, RFmxCdma2kMXSlotPhaseReceiveFilterEnabled)

Sets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetReceiveFilterEnabled(string selectorString, RFmxCdma2kMXSlotPhaseReceiveFilterEnabled value)

#### Remarks

This method sets the value of [SlotPhaseReceiveFilterEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasereceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSlotPhaseReceiveFilterEnabled | Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setspectruminverted__string-rfmxcdma2kmxslotphasespectruminverted.html language=enus -->
## TOPIC 00271: SetSpectrumInverted(string, RFmxCdma2kMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setspectruminverted__string-rfmxcdma2kmxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setspectruminverted__string-rfmxcdma2kmxslotphasespectruminverted.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSpectrumInverted(string selectorString, RFmxCdma2kMXSlotPhaseSpectrumInverted value)RemarksThis method sets the value of SlotPhaseSpectrumInverted attribute.The default value is False

### SetSpectrumInverted(string, RFmxCdma2kMXSlotPhaseSpectrumInverted)

Sets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSpectrumInverted(string selectorString, RFmxCdma2kMXSlotPhaseSpectrumInverted value)

#### Remarks

This method sets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSlotPhaseSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00272: SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotphasesynchronizationmode.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSynchronizationMode(string selectorString, RFmxCdma2kMXSlotPhaseSynchronizationMode value)RemarksThis method sets the value of SlotPhaseSynchronizationMode attri

### SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode)

Sets whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSynchronizationMode(string selectorString, RFmxCdma2kMXSlotPhaseSynchronizationMode value)

#### Remarks

This method sets the value of [SlotPhaseSynchronizationMode](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasesynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-settransientduration__string-double.html language=enus -->
## TOPIC 00273: SetTransientDuration(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-settransientduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration-settransientduration__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetTransientDuration(string selectorString, double value)RemarksThis method sets the value of SlotPhaseTransientDu

### SetTransientDuration(string, double)

Sets the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetTransientDuration(string selectorString, double value)

#### Remarks

This method sets the value of [SlotPhaseTransientDuration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0. The valid values are 0 to 0.0002, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration.html language=enus -->
## TOPIC 00274: RFmxCdma2kMXSlotPhaseConfiguration Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SlotPhase measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSlotPhaseConfiguration : RFmxCdma2kMXSubObjectMethodsNameDescriptionConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPha

### RFmxCdma2kMXSlotPhaseConfiguration Class

Provides methods to configure the SlotPhase measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSlotPhaseConfiguration : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPhaseSynchronizationMode, int, int) | Configures the synchronizationMode, measurementOffset, and measurementLength parameters of the SlotPhase measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SlotPhase measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of the SlotPhase measurement. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. |
| GetReceiveFilterEnabled(string, out RFmxCdma2kMXSlotPhaseReceiveFilterEnabled) | Gets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. |
| GetSpectrumInverted(string, out RFmxCdma2kMXSlotPhaseSpectrumInverted) | Gets whether the spectrum of the signal is inverted. |
| GetSynchronizationMode(string, out RFmxCdma2kMXSlotPhaseSynchronizationMode) | Gets whether the measurement is performed from the frame or slot boundary. |
| GetTransientDuration(string, out double) | Gets the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SlotPhase measurement. |
| SetMeasurementLength(string, int) | Sets the duration of the SlotPhase measurement. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. |
| SetReceiveFilterEnabled(string, RFmxCdma2kMXSlotPhaseReceiveFilterEnabled) | Sets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. |
| SetSpectrumInverted(string, RFmxCdma2kMXSlotPhaseSpectrumInverted) | Sets whether the spectrum of the signal is inverted. |
| SetSynchronizationMode(string, RFmxCdma2kMXSlotPhaseSynchronizationMode) | Sets whether the measurement is performed from the frame or slot boundary. |
| SetTransientDuration(string, double) | Sets the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasereceivefilterenabled.html language=enus -->
## TOPIC 00275: RFmxCdma2kMXSlotPhaseReceiveFilterEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasereceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasereceivefilterenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received sign

### RFmxCdma2kMXSlotPhaseReceiveFilterEnabled Enumeration

Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSlotPhaseReceiveFilterEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables received filtering for the SlotPhase measurement. |
| True | 1 | Enables received filtering for the SlotPhase measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html language=enus -->
## TOPIC 00276: FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of th

### FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the slot boundary and extrapolates the phase error to the slot boundaries.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchChipPhaseErrorLinearFitTrace(string selectorString, double timeout, ref AnalogWaveform< float > chipPhaseErrorLinearFit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| chipPhaseErrorLinearFit | ref AnalogWaveform< float > | Upon return, contains the chip phase error linear fit trace for the SlotPhase measurement. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchchipphaseerrortrace__string-double-ref.html language=enus -->
## TOPIC 00277: FetchChipPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchchipphaseerrortrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchchipphaseerrortrace__string-double-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchChipPhaseErrorTrace(string selectorString, double timeout, ref AnalogWa

### FetchChipPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchChipPhaseErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > chipPhaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| chipPhaseError | ref AnalogWaveform< float > | Upon return, contains the chip phase error for the SlotPhase measurement. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchmaximumphasediscontinuity__string-double-out.html language=enus -->
## TOPIC 00278: FetchMaximumPhaseDiscontinuity(string, double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchmaximumphasediscontinuity__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchmaximumphasediscontinuity__string-double-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity value observed in the measurement interval.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchMaximumPhaseDiscontinuity(string selectorString, double timeout, out double maximumPhaseDiscontinuity)ParametersNameTypeDescriptionselectorStringstring

### FetchMaximumPhaseDiscontinuity(string, double, out double)

Fetches the maximum phase discontinuity value observed in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchMaximumPhaseDiscontinuity(string selectorString, double timeout, out double maximumPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| maximumPhaseDiscontinuity | out double | Upon return, contains the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchphasediscontinuities__string-double-ref.html language=enus -->
## TOPIC 00279: FetchPhaseDiscontinuities(string, double, ref double[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchphasediscontinuities__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-fetchphasediscontinuities__string-double-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity values for the slot boundaries in the measurement interval.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] slotPhaseDiscontinuity)ParametersNameTypeDescriptionselectorStringstri

### FetchPhaseDiscontinuities(string, double, ref double[])

Fetches the phase discontinuity values for the slot boundaries in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] slotPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| slotPhaseDiscontinuity | ref double[] | Upon return, contains the array of phase discontinuity values for the slot boundaries in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-getmaximumphasediscontinuity__string-out.html language=enus -->
## TOPIC 00280: GetMaximumPhaseDiscontinuity(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-getmaximumphasediscontinuity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults-getmaximumphasediscontinuity__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMaximumPhaseDiscontinuity(string selectorString, out double value)RemarksThis method gets the value of SlotPhaseRe

### GetMaximumPhaseDiscontinuity(string, out double)

Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMaximumPhaseDiscontinuity(string selectorString, out double value)

#### Remarks

This method gets the value of [SlotPhaseResultsMaximumPhaseDiscontinuity](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults.html language=enus -->
## TOPIC 00281: RFmxCdma2kMXSlotPhaseResults Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphaseresults.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SlotPhase measurement results. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSlotPhaseResults : RFmxCdma2kMXSubObjectMethodsNameDescriptionFetchChipPhaseErrorLinearFitTrace(string, double, ref Analog

### RFmxCdma2kMXSlotPhaseResults Class

Provides methods to fetch and read the SlotPhase measurement results.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSlotPhaseResults : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >) | Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the slot boundary and extrapolates the phase error to the slot boundaries. |
| FetchChipPhaseErrorTrace(string, double, ref AnalogWaveform< float >) | Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform. |
| FetchMaximumPhaseDiscontinuity(string, double, out double) | Fetches the maximum phase discontinuity value observed in the measurement interval. |
| FetchPhaseDiscontinuities(string, double, ref double[]) | Fetches the phase discontinuity values for the slot boundaries in the measurement interval. |
| GetMaximumPhaseDiscontinuity(string, out double) | Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasespectruminverted.html language=enus -->
## TOPIC 00282: RFmxCdma2kMXSlotPhaseSpectrumInverted Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasespectruminverted.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSlotPhaseSpectrumInvertedMembersNameValueDescriptionFalse0The measured spectrum is not inverted. True1The measured spectrum is inverted.

### RFmxCdma2kMXSlotPhaseSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSlotPhaseSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measured spectrum is not inverted. |
| True | 1 | The measured spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00283: RFmxCdma2kMXSlotPhaseSynchronizationMode Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphasesynchronizationmode.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSlotPhaseSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of s

### RFmxCdma2kMXSlotPhaseSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSlotPhaseSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(string, int) method starting at the SlotPhase measurement offset slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length method starting at the SlotPhase measurement offset slots from the slot boundary. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower-configuration.html language=enus -->
## TOPIC 00284: Configuration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower-configuration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSlotPowerConfiguration instance that provides methods to configure the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSlotPowerConfiguration Configuration { get; }

### Configuration

Gets the [RFmxCdma2kMXSlotPowerConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration.html) instance that provides methods to configure the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSlotPowerConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration.html) Configuration { get; }

Parent topic:

RFmxCdma2kMXSlotPower Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower-results.html language=enus -->
## TOPIC 00285: Results

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower-results.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSlotPowerResults instance that provides methods to fetch and read the SlotPower measurement results. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSlotPowerResults Results { get; }

### Results

Gets the [RFmxCdma2kMXSlotPowerResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults.html) instance that provides methods to fetch and read the SlotPower measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSlotPowerResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults.html) Results { get; }

Parent topic:

RFmxCdma2kMXSlotPower Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower.html language=enus -->
## TOPIC 00286: RFmxCdma2kMXSlotPower Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SlotPower measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSlotPower : RFmxCdma2kMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxCdma2kMXSlotPowerConfiguration instance that provides methods to confi

### RFmxCdma2kMXSlotPower Class

Represents the SlotPower measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSlotPower : RFmxCdma2kMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxCdma2kMXSlotPowerConfiguration instance that provides methods to configure the SlotPower measurement. |
| Results | Gets the RFmxCdma2kMXSlotPowerResults instance that provides methods to fetch and read the SlotPower measurement results. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxslotpowersynchronizationmode-int-int.html language=enus -->
## TOPIC 00287: ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPowerSynchronizationMode, int, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxslotpowersynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxslotpowersynchronizationmode-int-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronizationMode, measurementOffset, and measurementLength parameters for the SlotPower measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXSlotPowerSynchronizationMode synchronizationMo

### ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPowerSynchronizationMode, int, int)

Configures the *synchronizationMode*, *measurementOffset*, and *measurementLength* parameters for the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXSlotPowerSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxCdma2kMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the synchronizationMode parameter. This value is expressed in slots. |
| measurementLength | int | Specifies the duration of SlotPower measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00288: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPowerMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescripti

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPowerMeasurementEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00289: GetMeasurementLength(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the SlotPower measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPowerMeasurementLength attribute.The default value is 16.P

### GetMeasurementLength(string, out int)

Gets the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPowerMeasurementLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the SlotPower measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00290: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetM

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotpowersynchronizationmode.html) method. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPowerMeasurementOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getreceivefilterenabled__string-out.html language=enus -->
## TOPIC 00291: GetReceiveFilterEnabled(string, out RFmxCdma2kMXSlotPowerReceiveFilterEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getreceivefilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getreceivefilterenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetReceiveFilterEnabled(string selectorString, out RFmxCdma2kMXSlotPowerReceiveFil

### GetReceiveFilterEnabled(string, out RFmxCdma2kMXSlotPowerReceiveFilterEnabled)

Gets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetReceiveFilterEnabled(string selectorString, out RFmxCdma2kMXSlotPowerReceiveFilterEnabled value)

#### Remarks

This method gets the value of [SlotPowerReceiveFilterEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerreceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSlotPowerReceiveFilterEnabled | Upon return, contains whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00292: GetSpectrumInverted(string, out RFmxCdma2kMXSlotPowerSpectrumInverted)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSpectrumInverted(string selectorString, out RFmxCdma2kMXSlotPowerSpectrumInverted value)RemarksThis method gets the value of SlotPowerSpectrumInverted attribute.The default value is F

### GetSpectrumInverted(string, out RFmxCdma2kMXSlotPowerSpectrumInverted)

Gets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSpectrumInverted(string selectorString, out RFmxCdma2kMXSlotPowerSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPowerSpectrumInverted](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSlotPowerSpectrumInverted | Upon return, contains whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getsynchronizationmode__string-out.html language=enus -->
## TOPIC 00293: GetSynchronizationMode(string, out RFmxCdma2kMXSlotPowerSynchronizationMode)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getsynchronizationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-getsynchronizationmode__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSynchronizationMode(string selectorString, out RFmxCdma2kMXSlotPowerSynchronizationMode value)RemarksThis method gets the value of SlotPowerSynchronizationMode a

### GetSynchronizationMode(string, out RFmxCdma2kMXSlotPowerSynchronizationMode)

Gets whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSynchronizationMode(string selectorString, out RFmxCdma2kMXSlotPowerSynchronizationMode value)

#### Remarks

This method gets the value of [SlotPowerSynchronizationMode](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowersynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSlotPowerSynchronizationMode | Upon return, contains whether the measurement is performed from the frame or slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00294: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPowerMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionse

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPowerMeasurementEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00295: SetMeasurementLength(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the SlotPower measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of SlotPowerMeasurementLength attribute.The default value is 16.Param

### SetMeasurementLength(string, int)

Sets the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPowerMeasurementLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00296: SetMeasurementOffset(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetM

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotpowersynchronizationmode.html) method. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPowerMeasurementOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setreceivefilterenabled__string-rfmxcdma2kmxslotpowerreceivefilterenabled.html language=enus -->
## TOPIC 00297: SetReceiveFilterEnabled(string, RFmxCdma2kMXSlotPowerReceiveFilterEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setreceivefilterenabled__string-rfmxcdma2kmxslotpowerreceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setreceivefilterenabled__string-rfmxcdma2kmxslotpowerreceivefilterenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetReceiveFilterEnabled(string selectorString, RFmxCdma2kMXSlotPowerReceiveFilterE

### SetReceiveFilterEnabled(string, RFmxCdma2kMXSlotPowerReceiveFilterEnabled)

Sets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetReceiveFilterEnabled(string selectorString, RFmxCdma2kMXSlotPowerReceiveFilterEnabled value)

#### Remarks

This method sets the value of [SlotPowerReceiveFilterEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerreceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSlotPowerReceiveFilterEnabled | Specifies whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setspectruminverted__string-rfmxcdma2kmxslotpowerspectruminverted.html language=enus -->
## TOPIC 00298: SetSpectrumInverted(string, RFmxCdma2kMXSlotPowerSpectrumInverted)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setspectruminverted__string-rfmxcdma2kmxslotpowerspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setspectruminverted__string-rfmxcdma2kmxslotpowerspectruminverted.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSpectrumInverted(string selectorString, RFmxCdma2kMXSlotPowerSpectrumInverted value)RemarksThis method sets the value of SlotPowerSpectrumInverted attribute.The default value is False

### SetSpectrumInverted(string, RFmxCdma2kMXSlotPowerSpectrumInverted)

Sets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSpectrumInverted(string selectorString, RFmxCdma2kMXSlotPowerSpectrumInverted value)

#### Remarks

This method sets the value of [SlotPowerSpectrumInverted](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSlotPowerSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotpowersynchronizationmode.html language=enus -->
## TOPIC 00299: SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotpowersynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration-setsynchronizationmode__string-rfmxcdma2kmxslotpowersynchronizationmode.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSynchronizationMode(string selectorString, RFmxCdma2kMXSlotPowerSynchronizationMode value)RemarksThis method sets the value of SlotPowerSynchronizationMode attri

### SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode)

Sets whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSynchronizationMode(string selectorString, RFmxCdma2kMXSlotPowerSynchronizationMode value)

#### Remarks

This method sets the value of [SlotPowerSynchronizationMode](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowersynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration.html language=enus -->
## TOPIC 00300: RFmxCdma2kMXSlotPowerConfiguration Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SlotPower measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSlotPowerConfiguration : RFmxCdma2kMXSubObjectMethodsNameDescriptionConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPow

### RFmxCdma2kMXSlotPowerConfiguration Class

Provides methods to configure the SlotPower measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSlotPowerConfiguration : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXSlotPowerSynchronizationMode, int, int) | Configures the synchronizationMode, measurementOffset, and measurementLength parameters for the SlotPower measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SlotPower measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of the SlotPower measurement. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |
| GetReceiveFilterEnabled(string, out RFmxCdma2kMXSlotPowerReceiveFilterEnabled) | Gets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |
| GetSpectrumInverted(string, out RFmxCdma2kMXSlotPowerSpectrumInverted) | Gets whether the spectrum of the signal is inverted. |
| GetSynchronizationMode(string, out RFmxCdma2kMXSlotPowerSynchronizationMode) | Gets whether the measurement is performed from the frame or slot boundary. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SlotPower measurement. |
| SetMeasurementLength(string, int) | Sets the duration of the SlotPower measurement. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |
| SetReceiveFilterEnabled(string, RFmxCdma2kMXSlotPowerReceiveFilterEnabled) | Sets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |
| SetSpectrumInverted(string, RFmxCdma2kMXSlotPowerSpectrumInverted) | Sets whether the spectrum of the signal is inverted. |
| SetSynchronizationMode(string, RFmxCdma2kMXSlotPowerSynchronizationMode) | Sets whether the measurement is performed from the frame or slot boundary. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerreceivefilterenabled.html language=enus -->
## TOPIC 00301: RFmxCdma2kMXSlotPowerReceiveFilterEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerreceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerreceivefilterenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSlotPowerReceiveFilterEnabledMembersNameValueDescriptionFalse0Di

### RFmxCdma2kMXSlotPowerReceiveFilterEnabled Enumeration

Specifies whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSlotPowerReceiveFilterEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables received filtering for the SlotPower measurement. |
| True | 1 | Enables received filtering for the SlotPower measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults-fetchpowers__string-double-ref-ref.html language=enus -->
## TOPIC 00302: FetchPowers(string, double, ref double[], ref double[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults-fetchpowers__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults-fetchpowers__string-double-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchPowers(string selectorString, double timeout, ref double[] s

### FetchPowers(string, double, ref double[], ref double[])

Fetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchPowers(string selectorString, double timeout, ref double[] slotPower, ref double[] slotPowerDelta)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| slotPower | ref double[] | Upon return, contains the array of SlotPower for all slots in the configured measurement interval. This value is expressed in dBm. |
| slotPowerDelta | ref double[] | Upon return, contains the array of SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSlotPowerResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults.html language=enus -->
## TOPIC 00303: RFmxCdma2kMXSlotPowerResults Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerresults.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SlotPower measurement results. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSlotPowerResults : RFmxCdma2kMXSubObjectMethodsNameDescriptionFetchPowers(string, double, ref double[], ref double[])Fetch

### RFmxCdma2kMXSlotPowerResults Class

Provides methods to fetch and read the SlotPower measurement results.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSlotPowerResults : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchPowers(string, double, ref double[], ref double[]) | Fetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerspectruminverted.html language=enus -->
## TOPIC 00304: RFmxCdma2kMXSlotPowerSpectrumInverted Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowerspectruminverted.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSlotPowerSpectrumInvertedMembersNameValueDescriptionFalse0The measurement spectrum is normal. True1The measurement spectrum is inverted.

### RFmxCdma2kMXSlotPowerSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSlotPowerSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement spectrum is normal. |
| True | 1 | The measurement spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowersynchronizationmode.html language=enus -->
## TOPIC 00305: RFmxCdma2kMXSlotPowerSynchronizationMode Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowersynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpowersynchronizationmode.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSlotPowerSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of s

### RFmxCdma2kMXSlotPowerSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSlotPowerSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(string, int) method starting at the SlotPower measurement offset slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length method starting at the SlotPower measurement offset slots from the slot boundary. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsubobject.html language=enus -->
## TOPIC 00306: RFmxCdma2kMXSubObject Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsubobject.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsubobject.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents members that are common to all sub-object of RFmxCdma2kMX classes. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSubObjectThread SafetyAny public static members of this type are thread safe. Any instance members are not guaranteed to be thread

### RFmxCdma2kMXSubObject Class

Represents members that are common to all sub-object of RFmxCdma2kMX classes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSubObject

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00307: RFmxCdma2kMXTriggerMinimumQuietTimeMode Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggerminimumquiettimemode.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXTriggerMinimumQuietTimeModeMembersNameValueDescriptionManual0The minimum quiet time for triggering is the value of the SetTriggerMinimumQui

### RFmxCdma2kMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXTriggerMinimumQuietTimeMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(string, double) method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html language=enus -->
## TOPIC 00308: RFmxCdma2kMXTriggerType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXTriggerTypeMembersNameValueDescriptionNone0No Reference Trigger is configured. DigitalEdge1The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is s

### RFmxCdma2kMXTriggerType Enumeration

Specifies the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(string, string) method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSource(string, string) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx.html language=enus -->
## TOPIC 00309: NationalInstruments.RFmx.Cdma2kMX

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxCdma2kMXDefines a root class which is used to identify and control CDMA2k signal configuration. RFmxCdma2kMXAcpRepresents the ACP measurement. RFmxCdma2kMXAcpConfigurationProvides methods to configure the ACP measurement. RFmxCdma2kMXAcpResultsProvides methods to fetch and

### NationalInstruments.RFmx.Cdma2kMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxCdma2kMX | Defines a root class which is used to identify and control CDMA2k signal configuration. |
| RFmxCdma2kMXAcp | Represents the ACP measurement. |
| RFmxCdma2kMXAcpConfiguration | Provides methods to configure the ACP measurement. |
| RFmxCdma2kMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
| RFmxCdma2kMXCda | Represents the CDA measurement. |
| RFmxCdma2kMXCdaConfiguration | Provides methods to configure the CDA measurement. |
| RFmxCdma2kMXCdaResults | Provides methods to fetch and read the CDA measurement results. |
| RFmxCdma2kMXChp | Represents the CHP measurement. |
| RFmxCdma2kMXChpConfiguration | Provides methods to configure the CHP measurement. |
| RFmxCdma2kMXChpResults | Provides methods to fetch and read the CHP measurement results. |
| RFmxCdma2kMXConstants | Specifies constants for I/O terminals. |
| RFmxCdma2kMXModAcc | Represents the ModAcc measurement. |
| RFmxCdma2kMXModAccConfiguration | Provides methods to configure the ModAcc measurement. |
| RFmxCdma2kMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
| RFmxCdma2kMXObw | Represents the OBW measurement. |
| RFmxCdma2kMXObwConfiguration | Provides methods to configure the OBW measurement. |
| RFmxCdma2kMXObwResults | Provides methods to fetch and read the OBW measurement results. |
| RFmxCdma2kMXQevm | Represents the QEVM measurement. |
| RFmxCdma2kMXQevmConfiguration | Provides methods to configure the QEVM measurement. |
| RFmxCdma2kMXQevmResults | Provides methods to fetch and read the QEVM measurement results. |
| RFmxCdma2kMXSem | Represents the SEM measurement. |
| RFmxCdma2kMXSemConfiguration | Provides methods to configure the SEM measurement. |
| RFmxCdma2kMXSemResults | Provides methods to fetch and read the SEM measurement results. |
| RFmxCdma2kMXSlotPhase | Represents the SlotPhase measurement. |
| RFmxCdma2kMXSlotPhaseConfiguration | Provides methods to configure the SlotPhase measurement. |
| RFmxCdma2kMXSlotPhaseResults | Provides methods to fetch and read the SlotPhase measurement results. |
| RFmxCdma2kMXSlotPower | Represents the SlotPower measurement. |
| RFmxCdma2kMXSlotPowerConfiguration | Provides methods to configure the SlotPower measurement. |
| RFmxCdma2kMXSlotPowerResults | Provides methods to fetch and read the SlotPower measurement results. |
| RFmxCdma2kMXSubObject | Represents members that are common to all sub-object of RFmxCdma2kMX classes. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxCdma2kMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
| RFmxCdma2kMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
| RFmxCdma2kMXAcpFftOverlapMode | Specifies how the FFT overlap is applied to the acquired samples. The default Value is Disabled. |
| RFmxCdma2kMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is used only if you set the SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod) method to DynamicRange. |
| RFmxCdma2kMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |
| RFmxCdma2kMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxCdma2kMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxCdma2kMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxCdma2kMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxCdma2kMXBranch | Specifies the branch on which a specific user-defined channel is mapped. This method is used only when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method. |
| RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
| RFmxCdma2kMXCdaIQOffsetRemovalEnabled | Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
| RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
| RFmxCdma2kMXCdaMeasurementChannelBranch | Specifies the branch of a channel subject to channel specific analysis. |
| RFmxCdma2kMXCdaPowerUnit | Specifies the measurement unit of the measured code domain power results. |
| RFmxCdma2kMXCdaReceiveFilterEnabled | Specifies whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered. |
| RFmxCdma2kMXCdaSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxCdma2kMXCdaSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| RFmxCdma2kMXChannelConfigurationMode | Specifies whether to detect the channels automatically or to use a specified channel configuration. |
| RFmxCdma2kMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |
| RFmxCdma2kMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
| RFmxCdma2kMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxCdma2kMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxCdma2kMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxCdma2kMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to DigitalEdge. |
| RFmxCdma2kMXIQPowerEdgeTriggerLevelType | Specifies the reference for the IQ Power Edge Level Type method. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |
| RFmxCdma2kMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |
| RFmxCdma2kMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| RFmxCdma2kMXLinkDirection | Specifies the direction for which the frequency is calculated. Only Uplink is supported. |
| RFmxCdma2kMXMeasurementTypes | Specifies the type of measurement. |
| RFmxCdma2kMXModAccDetectedBranch | Returns the branch of the detected channel. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the branch of the configured channel.Use "channel(n)" as the Selector Strings to read this method. |
| RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before an EVM measurement. |
| RFmxCdma2kMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before an EVM measurement. |
| RFmxCdma2kMXModAccIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before an EVM measurement. |
| RFmxCdma2kMXModAccMultiCarrierFilterEnabled | Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers. |
| RFmxCdma2kMXModAccPeakActiveCdeBranch | Returns the branch of the channel corresponding to the value that the GetPeakActiveCde(string, out double) method returns. |
| RFmxCdma2kMXModAccPeakCdeBranch | Returns the branch corresponding to the value that the GetPeakCde(string, out double) method returns. |
| RFmxCdma2kMXModAccReceiveFilterEnabled | Specifies whether to enable the received filter for the ModAcc measurement. |
| RFmxCdma2kMXModAccSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxCdma2kMXModAccSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| RFmxCdma2kMXObwAveragingEnabled | Specifies whether to enable averaging for the OBW measurement. |
| RFmxCdma2kMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| RFmxCdma2kMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxCdma2kMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxCdma2kMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxCdma2kMXPropertyId | Specifies all the attribute identifiers. |
| RFmxCdma2kMXQevmAveragingEnabled | Specifies whether to enable averaging for the QEVM measurement. |
| RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabled | Specifies whether to remove I/Q gain imbalance before QEVM measurement. |
| RFmxCdma2kMXQevmIQOffsetRemovalEnabled | Specifies whether to remove I/Q offset before QEVM measurement. |
| RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled | Specifies whether to remove I/Q quadrature error before QEVM measurement. |
| RFmxCdma2kMXQevmReceiveFilterEnabled | Specifies whether to enable the received filter for the QEVM measurement. |
| RFmxCdma2kMXQevmSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxCdma2kMXRadioConfiguration | Specifies the radio configuration for the channel. |
| RFmxCdma2kMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |
| RFmxCdma2kMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
| RFmxCdma2kMXSemLowerOffsetMeasurementStatus | Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result. |
| RFmxCdma2kMXSemMeasurementStatus | Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. |
| RFmxCdma2kMXSemOffsetRbwFilterType | Returns the type of RBW filter used to sweep the offset segment. |
| RFmxCdma2kMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxCdma2kMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result. |
| RFmxCdma2kMXSlotPhaseReceiveFilterEnabled | Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. |
| RFmxCdma2kMXSlotPhaseSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxCdma2kMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |
| RFmxCdma2kMXSlotPowerReceiveFilterEnabled | Specifies whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |
| RFmxCdma2kMXSlotPowerSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxCdma2kMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |
| RFmxCdma2kMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxCdma2kMXTriggerType | Specifies the trigger type. |

#### Delegates

None

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension-getcdma2ksignalconfiguration__this-string.html language=enus -->
## TOPIC 00310: GetCdma2kSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension-getcdma2ksignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension-getcdma2ksignalconfiguration__this-string.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a CDMA2k signal configuration for specified signal name. Existing CDMA2k signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxCdma2kMX GetCdma2kSignalConfiguration(this RFmxInstrMX instrSession, string signalName

### GetCdma2kSignalConfiguration(this RFmxInstrMX, string)

Creates a CDMA2k signal configuration for specified signal name. Existing CDMA2k signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxCdma2kMX](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx.html) GetCdma2kSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxCdma2kMX.

Parent topic:

RFmxCdma2kMXExtension Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension-getcdma2ksignalconfiguration__this.html language=enus -->
## TOPIC 00311: GetCdma2kSignalConfiguration(this RFmxInstrMX)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension-getcdma2ksignalconfiguration__this.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension-getcdma2ksignalconfiguration__this.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new default CDMA2k signal configuration if it doesn't exist; otherwise, it returns the existing default CDMA2k signal configuration. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxCdma2kMX GetCdma2kSignalConfiguration(this RFmxInstrMX instrSession)ParametersNameTypeDesc

### GetCdma2kSignalConfiguration(this RFmxInstrMX)

Creates a new default CDMA2k signal configuration if it doesn't exist; otherwise, it returns the existing default CDMA2k signal configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxCdma2kMX](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx.html) GetCdma2kSignalConfiguration(this RFmxInstrMX instrSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |

#### Returns

Returns an object of type RFmxCdma2kMX.

Parent topic:

RFmxCdma2kMXExtension Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension.html language=enus -->
## TOPIC 00312: RFmxCdma2kMXExtension Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxcdma2kmxextension.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides extension methods to create CDMA2k signal configuration. These methods are added to RFmxInstrMX class. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic class RFmxCdma2kMXExtensionRemarksFor more information about RFmx Instruments, refer to the RFmx Instruments Help.Th

### RFmxCdma2kMXExtension Class

Provides extension methods to create CDMA2k signal configuration. These methods are added to RFmxInstrMX class.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public class RFmxCdma2kMXExtension

#### Remarks

For more information about RFmx Instruments, refer to the RFmx Instruments Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetCdma2kSignalConfiguration(this RFmxInstrMX, string) | Creates a CDMA2k signal configuration for specified signal name. Existing CDMA2k signal configuration is returned if specified signal name exists. |
| GetCdma2kSignalConfiguration(this RFmxInstrMX) | Creates a new default CDMA2k signal configuration if it doesn't exist; otherwise, it returns the existing default CDMA2k signal configuration. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00313: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxCdma2kMXExtensionProvides extension methods to create CDMA2k signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxCdma2kMXExtension | Provides extension methods to create CDMA2k signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None
