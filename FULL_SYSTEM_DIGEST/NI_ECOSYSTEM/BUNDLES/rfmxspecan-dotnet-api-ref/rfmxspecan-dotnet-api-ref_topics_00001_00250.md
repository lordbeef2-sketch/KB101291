# NI DOCUMENT BUNDLE: rfmxspecan-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-initiate__string-string.html language=enus -->
## TOPIC 00001: Initiate(string, string)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-initiate__string-string.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. To get the status of measurements, you can use the CheckMeasurementStatus(string, out b

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. To get the status of measurements, you can use the [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-specanmx-rfmxspecanmx-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int Initiate(string selectorString, string resultName)

#### Remarks

This method maps to the RFmxSpecAn_Initiate() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising the result name. The result name can either be specified through this input or the resultName parameter.If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-iq.html language=enus -->
## TOPIC 00002: IQ

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-iq.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-iq.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXIQ instance that represents the I/Q measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXIQ IQ { get; }RemarksReturns an object of type RFmxSpecAnMXIQ.

### IQ

Gets the RFmxSpecAnMXIQ instance that represents the I/Q measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXIQ](nationalinstruments-rfmx-specanmx-rfmxspecanmxiq.html) IQ { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXIQ.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-pavt.html language=enus -->
## TOPIC 00003: Pavt

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-pavt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-pavt.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXPavt instance that represents the PAVT measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXPavt Pavt { get; }

### Pavt

Gets the [RFmxSpecAnMXPavt](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavt.html) instance that represents the PAVT measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXPavt](nationalinstruments-rfmx-specanmx-rfmxspecanmxpavt.html) Pavt { get; }

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-phasenoise.html language=enus -->
## TOPIC 00004: PhaseNoise

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-phasenoise.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-phasenoise.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXPhaseNoise instance that represents the PhaseNoise measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXPhaseNoise PhaseNoise { get; }

### PhaseNoise

Gets the [RFmxSpecAnMXPhaseNoise](nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoise.html) instance that represents the PhaseNoise measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXPhaseNoise](nationalinstruments-rfmx-specanmx-rfmxspecanmxphasenoise.html) PhaseNoise { get; }

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-resetattribute__string-rfmxspecanmxpropertyid.html language=enus -->
## TOPIC 00005: ResetAttribute(string, RFmxSpecAnMXPropertyId)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-resetattribute__string-rfmxspecanmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-resetattribute__string-rfmxspecanmxpropertyid.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ResetAttribute(string selectorString, RFmxSpecAnMXPropertyId attributeId)RemarksThis method maps to the RFmxSpecAn_ResetAttribute() function in C.ParametersNameTypeDescriptionselectorStringstringS

### ResetAttribute(string, RFmxSpecAnMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ResetAttribute(string selectorString, RFmxSpecAnMXPropertyId attributeId)

#### Remarks

This method maps to the RFmxSpecAn_ResetAttribute() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string. |
| attributeId | RFmxSpecAnMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-resettodefault__string.html language=enus -->
## TOPIC 00006: ResetToDefault(string)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-resettodefault__string.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ResetToDefault(string selectorString)RemarksThis method maps to the RFmxSpecAn_ResetToDefault() function in C.ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name tha

### ResetToDefault(string)

Resets a signal to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ResetToDefault(string selectorString)

#### Remarks

This method maps to the RFmxSpecAn_ResetToDefault() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-sem.html language=enus -->
## TOPIC 00007: Sem

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-sem.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXSem instance that represents the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXSem Sem { get; }RemarksReturns an object of type RFmxSpecAnMXSem.

### Sem

Gets the RFmxSpecAnMXSem instance that represents the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXSem](nationalinstruments-rfmx-specanmx-rfmxspecanmxsem.html) Sem { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXSem.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-setattributedouble__string-int-double.html language=enus -->
## TOPIC 00008: SetAttributeDouble(string, int, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-setattributedouble__string-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-setattributedouble__string-int-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)RemarksThis method maps to the RFmxSpecAn_SetAttributeF64() function in C.ParametersNameTypeDescriptionselectorStringstri

### SetAttributeDouble(string, int, double)

Sets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)

#### Remarks

This method maps to the RFmxSpecAn_SetAttributeF64() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-setattributeint__string-int-int.html language=enus -->
## TOPIC 00009: SetAttributeInt(string, int, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-setattributeint__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-setattributeint__string-int-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Int attribute. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAttributeInt(string selectorString, int attributeIdentifier, int value)RemarksThis method maps to the RFmxSpecAn_SetAttributeI32() function in C.ParametersNameTypeDescriptionselectorStringstringSpecifi

### SetAttributeInt(string, int, int)

Sets the value of a Int attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAttributeInt(string selectorString, int attributeIdentifier, int value)

#### Remarks

This method maps to the RFmxSpecAn_SetAttributeI32() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmx-setexternalattenuation__string-double.html language=enus -->
## TOPIC 00010: SetExternalAttenuation(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmx-setexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmx-setexternalattenuation__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the RF signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetExternalAttenuation(string selectorString, double value)RemarksWhen you set this method and set the RF Attenuation and IF At

### SetExternalAttenuation(string, double)

Sets the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the RF signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetExternalAttenuation(string selectorString, double value)

#### Remarks

