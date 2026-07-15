# NI DOCUMENT BUNDLE: rfmxevdo-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxevdo-dotnet-api-ref start=1 end=227 -->
<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-configurecarrierfrequencyarray__string-double_arr1.html language=enus -->
## TOPIC 00001: ConfigureCarrierFrequencyArray(string, double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-configurecarrierfrequencyarray__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-configurecarrierfrequencyarray__string-double_arr1.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier frequency of the selected carriers as an offset frequency relative to the center frequency. Configure the center frequency by using the ConfigureFrequency(string, double) method. Configure the number of carriers using the ConfigureNumberOfCarriers(string, int) method.SyntaxNam

### ConfigureCarrierFrequencyArray(string, double[])

Configures the carrier frequency of the selected carriers as an offset frequency relative to the center frequency. 
 Configure the center frequency by using the [ConfigureFrequency(string, double)](nationalinstruments-rfmx-evdomx-rfmxevdomx-configurefrequency__string-double.html) method. Configure the number of carriers using the [ConfigureNumberOfCarriers(string, int)](nationalinstruments-rfmx-evdomx-rfmxevdomx-configurenumberofcarriers__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureCarrierFrequencyArray(string selectorString, double[] carrierFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| carrierFrequency | double[] | Specifies the carrier frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-configureiqpoweredgetrigger__string-string-rfmxevdomxiqpoweredgetriggerslope-double-double-rfmxevdomxtriggerminimumquiettimemode-double-rfmxev...d17e1024.html language=enus -->
## TOPIC 00002: ConfigureIQPowerEdgeTrigger(string, string, RFmxEvdoMXIQPowerEdgeTriggerSlope, double, double, RFmxEvdoMXTriggerMinimumQuietTimeMode, double, RFmxEvdoMXIQPowerEdgeTriggerLevelType, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-configureiqpoweredgetrigger__string-string-rfmxevdomxiqpoweredgetriggerslope-double-double-rfmxevdomxtriggerminimumquiettimemode-double-rfmxev...d17e1024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-configureiqpoweredgetrigger__string-string-rfmxevdomxiqpoweredgetriggerslope-double-double-rfmxevdomxtriggerminimumquiettimemode-double-rfmxev...d17e1024.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxEvdoMXI

### ConfigureIQPowerEdgeTrigger(string, string, RFmxEvdoMXIQPowerEdgeTriggerSlope, double, double, RFmxEvdoMXTriggerMinimumQuietTimeMode, double, RFmxEvdoMXIQPowerEdgeTriggerLevelType, bool)

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxEvdoMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope, double iqPowerEdgeTriggerLevel, double triggerDelay, RFmxEvdoMXTriggerMinimumQuietTimeMode minimumQuietTimeMode, double minimumQuietTimeDuration, RFmxEvdoMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| iqPowerEdgeTriggerSource | string | Specifies the channel from which the device monitors the trigger. |
| iqPowerEdgeTriggerSlope | RFmxEvdoMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| iqPowerEdgeTriggerLevel | double | Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| minimumQuietTimeMode | RFmxEvdoMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| minimumQuietTimeDuration | double | Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(string, RFmxEvdoMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level. |
| iqPowerEdgeTriggerLevelType | RFmxEvdoMXIQPowerEdgeTriggerLevelType | Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. |
| enableTrigger | bool | Specifies whether the trigger is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-configureuplinkuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxevdomxuplinkbranch_arr1.html language=enus -->
## TOPIC 00003: ConfigureUplinkUserDefinedChannelArray(string, int[], int[], RFmxEvdoMXUplinkBranch[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-configureuplinkuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxevdomxuplinkbranch_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-configureuplinkuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxevdomxuplinkbranch_arr1.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of user defined channels in the EV-DO uplink.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureUplinkUserDefinedChannelArray(string selectorString, int[] uplinkWalshCodeLength, int[] uplinkWalshCodeNumber, RFmxEvdoMXUplinkBranch[] uplinkBranch)ParametersNameTyp

### ConfigureUplinkUserDefinedChannelArray(string, int[], int[], RFmxEvdoMXUplinkBranch[])

Configures the array of user defined channels in the EV-DO uplink.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureUplinkUserDefinedChannelArray(string selectorString, int[] uplinkWalshCodeLength, int[] uplinkWalshCodeNumber, RFmxEvdoMXUplinkBranch[] uplinkBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| uplinkWalshCodeLength | int[] | Specifies the Walsh code length of a specific user-defined channel. |
| uplinkWalshCodeNumber | int[] | Specifies the Walsh code number of a specific user-defined channel. |
| uplinkBranch | RFmxEvdoMXUplinkBranch[] | Specifies the quadrature branch on which a specific user-defined channel is mapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getcarrierfrequency__string-out.html language=enus -->
## TOPIC 00004: GetCarrierFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getcarrierfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getcarrierfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. Use "carrier<em>(n)</em>" as the Selector Strings to configure or read this method. The default value is 0. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int G

### GetCarrierFrequency(string, out double)

Gets the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. Use "carrier<em>(n)</em>" as the Selector Strings to configure or read this method. The default value is 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [CarrierFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. Use "carrier<em>(n)</em>" as the Selector Strings to configure or read this method. The default value is 0. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getdigitaledgetriggeredge__string-out.html language=enus -->
## TOPIC 00005: GetDigitalEdgeTriggerEdge(string, out RFmxEvdoMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getdigitaledgetriggeredge__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getdigitaledgetriggeredge__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetDigitalEdgeTriggerEdge(string selectorString, out RFmxEvdoMXDigitalEdgeTriggerEdge value)

### GetDigitalEdgeTriggerEdge(string, out RFmxEvdoMXDigitalEdgeTriggerEdge)

Gets the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetDigitalEdgeTriggerEdge(string selectorString, out RFmxEvdoMXDigitalEdgeTriggerEdge value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-evdomx-rfmxevdomxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXDigitalEdgeTriggerEdge | Upon return, contains the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-geterror__out-out.html language=enus -->
## TOPIC 00006: GetError(out int, out string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-geterror__out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout stringUpon return, contains the

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getexternalattenuation__string-out.html language=enus -->
## TOPIC 00007: GetExternalAttenuation(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getexternalattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getexternalattenuation__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetExternalAttenuation(string selectorString, out double value)RemarksThis method gets the value of ExternalAtt

### GetExternalAttenuation(string, out double)

Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetExternalAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [ExternalAttenuation](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getiqpoweredgetriggerlevel__string-out.html language=enus -->
## TOPIC 00008: GetIQPowerEdgeTriggerLevel(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getiqpoweredgetriggerlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getiqpoweredgetriggerlevel__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxEvdoMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger whe

### GetIQPowerEdgeTriggerLevel(string, out double)

Gets the power level at which the device triggers. This value is expressed in dB when the [SetIQPowerEdgeTriggerLevelType(string, RFmxEvdoMXIQPowerEdgeTriggerLevelType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-setiqpoweredgetriggerleveltype__string-rfmxevdomxiqpoweredgetriggerleveltype.html) method is set to [Relative](nationalinstruments-rfmx-evdomx-rfmxevdomxiqpoweredgetriggerleveltype.html) and in dBm when the IQ Power Edge Level Type method is set to [Absolute](nationalinstruments-rfmx-evdomx-rfmxevdomxiqpoweredgetriggerleveltype.html). The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetIQPowerEdgeTriggerLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is -20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxEvdoMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getiqpoweredgetriggersource__string-out.html language=enus -->
## TOPIC 00009: GetIQPowerEdgeTriggerSource(string, out string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getiqpoweredgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getiqpoweredgetriggersource__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetIQPowerEdgeTriggerSource(string selectorString, out string value)R

### GetIQPowerEdgeTriggerSource(string, out string)

Gets the channel from which the device monitors the trigger. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetIQPowerEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getnumberofcarriers__string-out.html language=enus -->
## TOPIC 00010: GetNumberOfCarriers(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getnumberofcarriers__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getnumberofcarriers__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of carriers in the signal. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetNumberOfCarriers(string selectorString, out int value)RemarksThis method gets the value of NumberOfCarriers attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringPass

### GetNumberOfCarriers(string, out int)

Gets the number of carriers in the signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetNumberOfCarriers(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfCarriers](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of carriers in the signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getreferencelevelheadroom__string-out.html language=enus -->
## TOPIC 00011: GetReferenceLevelHeadroom(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getreferencelevelheadroom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getreferencelevelheadroom__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal

### GetReferenceLevelHeadroom(string, out double)

Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetReferenceLevelHeadroom(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getselectedports__string-out.html language=enus -->
## TOPIC 00012: GetSelectedPorts(string, out string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getselectedports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getselectedports__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default valu

### GetSelectedPorts(string, out string)

Gets the instrument port to be configured to acquire a signal. **Valid values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830: if0, if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Default values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830/5831/5832: if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Supported devices**: PXIe-5820/5830/5831/5832/5840 
</x></x>

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSelectedPorts(string selectorString, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Specifies the instrument port to be used by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getuplinkwalshcodelength__string-out.html language=enus -->
## TOPIC 00013: GetUplinkWalshCodeLength(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getuplinkwalshcodelength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getuplinkwalshcodelength__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Walsh Code Length of a specific user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method. SyntaxNamespace:

### GetUplinkWalshCodeLength(string, out int)

Gets the Walsh Code Length of a specific user-defined channel. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomx-setchannelconfigurationmode__string-rfmxevdomxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html). Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkWalshCodeLength(string selectorString, out int value)

#### Remarks

This method gets the value of [UplinkWalshCodeLength](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 64.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the channel number. Example: "channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the Walsh Code Length of a specific user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-getuplinkwalshcodenumber__string-out.html language=enus -->
## TOPIC 00014: GetUplinkWalshCodeNumber(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-getuplinkwalshcodenumber__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-getuplinkwalshcodenumber__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Walsh Code Number of a specific user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method. SyntaxNamespace:

### GetUplinkWalshCodeNumber(string, out int)

Gets the Walsh Code Number of a specific user-defined channel. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomx-setchannelconfigurationmode__string-rfmxevdomxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html). Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkWalshCodeNumber(string selectorString, out int value)

#### Remarks

This method gets the value of [UplinkWalshCodeNumber](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the channel number. Example: "channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the Walsh Code Number of a specific user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-initiate__string-string.html language=enus -->
## TOPIC 00015: Initiate(string, string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-initiate__string-string.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods. To get the

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods. To get the status of measurements, use the [WaitForMeasurementComplete(string, double)](nationalinstruments-rfmx-evdomx-rfmxevdomx-waitformeasurementcomplete__string-double.html) method or [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-evdomx-rfmxevdomx-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int Initiate(string selectorString, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. The result name can be specified either through this input or through the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-isdisposed.html language=enus -->
## TOPIC 00016: IsDisposed

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-isdisposed.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-resettodefault__string.html language=enus -->
## TOPIC 00017: ResetToDefault(string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-resettodefault__string.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used.ReturnsReturns th

### ResetToDefault(string)

Resets a signal to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00018: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-sendsoftwareedgetrigger.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxEVDO_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SendSoftwar

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the RFmxEVDO_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SendSoftwareEdgeTrigger()

#### Remarks

1. You configure an invalid trigger.
2. You have not previously called the RFmxEvdoMX.Initiate method.

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-setattributeint__string-int-int.html language=enus -->
## TOPIC 00019: SetAttributeInt(string, int, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-setattributeint__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-setattributeint__string-int-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Int attribute. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAttributeInt(string selectorString, int attributeIdentifier, int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a Sel

### SetAttributeInt(string, int, int)

Sets the value of a Int attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAttributeInt(string selectorString, int attributeIdentifier, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx EVDO Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-setdigitaledgetriggeredge__string-rfmxevdomxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00020: SetDigitalEdgeTriggerEdge(string, RFmxEvdoMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-setdigitaledgetriggeredge__string-rfmxevdomxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-setdigitaledgetriggeredge__string-rfmxevdomxdigitaledgetriggeredge.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetDigitalEdgeTriggerEdge(string selectorString, RFmxEvdoMXDigitalEdgeTriggerEdge value)Rema

### SetDigitalEdgeTriggerEdge(string, RFmxEvdoMXDigitalEdgeTriggerEdge)

Sets the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetDigitalEdgeTriggerEdge(string selectorString, RFmxEvdoMXDigitalEdgeTriggerEdge value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-evdomx-rfmxevdomxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-setdigitaledgetriggersource__string-string.html language=enus -->
## TOPIC 00021: SetDigitalEdgeTriggerSource(string, string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-setdigitaledgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-setdigitaledgetriggersource__string-string.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetDigitalEdgeTriggerSource(string selectorString, string value)RemarksThis

### SetDigitalEdgeTriggerSource(string, string)

Sets the source terminal for the digital edge trigger. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetDigitalEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is RFMXEVDO_VAL_PFI0_STR.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-setexternalattenuation__string-double.html language=enus -->
## TOPIC 00022: SetExternalAttenuation(string, double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-setexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-setexternalattenuation__string-double.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetExternalAttenuation(string selectorString, double value)RemarksThis method sets the value of ExternalAttenua

### SetExternalAttenuation(string, double)

Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetExternalAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [ExternalAttenuation](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-setiqpoweredgetriggerlevel__string-double.html language=enus -->
## TOPIC 00023: SetIQPowerEdgeTriggerLevel(string, double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-setiqpoweredgetriggerlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-setiqpoweredgetriggerlevel__string-double.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxEvdoMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger whe

### SetIQPowerEdgeTriggerLevel(string, double)

Sets the power level at which the device triggers. This value is expressed in dB when the [SetIQPowerEdgeTriggerLevelType(string, RFmxEvdoMXIQPowerEdgeTriggerLevelType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-setiqpoweredgetriggerleveltype__string-rfmxevdomxiqpoweredgetriggerleveltype.html) method is set to [Relative](nationalinstruments-rfmx-evdomx-rfmxevdomxiqpoweredgetriggerleveltype.html) and in dBm when the IQ Power Edge Level Type method is set to [Absolute](nationalinstruments-rfmx-evdomx-rfmxevdomxiqpoweredgetriggerleveltype.html). The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetIQPowerEdgeTriggerLevel(string selectorString, double value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is -20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxEvdoMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomx-setlimitedconfigurationchange__string-rfmxevdomxlimitedconfigurationchange.html language=enus -->
## TOPIC 00024: SetLimitedConfigurationChange(string, RFmxEvdoMXLimitedConfigurationChange)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomx-setlimitedconfigurationchange__string-rfmxevdomxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomx-setlimitedconfigurationchange__string-rfmxevdomxlimitedconfigurationchange.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetLimitedConfigurationChange(string selectorString, RFmxEvdoMXLimitedConfigurationChange value)RemarksThis method sets the value of LimitedConf

### SetLimitedConfigurationChange(string, RFmxEvdoMXLimitedConfigurationChange)

Sets the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetLimitedConfigurationChange(string selectorString, RFmxEvdoMXLimitedConfigurationChange value)

#### Remarks

This method sets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-evdomx-rfmxevdomxlimitedconfigurationchange.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMX Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configureaveraging__string-rfmxevdomxacpaveragingenabled-int-rfmxevdomxacpaveragingtype.html language=enus -->
## TOPIC 00025: ConfigureAveraging(string, RFmxEvdoMXAcpAveragingEnabled, int, RFmxEvdoMXAcpAveragingType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configureaveraging__string-rfmxevdomxacpaveragingenabled-int-rfmxevdomxacpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configureaveraging__string-rfmxevdomxacpaveragingenabled-int-rfmxevdomxacpaveragingtype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the adjacent channel power (ACP) measurement.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureAveraging(string selectorString, RFmxEvdoMXAcpAveragingEnabled averagingEnabled, int averagingCount, RFmxEvdoMXAcpAveragingType averagingType)ParametersNameTypeDe

### ConfigureAveraging(string, RFmxEvdoMXAcpAveragingEnabled, int, RFmxEvdoMXAcpAveragingType)

Configures averaging for the adjacent channel power (ACP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureAveraging(string selectorString, RFmxEvdoMXAcpAveragingEnabled averagingEnabled, int averagingCount, RFmxEvdoMXAcpAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxEvdoMXAcpAveragingEnabled | Specifies whether to enable averaging of the spectrum for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxEvdoMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configuremeasurementmethod__string-rfmxevdomxacpmeasurementmethod.html language=enus -->
## TOPIC 00026: ConfigureMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configuremeasurementmethod__string-rfmxevdomxacpmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configuremeasurementmethod__string-rfmxevdomxacpmeasurementmethod.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the adjacent channel power (ACP) measurement.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureMeasurementMethod(string selectorString, RFmxEvdoMXAcpMeasurementMethod measurementMethod)ParametersNameTypeDescriptionselectorStringstringPass an emp

### ConfigureMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod)

Configures the method for performing the adjacent channel power (ACP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureMeasurementMethod(string selectorString, RFmxEvdoMXAcpMeasurementMethod measurementMethod)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementMethod | RFmxEvdoMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configurenumberofoffsets__string-int.html language=enus -->
## TOPIC 00027: ConfigureNumberOfOffsets(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configurenumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configurenumberofoffsets__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureNumberOfOffsets(string selectorString, int numberOfOffsets)ParametersNameTypeDe

### ConfigureNumberOfOffsets(string, int)

Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureNumberOfOffsets(string selectorString, int numberOfOffsets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfOffsets | int | Specifies the number of offset channel pairs. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configureoffsetpowerreference__string-rfmxevdomxacpoffsetpowerreferencecarrier-int.html language=enus -->
## TOPIC 00028: ConfigureOffsetPowerReference(string, RFmxEvdoMXAcpOffsetPowerReferenceCarrier, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configureoffsetpowerreference__string-rfmxevdomxacpoffsetpowerreferencecarrier-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configureoffsetpowerreference__string-rfmxevdomxacpoffsetpowerreferencecarrier-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power reference of the offset channels in multi-carrier setups.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureOffsetPowerReference(string selectorString, RFmxEvdoMXAcpOffsetPowerReferenceCarrier offsetPowerReferenceCarrier, int offsetPowerReferenceSpecific)Paramet

### ConfigureOffsetPowerReference(string, RFmxEvdoMXAcpOffsetPowerReferenceCarrier, int)

Configures the power reference of the offset channels in multi-carrier setups.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureOffsetPowerReference(string selectorString, RFmxEvdoMXAcpOffsetPowerReferenceCarrier offsetPowerReferenceCarrier, int offsetPowerReferenceSpecific)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| offsetPowerReferenceCarrier | RFmxEvdoMXAcpOffsetPowerReferenceCarrier | Specifies how the reference power is selected. |
| offsetPowerReferenceSpecific | int | Specifies the carrier number that is used as power reference. This parameter only applies if you set the offsetPowerReferenceCarrier parameter to Specific. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configurerbwfilter__string-rfmxevdomxacprbwautobandwidth-double-rfmxevdomxacprbwfiltertype.html language=enus -->
## TOPIC 00029: ConfigureRbwFilter(string, RFmxEvdoMXAcpRbwAutoBandwidth, double, RFmxEvdoMXAcpRbwFilterType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configurerbwfilter__string-rfmxevdomxacprbwautobandwidth-double-rfmxevdomxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-configurerbwfilter__string-rfmxevdomxacprbwautobandwidth-double-rfmxevdomxacprbwfiltertype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureRbwFilter(string selectorString, RFmxEvdoMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxEvdoMXAcpRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an e

### ConfigureRbwFilter(string, RFmxEvdoMXAcpRbwAutoBandwidth, double, RFmxEvdoMXAcpRbwFilterType)

Configures the resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureRbwFilter(string selectorString, RFmxEvdoMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxEvdoMXAcpRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxEvdoMXAcpRbwAutoBandwidth | Specifies whether the measurement calculates the RBW. |
| rbw | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxEvdoMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00030: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ACP carrier integration bandwidth. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of AcpCarrierIntegrationBandwidth attribute.ParametersNameTyp

### GetCarrierIntegrationBandwidth(string, out double)

Gets the ACP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpCarrierIntegrationBandwidth](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the ACP carrier integration bandwidth. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getfarifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00031: GetFarIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getfarifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getfarifoutputpoweroffset__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRa

### GetFarIFOutputPowerOffset(string, out double)

Gets the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setmeasurementmethod__string-rfmxevdomxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-evdomx-rfmxevdomxacpmeasurementmethod.html) and set the [SetIFOutputPowerOffsetAuto(string, RFmxEvdoMXAcpIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxevdomxacpifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-evdomx-rfmxevdomxacpifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetFarIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpFarIFOutputPowerOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(string, RFmxEvdoMXAcpIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getfftoverlap__string-out.html language=enus -->
## TOPIC 00032: GetFftOverlap(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getfftoverlap__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getfftoverlap__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the percentage of acquired samples to overlap while performing FFT. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetFftOverlap(string selectorString, out double value)RemarksThis method gets the value of AcpFftOverlap attribute.ParametersNameTypeDescriptionselectorStringstringPass

### GetFftOverlap(string, out double)

Gets the percentage of acquired samples to overlap while performing FFT.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetFftOverlap(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpFftOverlap](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the number of samples to overlap between consecutive chunks while performing FFT. This value is expressed as a percentage of AcpSequentialFftSize method when you set the AcpMeasurementMethod method to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00033: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of AcpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStri

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [AcpMeasurementEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getnearifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00034: GetNearIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getnearifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getnearifoutputpoweroffset__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange

### GetNearIFOutputPowerOffset(string, out double)

Gets the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setmeasurementmethod__string-rfmxevdomxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-evdomx-rfmxevdomxacpmeasurementmethod.html) and set the [SetIFOutputPowerOffsetAuto(string, RFmxEvdoMXAcpIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxevdomxacpifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-evdomx-rfmxevdomxacpifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetNearIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpNearIFOutputPowerOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(string, RFmxEvdoMXAcpIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getoffsetpowerreferencecarrier__string-out.html language=enus -->
## TOPIC 00035: GetOffsetPowerReferenceCarrier(string, out RFmxEvdoMXAcpOffsetPowerReferenceCarrier)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getoffsetpowerreferencecarrier__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getoffsetpowerreferencecarrier__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier number that is used as the power reference to measure the offset channel relative power. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetOffsetPowerReferenceCarrier(string selectorString, out RFmxEvdoMXAcpOffsetPowerReferenceCarrier value)RemarksThis method gets the va

### GetOffsetPowerReferenceCarrier(string, out RFmxEvdoMXAcpOffsetPowerReferenceCarrier)

Gets the carrier number that is used as the power reference to measure the offset channel relative power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetOffsetPowerReferenceCarrier(string selectorString, out RFmxEvdoMXAcpOffsetPowerReferenceCarrier value)

#### Remarks

This method gets the value of [AcpOffsetPowerReferenceCarrier](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Composite](nationalinstruments-rfmx-evdomx-rfmxevdomxacpoffsetpowerreferencecarrier.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXAcpOffsetPowerReferenceCarrier | Upon return, contains the carrier number that is used as the power reference to measure the offset channel relative power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getoffsetpowerreferencespecific__string-out.html language=enus -->
## TOPIC 00036: GetOffsetPowerReferenceSpecific(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getoffsetpowerreferencespecific__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getoffsetpowerreferencespecific__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the SetOffsetPowerReferenceCarrier(string, RFmxEvdoMXAcpOffsetPowerReferenceCarrier) method to Specific. SyntaxN

### GetOffsetPowerReferenceSpecific(string, out int)

Gets the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the [SetOffsetPowerReferenceCarrier(string, RFmxEvdoMXAcpOffsetPowerReferenceCarrier)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setoffsetpowerreferencecarrier__string-rfmxevdomxacpoffsetpowerreferencecarrier.html) method to [Specific](nationalinstruments-rfmx-evdomx-rfmxevdomxacpoffsetpowerreferencecarrier.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetOffsetPowerReferenceSpecific(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpOffsetPowerReferenceSpecific](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the SetOffsetPowerReferenceCarrier(string, RFmxEvdoMXAcpOffsetPowerReferenceCarrier) method to Specific. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00037: GetRbwFilterAutoBandwidth(string, out RFmxEvdoMXAcpRbwAutoBandwidth)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getrbwfilterautobandwidth__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetRbwFilterAutoBandwidth(string selectorString, out RFmxEvdoMXAcpRbwAutoBandwidth value)RemarksThis method gets the value of AcpRbwFilterAutoBandwidth attribute.The default value is True.Parame

### GetRbwFilterAutoBandwidth(string, out RFmxEvdoMXAcpRbwAutoBandwidth)

Gets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetRbwFilterAutoBandwidth(string selectorString, out RFmxEvdoMXAcpRbwAutoBandwidth value)

#### Remarks

This method gets the value of [AcpRbwFilterAutoBandwidth](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-evdomx-rfmxevdomxacprbwautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXAcpRbwAutoBandwidth | Upon return, contains whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00038: GetRbwFilterType(string, out RFmxEvdoMXAcpRbwFilterType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetRbwFilterType(string selectorString, out RFmxEvdoMXAcpRbwFilterType value)RemarksThis method gets the value of AcpRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDescriptio

### GetRbwFilterType(string, out RFmxEvdoMXAcpRbwFilterType)

Gets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetRbwFilterType(string selectorString, out RFmxEvdoMXAcpRbwFilterType value)

#### Remarks

This method gets the value of [AcpRbwFilterType](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-evdomx-rfmxevdomxacprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXAcpRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getsequentialfftsize__string-out.html language=enus -->
## TOPIC 00039: GetSequentialFftSize(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getsequentialfftsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getsequentialfftsize__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of bins to use for FFT computation when the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method is set to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetSequentialFftSize(string selectorString, out int value)RemarksThis method gets the va

### GetSequentialFftSize(string, out int)

Gets the number of bins to use for FFT computation when the [SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setmeasurementmethod__string-rfmxevdomxacpmeasurementmethod.html) method is set to [SequentialFft](nationalinstruments-rfmx-evdomx-rfmxevdomxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSequentialFftSize(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpSequentialFftSize](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 512.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of bins to use for FFT computation when the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method is set to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00040: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxEvdoMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method gets the value of

### GetSweepTimeInterval(string, out double)

Gets the sweep time when you set the [SetSweepTimeAuto(string, RFmxEvdoMXAcpSweepTimeAuto)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setsweeptimeauto__string-rfmxevdomxacpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-evdomx-rfmxevdomxacpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpSweepTimeInterval](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.00167 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time when you set the SetSweepTimeAuto(string, RFmxEvdoMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00041: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of AcpAllTracesEnabled attribute.The default value is

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00042: SetAveragingCount(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXAcpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of AcpAveragi

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxEvdoMXAcpAveragingEnabled)](nationalinstruments-rfmx-evdomx-rfmxevdomxacpconfiguration-setaveragingenabled__string-rfmxevdomxacpaveragingenabled.html) method to [True](nationalinstruments-rfmx-evdomx-rfmxevdomxacpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [AcpAveragingCount](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXAcpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-fetchabsolutepowerstrace__string-double-int-ref.html language=enus -->
## TOPIC 00043: FetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-fetchabsolutepowerstrace__string-double-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-fetchabsolutepowerstrace__string-double-int-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the adjacent channel power (ACP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchAbsolutePowersTrace(string selectorString, double timeout, int traceIndex, ref Spectrum< float > absolutePowersTrace)ParametersNameTypeDescriptionselect

### FetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >)

Fetches the absolute powers trace for the adjacent channel power (ACP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchAbsolutePowersTrace(string selectorString, double timeout, int traceIndex, ref Spectrum< float > absolutePowersTrace)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| traceIndex | int | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| absolutePowersTrace | ref Spectrum< float > | Returns the trace of measured integrated power specified in the traceIndex parameter. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-fetchtotalcarrierpower__string-double-out.html language=enus -->
## TOPIC 00044: FetchTotalCarrierPower(string, double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-fetchtotalcarrierpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-fetchtotalcarrierpower__string-double-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power measured by the adjacent channel power (ACP) measurement.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchTotalCarrierPower(string selectorString, double timeout, out double totalCarrierPower)ParametersNameTypeDescriptionselectorStringstringSpecifies a

### FetchTotalCarrierPower(string, double, out double)

Fetches the total carrier power measured by the adjacent channel power (ACP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchTotalCarrierPower(string selectorString, double timeout, out double totalCarrierPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalCarrierPower | out double | Upon return, contains the total carrier power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-getcarrierrelativepower__string-out.html language=enus -->
## TOPIC 00045: GetCarrierRelativePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-getcarrierrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults-getcarrierrelativepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the relative measured carrier power. This value is expressed in dB. Use "carrier<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierRelativePower(string selectorString, out double value)RemarksThis method gets the value

### GetCarrierRelativePower(string, out double)

Gets the relative measured carrier power. This value is expressed in dB. Use "carrier<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsCarrierRelativePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the relative measured carrier power. This value is expressed in dB. Use "carrier<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXAcpResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults.html language=enus -->
## TOPIC 00046: RFmxEvdoMXAcpResults Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxacpresults.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the ACP measurement results. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXAcpResults : RFmxEvdoMXSubObjectMethodsNameDescriptionFetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >)Fetches the

### RFmxEvdoMXAcpResults Class

Provides methods to fetch and read the ACP measurement results.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXAcpResults : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >) | Fetches the absolute powers trace for the adjacent channel power (ACP) measurement. |
| FetchCarrierMeasurement(string, double, out double, out double) | Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier(n)" as the selector string to read results from this method. |
| FetchCarrierMeasurementArray(string, double, ref double[], ref double[]) | Returns the absolute and relative powers measured in the carrier channels. The relative powers are measured relative to the integrated power of the power reference carrier. |
| FetchOffsetMeasurement(string, double, out double, out double, out double, out double) | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Use "offset(n)" as the selector string to read results from this method. |
| FetchOffsetMeasurementArray(string, double, ref double[], ref double[], ref double[], ref double[]) | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
| FetchRelativePowersTrace(string, double, int, ref Spectrum< float >) | Fetches the relative powers trace for the adjacent channel power (ACP) measurement. |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for the adjacent channel power (ACP) measurement. |
| FetchTotalCarrierPower(string, double, out double) | Fetches the total carrier power measured by the adjacent channel power (ACP) measurement. |
| GetCarrierAbsolutePower(string, out double) | Gets the absolute measured carrier power. This value is expressed in dBm. Use "carrier<em>(n)</em>" as the selector string to read this method. |
| GetCarrierRelativePower(string, out double) | Gets the relative measured carrier power. This value is expressed in dB. Use "carrier<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetAbsolutePower(string, out double) | Gets the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetRelativePower(string, out double) | Gets the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetTotalCarrierPower(string, out double) | Gets the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm. |
| GetUpperOffsetAbsolutePower(string, out double) | Gets the absolute measured upper offset channel power. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetRelativePower(string, out double) | Gets the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-getuplinkwalshcodenumber__string-out.html language=enus -->
## TOPIC 00047: GetUplinkWalshCodeNumber(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-getuplinkwalshcodenumber__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-getuplinkwalshcodenumber__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Walsh code number of the channel, subject to channel-specific analysis. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkWalshCodeNumber(string selectorString, out int value)RemarksThis method gets the value of CdaUplinkWalshCodeNumber attribute.The default value is 0. Th

### GetUplinkWalshCodeNumber(string, out int)

Gets the Walsh code number of the channel, subject to channel-specific analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkWalshCodeNumber(string selectorString, out int value)

#### Remarks

This method gets the value of [CdaUplinkWalshCodeNumber](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0. The maximum value is 31.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the Walsh code number of the channel, subject to channel-specific analysis. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00048: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces after performing the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of CdaAllTracesEnabled attribute.The default value is FALSE.ParametersNameTypeDes

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces after performing the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [CdaAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces after performing the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00049: SetMeasurementLength(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the CDA measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of CdaMeasurementLength attribute.The default value is 1. Valid values are [1

### SetMeasurementLength(string, int)

Sets the duration of the CDA measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [CdaMeasurementLength](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 1. Valid values are [1, 16]. The sum of the CDA Meas Offset and CDA Meas Length is less than or equal to 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the CDA measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00050: SetMeasurementOffset(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXCdaSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasurement

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxEvdoMXCdaSynchronizationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setsynchronizationmode__string-rfmxevdomxcdasynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [CdaMeasurementOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0. Valid values are [0,15]. The sum of CDA Meas Offset and CDA Meas Length is less than or equal to 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXCdaSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setsynchronizationmode__string-rfmxevdomxcdasynchronizationmode.html language=enus -->
## TOPIC 00051: SetSynchronizationMode(string, RFmxEvdoMXCdaSynchronizationMode)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setsynchronizationmode__string-rfmxevdomxcdasynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setsynchronizationmode__string-rfmxevdomxcdasynchronizationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed from the frame, slot, or symbol boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetSynchronizationMode(string selectorString, RFmxEvdoMXCdaSynchronizationMode value)RemarksThis method sets the value of CdaSynchronizationMode attribute.Th

### SetSynchronizationMode(string, RFmxEvdoMXCdaSynchronizationMode)

Sets whether the measurement is performed from the frame, slot, or symbol boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetSynchronizationMode(string selectorString, RFmxEvdoMXCdaSynchronizationMode value)

#### Remarks

This method sets the value of [CdaSynchronizationMode](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Slot](nationalinstruments-rfmx-evdomx-rfmxevdomxcdasynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXCdaSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setuplinkwalshcodenumber__string-int.html language=enus -->
## TOPIC 00052: SetUplinkWalshCodeNumber(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setuplinkwalshcodenumber__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaconfiguration-setuplinkwalshcodenumber__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Walsh code number of the channel, subject to channel-specific analysis. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetUplinkWalshCodeNumber(string selectorString, int value)RemarksThis method sets the value of CdaUplinkWalshCodeNumber attribute.The default value is 0. The ma

### SetUplinkWalshCodeNumber(string, int)

Sets the Walsh code number of the channel, subject to channel-specific analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetUplinkWalshCodeNumber(string selectorString, int value)

#### Remarks

This method sets the value of [CdaUplinkWalshCodeNumber](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0. The maximum value is 31.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the Walsh code number of the channel, subject to channel-specific analysis. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaiqgainimbalanceremovalenabled.html language=enus -->
## TOPIC 00053: RFmxEvdoMXCdaIQGainImbalanceRemovalEnabled Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaiqgainimbalanceremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaiqgainimbalanceremovalenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXCdaIQGainImbalanceRemovalEnabledMembersNameValueDescriptionFalse0The I/Q gain imbalance is not removed before the CDA measurement. True1The I/Q gain im

### RFmxEvdoMXCdaIQGainImbalanceRemovalEnabled Enumeration

Specifies whether to remove the I/Q gain imbalance before the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXCdaIQGainImbalanceRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The I/Q gain imbalance is not removed before the CDA measurement. |
| True | 1 | The I/Q gain imbalance is removed before the CDA measurement. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinkcodedomainiandqpower__string-double-out-out-out-out.html language=enus -->
## TOPIC 00054: FetchUplinkCodeDomainIAndQPower(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinkcodedomainiandqpower__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinkcodedomainiandqpower__string-double-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q mean active powers and the I and Q peak inactive powers.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUplinkCodeDomainIAndQPower(string selectorString, double timeout, out double iMeanActivePower, out double qMeanActivePower, out double iPeakInactivePower, out d

### FetchUplinkCodeDomainIAndQPower(string, double, out double, out double, out double, out double)

Fetches the I and Q mean active powers and the I and Q peak inactive powers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUplinkCodeDomainIAndQPower(string selectorString, double timeout, out double iMeanActivePower, out double qMeanActivePower, out double iPeakInactivePower, out double qPeakInactivePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| iMeanActivePower | out double | Upon return, contains the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| qMeanActivePower | out double | Upon return, contains the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| iPeakInactivePower | out double | Upon return, contains the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| qPeakInactivePower | out double | Upon return, contains the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinkcodedomainpower__string-double-out-out-out-out-out-out.html language=enus -->
## TOPIC 00055: FetchUplinkCodeDomainPower(string, double, out double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinkcodedomainpower__string-double-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinkcodedomainpower__string-double-out-out-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the scalar code domain power results.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUplinkCodeDomainPower(string selectorString, double timeout, out double totalPower, out double totalActivePower, out double meanActivePower, out double peakActivePower, out double meanInactiv

### FetchUplinkCodeDomainPower(string, double, out double, out double, out double, out double, out double, out double)

Fetches the scalar code domain power results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUplinkCodeDomainPower(string selectorString, double timeout, out double totalPower, out double totalActivePower, out double meanActivePower, out double peakActivePower, out double meanInactivePower, out double peakInactivePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalPower | out double | Upon return, contains the mean power of the received signal. This value is expressed in dBm. |
| totalActivePower | out double | Upon return, contains the sum of the powers of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| meanActivePower | out double | Upon return, contains the average power of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| peakActivePower | out double | Upon return, contains the maximum power among all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| meanInactivePower | out double | Upon return, contains the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| peakInactivePower | out double | Upon return, contains the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinksymbolconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00056: FetchUplinkSymbolConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinksymbolconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-fetchuplinksymbolconstellationtrace__string-double-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the configured measurement channel.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUplinkSymbolConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] symbolConstellation)ParametersNameTypeDescriptionselectorStringstring

### FetchUplinkSymbolConstellationTrace(string, double, ref ComplexSingle[])

Fetches the symbol constellation trace of the configured measurement channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUplinkSymbolConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] symbolConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| symbolConstellation | ref ComplexSingle[] | Upon return, contains the complex signal values stored in an array. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getchiprateerror__string-out.html language=enus -->
## TOPIC 00057: GetChipRateError(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getchiprateerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getchiprateerror__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the chip rate error. This value is expressed in ppm. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetChipRateError(string selectorString, out double value)RemarksThis method gets the value of CdaResultsChipRateError attribute.ParametersNameTypeDescriptionselectorStringstringSpecif

### GetChipRateError(string, out double)

Gets the chip rate error. This value is expressed in ppm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetChipRateError(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsChipRateError](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the chip rate error. This value is expressed in ppm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getiqoriginoffset__string-out.html language=enus -->
## TOPIC 00058: GetIQOriginOffset(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getiqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getiqoriginoffset__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q origin offset. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetIQOriginOffset(string selectorString, out double value)RemarksThis method gets the value of CdaResultsIQOriginOffset attribute.ParametersNameTypeDescriptionselectorStringstringSpe

### GetIQOriginOffset(string, out double)

Gets the I/Q origin offset. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsIQOriginOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q origin offset. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getiqquadratureerror__string-out.html language=enus -->
## TOPIC 00059: GetIQQuadratureError(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getiqquadratureerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getiqquadratureerror__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q quadrature error. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetIQQuadratureError(string selectorString, out double value)RemarksThis method gets the value of CdaResultsIQQuadratureError attribute.ParametersNameTypeDescriptionselectorS

### GetIQQuadratureError(string, out double)

Gets the I/Q quadrature error. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetIQQuadratureError(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsIQQuadratureError](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q quadrature error. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkimeanactivepower__string-out.html language=enus -->
## TOPIC 00060: GetUplinkIMeanActivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkimeanactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkimeanactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. SyntaxNamespace: NationalInstruments.R

### GetUplinkIMeanActivePower(string, out double)

Gets the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkIMeanActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkIMeanActivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkipeakinactivepower__string-out.html language=enus -->
## TOPIC 00061: GetUplinkIPeakInactivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkipeakinactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkipeakinactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dB

### GetUplinkIPeakInactivePower(string, out double)

Gets the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkIPeakInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkIPeakInactivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanactivepower__string-out.html language=enus -->
## TOPIC 00062: GetUplinkMeanActivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetU

### GetUplinkMeanActivePower(string, out double)

Gets the average power of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkMeanActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkMeanActivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanauxiliarypilotpower__string-out.html language=enus -->
## TOPIC 00063: GetUplinkMeanAuxiliaryPilotPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanauxiliarypilotpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanauxiliarypilotpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkMeanAuxiliaryPilotPower(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkMeanAux

### GetUplinkMeanAuxiliaryPilotPower(string, out double)

Gets the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkMeanAuxiliaryPilotPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkMeanAuxiliaryPilotPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeaninactivepower__string-out.html language=enus -->
## TOPIC 00064: GetUplinkMeanInactivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeaninactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeaninactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement ret

### GetUplinkMeanInactivePower(string, out double)

Gets the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkMeanInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkMeanInactivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanpilotpower__string-out.html language=enus -->
## TOPIC 00065: GetUplinkMeanPilotPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanpilotpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeanpilotpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkMeanPilotPower(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkMeanPilotPower attribute.Pa

### GetUplinkMeanPilotPower(string, out double)

Gets the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkMeanPilotPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkMeanPilotPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeansymbolpower__string-out.html language=enus -->
## TOPIC 00066: GetUplinkMeanSymbolPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeansymbolpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkmeansymbolpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkMeanSymbolPower(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkMeanSymbolPower att

### GetUplinkMeanSymbolPower(string, out double)

Gets the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkMeanSymbolPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkMeanSymbolPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeakactivepower__string-out.html language=enus -->
## TOPIC 00067: GetUplinkPeakActivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeakactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeakactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum power among all the active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic i

### GetUplinkPeakActivePower(string, out double)

Gets the maximum power among all the active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkPeakActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkPeakActivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum power among all the active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeakinactivepower__string-out.html language=enus -->
## TOPIC 00068: GetUplinkPeakInactivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeakinactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeakinactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement re

### GetUplinkPeakInactivePower(string, out double)

Gets the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkPeakInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkPeakInactivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeaksymbolevm__string-out.html language=enus -->
## TOPIC 00069: GetUplinkPeakSymbolEvm(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeaksymbolevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkpeaksymbolevm__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkPeakSymbolEvm(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkPeakSymbolEvm attrib

### GetUplinkPeakSymbolEvm(string, out double)

Gets the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkPeakSymbolEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkPeakSymbolEvm](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkqmeanactivepower__string-out.html language=enus -->
## TOPIC 00070: GetUplinkQMeanActivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkqmeanactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkqmeanactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. SyntaxNamespace: NationalInstruments.R

### GetUplinkQMeanActivePower(string, out double)

Gets the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkQMeanActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkQMeanActivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkqpeakinactivepower__string-out.html language=enus -->
## TOPIC 00071: GetUplinkQPeakInactivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkqpeakinactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkqpeakinactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm.The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise.

### GetUplinkQPeakInactivePower(string, out double)

Gets the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm.The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkQPeakInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkQPeakInactivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm.The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolevm__string-out.html language=enus -->
## TOPIC 00072: GetUplinkRmsSymbolEvm(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolevm__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkRmsSymbolEvm(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkRmsSymbolEvm attribute

### GetUplinkRmsSymbolEvm(string, out double)

Gets the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkRmsSymbolEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkRmsSymbolEvm](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolmagnitudeerror__string-out.html language=enus -->
## TOPIC 00073: GetUplinkRmsSymbolMagnitudeError(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolmagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolmagnitudeerror__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkRmsSymbolMagnitudeError(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplin

### GetUplinkRmsSymbolMagnitudeError(string, out double)

Gets the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkRmsSymbolMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkRmsSymbolMagnitudeError](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolphaseerror__string-out.html language=enus -->
## TOPIC 00074: GetUplinkRmsSymbolPhaseError(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinkrmssymbolphaseerror__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkRmsSymbolPhaseError(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkRmsSymbolPha

### GetUplinkRmsSymbolPhaseError(string, out double)

Gets the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkRmsSymbolPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkRmsSymbolPhaseError](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinktotalactivepower__string-out.html language=enus -->
## TOPIC 00075: GetUplinkTotalActivePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinktotalactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinktotalactivepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sum of the powers of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int

### GetUplinkTotalActivePower(string, out double)

Gets the sum of the powers of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkTotalActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkTotalActivePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the sum of the powers of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinktotalpower__string-out.html language=enus -->
## TOPIC 00076: GetUplinkTotalPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinktotalpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults-getuplinktotalpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean power of the received signal. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUplinkTotalPower(string selectorString, out double value)RemarksThis method gets the value of CdaResultsUplinkTotalPower attribute.ParametersNameTypeDescriptionse

### GetUplinkTotalPower(string, out double)

Gets the mean power of the received signal. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUplinkTotalPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsUplinkTotalPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean power of the received signal. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXCdaResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults.html language=enus -->
## TOPIC 00077: RFmxEvdoMXCdaResults Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaresults.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the CDA measurement results. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXCdaResults : RFmxEvdoMXSubObjectMethodsNameDescriptionFetchIQImpairments(string, double, out double, out double, out double)Fetches th

### RFmxEvdoMXCdaResults Class

Provides methods to fetch and read the CDA measurement results.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXCdaResults : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchIQImpairments(string, double, out double, out double, out double) | Fetches the measured I/Q impairments. |
| FetchUplinkCodeDomainIAndQPower(string, double, out double, out double, out double, out double) | Fetches the I and Q mean active powers and the I and Q peak inactive powers. |
| FetchUplinkCodeDomainIandQPowerTrace(string, double, ref float[], ref float[]) | Fetches the I and Q code power traces measured in the code domain of the base spreading factor. |
| FetchUplinkCodeDomainPower(string, double, out double, out double, out double, out double, out double, out double) | Fetches the scalar code domain power results. |
| FetchUplinkSymbolConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the symbol constellation trace of the configured measurement channel. |
| FetchUplinkSymbolEvm(string, double, out double, out double, out double, out double, out double, out double, out double) | Fetches the modulation accuracy related measures for the configured measurement channel. |
| FetchUplinkSymbolEvmTrace(string, double, ref float[]) | Returns the symbol EVM trace of the configured measurement channel. |
| FetchUplinkSymbolMagnitudeErrorTrace(string, double, ref float[]) | Returns the symbol magnitude error trace of the configured measurement channel. |
| FetchUplinkSymbolPhaseErrorTrace(string, double, ref float[]) | Fetches the symbol phase error trace of the configured measurement channel. |
| FetchUplinkSymbolPowerTrace(string, double, ref float[]) | Returns the symbol power trace of the configured measurement channel. |
| GetChipRateError(string, out double) | Gets the chip rate error. This value is expressed in ppm. |
| GetFrequencyError(string, out double) | Gets the frequency error. This value is expressed in Hz. |
| GetIQGainImbalance(string, out double) | Gets the I/Q gain imbalance. This value is expressed in dB. |
| GetIQOriginOffset(string, out double) | Gets the I/Q origin offset. This value is expressed in dB. |
| GetIQQuadratureError(string, out double) | Gets the I/Q quadrature error. This value is expressed in degrees. |
| GetUplinkIMeanActivePower(string, out double) | Gets the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkIPeakInactivePower(string, out double) | Gets the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkMeanActivePower(string, out double) | Gets the average power of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkMeanAuxiliaryPilotPower(string, out double) | Gets the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm. |
| GetUplinkMeanInactivePower(string, out double) | Gets the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkMeanPilotPower(string, out double) | Gets the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm. |
| GetUplinkMeanSymbolPower(string, out double) | Gets the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. |
| GetUplinkPeakActivePower(string, out double) | Gets the maximum power among all the active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkPeakInactivePower(string, out double) | Gets the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkPeakSymbolEvm(string, out double) | Gets the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| GetUplinkQMeanActivePower(string, out double) | Gets the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkQPeakInactivePower(string, out double) | Gets the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm.The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise. |
| GetUplinkRmsSymbolEvm(string, out double) | Gets the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| GetUplinkRmsSymbolMagnitudeError(string, out double) | Gets the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |
| GetUplinkRmsSymbolPhaseError(string, out double) | Gets the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |
| GetUplinkTotalActivePower(string, out double) | Gets the sum of the powers of all active code channels. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| GetUplinkTotalPower(string, out double) | Gets the mean power of the received signal. This value is expressed in dBm. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdaspectruminverted.html language=enus -->
## TOPIC 00078: RFmxEvdoMXCdaSpectrumInverted Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdaspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdaspectruminverted.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXCdaSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxEvdoMXCdaSpectrumInverted Enumeration

Specifies whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXCdaSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdasynchronizationmode.html language=enus -->
## TOPIC 00079: RFmxEvdoMXCdaSynchronizationMode Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdasynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdasynchronizationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame, slot, or symbol boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXCdaSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of sl

### RFmxEvdoMXCdaSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXCdaSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(string, int) method starting at SetMeasurementOffset(string, int) slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. |
| Arbitrary | 2 | The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length method, starting at CDA Meas Offset slots from the symbol boundary. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxcdauplinkbranch.html language=enus -->
## TOPIC 00080: RFmxEvdoMXCdaUplinkBranch Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxcdauplinkbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxcdauplinkbranch.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Walsh branch of the channel, subject to channel-specific analysis. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXCdaUplinkBranchMembersNameValueDescriptionI0Specifies the in-phase branch. Q1Specifies the quadrature branch. IAndQ2Specifies the in-phase and quadra

### RFmxEvdoMXCdaUplinkBranch Enumeration

Specifies the Walsh branch of the channel, subject to channel-specific analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXCdaUplinkBranch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| I | 0 | Specifies the in-phase branch. |
| Q | 1 | Specifies the quadrature branch. |
| IAndQ | 2 | Specifies the in-phase and quadrature branch. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html language=enus -->
## TOPIC 00081: RFmxEvdoMXChannelConfigurationMode Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to detect the channels automatically or to use a specified channel configuration. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXChannelConfigurationModeMembersNameValueDescriptionAutoDetect0Specifies that the system automatically detects the channels. UserDe

### RFmxEvdoMXChannelConfigurationMode Enumeration

Specifies whether to detect the channels automatically or to use a specified channel configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXChannelConfigurationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AutoDetect | 0 | Specifies that the system automatically detects the channels. |
| UserDefined | 1 | Specifies that the system uses a specific channel configuration. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchp-configuration.html language=enus -->
## TOPIC 00082: Configuration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchp-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchp-configuration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxEvdoMXChpConfiguration instance that provides methods to configure the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic RFmxEvdoMXChpConfiguration Configuration { get; }

### Configuration

Gets the [RFmxEvdoMXChpConfiguration](nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration.html) instance that provides methods to configure the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public [RFmxEvdoMXChpConfiguration](nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration.html) Configuration { get; }

Parent topic:

RFmxEvdoMXChp Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchp-results.html language=enus -->
## TOPIC 00083: Results

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchp-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchp-results.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxEvdoMXChpResults instance that provides methods to fetch and read the CHP measurement results. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic RFmxEvdoMXChpResults Results { get; }

### Results

Gets the [RFmxEvdoMXChpResults](nationalinstruments-rfmx-evdomx-rfmxevdomxchpresults.html) instance that provides methods to fetch and read the CHP measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public [RFmxEvdoMXChpResults](nationalinstruments-rfmx-evdomx-rfmxevdomxchpresults.html) Results { get; }

Parent topic:

RFmxEvdoMXChp Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchp.html language=enus -->
## TOPIC 00084: RFmxEvdoMXChp Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchp.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the CHP measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXChp : RFmxEvdoMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxEvdoMXChpConfiguration instance that provides methods to configure the CHP measurement. Re

### RFmxEvdoMXChp Class

Represents the CHP measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXChp : RFmxEvdoMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxEvdoMXChpConfiguration instance that provides methods to configure the CHP measurement. |
| Results | Gets the RFmxEvdoMXChpResults instance that provides methods to fetch and read the CHP measurement results. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingenabled.html language=enus -->
## TOPIC 00085: RFmxEvdoMXChpAveragingEnabled Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXChpAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The CHP measurement uses the Averaging C

### RFmxEvdoMXChpAveragingEnabled Enumeration

Specifies whether to enable averaging for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXChpAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The CHP measurement uses the Averaging Count method as the number of acquisitions over which the CHP measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingtype.html language=enus -->
## TOPIC 00086: RFmxEvdoMXChpAveragingType Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingtype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXChpAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averag

### RFmxEvdoMXChpAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXChpAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configureaveraging__string-rfmxevdomxchpaveragingenabled-int-rfmxevdomxchpaveragingtype.html language=enus -->
## TOPIC 00087: ConfigureAveraging(string, RFmxEvdoMXChpAveragingEnabled, int, RFmxEvdoMXChpAveragingType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configureaveraging__string-rfmxevdomxchpaveragingenabled-int-rfmxevdomxchpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configureaveraging__string-rfmxevdomxchpaveragingenabled-int-rfmxevdomxchpaveragingtype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the channel power (CHP) measurement.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureAveraging(string selectorString, RFmxEvdoMXChpAveragingEnabled averagingEnabled, int averagingCount, RFmxEvdoMXChpAveragingType averagingType)ParametersNameTypeDescription

### ConfigureAveraging(string, RFmxEvdoMXChpAveragingEnabled, int, RFmxEvdoMXChpAveragingType)

Configures averaging for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureAveraging(string selectorString, RFmxEvdoMXChpAveragingEnabled averagingEnabled, int averagingCount, RFmxEvdoMXChpAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxEvdoMXChpAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxEvdoMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configurerbwfilter__string-rfmxevdomxchprbwautobandwidth-double-rfmxevdomxchprbwfiltertype.html language=enus -->
## TOPIC 00088: ConfigureRbwFilter(string, RFmxEvdoMXChpRbwAutoBandwidth, double, RFmxEvdoMXChpRbwFilterType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configurerbwfilter__string-rfmxevdomxchprbwautobandwidth-double-rfmxevdomxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configurerbwfilter__string-rfmxevdomxchprbwautobandwidth-double-rfmxevdomxchprbwfiltertype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureRbwFilter(string selectorString, RFmxEvdoMXChpRbwAutoBandwidth rbwAuto, double rbw, RFmxEvdoMXChpRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an e

### ConfigureRbwFilter(string, RFmxEvdoMXChpRbwAutoBandwidth, double, RFmxEvdoMXChpRbwFilterType)

Configures the resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureRbwFilter(string selectorString, RFmxEvdoMXChpRbwAutoBandwidth rbwAuto, double rbw, RFmxEvdoMXChpRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxEvdoMXChpRbwAutoBandwidth | Specifies whether the measurement calculates the RBW. |
| rbw | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxEvdoMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configuresweeptime__string-rfmxevdomxchpsweeptimeauto-double.html language=enus -->
## TOPIC 00089: ConfigureSweepTime(string, RFmxEvdoMXChpSweepTimeAuto, double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configuresweeptime__string-rfmxevdomxchpsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-configuresweeptime__string-rfmxevdomxchpsweeptimeauto-double.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureSweepTime(string selectorString, RFmxEvdoMXChpSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when

### ConfigureSweepTime(string, RFmxEvdoMXChpSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureSweepTime(string selectorString, RFmxEvdoMXChpSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxEvdoMXChpSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00090: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of ChpAllTracesEnabled attribute.T

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ChpAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00091: GetAveragingCount(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXChpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of ChpAve

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxEvdoMXChpAveragingEnabled)](nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-setaveragingenabled__string-rfmxevdomxchpaveragingenabled.html) method to [True](nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [ChpAveragingCount](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXChpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00092: GetAveragingEnabled(string, out RFmxEvdoMXChpAveragingEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetAveragingEnabled(string selectorString, out RFmxEvdoMXChpAveragingEnabled value)RemarksThis method gets the value of ChpAveragingEnabled attribute.The default value

### GetAveragingEnabled(string, out RFmxEvdoMXChpAveragingEnabled)

Gets whether to enable averaging for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetAveragingEnabled(string selectorString, out RFmxEvdoMXChpAveragingEnabled value)

#### Remarks

This method gets the value of [ChpAveragingEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXChpAveragingEnabled | Upon return, contains whether to enable averaging for the channel power (CHP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00093: GetAveragingType(string, out RFmxEvdoMXChpAveragingType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetAveragingType(string selectorString, out RFmxEvdoMXChpAveragingType value)RemarksThis method gets

### GetAveragingType(string, out RFmxEvdoMXChpAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetAveragingType(string selectorString, out RFmxEvdoMXChpAveragingType value)

#### Remarks

This method gets the value of [ChpAveragingType](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-evdomx-rfmxevdomxchpaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXChpAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00094: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CHP carrier integration bandwidth. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of ChpCarrierIntegrationBandwidth attribute.ParametersNameTyp

### GetCarrierIntegrationBandwidth(string, out double)

Gets the CHP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpCarrierIntegrationBandwidth](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the CHP carrier integration bandwidth. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00095: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of ChpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescrip

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ChpMeasurementEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the channel power (CHP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00096: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the channel power (CHP) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of ChpNumberOfAnalysisThreads attribute.The de

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the channel power (CHP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [ChpNumberOfAnalysisThreads](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the channel power (CHP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00097: GetRbwFilterAutoBandwidth(string, out RFmxEvdoMXChpRbwAutoBandwidth)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getrbwfilterautobandwidth__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetRbwFilterAutoBandwidth(string selectorString, out RFmxEvdoMXChpRbwAutoBandwidth value)RemarksThis method gets the value of ChpRbwFilterAutoBandwidth attribute.The default value is True.Parame

### GetRbwFilterAutoBandwidth(string, out RFmxEvdoMXChpRbwAutoBandwidth)

Gets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetRbwFilterAutoBandwidth(string selectorString, out RFmxEvdoMXChpRbwAutoBandwidth value)

#### Remarks

This method gets the value of [ChpRbwFilterAutoBandwidth](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-evdomx-rfmxevdomxchprbwautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXChpRbwAutoBandwidth | Upon return, contains whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00098: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxEvdoMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetRbwFilterBandwidth(string selectorS

### GetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxEvdoMXChpRbwAutoBandwidth)](nationalinstruments-rfmx-evdomx-rfmxevdomxchpconfiguration-setrbwfilterautobandwidth__string-rfmxevdomxchprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-evdomx-rfmxevdomxchprbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpRbwFilterBandwidth](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 30 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxEvdoMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi0.html language=enus -->
## TOPIC 00099: DioPfi0

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi0.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi0

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi1.html language=enus -->
## TOPIC 00100: DioPfi1

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi1.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi1

### DioPfi1

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi1

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi2.html language=enus -->
## TOPIC 00101: DioPfi2

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi2.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi2

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi3.html language=enus -->
## TOPIC 00102: DioPfi3

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi3.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi3

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi4.html language=enus -->
## TOPIC 00103: DioPfi4

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi4.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi4

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi5.html language=enus -->
## TOPIC 00104: DioPfi5

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi5.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi5

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi6.html language=enus -->
## TOPIC 00105: DioPfi6

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi6.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi6

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi7.html language=enus -->
## TOPIC 00106: DioPfi7

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-diopfi7.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string DioPfi7

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-pulsein.html language=enus -->
## TOPIC 00107: PulseIn

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxconstants-pulsein.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public const string PulseIn

Parent topic:

RFmxEvdoMXConstants Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00108: RFmxEvdoMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxdigitaledgetriggeredge.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asserts

### RFmxEvdoMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxEvdoMXTriggerType)](nationalinstruments-rfmx-evdomx-rfmxevdomx-settriggertype__string-rfmxevdomxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodacc.html language=enus -->
## TOPIC 00109: RFmxEvdoMXModAcc Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodacc.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ModAcc measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXModAcc : RFmxEvdoMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxEvdoMXModAccConfiguration instance that provides methods to configure the ModAcc mea

### RFmxEvdoMXModAcc Class

Represents the ModAcc measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXModAcc : RFmxEvdoMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxEvdoMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
| Results | Gets the RFmxEvdoMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00110: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of ModAccAllTracesEnabled attribute.The default val

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ModAccAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setiqoffsetremovalenabled__string-rfmxevdomxmodacciqoffsetremovalenabled.html language=enus -->
## TOPIC 00111: SetIQOffsetRemovalEnabled(string, RFmxEvdoMXModAccIQOffsetRemovalEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setiqoffsetremovalenabled__string-rfmxevdomxmodacciqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setiqoffsetremovalenabled__string-rfmxevdomxmodacciqoffsetremovalenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q offset before the EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetIQOffsetRemovalEnabled(string selectorString, RFmxEvdoMXModAccIQOffsetRemovalEnabled value)RemarksThis method sets the value of ModAccIQOffsetRemovalEnabled attribute.The d

### SetIQOffsetRemovalEnabled(string, RFmxEvdoMXModAccIQOffsetRemovalEnabled)

Sets whether to remove the I/Q offset before the EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetIQOffsetRemovalEnabled(string selectorString, RFmxEvdoMXModAccIQOffsetRemovalEnabled value)

#### Remarks

This method sets the value of [ModAccIQOffsetRemovalEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxmodacciqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the EVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setiqquadratureerrorremovalenabled__string-rfmxevdomxmodacciqquadratureerrorremovalenabled.html language=enus -->
## TOPIC 00112: SetIQQuadratureErrorRemovalEnabled(string, RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setiqquadratureerrorremovalenabled__string-rfmxevdomxmodacciqquadratureerrorremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration-setiqquadratureerrorremovalenabled__string-rfmxevdomxmodacciqquadratureerrorremovalenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q quadrature error before the EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetIQQuadratureErrorRemovalEnabled(string selectorString, RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled value)RemarksThis method sets the value of ModAccIQQuadratu

### SetIQQuadratureErrorRemovalEnabled(string, RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled)

Sets whether to remove the I/Q quadrature error before the EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetIQQuadratureErrorRemovalEnabled(string selectorString, RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled value)

#### Remarks

This method sets the value of [ModAccIQQuadratureErrorRemovalEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxmodacciqquadratureerrorremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the EVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration.html language=enus -->
## TOPIC 00113: RFmxEvdoMXModAccConfiguration Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccconfiguration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ModAcc measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXModAccConfiguration : RFmxEvdoMXSubObjectMethodsNameDescriptionConfigureMultiCarrierFilterEnabled(string, RFmxEvdoMXModAccMultiCarrierFilterEnab

### RFmxEvdoMXModAccConfiguration Class

Provides methods to configure the ModAcc measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXModAccConfiguration : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureMultiCarrierFilterEnabled(string, RFmxEvdoMXModAccMultiCarrierFilterEnabled) | Enables or disables the multicarrier filter. In multicarrier setups, EVM values are higher than in single carrier setups. The multicarrier filter attempts to minimize interferences from neighboring carriers by applying sharp edges. To save time, do not use this filter in single-carrier setups. |
| ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXModAccSynchronizationMode, int, int) | Configures how the modulation accuracy (ModAcc) measurement synchronizes to the signal and the synchronization interval length. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
| GetIQGainImbalanceRemovalEnabled(string, out RFmxEvdoMXModAccIQGainImbalanceRemovalEnabled) | Gets whether to remove the I/Q gain imbalance before the EVM measurement. |
| GetIQOffsetRemovalEnabled(string, out RFmxEvdoMXModAccIQOffsetRemovalEnabled) | Gets whether to remove the I/Q offset before the EVM measurement. |
| GetIQQuadratureErrorRemovalEnabled(string, out RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled) | Gets whether to remove the I/Q quadrature error before the EVM measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the ModAcc measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of the modulation accuracy measurement. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXModAccSynchronizationMode) method. |
| GetMultiCarrierFilterEnabled(string, out RFmxEvdoMXModAccMultiCarrierFilterEnabled) | Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers. |
| GetReceiveFilterEnabled(string, out RFmxEvdoMXModAccReceiveFilterEnabled) | Gets whether to enable receive filtering. |
| GetSpectrumInverted(string, out RFmxEvdoMXModAccSpectrumInverted) | Gets whether the measured spectrum is inverted. |
| GetSynchronizationMode(string, out RFmxEvdoMXModAccSynchronizationMode) | Gets whether the measurement is performed from frame, slot, or symbol boundary. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
| SetIQGainImbalanceRemovalEnabled(string, RFmxEvdoMXModAccIQGainImbalanceRemovalEnabled) | Sets whether to remove the I/Q gain imbalance before the EVM measurement. |
| SetIQOffsetRemovalEnabled(string, RFmxEvdoMXModAccIQOffsetRemovalEnabled) | Sets whether to remove the I/Q offset before the EVM measurement. |
| SetIQQuadratureErrorRemovalEnabled(string, RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled) | Sets whether to remove the I/Q quadrature error before the EVM measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the ModAcc measurement. |
| SetMeasurementLength(string, int) | Sets the duration of the modulation accuracy measurement. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXModAccSynchronizationMode) method. |
| SetMultiCarrierFilterEnabled(string, RFmxEvdoMXModAccMultiCarrierFilterEnabled) | Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers. |
| SetReceiveFilterEnabled(string, RFmxEvdoMXModAccReceiveFilterEnabled) | Sets whether to enable receive filtering. |
| SetSpectrumInverted(string, RFmxEvdoMXModAccSpectrumInverted) | Sets whether the measured spectrum is inverted. |
| SetSynchronizationMode(string, RFmxEvdoMXModAccSynchronizationMode) | Sets whether the measurement is performed from frame, slot, or symbol boundary. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccreceivefilterenabled.html language=enus -->
## TOPIC 00114: RFmxEvdoMXModAccReceiveFilterEnabled Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccreceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccreceivefilterenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXModAccReceiveFilterEnabledMembersNameValueDescriptionFalse0Receive filtering is disabled. True1Receive filtering is enabled.

### RFmxEvdoMXModAccReceiveFilterEnabled Enumeration

Specifies whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXModAccReceiveFilterEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Receive filtering is disabled. |
| True | 1 | Receive filtering is enabled. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccresults-fetchuplinkpeakactivecde__string-double-out-out-out-out.html language=enus -->
## TOPIC 00115: FetchUplinkPeakActiveCde(string, double, out double, out int, out int, out RFmxEvdoMXModAccUplinkPeakActiveCdeBranch)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccresults-fetchuplinkpeakactivecde__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxmodaccresults-fetchuplinkpeakactivecde__string-double-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUplinkPeakActiveCde(string selectorString, double timeout, out double uplinkPeakActiveCde, out int uplinkPeakActi

### FetchUplinkPeakActiveCde(string, double, out double, out int, out int, out RFmxEvdoMXModAccUplinkPeakActiveCdeBranch)

Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUplinkPeakActiveCde(string selectorString, double timeout, out double uplinkPeakActiveCde, out int uplinkPeakActiveCdeWalshCodeLength, out int uplinkPeakActiveCdeWalshCodeNumber, out RFmxEvdoMXModAccUplinkPeakActiveCdeBranch uplinkPeakActiveCdeBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| uplinkPeakActiveCde | out double | Upon return, contains the peak value of all CDEs of the active channels. This value is expressed in dB. |
| uplinkPeakActiveCdeWalshCodeLength | out int | Upon return, contains the Walsh code length of the channel corresponding to the uplinkPeakActiveCDE result. |
| uplinkPeakActiveCdeWalshCodeNumber | out int | Upon return, contains the Walsh code number of the channel corresponding to the uplinkPeakActiveCDE result. |
| uplinkPeakActiveCdeBranch | out RFmxEvdoMXModAccUplinkPeakActiveCdeBranch | Upon return, contains the branch of the channel corresponding to the Peak Active CDE (dB) result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXModAccResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxobwconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00116: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxobwconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxobwconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxEvdoMXObwSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of ObwS

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxEvdoMXObwSweepTimeAuto)](nationalinstruments-rfmx-evdomx-rfmxevdomxobwconfiguration-setsweeptimeauto__string-rfmxevdomxobwsweeptimeauto.html) method to [False](nationalinstruments-rfmx-evdomx-rfmxevdomxobwsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [ObwSweepTimeInterval](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.00167 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxEvdoMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxobwresults-getstopfrequency__string-out.html language=enus -->
## TOPIC 00117: GetStopFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxobwresults-getstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxobwresults-getstopfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of ObwResultsStopFrequency attribute.ParametersNameTypeDescrip

### GetStopFrequency(string, out double)

Gets the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsStopFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXObwResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingenabled.html language=enus -->
## TOPIC 00118: RFmxEvdoMXSemAveragingEnabled Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSemAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The SEM measurement uses the S

### RFmxEvdoMXSemAveragingEnabled Enumeration

Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSemAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The SEM measurement uses the SetAveragingCount(string, int) method as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingtype.html language=enus -->
## TOPIC 00119: RFmxEvdoMXSemAveragingType Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingtype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSemAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linea

### RFmxEvdoMXSemAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSemAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemcompositemeasurementstatus.html language=enus -->
## TOPIC 00120: RFmxEvdoMXSemCompositeMeasurementStatus Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemcompositemeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemcompositemeasurementstatus.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSemCompositeMeasurementStatusMembersNameValueDescriptionFail0The measurement fail

### RFmxEvdoMXSemCompositeMeasurementStatus Enumeration

Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSemCompositeMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The measurement fails. |
| Pass | 1 | The measurement passes. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-configureaveraging__string-rfmxevdomxsemaveragingenabled-int-rfmxevdomxsemaveragingtype.html language=enus -->
## TOPIC 00121: ConfigureAveraging(string, RFmxEvdoMXSemAveragingEnabled, int, RFmxEvdoMXSemAveragingType)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-configureaveraging__string-rfmxevdomxsemaveragingenabled-int-rfmxevdomxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-configureaveraging__string-rfmxevdomxsemaveragingenabled-int-rfmxevdomxsemaveragingtype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the spectral emission mask (SEM) measurement.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureAveraging(string selectorString, RFmxEvdoMXSemAveragingEnabled averagingEnabled, int averagingCount, RFmxEvdoMXSemAveragingType averagingType)ParametersNameTypeDe

### ConfigureAveraging(string, RFmxEvdoMXSemAveragingEnabled, int, RFmxEvdoMXSemAveragingType)

Configures averaging for the spectral emission mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureAveraging(string selectorString, RFmxEvdoMXSemAveragingEnabled averagingEnabled, int averagingCount, RFmxEvdoMXSemAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxEvdoMXSemAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxEvdoMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00122: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SemAllTracesEnabled attri

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SemAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00123: SetAveragingCount(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXSemAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of SemAveragi

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxEvdoMXSemAveragingEnabled)](nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration-setaveragingenabled__string-rfmxevdomxsemaveragingenabled.html) method to [True](nationalinstruments-rfmx-evdomx-rfmxevdomxsemaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [SemAveragingCount](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXSemAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration.html language=enus -->
## TOPIC 00124: RFmxEvdoMXSemConfiguration Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemconfiguration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SEM measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSemConfiguration : RFmxEvdoMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxEvdoMXSemAveragingEnabled, int, RFmxEvdoMXSemAveragingTy

### RFmxEvdoMXSemConfiguration Class

Provides methods to configure the SEM measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSemConfiguration : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxEvdoMXSemAveragingEnabled, int, RFmxEvdoMXSemAveragingType) | Configures averaging for the spectral emission mask (SEM) measurement. |
| ConfigureSweepTime(string, RFmxEvdoMXSemSweepTimeAuto, double) | Configures the sweep time. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXSemAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxEvdoMXSemAveragingEnabled) | Gets whether to enable averaging for the spectral emissions mask (SEM) measurement. |
| GetAveragingType(string, out RFmxEvdoMXSemAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. |
| GetCarrierIntegrationBandwidth(string, out double) | Gets the SEM carrier integration bandwidth. This value is expressed in Hz. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the spectral emissions mask (SEM) measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the spectral emissions mask (SEM) measurement. |
| GetNumberOfOffsets(string, out int) | Gets the number of SEM offset segments. |
| GetOffsetBandwidthIntegral(string, out int) | Gets the bandwidth integral for a specific offset segment. |
| GetOffsetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. |
| GetOffsetRbwFilterType(string, out RFmxEvdoMXSemOffsetRbwFilterType) | Gets the type of RBW filter used to sweep the offset segment. |
| GetOffsetStartFrequency(string, out double) | Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| GetOffsetStopFrequency(string, out double) | Gets the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| GetSweepTimeAuto(string, out RFmxEvdoMXSemSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxEvdoMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxEvdoMXSemAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxEvdoMXSemAveragingEnabled) | Sets whether to enable averaging for the spectral emissions mask (SEM) measurement. |
| SetAveragingType(string, RFmxEvdoMXSemAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the spectral emissions mask (SEM) measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the spectral emissions mask (SEM) measurement. |
| SetSweepTimeAuto(string, RFmxEvdoMXSemSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxEvdoMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemloweroffsetmeasurementstatus.html language=enus -->
## TOPIC 00125: RFmxEvdoMXSemLowerOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemloweroffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemloweroffsetmeasurementstatus.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSemLowerOffsetMeasurementSt

### RFmxEvdoMXSemLowerOffsetMeasurementStatus Enumeration

Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSemLowerOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The measurement fails. |
| Pass | 1 | The measurement passes. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00126: FetchLowerOffsetMargin(string, double, out RFmxEvdoMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchLowerOffsetMargin(string selectorString, double timeout, out

### FetchLowerOffsetMargin(string, double, out RFmxEvdoMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double)

Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchLowerOffsetMargin(string selectorString, double timeout, out RFmxEvdoMXSemLowerOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxEvdoMXSemLowerOffsetMeasurementStatus | Indicates the lower offset measurement status. |
| margin | out double | Upon return, contains the margin. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | out double | Upon return, contains the frequency at which the margin occurred in the lower (negative) offset. This value is expressed in Hz. |
| marginAbsolutePower | out double | Upon return, contains the power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | out double | Upon return, contains the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00127: FetchLowerOffsetMarginArray(string, double, ref RFmxEvdoMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchLowerOffsetMarginArray(string selectorString, double timeout, ref RFmxEvdoMXSemLowerOffsetMeasurementStatus[] measurementSta

### FetchLowerOffsetMarginArray(string, double, ref RFmxEvdoMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchLowerOffsetMarginArray(string selectorString, double timeout, ref RFmxEvdoMXSemLowerOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxEvdoMXSemLowerOffsetMeasurementStatus[] | Upon return, contains the array of lower offset measurement statuses. |
| margin | ref double[] | Upon return, contains the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | ref double[] | Upon return, contains the array of frequencies at which the margin occurred in each lower (negative) offset segment. This value is expressed in Hz. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00128: FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchLowerOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relat

### FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

Returns the lower offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchLowerOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the lower (negative) offset segment power measured. This value is expressed in dBm. |
| relativeIntegratedPower | out double | Upon return, contains the power in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | out double | Upon return, contains the peak power measured in the lower (negative) offset segment. The power is measured in dBm. |
| peakFrequency | out double | Upon return, contains the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | out double | Upon return, contains the peak power in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00129: FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchLowerOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref d

### FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Returns the arrays of lower offset segment power measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchLowerOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref double[] peakFrequency, ref double[] relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | ref double[] | Upon return, contains the array of lower (negative) offset segment powers measured. This value is expressed in dBm. |
| relativeIntegratedPower | ref double[] | Upon return, contains the array of powers in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | ref double[] | Upon return, contains the array of peak powers measured in each lower (negative) offset segment. |
| peakFrequency | ref double[] | Upon return, contains the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | ref double[] | Upon return, contains the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchmeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00130: FetchMeasurementStatus(string, double, out RFmxEvdoMXSemCompositeMeasurementStatus)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchmeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchmeasurementstatus__string-double-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SEM measurement status.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchMeasurementStatus(string selectorString, double timeout, out RFmxEvdoMXSemCompositeMeasurementStatus measurementStatus)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string compr

### FetchMeasurementStatus(string, double, out RFmxEvdoMXSemCompositeMeasurementStatus)

Fetches the SEM measurement status.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchMeasurementStatus(string selectorString, double timeout, out RFmxEvdoMXSemCompositeMeasurementStatus measurementStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxEvdoMXSemCompositeMeasurementStatus | Upon return, contains the status of the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchspectrum__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00131: FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchspectrum__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchspectrum__string-double-ref-ref-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the spectral emission mask (SEM) measurement.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum, ref Spectrum< float > relativeMask, ref Spectrum< float > absoluteMask)Parameters

### FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >)

Fetches the spectrum used for the spectral emission mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum, ref Spectrum< float > relativeMask, ref Spectrum< float > absoluteMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| spectrum | ref Spectrum< float > | Upon return, contains the trace of power levels in the spectral domain. This value is expressed in dBm. |
| relativeMask | ref Spectrum< float > | Upon return, contains the trace of power levels representing the relative mask in the spectral domain. |
| absoluteMask | ref Spectrum< float > | Upon return, contains the trace of power levels representing the absolute mask in the spectral domain. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchtotalcarrierpower__string-double-out.html language=enus -->
## TOPIC 00132: FetchTotalCarrierPower(string, double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchtotalcarrierpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchtotalcarrierpower__string-double-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total carrier power of the selected carrier.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchTotalCarrierPower(string selectorString, double timeout, out double totalCarrierPower)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the

### FetchTotalCarrierPower(string, double, out double)

Returns the total carrier power of the selected carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchTotalCarrierPower(string selectorString, double timeout, out double totalCarrierPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalCarrierPower | out double | Upon return, contains the total carrier power of the selected carrier. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00133: FetchUpperOffsetMargin(string, double, out RFmxEvdoMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUpperOffsetMargin(string selectorString, double timeout, out

### FetchUpperOffsetMargin(string, double, out RFmxEvdoMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUpperOffsetMargin(string selectorString, double timeout, out RFmxEvdoMXSemUpperOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxEvdoMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status. |
| margin | out double | Upon return, contains the margin from the limit mask value. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | out double | Upon return, contains the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00134: FetchUpperOffsetMarginArray(string, double, ref RFmxEvdoMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxEvdoMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref dou

### FetchUpperOffsetMarginArray(string, double, ref RFmxEvdoMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxEvdoMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxEvdoMXSemUpperOffsetMeasurementStatus[] | Upon return, contains the array of upper offset measurement statuses. |
| margin | ref double[] | Upon return, contains the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | ref double[] | Upon return, contains the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00135: FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUpperOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relat

### FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

Returns the upper offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUpperOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the upper (positive) offset segment power measured. This value is expressed in dBm. |
| relativeIntegratedPower | out double | Upon return, contains the power in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | out double | Upon return, contains the peak power measured in the upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | out double | Upon return, contains the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00136: FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of upper offset segment power measurements.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchUpperOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref d

### FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Returns the arrays of upper offset segment power measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchUpperOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref double[] peakFrequency, ref double[] relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | ref double[] | Upon return, contains the array of upper (positive) offset segment powers measured. This value is expressed in dBm. |
| relativeIntegratedPower | ref double[] | Upon return, contains the array of powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | ref double[] | Upon return, contains the array of peak powers measured in each upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | ref double[] | Upon return, contains the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | ref double[] | Upon return, contains the array of peak powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00137: GetCarrierAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierabsoluteintegratedpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute carrier power measurement. This value is expressed in dBm. Use "carrier(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierAbsoluteIntegratedPower(string selectorString, out double value)RemarksThis method gets the v

### GetCarrierAbsoluteIntegratedPower(string, out double)

Gets the absolute carrier power measurement. This value is expressed in dBm. Use "carrier(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierAbsoluteIntegratedPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute carrier power measurement. This value is expressed in dBm. Use "carrier(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00138: GetCarrierAbsolutePeakPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierabsolutepeakpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak absolute carrier power. This value is expressed in dBm. Use "carrier<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierAbsolutePeakPower(string selectorString, out double value)RemarksThis method gets the value

### GetCarrierAbsolutePeakPower(string, out double)

Gets the peak absolute carrier power. This value is expressed in dBm. Use "carrier<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierAbsolutePeakPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak absolute carrier power. This value is expressed in dBm. Use "carrier<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierpeakfrequency__string-out.html language=enus -->
## TOPIC 00139: GetCarrierPeakFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierpeakfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. Use "carrier(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierPeakFrequency(string selectorString, out double value)RemarksThis

### GetCarrierPeakFrequency(string, out double)

Gets the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. Use "carrier(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierPeakFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. Use "carrier(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00140: GetCarrierRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcarrierrelativeintegratedpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the relative carrier power measurement. This value is expressed in dB. Use "carrier(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCarrierRelativeIntegratedPower(string selectorString, out double value)RemarksThis method gets the va

### GetCarrierRelativeIntegratedPower(string, out double)

Gets the relative carrier power measurement. This value is expressed in dB. Use "carrier(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCarrierRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierRelativeIntegratedPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the relative carrier power measurement. This value is expressed in dB. Use "carrier(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcompositemeasurementstatus__string-out.html language=enus -->
## TOPIC 00141: GetCompositeMeasurementStatus(string, out RFmxEvdoMXSemCompositeMeasurementStatus)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcompositemeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getcompositemeasurementstatus__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetCompositeMeasurementStatus(string selectorString, out RFmxEvdoMXSemCompositeMeasurementSt

### GetCompositeMeasurementStatus(string, out RFmxEvdoMXSemCompositeMeasurementStatus)

Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetCompositeMeasurementStatus(string selectorString, out RFmxEvdoMXSemCompositeMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsCompositeMeasurementStatus](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxEvdoMXSemCompositeMeasurementStatus | Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00142: GetLowerOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out do

### GetLowerOffsetAbsoluteIntegratedPower(string, out double)

Gets the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00143: GetLowerOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetabsolutepeakpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetAbsolutePeakPower(string selectorString, out dou

### GetLowerOffsetAbsolutePeakPower(string, out double)

Gets the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsolutePeakPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmargin__string-out.html language=enus -->
## TOPIC 00144: GetLowerOffsetMargin(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmargin__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetMargin(string selectorString, out double value)RemarksThis

### GetLowerOffsetMargin(string, out double)

Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMargin](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00145: GetLowerOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginabsolutepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetMarginAbsolutePower(string select

### GetLowerOffsetMarginAbsolutePower(string, out double)

Gets the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginAbsolutePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginfrequency__string-out.html language=enus -->
## TOPIC 00146: GetLowerOffsetMarginFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetMarginFrequency(string selectorString,

### GetLowerOffsetMarginFrequency(string, out double)

Gets the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetMarginFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00147: GetLowerOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmarginrelativepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int

### GetLowerOffsetMarginRelativePower(string, out double)

Gets the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginRelativePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00148: GetLowerOffsetMeasurementStatus(string, out RFmxEvdoMXSemLowerOffsetMeasurementStatus)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetmeasurementstatus__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetMeasurementStatus(string

### GetLowerOffsetMeasurementStatus(string, out RFmxEvdoMXSemLowerOffsetMeasurementStatus)

Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxEvdoMXSemLowerOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMeasurementStatus](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxEvdoMXSemLowerOffsetMeasurementStatus | Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00149: GetLowerOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetpeakfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetPeakFrequency(string selectorString, out doubl

### GetLowerOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetPeakFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00150: GetLowerOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffsetRelativeIntegratedPower(string selec

### GetLowerOffsetRelativeIntegratedPower(string, out double)

Gets the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativeIntegratedPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00151: GetLowerOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getloweroffsetrelativepeakpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetLowerOffset

### GetLowerOffsetRelativePeakPower(string, out double)

Gets the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetLowerOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativePeakPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-gettotalcarrierpower__string-out.html language=enus -->
## TOPIC 00152: GetTotalCarrierPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-gettotalcarrierpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-gettotalcarrierpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total carrier power of the selected carrier. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetTotalCarrierPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsTotalCarrierPower attribute.ParametersNameTypeD

### GetTotalCarrierPower(string, out double)

Gets the total carrier power of the selected carrier. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetTotalCarrierPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsTotalCarrierPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the total carrier power of the selected carrier. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00153: GetUpperOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double valu

### GetUpperOffsetAbsoluteIntegratedPower(string, out double)

Gets the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00154: GetUpperOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetabsolutepeakpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetAbsolutePeakPower(string selectorString, out dou

### GetUpperOffsetAbsolutePeakPower(string, out double)

Gets the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsolutePeakPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmargin__string-out.html language=enus -->
## TOPIC 00155: GetUpperOffsetMargin(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmargin__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetMargin(string selectorString, out double value)RemarksThis

### GetUpperOffsetMargin(string, out double)

Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMargin](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00156: GetUpperOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginabsolutepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic i

### GetUpperOffsetMarginAbsolutePower(string, out double)

Gets the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginAbsolutePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginfrequency__string-out.html language=enus -->
## TOPIC 00157: GetUpperOffsetMarginFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetMarginFrequency(string selectorString, out doub

### GetUpperOffsetMarginFrequency(string, out double)

Gets the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetMarginFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00158: GetUpperOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmarginrelativepower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int

### GetUpperOffsetMarginRelativePower(string, out double)

Gets the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginRelativePower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00159: GetUpperOffsetMeasurementStatus(string, out RFmxEvdoMXSemUpperOffsetMeasurementStatus)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetmeasurementstatus__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetMeasurementStatus(string selecto

### GetUpperOffsetMeasurementStatus(string, out RFmxEvdoMXSemUpperOffsetMeasurementStatus)

Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetMeasurementStatus(string selectorString, out RFmxEvdoMXSemUpperOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMeasurementStatus](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxEvdoMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00160: GetUpperOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetpeakfrequency__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetPeakFrequency(string selectorString, out doubl

### GetUpperOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetPeakFrequency](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00161: GetUpperOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffsetRelativeIntegr

### GetUpperOffsetRelativeIntegratedPower(string, out double)

Gets the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativeIntegratedPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00162: GetUpperOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults-getupperoffsetrelativepeakpower__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetUpperOffset

### GetUpperOffsetRelativePeakPower(string, out double)

Gets the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetUpperOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativePeakPower](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSemResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults.html language=enus -->
## TOPIC 00163: RFmxEvdoMXSemResults Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemresults.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SEM measurement results. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSemResults : RFmxEvdoMXSubObjectMethodsNameDescriptionFetchCarrierMeasurement(string, double, out double, out double)Returns the carri

### RFmxEvdoMXSemResults Class

Provides methods to fetch and read the SEM measurement results.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSemResults : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchCarrierMeasurement(string, double, out double, out double) | Returns the carrier measurements for the carrier selected by the selector string. Use "carrier(n)" as the selector string to read parameters from this method. |
| FetchCarrierMeasurementArray(string, double, ref double[], ref double[]) | Returns the array of carrier measurements. |
| FetchLowerOffsetMargin(string, double, out RFmxEvdoMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchLowerOffsetMarginArray(string, double, ref RFmxEvdoMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments. |
| FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the lower offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns the arrays of lower offset segment power measurements. |
| FetchMeasurementStatus(string, double, out RFmxEvdoMXSemCompositeMeasurementStatus) | Fetches the SEM measurement status. |
| FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >) | Fetches the spectrum used for the spectral emission mask (SEM) measurement. |
| FetchTotalCarrierPower(string, double, out double) | Returns the total carrier power of the selected carrier. |
| FetchUpperOffsetMargin(string, double, out RFmxEvdoMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchUpperOffsetMarginArray(string, double, ref RFmxEvdoMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns the measurement status and margin from the limit line measured in the upper offset segments. |
| FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the upper offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method. |
| FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns the arrays of upper offset segment power measurements. |
| GetCarrierAbsoluteIntegratedPower(string, out double) | Gets the absolute carrier power measurement. This value is expressed in dBm. Use "carrier(n)" as the selector string to read this result. |
| GetCarrierAbsolutePeakPower(string, out double) | Gets the peak absolute carrier power. This value is expressed in dBm. Use "carrier<em>(n)</em>" as the selector string to read this method. |
| GetCarrierPeakFrequency(string, out double) | Gets the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. Use "carrier(n)" as the selector string to read this result. |
| GetCarrierRelativeIntegratedPower(string, out double) | Gets the relative carrier power measurement. This value is expressed in dB. Use "carrier(n)" as the selector string to read this result. |
| GetCompositeMeasurementStatus(string, out RFmxEvdoMXSemCompositeMeasurementStatus) | Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. |
| GetLowerOffsetAbsoluteIntegratedPower(string, out double) | Gets the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetAbsolutePeakPower(string, out double) | Gets the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetMargin(string, out double) | Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetMarginAbsolutePower(string, out double) | Gets the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetMarginFrequency(string, out double) | Gets the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetMarginRelativePower(string, out double) | Gets the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetMeasurementStatus(string, out RFmxEvdoMXSemLowerOffsetMeasurementStatus) | Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetRelativeIntegratedPower(string, out double) | Gets the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetLowerOffsetRelativePeakPower(string, out double) | Gets the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetTotalCarrierPower(string, out double) | Gets the total carrier power of the selected carrier. This value is expressed in dBm. |
| GetUpperOffsetAbsoluteIntegratedPower(string, out double) | Gets the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result. |
| GetUpperOffsetAbsolutePeakPower(string, out double) | Gets the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetMargin(string, out double) | Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetMarginAbsolutePower(string, out double) | Gets the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetMarginFrequency(string, out double) | Gets the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetMarginRelativePower(string, out double) | Gets the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetMeasurementStatus(string, out RFmxEvdoMXSemUpperOffsetMeasurementStatus) | Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<em>(n)</em>" as the selector string to read this method. |
| GetUpperOffsetRelativeIntegratedPower(string, out double) | Gets the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this result. |
| GetUpperOffsetRelativePeakPower(string, out double) | Gets the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<em>(n)</em>" as the selector string to read this method. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemsweeptimeauto.html language=enus -->
## TOPIC 00164: RFmxEvdoMXSemSweepTimeAuto Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemsweeptimeauto.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSemSweepTimeAutoMembersNameValueDescriptionTrue1The measurement calculates the sweep time using a default value. False0The measurement uses the default sweep time of 1.67

### RFmxEvdoMXSemSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSemSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| True | 1 | The measurement calculates the sweep time using a default value. |
| False | 0 | The measurement uses the default sweep time of 1.67 ms. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsemupperoffsetmeasurementstatus.html language=enus -->
## TOPIC 00165: RFmxEvdoMXSemUpperOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsemupperoffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsemupperoffsetmeasurementstatus.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSemUpperOffsetMeasurementStatusMemb

### RFmxEvdoMXSemUpperOffsetMeasurementStatus Enumeration

Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSemUpperOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The measurement fails. |
| Pass | 1 | The measurement passes. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase-configuration.html language=enus -->
## TOPIC 00166: Configuration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase-configuration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxEvdoMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic RFmxEvdoMXSlotPhaseConfiguration Configuration { get; }

### Configuration

Gets the [RFmxEvdoMXSlotPhaseConfiguration](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration.html) instance that provides methods to configure the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public [RFmxEvdoMXSlotPhaseConfiguration](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration.html) Configuration { get; }

Parent topic:

RFmxEvdoMXSlotPhase Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase-results.html language=enus -->
## TOPIC 00167: Results

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase-results.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxEvdoMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic RFmxEvdoMXSlotPhaseResults Results { get; }

### Results

Gets the [RFmxEvdoMXSlotPhaseResults](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults.html) instance that provides methods to fetch and read the SlotPhase measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public [RFmxEvdoMXSlotPhaseResults](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults.html) Results { get; }

Parent topic:

RFmxEvdoMXSlotPhase Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase.html language=enus -->
## TOPIC 00168: RFmxEvdoMXSlotPhase Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphase.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SlotPhase measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSlotPhase : RFmxEvdoMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxEvdoMXSlotPhaseConfiguration instance that provides methods to configure the S

### RFmxEvdoMXSlotPhase Class

Represents the SlotPhase measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSlotPhase : RFmxEvdoMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxEvdoMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. |
| Results | Gets the RFmxEvdoMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxevdomxslotphasesynchronizationmode-int-int.html language=enus -->
## TOPIC 00169: ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPhaseSynchronizationMode, int, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxevdomxslotphasesynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxevdomxslotphasesynchronizationmode-int-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxEvdoMXSlotPhaseSynchronizationMode synchronizationMode, int measurementOffset, int measurement

### ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPhaseSynchronizationMode, int, int)

Configures the synchronization mode, measurement offset, and measurement length.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxEvdoMXSlotPhaseSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxEvdoMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Mode method. |
| measurementLength | int | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00170: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseAllTracesEnabled attribute.The default value is FALSE.Param

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00171: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescription

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00172: GetMeasurementLength(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPhaseMeasurementLength attribute.The default value is 16.Par

### GetMeasurementLength(string, out int)

Gets the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00173: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)property. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeas

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setsynchronizationmode__string-rfmxevdomxslotphasesynchronizationmode.html)property.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)property. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getreceivefilterenabled__string-out.html language=enus -->
## TOPIC 00174: GetReceiveFilterEnabled(string, out RFmxEvdoMXSlotPhaseReceiveFilterEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getreceivefilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getreceivefilterenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetReceiveFilterEnabled(string selectorString, out RFmxEvdoMXSlotPhaseReceiveFilterEnabled value)RemarksThis method gets the value of SlotPhaseReceiveFilterEnabled attribute.The default value is True

### GetReceiveFilterEnabled(string, out RFmxEvdoMXSlotPhaseReceiveFilterEnabled)

Gets whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetReceiveFilterEnabled(string selectorString, out RFmxEvdoMXSlotPhaseReceiveFilterEnabled value)

#### Remarks

This method gets the value of [SlotPhaseReceiveFilterEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasereceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXSlotPhaseReceiveFilterEnabled | Upon return, contains whether to enable receive filtering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00175: GetSpectrumInverted(string, out RFmxEvdoMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetSpectrumInverted(string selectorString, out RFmxEvdoMXSlotPhaseSpectrumInverted value)RemarksThis method gets the value of SlotPhaseSpectrumInverted attribute.The default value is False.Parame

### GetSpectrumInverted(string, out RFmxEvdoMXSlotPhaseSpectrumInverted)

Gets whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSpectrumInverted(string selectorString, out RFmxEvdoMXSlotPhaseSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXSlotPhaseSpectrumInverted | Upon return, contains whether the signal spectrum is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getsynchronizationmode__string-out.html language=enus -->
## TOPIC 00176: GetSynchronizationMode(string, out RFmxEvdoMXSlotPhaseSynchronizationMode)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getsynchronizationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-getsynchronizationmode__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetSynchronizationMode(string selectorString, out RFmxEvdoMXSlotPhaseSynchronizationMode value)RemarksThis method gets the value of SlotPhaseSynchronizationMode a

### GetSynchronizationMode(string, out RFmxEvdoMXSlotPhaseSynchronizationMode)

Gets whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSynchronizationMode(string selectorString, out RFmxEvdoMXSlotPhaseSynchronizationMode value)

#### Remarks

This method gets the value of [SlotPhaseSynchronizationMode](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasesynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXSlotPhaseSynchronizationMode | Upon return, contains whether the measurement is performed from the frame or the slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-gettransientduration__string-out.html language=enus -->
## TOPIC 00177: GetTransientDuration(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-gettransientduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-gettransientduration__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the transient duration for the SlotPhase measurement. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetTransientDuration(string selectorString, out double value)RemarksThis method gets the value of SlotPhaseTransientDuration attribute.The transie

### GetTransientDuration(string, out double)

Gets the transient duration for the SlotPhase measurement. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetTransientDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [SlotPhaseTransientDuration](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The transient duration is applied equally on either side of a half-slot boundary, that is, at the start and end of each half-slot.Setting the transient duation equal to zero means that no transient period is considered, and the entire half-slot data is used to determine the phase error best-fit line used to compute the phase discontinuity at the half-slot boundaries. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the transient duration for the SlotPhase measurement. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00178: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPhaseAllTracesEnabled attribute.The default value is FALSE.Parameter

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00179: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPhaseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionsele

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00180: SetMeasurementLength(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of SlotPhaseMeasurementLength attribute.The default value is 16.Paramet

### SetMeasurementLength(string, int)

Sets the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00181: SetMeasurementOffset(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)property. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeas

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setsynchronizationmode__string-rfmxevdomxslotphasesynchronizationmode.html)property.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)property. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setreceivefilterenabled__string-rfmxevdomxslotphasereceivefilterenabled.html language=enus -->
## TOPIC 00182: SetReceiveFilterEnabled(string, RFmxEvdoMXSlotPhaseReceiveFilterEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setreceivefilterenabled__string-rfmxevdomxslotphasereceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setreceivefilterenabled__string-rfmxevdomxslotphasereceivefilterenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetReceiveFilterEnabled(string selectorString, RFmxEvdoMXSlotPhaseReceiveFilterEnabled value)RemarksThis method sets the value of SlotPhaseReceiveFilterEnabled attribute.The default value is True.Par

### SetReceiveFilterEnabled(string, RFmxEvdoMXSlotPhaseReceiveFilterEnabled)

Sets whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetReceiveFilterEnabled(string selectorString, RFmxEvdoMXSlotPhaseReceiveFilterEnabled value)

#### Remarks

This method sets the value of [SlotPhaseReceiveFilterEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasereceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXSlotPhaseReceiveFilterEnabled | Specifies whether to enable receive filtering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setspectruminverted__string-rfmxevdomxslotphasespectruminverted.html language=enus -->
## TOPIC 00183: SetSpectrumInverted(string, RFmxEvdoMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setspectruminverted__string-rfmxevdomxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setspectruminverted__string-rfmxevdomxslotphasespectruminverted.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetSpectrumInverted(string selectorString, RFmxEvdoMXSlotPhaseSpectrumInverted value)RemarksThis method sets the value of SlotPhaseSpectrumInverted attribute.The default value is False.Parameters

### SetSpectrumInverted(string, RFmxEvdoMXSlotPhaseSpectrumInverted)

Sets whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetSpectrumInverted(string selectorString, RFmxEvdoMXSlotPhaseSpectrumInverted value)

#### Remarks

This method sets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXSlotPhaseSpectrumInverted | Specifies whether the signal spectrum is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setsynchronizationmode__string-rfmxevdomxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00184: SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setsynchronizationmode__string-rfmxevdomxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-setsynchronizationmode__string-rfmxevdomxslotphasesynchronizationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetSynchronizationMode(string selectorString, RFmxEvdoMXSlotPhaseSynchronizationMode value)RemarksThis method sets the value of SlotPhaseSynchronizationMode attri

### SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)

Sets whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetSynchronizationMode(string selectorString, RFmxEvdoMXSlotPhaseSynchronizationMode value)

#### Remarks

This method sets the value of [SlotPhaseSynchronizationMode](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasesynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-settransientduration__string-double.html language=enus -->
## TOPIC 00185: SetTransientDuration(string, double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-settransientduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration-settransientduration__string-double.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the transient duration for the SlotPhase measurement. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetTransientDuration(string selectorString, double value)RemarksThis method sets the value of SlotPhaseTransientDuration attribute.The transient d

### SetTransientDuration(string, double)

Sets the transient duration for the SlotPhase measurement. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetTransientDuration(string selectorString, double value)

#### Remarks

This method sets the value of [SlotPhaseTransientDuration](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The transient duration is applied equally on either side of a half-slot boundary, that is, at the start and end of each half-slot.Setting the transient duation equal to zero means that no transient period is considered, and the entire half-slot data is used to determine the phase error best-fit line used to compute the phase discontinuity at the half-slot boundaries. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the transient duration for the SlotPhase measurement. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration.html language=enus -->
## TOPIC 00186: RFmxEvdoMXSlotPhaseConfiguration Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseconfiguration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SlotPhase measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSlotPhaseConfiguration : RFmxEvdoMXSubObjectMethodsNameDescriptionConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPhaseSynchron

### RFmxEvdoMXSlotPhaseConfiguration Class

Provides methods to configure the SlotPhase measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSlotPhaseConfiguration : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPhaseSynchronizationMode, int, int) | Configures the synchronization mode, measurement offset, and measurement length. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces after performing the SlotPhase measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SlotPhase measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of the SlotPhase measurement. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)property. |
| GetReceiveFilterEnabled(string, out RFmxEvdoMXSlotPhaseReceiveFilterEnabled) | Gets whether to enable receive filtering. |
| GetSpectrumInverted(string, out RFmxEvdoMXSlotPhaseSpectrumInverted) | Gets whether the signal spectrum is inverted. |
| GetSynchronizationMode(string, out RFmxEvdoMXSlotPhaseSynchronizationMode) | Gets whether the measurement is performed from the frame or the slot boundary. |
| GetTransientDuration(string, out double) | Gets the transient duration for the SlotPhase measurement. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces after performing the SlotPhase measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SlotPhase measurement. |
| SetMeasurementLength(string, int) | Sets the duration of the SlotPhase measurement. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode)property. |
| SetReceiveFilterEnabled(string, RFmxEvdoMXSlotPhaseReceiveFilterEnabled) | Sets whether to enable receive filtering. |
| SetSpectrumInverted(string, RFmxEvdoMXSlotPhaseSpectrumInverted) | Sets whether the signal spectrum is inverted. |
| SetSynchronizationMode(string, RFmxEvdoMXSlotPhaseSynchronizationMode) | Sets whether the measurement is performed from the frame or the slot boundary. |
| SetTransientDuration(string, double) | Sets the transient duration for the SlotPhase measurement. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasereceivefilterenabled.html language=enus -->
## TOPIC 00187: RFmxEvdoMXSlotPhaseReceiveFilterEnabled Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasereceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasereceivefilterenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSlotPhaseReceiveFilterEnabledMembersNameValueDescriptionFalse0Receive filtering is disabled. True1Receive filtering is enabled.

### RFmxEvdoMXSlotPhaseReceiveFilterEnabled Enumeration

Specifies whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSlotPhaseReceiveFilterEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Receive filtering is disabled. |
| True | 1 | Receive filtering is enabled. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html language=enus -->
## TOPIC 00188: FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a half-slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side

### FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a half-slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the half-slot boundary and extrapolates the phase error to the half-slot boundaries.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchChipPhaseErrorLinearFitTrace(string selectorString, double timeout, ref AnalogWaveform< float > chipPhaseErrorLinearFit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| chipPhaseErrorLinearFit | ref AnalogWaveform< float > | Upon return, contains the data for a real waveform including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchchipphaseerrortrace__string-double-ref.html language=enus -->
## TOPIC 00189: FetchChipPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchchipphaseerrortrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchchipphaseerrortrace__string-double-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace for the SlotPhase Measurement. The chip phase error is the phase error between the actually received waveform and the reference waveform.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchChipPhaseErrorTrace(string selectorString, double timeout, ref A

### FetchChipPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

Fetches the chip phase error trace for the SlotPhase Measurement. The chip phase error is the phase error between the actually received waveform and the reference waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchChipPhaseErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > chipPhaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| chipPhaseError | ref AnalogWaveform< float > | Upon return, contains the data for a real waveform including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchmaximumhalfslotphasediscontinuity__string-double-out.html language=enus -->
## TOPIC 00190: FetchMaximumHalfSlotPhaseDiscontinuity(string, double, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchmaximumhalfslotphasediscontinuity__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchmaximumhalfslotphasediscontinuity__string-double-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchMaximumHalfSlotPhaseDiscontinuity(string selectorString, double timeout, out double maximumHalfSlotPhaseDiscontinuity)ParametersNameTyp

### FetchMaximumHalfSlotPhaseDiscontinuity(string, double, out double)

Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchMaximumHalfSlotPhaseDiscontinuity(string selectorString, double timeout, out double maximumHalfSlotPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| maximumHalfSlotPhaseDiscontinuity | out double | Upon return, contains the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchphasediscontinuities__string-double-ref.html language=enus -->
## TOPIC 00191: FetchPhaseDiscontinuities(string, double, ref double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchphasediscontinuities__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-fetchphasediscontinuities__string-double-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] halfSlotPhaseDiscontinuity)ParametersNameTypeDescriptionselectorStri

### FetchPhaseDiscontinuities(string, double, ref double[])

Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] halfSlotPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| halfSlotPhaseDiscontinuity | ref double[] | Returns the array of slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-getmaximumhalfslotphasediscontinuity__string-out.html language=enus -->
## TOPIC 00192: GetMaximumHalfSlotPhaseDiscontinuity(string, out double)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-getmaximumhalfslotphasediscontinuity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults-getmaximumhalfslotphasediscontinuity__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMaximumHalfSlotPhaseDiscontinuity(string selectorString, out double value)RemarksThis method gets the value of SlotP

### GetMaximumHalfSlotPhaseDiscontinuity(string, out double)

Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMaximumHalfSlotPhaseDiscontinuity(string selectorString, out double value)

#### Remarks

This method gets the value of [SlotPhaseResultsMaximumHalfSlotPhaseDiscontinuity](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults.html language=enus -->
## TOPIC 00193: RFmxEvdoMXSlotPhaseResults Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphaseresults.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SlotPhase measurement results. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSlotPhaseResults : RFmxEvdoMXSubObjectMethodsNameDescriptionFetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform

### RFmxEvdoMXSlotPhaseResults Class

Provides methods to fetch and read the SlotPhase measurement results.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSlotPhaseResults : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >) | Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a half-slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the half-slot boundary and extrapolates the phase error to the half-slot boundaries. |
| FetchChipPhaseErrorTrace(string, double, ref AnalogWaveform< float >) | Fetches the chip phase error trace for the SlotPhase Measurement. The chip phase error is the phase error between the actually received waveform and the reference waveform. |
| FetchMaximumHalfSlotPhaseDiscontinuity(string, double, out double) | Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval. |
| FetchPhaseDiscontinuities(string, double, ref double[]) | Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval. |
| GetMaximumHalfSlotPhaseDiscontinuity(string, out double) | Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasespectruminverted.html language=enus -->
## TOPIC 00194: RFmxEvdoMXSlotPhaseSpectrumInverted Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasespectruminverted.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSlotPhaseSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxEvdoMXSlotPhaseSpectrumInverted Enumeration

Specifies whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSlotPhaseSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00195: RFmxEvdoMXSlotPhaseSynchronizationMode Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotphasesynchronizationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSlotPhaseSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of s

### RFmxEvdoMXSlotPhaseSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSlotPhaseSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(string, int) method starting at SetMeasurementOffset(string, int) slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPhase Meas Length method starting at SlotPhase Meas Offset slots from the slot boundary. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower-configuration.html language=enus -->
## TOPIC 00196: Configuration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower-configuration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxEvdoMXSlotPowerConfiguration instance that provides methods to configure the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic RFmxEvdoMXSlotPowerConfiguration Configuration { get; }

### Configuration

Gets the [RFmxEvdoMXSlotPowerConfiguration](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration.html) instance that provides methods to configure the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public [RFmxEvdoMXSlotPowerConfiguration](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration.html) Configuration { get; }

Parent topic:

RFmxEvdoMXSlotPower Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower-results.html language=enus -->
## TOPIC 00197: Results

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower-results.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxEvdoMXSlotPowerResults instance that provides methods to fetch and read the SlotPower measurement results. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic RFmxEvdoMXSlotPowerResults Results { get; }

### Results

Gets the [RFmxEvdoMXSlotPowerResults](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults.html) instance that provides methods to fetch and read the SlotPower measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public [RFmxEvdoMXSlotPowerResults](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults.html) Results { get; }

Parent topic:

RFmxEvdoMXSlotPower Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower.html language=enus -->
## TOPIC 00198: RFmxEvdoMXSlotPower Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpower.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SlotPower measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSlotPower : RFmxEvdoMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxEvdoMXSlotPowerConfiguration instance that provides methods to configure the S

### RFmxEvdoMXSlotPower Class

Represents the SlotPower measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSlotPower : RFmxEvdoMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxEvdoMXSlotPowerConfiguration instance that provides methods to configure the SlotPower measurement. |
| Results | Gets the RFmxEvdoMXSlotPowerResults instance that provides methods to fetch and read the SlotPower measurement results. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-configuresynchronizationmodeandinterval__string-rfmxevdomxslotpowersynchronizationmode-int-int.html language=enus -->
## TOPIC 00199: ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPowerSynchronizationMode, int, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-configuresynchronizationmodeandinterval__string-rfmxevdomxslotpowersynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-configuresynchronizationmodeandinterval__string-rfmxevdomxslotpowersynchronizationmode-int-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxEvdoMXSlotPowerSynchronizationMode synchronizationMode, int measurementOffset, int measurement

### ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPowerSynchronizationMode, int, int)

Configures the synchronization mode, measurement offset, and measurement length.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxEvdoMXSlotPowerSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxEvdoMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode method. |
| measurementLength | int | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00200: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPowerMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescription

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPowerMeasurementEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00201: GetMeasurementLength(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the SlotPower measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPowerMeasurementLength attribute.The default value is 16.Par

### GetMeasurementLength(string, out int)

Gets the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPowerMeasurementLength](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the SlotPower measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00202: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetMeasu

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setsynchronizationmode__string-rfmxevdomxslotpowersynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPowerMeasurementOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getreceivefilterenabled__string-out.html language=enus -->
## TOPIC 00203: GetReceiveFilterEnabled(string, out RFmxEvdoMXSlotPowerReceiveFilterEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getreceivefilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getreceivefilterenabled__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetReceiveFilterEnabled(string selectorString, out RFmxEvdoMXSlotPowerReceiveFilterEnabled value)RemarksThis method gets the value of SlotPowerReceiveFilterEnabled attribute.The default value is True

### GetReceiveFilterEnabled(string, out RFmxEvdoMXSlotPowerReceiveFilterEnabled)

Gets whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetReceiveFilterEnabled(string selectorString, out RFmxEvdoMXSlotPowerReceiveFilterEnabled value)

#### Remarks

This method gets the value of [SlotPowerReceiveFilterEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerreceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXSlotPowerReceiveFilterEnabled | Upon return, contains whether to enable receive filtering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00204: GetSpectrumInverted(string, out RFmxEvdoMXSlotPowerSpectrumInverted)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetSpectrumInverted(string selectorString, out RFmxEvdoMXSlotPowerSpectrumInverted value)RemarksThis method gets the value of SlotPowerSpectrumInverted attribute.The default value is False.Parame

### GetSpectrumInverted(string, out RFmxEvdoMXSlotPowerSpectrumInverted)

Gets whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSpectrumInverted(string selectorString, out RFmxEvdoMXSlotPowerSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPowerSpectrumInverted](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXSlotPowerSpectrumInverted | Upon return, contains whether the signal spectrum is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getsynchronizationmode__string-out.html language=enus -->
## TOPIC 00205: GetSynchronizationMode(string, out RFmxEvdoMXSlotPowerSynchronizationMode)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getsynchronizationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-getsynchronizationmode__string-out.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int GetSynchronizationMode(string selectorString, out RFmxEvdoMXSlotPowerSynchronizationMode value)RemarksThis method gets the value of SlotPowerSynchronizationMode a

### GetSynchronizationMode(string, out RFmxEvdoMXSlotPowerSynchronizationMode)

Gets whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int GetSynchronizationMode(string selectorString, out RFmxEvdoMXSlotPowerSynchronizationMode value)

#### Remarks

This method gets the value of [SlotPowerSynchronizationMode](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowersynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxEvdoMXSlotPowerSynchronizationMode | Upon return, contains whether the measurement is performed from the frame or the slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00206: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SlotPowerMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionsele

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SlotPowerMeasurementEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SlotPower measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00207: SetMeasurementLength(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the SlotPower measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of SlotPowerMeasurementLength attribute.The default value is 16.Paramet

### SetMeasurementLength(string, int)

Sets the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPowerMeasurementLength](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00208: SetMeasurementOffset(string, int)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetMeasu

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setsynchronizationmode__string-rfmxevdomxslotpowersynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPowerMeasurementOffset](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setreceivefilterenabled__string-rfmxevdomxslotpowerreceivefilterenabled.html language=enus -->
## TOPIC 00209: SetReceiveFilterEnabled(string, RFmxEvdoMXSlotPowerReceiveFilterEnabled)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setreceivefilterenabled__string-rfmxevdomxslotpowerreceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setreceivefilterenabled__string-rfmxevdomxslotpowerreceivefilterenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetReceiveFilterEnabled(string selectorString, RFmxEvdoMXSlotPowerReceiveFilterEnabled value)RemarksThis method sets the value of SlotPowerReceiveFilterEnabled attribute.The default value is True.Par

### SetReceiveFilterEnabled(string, RFmxEvdoMXSlotPowerReceiveFilterEnabled)

Sets whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetReceiveFilterEnabled(string selectorString, RFmxEvdoMXSlotPowerReceiveFilterEnabled value)

#### Remarks

This method sets the value of [SlotPowerReceiveFilterEnabled](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerreceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXSlotPowerReceiveFilterEnabled | Specifies whether to enable receive filtering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setspectruminverted__string-rfmxevdomxslotpowerspectruminverted.html language=enus -->
## TOPIC 00210: SetSpectrumInverted(string, RFmxEvdoMXSlotPowerSpectrumInverted)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setspectruminverted__string-rfmxevdomxslotpowerspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setspectruminverted__string-rfmxevdomxslotpowerspectruminverted.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetSpectrumInverted(string selectorString, RFmxEvdoMXSlotPowerSpectrumInverted value)RemarksThis method sets the value of SlotPowerSpectrumInverted attribute.The default value is False.Parameters

### SetSpectrumInverted(string, RFmxEvdoMXSlotPowerSpectrumInverted)

Sets whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetSpectrumInverted(string selectorString, RFmxEvdoMXSlotPowerSpectrumInverted value)

#### Remarks

This method sets the value of [SlotPowerSpectrumInverted](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXSlotPowerSpectrumInverted | Specifies whether the signal spectrum is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setsynchronizationmode__string-rfmxevdomxslotpowersynchronizationmode.html language=enus -->
## TOPIC 00211: SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setsynchronizationmode__string-rfmxevdomxslotpowersynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration-setsynchronizationmode__string-rfmxevdomxslotpowersynchronizationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int SetSynchronizationMode(string selectorString, RFmxEvdoMXSlotPowerSynchronizationMode value)RemarksThis method sets the value of SlotPowerSynchronizationMode attri

### SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode)

Sets whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int SetSynchronizationMode(string selectorString, RFmxEvdoMXSlotPowerSynchronizationMode value)

#### Remarks

This method sets the value of [SlotPowerSynchronizationMode](nationalinstruments-rfmx-evdomx-rfmxevdomxpropertyid.html) attribute.The default value is [Frame](nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowersynchronizationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxEvdoMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerConfiguration Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration.html language=enus -->
## TOPIC 00212: RFmxEvdoMXSlotPowerConfiguration Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerconfiguration.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SlotPower measurement. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSlotPowerConfiguration : RFmxEvdoMXSubObjectMethodsNameDescriptionConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPowerSynchron

### RFmxEvdoMXSlotPowerConfiguration Class

Provides methods to configure the SlotPower measurement.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSlotPowerConfiguration : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSynchronizationModeAndInterval(string, RFmxEvdoMXSlotPowerSynchronizationMode, int, int) | Configures the synchronization mode, measurement offset, and measurement length. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SlotPower measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of the SlotPower measurement. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) method. |
| GetReceiveFilterEnabled(string, out RFmxEvdoMXSlotPowerReceiveFilterEnabled) | Gets whether to enable receive filtering. |
| GetSpectrumInverted(string, out RFmxEvdoMXSlotPowerSpectrumInverted) | Gets whether the signal spectrum is inverted. |
| GetSynchronizationMode(string, out RFmxEvdoMXSlotPowerSynchronizationMode) | Gets whether the measurement is performed from the frame or the slot boundary. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SlotPower measurement. |
| SetMeasurementLength(string, int) | Sets the duration of the SlotPower measurement. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) method. |
| SetReceiveFilterEnabled(string, RFmxEvdoMXSlotPowerReceiveFilterEnabled) | Sets whether to enable receive filtering. |
| SetSpectrumInverted(string, RFmxEvdoMXSlotPowerSpectrumInverted) | Sets whether the signal spectrum is inverted. |
| SetSynchronizationMode(string, RFmxEvdoMXSlotPowerSynchronizationMode) | Sets whether the measurement is performed from the frame or the slot boundary. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerreceivefilterenabled.html language=enus -->
## TOPIC 00213: RFmxEvdoMXSlotPowerReceiveFilterEnabled Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerreceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerreceivefilterenabled.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable receive filtering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSlotPowerReceiveFilterEnabledMembersNameValueDescriptionFalse0Receive filtering is disabled. True1Receive filtering is enabled.

### RFmxEvdoMXSlotPowerReceiveFilterEnabled Enumeration

Specifies whether to enable receive filtering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSlotPowerReceiveFilterEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Receive filtering is disabled. |
| True | 1 | Receive filtering is enabled. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults-fetchpowers__string-double-ref-ref.html language=enus -->
## TOPIC 00214: FetchPowers(string, double, ref double[], ref double[])

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults-fetchpowers__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults-fetchpowers__string-double-ref-ref.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots.SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic int FetchPowers(string selectorString, double timeout, ref double[] halfSlotPow

### FetchPowers(string, double, ref double[], ref double[])

Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public int FetchPowers(string selectorString, double timeout, ref double[] halfSlotPower, ref double[] halfSlotPowerDelta)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| halfSlotPower | ref double[] | Upon return, contains the array of half slot powers. This value is expressed in dBm. |
| halfSlotPowerDelta | ref double[] | Upon return, contains the array of half slot power delta powers. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxEvdoMXSlotPowerResults Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults.html language=enus -->
## TOPIC 00215: RFmxEvdoMXSlotPowerResults Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerresults.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SlotPower measurement results. Derives fromRFmxEvdoMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSlotPowerResults : RFmxEvdoMXSubObjectMethodsNameDescriptionFetchPowers(string, double, ref double[], ref double[])Fetches the s

### RFmxEvdoMXSlotPowerResults Class

Provides methods to fetch and read the SlotPower measurement results.

#### Derives from

- RFmxEvdoMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSlotPowerResults : RFmxEvdoMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchPowers(string, double, ref double[], ref double[]) | Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerspectruminverted.html language=enus -->
## TOPIC 00216: RFmxEvdoMXSlotPowerSpectrumInverted Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowerspectruminverted.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSlotPowerSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxEvdoMXSlotPowerSpectrumInverted Enumeration

Specifies whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSlotPowerSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowersynchronizationmode.html language=enus -->
## TOPIC 00217: RFmxEvdoMXSlotPowerSynchronizationMode Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowersynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxslotpowersynchronizationmode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXSlotPowerSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of s

### RFmxEvdoMXSlotPowerSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXSlotPowerSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(string, int) method starting at SetMeasurementOffset(string, int) slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPower Meas Length method starting at SlotPower Meas Offset slots from the slot boundary. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxsubobject.html language=enus -->
## TOPIC 00218: RFmxEvdoMXSubObject Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxsubobject.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxsubobject.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents members that are common to all sub-object of RFmxEvdoMX classes. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic class RFmxEvdoMXSubObjectThread SafetyAny public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

### RFmxEvdoMXSubObject Class

Represents members that are common to all sub-object of RFmxEvdoMX classes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public class RFmxEvdoMXSubObject

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00219: RFmxEvdoMXTriggerMinimumQuietTimeMode Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxtriggerminimumquiettimemode.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXTriggerMinimumQuietTimeModeMembersNameValueDescriptionManual0The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTi

### RFmxEvdoMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXTriggerMinimumQuietTimeMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(string, double) method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html language=enus -->
## TOPIC 00220: RFmxEvdoMXTriggerType Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxtriggertype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXTriggerTypeMembersNameValueDescriptionNone0No Reference Trigger is configured. DigitalEdge1The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is speci

### RFmxEvdoMXTriggerType Enumeration

Specifies the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(string, string) method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSlope(string, RFmxEvdoMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxuplinkbranch.html language=enus -->
## TOPIC 00221: RFmxEvdoMXUplinkBranch Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxuplinkbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxuplinkbranch.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the quadrature branch on which a specific user defined-channel is mapped. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel<em>(n)</em>" as the Selector Strings to configure or read this met

### RFmxEvdoMXUplinkBranch Enumeration

Specifies the quadrature branch on which a specific user defined-channel is mapped. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomx-setchannelconfigurationmode__string-rfmxevdomxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html). Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXUplinkBranch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| I | 0 | Specifies the in-phase component. |
| Q | 1 | Specifies the quadrature component. |
| IAndQ | 2 | Specifies both the in-phase component and the quadrature component. |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx-rfmxevdomxuplinkdatamodulationtype.html language=enus -->
## TOPIC 00222: RFmxEvdoMXUplinkDataModulationType Enumeration

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx-rfmxevdomxuplinkdatamodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx-rfmxevdomxuplinkdatamodulationtype.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the modulation of the data channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. SyntaxNamespace: NationalInstruments.RFmx.EvdoMXpublic enum RFmxEvdoMXUplinkDataModulationTypeMembersNameValueDescripti

### RFmxEvdoMXUplinkDataModulationType Enumeration

Defines the modulation of the data channel. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode)](nationalinstruments-rfmx-evdomx-rfmxevdomx-setchannelconfigurationmode__string-rfmxevdomxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-evdomx-rfmxevdomxchannelconfigurationmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.EvdoMX](nationalinstruments-rfmx-evdomx.html)

public enum RFmxEvdoMXUplinkDataModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | 0 | Specifies that the measurement automatically detects the modulation type. |
| DataChannelAbsent | 1 | Specifies that the data channel is absent. |
| B4 | 2 | Specifies binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| Q4 | 3 | Specifies quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| Q2 | 4 | Specifies QPSK with the Walsh function W(2,1). |
| Q4Q2 | 5 | Specifies QPSK with the Walsh functions W(4,2) and W(2,1). |
| E4E2 | 6 | Specifies 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |

Parent topic:

NationalInstruments.RFmx.EvdoMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-evdomx.html language=enus -->
## TOPIC 00223: NationalInstruments.RFmx.EvdoMX

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-evdomx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-evdomx.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxEvdoMXDefines a root class which is used to identify and control EVDO signal configuration. RFmxEvdoMXAcpRepresents the ACP measurement. RFmxEvdoMXAcpConfigurationProvides methods to configure the ACP measurement. RFmxEvdoMXAcpResultsProvides methods to fetch and read the A

### NationalInstruments.RFmx.EvdoMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxEvdoMX | Defines a root class which is used to identify and control EVDO signal configuration. |
| RFmxEvdoMXAcp | Represents the ACP measurement. |
| RFmxEvdoMXAcpConfiguration | Provides methods to configure the ACP measurement. |
| RFmxEvdoMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
| RFmxEvdoMXCda | Represents the CDA measurement. |
| RFmxEvdoMXCdaConfiguration | Provides methods to configure the CDA measurement. |
| RFmxEvdoMXCdaResults | Provides methods to fetch and read the CDA measurement results. |
| RFmxEvdoMXChp | Represents the CHP measurement. |
| RFmxEvdoMXChpConfiguration | Provides methods to configure the CHP measurement. |
| RFmxEvdoMXChpResults | Provides methods to fetch and read the CHP measurement results. |
| RFmxEvdoMXConstants | Specifies constants for I/O terminals. |
| RFmxEvdoMXModAcc | Represents the ModAcc measurement. |
| RFmxEvdoMXModAccConfiguration | Provides methods to configure the ModAcc measurement. |
| RFmxEvdoMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
| RFmxEvdoMXObw | Represents the OBW measurement. |
| RFmxEvdoMXObwConfiguration | Provides methods to configure the OBW measurement. |
| RFmxEvdoMXObwResults | Provides methods to fetch and read the OBW measurement results. |
| RFmxEvdoMXSem | Represents the SEM measurement. |
| RFmxEvdoMXSemConfiguration | Provides methods to configure the SEM measurement. |
| RFmxEvdoMXSemResults | Provides methods to fetch and read the SEM measurement results. |
| RFmxEvdoMXSlotPhase | Represents the SlotPhase measurement. |
| RFmxEvdoMXSlotPhaseConfiguration | Provides methods to configure the SlotPhase measurement. |
| RFmxEvdoMXSlotPhaseResults | Provides methods to fetch and read the SlotPhase measurement results. |
| RFmxEvdoMXSlotPower | Represents the SlotPower measurement. |
| RFmxEvdoMXSlotPowerConfiguration | Provides methods to configure the SlotPower measurement. |
| RFmxEvdoMXSlotPowerResults | Provides methods to fetch and read the SlotPower measurement results. |
| RFmxEvdoMXSubObject | Represents members that are common to all sub-object of RFmxEvdoMX classes. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxEvdoMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
| RFmxEvdoMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
| RFmxEvdoMXAcpFftOverlapMode | Specifies how the FFT overlap is applied to the acquired samples. The default Value is Disabled. |
| RFmxEvdoMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. This method is used only if you set the SetMeasurementMethod(string, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange. |
| RFmxEvdoMXAcpMeasurementMethod | Specifies the method for performing the adjacent channel power (ACP) measurement. |
| RFmxEvdoMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. |
| RFmxEvdoMXAcpOffsetPowerReferenceCarrier | Specifies the carrier number that is used as the power reference to measure the offset channel relative power. |
| RFmxEvdoMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxEvdoMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxEvdoMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxEvdoMXCdaIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the CDA measurement. |
| RFmxEvdoMXCdaIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the CDA measurement. |
| RFmxEvdoMXCdaIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the CDA measurement. |
| RFmxEvdoMXCdaPowerUnit | Specifies the measurement unit of the code domain power results. |
| RFmxEvdoMXCdaReceiveFilterEnabled | Specifies whether to enable receive filtering. |
| RFmxEvdoMXCdaSpectrumInverted | Specifies whether the signal spectrum is inverted. |
| RFmxEvdoMXCdaSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| RFmxEvdoMXCdaUplinkBranch | Specifies the Walsh branch of the channel, subject to channel-specific analysis. |
| RFmxEvdoMXChannelConfigurationMode | Specifies whether to detect the channels automatically or to use a specified channel configuration. |
| RFmxEvdoMXChpAveragingEnabled | Specifies whether to enable averaging for the channel power (CHP) measurement. |
| RFmxEvdoMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement. |
| RFmxEvdoMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxEvdoMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxEvdoMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxEvdoMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to DigitalEdge. |
| RFmxEvdoMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to IQPowerEdge. |
| RFmxEvdoMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxEvdoMXTriggerType) method to IQPowerEdge. |
| RFmxEvdoMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| RFmxEvdoMXLinkDirection | Specifies the direction for which the frequency is calculated. Only Uplink is supported. |
| RFmxEvdoMXMeasurementTypes | Specifies the type of measurement. |
| RFmxEvdoMXModAccIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the EVM measurement. |
| RFmxEvdoMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the EVM measurement. |
| RFmxEvdoMXModAccIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the EVM measurement. |
| RFmxEvdoMXModAccMultiCarrierFilterEnabled | Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers. |
| RFmxEvdoMXModAccReceiveFilterEnabled | Specifies whether to enable receive filtering. |
| RFmxEvdoMXModAccSpectrumInverted | Specifies whether the measured spectrum is inverted. |
| RFmxEvdoMXModAccSynchronizationMode | Specifies whether the measurement is performed from frame, slot, or symbol boundary. |
| RFmxEvdoMXModAccUplinkDetectedBranch | Returns the quadrature branch of a particular detected channel. Use "channel<em>(n)</em>" as the selector string to read this method. |
| RFmxEvdoMXModAccUplinkDetectedDataModulationType | Returns the modulation type of the uplink data channel. |
| RFmxEvdoMXModAccUplinkPeakActiveCdeBranch | Returns the quadrature branch of the channel corresponding to the Peak Active CDE (dB) result. |
| RFmxEvdoMXModAccUplinkPeakCdeBranch | Returns the branch of the channel corresponding to the Peak Active CDE (dB) method result. |
| RFmxEvdoMXObwAveragingEnabled | Specifies whether to enable averaging for the occupied bandwidth (OBW) measurement. |
| RFmxEvdoMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for occupied bandwidth (OBW) measurement. |
| RFmxEvdoMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxEvdoMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxEvdoMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxEvdoMXPhysicalLayerSubtype | Selects the EV-DO physical layer subtype. |
| RFmxEvdoMXPropertyId | Specifies all the attribute identifiers. |
| RFmxEvdoMXSemAveragingEnabled | Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement. |
| RFmxEvdoMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. |
| RFmxEvdoMXSemCompositeMeasurementStatus | Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. |
| RFmxEvdoMXSemLowerOffsetMeasurementStatus | Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. |
| RFmxEvdoMXSemOffsetRbwFilterType | Returns the type of RBW filter used to sweep the offset segment. |
| RFmxEvdoMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxEvdoMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<em>(n)</em>" as the selector string to read this method. |
| RFmxEvdoMXSlotPhaseReceiveFilterEnabled | Specifies whether to enable receive filtering. |
| RFmxEvdoMXSlotPhaseSpectrumInverted | Specifies whether the signal spectrum is inverted. |
| RFmxEvdoMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| RFmxEvdoMXSlotPowerReceiveFilterEnabled | Specifies whether to enable receive filtering. |
| RFmxEvdoMXSlotPowerSpectrumInverted | Specifies whether the signal spectrum is inverted. |
| RFmxEvdoMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| RFmxEvdoMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxEvdoMXTriggerType | Specifies the trigger type. |
| RFmxEvdoMXUplinkBranch | Specifies the quadrature branch on which a specific user defined-channel is mapped. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel<em>(n)</em>" as the Selector Strings to configure or read this method. |
| RFmxEvdoMXUplinkDataModulationType | Defines the modulation of the data channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. |

#### Delegates

None

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxevdomxextension-getevdosignalconfiguration__this-string.html language=enus -->
## TOPIC 00224: GetEvdoSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxevdomxextension-getevdosignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxevdomxextension-getevdosignalconfiguration__this-string.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a EVDO signal configuration for specified signal name. Existing EVDO signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxEvdoMX GetEvdoSignalConfiguration(this RFmxInstrMX instrSession, string signalName)Paramet

### GetEvdoSignalConfiguration(this RFmxInstrMX, string)

Creates a EVDO signal configuration for specified signal name. Existing EVDO signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxEvdoMX](nationalinstruments-rfmx-evdomx-rfmxevdomx.html) GetEvdoSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxEvdoMX.

Parent topic:

RFmxEvdoMXExtension Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxevdomxextension-getevdosignalconfiguration__this.html language=enus -->
## TOPIC 00225: GetEvdoSignalConfiguration(this RFmxInstrMX)

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxevdomxextension-getevdosignalconfiguration__this.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxevdomxextension-getevdosignalconfiguration__this.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new default EVDO signal configuration if it doesn't exist; otherwise, it returns the existing default EVDO signal configuration. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxEvdoMX GetEvdoSignalConfiguration(this RFmxInstrMX instrSession)ParametersNameTypeDescriptioni

### GetEvdoSignalConfiguration(this RFmxInstrMX)

Creates a new default EVDO signal configuration if it doesn't exist; otherwise, it returns the existing default EVDO signal configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxEvdoMX](nationalinstruments-rfmx-evdomx-rfmxevdomx.html) GetEvdoSignalConfiguration(this RFmxInstrMX instrSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |

#### Returns

Returns an object of type RFmxEvdoMX.

Parent topic:

RFmxEvdoMXExtension Class

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxevdomxextension.html language=enus -->
## TOPIC 00226: RFmxEvdoMXExtension Class

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxevdomxextension.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxevdomxextension.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides extension methods to create EV-DO signal configuration. These methods are added to RFmxInstrMX class. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic class RFmxEvdoMXExtensionRemarksFor more information about RFmx Instruments, refer to the RFmx Instruments Help.Threa

### RFmxEvdoMXExtension Class

Provides extension methods to create EV-DO signal configuration. These methods are added to RFmxInstrMX class.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public class RFmxEvdoMXExtension

#### Remarks

For more information about RFmx Instruments, refer to the RFmx Instruments Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetEvdoSignalConfiguration(this RFmxInstrMX, string) | Creates a EVDO signal configuration for specified signal name. Existing EVDO signal configuration is returned if specified signal name exists. |
| GetEvdoSignalConfiguration(this RFmxInstrMX) | Creates a new default EVDO signal configuration if it doesn't exist; otherwise, it returns the existing default EVDO signal configuration. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxevdo-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00227: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxevdo-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxevdo-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxEvdoMXExtensionProvides extension methods to create EV-DO signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxEvdoMXExtension | Provides extension methods to create EV-DO signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None
