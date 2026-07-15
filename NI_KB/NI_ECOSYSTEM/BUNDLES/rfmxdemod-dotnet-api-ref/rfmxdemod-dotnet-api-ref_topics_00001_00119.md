# NI DOCUMENT BUNDLE: rfmxdemod-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxdemod-dotnet-api-ref start=1 end=119 -->
<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getattributecomplexsinglearray__string-int-ref.html language=enus -->
## TOPIC 00001: GetAttributeComplexSingleArray(string, int, ref ComplexSingle[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getattributecomplexsinglearray__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getattributecomplexsinglearray__string-int-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAttributeComplexSingleArray(string selectorString, int attributeIdentifier, ref ComplexSingle[] value)

### GetAttributeComplexSingleArray(string, int, ref ComplexSingle[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAttributeComplexSingleArray(string selectorString, int attributeIdentifier, ref ComplexSingle[] value)

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getattributesinglearray__string-int-ref.html language=enus -->
## TOPIC 00002: GetAttributeSingleArray(string, int, ref float[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getattributesinglearray__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getattributesinglearray__string-int-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAttributeSingleArray(string selectorString, int attributeIdentifier, ref float[] value)

### GetAttributeSingleArray(string, int, ref float[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAttributeSingleArray(string selectorString, int attributeIdentifier, ref float[] value)

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getautolevelinitialreferencelevel__string-out.html language=enus -->
## TOPIC 00003: GetAutoLevelInitialReferenceLevel(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getautolevelinitialreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getautolevelinitialreferencelevel__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAutoLevelInitialReferenceLevel(string selectorString, out doubl

### GetAutoLevelInitialReferenceLevel(string, out double)