When you set this method and set the RF Attenuation and IF Attenuation values, the appropriate attenuator settings are calculated based on [ConfigureExternalAttenuation(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmx-configureexternalattenuation__string-double.html) and [ConfigureReferenceLevel(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmx-configurereferencelevel__string-double.html) values. In this case, RFmxSpecAn interprets the reference level as the maximum expected power level of the signal at the input of the external gain device. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This method maps to the RFmxSpecAn_SetExternalAttenuation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the attenuation, in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMX Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-configurepowerunits__string-rfmxspecanmxacppowerunits.html language=enus -->
## TOPIC 00011: ConfigurePowerUnits(string, RFmxSpecAnMXAcpPowerUnits)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-configurepowerunits__string-rfmxspecanmxacppowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-configurepowerunits__string-rfmxspecanmxacppowerunits.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the units for the absolute power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigurePowerUnits(string selectorString, RFmxSpecAnMXAcpPowerUnits powerUnits)RemarksThis method maps to the RFmxSpecAn_ACPCfgPowerUnits() function in C.ParametersNameTypeDescriptionselectorSt

### ConfigurePowerUnits(string, RFmxSpecAnMXAcpPowerUnits)

Configures the units for the absolute power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigurePowerUnits(string selectorString, RFmxSpecAnMXAcpPowerUnits powerUnits)

#### Remarks

This method maps to the RFmxSpecAn_ACPCfgPowerUnits() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| powerUnits | RFmxSpecAnMXAcpPowerUnits | Specifies the units for the absolute power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00012: GetAmplitudeCorrectionType(string, out RFmxSpecAnMXAcpAmplitudeCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Natio

### GetAmplitudeCorrectionType(string, out RFmxSpecAnMXAcpAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxSpecAnMXAcpAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [AcpAmplitudeCorrectionType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXAcpAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getcarriermode__string-out.html language=enus -->
## TOPIC 00013: GetCarrierMode(string, out RFmxSpecAnMXAcpCarrierMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getcarriermode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getcarriermode__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to consider the carrier power as part of total carrier power measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierMode(string selectorString, out RFmxSpecAnMXAcpCarrierMode value)RemarksThis method maps to the RFmxSpecAn_ACPGetCarrierMode() function in C.P

### GetCarrierMode(string, out RFmxSpecAnMXAcpCarrierMode)

Gets whether to consider the carrier power as part of total carrier power measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierMode(string selectorString, out RFmxSpecAnMXAcpCarrierMode value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetCarrierMode() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXAcpCarrierMode | Upon return, indicates whether to consider the carrier power as part of total carrier power measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfarifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00014: GetFarIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfarifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfarifoutputpoweroffset__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset, in dB, by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFarIFOutputPowerOffset(string selectorString, out double value)RemarksThis meth

### GetFarIFOutputPowerOffset(string, out double)

Gets the offset, in dB, by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFarIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetFarIFOutputPowerOffset() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset, in dB, by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfftoverlapmode__string-out.html language=enus -->
## TOPIC 00015: GetFftOverlapMode(string, out RFmxSpecAnMXAcpFftOverlapMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfftoverlapmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfftoverlapmode__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the overlap mode when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFftOverlapMode(string selectorString, out RFmxSpecAnMXAcpFftOverlapMode value)RemarksThis method gets the val

### GetFftOverlapMode(string, out RFmxSpecAnMXAcpFftOverlapMode)

Gets the overlap mode when you set the [SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setmeasurementmethod__string-rfmxspecanmxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFftOverlapMode(string selectorString, out RFmxSpecAnMXAcpFftOverlapMode value)

#### Remarks

This method gets the value of [AcpFftOverlapMode](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftoverlapmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXAcpFftOverlapMode | Upon return, contains the overlap mode when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfftwindow__string-out.html language=enus -->
## TOPIC 00016: GetFftWindow(string, out RFmxSpecAnMXAcpFftWindow)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfftwindow__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getfftwindow__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT window type to use to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFftWindow(string selectorString, out RFmxSpecAnMXAcpFftWindow value)RemarksThis method maps to the RFmxSpecAn_ACPGetFFTWindow() function in C.ParametersNameTypeDescriptionselec

### GetFftWindow(string, out RFmxSpecAnMXAcpFftWindow)

Gets the FFT window type to use to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFftWindow(string selectorString, out RFmxSpecAnMXAcpFftWindow value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetFFTWindow() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXAcpFftWindow | Upon return, contains the FFT window type to use to reduce spectral leakage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnearifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00017: GetNearIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnearifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnearifoutputpoweroffset__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNearIFOutputPowerOffset(string selectorString, out double value)RemarksThis meth

### GetNearIFOutputPowerOffset(string, out double)

Gets the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNearIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetNearIFOutputPowerOffset() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnoisecalibrationaveragingauto__string-out.html language=enus -->
## TOPIC 00018: GetNoiseCalibrationAveragingAuto(string, out RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnoisecalibrationaveragingauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnoisecalibrationaveragingauto__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNoiseCalibrationAveragingAuto(string selectorString, out RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto value)RemarksThis method gets the

### GetNoiseCalibrationAveragingAuto(string, out RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto)

Gets whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCalibrationAveragingAuto(string selectorString, out RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto value)

#### Remarks

This method gets the value of [AcpNoiseCalibrationAveragingAuto](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpnoisecalibrationaveragingauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto | Upon return, contains whether RFmx automatically computes the averaging count used for instrument noise calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnoisecalibrationaveragingcount__string-out.html language=enus -->
## TOPIC 00019: GetNoiseCalibrationAveragingCount(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnoisecalibrationaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getnoisecalibrationaveragingcount__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) method to False. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNoiseCalibrationAveragingCount(string selectorString, out int v

### GetNoiseCalibrationAveragingCount(string, out int)

Gets the averaging count used for noise calibration when you set the [SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnoisecalibrationaveragingauto__string-rfmxspecanmxacpnoisecalibrationaveragingauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpnoisecalibrationaveragingauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCalibrationAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNoiseCalibrationAveragingCount](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 32.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetfrequencydefinition__string-out.html language=enus -->
## TOPIC 00020: GetOffsetFrequencyDefinition(string, out RFmxSpecAnMXAcpOffsetFrequencyDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetfrequencydefinition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetfrequencydefinition__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset frequency definition used to specify the SetOffsetFrequency(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetOffsetFrequencyDefinition(string selectorString, out RFmxSpecAnMXAcpOffsetFrequencyDefinition value)RemarksThis method maps to the RFmxS

### GetOffsetFrequencyDefinition(string, out RFmxSpecAnMXAcpOffsetFrequencyDefinition)

Gets the offset frequency definition used to specify the [SetOffsetFrequency(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetfrequency__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetOffsetFrequencyDefinition(string selectorString, out RFmxSpecAnMXAcpOffsetFrequencyDefinition value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetFrequencyDefinition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXAcpOffsetFrequencyDefinition | Upon return, contains the offset frequency definition used to specify the SetOffsetFrequency(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetrrcfilteralpha__string-out.html language=enus -->
## TOPIC 00021: GetOffsetRrcFilterAlpha(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetrrcfilteralpha__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetrrcfilteralpha__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetOffsetRrcFilterAlpha(string selectorString, out double value)RemarksThis method maps to the RFmxS

### GetOffsetRrcFilterAlpha(string, out double)

Gets the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetOffsetRrcFilterAlpha(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetRRCFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the roll-off factor for the RRC filter on the acquired offset channel before measuring the offset channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetrrcfilterenabled__string-out.html language=enus -->
## TOPIC 00022: GetOffsetRrcFilterEnabled(string, out RFmxSpecAnMXAcpOffsetRrcFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetrrcfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetrrcfilterenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the root-raised-cosine (RRC) filter is applied on the acquired offset channel before measuring the offset channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetOffsetRrcFilterEnabled(string selectorString, out RFmxSpecAnMXAcpOffsetRrcFilterEnabled value)RemarksT

### GetOffsetRrcFilterEnabled(string, out RFmxSpecAnMXAcpOffsetRrcFilterEnabled)

Gets whether the root-raised-cosine (RRC) filter is applied on the acquired offset channel before measuring the offset channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetOffsetRrcFilterEnabled(string selectorString, out RFmxSpecAnMXAcpOffsetRrcFilterEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetRRCFilterEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXAcpOffsetRrcFilterEnabled | Upon return, indicates whether the RRC filter is applied on the acquired offset channel before measuring the offset channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetsideband__string-out.html language=enus -->
## TOPIC 00023: GetOffsetSideband(string, out RFmxSpecAnMXAcpOffsetSideband)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetsideband__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getoffsetsideband__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the offset segment is present on one side, or on both sides of the carriers. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetOffsetSideband(string selectorString, out RFmxSpecAnMXAcpOffsetSideband value)RemarksThis method maps to the RFmxSpecAn_ACPGetOffsetSideband() fun

### GetOffsetSideband(string, out RFmxSpecAnMXAcpOffsetSideband)

Gets whether the offset segment is present on one side, or on both sides of the carriers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetOffsetSideband(string selectorString, out RFmxSpecAnMXAcpOffsetSideband value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetOffsetSideband() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXAcpOffsetSideband | Upon return, indicates whether the offset segment is present on one side, or on both sides of the carriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getpowerunits__string-out.html language=enus -->
## TOPIC 00024: GetPowerUnits(string, out RFmxSpecAnMXAcpPowerUnits)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getpowerunits__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-getpowerunits__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the adjacent channel power (ACP) power units. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetPowerUnits(string selectorString, out RFmxSpecAnMXAcpPowerUnits value)RemarksThis method maps to the RFmxSpecAn_ACPGetPowerUnits() function in C.ParametersNameTypeDescriptionselectorStr

### GetPowerUnits(string, out RFmxSpecAnMXAcpPowerUnits)

Gets the adjacent channel power (ACP) power units.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetPowerUnits(string selectorString, out RFmxSpecAnMXAcpPowerUnits value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetPowerUnits() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXAcpPowerUnits | Upon return, contains the ACP power units. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnearifoutputpoweroffset__string-double.html language=enus -->
## TOPIC 00025: SetNearIFOutputPowerOffset(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnearifoutputpoweroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnearifoutputpoweroffset__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNearIFOutputPowerOffset(string selectorString, double value)RemarksThis method m

### SetNearIFOutputPowerOffset(string, double)

Sets the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNearIFOutputPowerOffset(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetNearIFOutputPowerOffset() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnoisecompensationtype__string-rfmxspecanmxacpnoisecompensationtype.html language=enus -->
## TOPIC 00026: SetNoiseCompensationType(string, RFmxSpecAnMXAcpNoiseCompensationType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnoisecompensationtype__string-rfmxspecanmxacpnoisecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setnoisecompensationtype__string-rfmxspecanmxacpnoisecompensationtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNoiseCompensationType(string selectorString, RFmxSpecAnMXAcpNoiseCompensationType value)RemarksThis method sets the value of AcpNois

### SetNoiseCompensationType(string, RFmxSpecAnMXAcpNoiseCompensationType)

Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNoiseCompensationType(string selectorString, RFmxSpecAnMXAcpNoiseCompensationType value)

#### Remarks

This method sets the value of [AcpNoiseCompensationType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [AnalyzerAndTermination](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpnoisecompensationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXAcpNoiseCompensationType | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetpowerreferencecarrier__string-rfmxspecanmxacpoffsetpowerreferencecarrier.html language=enus -->
## TOPIC 00027: SetOffsetPowerReferenceCarrier(string, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetpowerreferencecarrier__string-rfmxspecanmxacpoffsetpowerreferencecarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetpowerreferencecarrier__string-rfmxspecanmxacpoffsetpowerreferencecarrier.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the carrier, for which the measured power is the power reference to measure offset channel relative power. The offset channel power is measured only if you set the ACP RFmxSpecAnMXAcpOffsetPowerReferenceCarrier to Active. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetOffsetPow

### SetOffsetPowerReferenceCarrier(string, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier)

Sets the carrier, for which the measured power is the power reference to measure offset channel relative power. The offset channel power is measured only if you set the ACP [RFmxSpecAnMXAcpOffsetPowerReferenceCarrier](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpoffsetpowerreferencecarrier.html) to [Active](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpcarriermode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetOffsetPowerReferenceCarrier(string selectorString, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetOffsetPowerReferenceCarrier() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | RFmxSpecAnMXAcpOffsetPowerReferenceCarrier | Specifies the carrier to be used as power reference to measure offset channel relative power. The offset channel power is measured only if you set the ACP RFmxSpecAnMXAcpOffsetPowerReferenceCarrier to Active. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetpowerreferencespecific__string-int.html language=enus -->
## TOPIC 00028: SetOffsetPowerReferenceSpecific(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetpowerreferencespecific__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetpowerreferencespecific__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the carrier index, for which the measured power is the power reference for the offset channel relative power, when you set the RFmxSpecAnMXAcpOffsetPowerReferenceCarrier method to Specific. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetOffsetPowerReferenceSpecific(string selec

### SetOffsetPowerReferenceSpecific(string, int)

Sets the carrier index, for which the measured power is the power reference for the offset channel relative power, when you set the [RFmxSpecAnMXAcpOffsetPowerReferenceCarrier](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpoffsetpowerreferencecarrier.html) method to [Specific](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpoffsetpowerreferencecarrier.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetOffsetPowerReferenceSpecific(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetOffsetPowerReferenceSpecific() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | int | Specifies the index of the carrier to be used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power, when you set the RFmxSpecAnMXAcpOffsetPowerReferenceCarrier method to Specific. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetrelativeattenuation__string-double.html language=enus -->
## TOPIC 00029: SetOffsetRelativeAttenuation(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetrelativeattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetrelativeattenuation__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation, in dB, relative to the external attenuation. Use this method to compensate for the variations in external attenuation when offset channels are spread wide in frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetOffsetRelativeAttenuation(string selectorStri

### SetOffsetRelativeAttenuation(string, double)

Sets the attenuation, in dB, relative to the external attenuation. Use this method to compensate for the variations in external attenuation when offset channels are spread wide in frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetOffsetRelativeAttenuation(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetOffsetRelativeAttenuation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | double | Specifies the attenuation, in dB, relative to the external attenuation. Use this method to compensate for variations in external attenuation when the offset channels are spread wide in frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetrrcfilteralpha__string-double.html language=enus -->
## TOPIC 00030: SetOffsetRrcFilterAlpha(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetrrcfilteralpha__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setoffsetrrcfilteralpha__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetOffsetRrcFilterAlpha(string selectorString, double value)RemarksThis method maps to the RFmxSpecA

### SetOffsetRrcFilterAlpha(string, double)

Sets the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetOffsetRrcFilterAlpha(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetOffsetRRCFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | double | Specifies the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setpowerunits__string-rfmxspecanmxacppowerunits.html language=enus -->
## TOPIC 00031: SetPowerUnits(string, RFmxSpecAnMXAcpPowerUnits)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setpowerunits__string-rfmxspecanmxacppowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setpowerunits__string-rfmxspecanmxacppowerunits.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the adjacent channel power (ACP) power units. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetPowerUnits(string selectorString, RFmxSpecAnMXAcpPowerUnits value)RemarksThis method maps to the RFmxSpecAn_ACPSetPowerUnits() function in C.ParametersNameTypeDescriptionselectorStrings

### SetPowerUnits(string, RFmxSpecAnMXAcpPowerUnits)

Sets the adjacent channel power (ACP) power units.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetPowerUnits(string selectorString, RFmxSpecAnMXAcpPowerUnits value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetPowerUnits() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXAcpPowerUnits | Specifies the ACP power units. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxacprbwautobandwidth.html language=enus -->
## TOPIC 00032: SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxacprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxacprbwautobandwidth.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the resolution bandwidth (RBW). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterAutoBandwidth(string selectorString, RFmxSpecAnMXAcpRbwAutoBandwidth value)RemarksThis method maps to the RFmxSpecAn_ACPSetRBWFilterAutoBandwidth() function

### SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth)

Sets whether the measurement computes the resolution bandwidth (RBW).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterAutoBandwidth(string selectorString, RFmxSpecAnMXAcpRbwAutoBandwidth value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetRBWFilterAutoBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00033: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth) to False. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterBandwidth(string selectorS

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set [SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth)](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxacprbwautobandwidth.html) to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxacprbwautobandwidth.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPSetRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth, in Hz, of the RBW filter used to sweep the acquired signal, when you set SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth) to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration.html language=enus -->
## TOPIC 00034: RFmxSpecAnMXAcpConfiguration Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ACP measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXAcpConfiguration : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny public

### RFmxSpecAnMXAcpConfiguration Class

Provides methods to configure the ACP measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXAcpConfiguration : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxSpecAnMXAcpAveragingEnabled, int, RFmxSpecAnMXAcpAveragingType) | Configures averaging for the adjacent channel power (ACP) measurement. |
| ConfigureCarrierAndOffsets(string, double, int, double) | Configures a carrier channel with offset channels on both sides of the carrier as specified by the number of offsets. The offset channels are separated by +/- (n*channel) spacing from the center of the carrier. Power is measured over the integration bandwidth for each channel. |
| ConfigureCarrierFrequency(string, double) | Configures the center frequency, in hertz (Hz), of the carrier, relative to the value of the GetCenterFrequency(string, out double) method. |
| ConfigureCarrierIntegrationBandwidth(string, double) | Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| ConfigureCarrierMode(string, RFmxSpecAnMXAcpCarrierMode) | Configures whether to consider the carrier power as part of total carrier power measurement. |
| ConfigureCarrierRrcFilter(string, RFmxSpecAnMXAcpCarrierRrcFilterEnabled, double) | Configures the root-raised-cosine (RRC) filter to apply on the carrier channel before measuring the carrier channel power. |
| ConfigureDetector(string, RFmxSpecAnMXAcpDetectorType, int) | Configures the detector settings, including detector type and the number of points to be detected. |
| ConfigureFft(string, RFmxSpecAnMXAcpFftWindow, double) | Configures window and FFT to obtain a spectrum for the adjacent channel power (ACP) measurement. |
| ConfigureMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) | Configures the method for performing the adjacent channel power (ACP) measurement. |
| ConfigureNoiseCompensationEnabled(string, RFmxSpecAnMXAcpNoiseCompensationEnabled) | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| ConfigureNumberOfCarriers(string, int) | Configures the number of carriers for the adjacent channel power (ACP) measurement. |
| ConfigureNumberOfOffsets(string, int) | Configures the number of offsets for the adjacent channel power (ACP) measurement. |
| ConfigureOffset(string, double, RFmxSpecAnMXAcpOffsetSideband, RFmxSpecAnMXAcpOffsetEnabled) | Configures an offset channel on one or both sides of carrier with center-to-center spacing as specified by the offset frequency and offset frequency definition. In case of multiple carriers, offset frequency is relative to the closest carrier. |
| ConfigureOffsetArray(string, double[], RFmxSpecAnMXAcpOffsetSideband[], RFmxSpecAnMXAcpOffsetEnabled[]) | Configures an offset channel on one or both sides of carrier with center-to-center spacing as specified by the offset frequency and offset frequency definition. In case of multiple carriers, offset frequency is relative to the closest carrier. |
| ConfigureOffsetFrequencyDefinition(string, RFmxSpecAnMXAcpOffsetFrequencyDefinition) | Configures the offset frequency definition for the ACP measurement. |
| ConfigureOffsetIntegrationBandwidth(string, double) | Configures the frequency range, in hertz (Hz), over which the adjacent channel power (ACP) measurement integrates the offset channel power. |
| ConfigureOffsetIntegrationBandwidthArray(string, double[]) | Configures the frequency range, in hertz (Hz), over which the measurement integrates the offset channel power. |
| ConfigureOffsetPowerReference(string, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier, int) | Configures the power reference to use for measuring the relative power of the offset channel. |
| ConfigureOffsetPowerReferenceArray(string, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier[], int[]) | Configures the power reference to use for measuring the relative power of the offset channel. |
| ConfigureOffsetRelativeAttenuation(string, double) | Configures the attenuation, in dB, relative to the external attenuation. |
| ConfigureOffsetRelativeAttenuationArray(string, double[]) | Configures the attenuation, in dB, relative to the external attenuation. |
| ConfigureOffsetRrcFilter(string, RFmxSpecAnMXAcpOffsetRrcFilterEnabled, double) | Configures the root raised cosine (RRC) channel filter to be applied on the offset channel before measuring the offset channel power. |
| ConfigureOffsetRrcFilterArray(string, RFmxSpecAnMXAcpOffsetRrcFilterEnabled[], double[]) | Configures the root raised cosine (RRC) channel filter to be applied on the offset channel before measuring the offset channel power. |
| ConfigurePowerUnits(string, RFmxSpecAnMXAcpPowerUnits) | Configures the units for the absolute power. |
| ConfigureRbwFilter(string, RFmxSpecAnMXAcpRbwAutoBandwidth, double, RFmxSpecAnMXAcpRbwFilterType) | Configures the resolution bandwidth (RBW) filter. |
| ConfigureSweepTime(string, RFmxSpecAnMXAcpSweepTimeAuto, double) | Configures the sweep time. |
| GetAllTracesEnabled(string, out bool) | Gets whether the traces to be stored and retrieved after performing the adjacent channel power (ACP) measurement are enabled. |
| GetAmplitudeCorrectionType(string, out RFmxSpecAnMXAcpAmplitudeCorrectionType) | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging. |
| GetAveragingEnabled(string, out RFmxSpecAnMXAcpAveragingEnabled) | Gets whether averaging is enabled for the adjacent channel power (ACP) measurement. |
| GetAveragingType(string, out RFmxSpecAnMXAcpAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. |
| GetCarrierFrequency(string, out double) | Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| GetCarrierIntegrationBandwidth(string, out double) | Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| GetCarrierMode(string, out RFmxSpecAnMXAcpCarrierMode) | Gets whether to consider the carrier power as part of total carrier power measurement. |
| GetCarrierRrcFilterAlpha(string, out double) | Gets the roll-off factor for the root-raised-cosine (RRC) filter on the carrier channel before measuring the carrier channel power. |
| GetCarrierRrcFilterEnabled(string, out RFmxSpecAnMXAcpCarrierRrcFilterEnabled) | Gets whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power. |
| GetDetectorPoints(string, out int) | Gets the number of trace points after the detector is applied. |
| GetDetectorType(string, out RFmxSpecAnMXAcpDetectorType) | Gets the type of detector to be used. |
| GetFarIFOutputPowerOffset(string, out double) | Gets the offset, in dB, by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. |
| GetFftOverlap(string, out double) | Gets the samples to overlap between the consecutive chunks as a percentage of the SetSequentialFftSize(string, int) method when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(string, RFmxSpecAnMXAcpFftOverlapMode) method to UserDefined. This value is expressed as a percentage. |
| GetFftOverlapMode(string, out RFmxSpecAnMXAcpFftOverlapMode) | Gets the overlap mode when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| GetFftPadding(string, out double) | Gets the factor by which the time-domain waveform is zero-padded before FFT. |
| GetFftWindow(string, out RFmxSpecAnMXAcpFftWindow) | Gets the FFT window type to use to reduce spectral leakage. |
| GetIFOutputPowerOffsetAuto(string, out RFmxSpecAnMXAcpIFOutputPowerOffsetAuto) | Gets whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether the adjacent channel power (ACP) measurement is enabled. |
| GetMeasurementMethod(string, out RFmxSpecAnMXAcpMeasurementMethod) | Gets the method for performing the adjacent channel power (ACP) measurement. |
| GetMeasurementMode(string, out RFmxSpecAnMXAcpMeasurementMode) | Gets whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNearIFOutputPowerOffset(string, out double) | Gets the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. |
| GetNoiseCalibrationAveragingAuto(string, out RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) | Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| GetNoiseCalibrationAveragingCount(string, out int) | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) method to False. |
| GetNoiseCalibrationMode(string, out RFmxSpecAnMXAcpNoiseCalibrationMode) | Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationEnabled(string, out RFmxSpecAnMXAcpNoiseCompensationEnabled) | Gets whether compensation of the channel powers for the inherent noise floor of the RF signal analyzer is enabled. |
| GetNoiseCompensationType(string, out RFmxSpecAnMXAcpNoiseCompensationType) | Gets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
| GetNumberOfCarriers(string, out int) | Gets the number of carriers. |
| GetNumberOfOffsets(string, out int) | Gets the number of offset channels. |
| GetOffsetEnabled(string, out RFmxSpecAnMXAcpOffsetEnabled) | Gets whether the offset channel for adjacent channel power (ACP) measurement is enabled. |
| GetOffsetFrequency(string, out double) | Gets the center or edge frequency, in hertz (Hz), of the offset channel, relative to the center frequency of the closest carrier as determined by the SetOffsetFrequencyDefinition(string, RFmxSpecAnMXAcpOffsetFrequencyDefinition) method. The sign of offset frequency is ignored and the SetOffsetSideband(string, RFmxSpecAnMXAcpOffsetSideband) method determines whether the upper, lower, or both offsets are measured. |
| GetOffsetFrequencyDefinition(string, out RFmxSpecAnMXAcpOffsetFrequencyDefinition) | Gets the offset frequency definition used to specify the SetOffsetFrequency(string, double) method. |
| GetOffsetIntegrationBandwidth(string, out double) | Gets the frequency range, in hertz (Hz), over which the measurement integrates the offset channel power. |
| GetOffsetPowerReferenceCarrier(string, out RFmxSpecAnMXAcpOffsetPowerReferenceCarrier) | Gets the carrier, for which the measured power is the power reference to measure offset channel relative power. |
| GetOffsetPowerReferenceSpecific(string, out int) | Gets the carrier index, for which the measured power is the power reference for the offset channel relative power. |
| GetOffsetRelativeAttenuation(string, out double) | Gets the attenuation, in dB, relative to the external attenuation. |
| GetOffsetRrcFilterAlpha(string, out double) | Gets the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. |
| GetOffsetRrcFilterEnabled(string, out RFmxSpecAnMXAcpOffsetRrcFilterEnabled) | Gets whether the root-raised-cosine (RRC) filter is applied on the acquired offset channel before measuring the offset channel power. |
| GetOffsetSideband(string, out RFmxSpecAnMXAcpOffsetSideband) | Gets whether the offset segment is present on one side, or on both sides of the carriers. |
| GetPowerUnits(string, out RFmxSpecAnMXAcpPowerUnits) | Gets the adjacent channel power (ACP) power units. |
| GetRbwFilterAutoBandwidth(string, out RFmxSpecAnMXAcpRbwAutoBandwidth) | Gets whether the measurement computes the resolution bandwidth (RBW). |
| GetRbwFilterBandwidth(string, out double) | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| GetRbwFilterBandwidthDefinition(string, out RFmxSpecAnMXAcpRbwFilterBandwidthDefinition) | Gets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. |
| GetRbwFilterType(string, out RFmxSpecAnMXAcpRbwFilterType) | Gets the shape of the digital resolution bandwidth (RBW) filter. |
| GetSequentialFftSize(string, out int) | Gets the FFT size when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| GetSweepTimeAuto(string, out RFmxSpecAnMXAcpSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXAcpSweepTimeAuto) method to False. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the adjacent channel power (ACP) measurement. |
| SetAmplitudeCorrectionType(string, RFmxSpecAnMXAcpAmplitudeCorrectionType) | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set SetAveragingEnabled(string, RFmxSpecAnMXAcpAveragingEnabled) to True. |
| SetAveragingEnabled(string, RFmxSpecAnMXAcpAveragingEnabled) | Sets whether to enable averaging of the spectrum for the adjacent channel power (ACP) measurement. |
| SetAveragingType(string, RFmxSpecAnMXAcpAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the adjacent channel power (ACP) measurement. |
| SetCarrierFrequency(string, double) | Sets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| SetCarrierIntegrationBandwidth(string, double) | Sets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| SetCarrierMode(string, RFmxSpecAnMXAcpCarrierMode) | Sets whether to consider the carrier power as part of total carrier power measurement. The total relative power of a carrier is measured with reference to the total power of all active carriers. The relative power of an offset channel is measured with reference to the total carrier power when you set the RFmxSpecAnMXAcpOffsetPowerReferenceCarrier to Composite. |
| SetCarrierRrcFilterAlpha(string, double) | Sets the roll-off factor for the root-raised-cosine (RRC) filter on the carrier channel before measuring the carrier channel power. |
| SetCarrierRrcFilterEnabled(string, RFmxSpecAnMXAcpCarrierRrcFilterEnabled) | Sets whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel after measuring the carrier channel power. |
| SetDetectorPoints(string, int) | Sets the number of trace points after the detector is applied. |
| SetDetectorType(string, RFmxSpecAnMXAcpDetectorType) | Sets the type of detector to be used. |
| SetFarIFOutputPowerOffset(string, double) | Sets the offset, in dB, by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. |
| SetFftOverlap(string, double) | Sets the samples to overlap between the consecutive chunks as a percentage of the SetSequentialFftSize(string, int) method when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(string, RFmxSpecAnMXAcpFftOverlapMode) method to UserDefined. This value is expressed as a percentage. |
| SetFftOverlapMode(string, RFmxSpecAnMXAcpFftOverlapMode) | Sets the overlap mode when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| SetFftPadding(string, double) | Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
| SetFftWindow(string, RFmxSpecAnMXAcpFftWindow) | Sets the FFT window type to use to reduce spectral leakage. |
| SetIFOutputPowerOffsetAuto(string, RFmxSpecAnMXAcpIFOutputPowerOffsetAuto) | Sets whether the measurement computes an IF output power level offset, for the offset channels to improve the dynamic range of the ACP measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the adjacent channel power (ACP) measurement. |
| SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) | Sets the method for performing the adjacent channel power (ACP) measurement. |
| SetMeasurementMode(string, RFmxSpecAnMXAcpMeasurementMode) | Sets whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNearIFOutputPowerOffset(string, double) | Sets the offset, in dB, by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. |
| SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) | Sets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| SetNoiseCalibrationAveragingCount(string, int) | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXAcpNoiseCalibrationAveragingAuto) method to False. |
| SetNoiseCalibrationMode(string, RFmxSpecAnMXAcpNoiseCalibrationMode) | Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationEnabled(string, RFmxSpecAnMXAcpNoiseCompensationEnabled) | Sets whether to enable compensation of the channel powers for the inherent noise floor of the RF signal analyzer. |
| SetNoiseCompensationType(string, RFmxSpecAnMXAcpNoiseCompensationType) | Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
| SetNumberOfCarriers(string, int) | Sets the number of carriers. |
| SetNumberOfOffsets(string, int) | Sets the number of offset channels. |
| SetOffsetEnabled(string, RFmxSpecAnMXAcpOffsetEnabled) | Sets whether to enable the offset channel for adjacent channel power (ACP) measurement. |
| SetOffsetFrequency(string, double) | Sets the center or edge frequency, in hertz (Hz), of the offset channel, relative to the center frequency of the closest carrier as determined by the SetOffsetFrequencyDefinition(string, RFmxSpecAnMXAcpOffsetFrequencyDefinition) method. The sign of offset frequency is ignored and the SetOffsetSideband(string, RFmxSpecAnMXAcpOffsetSideband) method determines whether the upper, lower, or both offsets are measured. |
| SetOffsetFrequencyDefinition(string, RFmxSpecAnMXAcpOffsetFrequencyDefinition) | Sets the offset frequency definition used to specify the SetOffsetFrequency(string, double) method. |
| SetOffsetIntegrationBandwidth(string, double) | Sets the frequency range, in hertz (Hz), over which the measurement integrates the offset channel power. |
| SetOffsetPowerReferenceCarrier(string, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier) | Sets the carrier, for which the measured power is the power reference to measure offset channel relative power. The offset channel power is measured only if you set the ACP RFmxSpecAnMXAcpOffsetPowerReferenceCarrier to Active. |
| SetOffsetPowerReferenceSpecific(string, int) | Sets the carrier index, for which the measured power is the power reference for the offset channel relative power, when you set the RFmxSpecAnMXAcpOffsetPowerReferenceCarrier method to Specific. |
| SetOffsetRelativeAttenuation(string, double) | Sets the attenuation, in dB, relative to the external attenuation. Use this method to compensate for the variations in external attenuation when offset channels are spread wide in frequency. |
| SetOffsetRrcFilterAlpha(string, double) | Sets the roll-off factor for the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. |
| SetOffsetRrcFilterEnabled(string, RFmxSpecAnMXAcpOffsetRrcFilterEnabled) | Sets whether to apply the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. |
| SetOffsetSideband(string, RFmxSpecAnMXAcpOffsetSideband) | Sets whether the offset segment is present on one side, or on both sides of the carriers. |
| SetPowerUnits(string, RFmxSpecAnMXAcpPowerUnits) | Sets the adjacent channel power (ACP) power units. |
| SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth) | Sets whether the measurement computes the resolution bandwidth (RBW). |
| SetRbwFilterBandwidth(string, double) | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXAcpRbwAutoBandwidth) to False. |
| SetRbwFilterBandwidthDefinition(string, RFmxSpecAnMXAcpRbwFilterBandwidthDefinition) | Sets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. |
| SetRbwFilterType(string, RFmxSpecAnMXAcpRbwFilterType) | Sets the shape of the digital resolution bandwidth (RBW) filter. |
| SetSequentialFftSize(string, int) | Sets the FFT size when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. |
| SetSweepTimeAuto(string, RFmxSpecAnMXAcpSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time, in seconds, when you set SetSweepTimeAuto(string, RFmxSpecAnMXAcpSweepTimeAuto) to False. |
| ValidateNoiseCalibrationData(string, out RFmxSpecAnMXAcpNoiseCalibrationDataValid) | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorstring parameter. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpdetectortype.html language=enus -->
## TOPIC 00035: RFmxSpecAnMXAcpDetectorType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpdetectortype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpdetectortype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of detector to be used. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAcpDetectorTypeMembersNameValueDescriptionNone0The detector is disabled. Sample1The middle sample in the bucket is detected. Normal2The maximum value of the samples within the bucket

### RFmxSpecAnMXAcpDetectorType Enumeration

Specifies the type of detector to be used.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAcpDetectorType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | The detector is disabled. |
| Sample | 1 | The middle sample in the bucket is detected. |
| Normal | 2 | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |
| Peak | 3 | The maximum value of the samples in the bucket is detected. |
| NegativePeak | 4 | The minimum value of the samples in the bucket is detected. |
| AverageRms | 5 | The average RMS of all the samples in the bucket is detected. |
| AverageVoltage | 6 | The average voltage of all the samples in the bucket is detected. |
| AverageLog | 7 | The average log of all the samples in the bucket is detected. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftoverlapmode.html language=enus -->
## TOPIC 00036: RFmxSpecAnMXAcpFftOverlapMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftoverlapmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftoverlapmode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the overlap mode when you set the SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod) method to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAcpFftOverlapModeMembersNameValueDescriptionDisabled0Disables the overlap between the chunks.

### RFmxSpecAnMXAcpFftOverlapMode Enumeration

Specifies the overlap mode when you set the [SetMeasurementMethod(string, RFmxSpecAnMXAcpMeasurementMethod)](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpconfiguration-setmeasurementmethod__string-rfmxspecanmxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-specanmx-rfmxspecanmxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAcpFftOverlapMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the overlap between the chunks. |
| Automatic | 1 | Measurement computes the overlap based on the ACP FFT Window set by the user. When you set the SetFftWindow(string, RFmxSpecAnMXAcpFftWindow) method to FlatTop, the number of overlapped samples between consecutive chunks is 50% of the value of the SetSequentialFftSize(string, int) method. When you set the ACP FFT Window method to None, the chunks are not overlapped. |
| UserDefined | 2 | Measurement uses the overlap that you specify in the SetFftOverlap(string, double) method. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftwindow.html language=enus -->
## TOPIC 00037: RFmxSpecAnMXAcpFftWindow Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftwindow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpfftwindow.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type to use to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAcpFftWindowMembersNameValueDescriptionNone0Analyzes transients for which duration is shorter than the window length. You can also use this window type to separa

### RFmxSpecAnMXAcpFftWindow Enumeration

Specifies the FFT window type to use to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAcpFftWindow

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| FlatTop | 1 | Measures single-tone amplitudes accurately. |
| Hanning | 2 | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| Hamming | 3 | Analyzes closely-spaced sine waves. |
| Gaussian | 4 | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |
| Blackman | 5 | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| BlackmanHarris | 6 | Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. |
| KaiserBessel | 7 | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getloweroffsetrelativepower__string-out.html language=enus -->
## TOPIC 00038: GetLowerOffsetRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getloweroffsetrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getloweroffsetrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower offset channel power, in dB, measured relative to the integrated power of the reference carrier. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLowerOffsetRelativePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_ACPGetResultsLowe

### GetLowerOffsetRelativePower(string, out double)

Gets the lower offset channel power, in dB, measured relative to the integrated power of the reference carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLowerOffsetRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsLowerOffsetRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the lower offset channel power, in dB, measured relative to the integrated power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetabsolutepower__string-out.html language=enus -->
## TOPIC 00039: GetUpperOffsetAbsolutePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetabsolutepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper offset channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUpperOffsetAbsolutePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetAbsolutePower() function in C.ParametersNameTypeDescriptionselectorS

### GetUpperOffsetAbsolutePower(string, out double)

Gets the upper offset channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperOffsetAbsolutePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetAbsolutePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the upper offset channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetfrequencyreferencecarrier__string-out.html language=enus -->
## TOPIC 00040: GetUpperOffsetFrequencyReferenceCarrier(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetfrequencyreferencecarrier__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetfrequencyreferencecarrier__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier index of the center frequency that was used as a reference to define the center frequency of the upper (positive) offset channel. Upper offset channels are channels that are to the right of the reference carrier. The reference carrier is the carrier that has an offset closest to the

### GetUpperOffsetFrequencyReferenceCarrier(string, out int)

Gets the carrier index of the center frequency that was used as a reference to define the center frequency of the upper (positive) offset channel. Upper offset channels are channels that are to the right of the reference carrier. The reference carrier is the carrier that has an offset closest to the lower offset channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperOffsetFrequencyReferenceCarrier(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetFrequencyReferenceCarrier() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out int | Upon return, contains the carrier index of the center frequency that was used as a reference to define the center frequency of the upper (positive) offset channel. Upper offset channels are channels that are to the right of the reference carrier. The reference carrier is the carrier that has an offset closest to the lower offset channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00041: GetUpperOffsetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetintegrationbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth used to measure the power in the upper offset channel. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUpperOffsetIntegrationBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetIntegrationB

### GetUpperOffsetIntegrationBandwidth(string, out double)

Gets the integration bandwidth used to measure the power in the upper offset channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperOffsetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth used to measure the power in the upper offset channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetrelativepower__string-out.html language=enus -->
## TOPIC 00042: GetUpperOffsetRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxacpresults-getupperoffsetrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper offset channel power, in dB, measured relative to the integrated power of the reference carrier. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUpperOffsetRelativePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_ACPGetResultsUppe

### GetUpperOffsetRelativePower(string, out double)

Gets the upper offset channel power, in dB, measured relative to the integrated power of the reference carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUpperOffsetRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_ACPGetResultsUpperOffsetRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and offset number. Example: "offset0", "result::r1/offset0". You can use the BuildOffsetString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the upper offset channel power, in dB, measured relative to the integrated power of the reference carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAcpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setcarrieroffset__string-double.html language=enus -->
## TOPIC 00043: SetCarrierOffset(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setcarrieroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setcarrieroffset__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the carrier offset when you set the SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierOffset(string selectorString, double value)RemarksThis m

### SetCarrierOffset(string, double)

Sets the carrier offset when you set the [SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setautocarrierdetectionenabled__string-rfmxspecanmxampmautocarrierdetectionenabled.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxampmautocarrierdetectionenabled.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierOffset(string selectorString, double value)

#### Remarks

This method sets the value of [AmpmCarrierOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | double | Specifies the carrier offset when you set the SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAmpmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setmeasurementsamplerate__string-double.html language=enus -->
## TOPIC 00044: SetMeasurementSampleRate(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setmeasurementsamplerate__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setmeasurementsamplerate__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition sample rate, in samples per second (S/s), when you set the SetMeasurementSampleRateMode(string, RFmxSpecAnMXAmpmMeasurementSampleRateMode) method to User. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementSampleRate(string selectorString, double value)Re

### SetMeasurementSampleRate(string, double)

Sets the acquisition sample rate, in samples per second (S/s), when you set the [SetMeasurementSampleRateMode(string, RFmxSpecAnMXAmpmMeasurementSampleRateMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxampmmeasurementsampleratemode.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxampmmeasurementsampleratemode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementSampleRate(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_AMPMSetMeasurementSampleRate() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Contains the acquisition sample rate, in S/s, when you set the SetMeasurementSampleRateMode(string, RFmxSpecAnMXAmpmMeasurementSampleRateMode) method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAmpmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setreferencepowertype__string-rfmxspecanmxampmreferencepowertype.html language=enus -->
## TOPIC 00045: SetReferencePowerType(string, RFmxSpecAnMXAmpmReferencePowerType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setreferencepowertype__string-rfmxspecanmxampmreferencepowertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setreferencepowertype__string-rfmxspecanmxampmreferencepowertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference power used for AM to AM and AM to PM traces. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetReferencePowerType(string selectorString, RFmxSpecAnMXAmpmReferencePowerType value)RemarksThis method sets the value of AmpmReferencePowerType attribute.The default value i

### SetReferencePowerType(string, RFmxSpecAnMXAmpmReferencePowerType)

Sets the reference power used for AM to AM and AM to PM traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetReferencePowerType(string selectorString, RFmxSpecAnMXAmpmReferencePowerType value)

#### Remarks

This method sets the value of [AmpmReferencePowerType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Input](nationalinstruments-rfmx-specanmx-rfmxspecanmxampmreferencepowertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXAmpmReferencePowerType | Specifies the reference power used for AM to AM and AM to PM traces. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXAmpmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setthresholdenabled__string-rfmxspecanmxampmthresholdenabled.html language=enus -->
## TOPIC 00046: SetThresholdEnabled(string, RFmxSpecAnMXAmpmThresholdEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setthresholdenabled__string-rfmxspecanmxampmthresholdenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmconfiguration-setthresholdenabled__string-rfmxspecanmxampmthresholdenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable thresholding of the acquired samples used for the AMPM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetThresholdEnabled(string selectorString, RFmxSpecAnMXAmpmThresholdEnabled value)RemarksThis method maps to the RFmxSpecAn_AMPMSetThresholdEnabled(

### SetThresholdEnabled(string, RFmxSpecAnMXAmpmThresholdEnabled)

Sets whether to enable thresholding of the acquired samples used for the AMPM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetThresholdEnabled(string selectorString, RFmxSpecAnMXAmpmThresholdEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_AMPMSetThresholdEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXAmpmThresholdEnabled | Contains a value that indicates whether to enable thresholding of the acquired samples used for the AMPM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAmpmConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmreferencepowertype.html language=enus -->
## TOPIC 00047: RFmxSpecAnMXAmpmReferencePowerType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmreferencepowertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmreferencepowertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference power used for AM to AM and AM to PM traces. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAmpmReferencePowerTypeMembersNameValueDescriptionInput0The instantaneous powers at the input port of device under test (DUT) forms the x-axis of AM to AM and

### RFmxSpecAnMXAmpmReferencePowerType Enumeration

Specifies the reference power used for AM to AM and AM to PM traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAmpmReferencePowerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Input | 0 | The instantaneous powers at the input port of device under test (DUT) forms the x-axis of AM to AM and AM to PM traces. |
| Output | 1 | The instantaneous powers at the output port of DUT forms the x-axis of AM to AM and AM to PM traces. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-fetchprocessedreferencewaveform__string-double-ref.html language=enus -->
## TOPIC 00048: FetchProcessedReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-fetchprocessedreferencewaveform__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-fetchprocessedreferencewaveform__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the segment of the reference waveform used to perform the AMPM measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchProcessedReferenceWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > processedReferenceWaveform)RemarksThis method m

### FetchProcessedReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

Fetches the segment of the reference waveform used to perform the AMPM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchProcessedReferenceWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > processedReferenceWaveform)

#### Remarks

This method maps to the RFmxSpecAn_AMPMFetchProcessedReferenceWaveform() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| processedReferenceWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the segment of the reference waveform used to perform the AMPM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAmpmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getamtoamcurvefitresidual__string-out.html language=enus -->
## TOPIC 00049: GetAMToAMCurveFitResidual(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getamtoamcurvefitresidual__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getamtoamcurvefitresidual__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the approximation error, in dB, in the polynomial approximation of the measured AM-to-AM characteristic of the device under test. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAMToAMCurveFitResidual(string selectorString, out double value)RemarksThis method maps to the RFmxSpe

### GetAMToAMCurveFitResidual(string, out double)

Gets the approximation error, in dB, in the polynomial approximation of the measured AM-to-AM characteristic of the device under test.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAMToAMCurveFitResidual(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_AMPMGetResultsAMToAMCurveFitResidual() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the approximation error, in dB, in the polynomial approximation of the measured AM-to-AM characteristic of the device under test. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition

Parent topic:

RFmxSpecAnMXAmpmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanlineargain__string-out.html language=enus -->
## TOPIC 00050: GetMeanLinearGain(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanlineargain__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanlineargain__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average linear gain, in dB, of the device under test, computed by rejecting signal samples containing gain compression. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeanLinearGain(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_AMPMGetRes

### GetMeanLinearGain(string, out double)

Gets the average linear gain, in dB, of the device under test, computed by rejecting signal samples containing gain compression.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanLinearGain(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_AMPMGetResultsMeanLinearGain() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Returns the average linear gain, in dB, of the device under test, computed by rejecting signal samples containing gain compression. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAmpmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanphaseerror__string-out.html language=enus -->
## TOPIC 00051: GetMeanPhaseError(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanphaseerror__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeanPhaseError(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_AMPMGetRe

### GetMeanPhaseError(string, out double)

Gets the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanPhaseError(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_AMPMGetResultsMeanPhaseError() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Returns the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAmpmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanrmsevm__string-out.html language=enus -->
## TOPIC 00052: GetMeanRmsEvm(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults-getmeanrmsevm__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ratio, as a percentage, of l^2 norm of difference between the normalized reference and acquired waveforms, to the l^2 norm of the normalized reference waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeanRmsEvm(string selectorString, out double value)RemarksThis met

### GetMeanRmsEvm(string, out double)

Gets the ratio, as a percentage, of l<sup>2</sup> norm of difference between the normalized reference and acquired waveforms, to the l<sup>2</sup> norm of the normalized reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanRmsEvm(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_AMPMGetResultsMeanRMSEVM() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the ratio, as a percentage, of l2 norm of difference between the normalized reference and acquired waveforms, to the l2 norm of the normalized reference waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXAmpmResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults.html language=enus -->
## TOPIC 00053: RFmxSpecAnMXAmpmResults Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmresults.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the AMPM measurement results. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXAmpmResults : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAn

### RFmxSpecAnMXAmpmResults Class

Provides methods to fetch and read the AMPM measurement results.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXAmpmResults : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| FetchAMToAMTrace(string, double, ref float[], ref float[], ref float[]) | Fetches the AM-to-AM trace where the inputPowers array forms the x-axis of the trace, and the measuredAMToAM and curveFitAMToAM arrays form the y-axis of the trace. |
| FetchAMToPMTrace(string, double, ref float[], ref float[], ref float[]) | Fetches the AM-to-AM trace where the inputPowers array forms the x-axis of the trace, and the measuredAMToPM and curveFitAMToPM arrays form the y-axis of the trace. |
| FetchCompressionPoints(string, double, ref double[], ref double[]) | Fetches the compression points. |
| FetchCurveFitCoefficients(string, double, ref float[], ref float[]) | Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test. |
| FetchCurveFitResidual(string, double, out double, out double) | Fetches the polynomial approximation residuals for AM-to-AM and AM-to-PM response of the device under test. |
| FetchDutCharacteristics(string, double, out double, out double, out double) | Fetches the mean linear gain, 1 dB compression point, and mean RMS EVM of the device under test. |
| FetchError(string, double, out double, out double, out double) | Fetches the maximum gain error range, phase error range, and mean phase error for the device under test. |
| FetchProcessedMeanAcquiredWaveform(string, double, ref ComplexWaveform< ComplexSingle >) | Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement. |
| FetchProcessedReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >) | Fetches the segment of the reference waveform used to perform the AMPM measurement. |
| FetchRelativePhaseTrace(string, double, ref AnalogWaveform< float >) | Fetches the phase of the processed mean acquired waveform relative to the processed reference waveform. |
| FetchRelativePowerTrace(string, double, ref AnalogWaveform< float >) | Fetches the power of the processed mean acquired waveform relative to the processed reference waveform. |
| Get1dBCompressionPoint(string, out double) | Gets the theoretical output power, in dBm, at which gain of the device under test drops by 1 dB from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. |
| GetAMToAMCurveFitCoefficients(string, ref float[]) | Gets the coefficients of the polynomial that approximates the measured AM-to-AM characteristic of the device under test. |
| GetAMToAMCurveFitResidual(string, out double) | Gets the approximation error, in dB, in the polynomial approximation of the measured AM-to-AM characteristic of the device under test. |
| GetAMToPMCurveFitCoefficients(string, ref float[]) | Gets the coefficients of the polynomial that approximates the measured AM-to-PM characteristic of the device under test. |
| GetAMToPMCurveFitResidual(string, out double) | Gets the approximation error, in degrees, in the polynomial approximation of the measured AM-to-PM characteristic of the device under test. |
| GetCompressionPointGainReference(string, out double) | Gets the gain reference used for compression point calculation. This value is expressed in dB. |
| GetGainErrorRange(string, out double) | Gets the peak-to-peak deviation of the gain, in dB, of the device under test. |
| GetInputCompressionPoint(string, ref double[]) | Gets the theoretical input power at which device gain drops by the compression level, specified through RFmxSpecAnMXAmpmConfiguration.GetCompressionPointLevel Method , from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. this value is expressed in dBm. |
| GetMeanLinearGain(string, out double) | Gets the average linear gain, in dB, of the device under test, computed by rejecting signal samples containing gain compression. |
| GetMeanPhaseError(string, out double) | Gets the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test. |
| GetMeanRmsEvm(string, out double) | Gets the ratio, as a percentage, of l2 norm of difference between the normalized reference and acquired waveforms, to the l2 norm of the normalized reference waveform. |
| GetOutputCompressionPoint(string, ref double[]) | Gets the theoretical output power at which device gain drops by the compression level, specified through RFmxSpecAnMXAmpmConfiguration.GetCompressionPointLevel Method , from a gain reference computed based on the value that you specify for the AmpmCompressionPointGainReference attribute. this value is expressed in dBm. |
| GetPeakReferencePower(string, out double) | Gets the peak reference power. This value is expressed in dBm. |
| GetPeakReferencePowerGain(string, out double) | Gets the gain at the peak reference power. This value is expressed in dB. |
| GetPhaseErrorRange(string, out double) | Gets the peak-to-peak deviation, in degrees, in the phase distortion of the acquired signal relative to the reference waveform caused by the device under test. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmsignaltype.html language=enus -->
## TOPIC 00054: RFmxSpecAnMXAmpmSignalType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmsignaltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmsignaltype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference waveform is a modulated signal or tones. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAmpmSignalTypeMembersNameValueDescriptionModulated0The reference waveform is a cellular or connectivity standard signal. Tones1The reference waveform is

### RFmxSpecAnMXAmpmSignalType Enumeration

Specifies whether the reference waveform is a modulated signal or tones.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAmpmSignalType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Modulated | 0 | The reference waveform is a cellular or connectivity standard signal. |
| Tones | 1 | The reference waveform is a continuous signal comprising of one or more tones. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmsynchronizationmethod.html language=enus -->
## TOPIC 00055: RFmxSpecAnMXAmpmSynchronizationMethod Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmsynchronizationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmsynchronizationmethod.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used for synchronization of acquired waveform with reference waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAmpmSynchronizationMethodMembersNameValueDescriptionDirect1Synchronizes the acquired and reference waveforms assuming that sample rate

### RFmxSpecAnMXAmpmSynchronizationMethod Enumeration

Specifies the method used for synchronization of acquired waveform with reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAmpmSynchronizationMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Direct | 1 | Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when the measurement sampling rate is high. |
| AliasProtected | 2 | Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when the measurement sampling rate is low. Refer to AMPM concept help for more information. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxampmthresholdtype.html language=enus -->
## TOPIC 00056: RFmxSpecAnMXAmpmThresholdType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxampmthresholdtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxampmthresholdtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXAmpmThresholdTypeMembersNameValueDescriptionRelative0The threshold is relative to the peak power, in dB, of the acquired samples. Absolute1The threshold is the

### RFmxSpecAnMXAmpmThresholdType Enumeration

Specifies the reference for the power level used for thresholding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXAmpmThresholdType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The threshold is relative to the peak power, in dB, of the acquired samples. |
| Absolute | 1 | The threshold is the absolute power, in dBm. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdf-configuration.html language=enus -->
## TOPIC 00057: Configuration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdf-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdf-configuration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXCcdfConfiguration instance that allows configuration of CCDF measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXCcdfConfiguration Configuration { get; }RemarksReturns an object of type RFmxSpecAnMXCcdfConfiguration.

### Configuration

Gets the [RFmxSpecAnMXCcdfConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration.html) instance that allows configuration of CCDF measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXCcdfConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration.html) Configuration { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXCcdfConfiguration.

Parent topic:

RFmxSpecAnMXCcdf Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdf-results.html language=enus -->
## TOPIC 00058: Results

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdf-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdf-results.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXCcdfResults instance that provides methods to retrieve CCDF measurement results. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXCcdfResults Results { get; }RemarksReturns an object of type RFmxSpecAnMXCcdfResults.

### Results

Gets the [RFmxSpecAnMXCcdfResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults.html) instance that provides methods to retrieve CCDF measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXCcdfResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults.html) Results { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXCcdfResults.

Parent topic:

RFmxSpecAnMXCcdf Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00059: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the traces to be stored and retrieved after performing the complementary cumulative distribution function (CCDF) measurement are enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method maps to the

### GetAllTracesEnabled(string, out bool)

Gets whether the traces to be stored and retrieved after performing the complementary cumulative distribution function (CCDF) measurement are enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if the traces to be stored and retrieved after performing the CCDF measurement are enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00060: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the complementary cumulative distribution function (CCDF) measurement is enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_CCDFGetMeasurementEnabled() function in C.

### GetMeasurementEnabled(string, out bool)

Gets whether the complementary cumulative distribution function (CCDF) measurement is enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if the CCDF measurement is enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getmeasurementinterval__string-out.html language=enus -->
## TOPIC 00061: GetMeasurementInterval(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getmeasurementinterval__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementInterval(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CCDFGetMeasurementIn

### GetMeasurementInterval(string, out double)

Gets the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementInterval(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the acquisition time, in seconds, for the CCDF measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00062: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for complementary cumulative distribution function (CCDF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_CCDFGe

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for complementary cumulative distribution function (CCDF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for CCDF measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00063: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the complementary cumulative distribution function (CCDF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_CCDFSetMeasurementEnabled() function in C.Param

### SetMeasurementEnabled(string, bool)

Sets whether to enable the complementary cumulative distribution function (CCDF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFSetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the CCDF measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setmeasurementinterval__string-double.html language=enus -->
## TOPIC 00064: SetMeasurementInterval(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setmeasurementinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setmeasurementinterval__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementInterval(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CCDFSetMeasurementInterv

### SetMeasurementInterval(string, double)

Sets the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementInterval(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFSetMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the acquisition time, in seconds, for the CCDF measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00065: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for complementary cumulative distribution function (CCDF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_CCDFSetNum

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for complementary cumulative distribution function (CCDF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFSetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for CCDF measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setnumberofrecords__string-int.html language=enus -->
## TOPIC 00066: SetNumberOfRecords(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setnumberofrecords__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setnumberofrecords__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for the complementary cumulative distribution function (CCDF) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfRecords(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_CCDFSetNumberOfRecords() function

### SetNumberOfRecords(string, int)

Sets the number of acquisitions used for the complementary cumulative distribution function (CCDF) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfRecords(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFSetNumberOfRecords() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for the CCDF measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00067: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterBandwidth(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CCDFSetRBWFilterBandwidth()

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFSetRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth, in Hz, of the RBW filter used to sweep the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setrbwfilterrrcalpha__string-double.html language=enus -->
## TOPIC 00068: SetRbwFilterRrcAlpha(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setrbwfilterrrcalpha__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setrbwfilterrrcalpha__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterRrcAlpha(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CCDFSetRBWFilterRRCAlpha() function in C.ParametersNameTypeDescriptionsele

### SetRbwFilterRrcAlpha(string, double)

Sets the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterRrcAlpha(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFSetRBWFilterRRCAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the roll-off factor for the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfrbwfiltertype.html language=enus -->
## TOPIC 00069: RFmxSpecAnMXCcdfRbwFilterType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfrbwfiltertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital resolution bandwidth (RBW) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXCcdfRbwFilterTypeMembersNameValueDescriptionNone5The measurement does not use any RBW filtering. Gaussian1The RBW filter has a Gaussian response. Flat2The R

### RFmxSpecAnMXCcdfRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXCcdfRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 5 | The measurement does not use any RBW filtering. |
| Gaussian | 1 | The RBW filter has a Gaussian response. |
| Flat | 2 | The RBW filter has a flat response. |
| Rrc | 6 | The RRC filter with the roll-off specified by the SetRbwFilterRrcAlpha(string, double) is used as the RBW filter. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeanpowerpercentile__string-out.html language=enus -->
## TOPIC 00070: GetMeanPowerPercentile(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeanpowerpercentile__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeanpowerpercentile__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the percentage of samples that have more power than the value returned by the GetMeanPower(string, out double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeanPowerPercentile(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CCDFGetRes

### GetMeanPowerPercentile(string, out double)

Gets the percentage of samples that have more power than the value returned by the [GetMeanPower(string, out double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeanpower__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeanPowerPercentile(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetResultsMeanPowerPercentile() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| value | out double | Upon return, contains the percentage of samples that have more power than the value returned by the GetMeanPower(string, out double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeasuredsamplescount__string-out.html language=enus -->
## TOPIC 00071: GetMeasuredSamplesCount(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeasuredsamplescount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-getmeasuredsamplescount__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total number of samples measured. The total number of samples includes only the samples above the threshold, when you set the SetThresholdEnabled(string, RFmxSpecAnMXCcdfThresholdEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasuredSamplesCount(st

### GetMeasuredSamplesCount(string, out int)

Gets the total number of samples measured. The total number of samples includes only the samples above the threshold, when you set the [SetThresholdEnabled(string, RFmxSpecAnMXCcdfThresholdEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfconfiguration-setthresholdenabled__string-rfmxspecanmxccdfthresholdenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfthresholdenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasuredSamplesCount(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetResultsMeasuredSampleCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| value | out int | Upon return, contains the total number of samples measured. The total number of samples includes only the samples above the threshold, when you set the SetThresholdEnabled(string, RFmxSpecAnMXCcdfThresholdEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-gettenpercentpower__string-out.html language=enus -->
## TOPIC 00072: GetTenPercentPower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-gettenpercentpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxccdfresults-gettenpercentpower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power, in dB, above the mean power, over which 10% of the total samples in the signal are present. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetTenPercentPower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CCDFGetResultsTenPercentPower(

### GetTenPercentPower(string, out double)

Gets the power, in dB, above the mean power, over which 10% of the total samples in the signal are present.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetTenPercentPower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CCDFGetResultsTenPercentPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| value | out double | Upon return, contains the power, in dB, above the mean power, over which 10% of the total samples in the signal are present. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXCcdfResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configurerrcfilter__string-rfmxspecanmxchpcarrierrrcfilterenabled-double.html language=enus -->
## TOPIC 00073: ConfigureRrcFilter(string, RFmxSpecAnMXChpCarrierRrcFilterEnabled, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configurerrcfilter__string-rfmxspecanmxchpcarrierrrcfilterenabled-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configurerrcfilter__string-rfmxspecanmxchpcarrierrrcfilterenabled-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the root-raised-cosine (RRC) filter to apply on the channel before measuring the channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureRrcFilter(string selectorString, RFmxSpecAnMXChpCarrierRrcFilterEnabled rrcFilterEnabled, double rrcAlpha)RemarksThis metho

### ConfigureRrcFilter(string, RFmxSpecAnMXChpCarrierRrcFilterEnabled, double)

Configures the root-raised-cosine (RRC) filter to apply on the channel before measuring the channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureRrcFilter(string selectorString, RFmxSpecAnMXChpCarrierRrcFilterEnabled rrcFilterEnabled, double rrcAlpha)

#### Remarks

This method maps to the RFmxSpecAn_CHPCfgRRCFilter() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| rrcFilterEnabled | RFmxSpecAnMXChpCarrierRrcFilterEnabled | Specifies whether to apply the RRC filter on the acquired channel before measuring the channel power. |
| rrcAlpha | double | Specifies the roll-off factor for the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configurespan__string-double.html language=enus -->
## TOPIC 00074: ConfigureSpan(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configurespan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configurespan__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSpan(string selectorString, double span)RemarksThis method maps to the RFmxSpecAn_CHPCfgSpan() functio

### ConfigureSpan(string, double)

Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSpan(string selectorString, double span)

#### Remarks

This method maps to the RFmxSpecAn_CHPCfgSpan() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| span | double | Specifies the frequency range, in Hz, around the center frequency, to acquire for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configuresweeptime__string-rfmxspecanmxchpsweeptimeauto-double.html language=enus -->
## TOPIC 00075: ConfigureSweepTime(string, RFmxSpecAnMXChpSweepTimeAuto, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configuresweeptime__string-rfmxspecanmxchpsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-configuresweeptime__string-rfmxspecanmxchpsweeptimeauto-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) method to False. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureSweepTime(string selectorString, RFmxSpecAnMXChpSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

### ConfigureSweepTime(string, RFmxSpecAnMXChpSweepTimeAuto, double)

Configures the sweep time, in seconds, when you set the [SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeauto__string-rfmxspecanmxchpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpsweeptimeauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureSweepTime(string selectorString, RFmxSpecAnMXChpSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Remarks

This method maps to the RFmxSpecAn_CHPCfgSweepTime() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxSpecAnMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00076: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the traces to be stored and retrieved after performing the channel power (CHP) measurement are enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_CHPGetAllTracesEnabled

### GetAllTracesEnabled(string, out bool)

Gets whether the traces to be stored and retrieved after performing the channel power (CHP) measurement are enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if the traces to be stored and retrieved after performing the CHP measurement are enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00077: GetAmplitudeCorrectionType(string, out RFmxSpecAnMXChpAmplitudeCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Natio

### GetAmplitudeCorrectionType(string, out RFmxSpecAnMXChpAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxSpecAnMXChpAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [ChpAmplitudeCorrectionType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00078: GetAveragingCount(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_CHPGetAveragingCount() function in C.ParametersNameTypeDescriptionselectorStringstringPass

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetAveragingCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00079: GetAveragingEnabled(string, out RFmxSpecAnMXChpAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether averaging for the channel power (CHP) measurement is enabled. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXChpAveragingEnabled value)RemarksThis method maps to the RFmxSpecAn_CHPGetAveragingEnabled() functio

### GetAveragingEnabled(string, out RFmxSpecAnMXChpAveragingEnabled)

Indicates whether averaging for the channel power (CHP) measurement is enabled.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXChpAveragingEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpAveragingEnabled | Upon return, contains a value that indicates whether averaging for the CHP measurement is enabled. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00080: GetAveragingType(string, out RFmxSpecAnMXChpAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingType(string selectorString, out RFmxSpecAnMXChpAveragingType value)RemarksThis method maps to the RFmxSpecAn_CHPGetAveragingType() function in C.ParametersNa

### GetAveragingType(string, out RFmxSpecAnMXChpAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingType(string selectorString, out RFmxSpecAnMXChpAveragingType value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetAveragingType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierfrequency__string-out.html language=enus -->
## TOPIC 00081: GetCarrierFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierfrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierFrequency(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetCarrierFrequency() function in C.Par

### GetCarrierFrequency(string, out double)

Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierFrequency(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetCarrierFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00082: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency range, in hertz (Hz), over which the measurement integrates the power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetCarrierIntegrationBandwidth()

### GetCarrierIntegrationBandwidth(string, out double)

Gets the frequency range, in hertz (Hz), over which the measurement integrates the power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetCarrierIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency range, in Hz, over which the measurement integrates the power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierrrcfilteralpha__string-out.html language=enus -->
## TOPIC 00083: GetCarrierRrcFilterAlpha(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierrrcfilteralpha__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierrrcfilteralpha__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierRrcFilterAlpha(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetCarrierRRCFilterAlpha() function in C.ParametersNameTypeDesc

### GetCarrierRrcFilterAlpha(string, out double)

Gets the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierRrcFilterAlpha(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetCarrierRRCFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the roll-off factor for the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierrrcfilterenabled__string-out.html language=enus -->
## TOPIC 00084: GetCarrierRrcFilterEnabled(string, out RFmxSpecAnMXChpCarrierRrcFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierrrcfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getcarrierrrcfilterenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierRrcFilterEnabled(string selectorString, out RFmxSpecAnMXChpCarrierRrcFilterEnabled value)RemarksThis method ma

### GetCarrierRrcFilterEnabled(string, out RFmxSpecAnMXChpCarrierRrcFilterEnabled)

Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierRrcFilterEnabled(string selectorString, out RFmxSpecAnMXChpCarrierRrcFilterEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetCarrierRRCFilterEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out RFmxSpecAnMXChpCarrierRrcFilterEnabled | Upon return, indicates whether the RRC filter is applied on the acquired channel after measuring the channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getdetectorpoints__string-out.html language=enus -->
## TOPIC 00085: GetDetectorPoints(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getdetectorpoints__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getdetectorpoints__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of trace points after the detector is applied. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetDetectorPoints(string selectorString, out int value)RemarksThis method gets the value of ChpDetectorPoints attribute.The default value is 1001.ParametersNameTypeDescriptions

### GetDetectorPoints(string, out int)

Gets the number of trace points after the detector is applied.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDetectorPoints(string selectorString, out int value)

#### Remarks

This method gets the value of [ChpDetectorPoints](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of trace points after the detector is applied. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getfftpadding__string-out.html language=enus -->
## TOPIC 00086: GetFftPadding(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getfftpadding__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getfftpadding__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFftPadding(string selectorString, out double value)RemarksThis method maps to the RFmx

### GetFftPadding(string, out double)

Gets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFftPadding(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetFFTPadding() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00087: GetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getintegrationbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency range, in hertz (Hz), over which the measurement integrates the power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetIntegrationBandwidth(string selectorString, out double value)RemarksThis method is obsoleted. Use GetCarrierIntegrationBandwidth method to get the

### GetIntegrationBandwidth(string, out double)

Gets the frequency range, in hertz (Hz), over which the measurement integrates the power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method is obsoleted. Use GetCarrierIntegrationBandwidth method to get the value. This method maps to the RFmxSpecAn_CHPGetIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the frequency range, in Hz, over which the measurement integrates the power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecalibrationaveragingauto__string-out.html language=enus -->
## TOPIC 00088: GetNoiseCalibrationAveragingAuto(string, out RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecalibrationaveragingauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecalibrationaveragingauto__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNoiseCalibrationAveragingAuto(string selectorString, out RFmxSpecAnMXChpNoiseCalibrationAveragingAuto value)RemarksThis method gets the

### GetNoiseCalibrationAveragingAuto(string, out RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)

Gets whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCalibrationAveragingAuto(string selectorString, out RFmxSpecAnMXChpNoiseCalibrationAveragingAuto value)

#### Remarks

This method gets the value of [ChpNoiseCalibrationAveragingAuto](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationaveragingauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpNoiseCalibrationAveragingAuto | Upon return, contains whether RFmx automatically computes the averaging count used for instrument noise calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecalibrationmode__string-out.html language=enus -->
## TOPIC 00089: GetNoiseCalibrationMode(string, out RFmxSpecAnMXChpNoiseCalibrationMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecalibrationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecalibrationmode__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNoiseCalibrationM

### GetNoiseCalibrationMode(string, out RFmxSpecAnMXChpNoiseCalibrationMode)

Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCalibrationMode(string selectorString, out RFmxSpecAnMXChpNoiseCalibrationMode value)

#### Remarks

This method gets the value of [ChpNoiseCalibrationMode](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpNoiseCalibrationMode | Upon return, contains whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecompensationenabled__string-out.html language=enus -->
## TOPIC 00090: GetNoiseCompensationEnabled(string, out RFmxSpecAnMXChpNoiseCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecompensationenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual an

### GetNoiseCompensationEnabled(string, out RFmxSpecAnMXChpNoiseCompensationEnabled)

Gets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the [SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationmode__string-rfmxspecanmxchpnoisecalibrationmode.html) method to [Auto](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html), or set the CHP Noise Cal Mode method to [Manual](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html) and [SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementmode__string-rfmxspecanmxchpmeasurementmode.html) method to [Measure](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpmeasurementmode.html). Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCompensationEnabled(string selectorString, out RFmxSpecAnMXChpNoiseCompensationEnabled value)

#### Remarks

This method gets the value of [ChpNoiseCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpNoiseCompensationEnabled | Upon return, contains whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecompensationtype__string-out.html language=enus -->
## TOPIC 00091: GetNoiseCompensationType(string, out RFmxSpecAnMXChpNoiseCompensationType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecompensationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnoisecompensationtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNoiseCompensationType(string selectorString, out RFmxSpecAnMXChpNoiseCompensationType value)RemarksThis method gets the value of Chp

### GetNoiseCompensationType(string, out RFmxSpecAnMXChpNoiseCompensationType)

Gets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNoiseCompensationType(string selectorString, out RFmxSpecAnMXChpNoiseCompensationType value)

#### Remarks

This method gets the value of [ChpNoiseCompensationType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [AnalyzerAndTermination](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpNoiseCompensationType | Upon return, contains the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00092: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_CHPGetNumberOfAnalysisThreads() function

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnumberofcarriers__string-out.html language=enus -->
## TOPIC 00093: GetNumberOfCarriers(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnumberofcarriers__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getnumberofcarriers__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of carriers. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNumberOfCarriers(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_CHPGetNumberOfCarriers() function in C.ParametersNameTypeDescriptionselectorStringstringPass an empty string. T

### GetNumberOfCarriers(string, out int)

Gets the number of carriers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfCarriers(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetNumberOfCarriers() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains a value that indicates the the number of carriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00094: GetRbwFilterAutoBandwidth(string, out RFmxSpecAnMXChpRbwAutoBandwidth)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterautobandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the resolution bandwidth (RBW). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterAutoBandwidth(string selectorString, out RFmxSpecAnMXChpRbwAutoBandwidth value)RemarksThis method maps to the RFmxSpecAn_CHPGetRBWFilterAutoBandwidth() funct

### GetRbwFilterAutoBandwidth(string, out RFmxSpecAnMXChpRbwAutoBandwidth)

Gets whether the measurement computes the resolution bandwidth (RBW).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterAutoBandwidth(string selectorString, out RFmxSpecAnMXChpRbwAutoBandwidth value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetRBWFilterAutoBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpRbwAutoBandwidth | Upon return, contains a value that indicates whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00095: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetRBWFilterBandwidth

### GetRbwFilterBandwidth(string, out double)

Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth, in Hz, of the RBW filter used to sweep the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterbandwidthdefinition__string-out.html language=enus -->
## TOPIC 00096: GetRbwFilterBandwidthDefinition(string, out RFmxSpecAnMXChpRbwFilterBandwidthDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterbandwidthdefinition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfilterbandwidthdefinition__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterBandwidthDefinition(string selectorString, out RFmxSpecAnMXChpRbwFilterBandwidthDefinition value)RemarksThis

### GetRbwFilterBandwidthDefinition(string, out RFmxSpecAnMXChpRbwFilterBandwidthDefinition)

Gets the bandwidth definition which you use to specify the value of the [SetRbwFilterBandwidth(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidth__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterBandwidthDefinition(string selectorString, out RFmxSpecAnMXChpRbwFilterBandwidthDefinition value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetRBWFilterBandwidthDefinition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpRbwFilterBandwidthDefinition | Upon return, contains the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00097: GetRbwFilterType(string, out RFmxSpecAnMXChpRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital resolution bandwidth (RBW) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRbwFilterType(string selectorString, out RFmxSpecAnMXChpRbwFilterType value)RemarksThis method maps to the RFmxSpecAn_CHPGetRBWFilterType() function in C.ParametersNameTyp

### GetRbwFilterType(string, out RFmxSpecAnMXChpRbwFilterType)

Gets the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRbwFilterType(string selectorString, out RFmxSpecAnMXChpRbwFilterType value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetRBWFilterType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrrcfilteralpha__string-out.html language=enus -->
## TOPIC 00098: GetRrcFilterAlpha(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrrcfilteralpha__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrrcfilteralpha__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRrcFilterAlpha(string selectorString, out double value)RemarksThis method is obsoleted. Use GetCarrierRrcFilterAlpha method to get the value. This method maps to the RFmx

### GetRrcFilterAlpha(string, out double)

Gets the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRrcFilterAlpha(string selectorString, out double value)

#### Remarks

This method is obsoleted. Use GetCarrierRrcFilterAlpha method to get the value. This method maps to the RFmxSpecAn_CHPGetRRCFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the roll-off factor for the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrrcfilterenabled__string-out.html language=enus -->
## TOPIC 00099: GetRrcFilterEnabled(string, out RFmxSpecAnMXChpRrcFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrrcfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getrrcfilterenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetRrcFilterEnabled(string selectorString, out RFmxSpecAnMXChpRrcFilterEnabled value)RemarksThis method is obsoleted. Us

### GetRrcFilterEnabled(string, out RFmxSpecAnMXChpRrcFilterEnabled)

Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetRrcFilterEnabled(string selectorString, out RFmxSpecAnMXChpRrcFilterEnabled value)

#### Remarks

This method is obsoleted. Use GetCarrierRrcFilterEnabled method to get the value. This method maps to the RFmxSpecAn_CHPGetRRCFilterEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpRrcFilterEnabled | Upon return, indicates whether the RRC filter is applied on the acquired channel after measuring the channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getspan__string-out.html language=enus -->
## TOPIC 00100: GetSpan(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getspan__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getspan__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSpan(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetSpan() function in C.ParametersNameTypeDe

### GetSpan(string, out double)

Gets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSpan(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetSpan() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the frequency range, in Hz, around the center frequency, to acquire for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00101: GetSweepTimeAuto(string, out RFmxSpecAnMXChpSweepTimeAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSweepTimeAuto(string selectorString, out RFmxSpecAnMXChpSweepTimeAuto value)RemarksThis method maps to the RFmxSpecAn_CHPGetSweepTimeAuto() function in C.ParametersNameTypeDescriptio

### GetSweepTimeAuto(string, out RFmxSpecAnMXChpSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxSpecAnMXChpSweepTimeAuto value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetSweepTimeAuto() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXChpSweepTimeAuto | Upon return, indicates whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00102: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time, in seconds. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetSweepTimeInterval() function in C.ParametersNameTypeDescriptionselectorStringstringPass an empty

### GetSweepTimeInterval(string, out double)

Gets the sweep time, in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetSweepTimeInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time, in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00103: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_CHPSetAllTracesEnabled() fun

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the traces to be stored and retrieved after performing the CHP measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setamplitudecorrectiontype__string-rfmxspecanmxchpamplitudecorrectiontype.html language=enus -->
## TOPIC 00104: SetAmplitudeCorrectionType(string, RFmxSpecAnMXChpAmplitudeCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setamplitudecorrectiontype__string-rfmxspecanmxchpamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setamplitudecorrectiontype__string-rfmxspecanmxchpamplitudecorrectiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Natio

### SetAmplitudeCorrectionType(string, RFmxSpecAnMXChpAmplitudeCorrectionType)

Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxSpecAnMXChpAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [ChpAmplitudeCorrectionType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00105: SetAveragingCount(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_C

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingenabled__string-rfmxspecanmxchpaveragingenabled.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetAveragingCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingenabled__string-rfmxspecanmxchpaveragingenabled.html language=enus -->
## TOPIC 00106: SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingenabled__string-rfmxspecanmxchpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingenabled__string-rfmxspecanmxchpaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingEnabled(string selectorString, RFmxSpecAnMXChpAveragingEnabled value)RemarksThis method maps to the RFmxSpecAn_CHPSetAveragingEnabled() function in C.Par

### SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled)

Sets whether to enable averaging for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingEnabled(string selectorString, RFmxSpecAnMXChpAveragingEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingtype__string-rfmxspecanmxchpaveragingtype.html language=enus -->
## TOPIC 00107: SetAveragingType(string, RFmxSpecAnMXChpAveragingType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingtype__string-rfmxspecanmxchpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setaveragingtype__string-rfmxspecanmxchpaveragingtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetAveragingType(string selectorString, RFmxSpecAnMXChpAveragingType value)RemarksThis method maps to

### SetAveragingType(string, RFmxSpecAnMXChpAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetAveragingType(string selectorString, RFmxSpecAnMXChpAveragingType value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetAveragingType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierfrequency__string-double.html language=enus -->
## TOPIC 00108: SetCarrierFrequency(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierfrequency__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierFrequency(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CHPSetCarrierFrequency() function in C.Paramet

### SetCarrierFrequency(string, double)

Sets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierFrequency(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetCarrierFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | double | Specifies the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierintegrationbandwidth__string-double.html language=enus -->
## TOPIC 00109: SetCarrierIntegrationBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierintegrationbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierintegrationbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency range, in hertz (Hz), over which the measurement integrates the power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierIntegrationBandwidth(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CHPSetCarrierIntegrationBandwidth() func

### SetCarrierIntegrationBandwidth(string, double)

Sets the frequency range, in hertz (Hz), over which the measurement integrates the power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierIntegrationBandwidth(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetCarrierIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | double | Specifies the frequency range, in Hz, over which the measurement integrates the power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierrrcfilteralpha__string-double.html language=enus -->
## TOPIC 00110: SetCarrierRrcFilterAlpha(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierrrcfilteralpha__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierrrcfilteralpha__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierRrcFilterAlpha(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CHPSetCarrierRRCFilterAlpha() function in C.ParametersNameTypeDescript

### SetCarrierRrcFilterAlpha(string, double)

Sets the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierRrcFilterAlpha(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetCarrierRRCFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | double | Specifies the roll-off factor for the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierrrcfilterenabled__string-rfmxspecanmxchpcarrierrrcfilterenabled.html language=enus -->
## TOPIC 00111: SetCarrierRrcFilterEnabled(string, RFmxSpecAnMXChpCarrierRrcFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierrrcfilterenabled__string-rfmxspecanmxchpcarrierrrcfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setcarrierrrcfilterenabled__string-rfmxspecanmxchpcarrierrrcfilterenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierRrcFilterEnabled(string selectorString, RFmxSpecAnMXChpCarrierRrcFilterEnabled value)RemarksThis method maps to

### SetCarrierRrcFilterEnabled(string, RFmxSpecAnMXChpCarrierRrcFilterEnabled)

Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierRrcFilterEnabled(string selectorString, RFmxSpecAnMXChpCarrierRrcFilterEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetCarrierRRCFilterEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | RFmxSpecAnMXChpCarrierRrcFilterEnabled | Specifies whether to apply the RRC filter on the acquired channel after measuring the channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setdetectorpoints__string-int.html language=enus -->
## TOPIC 00112: SetDetectorPoints(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setdetectorpoints__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setdetectorpoints__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of trace points after the detector is applied. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetDetectorPoints(string selectorString, int value)RemarksThis method sets the value of ChpDetectorPoints attribute.The default value is 1001.ParametersNameTypeDescriptionselec

### SetDetectorPoints(string, int)

Sets the number of trace points after the detector is applied.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetDetectorPoints(string selectorString, int value)

#### Remarks

This method sets the value of [ChpDetectorPoints](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 1001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of trace points after the detector is applied. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setdetectortype__string-rfmxspecanmxchpdetectortype.html language=enus -->
## TOPIC 00113: SetDetectorType(string, RFmxSpecAnMXChpDetectorType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setdetectortype__string-rfmxspecanmxchpdetectortype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setdetectortype__string-rfmxspecanmxchpdetectortype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of detector to be used. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetDetectorType(string selectorString, RFmxSpecAnMXChpDetectorType value)RemarksThis method sets the value of ChpDetectorType attribute.The default value is None. Refer to Spectral Measurements topic f

### SetDetectorType(string, RFmxSpecAnMXChpDetectorType)

Sets the type of detector to be used.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetDetectorType(string selectorString, RFmxSpecAnMXChpDetectorType value)

#### Remarks

This method sets the value of [ChpDetectorType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is None. Refer to Spectral Measurements topic for more information on detector types.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpDetectorType | Specifies the type of detector to be used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setfftpadding__string-double.html language=enus -->
## TOPIC 00114: SetFftPadding(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setfftpadding__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setfftpadding__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. SyntaxNamespace: NationalInstr

### SetFftPadding(string, double)

Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFftPadding(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetFFTPadding() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setfftwindow__string-rfmxspecanmxchpfftwindow.html language=enus -->
## TOPIC 00115: SetFftWindow(string, RFmxSpecAnMXChpFftWindow)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setfftwindow__string-rfmxspecanmxchpfftwindow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setfftwindow__string-rfmxspecanmxchpfftwindow.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the FFT window type used to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetFftWindow(string selectorString, RFmxSpecAnMXChpFftWindow value)RemarksThis method maps to the RFmxSpecAn_CHPSetFFTWindow() function in C.ParametersNameTypeDescriptionselectorStr

### SetFftWindow(string, RFmxSpecAnMXChpFftWindow)

Sets the FFT window type used to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetFftWindow(string selectorString, RFmxSpecAnMXChpFftWindow value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetFFTWindow() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpFftWindow | Specifies the FFT window type used to reduce spectral leakage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setintegrationbandwidth__string-double.html language=enus -->
## TOPIC 00116: SetIntegrationBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setintegrationbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setintegrationbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency range, in hertz (Hz), over which the measurement integrates the power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetIntegrationBandwidth(string selectorString, double value)RemarksThis method is obsoleted. Use SetCarrierIntegrationBandwidth method to set the val

### SetIntegrationBandwidth(string, double)

Sets the frequency range, in hertz (Hz), over which the measurement integrates the power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetIntegrationBandwidth(string selectorString, double value)

#### Remarks

This method is obsoleted. Use SetCarrierIntegrationBandwidth method to set the value. This method maps to the RFmxSpecAn_CHPSetIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the frequency range, in Hz, over which the measurement integrates the power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00117: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_CHPSetMeasurementEnabled() function in C.ParametersNameTypeDescriptionselectorStr

### SetMeasurementEnabled(string, bool)

Sets whether to enable the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable the traces to enable the CHP measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementmode__string-rfmxspecanmxchpmeasurementmode.html language=enus -->
## TOPIC 00118: SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementmode__string-rfmxspecanmxchpmeasurementmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementmode__string-rfmxspecanmxchpmeasurementmode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementMode(string sele

### SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode)

Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementMode(string selectorString, RFmxSpecAnMXChpMeasurementMode value)

#### Remarks

This method sets the value of [ChpMeasurementMode](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Measure](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpmeasurementmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpMeasurementMode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxspecanmxchpnoisecalibrationaveragingauto.html language=enus -->
## TOPIC 00119: SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxspecanmxchpnoisecalibrationaveragingauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxspecanmxchpnoisecalibrationaveragingauto.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNoiseCalibrationAveragingAuto(string selectorString, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto value)RemarksThis method sets the valu

### SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)

Sets whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNoiseCalibrationAveragingAuto(string selectorString, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto value)

#### Remarks

This method sets the value of [ChpNoiseCalibrationAveragingAuto](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationaveragingauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpNoiseCalibrationAveragingAuto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingcount__string-int.html language=enus -->
## TOPIC 00120: SetNoiseCalibrationAveragingCount(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingcount__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNoiseCalibrationAveragingCount(string selectorString, int value

### SetNoiseCalibrationAveragingCount(string, int)

Sets the averaging count used for noise calibration when you set the [SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxspecanmxchpnoisecalibrationaveragingauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationaveragingauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNoiseCalibrationAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ChpNoiseCalibrationAveragingCount](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 32.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationmode__string-rfmxspecanmxchpnoisecalibrationmode.html language=enus -->
## TOPIC 00121: SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationmode__string-rfmxspecanmxchpnoisecalibrationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationmode__string-rfmxspecanmxchpnoisecalibrationmode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNoiseCalibrationM

### SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode)

Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNoiseCalibrationMode(string selectorString, RFmxSpecAnMXChpNoiseCalibrationMode value)

#### Remarks

This method sets the value of [ChpNoiseCalibrationMode](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpNoiseCalibrationMode | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecompensationenabled__string-rfmxspecanmxchpnoisecompensationenabled.html language=enus -->
## TOPIC 00122: SetNoiseCompensationEnabled(string, RFmxSpecAnMXChpNoiseCompensationEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecompensationenabled__string-rfmxspecanmxchpnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecompensationenabled__string-rfmxspecanmxchpnoisecompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual an

### SetNoiseCompensationEnabled(string, RFmxSpecAnMXChpNoiseCompensationEnabled)

Sets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the [SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationmode__string-rfmxspecanmxchpnoisecalibrationmode.html) method to [Auto](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html), or set the CHP Noise Cal Mode method to [Manual](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html) and [SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementmode__string-rfmxspecanmxchpmeasurementmode.html) method to [Measure](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpmeasurementmode.html). Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNoiseCompensationEnabled(string selectorString, RFmxSpecAnMXChpNoiseCompensationEnabled value)

#### Remarks

This method sets the value of [ChpNoiseCompensationEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpNoiseCompensationEnabled | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecompensationtype__string-rfmxspecanmxchpnoisecompensationtype.html language=enus -->
## TOPIC 00123: SetNoiseCompensationType(string, RFmxSpecAnMXChpNoiseCompensationType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecompensationtype__string-rfmxspecanmxchpnoisecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecompensationtype__string-rfmxspecanmxchpnoisecompensationtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNoiseCompensationType(string selectorString, RFmxSpecAnMXChpNoiseCompensationType value)RemarksThis method sets the value of ChpNois

### SetNoiseCompensationType(string, RFmxSpecAnMXChpNoiseCompensationType)

Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNoiseCompensationType(string selectorString, RFmxSpecAnMXChpNoiseCompensationType value)

#### Remarks

This method sets the value of [ChpNoiseCompensationType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [AnalyzerAndTermination](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpNoiseCompensationType | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00124: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_CHPSetNumberOfAnalysisThreads() function in

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnumberofcarriers__string-int.html language=enus -->
## TOPIC 00125: SetNumberOfCarriers(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnumberofcarriers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnumberofcarriers__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of carriers. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetNumberOfCarriers(string selectorString, int value)RemarksThis method maps to the RFmxSpecAn_CHPSetNumberOfCarriers() function in C.ParametersNameTypeDescriptionselectorStringstringPass an empty string. The s

### SetNumberOfCarriers(string, int)

Sets the number of carriers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetNumberOfCarriers(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetNumberOfCarriers() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of carriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxchprbwautobandwidth.html language=enus -->
## TOPIC 00126: SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXChpRbwAutoBandwidth)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxchprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterautobandwidth__string-rfmxspecanmxchprbwautobandwidth.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the resolution bandwidth (RBW). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterAutoBandwidth(string selectorString, RFmxSpecAnMXChpRbwAutoBandwidth value)RemarksThis method maps to the RFmxSpecAn_CHPSetRBWFilterAutoBandwidth() function

### SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXChpRbwAutoBandwidth)

Sets whether the measurement computes the resolution bandwidth (RBW).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterAutoBandwidth(string selectorString, RFmxSpecAnMXChpRbwAutoBandwidth value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetRBWFilterAutoBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00127: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterBandwidth(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CHPSetRBWFilterBandwidth() f

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetRBWFilterBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth, in Hz, of the RBW filter used to sweep the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidthdefinition__string-rfmxspecanmxchprbwfilterbandwidthdefinition.html language=enus -->
## TOPIC 00128: SetRbwFilterBandwidthDefinition(string, RFmxSpecAnMXChpRbwFilterBandwidthDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidthdefinition__string-rfmxspecanmxchprbwfilterbandwidthdefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidthdefinition__string-rfmxspecanmxchprbwfilterbandwidthdefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterBandwidthDefinition(string selectorString, RFmxSpecAnMXChpRbwFilterBandwidthDefinition value)RemarksThis meth

### SetRbwFilterBandwidthDefinition(string, RFmxSpecAnMXChpRbwFilterBandwidthDefinition)

Sets the bandwidth definition which you use to specify the value of the [SetRbwFilterBandwidth(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfilterbandwidth__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterBandwidthDefinition(string selectorString, RFmxSpecAnMXChpRbwFilterBandwidthDefinition value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetRBWFilterBandwidthDefinition() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpRbwFilterBandwidthDefinition | Specifies the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfiltertype__string-rfmxspecanmxchprbwfiltertype.html language=enus -->
## TOPIC 00129: SetRbwFilterType(string, RFmxSpecAnMXChpRbwFilterType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfiltertype__string-rfmxspecanmxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrbwfiltertype__string-rfmxspecanmxchprbwfiltertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital resolution bandwidth (RBW) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRbwFilterType(string selectorString, RFmxSpecAnMXChpRbwFilterType value)RemarksThis method maps to the RFmxSpecAn_CHPSetRBWFilterType() function in C.ParametersNameTypeDes

### SetRbwFilterType(string, RFmxSpecAnMXChpRbwFilterType)

Sets the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRbwFilterType(string selectorString, RFmxSpecAnMXChpRbwFilterType value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetRBWFilterType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrrcfilteralpha__string-double.html language=enus -->
## TOPIC 00130: SetRrcFilterAlpha(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrrcfilteralpha__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrrcfilteralpha__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRrcFilterAlpha(string selectorString, double value)RemarksThis method is obsoleted. Use SetCarrierRrcFilterAlpha method to set the value. This method maps to the RFmxSpec

### SetRrcFilterAlpha(string, double)

Sets the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRrcFilterAlpha(string selectorString, double value)

#### Remarks

This method is obsoleted. Use SetCarrierRrcFilterAlpha method to set the value. This method maps to the RFmxSpecAn_CHPSetRRCFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the roll-off factor for the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrrcfilterenabled__string-rfmxspecanmxchprrcfilterenabled.html language=enus -->
## TOPIC 00131: SetRrcFilterEnabled(string, RFmxSpecAnMXChpRrcFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrrcfilterenabled__string-rfmxspecanmxchprrcfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setrrcfilterenabled__string-rfmxspecanmxchprrcfilterenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetRrcFilterEnabled(string selectorString, RFmxSpecAnMXChpRrcFilterEnabled value)RemarksThis method is obsoleted. Use SetC

### SetRrcFilterEnabled(string, RFmxSpecAnMXChpRrcFilterEnabled)

Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetRrcFilterEnabled(string selectorString, RFmxSpecAnMXChpRrcFilterEnabled value)

#### Remarks

This method is obsoleted. Use SetCarrierRrcFilterEnabled method to set the value. This method maps to the RFmxSpecAn_CHPSetRRCFilterEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpRrcFilterEnabled | Specifies whether to apply the RRC filter on the acquired channel after measuring the channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setspan__string-double.html language=enus -->
## TOPIC 00132: SetSpan(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setspan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setspan__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSpan(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CHPSetSpan() function in C.ParametersNameTypeDescri

### SetSpan(string, double)

Sets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSpan(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetSpan() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the frequency range, in Hz, around the center frequency, to acquire for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeauto__string-rfmxspecanmxchpsweeptimeauto.html language=enus -->
## TOPIC 00133: SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeauto__string-rfmxspecanmxchpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeauto__string-rfmxspecanmxchpsweeptimeauto.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSweepTimeAuto(string selectorString, RFmxSpecAnMXChpSweepTimeAuto value)RemarksThis method maps to the RFmxSpecAn_CHPSetSweepTimeAuto() function in C.ParametersNameTypeDescriptionsel

### SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto)

Sets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSweepTimeAuto(string selectorString, RFmxSpecAnMXChpSweepTimeAuto value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetSweepTimeAuto() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00134: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) method to False. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method maps to the RFmxSpecAn_CHPSetSweepTimeInt

### SetSweepTimeInterval(string, double)

Sets the sweep time, in seconds, when you set the [SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setsweeptimeauto__string-rfmxspecanmxchpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpsweeptimeauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPSetSweepTimeInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-validatenoisecalibrationdata__string-out.html language=enus -->
## TOPIC 00135: ValidateNoiseCalibrationData(string, out RFmxSpecAnMXChpNoiseCalibrationDataValid)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-validatenoisecalibrationdata__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-validatenoisecalibrationdata__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorstring parameter.SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ValidateNoiseCalibrationData(string selectorString, out RFmxSpecAnMXChpNoiseCalibrationDataValid noiseCalibratio

### ValidateNoiseCalibrationData(string, out RFmxSpecAnMXChpNoiseCalibrationDataValid)

Indicates whether calibration data is valid for the configuration specified by the signal name in the *selectorstring* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ValidateNoiseCalibrationData(string selectorString, out RFmxSpecAnMXChpNoiseCalibrationDataValid noiseCalibrationDataValid)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| noiseCalibrationDataValid | out RFmxSpecAnMXChpNoiseCalibrationDataValid | Upon return, contains whether the calibration data is valid. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration.html language=enus -->
## TOPIC 00136: RFmxSpecAnMXChpConfiguration Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the channel power (CHP) measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXChpConfiguration : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread S

### RFmxSpecAnMXChpConfiguration Class

Provides methods to configure the channel power (CHP) measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXChpConfiguration : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxSpecAnMXChpAveragingEnabled, int, RFmxSpecAnMXChpAveragingType) | Configures averaging for the channel power (CHP) measurement. |
| ConfigureCarrierOffset(string, double) | Configures the center frequency of the carrier, relative to the RF center frequency. |
| ConfigureDetector(string, RFmxSpecAnMXChpDetectorType, int) | Configures the detector settings, including detector type and the number of points to be detected. |
| ConfigureFft(string, RFmxSpecAnMXChpFftWindow, double) | Configures window and FFT to obtain a spectrum for the channel power (CHP) measurement. |
| ConfigureIntegrationBandwidth(string, double) | Configures the frequency range, in hertz (Hz), over which the measurement integrates the carrier channel power. |
| ConfigureNumberOfCarriers(string, int) | Configures the number of carriers for the CHP measurement. |
| ConfigureRbwFilter(string, RFmxSpecAnMXChpRbwAutoBandwidth, double, RFmxSpecAnMXChpRbwFilterType) | Configures the resolution bandwidth (RBW) filter. |
| ConfigureRrcFilter(string, RFmxSpecAnMXChpCarrierRrcFilterEnabled, double) | Configures the root-raised-cosine (RRC) filter to apply on the channel before measuring the channel power. |
| ConfigureSpan(string, double) | Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the channel power (CHP) measurement. |
| ConfigureSweepTime(string, RFmxSpecAnMXChpSweepTimeAuto, double) | Configures the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) method to False. |
| GetAllTracesEnabled(string, out bool) | Gets whether the traces to be stored and retrieved after performing the channel power (CHP) measurement are enabled. |
| GetAmplitudeCorrectionType(string, out RFmxSpecAnMXChpAmplitudeCorrectionType) | Gets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging. |
| GetAveragingEnabled(string, out RFmxSpecAnMXChpAveragingEnabled) | Indicates whether averaging for the channel power (CHP) measurement is enabled. |
| GetAveragingType(string, out RFmxSpecAnMXChpAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. |
| GetCarrierFrequency(string, out double) | Gets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| GetCarrierIntegrationBandwidth(string, out double) | Gets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
| GetCarrierRrcFilterAlpha(string, out double) | Gets the roll-off factor for the root-raised-cosine (RRC) filter. |
| GetCarrierRrcFilterEnabled(string, out RFmxSpecAnMXChpCarrierRrcFilterEnabled) | Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power. |
| GetDetectorPoints(string, out int) | Gets the number of trace points after the detector is applied. |
| GetDetectorType(string, out RFmxSpecAnMXChpDetectorType) | Gets the type of detector to be used. |
| GetFftPadding(string, out double) | Gets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. |
| GetFftWindow(string, out RFmxSpecAnMXChpFftWindow) | Gets the FFT window type used to reduce spectral leakage. |
| GetIntegrationBandwidth(string, out double) | Gets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
| GetMeasurementEnabled(string, out bool) | Gets whether the channel power (CHP) measurement is enabled. |
| GetMeasurementMode(string, out RFmxSpecAnMXChpMeasurementMode) | Gets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCalibrationAveragingAuto(string, out RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) | Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| GetNoiseCalibrationAveragingCount(string, out int) | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. |
| GetNoiseCalibrationMode(string, out RFmxSpecAnMXChpNoiseCalibrationMode) | Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationEnabled(string, out RFmxSpecAnMXChpNoiseCompensationEnabled) | Gets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationType(string, out RFmxSpecAnMXChpNoiseCompensationType) | Gets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for channel power (CHP) measurement. |
| GetNumberOfCarriers(string, out int) | Gets the number of carriers. |
| GetRbwFilterAutoBandwidth(string, out RFmxSpecAnMXChpRbwAutoBandwidth) | Gets whether the measurement computes the resolution bandwidth (RBW). |
| GetRbwFilterBandwidth(string, out double) | Gets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| GetRbwFilterBandwidthDefinition(string, out RFmxSpecAnMXChpRbwFilterBandwidthDefinition) | Gets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. |
| GetRbwFilterType(string, out RFmxSpecAnMXChpRbwFilterType) | Gets the shape of the digital resolution bandwidth (RBW) filter. |
| GetRrcFilterAlpha(string, out double) | Gets the roll-off factor for the root-raised-cosine (RRC) filter. |
| GetRrcFilterEnabled(string, out RFmxSpecAnMXChpRrcFilterEnabled) | Gets whether the root-raised-cosine (RRC) filter is applied on the acquired channel after measuring the channel power. |
| GetSpan(string, out double) | Gets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |
| GetSweepTimeAuto(string, out RFmxSpecAnMXChpSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time, in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. |
| SetAmplitudeCorrectionType(string, RFmxSpecAnMXChpAmplitudeCorrectionType) | Sets whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the _RFmxInstrCfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxSpecAnMXChpAveragingEnabled) | Sets whether to enable averaging for the channel power (CHP) measurement. |
| SetAveragingType(string, RFmxSpecAnMXChpAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for channel power (CHP) measurement. |
| SetCarrierFrequency(string, double) | Sets the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |
| SetCarrierIntegrationBandwidth(string, double) | Sets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
| SetCarrierRrcFilterAlpha(string, double) | Sets the roll-off factor for the root-raised-cosine (RRC) filter. |
| SetCarrierRrcFilterEnabled(string, RFmxSpecAnMXChpCarrierRrcFilterEnabled) | Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. |
| SetDetectorPoints(string, int) | Sets the number of trace points after the detector is applied. |
| SetDetectorType(string, RFmxSpecAnMXChpDetectorType) | Sets the type of detector to be used. |
| SetFftPadding(string, double) | Sets the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This method is applicable only when the acquisition span is less than the device instantaneous bandwidth of the device. |
| SetFftWindow(string, RFmxSpecAnMXChpFftWindow) | Sets the FFT window type used to reduce spectral leakage. |
| SetIntegrationBandwidth(string, double) | Sets the frequency range, in hertz (Hz), over which the measurement integrates the power. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the channel power (CHP) measurement. |
| SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode) | Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) | Sets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| SetNoiseCalibrationAveragingCount(string, int) | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxSpecAnMXChpNoiseCalibrationAveragingAuto) method to False. |
| SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) | Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationEnabled(string, RFmxSpecAnMXChpNoiseCompensationEnabled) | Sets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationType(string, RFmxSpecAnMXChpNoiseCompensationType) | Sets the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for channel power (CHP) measurement. |
| SetNumberOfCarriers(string, int) | Sets the number of carriers. |
| SetRbwFilterAutoBandwidth(string, RFmxSpecAnMXChpRbwAutoBandwidth) | Sets whether the measurement computes the resolution bandwidth (RBW). |
| SetRbwFilterBandwidth(string, double) | Sets the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter used to sweep the acquired signal. |
| SetRbwFilterBandwidthDefinition(string, RFmxSpecAnMXChpRbwFilterBandwidthDefinition) | Sets the bandwidth definition which you use to specify the value of the SetRbwFilterBandwidth(string, double) method. |
| SetRbwFilterType(string, RFmxSpecAnMXChpRbwFilterType) | Sets the shape of the digital resolution bandwidth (RBW) filter. |
| SetRrcFilterAlpha(string, double) | Sets the roll-off factor for the root-raised-cosine (RRC) filter. |
| SetRrcFilterEnabled(string, RFmxSpecAnMXChpRrcFilterEnabled) | Sets whether to apply the root-raised-cosine (RRC) filter on the acquired channel after measuring the channel power. |
| SetSpan(string, double) | Sets the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |
| SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time, in seconds, when you set the SetSweepTimeAuto(string, RFmxSpecAnMXChpSweepTimeAuto) method to False. |
| ValidateNoiseCalibrationData(string, out RFmxSpecAnMXChpNoiseCalibrationDataValid) | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorstring parameter. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationaveragingauto.html language=enus -->
## TOPIC 00137: RFmxSpecAnMXChpNoiseCalibrationAveragingAuto Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationaveragingauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationaveragingauto.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXChpNoiseCalibrationAveragingAutoMembersNameValueDescriptionFalse0RFmx uses the averages that you set for the SetNoiseCali

### RFmxSpecAnMXChpNoiseCalibrationAveragingAuto Enumeration

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXChpNoiseCalibrationAveragingAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | RFmx uses the averages that you set for the SetNoiseCalibrationAveragingCount(string, int) method. |
| True | 1 | RFmx uses a noise calibration averaging count of 32. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationenabled.html language=enus -->
## TOPIC 00138: RFmxSpecAnMXChpNoiseCompensationEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manu

### RFmxSpecAnMXChpNoiseCompensationEnabled Enumeration

Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the [SetNoiseCalibrationMode(string, RFmxSpecAnMXChpNoiseCalibrationMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setnoisecalibrationmode__string-rfmxspecanmxchpnoisecalibrationmode.html) method to [Auto](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html), or set the CHP Noise Cal Mode method to [Manual](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecalibrationmode.html) and [SetMeasurementMode(string, RFmxSpecAnMXChpMeasurementMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setmeasurementmode__string-rfmxspecanmxchpmeasurementmode.html) method to [Measure](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpmeasurementmode.html). Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXChpNoiseCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables noise compensation. |
| True | 1 | Enables noise compensation. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationtype.html language=enus -->
## TOPIC 00139: RFmxSpecAnMXChpNoiseCompensationType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpnoisecompensationtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXChpNoiseCompensationTypeMembersNameValueDescriptionAnalyzerAndTermination0Compensates for noise from the analyzer and

### RFmxSpecAnMXChpNoiseCompensationType Enumeration

Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXChpNoiseCompensationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AnalyzerAndTermination | 0 | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
| AnalyzerOnly | 1 | Compensates for the analyzer noise only. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchprbwfiltertype.html language=enus -->
## TOPIC 00140: RFmxSpecAnMXChpRbwFilterType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchprbwfiltertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital resolution bandwidth (RBW) filter. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXChpRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW f

### RFmxSpecAnMXChpRbwFilterType Enumeration

Specifies the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXChpRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchmeasurement__string-double-out-out-out.html language=enus -->
## TOPIC 00141: FetchMeasurement(string, double, out double, out double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchmeasurement__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchmeasurement__string-double-out-out-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged channel power (CHP) measurements. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchMeasurement(string selectorString, double timeout, out double averageChannelPower, out double averageChannelPsd, out double frequencyResolution)RemarksThis method maps to the RFmx

### FetchMeasurement(string, double, out double, out double, out double)

Fetches the averaged channel power (CHP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchMeasurement(string selectorString, double timeout, out double averageChannelPower, out double averageChannelPsd, out double frequencyResolution)

#### Remarks

This method maps to the RFmxSpecAn_CHPFetchMeasurement() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| averageChannelPower | out double | Upon return, contains the averaged CHP, in dBm, measured in the specified integration bandwidth. |
| averageChannelPsd | out double | Upon return, contains the power spectral density of the channel, in dBm/Hz. |
| frequencyResolution | out double | Upon return, contains the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchspectrum__string-double-ref.html language=enus -->
## TOPIC 00142: FetchSpectrum(string, double, ref Spectrum< float >)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchspectrum__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchspectrum__string-double-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum)RemarksThis method maps to the RFmxSpecAn_CHPFetchSpectrum() function in C.ParametersNameTyp

### FetchSpectrum(string, double, ref Spectrum< float >)

Fetches the spectrum used for channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum)

#### Remarks

This method maps to the RFmxSpecAn_CHPFetchSpectrum() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| spectrum | ref Spectrum< float > | Upon return, contains the spectrum trace values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchtotalcarrierpower__string-double-out.html language=enus -->
## TOPIC 00143: FetchTotalCarrierPower(string, double, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchtotalcarrierpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-fetchtotalcarrierpower__string-double-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total integrated carrier power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int FetchTotalCarrierPower(string selectorString, double timeout, out double totalCarrierPower)RemarksThis method maps to the RFmxSpecAn_CHPFetchTotalCarrierPower() function in C.ParametersNameTypeDe

### FetchTotalCarrierPower(string, double, out double)

Fetches the total integrated carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int FetchTotalCarrierPower(string selectorString, double timeout, out double totalCarrierPower)

#### Remarks

This method maps to the RFmxSpecAn_CHPFetchTotalCarrierPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalCarrierPower | out double | Upon return, contains the total integrated power of all carriers, in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getaveragechannelpowerpsd__string-out.html language=enus -->
## TOPIC 00144: GetAverageChannelPowerPsd(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getaveragechannelpowerpsd__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getaveragechannelpowerpsd__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the spectral density of the averaged channel power (CHP), in dBm/Hz, of the channel. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAverageChannelPowerPsd(string selectorString, out double value)RemarksThis method is obsoleted. Use GetAverageCarrierPsd to get the value. This me

### GetAverageChannelPowerPsd(string, out double)

Gets the spectral density of the averaged channel power (CHP), in dBm/Hz, of the channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAverageChannelPowerPsd(string selectorString, out double value)

#### Remarks

This method is obsoleted. Use GetAverageCarrierPsd to get the value. This method maps to the RFmxSpecAn_CHPGetResultsAverageChannelPSD() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| value | out double | Upon return, contains the spectral density of the averaged CHP, in dBm/Hz, of the channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierabsolutepower__string-out.html language=enus -->
## TOPIC 00145: GetCarrierAbsolutePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierabsolutepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier power, in dBm, measured in the integration bandwidth that you specify in the SetIntegrationBandwidth(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierAbsolutePower(string selectorString, out double value)RemarksThis method maps to the RF

### GetCarrierAbsolutePower(string, out double)

Gets the carrier power, in dBm, measured in the integration bandwidth that you specify in the [SetIntegrationBandwidth(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxchpconfiguration-setintegrationbandwidth__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierAbsolutePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetResultsCarrierAbsolutePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier power, in dBm, measured in the integration bandwidth that you specify in the SetIntegrationBandwidth(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierfrequency__string-out.html language=enus -->
## TOPIC 00146: GetCarrierFrequency(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierfrequency__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the center frequency, in hertz (Hz), of the carrier relative to the SetCenterFrequency(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierFrequency(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetResultsCarrierF

### GetCarrierFrequency(string, out double)

Gets the center frequency, in hertz (Hz), of the carrier relative to the [SetCenterFrequency(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmx-setcenterfrequency__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierFrequency(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetResultsCarrierFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string.. |
| value | out double | Upon return, contains the center frequency, in Hz, of the carrier relative to the SetCenterFrequency(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00147: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetResultsCarrierIntegrat

### GetCarrierIntegrationBandwidth(string, out double)

Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetResultsCarrierIntegrationBandwidth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency range, in Hz, over which the measurement integrates the carrier power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierrelativepower__string-out.html language=enus -->
## TOPIC 00148: GetCarrierRelativePower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-getcarrierrelativepower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier power, in dB, measured relative to the total carrier power of all carriers. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierRelativePower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetResultsCarrierRelativePower() func

### GetCarrierRelativePower(string, out double)

Gets the carrier power, in dB, measured relative to the total carrier power of all carriers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierRelativePower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetResultsCarrierRelativePower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and carrier number. Example: "carrier0", "result::r1/carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier power, in dB, measured relative to the total carrier power of all carriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-gettotalcarrierpower__string-out.html language=enus -->
## TOPIC 00149: GetTotalCarrierPower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-gettotalcarrierpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults-gettotalcarrierpower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total integrated carrier power of all carriers, in dBm. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetTotalCarrierPower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_CHPGetResultsTotalCarrierPower() function in C.ParametersNameTypeDescri

### GetTotalCarrierPower(string, out double)

Gets the total integrated carrier power of all carriers, in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetTotalCarrierPower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_CHPGetResultsTotalCarrierPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| value | out double | Upon return, contains the total integrated carrier power of all carriers, in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXChpResults Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults.html language=enus -->
## TOPIC 00150: RFmxSpecAnMXChpResults Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxchpresults.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the channel power (CHP) measurement results. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXChpResults : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.T

### RFmxSpecAnMXChpResults Class

Provides methods to fetch and read the channel power (CHP) measurement results.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXChpResults : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| FetchCarrierMeasurement(string, double, out double, out double, out double) | Fetches channel power (CHP) measurement results. |
| FetchMeasurement(string, double, out double, out double, out double) | Fetches the averaged channel power (CHP) measurements. |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for channel power (CHP) measurement. |
| FetchTotalCarrierPower(string, double, out double) | Fetches the total integrated carrier power. |
| GetAverageChannelPower(string, out double) | Gets the averaged channel power (CHP), in dBm, measured in the specified integration bandwidth. |
| GetAverageChannelPowerPsd(string, out double) | Gets the spectral density of the averaged channel power (CHP), in dBm/Hz, of the channel. |
| GetCarrierAbsolutePower(string, out double) | Gets the carrier power, in dBm, measured in the integration bandwidth that you specify in the SetIntegrationBandwidth(string, double) method. |
| GetCarrierFrequency(string, out double) | Gets the center frequency, in hertz (Hz), of the carrier relative to the SetCenterFrequency(string, double) method. |
| GetCarrierIntegrationBandwidth(string, out double) | Gets the frequency range, in hertz (Hz), over which the measurement integrates the carrier power. |
| GetCarrierPsd(string, out double) | Gets the power spectral density, in dBm/Hz, of the channel. |
| GetCarrierRelativePower(string, out double) | Gets the carrier power, in dB, measured relative to the total carrier power of all carriers. |
| GetFrequencyResolution(string, out double) | Gets the frequency resolution, in hertz (Hz), of the spectrum acquired by the measurement. |
| GetTotalCarrierPower(string, out double) | Gets the total integrated carrier power of all carriers, in dBm. |
| Read(string, double, out double, out double) | Configures hardware for acquisition, performs measurement on acquired data, and returns the channel power (CHP) measurement results. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pfi1.html language=enus -->
## TOPIC 00151: Pfi1

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pfi1.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public const string Pfi1

Parent topic:

RFmxSpecAnMXConstants Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00152: PxieDStarBLine

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxiedstarbline.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXIe DStar B trigger line. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic const string PxieDStarBLine

### PxieDStarBLine

The signal is exported to the PXIe DStar B trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public const string PxieDStarBLine

Parent topic:

RFmxSpecAnMXConstants Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxistarline.html language=enus -->
## TOPIC 00153: PxiStarLine

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxistarline.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI star trigger line. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic const string PxiStarLine

### PxiStarLine

The signal is exported to the PXI star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public const string PxiStarLine

Parent topic:

RFmxSpecAnMXConstants Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00154: PxiTriggerLine3

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-pxitriggerline3.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

The signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxSpecAnMXConstants Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-timerevent.html language=enus -->
## TOPIC 00155: TimerEvent

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants-timerevent.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public const string TimerEvent

Parent topic:

RFmxSpecAnMXConstants Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants.html language=enus -->
## TOPIC 00156: RFmxSpecAnMXConstants Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxconstants.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXConstantsRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny public static members of this type are thread safe. Any instance me

### RFmxSpecAnMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXConstants

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

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
| Pfi0 | The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. |
| Pfi1 | The signal is exported to the PXI trigger line 0. |
| PulseIn |  |
| PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. |
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

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00157: RFmxSpecAnMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdigitaledgetriggeredge.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This enum is used only when you set the SetTriggerType(string, RFmxSpecAnMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asse

### RFmxSpecAnMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This enum is used only when you set the [SetTriggerType(string, RFmxSpecAnMXTriggerType)](nationalinstruments-rfmx-specanmx-rfmxspecanmx-settriggertype__string-rfmxspecanmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-specanmx-rfmxspecanmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-applydpd.html language=enus -->
## TOPIC 00158: ApplyDpd

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-applydpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-applydpd.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXDpdApplyDpd instance that provides methods to apply DPD measurements. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXDpdApplyDpd ApplyDpd { get; }

### ApplyDpd

Gets the [RFmxSpecAnMXDpdApplyDpd](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd.html) instance that provides methods to apply DPD measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXDpdApplyDpd](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd.html) ApplyDpd { get; }

Parent topic:

RFmxSpecAnMXDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-predpd.html language=enus -->
## TOPIC 00159: PreDpd

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-predpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-predpd.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXDpdPreDpd instance that provides methods to apply DPD measurements. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXDpdPreDpd PreDpd { get; }

### PreDpd

Gets the [RFmxSpecAnMXDpdPreDpd](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd.html) instance that provides methods to apply DPD measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXDpdPreDpd](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd.html) PreDpd { get; }

Parent topic:

RFmxSpecAnMXDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-results.html language=enus -->
## TOPIC 00160: Results

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd-results.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXDpdResults instance that provides methods to retrieve the DPD measurement results. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXDpdResults Results { get; }

### Results

Gets the [RFmxSpecAnMXDpdResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdresults.html) instance that provides methods to retrieve the DPD measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXDpdResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdresults.html) Results { get; }

Parent topic:

RFmxSpecAnMXDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd.html language=enus -->
## TOPIC 00161: RFmxSpecAnMXDpd Class

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpd.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DPD measurement. Derives fromRFmxSpecAnMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic class RFmxSpecAnMXDpd : RFmxSpecAnMXSubObjectRemarksFor more information about RFmx SpecAn, refer to the RFmx SpecAn Help.Thread SafetyAny public static members of this type are th

### RFmxSpecAnMXDpd Class

Represents a DPD measurement.

#### Derives from

- RFmxSpecAnMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public class RFmxSpecAnMXDpd : RFmxSpecAnMXSubObject

#### Remarks

For more information about RFmx SpecAn, refer to the RFmx SpecAn Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ApplyDpd | Gets the RFmxSpecAnMXDpdApplyDpd instance that provides methods to apply DPD measurements. |
| Configuration | Gets the RFmxSpecAnMXDpdConfiguration instance that allows configuration of DPD measurement. |
| PreDpd | Gets the RFmxSpecAnMXDpdPreDpd instance that provides methods to apply DPD measurements. |
| Results | Gets the RFmxSpecAnMXDpdResults instance that provides methods to retrieve the DPD measurement results. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-applydpd__string-complexwaveform_complexsingle_-rfmxspecanmxdpdapplydpdidledurationpresent-double-ref-out.html language=enus -->
## TOPIC 00162: ApplyDpd(string, ComplexWaveform< ComplexSingle >, RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, double, ref ComplexWaveform< ComplexSingle >, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-applydpd__string-complexwaveform_complexsingle_-rfmxspecanmxdpdapplydpdidledurationpresent-double-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-applydpd__string-complexwaveform_complexsingle_-rfmxspecanmxdpdapplydpdidledurationpresent-double-ref-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Scales the input waveform to DUT Average Input Power and then predistorts the waveform using the DPD polynomial or the lookup table. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ApplyDpd(string selectorString, ComplexWaveform< ComplexSingle > waveformIn, RFmxSpecAnMXDpdApplyDpdIdleDu

### ApplyDpd(string, ComplexWaveform< ComplexSingle >, RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, double, ref ComplexWaveform< ComplexSingle >, out double)

Scales the input waveform to DUT Average Input Power and then predistorts the waveform using the DPD polynomial or the lookup table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ApplyDpd(string selectorString, ComplexWaveform< ComplexSingle > waveformIn, RFmxSpecAnMXDpdApplyDpdIdleDurationPresent idleDurationPresent, double measurementTimeout, ref ComplexWaveform< ComplexSingle > waveformOut, out double appliedHeadroom)

#### Remarks

To scale the waveform correctly, specify whether the idle duration is present in the waveform. 
 This method maps to the RFmxSpecAn_DPDApplyDPD() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| waveformIn | ComplexWaveform< ComplexSingle > | Specifies the complex baseband equivalent of the RF signal on which to apply digital predistortion. |
| idleDurationPresent | RFmxSpecAnMXDpdApplyDpdIdleDurationPresent | Specifies whether the waveform contains an idle duration. |
| measurementTimeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. |
| appliedHeadroom | out double | Specifies the headroom, in dB, applied to the predistorted waveform when you set the headroomMode parameter to Manual. |
| waveformOut | ref ComplexWaveform< ComplexSingle > | Upon return, contains the complex baseband equivalent of the RF signal on which to apply digital predistortion. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-configureheadroom__string-rfmxspecanmxdpdapplydpdheadroommode-double.html language=enus -->
## TOPIC 00163: ConfigureHeadroom(string, RFmxSpecAnMXDpdApplyDpdHeadroomMode, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-configureheadroom__string-rfmxspecanmxdpdapplydpdheadroommode-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-configureheadroom__string-rfmxspecanmxdpdapplydpdheadroommode-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the headroom, in dB, for the predistorted waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureHeadroom(string selectorString, RFmxSpecAnMXDpdApplyDpdHeadroomMode headroomMode, double headroom)RemarksThis method maps to the RFmxSpecAn_DPDCfgApplyDPDHeadroom() fu

### ConfigureHeadroom(string, RFmxSpecAnMXDpdApplyDpdHeadroomMode, double)

Configures the headroom, in dB, for the predistorted waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureHeadroom(string selectorString, RFmxSpecAnMXDpdApplyDpdHeadroomMode headroomMode, double headroom)

#### Remarks

This method maps to the RFmxSpecAn_DPDCfgApplyDPDHeadroom() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| headroomMode | RFmxSpecAnMXDpdApplyDpdHeadroomMode | Specifies the mode of applying headroom on the predistorted waveform. |
| headroom | double | Specifies the headroom, in dB, to apply to the predistorted waveform when you set the headroomMode parameter to Manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getapplydpduserlookuptabletype__string-out.html language=enus -->
## TOPIC 00164: GetApplyDpdUserLookupTableType(string, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getapplydpduserlookuptabletype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getapplydpduserlookuptabletype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DPD Lookup Table (LUT) type. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetApplyDpdUserLookupTableType(string selectorString, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType value)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is

### GetApplyDpdUserLookupTableType(string, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType)

Gets the DPD Lookup Table (LUT) type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetApplyDpdUserLookupTableType(string selectorString, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdApplyDpdUserLookupTableType | Upon return, contains the the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrshapingthreshold__string-out.html language=enus -->
## TOPIC 00165: GetCfrShapingThreshold(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrshapingthreshold__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrshapingthreshold__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shaping threshold to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic

### GetCfrShapingThreshold(string, out double)

Gets the shaping threshold to be used when you set the [DpdApplyDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrenabled.html) and the [DpdApplyDpdCfrMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [Sigmoid](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrmethod.html). This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrShapingThreshold(string selectorString, out double value)

#### Remarks

This method gets the value of [DpdApplyDpdCfrShapingThreshold](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is -5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the shaping threshold to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrtargetpaprtype__string-out.html language=enus -->
## TOPIC 00166: GetCfrTargetPaprType(string, out RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrtargetpaprtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrtargetpaprtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the target PAPR type when you set the DpdApplyDpdCfrEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCfrTargetPaprType(string selectorString, out RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType value)RemarksThis method gets the value of DpdApplyDpdCfrTargetPaprTy

### GetCfrTargetPaprType(string, out RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType)

Gets the target PAPR type when you set the [DpdApplyDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrTargetPaprType(string selectorString, out RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType value)

#### Remarks

This method gets the value of [DpdApplyDpdCfrTargetPaprType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [InputPapr](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrtargetpaprtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType | Upon return, contains the target PAPR type when you set the DpdApplyDpdCfrEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrwindowtype__string-out.html language=enus -->
## TOPIC 00167: GetCfrWindowType(string, out RFmxSpecAnMXDpdApplyDpdCfrWindowType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrwindowtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getcfrwindowtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the window type to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCfrWindowType(string selectorString, out RFmxSpecAnMXDpdApplyDpdCfrWindowType value)RemarksThis

### GetCfrWindowType(string, out RFmxSpecAnMXDpdApplyDpdCfrWindowType)

Gets the window type to be used when you set the [DpdApplyDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrenabled.html) and the [DpdApplyDpdCfrMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [PeakWindowing](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrWindowType(string selectorString, out RFmxSpecAnMXDpdApplyDpdCfrWindowType value)

#### Remarks

This method gets the value of [DpdApplyDpdCfrWindowType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is Kaiser-Bessel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdApplyDpdCfrWindowType | Upon return, contains the window type to be used when you set the DpdApplyDpdCfrEnabled method to True and the DpdApplyDpdCfrMethod method to PeakWindowing. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getheadroommode__string-out.html language=enus -->
## TOPIC 00168: GetHeadroomMode(string, out RFmxSpecAnMXDpdApplyDpdHeadroomMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getheadroommode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getheadroommode__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to compute and apply the headroom of the predistorted waveform or to apply the value that you specify using the SetHeadroom(string, double) method on the predistorted waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetHeadroomMode(string selectorString, out RFmxSp

### GetHeadroomMode(string, out RFmxSpecAnMXDpdApplyDpdHeadroomMode)

Gets whether to compute and apply the headroom of the predistorted waveform or to apply the value that you specify using the [SetHeadroom(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setheadroom__string-double.html) method on the predistorted waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetHeadroomMode(string selectorString, out RFmxSpecAnMXDpdApplyDpdHeadroomMode value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDHeadroomMode() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdApplyDpdHeadroomMode | Upon return, contains a value that indicates whether to compute and apply the headroom of the predistorted waveform or to apply the value that you specify using SetHeadroom(string, double) on the predistorted waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getlookuptablecorrectiontype__string-out.html language=enus -->
## TOPIC 00169: GetLookupTableCorrectionType(string, out RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getlookuptablecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getlookuptablecorrectiontype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the predistortion type. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableCorrectionType(string selectorString, out RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType value)RemarksThis method maps to the RFmxSpecAn_DPDGetApplyDPDLookupTableCorrectionType() function in C.P

### GetLookupTableCorrectionType(string, out RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType)

Gets the predistortion type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableCorrectionType(string selectorString, out RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDLookupTableCorrectionType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType | Upon return, contains a value that indicates the predistortion type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getuserdutaverageinputpower__string-out.html language=enus -->
## TOPIC 00170: GetUserDutAverageInputPower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getuserdutaverageinputpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getuserdutaverageinputpower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUserDutAverageInputPower(string selectorString, out double value)RemarksThis method maps to th

### GetUserDutAverageInputPower(string, out double)

Gets the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUserDutAverageInputPower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserDUTAverageInputPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getuserlookuptableinputpower__string-ref.html language=enus -->
## TOPIC 00171: GetUserLookupTableInputPower(string, ref float[])

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getuserlookuptableinputpower__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getuserlookuptableinputpower__string-ref.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the input power array, in dBm, for the predistortion lookup table. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetUserLookupTableInputPower(string selectorString, ref float[] value)RemarksThis method maps to the RFmxSpecAn_DPDGetApplyDPDUserLookupTableInputPower() function in C

### GetUserLookupTableInputPower(string, ref float[])

Gets the input power array, in dBm, for the predistortion lookup table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetUserLookupTableInputPower(string selectorString, ref float[] value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetApplyDPDUserLookupTableInputPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref float[] | Upon return, contains the input power array, in dBm, for the predistortion lookup table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setheadroommode__string-rfmxspecanmxdpdapplydpdheadroommode.html language=enus -->
## TOPIC 00172: SetHeadroomMode(string, RFmxSpecAnMXDpdApplyDpdHeadroomMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setheadroommode__string-rfmxspecanmxdpdapplydpdheadroommode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setheadroommode__string-rfmxspecanmxdpdapplydpdheadroommode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to compute and apply the headroom of the predistorted waveform, or to apply the value that you specify using the SetHeadroom(string, double) method, on the predistorted waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetHeadroomMode(string selectorString, RFmxSpec

### SetHeadroomMode(string, RFmxSpecAnMXDpdApplyDpdHeadroomMode)

Sets whether to compute and apply the headroom of the predistorted waveform, or to apply the value that you specify using the [SetHeadroom(string, double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setheadroom__string-double.html) method, on the predistorted waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetHeadroomMode(string selectorString, RFmxSpecAnMXDpdApplyDpdHeadroomMode value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDHeadroomMode() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdApplyDpdHeadroomMode | Contains a value that indicates whether to compute and apply the headroom of the predistorted waveform, or to apply the value that you specify using the SetHeadroom(string, double) method, on the predistorted waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setmemorymodelcorrectiontype__string-rfmxspecanmxdpdapplydpdmemorymodelcorrectiontype.html language=enus -->
## TOPIC 00173: SetMemoryModelCorrectionType(string, RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setmemorymodelcorrectiontype__string-rfmxspecanmxdpdapplydpdmemorymodelcorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setmemorymodelcorrectiontype__string-rfmxspecanmxdpdapplydpdmemorymodelcorrectiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the predistortion type when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMemoryModelCorrectionType(string selectorString, RFmxSpecAnMXDpdApplyDpdMemoryModelCorrection

### SetMemoryModelCorrectionType(string, RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType)

Sets the predistortion type when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [MemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) or [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryModelCorrectionType(string selectorString, RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDpdMemoryModelCorrectionType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType | Contains a value that indicates the predistortion type when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdutaverageinputpower__string-double.html language=enus -->
## TOPIC 00174: SetUserDutAverageInputPower(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdutaverageinputpower__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdutaverageinputpower__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain when you set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpub

### SetUserDutAverageInputPower(string, double)

Sets the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain when you set the [SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setconfigurationinput__string-rfmxspecanmxdpdapplydpdconfigurationinput.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdconfigurationinput.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetUserDutAverageInputPower(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetApplyDPDUserDUTAverageInputPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Contains the average input power for the device under test, in dBm, used to compute the DPD User DPD Polynomial or the DPD User LUT Complex Gain when you set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdApplyDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrenabled.html language=enus -->
## TOPIC 00175: RFmxSpecAnMXDpdApplyDpdCfrEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdcfrenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the crest factor reduction (CFR) on the pre-distorted waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdApplyDpdCfrEnabledMembersNameValueDescriptionFalse0Disables CFR. The maximum increase in PAPR, after pre-distortion, is limited to

### RFmxSpecAnMXDpdApplyDpdCfrEnabled Enumeration

Specifies whether to enable the crest factor reduction (CFR) on the pre-distorted waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdApplyDpdCfrEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables CFR. The maximum increase in PAPR, after pre-distortion, is limited to 6 dB. |
| True | 1 | Enables CFR. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdheadroommode.html language=enus -->
## TOPIC 00176: RFmxSpecAnMXDpdApplyDpdHeadroomMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdheadroommode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdheadroommode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compute and apply the headroom of the predistorted waveform or to apply the value specified by GetHeadroom(string, out double) on the predistorted waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdApplyDpdHeadroomModeMembersNameValueDescripti

### RFmxSpecAnMXDpdApplyDpdHeadroomMode Enumeration

Specifies whether to compute and apply the headroom of the predistorted waveform or to apply the value specified by [GetHeadroom(string, out double)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-getheadroom__string-out.html) on the predistorted waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdApplyDpdHeadroomMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | The measurement returns the predistorted waveform without applying headroom. |
| Auto | 1 | The measurement returns the predistorted waveform after computing and applying the headroom. |
| Manual | 2 | The measurement returns the predistorted waveform after applying the headroom that you specify in the SetHeadroom(string, double) method. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdidledurationpresent.html language=enus -->
## TOPIC 00177: RFmxSpecAnMXDpdApplyDpdIdleDurationPresent Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdidledurationpresent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdidledurationpresent.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the waveform contains an idle duration. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdApplyDpdIdleDurationPresentMembersNameValueDescriptionFalse0The reference waveform does not contain an idle duration. True1The reference waveform contains an idle du

### RFmxSpecAnMXDpdApplyDpdIdleDurationPresent Enumeration

Specifies whether the waveform contains an idle duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdApplyDpdIdleDurationPresent

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The reference waveform does not contain an idle duration. |
| True | 1 | The reference waveform contains an idle duration. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdlookuptablecorrectiontype.html language=enus -->
## TOPIC 00178: RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdlookuptablecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdlookuptablecorrectiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the predistortion type when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionTypeMembersNameValueDescriptionMagnitudeAndPhase0The measurement predistorts the m

### RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType Enumeration

Specifies the predistortion type when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [LookupTable](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MagnitudeAndPhase | 0 | The measurement predistorts the magnitude and phase of the input waveform. |
| MagnitudeOnly | 1 | The measurement predistorts only the phase of the input waveform. |
| PhaseOnly | 2 | The measurement predistorts only the magnitude of the input waveform. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdmemorymodelcorrectiontype.html language=enus -->
## TOPIC 00179: RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdmemorymodelcorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdmemorymodelcorrectiontype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the predistortion type when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionTypeMembersNameValueDescriptionMagnitudeAndPha

### RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType Enumeration

Specifies the predistortion type when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [MemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) or [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MagnitudeAndPhase | 0 | The measurement predistorts the magnitude and phase of the input waveform. |
| MagnitudeOnly | 1 | The measurement predistorts only the magnitude of the input waveform. |
| PhaseOnly | 2 | The measurement predistorts only the phase of the input waveform. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html language=enus -->
## TOPIC 00180: RFmxSpecAnMXDpdApplyDpdUserDpdModel Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DPD model for applying DPD when you set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdApplyDpdUserDpdModelMembersNameValueDescriptionLookupTable0This model comput

### RFmxSpecAnMXDpdApplyDpdUserDpdModel Enumeration

Specifies the DPD model for applying DPD when you set the [SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setconfigurationinput__string-rfmxspecanmxdpdapplydpdconfigurationinput.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdconfigurationinput.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdApplyDpdUserDpdModel

#### Members

| Name | Value | Description |
| --- | --- | --- |
| LookupTable | 0 | This model computes the complex gain coefficients applied while performing digital predistortion to linearize systems with negligible memory effects. |
| MemoryPolynomial | 1 | This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. |
| GeneralizedMemoryPolynomial | 2 | This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdaveragingenabled.html language=enus -->
## TOPIC 00181: RFmxSpecAnMXDpdAveragingEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdaveragingenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the DPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdAveragingEnabledMembersNameValueDescriptionFalse0Performs the measurement on a single acquisition. True1The DPD measurement uses the value returned by GetAverag

### RFmxSpecAnMXDpdAveragingEnabled Enumeration

Specifies whether to enable averaging for the DPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Performs the measurement on a single acquisition. |
| True | 1 | The DPD measurement uses the value returned by GetAveragingCount(string, out int) as the number of acquisitions over which to average the signal. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configurelookuptablethreshold__string-rfmxspecanmxdpdlookuptablethresholdenabled-double-rfmxspecanmxdpdlookuptablethresholdtype.html language=enus -->
## TOPIC 00182: ConfigureLookupTableThreshold(string, RFmxSpecAnMXDpdLookupTableThresholdEnabled, double, RFmxSpecAnMXDpdLookupTableThresholdType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configurelookuptablethreshold__string-rfmxspecanmxdpdlookuptablethresholdenabled-double-rfmxspecanmxdpdlookuptablethresholdtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configurelookuptablethreshold__string-rfmxspecanmxdpdlookuptablethresholdenabled-double-rfmxspecanmxdpdlookuptablethresholdtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the threshold level for the samples considered for the DPD measurement when you set the SetModel(string, RFmxSpecAnMXDpdModel) to LookupTable. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureLookupTableThreshold(string selectorString, RFmxSpecAnMXDpdLookupTableThresh

### ConfigureLookupTableThreshold(string, RFmxSpecAnMXDpdLookupTableThresholdEnabled, double, RFmxSpecAnMXDpdLookupTableThresholdType)

Configures the threshold level for the samples considered for the DPD measurement when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) to [LookupTable](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureLookupTableThreshold(string selectorString, RFmxSpecAnMXDpdLookupTableThresholdEnabled thresholdEnabled, double thresholdLevel, RFmxSpecAnMXDpdLookupTableThresholdType thresholdType)

#### Remarks

This method maps to the RFmxSpecAn_DPDCfgLookupTableThreshold() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| thresholdEnabled | RFmxSpecAnMXDpdLookupTableThresholdEnabled | Specifies whether to enable thresholding for the acquired samples used in the DPD measurement. |
| thresholdLevel | double | Specifies either the relative or the absolute threshold power level based on the value of the thresholdType parameter. |
| thresholdType | RFmxSpecAnMXDpdLookupTableThresholdType | Specifies the reference for the power level used for thresholding. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configuremeasurementinterval__string-double.html language=enus -->
## TOPIC 00183: ConfigureMeasurementInterval(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configuremeasurementinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configuremeasurementinterval__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference wavefo

### ConfigureMeasurementInterval(string, double)

Configures the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureMeasurementInterval(string selectorString, double measurementInterval)

#### Remarks

This method maps to the RFmxSpecAn_DPDCfgMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading upto the start of the first active portion of the reference waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configurememorypolynomial__string-int-int.html language=enus -->
## TOPIC 00184: ConfigureMemoryPolynomial(string, int, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configurememorypolynomial__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-configurememorypolynomial__string-int-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the order and memory depth of the DPD polynomial when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int ConfigureMemoryPolynomial(string selectorString, int memoryPolyn

### ConfigureMemoryPolynomial(string, int, int)

Configures the order and memory depth of the DPD polynomial when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [MemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) or [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int ConfigureMemoryPolynomial(string selectorString, int memoryPolynomialOrder, int memoryPolynomialMemoryDepth)

#### Remarks

This method maps to the RFmxSpecAn_DPDCfgMemoryPolynomial() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| memoryPolynomialOrder | int | Specifies the order of the DPD polynomial when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |
| memoryPolynomialMemoryDepth | int | Specifies the memory depth of the DPD polynomial when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00185: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the DPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_DPDGetAllTracesEnabled() function in C.P

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the DPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if the traces to be stored and retrieved after performing the DPD measurement are enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getapplydpduserlookuptabletype__string-out.html language=enus -->
## TOPIC 00186: GetApplyDpdUserLookupTableType(string, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getapplydpduserlookuptabletype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getapplydpduserlookuptabletype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method toUser. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetApplyDpdUserLookupTableType(string selectorString, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType value)RemarksThis method gets the value

### GetApplyDpdUserLookupTableType(string, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType)

Gets the DPD Lookup Table (LUT) type when you set the [DpdApplyDpdConfigurationInput](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method toUser.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetApplyDpdUserLookupTableType(string selectorString, out RFmxSpecAnMXDpdApplyDpdUserLookupTableType value)

#### Remarks

This method gets the value of [DpdApplyDpdUserLookupTableType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdApplyDpdUserLookupTableType | Upon return, contains the DPD Lookup Table (LUT) type when you set the DpdApplyDpdConfigurationInput method toUser. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00187: GetAveragingCount(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_DPDGetAveragingCount() function in C.ParametersNameTypeDescriptionselectorStringstringPass

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetAveragingCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00188: GetAveragingEnabled(string, out RFmxSpecAnMXDpdAveragingEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether averaging is enabled for the DPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXDpdAveragingEnabled value)RemarksThis method maps to the RFmxSpecAn_DPDGetAveragingEnabled() function in C.ParametersName

### GetAveragingEnabled(string, out RFmxSpecAnMXDpdAveragingEnabled)

Gets whether averaging is enabled for the DPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxSpecAnMXDpdAveragingEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdAveragingEnabled | Upon return, contains a value that indicates whether averaging is enabled for the DPD measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getcarrierbandwidth__string-out.html language=enus -->
## TOPIC 00189: GetCarrierBandwidth(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getcarrierbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getcarrierbandwidth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierBandwidth(string selectorString, out double value)Rema

### GetCarrierBandwidth(string, out double)

Gets the carrier bandwidth when you set the [SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setautocarrierdetectionenabled__string-rfmxspecanmxdpdautocarrierdetectionenabled.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdautocarrierdetectionenabled.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [DpdCarrierBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 20 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier bandwidth when you set the SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getcarrieroffset__string-out.html language=enus -->
## TOPIC 00190: GetCarrierOffset(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getcarrieroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getcarrieroffset__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier offset when you set the SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCarrierOffset(string selectorString, out double value)RemarksThi

### GetCarrierOffset(string, out double)

Gets the carrier offset when you set the [SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setautocarrierdetectionenabled__string-rfmxspecanmxdpdautocarrierdetectionenabled.html) method to [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdautocarrierdetectionenabled.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCarrierOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [DpdCarrierOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString2(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier offset when you set the SetAutoCarrierDetectionEnabled(string, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdutaverageinputpower__string-out.html language=enus -->
## TOPIC 00191: GetDutAverageInputPower(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdutaverageinputpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdutaverageinputpower__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power, in dBm, of the signal at the input port of the device under test. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetDutAverageInputPower(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_DPDGetDUTAverageInputPower() function in C.

### GetDutAverageInputPower(string, out double)

Gets the average power, in dBm, of the signal at the input port of the device under test.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDutAverageInputPower(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetDUTAverageInputPower() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the average power, in dBm, of the signal at the input port of the device under test. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdvrnonlinearmemorydepth__string-out.html language=enus -->
## TOPIC 00192: GetDvrNonlinearMemoryDepth(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdvrnonlinearmemorydepth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdvrnonlinearmemorydepth__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the nonlinear memory depth of the Decomposed Vector Rotation model when you set the DpdModel method to DecomposedVectorRotation. This value corresponds to Mnl in the equation for the decomposed vector rotation model. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetDvrNonlinearMe

### GetDvrNonlinearMemoryDepth(string, out int)

Gets the nonlinear memory depth of the Decomposed Vector Rotation model when you set the [DpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [DecomposedVectorRotation](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html). This value corresponds to Mnl in the equation for the decomposed vector rotation model.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDvrNonlinearMemoryDepth(string selectorString, out int value)

#### Remarks

This method gets the value of [DpdDvrNonlinearMemoryDepth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 2. This value must be greater than or equal to 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the nonlinear memory depth of the Decomposed Vector Rotation model when you set the DpdModel method to DecomposedVectorRotation. This value corresponds to Mnl in the equation for the decomposed vector rotation model. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdvrnumberofsegments__string-out.html language=enus -->
## TOPIC 00193: GetDvrNumberOfSegments(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdvrnumberofsegments__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getdvrnumberofsegments__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of segments of the Decomposed Vector Rotation model when you set the DpdModel method to DecomposedVectorRotation. This value corresponds to K in the equation for the Decomposed Vector Rotation model. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetDvrNumberOfSegments(

### GetDvrNumberOfSegments(string, out int)

Gets the number of segments of the Decomposed Vector Rotation model when you set the [DpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [DecomposedVectorRotation](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html). This value corresponds to K in the equation for the Decomposed Vector Rotation model.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetDvrNumberOfSegments(string selectorString, out int value)

#### Remarks

This method gets the value of [DpdDvrNumberOfSegments](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 4. This value must be greater than or equal to 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of segments of the Decomposed Vector Rotation model when you set the DpdModel method to DecomposedVectorRotation. This value corresponds to K in the equation for the Decomposed Vector Rotation model. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getfrequencyoffsetcorrectionenabled__string-out.html language=enus -->
## TOPIC 00194: GetFrequencyOffsetCorrectionEnabled(string, out RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getfrequencyoffsetcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getfrequencyoffsetcorrectionenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable frequency offset correction for the DPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetFrequencyOffsetCorrectionEnabled(string selectorString, out RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled value)RemarksThis method gets the value of DpdFreque

### GetFrequencyOffsetCorrectionEnabled(string, out RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled)

Gets whether to enable frequency offset correction for the DPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetFrequencyOffsetCorrectionEnabled(string selectorString, out RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled value)

#### Remarks

This method gets the value of [DpdFrequencyOffsetCorrectionEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdfrequencyoffsetcorrectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled | Upon return, contains whether to enable frequency offset correction for the DPD measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getiqoriginoffsetcorrectionenabled__string-out.html language=enus -->
## TOPIC 00195: GetIQOriginOffsetCorrectionEnabled(string, out RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getiqoriginoffsetcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getiqoriginoffsetcorrectionenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the IQ origin offset correction for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetIQOriginOffsetCorrectionEnabled(string selectorString, out RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled value)ParametersNameTypeDescriptionselectorStringstringPass an empty str

### GetIQOriginOffsetCorrectionEnabled(string, out RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled)

Gets the IQ origin offset correction for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIQOriginOffsetCorrectionEnabled(string selectorString, out RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled | Upon return, indicates whether the IQ origin offset correction for the measurement is enabled. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getiterativedpdenabled__string-out.html language=enus -->
## TOPIC 00196: GetIterativeDpdEnabled(string, out RFmxSpecAnMXDpdIterativeDpdEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getiterativedpdenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getiterativedpdenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetIterativeDpdEnabled(string selectorString, out RFmxSpecAnMXDpdIterativeDpdEnabled value)RemarksThis method maps to the

### GetIterativeDpdEnabled(string, out RFmxSpecAnMXDpdIterativeDpdEnabled)

Gets whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetIterativeDpdEnabled(string selectorString, out RFmxSpecAnMXDpdIterativeDpdEnabled value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetIterativeDPDEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdIterativeDpdEnabled | Upon return, contains a value that indicates whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtoamcurvefitorder__string-out.html language=enus -->
## TOPIC 00197: GetLookupTableAMToAMCurveFitOrder(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtoamcurvefitorder__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtoamcurvefitorder__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableAMToAMCurveFitOrder(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_DPDGetLookupTableA

### GetLookupTableAMToAMCurveFitOrder(string, out int)

Gets the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableAMToAMCurveFitOrder(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableAMtoAMCurveFitOrder() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the degree of the polynomial used to approximate the AM-to-AM characteristic of the device under test. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtoamcurvefittype__string-out.html language=enus -->
## TOPIC 00198: GetLookupTableAMToAMCurveFitType(string, out RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtoamcurvefittype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtoamcurvefittype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the polynomial approximation cost-function of the device under test AM-to-AM characteristic. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableAMToAMCurveFitType(string selectorString, out RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType value)RemarksThis method maps to the

### GetLookupTableAMToAMCurveFitType(string, out RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType)

Gets the polynomial approximation cost-function of the device under test AM-to-AM characteristic.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableAMToAMCurveFitType(string selectorString, out RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableAMtoAMCurveFitType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType | Upon return, contains the polynomial approximation cost-function of the device under test AM-to-AM characteristic. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtopmcurvefitorder__string-out.html language=enus -->
## TOPIC 00199: GetLookupTableAMToPMCurveFitOrder(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtopmcurvefitorder__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtopmcurvefitorder__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableAMToPMCurveFitOrder(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_DPDGetLookupTableA

### GetLookupTableAMToPMCurveFitOrder(string, out int)

Gets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableAMToPMCurveFitOrder(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableAMtoPMCurveFitOrder() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtopmcurvefittype__string-out.html language=enus -->
## TOPIC 00200: GetLookupTableAMToPMCurveFitType(string, out RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtopmcurvefittype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptableamtopmcurvefittype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the cost-function for polynomial approximation of the AM-to-PM characteristic of the device under test. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableAMToPMCurveFitType(string selectorString, out RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType value)RemarksThis method

### GetLookupTableAMToPMCurveFitType(string, out RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType)

Gets the cost-function for polynomial approximation of the AM-to-PM characteristic of the device under test.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableAMToPMCurveFitType(string selectorString, out RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableAMtoPMCurveFitType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType | Upon return, contains the cost-function for polynomial approximation of the AM-to-PM characteristic of the device under test. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablestepsize__string-out.html language=enus -->
## TOPIC 00201: GetLookupTableStepSize(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablestepsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablestepsize__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the step size, in dB, of the input power levels in the predistortion lookup table. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableStepSize(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_DPDGetLookupTableStepSize() function in C.Para

### GetLookupTableStepSize(string, out double)

Gets the step size, in dB, of the input power levels in the predistortion lookup table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableStepSize(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableStepSize() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the step size, in dB, of the input power levels in the predistortion lookup table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholddefinition__string-out.html language=enus -->
## TOPIC 00202: GetLookupTableThresholdDefinition(string, out RFmxSpecAnMXDpdLookupTableThresholdDefinition)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholddefinition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholddefinition__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableThresholdDefinition(string selectorString, out RFmxSpecAnMXDpdLookupTableThresholdDefinition value)

### GetLookupTableThresholdDefinition(string, out RFmxSpecAnMXDpdLookupTableThresholdDefinition)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableThresholdDefinition(string selectorString, out RFmxSpecAnMXDpdLookupTableThresholdDefinition value)

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholdlevel__string-out.html language=enus -->
## TOPIC 00203: GetLookupTableThresholdLevel(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholdlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholdlevel__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets either the relative or absolute threshold power level. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableThresholdLevel(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_DPDGetLookupTableThresholdLevel() function in C.ParametersNameTypeDe

### GetLookupTableThresholdLevel(string, out double)

Gets either the relative or absolute threshold power level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableThresholdLevel(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableThresholdLevel() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains either the relative or absolute threshold power level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholdtype__string-out.html language=enus -->
## TOPIC 00204: GetLookupTableThresholdType(string, out RFmxSpecAnMXDpdLookupTableThresholdType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholdtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptablethresholdtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference for the power level used for thresholding. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableThresholdType(string selectorString, out RFmxSpecAnMXDpdLookupTableThresholdType value)RemarksThis method maps to the RFmxSpecAn_DPDGetLookupTableThresholdType() f

### GetLookupTableThresholdType(string, out RFmxSpecAnMXDpdLookupTableThresholdType)

Gets the reference for the power level used for thresholding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableThresholdType(string selectorString, out RFmxSpecAnMXDpdLookupTableThresholdType value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetLookupTableThresholdType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdLookupTableThresholdType | Upon return, contains the reference for the power level used for thresholding. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptabletype__string-out.html language=enus -->
## TOPIC 00205: GetLookupTableType(string, out RFmxSpecAnMXDpdLookupTableType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptabletype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getlookuptabletype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of the DPD lookup table (LUT). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetLookupTableType(string selectorString, out RFmxSpecAnMXDpdLookupTableType value)RemarksThis method gets the value of DpdLookupTableType attribute.The default value is Log.ParametersNameTypeDe

### GetLookupTableType(string, out RFmxSpecAnMXDpdLookupTableType)

Gets the type of the DPD lookup table (LUT).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetLookupTableType(string selectorString, out RFmxSpecAnMXDpdLookupTableType value)

#### Remarks

This method gets the value of [DpdLookupTableType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Log](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptabletype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdLookupTableType | Upon return, contains the type of the DPD lookup table (LUT). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmeasurementsampleratemode__string-out.html language=enus -->
## TOPIC 00206: GetMeasurementSampleRateMode(string, out RFmxSpecAnMXDpdMeasurementSampleRateMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmeasurementsampleratemode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmeasurementsampleratemode__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition sample rate configuration mode. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementSampleRateMode(string selectorString, out RFmxSpecAnMXDpdMeasurementSampleRateMode value)RemarksThis method maps to the RFmxSpecAn_DPDGetMeasurementSampleRateMode() functio

### GetMeasurementSampleRateMode(string, out RFmxSpecAnMXDpdMeasurementSampleRateMode)

Gets the acquisition sample rate configuration mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementSampleRateMode(string selectorString, out RFmxSpecAnMXDpdMeasurementSampleRateMode value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetMeasurementSampleRateMode() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdMeasurementSampleRateMode | Upon return, contains the acquisition sample rate configuration mode. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomiallagordertype__string-out.html language=enus -->
## TOPIC 00207: GetMemoryPolynomialLagOrderType(string, out RFmxSpecAnMXDpdMemoryPolynomialLagOrderType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomiallagordertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomiallagordertype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of terms of the lag order DPD polynomial when you set theRFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMemoryPolynomialLagOrderType(string selectorString, out RFmxSpecAnMXDpdMemoryPolynomialLagOrderType value)Parame

### GetMemoryPolynomialLagOrderType(string, out RFmxSpecAnMXDpdMemoryPolynomialLagOrderType)

Gets the type of terms of the lag order DPD polynomial when you set the[RFmxSpecAnMXDpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) to [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMemoryPolynomialLagOrderType(string selectorString, out RFmxSpecAnMXDpdMemoryPolynomialLagOrderType value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdMemoryPolynomialLagOrderType | Upon return, contains the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomialmaximumlead__string-out.html language=enus -->
## TOPIC 00208: GetMemoryPolynomialMaximumLead(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomialmaximumlead__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomialmaximumlead__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum lead stagger cross term of the DPD polynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMemoryPolynomialMaximumLead(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_DPDGetMemoryPolynomialMaximumLead() function in C.ParametersNameT

### GetMemoryPolynomialMaximumLead(string, out int)

Gets the maximum lead stagger cross term of the DPD polynomial.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMemoryPolynomialMaximumLead(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetMemoryPolynomialMaximumLead() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return,Specifies the maximum lead stagger cross term of the DPD polynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomialorder__string-out.html language=enus -->
## TOPIC 00209: GetMemoryPolynomialOrder(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomialorder__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-getmemorypolynomialorder__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the order of the DPD polynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMemoryPolynomialOrder(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_DPDGetMemoryPolynomialOrder() function in C.ParametersNameTypeDescriptionselectorStringstringPass

### GetMemoryPolynomialOrder(string, out int)

Gets the order of the DPD polynomial.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMemoryPolynomialOrder(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDGetMemoryPolynomialOrder() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the order of the DPD polynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptableamtopmcurvefitorder__string-int.html language=enus -->
## TOPIC 00210: SetLookupTableAMToPMCurveFitOrder(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptableamtopmcurvefitorder__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptableamtopmcurvefitorder__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetLookupTableAMToPMCurveFitOrder(string selectorStri

### SetLookupTableAMToPMCurveFitOrder(string, int)

Sets the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [LookupTable](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetLookupTableAMToPMCurveFitOrder(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetLookupTableAMtoPMCurveFitOrder() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Contains the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptableamtopmcurvefittype__string-rfmxspecanmxdpdlookuptableamtopmcurvefittype.html language=enus -->
## TOPIC 00211: SetLookupTableAMToPMCurveFitType(string, RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptableamtopmcurvefittype__string-rfmxspecanmxdpdlookuptableamtopmcurvefittype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptableamtopmcurvefittype__string-rfmxspecanmxdpdlookuptableamtopmcurvefittype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetLookupTableAMToPMCurveFitType(string selectorString, RFmxSpe

### SetLookupTableAMToPMCurveFitType(string, RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType)

Sets the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [LookupTable](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetLookupTableAMToPMCurveFitType(string selectorString, RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetLookupTableAMtoPMCurveFitType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType | Contains the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptablestepsize__string-double.html language=enus -->
## TOPIC 00212: SetLookupTableStepSize(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptablestepsize__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setlookuptablestepsize__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the step size, in dB, of the input power levels in the predistortion lookup table when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetLookupTableStepSize(string selectorString, double value)RemarksThis me

### SetLookupTableStepSize(string, double)

Sets the step size, in dB, of the input power levels in the predistortion lookup table when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [LookupTable](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetLookupTableStepSize(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetLookupTableStepSize() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Contains the step size, in dB, of the input power levels in the predistortion lookup table when you set RFmxSpecAnMXDpdModel to LookupTable. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00213: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the DPD measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxSpecAn_DPDSetMeasurementEnabled() function in C.ParametersNameTypeDescriptionselectorStringstringPass an

### SetMeasurementEnabled(string, bool)

Sets whether to enable the DPD measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True if the DPD measurement is enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsamplerate__string-double.html language=enus -->
## TOPIC 00214: SetMeasurementSampleRate(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsamplerate__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsamplerate__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition sample rate, in samples per second (S/s), when you set the SetMeasurementSampleRateMode(string, RFmxSpecAnMXDpdMeasurementSampleRateMode) method to User. Actual sample rate may differ from requested sample rate in order to ensure waveform is phase continuous. SyntaxNamespace: Na

### SetMeasurementSampleRate(string, double)

Sets the acquisition sample rate, in samples per second (S/s), when you set the [SetMeasurementSampleRateMode(string, RFmxSpecAnMXDpdMeasurementSampleRateMode)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxdpdmeasurementsampleratemode.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmeasurementsampleratemode.html). Actual sample rate may differ from requested sample rate in order to ensure waveform is phase continuous.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementSampleRate(string selectorString, double value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMeasurementSampleRate() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the acquisition sample rate, in S/s, when you set the SetMeasurementSampleRateMode(string, RFmxSpecAnMXDpdMeasurementSampleRateMode) to User. Actual sample rate may differ from requested sample rate in order to ensure waveform is phase continuous. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxdpdmeasurementsampleratemode.html language=enus -->
## TOPIC 00215: SetMeasurementSampleRateMode(string, RFmxSpecAnMXDpdMeasurementSampleRateMode)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxdpdmeasurementsampleratemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmeasurementsampleratemode__string-rfmxspecanmxdpdmeasurementsampleratemode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition sample rate configuration mode. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMeasurementSampleRateMode(string selectorString, RFmxSpecAnMXDpdMeasurementSampleRateMode value)RemarksThis method maps to the RFmxSpecAn_DPDSetMeasurementSampleRateMode() function in

### SetMeasurementSampleRateMode(string, RFmxSpecAnMXDpdMeasurementSampleRateMode)

Sets the acquisition sample rate configuration mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMeasurementSampleRateMode(string selectorString, RFmxSpecAnMXDpdMeasurementSampleRateMode value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMeasurementSampleRateMode() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdMeasurementSampleRateMode | Contains the acquisition sample rate configuration mode. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagmemorydepth__string-int.html language=enus -->
## TOPIC 00216: SetMemoryPolynomialLagMemoryDepth(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagmemorydepth__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagmemorydepth__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the lag memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. Synt

### SetMemoryPolynomialLagMemoryDepth(string, int)

Sets the lag memory depth cross term of the DPD polynomial when you set the [SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdpdmodel__string-rfmxspecanmxdpdapplydpduserdpdmodel.html) method to [MemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html) or [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html) and set the [SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setconfigurationinput__string-rfmxspecanmxdpdapplydpdconfigurationinput.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdconfigurationinput.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryPolynomialLagMemoryDepth(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialLagMemoryDepth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the lag memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagorder__string-int.html language=enus -->
## TOPIC 00217: SetMemoryPolynomialLagOrder(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagorder__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagorder__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the order of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. SyntaxNamespace: NationalI

### SetMemoryPolynomialLagOrder(string, int)

Sets the order of the DPD polynomial when you set the [SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdpdmodel__string-rfmxspecanmxdpdapplydpduserdpdmodel.html) method to [MemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html) or [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html) and set the [SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setconfigurationinput__string-rfmxspecanmxdpdapplydpdconfigurationinput.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdconfigurationinput.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryPolynomialLagOrder(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialLagOrder() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Contains the order of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to MemoryPolynomial or GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagordertype__string-rfmxspecanmxdpdmemorypolynomiallagordertype.html language=enus -->
## TOPIC 00218: SetMemoryPolynomialLagOrderType(string, RFmxSpecAnMXDpdMemoryPolynomialLagOrderType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagordertype__string-rfmxspecanmxdpdmemorypolynomiallagordertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomiallagordertype__string-rfmxspecanmxdpdmemorypolynomiallagordertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMemoryPolynomialLagOrderType(string selectorString, RFmxSpecAnMXDpdMemoryPolynomialLagOrderType value)Parameter

### SetMemoryPolynomialLagOrderType(string, RFmxSpecAnMXDpdMemoryPolynomialLagOrderType)

Sets the type of terms of the lag order DPD polynomial when you set the [RFmxSpecAnMXDpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) to [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryPolynomialLagOrderType(string selectorString, RFmxSpecAnMXDpdMemoryPolynomialLagOrderType value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdMemoryPolynomialLagOrderType | Specifies the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadmemorydepth__string-int.html language=enus -->
## TOPIC 00219: SetMemoryPolynomialLeadMemoryDepth(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadmemorydepth__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadmemorydepth__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the lead memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. SyntaxNamespace: Nation

### SetMemoryPolynomialLeadMemoryDepth(string, int)

Sets the lead memory depth cross term of the DPD polynomial when you set the [SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdpdmodel__string-rfmxspecanmxdpdapplydpduserdpdmodel.html) method to [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html) and set the [SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setconfigurationinput__string-rfmxspecanmxdpdapplydpdconfigurationinput.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdconfigurationinput.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryPolynomialLeadMemoryDepth(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialLeadMemoryDepth() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Contains the lead memory depth cross term of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadorder__string-int.html language=enus -->
## TOPIC 00220: SetMemoryPolynomialLeadOrder(string, int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadorder__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadorder__string-int.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the lead order cross term of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. SyntaxNamespace: NationalInstr

### SetMemoryPolynomialLeadOrder(string, int)

Sets the lead order cross term of the DPD polynomial when you set the [SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setuserdpdmodel__string-rfmxspecanmxdpdapplydpduserdpdmodel.html) method to [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpduserdpdmodel.html) and set the [SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpd-setconfigurationinput__string-rfmxspecanmxdpdapplydpdconfigurationinput.html) method to [User](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdapplydpdconfigurationinput.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryPolynomialLeadOrder(string selectorString, int value)

#### Remarks

This method maps to the RFmxSpecAn_DPDSetMemoryPolynomialLeadOrder() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the lead order cross term of the DPD polynomial when you set the SetUserDpdModel(string, RFmxSpecAnMXDpdApplyDpdUserDpdModel) method to GeneralizedMemoryPolynomial and set the SetConfigurationInput(string, RFmxSpecAnMXDpdApplyDpdConfigurationInput) method to User. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadordertype__string-rfmxspecanmxdpdmemorypolynomialleadordertype.html language=enus -->
## TOPIC 00221: SetMemoryPolynomialLeadOrderType(string, RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadordertype__string-rfmxspecanmxdpdmemorypolynomialleadordertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmemorypolynomialleadordertype__string-rfmxspecanmxdpdmemorypolynomialleadordertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetMemoryPolynomialLeadOrderType(string selectorString, RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType value)Parame

### SetMemoryPolynomialLeadOrderType(string, RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType)

Sets the type of terms of the lead order DPD polynomial when you set the [RFmxSpecAnMXDpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) to [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetMemoryPolynomialLeadOrderType(string selectorString, RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdMemoryPolynomialLeadOrderType | Specifies the type of terms of the lead order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdiqoriginoffsetcorrectionenabled.html language=enus -->
## TOPIC 00222: RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdiqoriginoffsetcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdiqoriginoffsetcorrectionenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the IQ origin offset correction for the measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabledMembersNameValueDescriptionFalse0Enables the IQ origin offset correction for the measurement. True1Disables the

### RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled Enumeration

Specifies whether to enable the IQ origin offset correction for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Enables the IQ origin offset correction for the measurement. |
| True | 1 | Disables the IQ origin offset correction for the measurement. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptableamtopmcurvefittype.html language=enus -->
## TOPIC 00223: RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptableamtopmcurvefittype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptableamtopmcurvefittype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the SetModel(string, RFmxSpecAnMXDpdModel) method to LookupTable. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdLookupTableAMToPMCurveFitTypeMembersNameVa

### RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType Enumeration

Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the [SetModel(string, RFmxSpecAnMXDpdModel)](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdconfiguration-setmodel__string-rfmxspecanmxdpdmodel.html) method to [LookupTable](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| LeastSquare | 0 | Minimizes the energy of the polynomial approximation error. |
| LeastAbsoluteResidual | 1 | Minimizes the magnitude of the polynomial approximation error. |
| Bisquare | 2 | Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptablethresholddefinition.html language=enus -->
## TOPIC 00224: RFmxSpecAnMXDpdLookupTableThresholdDefinition Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptablethresholddefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptablethresholddefinition.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdLookupTableThresholdDefinitionMembersNameValueDescriptionInputAndOutput0Input1

### RFmxSpecAnMXDpdLookupTableThresholdDefinition Enumeration

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdLookupTableThresholdDefinition

#### Members

| Name | Value | Description |
| --- | --- | --- |
| InputAndOutput | 0 |  |
| Input | 1 |  |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptablethresholdtype.html language=enus -->
## TOPIC 00225: RFmxSpecAnMXDpdLookupTableThresholdType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptablethresholdtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptablethresholdtype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdLookupTableThresholdTypeMembersNameValueDescriptionRelative0The threshold is relative to the peak power, in dB, of the acquired samples. Absolute1The thresh

### RFmxSpecAnMXDpdLookupTableThresholdType Enumeration

Specifies the reference for the power level used for thresholding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdLookupTableThresholdType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The threshold is relative to the peak power, in dB, of the acquired samples. |
| Absolute | 1 | The threshold is the absolute power, in dBm. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptabletype.html language=enus -->
## TOPIC 00226: RFmxSpecAnMXDpdLookupTableType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptabletype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdlookuptabletype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of the DPD lookup table (LUT). SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdLookupTableTypeMembersNameValueDescriptionLog0Input powers in the LUT are specified in dBm. Linear1Input powers in the LUT are specified in watts.

### RFmxSpecAnMXDpdLookupTableType Enumeration

Specifies the type of the DPD lookup table (LUT).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdLookupTableType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Log | 0 | Input powers in the LUT are specified in dBm. |
| Linear | 1 | Input powers in the LUT are specified in watts. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmeasurementmode.html language=enus -->
## TOPIC 00227: RFmxSpecAnMXDpdMeasurementMode Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmeasurementmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmeasurementmode.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the training waveform required for the extraction of the DPD model coefficients is acquired from the hardware or is configured by the user. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdMeasurementModeMembersNameValueDescriptionAcquireAndExtract0The measur

### RFmxSpecAnMXDpdMeasurementMode Enumeration

Specifies if the training waveform required for the extraction of the DPD model coefficients is acquired from the hardware or is configured by the user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdMeasurementMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AcquireAndExtract | 0 | The measurement acquires the training waveform required for the extraction of the DPD model coefficients from the hardware and then computes the model coefficients. |
| ExtractOnly | 1 | The measurement uses the user configured training waveform required for the extraction of the DPD model coefficients. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmemorypolynomiallagordertype.html language=enus -->
## TOPIC 00228: RFmxSpecAnMXDpdMemoryPolynomialLagOrderType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmemorypolynomiallagordertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmemorypolynomiallagordertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of terms of the lag order DPD polynomial when you set the RFmxSpecAnMXDpdModel to GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdMemoryPolynomialLagOrderTypeMembersNameValueDescriptionAllOrders0The memory polynomial will

### RFmxSpecAnMXDpdMemoryPolynomialLagOrderType Enumeration

Configures the type of terms of the lag order DPD polynomial when you set the [RFmxSpecAnMXDpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) to [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdMemoryPolynomialLagOrderType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AllOrders | 0 | The memory polynomial will compute all the terms for the given order. |
| OddOrdersOnly | 1 | The memory polynomial will compute the non-zero coefficients only for the odd terms. |
| EvenOrdersOnly | 2 | The memory polynomial will compute the non-zero coefficents only for the even terms. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmemorypolynomialordertype.html language=enus -->
## TOPIC 00229: RFmxSpecAnMXDpdMemoryPolynomialOrderType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmemorypolynomialordertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmemorypolynomialordertype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of terms of the DPD polynomial when you set the RFmxSpecAnMXDpdModel to MemoryPolynomial or GeneralizedMemoryPolynomial. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdMemoryPolynomialOrderTypeMembersNameValueDescriptionAllOrders0The memory polynomia

### RFmxSpecAnMXDpdMemoryPolynomialOrderType Enumeration

Configures the type of terms of the DPD polynomial when you set the [RFmxSpecAnMXDpdModel](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) to [MemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html) or [GeneralizedMemoryPolynomial](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdmodel.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdMemoryPolynomialOrderType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AllOrders | 0 | The memory polynomial will compute all the terms for the given order. |
| OddOrdersOnly | 1 | The memory polynomial will compute the non-zero coefficients only for the odd terms. |
| EvenOrdersOnly | 2 | The memory polynomial will compute the non-zero coefficents only for the first linear term and all even terms. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdnmseenabled.html language=enus -->
## TOPIC 00230: RFmxSpecAnMXDpdNmseEnabled Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdnmseenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdnmseenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the normalized mean-squared error (NMSE) computation. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdNmseEnabledMembersNameValueDescriptionFalse0Disables NMSE computation. NaN is returned as NMSE. True1Enables NMSE computation.

### RFmxSpecAnMXDpdNmseEnabled Enumeration

Specifies whether to enable the normalized mean-squared error (NMSE) computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdNmseEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables NMSE computation. NaN is returned as NMSE. |
| True | 1 | Enables NMSE computation. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrfilterenabled__string-out.html language=enus -->
## TOPIC 00231: GetCfrFilterEnabled(string, out RFmxSpecAnMXDpdPreDpdCfrFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrfilterenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the filtering operation when you set the DpdApplyDpdCfrEnabled method to True. Refer to DPD concept topic for more information about filtering. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCfrFilterEnabled(string selectorString, out RFmxSpecAnMXDpdPreDpdCfrF

### GetCfrFilterEnabled(string, out RFmxSpecAnMXDpdPreDpdCfrFilterEnabled)

Gets whether to enable the filtering operation when you set the [DpdApplyDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrfilterenabled.html). Refer to DPD concept topic for more information about filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrFilterEnabled(string selectorString, out RFmxSpecAnMXDpdPreDpdCfrFilterEnabled value)

#### Remarks

This method gets the value of [DpdPreDpdCfrFilterEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdPreDpdCfrFilterEnabled | Upon return, contains whether to enable the filtering operation when you set the DpdApplyDpdCfrEnabled method to True. Refer to DPD concept topic for more information about filtering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrmaximumiterations__string-out.html language=enus -->
## TOPIC 00232: GetCfrMaximumIterations(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrmaximumiterations__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrmaximumiterations__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of iterations required to converge waveform PAPR to target PAPR, when you set the DpdPreDpdCfrEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCfrMaximumIterations(string selectorString, out int value)RemarksThis method gets the value of

### GetCfrMaximumIterations(string, out int)

Gets the maximum number of iterations required to converge waveform PAPR to target PAPR, when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrMaximumIterations(string selectorString, out int value)

#### Remarks

This method gets the value of [DpdPreDpdCfrMaximumIterations](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of iterations required to converge waveform PAPR to target PAPR, when you set the DpdPreDpdCfrEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrmethod__string-out.html language=enus -->
## TOPIC 00233: GetCfrMethod(string, out RFmxSpecAnMXDpdPreDpdCfrMethod)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrmethod__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method used to perform crest factor reduction (CFR) when you set the DpdPreDpdCfrEnabled method to True. Refer to DPD concept topic for more information about CFR methods. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCfrMethod(string selectorString, out RFmxSpecAnMXDpdPre

### GetCfrMethod(string, out RFmxSpecAnMXDpdPreDpdCfrMethod)

Gets the method used to perform crest factor reduction (CFR) when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html). Refer to DPD concept topic for more information about CFR methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrMethod(string selectorString, out RFmxSpecAnMXDpdPreDpdCfrMethod value)

#### Remarks

This method gets the value of [DpdPreDpdCfrMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Clipping](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdPreDpdCfrMethod | Upon return, contains the method used to perform crest factor reduction (CFR) when you set the DpdPreDpdCfrEnabled method to True. Refer to DPD concept topic for more information about CFR methods. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrwindowtype__string-out.html language=enus -->
## TOPIC 00234: GetCfrWindowType(string, out RFmxSpecAnMXDpdPreDpdCfrWindowType)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrwindowtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-getcfrwindowtype__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: >Gets the window type to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to PeakWindowing. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetCfrWindowType(string selectorString, out RFmxSpecAnMXDpdPreDpdCfrWindowType value)RemarksThis metho

### GetCfrWindowType(string, out RFmxSpecAnMXDpdPreDpdCfrWindowType)

>Gets the window type to be used when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html) and the [DpdPreDpdCfrMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [PeakWindowing](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetCfrWindowType(string selectorString, out RFmxSpecAnMXDpdPreDpdCfrWindowType value)

#### Remarks

This method gets the value of [DpdPreDpdCfrWindowType](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is Kaiser-Bessel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxSpecAnMXDpdPreDpdCfrWindowType | Upon return, contains the window type to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to PeakWindowing. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcarrierbandwidth__string-double.html language=enus -->
## TOPIC 00235: SetCarrierBandwidth(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcarrierbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcarrierbandwidth__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the carrier bandwidth when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierBandwidth(string selectorString, double value)RemarksThis method sets the val

### SetCarrierBandwidth(string, double)

Sets the carrier bandwidth when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method and the [DpdPreDpdCfrFilterEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [DpdPreDpdCarrierBandwidth](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 20 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the carrier bandwidth when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcarrieroffset__string-double.html language=enus -->
## TOPIC 00236: SetCarrierOffset(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcarrieroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcarrieroffset__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the carrier offset relative to the center of the complex baseband equivalent of the RF signal when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCarrierOffse

### SetCarrierOffset(string, double)

Sets the carrier offset relative to the center of the complex baseband equivalent of the RF signal when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method and the [DpdPreDpdCfrFilterEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCarrierOffset(string selectorString, double value)

#### Remarks

This method sets the value of [DpdPreDpdCarrierOffset](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the carrier offset relative to the center of the complex baseband equivalent of the RF signal when you set the DpdPreDpdCfrEnabled method and the DpdPreDpdCfrFilterEnabled method to True. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrenabled__string-rfmxspecanmxdpdpredpdcfrenabled.html language=enus -->
## TOPIC 00237: SetCfrEnabled(string, RFmxSpecAnMXDpdPreDpdCfrEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrenabled__string-rfmxspecanmxdpdpredpdcfrenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrenabled__string-rfmxspecanmxdpdpredpdcfrenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCfrEnabled(string selectorString, RFmxSpecAnMXDpdPreDpdCfrEnabled value)RemarksThis method sets the value of DpdPreDpdCfrEnabled attribut

### SetCfrEnabled(string, RFmxSpecAnMXDpdPreDpdCfrEnabled)

Sets whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCfrEnabled(string selectorString, RFmxSpecAnMXDpdPreDpdCfrEnabled value)

#### Remarks

This method sets the value of [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdPreDpdCfrEnabled | Specifies whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrfilterenabled__string-rfmxspecanmxdpdpredpdcfrfilterenabled.html language=enus -->
## TOPIC 00238: SetCfrFilterEnabled(string, RFmxSpecAnMXDpdPreDpdCfrFilterEnabled)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrfilterenabled__string-rfmxspecanmxdpdpredpdcfrfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrfilterenabled__string-rfmxspecanmxdpdpredpdcfrfilterenabled.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the filtering operation when you set the DpdApplyDpdCfrEnabled method to True. Refer to DPD concept topic for more information about filtering. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCfrFilterEnabled(string selectorString, RFmxSpecAnMXDpdPreDpdCfrFilte

### SetCfrFilterEnabled(string, RFmxSpecAnMXDpdPreDpdCfrFilterEnabled)

Sets whether to enable the filtering operation when you set the [DpdApplyDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrfilterenabled.html). Refer to DPD concept topic for more information about filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCfrFilterEnabled(string selectorString, RFmxSpecAnMXDpdPreDpdCfrFilterEnabled value)

#### Remarks

This method sets the value of [DpdPreDpdCfrFilterEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdPreDpdCfrFilterEnabled | Specifies whether to enable the filtering operation when you set the DpdApplyDpdCfrEnabled method to True. Refer to DPD concept topic for more information about filtering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrmethod__string-rfmxspecanmxdpdpredpdcfrmethod.html language=enus -->
## TOPIC 00239: SetCfrMethod(string, RFmxSpecAnMXDpdPreDpdCfrMethod)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrmethod__string-rfmxspecanmxdpdpredpdcfrmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrmethod__string-rfmxspecanmxdpdpredpdcfrmethod.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the method used to perform crest factor reduction (CFR) when you set the DpdPreDpdCfrEnabled method to True. Refer to DPD concept topic for more information about CFR methods. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCfrMethod(string selectorString, RFmxSpecAnMXDpdPreDpdC

### SetCfrMethod(string, RFmxSpecAnMXDpdPreDpdCfrMethod)

Sets the method used to perform crest factor reduction (CFR) when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html). Refer to DPD concept topic for more information about CFR methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCfrMethod(string selectorString, RFmxSpecAnMXDpdPreDpdCfrMethod value)

#### Remarks

This method sets the value of [DpdPreDpdCfrMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is [Clipping](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxSpecAnMXDpdPreDpdCfrMethod | Specifies the method used to perform crest factor reduction (CFR) when you set the DpdPreDpdCfrEnabled method to True. Refer to DPD concept topic for more information about CFR methods. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrshapingfactor__string-double.html language=enus -->
## TOPIC 00240: SetCfrShapingFactor(string, double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrshapingfactor__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpd-setcfrshapingfactor__string-double.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shaping factor to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to Sigmoid. Refer to the DPD concept topic for more information about shaping factor. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int SetCfrShapingFactor(string selec

### SetCfrShapingFactor(string, double)

Sets the shaping factor to be used when you set the [DpdPreDpdCfrEnabled](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [True](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrenabled.html) and the [DpdPreDpdCfrMethod](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) method to [Sigmoid](nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdpredpdcfrmethod.html). Refer to the DPD concept topic for more information about shaping factor.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int SetCfrShapingFactor(string selectorString, double value)

#### Remarks

This method sets the value of [DpdPreDpdCfrShapingFactor](nationalinstruments-rfmx-specanmx-rfmxspecanmxpropertyid.html) attribute.The default value is 5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the shaping factor to be used when you set the DpdPreDpdCfrEnabled method to True and the DpdPreDpdCfrMethod method to Sigmoid. Refer to the DPD concept topic for more information about shaping factor. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxSpecAnMXDpdPreDpd Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdsignaltype.html language=enus -->
## TOPIC 00241: RFmxSpecAnMXDpdSignalType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdsignaltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdsignaltype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdSignalTypeMembersNameValueDescriptionModulated0The reference waveform is a cellular or connectivity standard

### RFmxSpecAnMXDpdSignalType Enumeration

Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdSignalType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Modulated | 0 | The reference waveform is a cellular or connectivity standard signal. |
| Tones | 1 | The reference waveform is a continuous signal. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdsynchronizationmethod.html language=enus -->
## TOPIC 00242: RFmxSpecAnMXDpdSynchronizationMethod Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdsynchronizationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdsynchronizationmethod.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used for synchronization of the acquired waveform with the reference waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdSynchronizationMethodMembersNameValueDescriptionDirect1Synchronizes the acquired and reference waveforms assuming that samp

### RFmxSpecAnMXDpdSynchronizationMethod Enumeration

Specifies the method used for synchronization of the acquired waveform with the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdSynchronizationMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Direct | 1 | Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when measurement sampling rate is high. |
| AliasProtected | 2 | Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when measurement sampling rate is low. Refer to DPD concept help for more information. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdtargetgaintype.html language=enus -->
## TOPIC 00243: RFmxSpecAnMXDpdTargetGainType Enumeration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdtargetgaintype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxdpdtargetgaintype.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain expected from the DUT after applying DPD on the input waveform. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic enum RFmxSpecAnMXDpdTargetGainTypeMembersNameValueDescriptionAverageGain0The DPD polynomial or lookup table is computed by assuming that the linearized gain exp

### RFmxSpecAnMXDpdTargetGainType Enumeration

Specifies the gain expected from the DUT after applying DPD on the input waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public enum RFmxSpecAnMXDpdTargetGainType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AverageGain | 0 | The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the average power gain provided by the DUT without DPD. |
| LinearRegionGain | 1 | The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the gain provided by the DUT, without DPD, to the parts of the reference waveform that do not drive the DUT into non-linear gain-expansion or compression regions of its input-output characteristics. The measurement computes the linear region gain as the average gain experienced by the parts of the reference waveform that are below a threshold which is computed as shown in the following equation: Linear region threshold (dBm) = Max {-25, Min {reference waveform power} + 6, DUT Average Input Power -15}. |
| PeakInputPowerGain | 2 | The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the average power gain provided by the DUT, without DPD, to all the samples of the reference waveform for which the magnitude is greater than the peak power in the <format tpye="italics">reference waveform (dBm)</format> - 0.5 dB. |

Parent topic:

NationalInstruments.RFmx.SpecAnMX

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcnt-configuration.html language=enus -->
## TOPIC 00244: Configuration

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcnt-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcnt-configuration.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXFcntConfiguration instance that allows configuration of frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXFcntConfiguration Configuration { get; }RemarksReturns an object of type RFmxSpecAnMXFcntConfiguration

### Configuration

Gets the RFmxSpecAnMXFcntConfiguration instance that allows configuration of frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXFcntConfiguration](nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration.html) Configuration { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXFcntConfiguration

Parent topic:

RFmxSpecAnMXFcnt Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcnt-results.html language=enus -->
## TOPIC 00245: Results

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcnt-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcnt-results.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxSpecAnMXFcntResults instance that provides methods to retrieve frequency count (Fcnt) measurement results. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic RFmxSpecAnMXFcntResults Results { get; }RemarksReturns an object of type RFmxSpecAnMXFcntResults.

### Results

Gets the RFmxSpecAnMXFcntResults instance that provides methods to retrieve frequency count (Fcnt) measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public [RFmxSpecAnMXFcntResults](nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntresults.html) Results { get; }

#### Remarks

Returns an object of type RFmxSpecAnMXFcntResults.

Parent topic:

RFmxSpecAnMXFcnt Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00246: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_FCntGetAllTracesEnabl

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_FCntGetAllTracesEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if the traces to be stored and retrieved after performing the Fcnt measurement are enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00247: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method maps to the RFmxSpecAn_FCntGetMeasurementEnabled() function in C.ParametersNameTypeDescriptionsel

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method maps to the RFmxSpecAn_FCntGetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | True if Fcnt measurement is enabled; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getmeasurementinterval__string-out.html language=enus -->
## TOPIC 00248: GetMeasurementInterval(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getmeasurementinterval__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition time, in seconds, for the frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetMeasurementInterval(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_FCntGetMeasurementInterval() function in C.Paramete

### GetMeasurementInterval(string, out double)

Gets the acquisition time, in seconds, for the frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetMeasurementInterval(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_FCntGetMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the acquisition time, in seconds, for the Fcnt measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00249: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for frequency count (Fcnt) measurement. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method maps to the RFmxSpecAn_FCntGetNumberOfAnalysisThreads() func

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for frequency count (Fcnt) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method maps to the RFmxSpecAn_FCntGetNumberOfAnalysisThreads() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for Fcnt measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class

<!--NI_TOPIC bundle=rfmxspecan-dotnet-api-ref path=nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getthresholdlevel__string-out.html language=enus -->
## TOPIC 00250: GetThresholdLevel(string, out double)

- bundle_id: `rfmxspecan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getthresholdlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-specanmx-rfmxspecanmxfcntconfiguration-getthresholdlevel__string-out.html
- document_id: `rfmxspecan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets either the relative or absolute threshold power level. SyntaxNamespace: NationalInstruments.RFmx.SpecAnMXpublic int GetThresholdLevel(string selectorString, out double value)RemarksThis method maps to the RFmxSpecAn_FCntGetThresholdLevel() function in C.ParametersNameTypeDescriptionselectorStri

### GetThresholdLevel(string, out double)

Gets either the relative or absolute threshold power level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.SpecAnMX](nationalinstruments-rfmx-specanmx.html)

public int GetThresholdLevel(string selectorString, out double value)

#### Remarks

This method maps to the RFmxSpecAn_FCntGetThresholdLevel() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, indicates either the relative or absolute threshold power level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxSpecAnMXFcntConfiguration Class
