# NI DOCUMENT BUNDLE: rfmxlte-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxlte-dotnet-api-ref start=251 end=318 -->
<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-gettotalaggregatedpower__string-out.html language=enus -->
## TOPIC 00251: GetTotalAggregatedPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-gettotalaggregatedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-gettotalaggregatedpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetTotalAggregatedPower(string selectorSt

### GetTotalAggregatedPower(string, out double)

Gets the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetTotalAggregatedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsTotalAggregatedPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00252: GetUpperOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper (positive) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is pe

### GetUpperOffsetAbsoluteIntegratedPower(string, out double)

Gets the upper (positive) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the upper (positive) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00253: GetUpperOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginabsolutepower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment i

### GetUpperOffsetMarginAbsolutePower(string, out double)

Gets the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginAbsolutePower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginfrequency__string-out.html language=enus -->
## TOPIC 00254: GetUpperOffsetMarginFrequency(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginfrequency__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the margin occurs in the upper (positive) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is tr

### GetUpperOffsetMarginFrequency(string, out double)

Gets the frequency at which the margin occurs in the upper (positive) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetMarginFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginFrequency](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the margin occurs in the upper (positive) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00255: GetUpperOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmarginrelativepower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521

### GetUpperOffsetMarginRelativePower(string, out double)

Gets the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginRelativePower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00256: GetUpperOffsetMeasurementStatus(string, out RFmxLteMXSemUpperOffsetMeasurementStatus)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetmeasurementstatus__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in th

### GetUpperOffsetMeasurementStatus(string, out RFmxLteMXSemUpperOffsetMeasurementStatus)

Gets the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetMeasurementStatus(string selectorString, out RFmxLteMXSemUpperOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMeasurementStatus](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxLteMXSemUpperOffsetMeasurementStatus | Upon return, contains the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00257: GetUpperOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetpeakfrequency__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset s

### GetUpperOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetPeakFrequency](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00258: GetUpperOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power in the upper (positive) offset segment relative to the total aggregated power. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetUpperOffsetRelativeIntegratedPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsUpperOffsetRelativeInte

### GetUpperOffsetRelativeIntegratedPower(string, out double)

Gets the power in the upper (positive) offset segment relative to the total aggregated power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativeIntegratedPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power in the upper (positive) offset segment relative to the total aggregated power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00259: GetUpperOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getupperoffsetrelativepeakpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the

### GetUpperOffsetRelativePeakPower(string, out double)

Gets the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetUpperOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativePeakPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults.html language=enus -->
## TOPIC 00260: RFmxLteMXSemResults Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SEM measurement results. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSemResults : RFmxLteMXSubObjectPropertiesNameDescriptionComponentCarrierGets the RFmxLteMXSemComponentCarrierResults instance that provid

### RFmxLteMXSemResults Class

Provides methods to fetch and read the SEM measurement results.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSemResults : RFmxLteMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| ComponentCarrier | Gets the RFmxLteMXSemComponentCarrierResults instance that provides methods to fetch and read the SEM Component Carrier results. |

#### Methods

| Name | Description |
| --- | --- |
| FetchLowerOffsetMargin(string, double, out RFmxLteMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status, margin, frequency at margin, and the absolute and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchLowerOffsetMarginArray(string, double, ref RFmxLteMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchMeasurementStatus(string, double, out RFmxLteMXSemMeasurementStatus) | Returns the overall measurement status based on the standard mask type that you configure. |
| FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >) | Fetches the spectrum used for the SEM measurement. |
| FetchSubblockMeasurement(string, double, out double, out double, out double) | Returns the power, integration bandwidth and center frequency of the subblock. Use "subblock(n)" as the selector string to read results from this method. |
| FetchTotalAggregatedPower(string, double, out double) | Returns the sum of powers of all subblocks. |
| FetchUpperOffsetMargin(string, double, out RFmxLteMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchUpperOffsetMarginArray(string, double, ref RFmxLteMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the total absolute and relative powers, peak, absolute, and relative powers, and frequency at peak absolute power of upper offset segment. The relative power is relative to total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information. |
| GetLowerOffsetAbsoluteIntegratedPower(string, out double) | Gets the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetAbsolutePeakPower(string, out double) | Gets the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetMargin(string, out double) | Gets the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetMarginAbsolutePower(string, out double) | Gets the power at which the margin occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetMarginFrequency(string, out double) | Gets the frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetMarginRelativePower(string, out double) | Gets the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetMeasurementStatus(string, out RFmxLteMXSemLowerOffsetMeasurementStatus) | Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type method. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetRelativeIntegratedPower(string, out double) | Gets the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetLowerOffsetRelativePeakPower(string, out double) | Gets the peak power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetMeasurementStatus(string, out RFmxLteMXSemMeasurementStatus) | Gets the overall measurement status based on the standard mask type that you configure in the SEM Standard Mask Type method. |
| GetSubblockCenterFrequency(string, out double) | Gets the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. |
| GetSubblockIntegrationBandwidth(string, out double) | Gets the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. |
| GetSubblockPower(string, out double) | Gets the power measured over the integration bandwidth of the subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
| GetTotalAggregatedPower(string, out double) | Gets the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. |
| GetUpperOffsetAbsoluteIntegratedPower(string, out double) | Gets the upper (positive) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetAbsolutePeakPower(string, out double) | Gets the power in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetMargin(string, out double) | Gets the margin from the absolute limit mask for the upper (positive) offset. The Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetMarginAbsolutePower(string, out double) | Gets the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetMarginFrequency(string, out double) | Gets the frequency at which the margin occurs in the upper (positive) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetMarginRelativePower(string, out double) | Gets the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetMeasurementStatus(string, out RFmxLteMXSemUpperOffsetMeasurementStatus) | Gets the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |
| GetUpperOffsetRelativeIntegratedPower(string, out double) | Gets the power in the upper (positive) offset segment relative to the total aggregated power. |
| GetUpperOffsetRelativePeakPower(string, out double) | Gets the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemsidelinkmasktype.html language=enus -->
## TOPIC 00261: RFmxLteMXSemSidelinkMaskType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemsidelinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemsidelinkmasktype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about

### RFmxLteMXSemSidelinkMaskType Enumeration

Specifies the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the *3GPP 36.521* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSemSidelinkMaskType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| General_NS01 | 0 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.1G.1.5-1 and Table 6.6.2.1G.3.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS33_Or_NS34 | 1 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.2G.1.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| Custom | 5 | You need to configure the SetNumberOfOffsets(string, int), SetOffsetStartFrequency(string, double), SetOffsetStopFrequency(string, double), SetOffsetAbsoluteLimitStart(string, double), SetOffsetAbsoluteLimitStop(string, double), SetOffsetSideband(string, RFmxLteMXSemOffsetSideband), SetOffsetRbwFilterBandwidth(string, double), SetOffsetRbwFilterType(string, RFmxLteMXSemOffsetRbwFilterType), and SetOffsetBandwidthIntegral(string, int) properties for each offset. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemsweeptimeauto.html language=enus -->
## TOPIC 00262: RFmxLteMXSemSweepTimeAuto Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemsweeptimeauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSemSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The measuremen

### RFmxLteMXSemSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSemSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemuplinkmasktype.html language=enus -->
## TOPIC 00263: RFmxLteMXSemUplinkMaskType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemuplinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemuplinkmasktype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spectrum emission mask used in the measurement for uplink. Each mask type refers to a different Network Signalled (NS) value. General_CAClassB, CANS04, CANCNS01, CANS09, and CANS10 refers to the carrier aggregation case. You must set the mask type to Custom to configure the custom offs

### RFmxLteMXSemUplinkMaskType Enumeration

Specifies the spectrum emission mask used in the measurement for uplink. Each mask type refers to a different Network Signalled (NS) value. General_CAClassB, CANS04, CANCNS01, CANS09, and CANS10 refers to the carrier aggregation case. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2.1 of the *3GPP 36.521* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSemUplinkMaskType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| General_NS01 | 0 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.5-1, 6.6.2.1A.1.5-2, 6.6.2.1A.1.5-3, and 6.6.2.1A.5-4 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS03_Or_NS11_Or_NS20_Or_NS21 | 1 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS04 | 2 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS06_Or_NS07 | 3 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| CANS04 | 4 | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.6.2.2A.1.5.1-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. This mask applies only for aggregated carriers. |
| Custom | 5 | You need to configure the SetNumberOfOffsets(string, int), SetOffsetStartFrequency(string, double), SetOffsetStopFrequency(string, double), SetOffsetAbsoluteLimitStart(string, double), SetOffsetAbsoluteLimitStop(string, double), SetOffsetSideband(string, RFmxLteMXSemOffsetSideband), SetOffsetRbwFilterBandwidth(string, double), SetOffsetRbwFilterType(string, RFmxLteMXSemOffsetRbwFilterType), and SetOffsetBandwidthIntegral(string, int) properties for each offset. |
| General_CAClassB | 6 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.1A.1.5-3 and 6.6.2.1A.1.5-4 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| CANCNS01 | 7 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.2A.3.5-1 and 6.6.2.2A.3.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS27_Or_NS43 | 8 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.2.5-1 in section 6.6.2.2.5 of the 3GPP TS 36.101-1 specification. |
| NS35 | 9 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.2.5.5-1 in section 6.6.2.2.5.5 of the 3GPP TS 36.521-1 specification. |
| NS28 | 10 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.2.6-1 in section 6.6.2.2.6 of the 3GPP TS 36.101-1 specification. |
| CANS09 | 11 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.2A.2-1 in section 6.6.2.2A.2, and Table 6.6.2.2A.3-1 in section 6.6.2.2A.3 of the 3GPP TS 36.101-1 specification. |
| CANS10 | 12 | The measurement selects offset frequencies and limits for the SEM as defined in Table 6.6.2.2A.4-1 in section 6.6.2.2A.4 of the 3GPP TS 36.101-1 specification. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemupperoffsetmeasurementstatus.html language=enus -->
## TOPIC 00264: RFmxLteMXSemUpperOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemupperoffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemupperoffsetmeasurementstatus.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in

### RFmxLteMXSemUpperOffsetMeasurementStatus Enumeration

Returns the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSemUpperOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | Indicates that the measurement has failed. |
| Pass | 1 | Indicates that the measurement has passed. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphase-configuration.html language=enus -->
## TOPIC 00265: Configuration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphase-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphase-configuration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXSlotPhaseConfiguration Configuration { get; }

### Configuration

Gets the [RFmxLteMXSlotPhaseConfiguration](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration.html) instance that provides methods to configure the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXSlotPhaseConfiguration](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration.html) Configuration { get; }

Parent topic:

RFmxLteMXSlotPhase Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphase-results.html language=enus -->
## TOPIC 00266: Results

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphase-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphase-results.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXSlotPhaseResults Results { get; }

### Results

Gets the [RFmxLteMXSlotPhaseResults](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults.html) instance that provides methods to fetch and read the SlotPhase measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXSlotPhaseResults](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults.html) Results { get; }

Parent topic:

RFmxLteMXSlotPhase Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphase.html language=enus -->
## TOPIC 00267: RFmxLteMXSlotPhase Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphase.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SlotPhase measurement. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSlotPhase : RFmxLteMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxLteMXSlotPhaseConfiguration instance that provides methods to configure the SlotPh

### RFmxLteMXSlotPhase Class

Represents the SlotPhase measurement.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSlotPhase : RFmxLteMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxLteMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. |
| Results | Gets the RFmxLteMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphasecommonclocksourceenabled.html language=enus -->
## TOPIC 00268: RFmxLteMXSlotPhaseCommonClockSourceEnabled Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphasecommonclocksourceenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphasecommonclocksourceenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSlotPhaseCommonC

### RFmxLteMXSlotPhaseCommonClockSourceEnabled Enumeration

Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSlotPhaseCommonClockSourceEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The Sample Clock error is estimated independently. |
| True | 1 | The Sample Clock error is estimated from carrier frequency offset. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxltemxslotphasesynchronizationmode-int-int.html language=enus -->
## TOPIC 00269: ConfigureSynchronizationModeAndInterval(string, RFmxLteMXSlotPhaseSynchronizationMode, int, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxltemxslotphasesynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxltemxslotphasesynchronizationmode-int-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronizationhronizationMode, measurementOffset, and measurementLength parameters of SlotPhase measurement.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxLteMXSlotPhaseSynchronizationMode synchronizationMo

### ConfigureSynchronizationModeAndInterval(string, RFmxLteMXSlotPhaseSynchronizationMode, int, int)

Configures the *synchronizationhronizationMode*, *measurementOffset*, and *measurementLength* parameters of SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxLteMXSlotPhaseSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxLteMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the Synchronization Mode parameter. This value is expressed in slots. |
| measurementLength | int | Specifies the number of slots to be measured. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00270: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseAllTracesEnabled attribute. The d

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getcommonclocksourceenabled__string-out.html language=enus -->
## TOPIC 00271: GetCommonClockSourceEnabled(string, out RFmxLteMXSlotPhaseCommonClockSourceEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getcommonclocksourceenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getcommonclocksourceenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetCommonClockSourceEnabled(str

### GetCommonClockSourceEnabled(string, out RFmxLteMXSlotPhaseCommonClockSourceEnabled)

Gets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetCommonClockSourceEnabled(string selectorString, out RFmxLteMXSlotPhaseCommonClockSourceEnabled value)

#### Remarks

This method gets the value of [SlotPhaseCommonClockSourceEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxslotphasecommonclocksourceenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSlotPhaseCommonClockSourceEnabled | Upon return, contains whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getexclusionperiodenabled__string-out.html language=enus -->
## TOPIC 00272: GetExclusionPeriodEnabled(string, out RFmxLteMXSlotPhaseExclusionPeriodEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getexclusionperiodenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getexclusionperiodenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. SyntaxNamespace: NationalInstruments

### GetExclusionPeriodEnabled(string, out RFmxLteMXSlotPhaseExclusionPeriodEnabled)

Gets whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the *3GPP 36.521-1* specification for more information about the exclusion.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetExclusionPeriodEnabled(string selectorString, out RFmxLteMXSlotPhaseExclusionPeriodEnabled value)

#### Remarks

This method gets the value of [SlotPhaseExclusionPeriodEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseexclusionperiodenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSlotPhaseExclusionPeriodEnabled | Upon return, contains whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00273: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseMeasurementEnabled attribute. The default value is FALSE.ParametersNameTypeDescription

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00274: GetMeasurementLength(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of slots to be measured. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPhaseMeasurementLength attribute. The default value is 20.Parameters

### GetMeasurementLength(string, out int)

Gets the number of slots to be measured. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of slots to be measured. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00275: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasure

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setsynchronizationmode__string-rfmxltemxslotphasesynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0. Valid values are 0 to 19, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00276: GetSpectrumInverted(string, out RFmxLteMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSpectrumInverted(string selectorString, out RFmxLteMXSlotPhaseSpectrumInverted

### GetSpectrumInverted(string, out RFmxLteMXSlotPhaseSpectrumInverted)

Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSpectrumInverted(string selectorString, out RFmxLteMXSlotPhaseSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-ltemx-rfmxltemxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSlotPhaseSpectrumInverted | Upon return, contains whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getsynchronizationmode__string-out.html language=enus -->
## TOPIC 00277: GetSynchronizationMode(string, out RFmxLteMXSlotPhaseSynchronizationMode)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getsynchronizationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-getsynchronizationmode__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSynchronizationMode(string selectorString, out RFmxLteMXSlotPhaseSynchronizationMode value)RemarksThis method gets the value of SlotPhaseSynchronizationMode att

### GetSynchronizationMode(string, out RFmxLteMXSlotPhaseSynchronizationMode)

Gets whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSynchronizationMode(string selectorString, out RFmxLteMXSlotPhaseSynchronizationMode value)

#### Remarks

This method gets the value of [SlotPhaseSynchronizationMode](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Frame](nationalinstruments-rfmx-ltemx-rfmxltemxslotphasesynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSlotPhaseSynchronizationMode | Upon return, contains whether the measurement is performed from the frame or the slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00278: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPhaseAllTracesEnabled attribute. The defau

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setcommonclocksourceenabled__string-rfmxltemxslotphasecommonclocksourceenabled.html language=enus -->
## TOPIC 00279: SetCommonClockSourceEnabled(string, RFmxLteMXSlotPhaseCommonClockSourceEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setcommonclocksourceenabled__string-rfmxltemxslotphasecommonclocksourceenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setcommonclocksourceenabled__string-rfmxltemxslotphasecommonclocksourceenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetCommonClockSourceEnabled(str

### SetCommonClockSourceEnabled(string, RFmxLteMXSlotPhaseCommonClockSourceEnabled)

Sets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetCommonClockSourceEnabled(string selectorString, RFmxLteMXSlotPhaseCommonClockSourceEnabled value)

#### Remarks

This method sets the value of [SlotPhaseCommonClockSourceEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxslotphasecommonclocksourceenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXSlotPhaseCommonClockSourceEnabled | Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setexclusionperiodenabled__string-rfmxltemxslotphaseexclusionperiodenabled.html language=enus -->
## TOPIC 00280: SetExclusionPeriodEnabled(string, RFmxLteMXSlotPhaseExclusionPeriodEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setexclusionperiodenabled__string-rfmxltemxslotphaseexclusionperiodenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setexclusionperiodenabled__string-rfmxltemxslotphaseexclusionperiodenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. SyntaxNamespace: NationalInstruments

### SetExclusionPeriodEnabled(string, RFmxLteMXSlotPhaseExclusionPeriodEnabled)

Sets whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the *3GPP 36.521-1* specification for more information about the exclusion.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetExclusionPeriodEnabled(string selectorString, RFmxLteMXSlotPhaseExclusionPeriodEnabled value)

#### Remarks

This method sets the value of [SlotPhaseExclusionPeriodEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseexclusionperiodenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXSlotPhaseExclusionPeriodEnabled | Specifies whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00281: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPhaseMeasurementEnabled attribute. The default value is FALSE.ParametersNameTypeDescriptionsele

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00282: SetMeasurementLength(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of slots to be measured. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of SlotPhaseMeasurementLength attribute. The default value is 20.ParametersName

### SetMeasurementLength(string, int)

Sets the number of slots to be measured. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of slots to be measured. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00283: SetMeasurementOffset(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetMeasure

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setsynchronizationmode__string-rfmxltemxslotphasesynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0. Valid values are 0 to 19, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setspectruminverted__string-rfmxltemxslotphasespectruminverted.html language=enus -->
## TOPIC 00284: SetSpectrumInverted(string, RFmxLteMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setspectruminverted__string-rfmxltemxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setspectruminverted__string-rfmxltemxslotphasespectruminverted.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetSpectrumInverted(string selectorString, RFmxLteMXSlotPhaseSpectrumInverted valu

### SetSpectrumInverted(string, RFmxLteMXSlotPhaseSpectrumInverted)

Sets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetSpectrumInverted(string selectorString, RFmxLteMXSlotPhaseSpectrumInverted value)

#### Remarks

This method sets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-ltemx-rfmxltemxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXSlotPhaseSpectrumInverted | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setsynchronizationmode__string-rfmxltemxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00285: SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setsynchronizationmode__string-rfmxltemxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setsynchronizationmode__string-rfmxltemxslotphasesynchronizationmode.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetSynchronizationMode(string selectorString, RFmxLteMXSlotPhaseSynchronizationMode value)RemarksThis method sets the value of SlotPhaseSynchronizationMode attribu

### SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode)

Sets whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetSynchronizationMode(string selectorString, RFmxLteMXSlotPhaseSynchronizationMode value)

#### Remarks

This method sets the value of [SlotPhaseSynchronizationMode](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Frame](nationalinstruments-rfmx-ltemx-rfmxltemxslotphasesynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration.html language=enus -->
## TOPIC 00286: RFmxLteMXSlotPhaseConfiguration Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SlotPhase measurement. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSlotPhaseConfiguration : RFmxLteMXSubObjectMethodsNameDescriptionConfigureSynchronizationModeAndInterval(string, RFmxLteMXSlotPhaseSynchronizati

### RFmxLteMXSlotPhaseConfiguration Class

Provides methods to configure the SlotPhase measurement.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSlotPhaseConfiguration : RFmxLteMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSynchronizationModeAndInterval(string, RFmxLteMXSlotPhaseSynchronizationMode, int, int) | Configures the synchronizationhronizationMode, measurementOffset, and measurementLength parameters of SlotPhase measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| GetCommonClockSourceEnabled(string, out RFmxLteMXSlotPhaseCommonClockSourceEnabled) | Gets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
| GetExclusionPeriodEnabled(string, out RFmxLteMXSlotPhaseExclusionPeriodEnabled) | Gets whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SlotPhase measurement. |
| GetMeasurementLength(string, out int) | Gets the number of slots to be measured. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) method. |
| GetSpectrumInverted(string, out RFmxLteMXSlotPhaseSpectrumInverted) | Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
| GetSynchronizationMode(string, out RFmxLteMXSlotPhaseSynchronizationMode) | Gets whether the measurement is performed from the frame or the slot boundary. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| SetCommonClockSourceEnabled(string, RFmxLteMXSlotPhaseCommonClockSourceEnabled) | Sets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
| SetExclusionPeriodEnabled(string, RFmxLteMXSlotPhaseExclusionPeriodEnabled) | Sets whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SlotPhase measurement. |
| SetMeasurementLength(string, int) | Sets the number of slots to be measured. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) method. |
| SetSpectrumInverted(string, RFmxLteMXSlotPhaseSpectrumInverted) | Sets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
| SetSynchronizationMode(string, RFmxLteMXSlotPhaseSynchronizationMode) | Sets whether the measurement is performed from the frame or the slot boundary. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseexclusionperiodenabled.html language=enus -->
## TOPIC 00287: RFmxLteMXSlotPhaseExclusionPeriodEnabled Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseexclusionperiodenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseexclusionperiodenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. SyntaxNamespace: NationalInstru

### RFmxLteMXSlotPhaseExclusionPeriodEnabled Enumeration

Specifies whether to exclude some portions of the slots when calculating the phase. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the *3GPP 36.521-1* specification for more information about the exclusion.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSlotPhaseExclusionPeriodEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Phase is calculated on complete slots. |
| True | 1 | Phase is calculated on truncated slots. The power changes at the slot boundaries are detected by the measurement, and the defined 3GPP specification period is excluded from the slots being measured. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchmaximumphasediscontinuity__string-double-out.html language=enus -->
## TOPIC 00288: FetchMaximumPhaseDiscontinuity(string, double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchmaximumphasediscontinuity__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchmaximumphasediscontinuity__string-double-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum value of phase differences at slot boundaries within the measurement interval. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchMaximumPhaseDiscontinuity(string sele

### FetchMaximumPhaseDiscontinuity(string, double, out double)

Fetches the maximum value of phase differences at slot boundaries within the measurement interval. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchMaximumPhaseDiscontinuity(string selectorString, double timeout, out double maximumPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| maximumPhaseDiscontinuity | out double | Upon return, contains the maximum value of phase difference at the slot boundaries within the SetMeasurementLength(string, int). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchmaximumphasediscontinuityarray__string-double-ref.html language=enus -->
## TOPIC 00289: FetchMaximumPhaseDiscontinuityArray(string, double, ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchmaximumphasediscontinuityarray__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchmaximumphasediscontinuityarray__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of maximum values of phase differences at slot boundaries within the measurement interval. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchMaximumPhaseDiscontinuityArray(string selectorString,

### FetchMaximumPhaseDiscontinuityArray(string, double, ref double[])

Fetches the array of maximum values of phase differences at slot boundaries within the measurement interval. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchMaximumPhaseDiscontinuityArray(string selectorString, double timeout, ref double[] maximumPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| maximumPhaseDiscontinuity | ref double[] | Upon return, contains the array of maximum values of phase difference at the slot boundaries within the SetMeasurementLength(string, int). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchphasediscontinuities__string-double-ref.html language=enus -->
## TOPIC 00290: FetchPhaseDiscontinuities(string, double, ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchphasediscontinuities__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchphasediscontinuities__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of phase differences at slot boundaries within measurement interval.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] slotPhaseDiscontinuity)ParametersNameTypeDescriptionselectorStringstringSpecif

### FetchPhaseDiscontinuities(string, double, ref double[])

Fetches the array of phase differences at slot boundaries within measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] slotPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| slotPhaseDiscontinuity | ref double[] | Upon return, contains the array of phase differences at the slot boundaries within the SetMeasurementLength(string, int). This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchsamplephaseerror__string-double-ref.html language=enus -->
## TOPIC 00291: FetchSamplePhaseError(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchsamplephaseerror__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchsamplephaseerror__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the sample phase error trace for the SlotPhase measurement. At each sample, this is the phase difference between received signal and locally generated reference signal.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSamplePhaseError(string selectorString, double timeout, ref A

### FetchSamplePhaseError(string, double, ref AnalogWaveform< float >)

Fetches the sample phase error trace for the SlotPhase measurement. At each sample, this is the phase difference between received signal and locally generated reference signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSamplePhaseError(string selectorString, double timeout, ref AnalogWaveform< float > samplePhaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| samplePhaseError | ref AnalogWaveform< float > | Upon return, contains the sample phase error traces. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchsamplephaseerrorlinearfittrace__string-double-ref.html language=enus -->
## TOPIC 00292: FetchSamplePhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchsamplephaseerrorlinearfittrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-fetchsamplephaseerrorlinearfittrace__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the sample phase error linear fit trace for the SlotPhase measurement. The linear fit is over the array of phase differences at each sample between the received signal and the locally generated reference signal.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSamplePhaseErrorLi

### FetchSamplePhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

Fetches the sample phase error linear fit trace for the SlotPhase measurement. The linear fit is over the array of phase differences at each sample between the received signal and the locally generated reference signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSamplePhaseErrorLinearFitTrace(string selectorString, double timeout, ref AnalogWaveform< float > samplePhaseErrorLinearFit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| samplePhaseErrorLinearFit | ref AnalogWaveform< float > | Upon return, contains the sample phase error linear fit trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-getmaximumphasediscontinuity__string-out.html language=enus -->
## TOPIC 00293: GetMaximumPhaseDiscontinuity(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-getmaximumphasediscontinuity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults-getmaximumphasediscontinuity__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of phase difference at the slot boundaries within the SetMeasurementLength(string, int). This values is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMaximumPhaseDiscontinuity(string selectorString, out double value)RemarksThis method gets

### GetMaximumPhaseDiscontinuity(string, out double)

Gets the maximum value of phase difference at the slot boundaries within the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseconfiguration-setmeasurementlength__string-int.html). This values is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMaximumPhaseDiscontinuity(string selectorString, out double value)

#### Remarks

This method gets the value of [SlotPhaseResultsMaximumPhaseDiscontinuity](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value of phase difference at the slot boundaries within the SetMeasurementLength(string, int). This values is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults.html language=enus -->
## TOPIC 00294: RFmxLteMXSlotPhaseResults Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphaseresults.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SlotPhase measurement results. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSlotPhaseResults : RFmxLteMXSubObjectMethodsNameDescriptionFetchMaximumPhaseDiscontinuity(string, double, out double)Fetches the ma

### RFmxLteMXSlotPhaseResults Class

Provides methods to fetch and read the SlotPhase measurement results.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSlotPhaseResults : RFmxLteMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMaximumPhaseDiscontinuity(string, double, out double) | Fetches the maximum value of phase differences at slot boundaries within the measurement interval. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchMaximumPhaseDiscontinuityArray(string, double, ref double[]) | Fetches the array of maximum values of phase differences at slot boundaries within the measurement interval. Use "subblock(n)" as the selector string to read results from this method. |
| FetchPhaseDiscontinuities(string, double, ref double[]) | Fetches the array of phase differences at slot boundaries within measurement interval. |
| FetchSamplePhaseError(string, double, ref AnalogWaveform< float >) | Fetches the sample phase error trace for the SlotPhase measurement. At each sample, this is the phase difference between received signal and locally generated reference signal. |
| FetchSamplePhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >) | Fetches the sample phase error linear fit trace for the SlotPhase measurement. The linear fit is over the array of phase differences at each sample between the received signal and the locally generated reference signal. |
| GetMaximumPhaseDiscontinuity(string, out double) | Gets the maximum value of phase difference at the slot boundaries within the SetMeasurementLength(string, int). This values is expressed in degrees. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphasespectruminverted.html language=enus -->
## TOPIC 00295: RFmxLteMXSlotPhaseSpectrumInverted Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphasespectruminverted.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSlotPhaseSpectrumInvertedMembersNameValueDescriptionFalse0The spect

### RFmxLteMXSlotPhaseSpectrumInverted Enumeration

Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSlotPhaseSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum of the measured signal is not inverted. |
| True | 1 | The measured signal is inverted and the measurement corrects the signal by swapping the I and the Q components. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00296: RFmxLteMXSlotPhaseSynchronizationMode Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotphasesynchronizationmode.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSlotPhaseSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary in the acquired signal is detected, and the measurement is performed

### RFmxLteMXSlotPhaseSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSlotPhaseSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(string, int) method, starting at the offset from the boundary specified by the SetMeasurementOffset(string, int) method. When the SetTriggerType(string, RFmxLteMXTriggerType) method is set to Digital, the measurement expects a trigger at the frame boundary. |
| Slot | 1 | The slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length method, starting at the offset from the boundary specified by the SlotPhase Meas Offset method. When the Trigger Type method is set to Digital, the measurement expects a trigger at any slot boundary. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpower.html language=enus -->
## TOPIC 00297: RFmxLteMXSlotPower Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpower.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SlotPower measurement. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSlotPower : RFmxLteMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxLteMXSlotPowerConfiguration instance that provides methods to configure the SlotPo

### RFmxLteMXSlotPower Class

Represents the SlotPower measurement.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSlotPower : RFmxLteMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxLteMXSlotPowerConfiguration instance that provides methods to configure the SlotPower measurement. |
| Results | Gets the RFmxLteMXSlotPowerResults instance that provides methods to fetch and read the SlotPower measurement results. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-configuremeasurementinterval__string-int-int.html language=enus -->
## TOPIC 00298: ConfigureMeasurementInterval(string, int, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-configuremeasurementinterval__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-configuremeasurementinterval__string-int-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurementOffset and measurementLength parameters of SlotPower measurement.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureMeasurementInterval(string selectorString, int measurementOffset, int measurementLength)ParametersNameTypeDescriptionselectorStringstringPass

### ConfigureMeasurementInterval(string, int, int)

Configures the *measurementOffset* and *measurementLength* parameters of SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureMeasurementInterval(string selectorString, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementOffset | int | Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframes. |
| measurementLength | int | Specifies the number of subframes to be measured. This value is expressed in subframes. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00299: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPowerAllTracesEnabled attribute. The d

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPowerAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00300: GetMeasurementLength(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of subframes to be measured. This value is expressed in subframe. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPowerMeasurementLength attribute. The default value is 10.Par

### GetMeasurementLength(string, out int)

Gets the number of subframes to be measured. This value is expressed in subframe.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPowerMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of subframes to be measured. This value is expressed in subframe. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00301: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasurementOffset(string selectorString, out int value)RemarksThis method gets the value of SlotPow

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPowerMeasurementOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00302: GetSpectrumInverted(string, out RFmxLteMXSlotPowerSpectrumInverted)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSpectrumInverted(string selectorString, out RFmxLteMXSlotPowerSpectrumInverted

### GetSpectrumInverted(string, out RFmxLteMXSlotPowerSpectrumInverted)

Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSpectrumInverted(string selectorString, out RFmxLteMXSlotPowerSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPowerSpectrumInverted](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSlotPowerSpectrumInverted | Upon return, contains whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00303: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPowerAllTracesEnabled attribute. The defau

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPowerAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setcommonclocksourceenabled__string-rfmxltemxslotpowercommonclocksourceenabled.html language=enus -->
## TOPIC 00304: SetCommonClockSourceEnabled(string, RFmxLteMXSlotPowerCommonClockSourceEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setcommonclocksourceenabled__string-rfmxltemxslotpowercommonclocksourceenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setcommonclocksourceenabled__string-rfmxltemxslotpowercommonclocksourceenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetCommo

### SetCommonClockSourceEnabled(string, RFmxLteMXSlotPowerCommonClockSourceEnabled)

Sets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetCommonClockSourceEnabled(string selectorString, RFmxLteMXSlotPowerCommonClockSourceEnabled value)

#### Remarks

This method sets the value of [SlotPowerCommonClockSourceEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxslotpowercommonclocksourceenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXSlotPowerCommonClockSourceEnabled | Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00305: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPowerMeasurementEnabled attribute. The default value is FALSE.ParametersNameTypeDescriptionsele

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPowerMeasurementEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00306: SetMeasurementOffset(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetMeasurementOffset(string selectorString, int value)RemarksThis method sets the value of SlotPowerMe

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPowerMeasurementOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration.html language=enus -->
## TOPIC 00307: RFmxLteMXSlotPowerConfiguration Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerconfiguration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SlotPower measurement. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSlotPowerConfiguration : RFmxLteMXSubObjectMethodsNameDescriptionConfigureMeasurementInterval(string, int, int)Configures the measurementOffset

### RFmxLteMXSlotPowerConfiguration Class

Provides methods to configure the SlotPower measurement.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSlotPowerConfiguration : RFmxLteMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureMeasurementInterval(string, int, int) | Configures the measurementOffset and measurementLength parameters of SlotPower measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. |
| GetCommonClockSourceEnabled(string, out RFmxLteMXSlotPowerCommonClockSourceEnabled) | Gets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SlotPower measurement. |
| GetMeasurementLength(string, out int) | Gets the number of subframes to be measured. This value is expressed in subframe. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. |
| GetSpectrumInverted(string, out RFmxLteMXSlotPowerSpectrumInverted) | Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. |
| SetCommonClockSourceEnabled(string, RFmxLteMXSlotPowerCommonClockSourceEnabled) | Sets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SlotPower measurement. |
| SetMeasurementLength(string, int) | Sets the number of subframes to be measured. This value is expressed in subframe. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. |
| SetSpectrumInverted(string, RFmxLteMXSlotPowerSpectrumInverted) | Sets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerresults-fetchpowers__string-double-ref-ref.html language=enus -->
## TOPIC 00308: FetchPowers(string, double, ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerresults-fetchpowers__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerresults-fetchpowers__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of Subframe Power and the Subframe Power Delta parameters over the measurement interval. A NaN is returned as subframe power delta, when the preceding slot is not occupied.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPowers(string selectorString, double timeout, r

### FetchPowers(string, double, ref double[], ref double[])

Fetches the array of Subframe Power and the Subframe Power Delta parameters over the measurement interval. A NaN is returned as subframe power delta, when the preceding slot is not occupied.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPowers(string selectorString, double timeout, ref double[] subframePower, ref double[] subframePowerDelta)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| subframePower | ref double[] | Upon return, contains the array of subframe power values over the measurement interval. The values are expressed in dBm. |
| subframePowerDelta | ref double[] | Upon return, contains the array of subframe power delta values over the measurement interval. Subframe power delta values are the power difference between the two consecutive subframes. The values are expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSlotPowerResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerspectruminverted.html language=enus -->
## TOPIC 00309: RFmxLteMXSlotPowerSpectrumInverted Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxslotpowerspectruminverted.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSlotPowerSpectrumInvertedMembersNameValueDescriptionFalse0The spect

### RFmxLteMXSlotPowerSpectrumInverted Enumeration

Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSlotPowerSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum of the measured signal is not inverted. |
| True | 1 | The measured signal is inverted and the measurement corrects the signal by swapping the I and the Q components. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsrsmaximumupptsenabled.html language=enus -->
## TOPIC 00310: RFmxLteMXSrsMaximumUpPtsEnabled Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsrsmaximumupptsenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsrsmaximumupptsenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSrsMaximumUpPtsEnabledMembersNameV

### RFmxLteMXSrsMaximumUpPtsEnabled Enumeration

Specifies SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of *3GPP 36.211* specification for more details.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSrsMaximumUpPtsEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | In special subframe, SRS is transmitted in RBs specified by SRS bandwidth configurations. |
| True | 1 | In special subframe, SRS is transmitted in all possible RBs. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxtxpconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00311: GetMeasurementOffset(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxtxpconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxtxpconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasurementOffset(string selectorString, out double value)RemarksThis method gets the value of TxpMeasurementO

### GetMeasurementOffset(string, out double)

Gets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpMeasurementOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxtxpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00312: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxtxpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxtxpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism inside TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of TxpNumberOfAnalysisThreads attribute.The number of threads mu

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism inside TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [TxpNumberOfAnalysisThreads](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.The number of threads must range from 1 to the number of physical cores. The default value is 1. The number of threads set used in calculations is not guaranteed. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism inside TXP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-fetchmeasurement__string-double-out-out.html language=enus -->
## TOPIC 00313: FetchMeasurement(string, double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-fetchmeasurement__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-fetchmeasurement__string-double-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power and peak power of the the signal over which power measurments are performed. Use "subblock(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchMeasurement(string selectorString, double timeout, out doub

### FetchMeasurement(string, double, out double, out double)

Fetches the average power and peak power of the the signal over which power measurments are performed. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchMeasurement(string selectorString, double timeout, out double averagePowerMean, out double peakPowerMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the RFmxLTE Build Subblock String method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| averagePowerMean | out double | Upon return, contains the average power of the the signal over which power measurments are performed. This value is expressed in dBm. |
| peakPowerMaximum | out double | Upon return, contains the peak power of the the signal over which power measurments are performed. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXTxpResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-fetchpowertrace__string-double-ref.html language=enus -->
## TOPIC 00314: FetchPowerTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-fetchpowertrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-fetchpowertrace__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches power versus time trace.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you do not

### FetchPowerTrace(string, double, ref AnalogWaveform< float >)

Fetches power versus time trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the RFmxLTE Build Signal String method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| power | ref AnalogWaveform< float > | Upon return, contains power versus time trace. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXTxpResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-getpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00315: GetPeakPowerMaximum(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-getpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults-getpeakpowermaximum__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of TxpResultsPeakPowerMaximum attribute.ParametersNameTypeDescriptionselectorStringstringSpecifies a sel

### GetPeakPowerMaximum(string, out double)

Gets the peak power of the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsPeakPowerMaximum](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXTxpResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults.html language=enus -->
## TOPIC 00316: RFmxLteMXTxpResults Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxtxpresults.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the TXP measurement results. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXTxpResults : RFmxLteMXSubObjectMethodsNameDescriptionFetchMeasurement(string, double, out double, out double)Fetches the average power an

### RFmxLteMXTxpResults Class

Provides methods to fetch and read the TXP measurement results.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXTxpResults : RFmxLteMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMeasurement(string, double, out double, out double) | Fetches the average power and peak power of the the signal over which power measurments are performed. Use "subblock(n)" as the selector string to read results from this method. |
| FetchPowerTrace(string, double, ref AnalogWaveform< float >) | Fetches power versus time trace. |
| GetAveragePowerMean(string, out double) | Gets the average power of the acquired signal. |
| GetPeakPowerMaximum(string, out double) | Gets the peak power of the acquired signal. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxuplinkdownlinkconfiguration.html language=enus -->
## TOPIC 00317: RFmxLteMXUplinkDownlinkConfiguration Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxuplinkdownlinkconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxuplinkdownlinkconfiguration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXUplinkDownlinkConfigurationMembersNameValueDescripti

### RFmxLteMXUplinkDownlinkConfiguration Enumeration

Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the *3GPP TS 36.211* specification to configure the LTE frame.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXUplinkDownlinkConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Configuration0 | 0 | The configuration of the LTE frame structure in the TDD duplex mode is 0. |
| Configuration1 | 1 | The configuration of the LTE frame structure in the TDD duplex mode is 1. |
| Configuration2 | 2 | The configuration of the LTE frame structure in the TDD duplex mode is 2. |
| Configuration3 | 3 | The configuration of the LTE frame structure in the TDD duplex mode is 3. |
| Configuration4 | 4 | The configuration of the LTE frame structure in the TDD duplex mode is 4. |
| Configuration5 | 5 | The configuration of the LTE frame structure in the TDD duplex mode is 5. |
| Configuration6 | 6 | The configuration of the LTE frame structure in the TDD duplex mode is 6. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxuplinkgrouphoppingenabled.html language=enus -->
## TOPIC 00318: RFmxLteMXUplinkGroupHoppingEnabled Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxuplinkgrouphoppingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxuplinkgrouphoppingenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXUplinkGroupHoppingEnabledMembersNameValueDescriptionFalse0Th

### RFmxLteMXUplinkGroupHoppingEnabled Enumeration

Specifies whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the *3GPP TS 36.211* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXUplinkGroupHoppingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses zero as the sequence group number for all the slots. |
| True | 1 | Calculates the sequence group number for each slot, as defined in the section 5.5.1.3 of 3GPP 36.211 Specification. |

Parent topic:

NationalInstruments.RFmx.LteMX