Gets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAutoLevelInitialReferenceLevel(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_GetAutoLevelInitialReferenceLevel() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getcenterfrequency__string-out.html language=enus -->
## TOPIC 00004: GetCenterFrequency(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getcenterfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getcenterfrequency__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier frequency, in hertz (Hz), of the RF signal to acquire. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetCenterFrequency(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_GetCenterFrequency() fu

### GetCenterFrequency(string, out double)

Gets the carrier frequency, in hertz (Hz), of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetCenterFrequency(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_GetCenterFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the carrier frequency, in Hz, of the RF signal to acquire. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getdigitaledgetriggersource__string-out.html language=enus -->
## TOPIC 00005: GetDigitalEdgeTriggerSource(string, out string)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getdigitaledgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getdigitaledgetriggersource__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value that indicates the source terminal for the digital-edge trigger. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetDigitalEdgeTriggerSource(string selectorString, out string value)RemarksThis method maps to the RFmxDemod_GetDigitalEdgeTriggerSource() function in C.Paramet

### GetDigitalEdgeTriggerSource(string, out string)

Gets the value that indicates the source terminal for the digital-edge trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetDigitalEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method maps to the RFmxDemod_GetDigitalEdgeTriggerSource() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the source terminal for the digital-edge trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getiqpoweredgetriggerlevel__string-out.html language=enus -->
## TOPIC 00006: GetIQPowerEdgeTriggerLevel(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getiqpoweredgetriggerlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getiqpoweredgetriggerlevel__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power level at which the device triggers. This value is expressed in dB when you set the NationalInstruments.RFmx.DemodMX.RFmxDemodMX.GetIQPowerEdgeTriggerLevelType(string,NationalInstruments.RFmx.DemodMX.RFmxDemodMXIQPowerEdgeTriggerLevelType@) to Relative and in dBm when you set the Natio

### GetIQPowerEdgeTriggerLevel(string, out double)

Gets the power level at which the device triggers. This value is expressed in dB when you set the NationalInstruments.RFmx.DemodMX.RFmxDemodMX.GetIQPowerEdgeTriggerLevelType(string,NationalInstruments.RFmx.DemodMX.RFmxDemodMXIQPowerEdgeTriggerLevelType@) to Relative and in dBm when you set the NationalInstruments.RFmx.DemodMX.RFmxDemodMX.GetIQPowerEdgeTriggerLevelType(string,NationalInstruments.RFmx.DemodMX.RFmxDemodMXIQPowerEdgeTriggerLevelType@) method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the NationalInstruments.RFmx.DemodMX.RFmxDemodMX.GetTriggerType(string,NationalInstruments.RFmx.DemodMX.RFmxDemodMXTriggerType@) method to IQ Power Edge.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetIQPowerEdgeTriggerLevel(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_GetIQPowerEdgeTriggerLevel() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the power level at which the device triggers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-getreferencelevelunits__string-out.html language=enus -->
## TOPIC 00007: GetReferenceLevelUnits(string, out RFmxDemodMXReferenceLevelUnits)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-getreferencelevelunits__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-getreferencelevelunits__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetReferenceLevelUnits(string selectorString, out RFmxDemodMXReferenceLevelUnits value)

### GetReferenceLevelUnits(string, out RFmxDemodMXReferenceLevelUnits)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetReferenceLevelUnits(string selectorString, out RFmxDemodMXReferenceLevelUnits value)

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-initiate__string-string.html language=enus -->
## TOPIC 00008: Initiate(string, string)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-initiate__string-string.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. To get the status of measurements, you can use the CheckMeasurementStatus(string, out b

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. To get the status of measurements, you can use the [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-demodmx-rfmxdemodmx-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int Initiate(string selectorString, string resultName)

#### Remarks

This method maps to the RFmxDemod_Initiate() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies a selector string comprising the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-isdisposed.html language=enus -->
## TOPIC 00009: IsDisposed

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-isdisposed.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic bool IsDisposed { get; }Remarkstrue If the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public bool IsDisposed { get; }

#### Remarks

true If the session is disposed; otherwise, false.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00010: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-sendsoftwareedgetrigger.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the ConfigureSoftwareEdgeTrigger(string, double, bool) to choose a software version of a trigger, and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. SyntaxNamespace: NationalInstruments.RFmx.De

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the [ConfigureSoftwareEdgeTrigger(string, double, bool)](nationalinstruments-rfmx-demodmx-rfmxdemodmx-configuresoftwareedgetrigger__string-double-bool.html) to choose a software version of a trigger, and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SendSoftwareEdgeTrigger()

#### Remarks

This method maps to the RFmxDemod_SendSoftwareEdgeTrigger() function in C.

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00011: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributebool__string-int-bool.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Boolean attribute. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Usin

### SetAttributeBool(string, int, bool)

Sets the value of a Boolean attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributecomplexsinglearray__string-int-complexsingle_arr1.html language=enus -->
## TOPIC 00012: SetAttributeComplexSingleArray(string, int, ComplexSingle[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributecomplexsinglearray__string-int-complexsingle_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributecomplexsinglearray__string-int-complexsingle_arr1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAttributeComplexSingleArray(string selectorString, int attributeIdentifier, ComplexSingle[] value)

### SetAttributeComplexSingleArray(string, int, ComplexSingle[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAttributeComplexSingleArray(string selectorString, int attributeIdentifier, ComplexSingle[] value)

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributedouble__string-int-double.html language=enus -->
## TOPIC 00013: SetAttributeDouble(string, int, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributedouble__string-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributedouble__string-int-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a double attribute. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)RemarksThis method maps to the RFmxDemod_SetAttributeF64() function in C.ParametersNameTypeDescriptionselectorStringstring

### SetAttributeDouble(string, int, double)

Sets the value of a double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)

#### Remarks

This method maps to the RFmxDemod_SetAttributeF64() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributesbytearray__string-int-sbyte_arr1.html language=enus -->
## TOPIC 00014: SetAttributeSByteArray(string, int, sbyte[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributesbytearray__string-int-sbyte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributesbytearray__string-int-sbyte_arr1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the value of a signed byte array attribute. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAttributeSByteArray(string selectorString, int attributeIdentifier, sbyte[] value)RemarksThis method maps to the RFmxDemod_SetAttributeI8Array() function in C.ParametersNameTypeDescriptions

### SetAttributeSByteArray(string, int, sbyte[])

Set the value of a signed byte array attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAttributeSByteArray(string selectorString, int attributeIdentifier, sbyte[] value)

#### Remarks

This method maps to the RFmxDemod_SetAttributeI8Array() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | sbyte[] | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributesinglearray__string-int-float_arr1.html language=enus -->
## TOPIC 00015: SetAttributeSingleArray(string, int, float[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributesinglearray__string-int-float_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributesinglearray__string-int-float_arr1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAttributeSingleArray(string selectorString, int attributeIdentifier, float[] value)

### SetAttributeSingleArray(string, int, float[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAttributeSingleArray(string selectorString, int attributeIdentifier, float[] value)

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributestring__string-int-string.html language=enus -->
## TOPIC 00016: SetAttributeString(string, int, string)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributestring__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setattributestring__string-int-string.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a string attribute. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAttributeString(string selectorString, int attributeIdentifier, string value)RemarksThis method maps to the RFmxDemod_SetAttributeString() function in C.ParametersNameTypeDescriptionselectorStringstr

### SetAttributeString(string, int, string)

Sets the value of a string attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAttributeString(string selectorString, int attributeIdentifier, string value)

#### Remarks

This method maps to the RFmxDemod_SetAttributeString() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | string | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setautolevelinitialreferencelevel__string-double.html language=enus -->
## TOPIC 00017: SetAutoLevelInitialReferenceLevel(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setautolevelinitialreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setautolevelinitialreferencelevel__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAutoLevelInitialReferenceLevel(string selectorString, double va

### SetAutoLevelInitialReferenceLevel(string, double)

Sets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAutoLevelInitialReferenceLevel(string selectorString, double value)

#### Remarks

This method maps to the RFmxDemod_SetAutoLevelInitialReferenceLevel() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | double | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setcenterfrequency__string-double.html language=enus -->
## TOPIC 00018: SetCenterFrequency(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setcenterfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setcenterfrequency__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the carrier frequency, in hertz (Hz), of the RF signal to acquire. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetCenterFrequency(string selectorString, double value)RemarksThis method maps to the RFmxDemod_SetCenterFrequency() functi

### SetCenterFrequency(string, double)

Sets the carrier frequency, in hertz (Hz), of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetCenterFrequency(string selectorString, double value)

#### Remarks

This method maps to the RFmxDemod_SetCenterFrequency() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | double | Specifies the carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setiqpoweredgetriggerleveltype__string-rfmxdemodmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00019: SetIQPowerEdgeTriggerLevelType(string, RFmxDemodMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setiqpoweredgetriggerleveltype__string-rfmxdemodmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setiqpoweredgetriggerleveltype__string-rfmxdemodmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. This method is used only when you set the SetTriggerType(string, RFmxDemodMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetIQPowerEdgeTriggerLevelType(string selectorStri

### SetIQPowerEdgeTriggerLevelType(string, RFmxDemodMXIQPowerEdgeTriggerLevelType)

Sets the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-demodmx-rfmxdemodmx-setiqpoweredgetriggerlevel__string-double.html) method. This method is used only when you set the [SetTriggerType(string, RFmxDemodMXTriggerType)](nationalinstruments-rfmx-demodmx-rfmxdemodmx-settriggertype__string-rfmxdemodmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-demodmx-rfmxdemodmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetIQPowerEdgeTriggerLevelType(string selectorString, RFmxDemodMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method maps to the RFmxDemod_SetIQPowerEdgeTriggerLevelType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name passed when creating the signal configuration is used. |
| value | RFmxDemodMXIQPowerEdgeTriggerLevelType | Upon return, contains the value that indicates the reference for the SetIQPowerEdgeTriggerLevelType(string, RFmxDemodMXIQPowerEdgeTriggerLevelType) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setlimitedconfigurationchange__string-rfmxdemodmxlimitedconfigurationchange.html language=enus -->
## TOPIC 00020: SetLimitedConfigurationChange(string, RFmxDemodMXLimitedConfigurationChange)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setlimitedconfigurationchange__string-rfmxdemodmxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setlimitedconfigurationchange__string-rfmxdemodmxlimitedconfigurationchange.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetLimitedConfigurationChange(string selectorString, RFmxDemodMXLimitedConfigurationChange value)RemarksIf your test system performs the same m

### SetLimitedConfigurationChange(string, RFmxDemodMXLimitedConfigurationChange)

Sets the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetLimitedConfigurationChange(string selectorString, RFmxDemodMXLimitedConfigurationChange value)

#### Remarks

If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this property can help achieve faster measurements. When you set this property to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. 
 You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration. 
 NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than Disabled for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case. 
 Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxDemodMXLimitedConfigurationChange | Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-setreferencelevelunits__string-rfmxdemodmxreferencelevelunits.html language=enus -->
## TOPIC 00021: SetReferenceLevelUnits(string, RFmxDemodMXReferenceLevelUnits)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-setreferencelevelunits__string-rfmxdemodmxreferencelevelunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-setreferencelevelunits__string-rfmxdemodmxreferencelevelunits.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetReferenceLevelUnits(string selectorString, RFmxDemodMXReferenceLevelUnits value)

### SetReferenceLevelUnits(string, RFmxDemodMXReferenceLevelUnits)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetReferenceLevelUnits(string selectorString, RFmxDemodMXReferenceLevelUnits value)

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00022: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the number for seconds specified using the timeout parameter for all measurements to complete. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)RemarksThis method maps to the RFmxDemod_WaitForMeasurementComplete()

### WaitForMeasurementComplete(string, double)

Waits for the number for seconds specified using the timeout parameter for all measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Remarks

This method maps to the RFmxDemod_WaitForMeasurementComplete() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMX Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00023: GetAveragingType(string, out RFmxDemodMXADemodAveragingType)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for the measurement. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAveragingType(string selectorString, out RFmxDemodMXADemodAveragingType value)RemarksThis method maps to the RFmxDemod_ADemodGetAveragingType() function in C.ParametersNameTypeDescriptionselec

### GetAveragingType(string, out RFmxDemodMXADemodAveragingType)

Gets the averaging type for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAveragingType(string selectorString, out RFmxDemodMXADemodAveragingType value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetAveragingType() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxDemodMXADemodAveragingType | Upon return, contains the averaging type for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getfmdeemphasis__string-out.html language=enus -->
## TOPIC 00024: GetFMDeEmphasis(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getfmdeemphasis__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getfmdeemphasis__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetFMDeEmphasis(string selectorString, out double value)RemarksThis method maps to the

### GetFMDeEmphasis(string, out double)

Gets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetFMDeEmphasis(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetFMDeEmphasis() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getmeasurementinterval__string-out.html language=enus -->
## TOPIC 00025: GetMeasurementInterval(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-getmeasurementinterval__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetMeasurementInterval(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetMeasurementInterv

### GetMeasurementInterval(string, out double)

Gets the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetMeasurementInterval(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetMeasurementInterval() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the signal acquisition time, in seconds, for the analog demodulation measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setaveragingenabled__string-rfmxdemodmxademodaveragingenabled.html language=enus -->
## TOPIC 00026: SetAveragingEnabled(string, RFmxDemodMXADemodAveragingEnabled)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setaveragingenabled__string-rfmxdemodmxademodaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setaveragingenabled__string-rfmxdemodmxademodaveragingenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the measurement. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetAveragingEnabled(string selectorString, RFmxDemodMXADemodAveragingEnabled value)RemarksWhen averaging is enabled, the measurement uses averaging count for the number of acquisitions o

### SetAveragingEnabled(string, RFmxDemodMXADemodAveragingEnabled)

Sets whether to enable averaging for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetAveragingEnabled(string selectorString, RFmxDemodMXADemodAveragingEnabled value)

#### Remarks

When averaging is enabled, the measurement uses averaging count for the number of acquisitions over which the measurement is averaged. The traces are not averaged. When averaging is disabled, the number of acquisitions is 1. This method maps to the RFmxDemod_ADemodSetAveragingEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxDemodMXADemodAveragingEnabled | Specifies whether to enable averaging for the analog demodulation measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setcarriercorrectionfrequencyenabled__string-rfmxdemodmxademodcarrierfrequencycorrectionenabled.html language=enus -->
## TOPIC 00027: SetCarrierCorrectionFrequencyEnabled(string, RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setcarriercorrectionfrequencyenabled__string-rfmxdemodmxademodcarrierfrequencycorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setcarriercorrectionfrequencyenabled__string-rfmxdemodmxademodcarrierfrequencycorrectionenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetCarrierCorrectionFrequencyEnabled(string selectorString, RFmxDemodMXADemodCarrierFrequencyCorrectionEn

### SetCarrierCorrectionFrequencyEnabled(string, RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled)

Sets whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetCarrierCorrectionFrequencyEnabled(string selectorString, RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled value)

#### Remarks

This method maps to the RFmxDemod_ADemodSetCarrierCorrectionFrequencyEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxDemodMXADemodCarrierFrequencyCorrectionEnabled | Specifies whether to correct the carrier phase error when demodulating PM signals. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setfmdeemphasis__string-double.html language=enus -->
## TOPIC 00028: SetFMDeEmphasis(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setfmdeemphasis__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setfmdeemphasis__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetFMDeEmphasis(string selectorString, double value)RemarksThis method maps to the RFm

### SetFMDeEmphasis(string, double)

Sets the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the frequency-modulated (FM) transmitter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetFMDeEmphasis(string selectorString, double value)

#### Remarks

This method maps to the RFmxDemod_ADemodSetFMDeEmphasis() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setrbwfilteralpha__string-double.html language=enus -->
## TOPIC 00029: SetRbwFilterAlpha(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setrbwfilteralpha__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodconfiguration-setrbwfilteralpha__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the roll-off factor of the root-raised-cosine (RRC) filter. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetRbwFilterAlpha(string selectorString, double value)RemarksThis method maps to the RFmxDemod_ADemodSetRBWFilterAlpha() function in C.ParametersNameTypeDescriptionselectorStr

### SetRbwFilterAlpha(string, double)

Sets the roll-off factor of the root-raised-cosine (RRC) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetRbwFilterAlpha(string selectorString, double value)

#### Remarks

This method maps to the RFmxDemod_ADemodSetRBWFilterAlpha() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the roll-off factor of the RRC filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-fetchpmmaximumdeviation__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00030: FetchPMMaximumDeviation(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-fetchpmmaximumdeviation__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-fetchpmmaximumdeviation__string-double-out-out-out-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase-modulated (PM) maximum deviation. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchPMMaximumDeviation(string selectorString, double timeout, out double maximumDeviation, out double maximumHalfPeakToPeak, out double maximumRms, out double maximumPositivePeak, out dou

### FetchPMMaximumDeviation(string, double, out double, out double, out double, out double, out double)

Fetches the phase-modulated (PM) maximum deviation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchPMMaximumDeviation(string selectorString, double timeout, out double maximumDeviation, out double maximumHalfPeakToPeak, out double maximumRms, out double maximumPositivePeak, out double maximumNegativePeak)

#### Remarks

This method maps to the RFmxDemod_ADemodFetchPMMaximumDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| maximumDeviation | out double | Upon return, contains the maximum phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. |
| maximumHalfPeakToPeak | out double | Upon return, contains the maximum (peak to peak)/2 phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. |
| maximumRms | out double | Upon return, contains the maximum RMS phase deviation, in degrees, of the PM signal measured over multiple acquisitions. |
| maximumPositivePeak | out double | Upon return, contains the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
| maximumNegativePeak | out double | Upon return, contains the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-fetchpmmeandeviation__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00031: FetchPMMeanDeviation(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-fetchpmmeandeviation__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-fetchpmmeandeviation__string-double-out-out-out-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase-modulated (PM) mean deviation measurements. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchPMMeanDeviation(string selectorString, double timeout, out double meanDeviation, out double meanHalfPeakToPeak, out double meanRms, out double meanPositivePeak, out double m

### FetchPMMeanDeviation(string, double, out double, out double, out double, out double, out double)

Fetches the phase-modulated (PM) mean deviation measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchPMMeanDeviation(string selectorString, double timeout, out double meanDeviation, out double meanHalfPeakToPeak, out double meanRms, out double meanPositivePeak, out double meanNegativePeak)

#### Remarks

This method maps to the RFmxDemod_ADemodFetchPMMeanDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanDeviation | out double | Upon return, contains the mean negative peak phase deviation around the unmodulated carrier phase. |
| meanHalfPeakToPeak | out double | Upon return, contains the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. |
| meanRms | out double | Upon return, contains the mean RMS phase deviation, in degrees, of the phase-modulated signal. |
| meanPositivePeak | out double | Upon return, contains the mean positive peak phase deviation, in degrees, around the unmodulated carrier phase. |
| meanNegativePeak | out double | Upon return, contains the mean negative peak phase deviation, in degrees, around the unmodulated carrier phase. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumhalfpeaktopeak__string-out.html language=enus -->
## TOPIC 00032: GetAMModulationDepthMaximumHalfPeakToPeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumhalfpeaktopeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumhalfpeaktopeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMaximumHalfPeakToPeak(string selectorString, out double value)RemarksThis method maps to the RF

### GetAMModulationDepthMaximumHalfPeakToPeak(string, out double)

Gets the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMaximumHalfPeakToPeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumHalfPeaktoPeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of all the (peak-to-peak)/2 values in multiple acquisition, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumnegativepeak__string-out.html language=enus -->
## TOPIC 00033: GetAMModulationDepthMaximumNegativePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumnegativepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumnegativepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMaximumNegativePeak(string selectorString, out double value)RemarksThis method maps to the RFmxDem

### GetAMModulationDepthMaximumNegativePeak(string, out double)

Gets the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMaximumNegativePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumNegativePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumpositivepeak__string-out.html language=enus -->
## TOPIC 00034: GetAMModulationDepthMaximumPositivePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumpositivepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumpositivepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMaximumPositivePeak(string selectorString, out double value)RemarksThis method maps to the RFmxDem

### GetAMModulationDepthMaximumPositivePeak(string, out double)

Gets the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMaximumPositivePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumPositivePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of all positive peak values in multiple acquisitions, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumrms__string-out.html language=enus -->
## TOPIC 00035: GetAMModulationDepthMaximumRms(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumrms__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumrms__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMaximumRms(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResults

### GetAMModulationDepthMaximumRms(string, out double)

Gets the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMaximumRms(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumRMS() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of all RMS values in multiple acquisitions, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumstandarddeviation__string-out.html language=enus -->
## TOPIC 00036: GetAMModulationDepthMaximumStandardDeviation(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmaximumstandarddeviation__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum modulation depth measured across multiple acquisitions, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMaximumStandardDeviation(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsAMModula

### GetAMModulationDepthMaximumStandardDeviation(string, out double)

Gets the maximum modulation depth measured across multiple acquisitions, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMaximumStandardDeviation(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMaximumStandardDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of all the modulation depths in multiple acquisitions, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeannegativepeak__string-out.html language=enus -->
## TOPIC 00037: GetAMModulationDepthMeanNegativePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeannegativepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeannegativepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean negative peak amplitude of the modulating signal, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMeanNegativePeak(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanNega

### GetAMModulationDepthMeanNegativePeak(string, out double)

Gets the mean negative peak amplitude of the modulating signal, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMeanNegativePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanNegativePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean negative peak amplitude of the modulating signal, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeanrms__string-out.html language=enus -->
## TOPIC 00038: GetAMModulationDepthMeanRms(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeanrms__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeanrms__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean root mean square (RMS) amplitude of the modulating signal, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMeanRms(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanRMS(

### GetAMModulationDepthMeanRms(string, out double)

Gets the mean root mean square (RMS) amplitude of the modulating signal, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMeanRms(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanRMS() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean RMS amplitude of the modulating signal, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeanstandarddeviation__string-out.html language=enus -->
## TOPIC 00039: GetAMModulationDepthMeanStandardDeviation(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeanstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getammodulationdepthmeanstandarddeviation__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAMModulationDepthMeanStandardDeviation(string select

### GetAMModulationDepthMeanStandardDeviation(string, out double)

Gets the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAMModulationDepthMeanStandardDeviation(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAMModulationDepthMeanStandardDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragesinad__string-out.html language=enus -->
## TOPIC 00040: GetAverageSinad(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragesinad__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragesinad__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAverageSinad(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsAverageSINAD() function in C.Paramete

### GetAverageSinad(string, out double)

Gets the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAverageSinad(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAverageSINAD() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragesnr__string-out.html language=enus -->
## TOPIC 00041: GetAverageSnr(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragesnr__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragesnr__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaged signal-to-noise ratio, in dB, of the demodulated signal. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAverageSnr(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsAverageSNR() function in C.ParametersNameTypeDescripti

### GetAverageSnr(string, out double)

Gets the averaged signal-to-noise ratio, in dB, of the demodulated signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAverageSnr(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAverageSNR() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the averaged signal-to-noise ratio, in dB, of the demodulated signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragethd__string-out.html language=enus -->
## TOPIC 00042: GetAverageThd(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragethd__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getaveragethd__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average of total harmonic distortion (THD) present in the signal, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAverageThd(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsAverageTHD() function in C.Parameters

### GetAverageThd(string, out double)

Gets the average of total harmonic distortion (THD) present in the signal, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAverageThd(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsAverageTHD() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average of THD present in the signal, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getfmdeviationmaximumnegativepeak__string-out.html language=enus -->
## TOPIC 00043: GetFMDeviationMaximumNegativePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getfmdeviationmaximumnegativepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getfmdeviationmaximumnegativepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum negative peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetFMDeviationMaximumNegativePeak(string selectorString, out double value)RemarksThis method ma

### GetFMDeviationMaximumNegativePeak(string, out double)

Gets the maximum negative peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetFMDeviationMaximumNegativePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMaximumNegativePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum negative peak frequency deviation, in Hz, of the FM signal measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getfmdeviationmaximumpositivepeak__string-out.html language=enus -->
## TOPIC 00044: GetFMDeviationMaximumPositivePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getfmdeviationmaximumpositivepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getfmdeviationmaximumpositivepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum positive peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetFMDeviationMaximumPositivePeak(string selectorString, out double value)RemarksThis method ma

### GetFMDeviationMaximumPositivePeak(string, out double)

Gets the maximum positive peak frequency deviation, in hertz (Hz), of the frequency-modulated (FM) signal measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetFMDeviationMaximumPositivePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsFMDeviationMaximumPositivePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum positive peak frequency deviation, in Hz, of the FM signal measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumhalfpeaktopeak__string-out.html language=enus -->
## TOPIC 00045: GetPMDeviationMaximumHalfPeakToPeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumhalfpeaktopeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumhalfpeaktopeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetPMDeviationMaximumHalfPeakToPeak(string selectorString, out double value)RemarksThis method maps

### GetPMDeviationMaximumHalfPeakToPeak(string, out double)

Gets the maximum (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetPMDeviationMaximumHalfPeakToPeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumHalfPeaktoPeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumnegativepeak__string-out.html language=enus -->
## TOPIC 00046: GetPMDeviationMaximumNegativePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumnegativepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumnegativepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetPMDeviationMaximumNegativePeak(string selectorString, out double value)RemarksThis method maps to th

### GetPMDeviationMaximumNegativePeak(string, out double)

Gets the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetPMDeviationMaximumNegativePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumNegativePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumpositivepeak__string-out.html language=enus -->
## TOPIC 00047: GetPMDeviationMaximumPositivePeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumpositivepeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumpositivepeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetPMDeviationMaximumPositivePeak(string selectorString, out double value)RemarksThis method maps to th

### GetPMDeviationMaximumPositivePeak(string, out double)

Gets the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetPMDeviationMaximumPositivePeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumPositivePeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumrms__string-out.html language=enus -->
## TOPIC 00048: GetPMDeviationMaximumRms(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumrms__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumrms__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum root mean squared (RMS) phase deviation, in degrees, of the phase-modulated (PM) signal measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetPMDeviationMaximumRms(string selectorString, out double value)RemarksThis method maps to the

### GetPMDeviationMaximumRms(string, out double)

Gets the maximum root mean squared (RMS) phase deviation, in degrees, of the phase-modulated (PM) signal measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetPMDeviationMaximumRms(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumRMS() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum RMS phase deviation, in degrees, of the PM signal measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumstandarddeviation__string-out.html language=enus -->
## TOPIC 00049: GetPMDeviationMaximumStandardDeviation(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumstandarddeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmaximumstandarddeviation__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetPMDeviationMaximumStandardDeviation(string selectorString, out double value)RemarksThis method maps to the RFmxDem

### GetPMDeviationMaximumStandardDeviation(string, out double)

Gets the maximum phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetPMDeviationMaximumStandardDeviation(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMaximumStandardDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmeanhalfpeaktopeak__string-out.html language=enus -->
## TOPIC 00050: GetPMDeviationMeanHalfPeakToPeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmeanhalfpeaktopeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxademodresults-getpmdeviationmeanhalfpeaktopeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetPMDeviationMeanHalfPeakToPeak(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_ADemodGetResultsPMDeviationM

### GetPMDeviationMeanHalfPeakToPeak(string, out double)

Gets the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetPMDeviationMeanHalfPeakToPeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_ADemodGetResultsPMDeviationMeanHalfPeaktoPeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXADemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi2.html language=enus -->
## TOPIC 00051: DioPfi2

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi2.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string DioPfi2

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi3.html language=enus -->
## TOPIC 00052: DioPfi3

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi3.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string DioPfi3

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi5.html language=enus -->
## TOPIC 00053: DioPfi5

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi5.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string DioPfi5

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi6.html language=enus -->
## TOPIC 00054: DioPfi6

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-diopfi6.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string DioPfi6

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pfi1.html language=enus -->
## TOPIC 00055: Pfi1

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pfi1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the signal to the PFI 1 connector on the NI 5142 and NI 5622. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string Pfi1

### Pfi1

Exports the signal to the PFI 1 connector on the NI 5142 and NI 5622.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string Pfi1

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00056: PxiTriggerLine1

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the signal to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

Exports the signal to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00057: PxiTriggerLine2

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline2.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the signal to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

Exports the signal to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00058: PxiTriggerLine3

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline3.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the signal to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

Exports the signal to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline4.html language=enus -->
## TOPIC 00059: PxiTriggerLine4

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline4.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the signal to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string PxiTriggerLine4

### PxiTriggerLine4

Exports the signal to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string PxiTriggerLine4

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00060: PxiTriggerLine5

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxconstants-pxitriggerline5.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the signal to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

Exports the signal to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxDemodMXConstants Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemod-results.html language=enus -->
## TOPIC 00061: Results

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemod-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemod-results.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxDemodMXDDemodResults instance that provides methods to retrieve digital demodulation measurement results. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic RFmxDemodMXDDemodResults Results { get; }RemarksReturns an object of type RFmxDemodMXDDemodResults.

### Results

Gets the [RFmxDemodMXDDemodResults](nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults.html) instance that provides methods to retrieve digital demodulation measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public [RFmxDemodMXDDemodResults](nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults.html) Results { get; }

#### Remarks

Returns an object of type RFmxDemodMXDDemodResults.

Parent topic:

RFmxDemodMXDDemod Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configureequalizer__string-rfmxdemodmxddemodequalizermode-int-double-double-complexsingle_arr1-int-double.html language=enus -->
## TOPIC 00062: ConfigureEqualizer(string, RFmxDemodMXDDemodEqualizerMode, int, double, double, ComplexSingle[], int, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configureequalizer__string-rfmxdemodmxddemodequalizermode-int-double-double-complexsingle_arr1-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configureequalizer__string-rfmxdemodmxddemodequalizermode-int-double-double-complexsingle_arr1-int-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int ConfigureEqualizer(string selectorString, RFmxDemodMXDDemodEqualizerMode equalizerMode, int equalizerFilterLength, double x0, double dx, ComplexSingle[] y, int equalizerTrainingCount, double equalizerConvergenceFac

### ConfigureEqualizer(string, RFmxDemodMXDDemodEqualizerMode, int, double, double, ComplexSingle[], int, double)

Configures the equalizer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int ConfigureEqualizer(string selectorString, RFmxDemodMXDDemodEqualizerMode equalizerMode, int equalizerFilterLength, double x0, double dx, ComplexSingle[] y, int equalizerTrainingCount, double equalizerConvergenceFactor)

#### Remarks

This method maps to the RFmxDemod_DDemodCfgEqualizer() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| equalizerMode | RFmxDemodMXDDemodEqualizerMode | Specifies whether the measurement needs to perform equalization. |
| equalizerFilterLength | int | Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. This parameter is ignored when the equalizer initial coefficients are specified. |
| x0 | double | Always pass 0 to this parameter. Any other values will be ignored. |
| dx | double | Specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| y | ComplexSingle[] | Specifies the initial coefficients to be used by the equalizer. |
| equalizerTrainingCount | int | Specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. |
| equalizerConvergenceFactor | double | Specifies the incremental step used by the equalizer to adapt to the channel, during the training stage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configureequalizerinitialcoefficients__string-double-double-complexsingle_arr1.html language=enus -->
## TOPIC 00063: ConfigureEqualizerInitialCoefficients(string, double, double, ComplexSingle[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configureequalizerinitialcoefficients__string-double-double-complexsingle_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configureequalizerinitialcoefficients__string-double-double-complexsingle_arr1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer coefficients. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int ConfigureEqualizerInitialCoefficients(string selectorString, double x0, double dx, ComplexSingle[] equalizerInitialCoefficients)RemarksThis method maps to the RFmxDemod_DDemodCfgEqualizerInitialCoeffic

### ConfigureEqualizerInitialCoefficients(string, double, double, ComplexSingle[])

Configures the equalizer coefficients.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int ConfigureEqualizerInitialCoefficients(string selectorString, double x0, double dx, ComplexSingle[] equalizerInitialCoefficients)

#### Remarks

This method maps to the RFmxDemod_DDemodCfgEqualizerInitialCoefficients() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| x0 | double | Always pass 0 to this parameter. Any other values will be ignored. |
| dx | double | Specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerInitialCoefficients | ComplexSingle[] | Specifies the initial coefficients to be used by the equalizer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configurefskdeviation__string-double-rfmxdemodmxddemodfskreferencecompensationenabled.html language=enus -->
## TOPIC 00064: ConfigureFskDeviation(string, double, RFmxDemodMXDDemodFskReferenceCompensationEnabled)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configurefskdeviation__string-double-rfmxdemodmxddemodfskreferencecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configurefskdeviation__string-double-rfmxdemodmxddemodfskreferencecompensationenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected frequency-shift keying (FSK) deviation. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int ConfigureFskDeviation(string selectorString, double fskDeviation, RFmxDemodMXDDemodFskReferenceCompensationEnabled fskRefCompEnabled)RemarksThis method maps to the RFmxDemod_DD

### ConfigureFskDeviation(string, double, RFmxDemodMXDDemodFskReferenceCompensationEnabled)

Configures the expected frequency-shift keying (FSK) deviation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int ConfigureFskDeviation(string selectorString, double fskDeviation, RFmxDemodMXDDemodFskReferenceCompensationEnabled fskRefCompEnabled)

#### Remarks

This method maps to the RFmxDemod_DDemodCfgFSKDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| fskDeviation | double | Specifies the expected FSK frequency deviation. |
| fskRefCompEnabled | RFmxDemodMXDDemodFskReferenceCompensationEnabled | Specifies whether the FSK deviation that you specify is to be compensated for gain errors, and is used to compute FSK error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configuremeasurementfilter__string-rfmxdemodmxddemodmeasurementfiltertype-double-double-float_arr1.html language=enus -->
## TOPIC 00065: ConfigureMeasurementFilter(string, RFmxDemodMXDDemodMeasurementFilterType, double, double, float[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configuremeasurementfilter__string-rfmxdemodmxddemodmeasurementfiltertype-double-double-float_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configuremeasurementfilter__string-rfmxdemodmxddemodmeasurementfiltertype-double-double-float_arr1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement filter. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int ConfigureMeasurementFilter(string selectorString, RFmxDemodMXDDemodMeasurementFilterType measurementFilterType, double x0, double dx, float[] y)RemarksThis method maps to the RFmxDemod_DDemodCfgMeasurement

### ConfigureMeasurementFilter(string, RFmxDemodMXDDemodMeasurementFilterType, double, double, float[])

Configures the measurement filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int ConfigureMeasurementFilter(string selectorString, RFmxDemodMXDDemodMeasurementFilterType measurementFilterType, double x0, double dx, float[] y)

#### Remarks

This method maps to the RFmxDemod_DDemodCfgMeasurementFilter() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementFilterType | RFmxDemodMXDDemodMeasurementFilterType | Specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients. |
| x0 | double | Always pass 0 to this parameter. Any other values will be ignored. |
| dx | double | Specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| y | float[] | Specifies the filter coefficients to be used by demodulator. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configurepulseshapingfilter__string-rfmxdemodmxddemodpulseshapingfiltertype-double-double-double-float_arr1.html language=enus -->
## TOPIC 00066: ConfigurePulseShapingFilter(string, RFmxDemodMXDDemodPulseShapingFilterType, double, double, double, float[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configurepulseshapingfilter__string-rfmxdemodmxddemodpulseshapingfiltertype-double-double-double-float_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configurepulseshapingfilter__string-rfmxdemodmxddemodpulseshapingfiltertype-double-double-double-float_arr1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse shaping filter. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int ConfigurePulseShapingFilter(string selectorString, RFmxDemodMXDDemodPulseShapingFilterType pulseShapingFilterType, double pulseShapingFilterParameter, double x0, double dx, float[] y)RemarksThis method m

### ConfigurePulseShapingFilter(string, RFmxDemodMXDDemodPulseShapingFilterType, double, double, double, float[])

Configures the pulse shaping filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int ConfigurePulseShapingFilter(string selectorString, RFmxDemodMXDDemodPulseShapingFilterType pulseShapingFilterType, double pulseShapingFilterParameter, double x0, double dx, float[] y)

#### Remarks

This method maps to the RFmxDemod_DDemodCfgPulseShapingFilter() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| pulseShapingFilterType | RFmxDemodMXDDemodPulseShapingFilterType | Specifies the pulse shaping filter used to transmit the signal, and determines the measurement filter to be used for analysis when you set the SetMeasurementFilterType(string, RFmxDemodMXDDemodMeasurementFilterType) to Auto. |
| pulseShapingFilterParameter | double | Specifies the rolloff factor for the raised cosine and root-raised cosine filters that are used as pulse shaping filter, and measurement filter respectively. When pulse shaping filter type is Gaussian, this method specifies bandwidth*sample duration (BT). |
| x0 | double | Always pass 0 to this parameter. Any other values will be ignored. |
| dx | double | Specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| y | float[] | Specifies the filter coefficients used as the pulse shaping filter on the transmitter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configuresymbolrate__string-double.html language=enus -->
## TOPIC 00067: ConfigureSymbolRate(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configuresymbolrate__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-configuresymbolrate__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the symbol rate for digital demodulation measurements. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int ConfigureSymbolRate(string selectorString, double symbolRate)RemarksThis method maps to the RFmxDemod_DDemodCfgSymbolRate() function in C.ParametersNameTypeDescriptionselecto

### ConfigureSymbolRate(string, double)

Configures the symbol rate for digital demodulation measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int ConfigureSymbolRate(string selectorString, double symbolRate)

#### Remarks

This method maps to the RFmxDemod_DDemodCfgSymbolRate() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| symbolRate | double | Specifies the symbol rate in hertz (Hz). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getapskr2tor1ratio__string-out.html language=enus -->
## TOPIC 00068: GetApskR2ToR1Ratio(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getapskr2tor1ratio__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getapskr2tor1ratio__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetApskR2ToR1Ratio(string selectorString, out double value)RemarksThis method gets th

### GetApskR2ToR1Ratio(string, out double)

Gets the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetApskR2ToR1Ratio(string selectorString, out double value)

#### Remarks

This method gets the value of [DDemodApskR2ToR1Ratio](nationalinstruments-rfmx-demodmx-rfmxdemodmxpropertyid.html) attribute.The default value is 2.84. Valid values are from 2 to 8, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getapskr3tor1ratio__string-out.html language=enus -->
## TOPIC 00069: GetApskR3ToR1Ratio(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getapskr3tor1ratio__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getapskr3tor1ratio__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetApskR3ToR1Ratio(string selectorString, out double value)RemarksThis method gets the value of DDemod

### GetApskR3ToR1Ratio(string, out double)

Gets the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetApskR3ToR1Ratio(string selectorString, out double value)

#### Remarks

This method gets the value of [DDemodApskR3ToR1Ratio](nationalinstruments-rfmx-demodmx-rfmxdemodmxpropertyid.html) attribute.The default value is 5.27. Valid values are from 3 to 12, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00070: GetAveragingCount(string, out int)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method maps to the RFmxDemod_DDemodGetAveragingCount() function in C.ParametersNameTypeDescriptionselectorStringstringPas

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetAveragingCount() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the value that indicates the number of acquisitions used for averaging. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getburststartexclusionsymbols__string-out.html language=enus -->
## TOPIC 00071: GetBurstStartExclusionSymbols(string, out int)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getburststartexclusionsymbols__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getburststartexclusionsymbols__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the number of symbols from the start of the burst trigger that is excluded from the measurement. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetBurstStartExclusionSymbols(string selectorString, out int value)ParametersNameTypeDescriptionselectorStringstringPass an empty string. T

### GetBurstStartExclusionSymbols(string, out int)

Get the number of symbols from the start of the burst trigger that is excluded from the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetBurstStartExclusionSymbols(string selectorString, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getequalizerfilterlength__string-out.html language=enus -->
## TOPIC 00072: GetEqualizerFilterLength(string, out int)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getequalizerfilterlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getequalizerfilterlength__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the length of the equalization filter to be computed. The length is specified in terms of symbols. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetEqualizerFilterLength(string selectorString, out int value)RemarksThis method maps to the RFmxDemod_DDemodGetEqualizerFilterLength()

### GetEqualizerFilterLength(string, out int)

Gets the length of the equalization filter to be computed. The length is specified in terms of symbols.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetEqualizerFilterLength(string selectorString, out int value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetEqualizerFilterLength() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the value that indicates the length of the equalization filter to be computed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getsearchlengthauto__string-out.html language=enus -->
## TOPIC 00073: GetSearchLengthAuto(string, out RFmxDemodMXDDemodSearchLengthAuto)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getsearchlengthauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-getsearchlengthauto__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetSearchLengthAuto(string selectorString, out RFmxDemodMXDDemodSearchLengthAu

### GetSearchLengthAuto(string, out RFmxDemodMXDDemodSearchLengthAuto)

Gets whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetSearchLengthAuto(string selectorString, out RFmxDemodMXDDemodSearchLengthAuto value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxDemodMXDDemodSearchLengthAuto | Upon return, contains synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setapskr2tor1ratio__string-double.html language=enus -->
## TOPIC 00074: SetApskR2ToR1Ratio(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setapskr2tor1ratio__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setapskr2tor1ratio__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetApskR2ToR1Ratio(string selectorString, double value)RemarksThis method sets the va

### SetApskR2ToR1Ratio(string, double)

Sets the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetApskR2ToR1Ratio(string selectorString, double value)

#### Remarks

This method sets the value of [DDemodApskR2ToR1Ratio](nationalinstruments-rfmx-demodmx-rfmxdemodmxpropertyid.html) attribute.The default value is 2.84. Valid values are from 2 to 8, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setfskdeviation__string-double.html language=enus -->
## TOPIC 00075: SetFskDeviation(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setfskdeviation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setfskdeviation__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the expected frequency-shift keying (FSK) frequency deviation. At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetFskDeviation(string

### SetFskDeviation(string, double)

Sets the expected frequency-shift keying (FSK) frequency deviation. At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetFskDeviation(string selectorString, double value)

#### Remarks

This method maps to the RFmxDemod_DDemodSetFSKDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the expected FSK frequency deviation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setiqoffsetremovalenabled__string-rfmxdemodmxddemodiqoffsetremovalenabled.html language=enus -->
## TOPIC 00076: SetIQOffsetRemovalEnabled(string, RFmxDemodMXDDemodIQOffsetRemovalEnabled)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setiqoffsetremovalenabled__string-rfmxdemodmxddemodiqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setiqoffsetremovalenabled__string-rfmxdemodmxddemodiqoffsetremovalenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q offset before the EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetIQOffsetRemovalEnabled(string selectorString, RFmxDemodMXDDemodIQOffsetRemovalEnabled value)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The sign

### SetIQOffsetRemovalEnabled(string, RFmxDemodMXDDemodIQOffsetRemovalEnabled)

Sets whether to remove the I/Q offset before the EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetIQOffsetRemovalEnabled(string selectorString, RFmxDemodMXDDemodIQOffsetRemovalEnabled value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxDemodMXDDemodIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the EVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00077: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable digital demodulation measurements. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method maps to the RFmxDemod_DDemodSetMeasurementEnabled() function in C.ParametersNameTypeDescriptionselectorStri

### SetMeasurementEnabled(string, bool)

Sets whether to enable digital demodulation measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method maps to the RFmxDemod_DDemodSetMeasurementEnabled() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | True to enable digital demodulation measurements; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setpulseshapingfilterparameter__string-double.html language=enus -->
## TOPIC 00078: SetPulseShapingFilterParameter(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setpulseshapingfilterparameter__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setpulseshapingfilterparameter__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the rolloff factor for raised cosine and root raised cosine filter, which are used as pulse shaping filter and measurement filter respectively. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetPulseShapingFilterParameter(string selectorString, double value)RemarksThis method maps

### SetPulseShapingFilterParameter(string, double)

Sets the rolloff factor for raised cosine and root raised cosine filter, which are used as pulse shaping filter and measurement filter respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetPulseShapingFilterParameter(string selectorString, double value)

#### Remarks

This method maps to the RFmxDemod_DDemodSetPulseShapingFilterParameter() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the rolloff factor for raised cosine and root raised cosine filter used as pulse shaping filter and measurement filter. Specifies the Bandwidth * Sample Duration for Gaussian filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsearchlength__string-double.html language=enus -->
## TOPIC 00079: SetSearchLength(string, double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsearchlength__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsearchlength__string-double.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length of the waveform within which the synchronization bit pattern needs to be searched when you set the RFmxDemodMXDDemodConfiguration. SetSearchLengthAuto method to True. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetSearchLength(string selectorString, double value)Param

### SetSearchLength(string, double)

Sets the length of the waveform within which the synchronization bit pattern needs to be searched when you set the RFmxDemodMXDDemodConfiguration. SetSearchLengthAuto method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetSearchLength(string selectorString, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the RFmxDemodMXDDemodConfiguration. SetSearchLengthAuto method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsearchlengthauto__string-rfmxdemodmxddemodsearchlengthauto.html language=enus -->
## TOPIC 00080: SetSearchLengthAuto(string, RFmxDemodMXDDemodSearchLengthAuto)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsearchlengthauto__string-rfmxdemodmxddemodsearchlengthauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsearchlengthauto__string-rfmxdemodmxddemodsearchlengthauto.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetSearchLengthAuto(string selectorString, RFmxDemodMXDDemodSearchLengthAuto v

### SetSearchLengthAuto(string, RFmxDemodMXDDemodSearchLengthAuto)

Sets whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetSearchLengthAuto(string selectorString, RFmxDemodMXDDemodSearchLengthAuto value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxDemodMXDDemodSearchLengthAuto | Specifies the synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsynchronizationenabled__string-rfmxdemodmxddemodsynchronizationenabled.html language=enus -->
## TOPIC 00081: SetSynchronizationEnabled(string, RFmxDemodMXDDemodSynchronizationEnabled)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsynchronizationenabled__string-rfmxdemodmxddemodsynchronizationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsynchronizationenabled__string-rfmxdemodmxddemodsynchronizationenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the demodulator needs to search and synchronize the signal to a known reference sequence. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int SetSynchronizationEnabled(string selectorString, RFmxDemodMXDDemodSynchronizationEnabled value)RemarksThis method maps to the RFmxDemod_D

### SetSynchronizationEnabled(string, RFmxDemodMXDDemodSynchronizationEnabled)

Sets whether the demodulator needs to search and synchronize the signal to a known reference sequence.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetSynchronizationEnabled(string selectorString, RFmxDemodMXDDemodSynchronizationEnabled value)

#### Remarks

This method maps to the RFmxDemod_DDemodSetSynchronizationEnabled() function in C.

The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxDemodMXDDemodSynchronizationEnabled | Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsynchronizationmeasurementoffset__string-int.html language=enus -->
## TOPIC 00082: SetSynchronizationMeasurementOffset(string, int)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsynchronizationmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setsynchronizationmeasurementoffset__string-int.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset, which is the location from which the signal is considered for further measurements. The offset is specified in symbols of the reference sequence. This offset is not applicable when the synchronization bits are not found. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int Se

### SetSynchronizationMeasurementOffset(string, int)

Sets the offset, which is the location from which the signal is considered for further measurements. The offset is specified in symbols of the reference sequence. This offset is not applicable when the synchronization bits are not found.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int SetSynchronizationMeasurementOffset(string selectorString, int value)

#### Remarks

This method maps to the RFmxDemod_DDemodSetSynchronizationMeasurementOffset() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset in symbols from the reference sequence from where the signal is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodConfiguration Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemoddifferentialenabled.html language=enus -->
## TOPIC 00083: RFmxDemodMXDDemodDifferentialEnabled Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemoddifferentialenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemoddifferentialenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the symbols are differentially encoded, and is applicable only to phase-shift keying (PSK) and minimum-shift keying (MSK) modulation types. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodDifferentialEnabledMembersNameValueDescriptionFalse0The symbols

### RFmxDemodMXDDemodDifferentialEnabled Enumeration

Specifies whether the symbols are differentially encoded, and is applicable only to phase-shift keying (PSK) and minimum-shift keying (MSK) modulation types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodDifferentialEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The symbols are directly mapped onto the symbol map. |
| True | 1 | In case of PSK modulation, the transition between two consecutive symbols is mapped onto the symbol map. In case of MSK modulation, the consecutive bits are XORed. Other modulation types do not have any impact. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodequalizermode.html language=enus -->
## TOPIC 00084: RFmxDemodMXDDemodEqualizerMode Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodequalizermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodequalizermode.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement needs to perform equalization. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodEqualizerModeMembersNameValueDescriptionOff0Equalization is not performed. Train1The adaptive feedforward equalizer is turned ON to compensate for the effect

### RFmxDemodMXDDemodEqualizerMode Enumeration

Specifies whether the measurement needs to perform equalization.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodEqualizerMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | Equalization is not performed. |
| Train | 1 | The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. |
| Hold | 2 | The filter that you specify using the NationalInstruments.RFmx.DemodMX.RFmxDemodMXDDemodConfiguration.ConfigureEqualizerInitialCoefficients(string,double,double,NationalInstruments.ComplexSingle[]) method is used as the channel filter, and is applied before demodulating the acquired signal. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodevmnormalizationreference.html language=enus -->
## TOPIC 00085: RFmxDemodMXDDemodEvmNormalizationReference Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodevmnormalizationreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodevmnormalizationreference.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used to normalize the error vector magnitude (EVM). SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodEvmNormalizationReferenceMembersNameValueDescriptionPeak0The EVM is normalized to the peak magnitude of the reference symbols. Rms1The EVM is norm

### RFmxDemodMXDDemodEvmNormalizationReference Enumeration

Specifies the reference used to normalize the error vector magnitude (EVM).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodEvmNormalizationReference

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Peak | 0 | The EVM is normalized to the peak magnitude of the reference symbols. |
| Rms | 1 | The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM), in which the symbols in the map do not have a constant amplitude. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodfskreferencecompensationenabled.html language=enus -->
## TOPIC 00086: RFmxDemodMXDDemodFskReferenceCompensationEnabled Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodfskreferencecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodfskreferencecompensationenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the frequency-shift keying (FSK) deviation that you specify is to be compensated for gain errors, and is used to compute the FSK error. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodFskReferenceCompensationEnabledMembersNameValueDescriptionFalse0Does

### RFmxDemodMXDDemodFskReferenceCompensationEnabled Enumeration

Specifies whether the frequency-shift keying (FSK) deviation that you specify is to be compensated for gain errors, and is used to compute the FSK error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodFskReferenceCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Does not compensate for gain errors. |
| True | 1 | Compensates for gain errors. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodiqoffsetremovalenabled.html language=enus -->
## TOPIC 00087: RFmxDemodMXDDemodIQOffsetRemovalEnabled Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodiqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodiqoffsetremovalenabled.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodIQOffsetRemovalEnabledMembersNameValueDescriptionFalse0The IQ offset is not removed before the EVM measurement. True1The IQ offset is not removed befor

### RFmxDemodMXDDemodIQOffsetRemovalEnabled Enumeration

Specifies whether to remove the I/Q offset before the EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodIQOffsetRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The IQ offset is not removed before the EVM measurement. |
| True | 1 | The IQ offset is not removed before the EVM measurement. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodm.html language=enus -->
## TOPIC 00088: RFmxDemodMXDDemodM Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodm.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodMMembersNameValueDescriptionM22The M-ary number is 2. M44The M-ary number is 4. M88The M

### RFmxDemodMXDDemodM Enumeration

Specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodM

#### Members

| Name | Value | Description |
| --- | --- | --- |
| M2 | 2 | The M-ary number is 2. |
| M4 | 4 | The M-ary number is 4. |
| M8 | 8 | The M-ary number is 8. |
| M16 | 0x10 | The M-ary number is 16. |
| M32 | 0x20 | The M-ary number is 32. |
| M64 | 0x40 | The M-ary number is 64. |
| M128 | 0x80 | The M-ary number is 128. |
| M256 | 0x100 | The M-ary number is 256. |
| M512 | 0x200 | The M-ary number is 512. |
| M1024 | 0x400 | The M-ary number is 1024. |
| M2048 | 0x800 | The M-ary number is 2048. |
| M4096 | 0x1000 | The M-ary number is 4096. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmeasurementfiltertype.html language=enus -->
## TOPIC 00089: RFmxDemodMXDDemodMeasurementFilterType Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmeasurementfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmeasurementfiltertype.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodMeasurementFilterTypeMembersNameValueDescriptionAuto0The

### RFmxDemodMXDDemodMeasurementFilterType Enumeration

Specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodMeasurementFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | 0 | The signal analyzer computes the measurement filter coefficients based on the pulse shaping filter information that you specify in the pulse shaping filter. If the SetPulseShapingFilterType(string, RFmxDemodMXDDemodPulseShapingFilterType) method is set to Custom, then the signal analyzer enables equalization. |
| Custom | 1 | The signal analyzer uses the coefficients specified by ConfigureMeasurementFilterCustomCoefficients(string, double, double, float[]) method. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmodulationtype.html language=enus -->
## TOPIC 00090: RFmxDemodMXDDemodModulationType Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmodulationtype.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital modulation type of the signal that needs to be analyzed. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodModulationTypeMembersNameValueDescriptionAsk0The modulation type is amplitude-shift keying (ASK). Fsk1The modulation type is frequency-shift ke

### RFmxDemodMXDDemodModulationType Enumeration

Specifies the digital modulation type of the signal that needs to be analyzed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Ask | 0 | The modulation type is amplitude-shift keying (ASK). |
| Fsk | 1 | The modulation type is frequency-shift keying (FSK). |
| Psk | 2 | The modulation type is phase-shift keying (PSK). |
| Qam | 3 | The modulation type is quadrature-amplitude modulation (QAM). |
| Msk | 4 | The modulation type is minimum shift keying (MSK). |
| Apsk | 5 | The modulation type is amplitude phase-shift keying (APSK). |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodpskformat.html language=enus -->
## TOPIC 00091: RFmxDemodMXDDemodPskFormat Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodpskformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodpskformat.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase shift keying (PSK) format. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodPskFormatMembersNameValueDescriptionNormal0Sets the modulation type to PSK. OffsetQpsk1Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q

### RFmxDemodMXDDemodPskFormat Enumeration

Specifies the phase shift keying (PSK) format.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodPskFormat

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 0 | Sets the modulation type to PSK. |
| OffsetQpsk | 1 | Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |
| PiBy4_Qpsk | 2 | Sets the modulation type to π/4 QPSK. In this modulation, each QPSK symbol is rotated by π/4. |
| PiBy8_8Psk | 3 | Sets the modulation type to π/8 8 PSK. In this modulation, each 8 PSK symbol is rotated by π/8. |
| PskFormat3PiBy8_8Psk | 4 | Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |
| ShapedOffsetQpsk | 5 | Sets the modulation type to Shaped Offset Quadrature PSK (SOQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodpulseshapingfiltertype.html language=enus -->
## TOPIC 00092: RFmxDemodMXDDemodPulseShapingFilterType Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodpulseshapingfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodpulseshapingfiltertype.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse shaping filter used to transmit the signal, and determines the measurement filter to be used for analysis when the SetMeasurementFilterType(string, RFmxDemodMXDDemodMeasurementFilterType) method is set to Auto. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemo

### RFmxDemodMXDDemodPulseShapingFilterType Enumeration

Specifies the pulse shaping filter used to transmit the signal, and determines the measurement filter to be used for analysis when the [SetMeasurementFilterType(string, RFmxDemodMXDDemodMeasurementFilterType)](nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodconfiguration-setmeasurementfiltertype__string-rfmxdemodmxddemodmeasurementfiltertype.html) method is set to [Auto](nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodmeasurementfiltertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodPulseShapingFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rectangular | 0 | The transmitted waveform is filtered using a rectangular filter. |
| RaisedCosine | 1 | The transmitted waveform is filtered using a raised cosine filter. Specify the filter alpha in the pulse shaping filter alpha or BT. |
| RootRaisedCosine | 2 | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter alpha in the pulse shaping filter alpha or BT. |
| Gaussian | 3 | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the pulse shaping filter alpha or BT. This filter is applicable only to FSK and MSK modulation types. |
| Custom | 4 | The transmitted waveform is filtered using the coefficients that you specify in the ConfigurePulseShapingFilterCustomCoefficients(string, double, double, float[]) method. |
| HalfSine | 5 | The transmitted waveform is filtered using a half sine filter. |
| LinearGmskEdge | 6 | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |
| SoqpskTG | 7 | The transmitted waveform is filtered using a SOQPSK-TG filter. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchcarriermeasurement__string-double-out-out-out.html language=enus -->
## TOPIC 00093: FetchCarrierMeasurement(string, double, out double, out double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchcarriermeasurement__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchcarriermeasurement__string-double-out-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier measurement. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchCarrierMeasurement(string selectorString, double timeout, out double meanFrequencyOffset, out double meanFrequencyDrift, out double meanPhaseError)RemarksThis method maps to the RFmxDemod_DDemodFetchCar

### FetchCarrierMeasurement(string, double, out double, out double, out double)

Fetches the carrier measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchCarrierMeasurement(string selectorString, double timeout, out double meanFrequencyOffset, out double meanFrequencyDrift, out double meanPhaseError)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchCarrierMeasurement() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete |
| meanFrequencyOffset | out double | Upon return, contains the mean of the measured carrier frequency offset, in hertz (Hz). |
| meanFrequencyDrift | out double | Upon return, contains the mean of the measured carrier frequency drift, in Hz. |
| meanPhaseError | out double | Upon return, contains the mean of the measured phase offset, in degrees, from the transmitted carrier phase. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00094: FetchConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchconstellationtrace__string-double-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] constellationTrace)RemarksThis method maps to the RFmxDemod_DDemodFetchConstellationTrace() function in C.ParametersNameType

### FetchConstellationTrace(string, double, ref ComplexSingle[])

Fetches the constellation trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] constellationTrace)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchConstellationTrace() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| constellationTrace | ref ComplexSingle[] | Upon return, contains the demodulated waveform used for measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchdemodulatedbits__string-double-ref.html language=enus -->
## TOPIC 00095: FetchDemodulatedBits(string, double, ref sbyte[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchdemodulatedbits__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchdemodulatedbits__string-double-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated bit stream. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchDemodulatedBits(string selectorString, double timeout, ref sbyte[] demodulatedBits)RemarksThis method maps to the RFmxDemod_DDemodFetchDemodulatedBits() function in C.ParametersNameTypeDescriptionsel

### FetchDemodulatedBits(string, double, ref sbyte[])

Fetches the demodulated bit stream.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchDemodulatedBits(string selectorString, double timeout, ref sbyte[] demodulatedBits)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchDemodulatedBits() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| demodulatedBits | ref sbyte[] | Upon return, contains the demodulated bit stream. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchequalizercoefficients__string-double-out-out-ref.html language=enus -->
## TOPIC 00096: FetchEqualizerCoefficients(string, double, out double, out double, ref ComplexSingle[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchequalizercoefficients__string-double-out-out-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchequalizercoefficients__string-double-out-out-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the updated equalizer coefficients. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchEqualizerCoefficients(string selectorString, double timeout, out double x0, out double dx, ref ComplexSingle[] equalizerCoefficients)RemarksThis method maps to the RFmxDemod_DDemodFetchEquali

### FetchEqualizerCoefficients(string, double, out double, out double, ref ComplexSingle[])

Fetches the updated equalizer coefficients.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchEqualizerCoefficients(string selectorString, double timeout, out double x0, out double dx, ref ComplexSingle[] equalizerCoefficients)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchEqualizerCoefficients() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete |
| x0 | out double | This parameter always returns 0. |
| dx | out double | Upon return, contains the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerCoefficients | ref ComplexSingle[] | Upon return, contains the updated coefficients. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchevm__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00097: FetchEvm(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchevm__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchevm__string-double-out-out-out-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the error vector magnitude (EVM) measurements. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchEvm(string selectorString, double timeout, out double meanRmsEvm, out double maximumRmsEvm, out double meanModulationErrorRatio, out double maximumPeakEvm, out double meanPeakEvm)R

### FetchEvm(string, double, out double, out double, out double, out double, out double)

Fetches the error vector magnitude (EVM) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchEvm(string selectorString, double timeout, out double meanRmsEvm, out double maximumRmsEvm, out double meanModulationErrorRatio, out double maximumPeakEvm, out double meanPeakEvm)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchEVM() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsEvm | out double | Upon return, contains the mean of the RMS EVM, as a percentage, measured per acquisition. |
| maximumRmsEvm | out double | Upon return, contains the maximum of the RMS EVM, as a percentage, measured per acquisition. |
| meanModulationErrorRatio | out double | Upon return, contains the modulation error ratio, in dB. |
| maximumPeakEvm | out double | Upon return, contains the maximum of the peak EVM measured per acquisition. |
| meanPeakEvm | out double | Upon return, contains the mean of the peak EVM measured per acquisition. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchevmtrace__string-double-ref.html language=enus -->
## TOPIC 00098: FetchEvmTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchevmtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchevmtrace__string-double-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the error vector magnitude (EVM) trace. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)RemarksThis method maps to the RFmxDemod_DDemodFetchEVMTrace() function in C.ParametersNameTypeDescriptions

### FetchEvmTrace(string, double, ref AnalogWaveform< float >)

Fetches the error vector magnitude (EVM) trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchEVMTrace() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| evm | ref AnalogWaveform< float > | Upon return, contains the EVM measured per symbol. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanamplitudedroop__string-double-out.html language=enus -->
## TOPIC 00099: FetchMeanAmplitudeDroop(string, double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanamplitudedroop__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanamplitudedroop__string-double-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean amplitude droop per symbol. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchMeanAmplitudeDroop(string selectorString, double timeout, out double meanAmplitudeDroop)RemarksThis method maps to the RFmxDemod_DDemodFetchMeanAmplitudeDroop() function in C.ParametersNameT

### FetchMeanAmplitudeDroop(string, double, out double)

Fetches the mean amplitude droop per symbol.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchMeanAmplitudeDroop(string selectorString, double timeout, out double meanAmplitudeDroop)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchMeanAmplitudeDroop() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanAmplitudeDroop | out double | Upon return, contains the mean amplitude droop per symbol. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanquadratureskew__string-double-out.html language=enus -->
## TOPIC 00100: FetchMeanQuadratureSkew(string, double, out float)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanquadratureskew__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanquadratureskew__string-double-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean quadrature skew. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchMeanQuadratureSkew(string selectorString, double timeout, out float meanQuadratureSkew)RemarksThis method maps to the RFmxDemod_DDemodFetchMeanQuadratureSkew() function in C.ParametersNameTypeDescripti

### FetchMeanQuadratureSkew(string, double, out float)

Fetches the mean quadrature skew.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchMeanQuadratureSkew(string selectorString, double timeout, out float meanQuadratureSkew)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchMeanQuadratureSkew() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanQuadratureSkew | out float | Upon return, contains a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanrhofactor__string-double-out.html language=enus -->
## TOPIC 00101: FetchMeanRhoFactor(string, double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanrhofactor__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeanrhofactor__string-double-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the correlation of the measurement waveform and the reference waveform. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchMeanRhoFactor(string selectorString, double timeout, out double meanRhoFactor)RemarksThis method maps to the RFmxDemod_DDemodFetchMeanRhoFactor() function

### FetchMeanRhoFactor(string, double, out double)

Fetches the correlation of the measurement waveform and the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchMeanRhoFactor(string selectorString, double timeout, out double meanRhoFactor)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchMeanRhoFactor() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRhoFactor | out double | Upon return, contains the correlation of the measurement waveform and the reference waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeasurementwaveform__string-double-ref-out-out.1.html language=enus -->
## TOPIC 00102: FetchMeasurementWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out RFmxDemodMXDDemodSamplesPerSymbol, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeasurementwaveform__string-double-ref-out-out.1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeasurementwaveform__string-double-ref-out-out.1.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement waveform. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchMeasurementWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > measurementWaveform, out RFmxDemodMXDDemodSamplesPerSymbol samplesPerSymbol, out double symbolRate)Remark

### FetchMeasurementWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out RFmxDemodMXDDemodSamplesPerSymbol, out double)

Fetches the measurement waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchMeasurementWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > measurementWaveform, out RFmxDemodMXDDemodSamplesPerSymbol samplesPerSymbol, out double symbolRate)

#### Remarks

This method has been Obseleted. Use FetchMeasurementWaveform() overload that takes in samplesPerSymbol as an integer.

This method maps to the RFmxDemod_DDemodFetchMeasurementWaveform() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the demodulated waveform used for measurement. |
| samplesPerSymbol | out RFmxDemodMXDDemodSamplesPerSymbol | Upon return, contains the samples per symbol used to acquire the signal for the measurement. |
| symbolRate | out double | Upon return, contains the symbol rate in hertz (Hz). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeasurementwaveform__string-double-ref-out-out.html language=enus -->
## TOPIC 00103: FetchMeasurementWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out int, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeasurementwaveform__string-double-ref-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchmeasurementwaveform__string-double-ref-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement waveform. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchMeasurementWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > measurementWaveform, out int samplesPerSymbol, out double symbolRate)RemarksThis method maps to the RFmxD

### FetchMeasurementWaveform(string, double, ref ComplexWaveform< ComplexSingle >, out int, out double)

Fetches the measurement waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchMeasurementWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > measurementWaveform, out int samplesPerSymbol, out double symbolRate)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchMeasurementWaveform() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the demodulated waveform used for measurement. |
| samplesPerSymbol | out int | Upon return, contains the samples per symbol used to acquire the signal for the measurement. |
| symbolRate | out double | Upon return, contains the symbol rate in hertz (Hz). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00104: FetchOffsetConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetconstellationtrace__string-double-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset constellation trace. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchOffsetConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] offsetConstellationTrace)RemarksThis method maps to the RFmxDemod_DDemodFetchOffsetConstellationTrace() functio

### FetchOffsetConstellationTrace(string, double, ref ComplexSingle[])

Fetches the offset constellation trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchOffsetConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] offsetConstellationTrace)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchOffsetConstellationTrace() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| offsetConstellationTrace | ref ComplexSingle[] | Upon return, contains the offset constellation trace |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetevm__string-double-out-out-out-out.html language=enus -->
## TOPIC 00105: FetchOffsetEvm(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetevm__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetevm__string-double-out-out-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset error vector magnitude (EVM). SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchOffsetEvm(string selectorString, double timeout, out double meanRmsOffsetEvm, out double maximumRmsOffsetEvm, out double maximumPeakOffsetEvm, out double meanPeakOffsetEvm)RemarksThis me

### FetchOffsetEvm(string, double, out double, out double, out double, out double)

Fetches the offset error vector magnitude (EVM).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchOffsetEvm(string selectorString, double timeout, out double meanRmsOffsetEvm, out double maximumRmsOffsetEvm, out double maximumPeakOffsetEvm, out double meanPeakOffsetEvm)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchOffsetEVM() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsOffsetEvm | out double | Upon return, contains the mean of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of offset quadrature PSK (OQPSK) demodulated signal. |
| maximumRmsOffsetEvm | out double | Upon return, contains the maximum of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
| maximumPeakOffsetEvm | out double | Upon return, contains the maximum of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
| meanPeakOffsetEvm | out double | Upon return, contains the mean of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetevmtrace__string-double-ref.html language=enus -->
## TOPIC 00106: FetchOffsetEvmTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetevmtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchoffsetevmtrace__string-double-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset error vector magnitude (EVM) trace measured on offset quadrature PSK (OQPSK) signal. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchOffsetEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > offsetEvm)RemarksThis method maps to the RFmxDemo

### FetchOffsetEvmTrace(string, double, ref AnalogWaveform< float >)

Fetches the offset error vector magnitude (EVM) trace measured on offset quadrature PSK (OQPSK) signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchOffsetEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > offsetEvm)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchOffsetEVMTrace() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| offsetEvm | ref AnalogWaveform< float > | Upon return, contains the offset EVM trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchphaseerror__string-double-out-out.html language=enus -->
## TOPIC 00107: FetchPhaseError(string, double, out double, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchphaseerror__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchphaseerror__string-double-out-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error measurements. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchPhaseError(string selectorString, double timeout, out double meanPhaseError, out double maximumPhaseError)RemarksThis method maps to the RFmxDemod_DDemodFetchPhaseError() function in C.ParametersNa

### FetchPhaseError(string, double, out double, out double)

Fetches the phase error measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchPhaseError(string selectorString, double timeout, out double meanPhaseError, out double maximumPhaseError)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchPhaseError() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| meanPhaseError | out double | Upon return, contains the mean of the phase error. |
| maximumPhaseError | out double | Upon return, contains the maximum of the phase error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchreferencewaveform__string-double-ref.html language=enus -->
## TOPIC 00108: FetchReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchreferencewaveform__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-fetchreferencewaveform__string-double-ref.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int FetchReferenceWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > referenceWaveform)RemarksThis method maps to the RFmxDemod_DDemodFetchReferenceWaveform() function in C.Param

### FetchReferenceWaveform(string, double, ref ComplexWaveform< ComplexSingle >)

Fetches the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int FetchReferenceWaveform(string selectorString, double timeout, ref ComplexWaveform< ComplexSingle > referenceWaveform)

#### Remarks

This method maps to the RFmxDemod_DDemodFetchReferenceWaveform() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |
| referenceWaveform | ref ComplexWaveform< ComplexSingle > | Upon return, contains the reference waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getevmmaximumpeak__string-out.html language=enus -->
## TOPIC 00109: GetEvmMaximumPeak(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getevmmaximumpeak__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getevmmaximumpeak__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the peak EVM measured per acquisition, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetEvmMaximumPeak(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_DDemodGetResultsEVMMaximumPeak() function in C.ParametersNameType

### GetEvmMaximumPeak(string, out double)

Gets the maximum of the peak EVM measured per acquisition, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetEvmMaximumPeak(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetResultsEVMMaximumPeak() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the peak EVM measured per acquisition. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getfskmeandeviation__string-out.html language=enus -->
## TOPIC 00110: GetFskMeanDeviation(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getfskmeandeviation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getfskmeandeviation__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference frequency-shift keying (FSK) deviation, in hertz (Hz), used to measure the FSK error. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetFskMeanDeviation(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_DDemodGetResultsFSKMeanDeviation()

### GetFskMeanDeviation(string, out double)

Gets the reference frequency-shift keying (FSK) deviation, in hertz (Hz), used to measure the FSK error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetFskMeanDeviation(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetResultsFSKMeanDeviation() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the reference FSK deviation, in Hz, used to measure the FSK error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getiqimpairmentsmeaniqoriginoffset__string-out.html language=enus -->
## TOPIC 00111: GetIQImpairmentsMeanIQOriginOffset(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getiqimpairmentsmeaniqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getiqimpairmentsmeaniqoriginoffset__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset, in dB, from the ideal location of the constellation origin. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetIQImpairmentsMeanIQOriginOffset(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_DDemodGetResultsIQImpairmentsMeanIQOriginOffset

### GetIQImpairmentsMeanIQOriginOffset(string, out double)

Gets the offset, in dB, from the ideal location of the constellation origin.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetIQImpairmentsMeanIQOriginOffset(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetResultsIQImpairmentsMeanIQOriginOffset() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the offset, in dB, from the ideal location of the constellation origin. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getmagnitudeerrormaximum__string-out.html language=enus -->
## TOPIC 00112: GetMagnitudeErrorMaximum(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getmagnitudeerrormaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getmagnitudeerrormaximum__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the magnitude error measured per acquisition, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetMagnitudeErrorMaximum(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_DDemodGetResultsMagnitudeErrorMaximum() function in

### GetMagnitudeErrorMaximum(string, out double)

Gets the maximum of the magnitude error measured per acquisition, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetMagnitudeErrorMaximum(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetResultsMagnitudeErrorMaximum() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the magnitude error measured per acquisition, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getmeanrhofactor__string-out.html language=enus -->
## TOPIC 00113: GetMeanRhoFactor(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getmeanrhofactor__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getmeanrhofactor__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the correlation of the measurement waveform and the reference waveform. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetMeanRhoFactor(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_DDemodGetResultsMeanRhoFactor() function in C.ParametersNameTypeD

### GetMeanRhoFactor(string, out double)

Gets the correlation of the measurement waveform and the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetMeanRhoFactor(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetResultsMeanRhoFactor() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the correlation of the measurement waveform and the reference waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getoffsetevmmeanrms__string-out.html language=enus -->
## TOPIC 00114: GetOffsetEvmMeanRms(string, out double)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getoffsetevmmeanrms__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodresults-getoffsetevmmeanrms__string-out.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS EVM measured per acquisition, as a percentage. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic int GetOffsetEvmMeanRms(string selectorString, out double value)RemarksThis method maps to the RFmxDemod_DDemodGetResultsOffsetEVMMeanRMS() function in C.ParametersNameType

### GetOffsetEvmMeanRms(string, out double)

Gets the mean of the RMS EVM measured per acquisition, as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public int GetOffsetEvmMeanRms(string selectorString, out double value)

#### Remarks

This method maps to the RFmxDemod_DDemodGetResultsOffsetEVMMeanRMS() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "", "result::r1". You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the RMS EVM measured per acquisition, as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxDemodMXDDemodResults Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodsearchlengthauto.html language=enus -->
## TOPIC 00115: RFmxDemodMXDDemodSearchLengthAuto Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodsearchlengthauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxddemodsearchlengthauto.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXDDemodSearchLengthAutoMembersNameValueDescriptionFalse0Synchr

### RFmxDemodMXDDemodSearchLengthAuto Enumeration

Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXDDemodSearchLengthAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Synchronization bit pattern is searched in a waveform within the search Length duration. |
| True | 1 | Synchronization bit pattern is searched in a waveform of length determined by the measurement. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00116: RFmxDemodMXIQPowerEdgeTriggerSlope Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxiqpoweredgetriggerslope.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify, and is used only when you set the SetTriggerType(string, RFmxDemodMXTriggerType) to DigitalEdge. S

### RFmxDemodMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify, and is used only when you set the [SetTriggerType(string, RFmxDemodMXTriggerType)](nationalinstruments-rfmx-demodmx-rfmxdemodmx-settriggertype__string-rfmxdemodmxtriggertype.html) to [DigitalEdge](nationalinstruments-rfmx-demodmx-rfmxdemodmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXIQPowerEdgeTriggerSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-demodmx-rfmxdemodmxpropertyid.html language=enus -->
## TOPIC 00117: RFmxDemodMXPropertyId Enumeration

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-demodmx-rfmxdemodmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-demodmx-rfmxdemodmxpropertyid.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute IDs. SyntaxNamespace: NationalInstruments.RFmx.DemodMXpublic enum RFmxDemodMXPropertyIdMembersNameValueDescriptionSelectedPorts2109437Specifies the instrument port to be configured to acquire a signal. Use RFmxInstrMX.GetAvailablePorts Method to get the valid port names.

### RFmxDemodMXPropertyId Enumeration

Specifies all the attribute IDs.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.DemodMX](nationalinstruments-rfmx-demodmx.html)

public enum RFmxDemodMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SelectedPorts | 2109437 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstrMX.GetAvailablePorts Method to get the valid port names. |
| CenterFrequency | 2105345 | Specifies the carrier frequency, in hertz (Hz), of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| ReferenceLevel | 2105347 | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ExternalAttenuation | 2105346 | Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
| ReferenceLevelHeadroom | 2109436 | Specifies the margin RFmx adds to the Reference Level method. |
| TriggerType | 2105348 | Specifies the type of reference trigger to use for signal acquisition. |
| DigitalEdgeTriggerSource | 2105349 | Specifies the source terminal for the digital-edge trigger. |
| DigitalEdgeTriggerEdge | 2105350 | Specifies a value that indicates whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. |
| IQPowerEdgeTriggerSource | 2105351 | Specifies the channel from which the device monitors the trigger. |
| IQPowerEdgeTriggerLevel | 2105352 | Specifies the threshold above or below which the signal analyzer triggers. |
| IQPowerEdgeTriggerLevelType | 2109439 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. |
| IQPowerEdgeTriggerSlope | 2105353 | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
| TriggerDelay | 2105354 | Specifies the trigger delay time, in seconds. |
| TriggerMinimumQuietTimeMode | 2105355 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 2105356 | Specifies the time duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q power-edge trigger. |
| ADemodMeasurementEnabled | 2097209 | Specifies whether to enable analog demodulation measurement. |
| ADemodAudioMeasurementEnabled | 2097216 | Specifies whether to enable audio measurement. |
| ADemodModulationType | 2097166 | Specifies the digital modulation type of the signal that needs to be analyzed. |
| ADemodAMCarrierSuppressed | 2097154 | Specifies the modulation type of the signal that needs to analyzed. |
| ADemodRbwFilterType | 2097168 | Specifies the shape of the digital resolution bandwidth (RBW) filter. |
| ADemodRbwFilterBandwidth | 2097169 | Specifies the bandwidth, in hertz (Hz), of the resolution bandwidth (RBW) filter to be applied to the signal acquired using zero span. |
| ADemodRbwFilterAlpha | 2097170 | Specifies the roll-off factor of the root-raised-cosine (RRC) filter. |
| ADemodMeasurementInterval | 2097165 | Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. |
| ADemodCarrierCorrectionFrequencyEnabled | 2097162 | Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. |
| ADemodCarrierCorrectionPhaseEnabled | 2097163 | Specifies whether to correct the carrier phase error when demodulating phase-modulated signals. |
| ADemodFMDeEmphasis | 2097164 | Specifies the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. |
| ADemodAudioFilterType | 2097155 | Specifies the audio filter to be applied on the analog demodulated signal. |
| ADemodAudioFilterLowerCutoffFrequency | 2097156 | Specifies the lower cutoff frequency, in hertz (Hz), of the custom audio filter. |
| ADemodAudioFilterUpperCutoffFrequency | 2097157 | Specifies the upper cutoff frequency, in hertz (Hz), of the custom audio filter. |
| ADemodAveragingEnabled | 2097158 | Specifies whether to enable averaging for the analog demodulation measurement. |
| ADemodAveragingCount | 2097159 | Specifies the number of acquisitions used for averaging. |
| ADemodAveragingType | 2097161 | Specifies the averaging type for the measurement. |
| ADemodAllTracesEnabled | 2097171 | Specifies whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement. |
| ADemodResultsMeanCarrierFrequencyError | 2097172 | Specifies the mean of the measured carrier frequency offset, in hertz (Hz). |
| ADemodResultsMeanCarrierPower | 2097173 | Specifies the mean of the measured carrier power, in dBm. |
| ADemodResultsMeanModulationFrequency | 2097174 | Specifies the mean of the demodulated signal frequency, in hertz (Hz). |
| ADemodResultsAverageSinad | 2097175 | Specifies the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. |
| ADemodResultsAverageThdWithNoise | 2097176 | Specifies the average of total harmonic distortion and noise present in the signal, as a percentage. |
| ADemodResultsAverageThd | 2097177 | Specifies the average of total harmonic distortion (TDH) present in the signal, as a percentage. |
| ADemodResultsAverageSnr | 2097178 | Specifies the averaged signal-to-noise ratio, in dB, of the demodulated signal. |
| ADemodResultsAMModulationDepthMeanStandardDeviation | 2097179 | Specifies the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |
| ADemodResultsAMModulationDepthMeanHalfPeakToPeak | 2097180 | Specifies the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage. |
| ADemodResultsAMModulationDepthMeanPositivePeak | 2097181 | Specifies the mean positive peak amplitude of the modulating signal, as a percentage. |
| ADemodResultsAMModulationDepthMeanNegativePeak | 2097182 | Specifies the mean negative peak amplitude of the modulating signal, as a percentage. |
| ADemodResultsAMModulationDepthMeanRms | 2097183 | Specifies the mean root mean square (RMS) amplitude of the modulating signal, as a percentage. |
| ADemodResultsAMModulationDepthMaximumStandardDeviation | 2097184 | Specifies the maximum modulation depth measured across multiple acquisitions, as a percentage. |
| ADemodResultsAMModulationDepthMaximumHalfPeakToPeak | 2097185 | Specifies the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| ADemodResultsAMModulationDepthMaximumPositivePeak | 2097186 | Specifies the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| ADemodResultsAMModulationDepthMaximumNegativePeak | 2097187 | Specifies the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| ADemodResultsAMModulationDepthMaximumRms | 2097188 | Specifies the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| ADemodResultsFMDeviationMeanStandardDeviation | 2097189 | Specifies the mean frequency deviation, in hertz (Hz), around the nominal frequency of the FM carrier. |
| ADemodResultsFMDeviationMeanHalfPeakToPeak | 2097190 | Specifies the mean (peak-to-peak)/2 frequency variation, in hertz (Hz), around the nominal frequency of the FM carrier. |
| ADemodResultsFMDeviationMeanPositivePeak | 2097191 | Specifies the mean positive peak frequency deviation, in hertz (Hz), of the frequency-modulated signal. |
| ADemodResultsFMDeviationMeanNegativePeak | 2097192 | Specifies the mean negative peak frequency deviation, in hertz (Hz), of the frequency-modulated signal. |
| ADemodResultsFMDeviationMeanRms | 2097193 | Specifies the mean RMS frequency deviation, in hertz (Hz), of the frequency-modulated signal. |
| ADemodResultsFMDeviationMaximumStandardDeviation | 2097194 | Specifies the maximum frequency deviation, in hertz (Hz), of the frequency-modulated signal measured across multiple acquisitions. |
| ADemodResultsFMDeviationMaximumHalfPeakToPeak | 2097195 | Specifies the maximum (peak-to-peak)/2 frequency variation, in hertz (Hz), around the nominal frequency of the FM carrier measured across multiple acquisitions. |
| ADemodResultsFMDeviationMaximumPositivePeak | 2097196 | Specifies the maximum positive peak frequency deviation, in hertz (Hz), of the frequency-modulated signal measured across multiple acquisitions. |
| ADemodResultsFMDeviationMaximumNegativePeak | 2097197 | Specifies the maximum negative peak frequency deviation, in hertz (Hz), of the frequency-modulated signal measured across multiple acquisitions. |
| ADemodResultsFMDeviationMaximumRms | 2097198 | Specifies the maximum RMS frequency deviation, in hertz (Hz), of the frequency-modulated signal measured across multiple acquisitions. |
| ADemodResultsPMDeviationMeanStandardDeviation | 2097199 | Specifies the the mean phase deviation, in degrees, around the unmodulated carrier phase. |
| ADemodResultsPMDeviationMeanHalfPeakToPeak | 2097200 | Specifies the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. |
| ADemodResultsPMDeviationMeanPositivePeak | 2097201 | Specifies the the mean positive peak phase deviation, in degrees, around the unmodulated carrier phase. |
| ADemodResultsPMDeviationMeanNegativePeak | 2097202 | Specifies the mean negative peak phase deviation, in degrees, around the unmodulated carrier phase. |
| ADemodResultsPMDeviationMeanRms | 2097203 | Specifies the mean RMS phase deviation, in degrees, of the phase-modulated signal. |
| ADemodResultsPMDeviationMaximumStandardDeviation | 2097204 | Specifies the maximum phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
| ADemodResultsPMDeviationMaximumHalfPeakToPeak | 2097205 | Specifies the maximum (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
| ADemodResultsPMDeviationMaximumPositivePeak | 2097206 | Specifies the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
| ADemodResultsPMDeviationMaximumNegativePeak | 2097207 | Specifies the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
| ADemodResultsPMDeviationMaximumRms | 2097208 | Specifies the maximum RMS phase deviation, in degrees, of the phase-modulated signal measured across multiple acquisitions. |
| DDemodMeasurementEnabled | 2101248 | Specifies whether digital demodulation measurement is enabled. |
| DDemodModulationType | 2101259 | Specifies the modulation type of the signal which needs to analyzed. |
| DDemodM | 2101257 | Specifies the M-ary number. The M-ary number is the number of distinct states that represent symbols in the complex baseband modulated waveform. |
| DDemodSpectrumInverted | 2101266 | Specifies whether to swap the acquired I and Q samples for demodulation. |
| DDemodPskFormat | 2101262 | Specifies the PSK format. |
| DDemodDifferentialEnabled | 2101253 | Specifies whether the symbols are differentially encoded, and applicable only to PSK and MSK modulation types. |
| DDemodSymbolRate | 2101267 | Specifies the number of symbols transmitted in one second, in hertz (Hz). |
| DDemodNumberOfSymbols | 2101261 | Specifies the number of symbols to be acquired and analyzed. The measurement acquires additional symbols to account for filter delays. |
| DDemodSamplesPerSymbol | 2101265 | Specifies the samples per symbol used to acquire and demodulate the signal. Sample Rate = Symbol Rate * Samples per Symbol. |
| DDemodEvmNormalizationReference | 2101305 | Specifies the reference used to normalize the error vector magnitude (EVM). |
| DDemodFskDeviation | 2101256 | Specifies the expected FSK frequency deviation. At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation. |
| DDemodFskReferenceCompensationEnabled | 2101304 | Specifies whether the FSK deviation that you specify is to be compensated for gain errors and is used to compute FSK error. |
| DDemodApskR2ToR1Ratio | 2101321 | Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. |
| DDemodApskR3ToR1Ratio | 2101322 | Specifies the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK. |
| DDemodSymbolMapType | 2101312 | Specifies whether the measurement uses the default symbol map or the map that you configure using the method. |
| DDemodPulseShapingFilterType | 2101263 | Specifies the pulse-shaping filter used to transmit the signal. |
| DDemodPulseShapingFilterParameter | 2101264 | Specifies the rolloff factor for raised cosine and root raised cosine filter, which are used as pulse shaping filter and measurement filter, respectively. |
| DDemodMeasurementFilterType | 2101258 | Specifies the measurement needed to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients. |
| DDemodEqualizerMode | 2101254 | Specifies whether the measurement needs to perform equalization. |
| DDemodEqualizerFilterLength | 2101302 | Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. |
| DDemodEqualizerTrainingCount | 2101303 | Specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. After the training stage, the measurement is performed over the specified number of averages. |
| DDemodEqualizerConvergenceFactor | 2101255 | Specifies the incremental step used by the equalizer to adapt to the channel during the training stage. |
| DDemodSynchronizationEnabled | 2101268 | Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. |
| DDemodSynchronizationBits | 2101279 | Specifies the synchronization bits used to create the reference sequence that needs to be searched in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence. |
| DDemodSynchronizationMeasurementOffset | 2101300 | Specifies the offset, which is the location from which the signal is considered for further measurements. |
| DDemodAveragingEnabled | 2101250 | Specifies whether averaging is enabled for digital demodulation measurements. |
| DDemodAveragingCount | 2101251 | Specifies the number of acquisitions used for averaging when averaging enabled is set to True. |
| DDemodSignalStructure | 2101313 | Specifies whether the signal is either a bursty signal or a continuous signal. |
| DDemodBurstStartExclusionSymbols | 2101314 | Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement. |
| DDemodBurstEndExclusionSymbols | 2101315 | Specifies the number of symbols that is excluded from the measurement before the falling edge of the burst. |
| DDemodIQOffsetRemovalEnabled | 2101316 | Specifies whether to remove the I/Q offset before the EVM measurement. |
| DDemodCfoEstimationMode | 2101317 | Specifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals. |
| DDemodSearchLengthAuto | 2101319 | Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. |
| DDemodSearchLength | 2101320 | Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the DDemod Search Length Auto property to True. |
| DDemodAllTracesEnabled | 2101269 | Specifies whether to enable the traces to be stored and retrieved after performing the digital demodulation. |
| DDemodResultsCarrierMeanFrequencyOffset | 2101281 | Specifies the frequency offset, in hertz (Hz), from the transmitted carrier frequency. |
| DDemodResultsCarrierMeanFrequencyDrift | 2101282 | Specifies the measured carrier frequency drift, in hertz (Hz). |
| DDemodResultsCarrierMeanPhaseError | 2101283 | Specifies the phase offset, in degrees, from the transmitted carrier phase. |
| DDemodResultsEvmMeanRms | 2101284 | Specifies the mean of the RMS EVM measured per acquisition, as a percentage. |
| DDemodResultsEvmMaximumRms | 2101285 | Specifies the maximum of the RMS EVM measured per acquisition, as a percentage. |
| DDemodResultsEvmMeanPeak | 2101286 | Specifies the mean of the peak error vector magnitude (EVM) measured per acquisition, as a percentage. |
| DDemodResultsEvmMaximumPeak | 2101287 | Specifies the maximum of the peak EVM measured per acquisition, as a percentage. |
| DDemodResultsEvmMeanModulationErrorRatio | 2101288 | Specifies the modulation error ratio (MER), in dB. |
| DDemodResultsOffsetEvmMeanRms | 2101306 | Specifies the mean of the RMS EVM measured per acquisition, as a percentage. |
| DDemodResultsOffsetEvmMeanPeak | 2101307 | Specifies the mean of the peak EVM measured per acquisition, as a percentage. |
| DDemodResultsOffsetEvmMaximumRms | 2101308 | Specifies the maximum of the RMS EVM, as a percentage, measured per acquisition, as a percentage. |
| DDemodResultsOffsetEvmMaximumPeak | 2101309 | Specifies the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
| DDemodResultsMagnitudeErrorMean | 2101289 | Specifies the mean of the magnitude error measured per acquisition, as a percentage. |
| DDemodResultsMagnitudeErrorMaximum | 2101290 | Specifies the maximum of the magnitude error measured per acquisition, as a percentage. |
| DDemodResultsPhaseErrorMean | 2101291 | Specifies the mean of the phase error, in degrees, measured per acquisition. |
| DDemodResultsPhaseErrorMaximum | 2101292 | Specifies the maximum of the phase error, in degrees, measured per acquisition. |
| DDemodResultsFskMeanDeviation | 2101293 | Specifies the reference frequency-shift keying (FSK) deviation, in hertz (Hz), used to measure the FSK error. |
| DDemodResultsFskMeanRmsFskError | 2101294 | Specifies the mean of the RMS frequency error, in hertz (Hz), of the FSK symbols measured per acquisition. |
| DDemodResultsFskMaximumPeakFskError | 2101295 | Specifies the mean peak deviation error, in hertz (Hz), of the FSK symbols measured per acquisition. |
| DDemodResultsIQImpairmentsMeanIQOriginOffset | 2101298 | Specifies the offset, in dB, from the ideal location of the constellation origin. |
| DDemodResultsIQImpairmentsMeanIQGainImbalance | 2101296 | Specifies the measured ratio of I gain to Q gain, in dB. |
| DDemodResultsIQImpairmentsMeanQuadratureSkew | 2101297 | Specifies a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. |
| DDemodResultsMeanRhoFactor | 2101310 | Specifies the correlation of the measurement waveform and the reference waveform. |
| DDemodResultsMeanAmplitudeDroop | 2101311 | Specifies the mean amplitude droop per symbol. |
| DDemodResultsSyncFound | 2101301 | Specifies whether the synchronization bits were found in the demodulated signal. |
| AutoLevelInitialReferenceLevel | 2105357 | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| LimitedConfigurationChange | 2105358 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| ResultFetchTimeout | 2109440 | Specifies the time, in seconds, for which the measurement waits for fetching results from the methods in the class. Set this value to a time longer than expected for fetching the measurement. |
| DDemodResultsCarrierMeanFrequencyError | 2101281 | Specifies the frequency offset, in hertz (Hz), from the transmitted carrier frequency. |
| DDemodResultsFskMeanRmsDeviationError | 2101294 | Specifies the mean of the RMS frequency error, in hertz (Hz), of the FSK symbols measured per acquisition. |
| DDemodResultsFskMeanPeakDeviationError | 2101295 | Specifies the mean peak deviation error, in hertz (Hz), of the FSK symbols measured per acquisition. |

Parent topic:

NationalInstruments.RFmx.DemodMX

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxdemodmxextension-getdemodsignalconfiguration__this-string.html language=enus -->
## TOPIC 00118: GetDemodSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxdemodmxextension-getdemodsignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxdemodmxextension-getdemodsignalconfiguration__this-string.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a Demod signal configuration for a specified signal name. An existing Demod signal configuration is returned if the specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxDemodMX GetDemodSignalConfiguration(this RFmxInstrMX instrSession, string signa

### GetDemodSignalConfiguration(this RFmxInstrMX, string)

Returns a Demod signal configuration for a specified signal name. An existing Demod signal configuration is returned if the specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxDemodMX](nationalinstruments-rfmx-demodmx-rfmxdemodmx.html) GetDemodSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Remarks

This method maps to the RFmxDemod_CreateSignalConfiguration() function in C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |
| signalName | string | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |

#### Returns

An object of type RFmxDemodMX

Parent topic:

RFmxDemodMXExtension Class

<!--NI_TOPIC bundle=rfmxdemod-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00119: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxdemod-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxdemod-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxDemodMXExtensionProvides extension methods to create Demod signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxDemodMXExtension | Provides extension methods to create Demod signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None
