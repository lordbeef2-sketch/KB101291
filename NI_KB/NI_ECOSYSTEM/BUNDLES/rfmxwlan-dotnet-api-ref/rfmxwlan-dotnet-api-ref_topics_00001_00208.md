# NI DOCUMENT BUNDLE: rfmxwlan-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwlan-dotnet-api-ref start=1 end=208 -->
<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getchannelbandwidth__string-out.html language=enus -->
## TOPIC 00001: GetChannelBandwidth(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getchannelbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getchannelbandwidth__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel spacing as defined under section 3.1 of IEEE Standard 802.11–2016 (pp. 130) . This value is specified in Hz. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetChannelBandwidth(string selectorString, out double value)RemarksThis method gets the value of ChannelBandwidth a

### GetChannelBandwidth(string, out double)

Gets the channel spacing as defined under section 3.1 of *IEEE Standard 802.11–2016 (pp. 130)* . This value is specified in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetChannelBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChannelBandwidth](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 20M.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the channel spacing as defined under section 3.1 of IEEE Standard 802.11–2016 (pp. 130) . This value is specified in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getdetectedburstlength__string-out.html language=enus -->
## TOPIC 00002: GetDetectedBurstLength(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getdetectedburstlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getdetectedburstlength__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the packet detected by the AutoDetectSignal(string, double) function. The value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetDetectedBurstLength(string selectorString, out double value)RemarksThis method gets the value of DetectedBurstLe

### GetDetectedBurstLength(string, out double)

Gets the duration of the packet detected by the [AutoDetectSignal(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-autodetectsignal__string-double.html) function. The value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetDetectedBurstLength(string selectorString, out double value)

#### Remarks

This method gets the value of [DetectedBurstLength](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.You do not need to use a selector string to configure or read this method for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the duration of the packet detected by the AutoDetectSignal(string, double) function. The value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getdigitaledgetriggersource__string-out.html language=enus -->
## TOPIC 00003: GetDigitalEdgeTriggerSource(string, out string)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getdigitaledgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getdigitaledgetriggersource__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is confi

### GetDigitalEdgeTriggerSource(string, out string)

Gets the source terminal for the digital edge trigger. This method is used only when you set the [SetTriggerType(string, RFmxWlanMXTriggerType)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggertype.html) . On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is configured to "segment0/chain0" and is considered as the master port.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetDigitalEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value off this method is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getiqpoweredgetriggerleveltype__string-out.html language=enus -->
## TOPIC 00004: GetIQPowerEdgeTriggerLevelType(string, out RFmxWlanMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getiqpoweredgetriggerleveltype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getiqpoweredgetriggerleveltype__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetIQPowerEdgeTriggerLevelT

### GetIQPowerEdgeTriggerLevelType(string, out RFmxWlanMXIQPowerEdgeTriggerLevelType)

Gets the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxWlanMXTriggerType)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggertype.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetIQPowerEdgeTriggerLevelType(string selectorString, out RFmxWlanMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-wlanmx-rfmxwlanmxiqpoweredgetriggerleveltype.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXIQPowerEdgeTriggerLevelType | Upon return, contains the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getlimitedconfigurationchange__string-out.html language=enus -->
## TOPIC 00005: GetLimitedConfigurationChange(string, out RFmxWlanMXLimitedConfigurationChange)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getlimitedconfigurationchange__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getlimitedconfigurationchange__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetLimitedConfigurationChange(string selectorString, out RFmxWlanMXLimitedConfigurationChange value)RemarksThis method gets the value of Limited

### GetLimitedConfigurationChange(string, out RFmxWlanMXLimitedConfigurationChange)

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetLimitedConfigurationChange(string selectorString, out RFmxWlanMXLimitedConfigurationChange value)

#### Remarks

This method gets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxlimitedconfigurationchange.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXLimitedConfigurationChange | Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getnumberoffrequencysegments__string-out.html language=enus -->
## TOPIC 00006: GetNumberOfFrequencySegments(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getnumberoffrequencysegments__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getnumberoffrequencysegments__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of frequency segments for 802.11ac and 802.11ax signals. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfFrequencySegments(string selectorString, out int value)RemarksThis method gets the value of NumberOfFrequencySegments attribute.The default value is 1. Valid

### GetNumberOfFrequencySegments(string, out int)

Gets the number of frequency segments for 802.11ac and 802.11ax signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfFrequencySegments(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfFrequencySegments](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1. Valid values are 1 and 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of frequency segments for 802.11ac and 802.11ax signals. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getnumberofreceivechains__string-out.html language=enus -->
## TOPIC 00007: GetNumberOfReceiveChains(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getnumberofreceivechains__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getnumberofreceivechains__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of receive chains for OFDM standards. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfReceiveChains(string selectorString, out int value)RemarksThis method gets the value of NumberOfReceiveChains attribute.The default value is 1. The valid values are as follows.

### GetNumberOfReceiveChains(string, out int)

Gets the number of receive chains for OFDM standards.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfReceiveChains(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfReceiveChains](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1. The valid values are as follows. StandardNumber of Receive Chains802.11a/g, 802.11j, 802.11p1802.11n1–4802.11ac, 802.11ax, 802.11be1–8

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of receive chains for OFDM standards. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmehtsigcompressionenabled__string-out.html language=enus -->
## TOPIC 00008: GetOfdmEhtSigCompressionEnabled(string, out RFmxWlanMXOfdmEhtSigCompressionEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmehtsigcompressionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmehtsigcompressionenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetOfdmEhtSigCompressionEnabled(string selectorString, out RFmxWlanMXOfdmEhtSigCompressionEnabled value)

### GetOfdmEhtSigCompressionEnabled(string, out RFmxWlanMXOfdmEhtSigCompressionEnabled)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmEhtSigCompressionEnabled(string selectorString, out RFmxWlanMXOfdmEhtSigCompressionEnabled value)

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmfrequencyband__string-out.html language=enus -->
## TOPIC 00009: GetOfdmFrequencyBand(string, out RFmxWlanMXOfdmFrequencyBand)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmfrequencyband__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmfrequencyband__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetOfdmFrequencyBand(string selectorString, out RFmxWlanMXOfdmFrequencyBand value)RemarksThis m

### GetOfdmFrequencyBand(string, out RFmxWlanMXOfdmFrequencyBand)

Gets the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in *IEEE Standard 802.11n – 2009* .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmFrequencyBand(string selectorString, out RFmxWlanMXOfdmFrequencyBand value)

#### Remarks

This method gets the value of [OfdmFrequencyBand](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 2.4 GHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmFrequencyBand | Upon return, contains the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmheaderdecodingenabled__string-out.html language=enus -->
## TOPIC 00010: GetOfdmHeaderDecodingEnabled(string, out RFmxWlanMXOfdmHeaderDecodingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmheaderdecodingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmheaderdecodingenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the decoding of the header fields in the PPDU. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetOfdmHeaderDecodingEnabled(string selectorString, out RFmxWlanMXOfdmHeaderDecodingEnabled value)RemarksThis method gets the value of OfdmHeaderDecodingEnabled attribute.

### GetOfdmHeaderDecodingEnabled(string, out RFmxWlanMXOfdmHeaderDecodingEnabled)

Gets whether to enable the decoding of the header fields in the PPDU.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmHeaderDecodingEnabled(string selectorString, out RFmxWlanMXOfdmHeaderDecodingEnabled value)

#### Remarks

This method gets the value of [OfdmHeaderDecodingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmheaderdecodingenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmHeaderDecodingEnabled | Upon return, contains whether to enable the decoding of the header fields in the PPDU. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmppdutype__string-out.html language=enus -->
## TOPIC 00011: GetOfdmPpduType(string, out RFmxWlanMXOfdmPpduType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmppdutype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmppdutype__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetOfdmPpduType(string selectorString, out RFmxWlanMXOfdmPpduType value)RemarksThis method gets the

### GetOfdmPpduType(string, out RFmxWlanMXOfdmPpduType)

Gets the PPDU type when you set the [SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmautoppdutypedetectionenabled__string-rfmxwlanmxofdmautoppdutypedetectionenabled.html) method to [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmautoppdutypedetectionenabled.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmPpduType(string selectorString, out RFmxWlanMXOfdmPpduType value)

#### Remarks

This method gets the value of [OfdmPpduType](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is Non-HT.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmPpduType | Upon return, contains the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmpreamblepuncturingbitmap__string-out.html language=enus -->
## TOPIC 00012: GetOfdmPreamblePuncturingBitmap(string, out long)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmpreamblepuncturingbitmap__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmpreamblepuncturingbitmap__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punct

### GetOfdmPreamblePuncturingBitmap(string, out long)

Gets the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmPreamblePuncturingBitmap(string selectorString, out long value)

#### Remarks

This method gets the value of [OfdmPreamblePuncturingBitmap](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 0xFFF FFFF FFFF FFFF, indicating that none of the eight 20 MHz sub-channels of a 160 MHz PPDU are punctured. The most significant 52 bits are reserved for future use.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out long | Upon return, contains the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmprefecpaddingfactor__string-out.html language=enus -->
## TOPIC 00013: GetOfdmPreFecPaddingFactor(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmprefecpaddingfactor__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmprefecpaddingfactor__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetOfdmPreFecPaddingFactor(string selectorString, out int value)RemarksThis method gets the valu

### GetOfdmPreFecPaddingFactor(string, out int)

Gets the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmPreFecPaddingFactor(string selectorString, out int value)

#### Remarks

This method gets the value of [OfdmPreFecPaddingFactor](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmruoffsetmruindex__string-out.html language=enus -->
## TOPIC 00014: GetOfdmRUOffsetMruIndex(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmruoffsetmruindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getofdmruoffsetmruindex__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 If a dRU i

### GetOfdmRUOffsetMruIndex(string, out int)

Gets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of *IEEE P802.11be/D7.0* If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of *IEEE P802.11bn/D1.3* .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOfdmRUOffsetMruIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [OfdmRUOffsetMruIndex](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the user number. Example: "user0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of IEEE P802.11bn/D1.3 . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getreferencelevelheadroom__string-out.html language=enus -->
## TOPIC 00015: GetReferenceLevelHeadroom(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getreferencelevelheadroom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getreferencelevelheadroom__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668

### GetReferenceLevelHeadroom(string, out double)

Gets the margin RFmx adds to the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setreferencelevel__string-double.html) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetReferenceLevelHeadroom(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-gettriggergateenabled__string-out.html language=enus -->
## TOPIC 00016: GetTriggerGateEnabled(string, out RFmxWlanMXTriggerGateEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-gettriggergateenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-gettriggergateenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables time-domain gating of the acquired signal for SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetTriggerGateEnabled(string selectorString, out RFmxWlanMXTriggerGateEnabled value)RemarksThis method gets the value of TriggerGateEnabled attribute.The default value is

### GetTriggerGateEnabled(string, out RFmxWlanMXTriggerGateEnabled)

Enables time-domain gating of the acquired signal for SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetTriggerGateEnabled(string selectorString, out RFmxWlanMXTriggerGateEnabled value)

#### Remarks

This method gets the value of [TriggerGateEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggergateenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXTriggerGateEnabled | Enables time-domain gating of the acquired signal for SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-gettriggergatelength__string-out.html language=enus -->
## TOPIC 00017: GetTriggerGateLength(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-gettriggergatelength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-gettriggergatelength__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled) method to True . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetTriggerGateLeng

### GetTriggerGateLength(string, out double)

Gets the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the [SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggergateenabled__string-rfmxwlanmxtriggergateenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggergateenabled.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetTriggerGateLength(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerGateLength](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1 millisecond.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled) method to True . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getwarning__out-out.html language=enus -->
## TOPIC 00018: GetWarning(out int, out string)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getwarning__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-getwarning__out-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest warning code and description. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetWarning(out int warningCode, out string warningDescription)ParametersNameTypeDescriptionwarningCodeout intUpon return, contains the latest warning code.warningDescriptionout stringUpon return,

### GetWarning(out int, out string)

Gets the latest warning code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetWarning(out int warningCode, out string warningDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warningCode | out int | Upon return, contains the latest warning code. |
| warningDescription | out string | Upon return, contains the latest warning description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-isdisposed.html language=enus -->
## TOPIC 00019: IsDisposed

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-isdisposed.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false .

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false .

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-resetattribute__string-rfmxwlanmxpropertyid.html language=enus -->
## TOPIC 00020: ResetAttribute(string, RFmxWlanMXPropertyId)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-resetattribute__string-rfmxwlanmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-resetattribute__string-rfmxwlanmxpropertyid.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ResetAttribute(string selectorString, RFmxWlanMXPropertyId attributeId)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the method being reset. Refer to the Using a

### ResetAttribute(string, RFmxWlanMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ResetAttribute(string selectorString, RFmxWlanMXPropertyId attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the method being reset. Refer to the Using a Selector String (.NET) topic in the NI-RFmx WLAN Help for more information about configuring the selector string. |
| attributeId | RFmxWlanMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setnumberofreceivechains__string-int.html language=enus -->
## TOPIC 00021: SetNumberOfReceiveChains(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setnumberofreceivechains__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setnumberofreceivechains__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of receive chains for OFDM standards. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetNumberOfReceiveChains(string selectorString, int value)RemarksThis method sets the value of NumberOfReceiveChains attribute.The default value is 1. The valid values are as follows. Sta

### SetNumberOfReceiveChains(string, int)

Sets the number of receive chains for OFDM standards.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetNumberOfReceiveChains(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfReceiveChains](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1. The valid values are as follows. StandardNumber of Receive Chains802.11a/g, 802.11j, 802.11p1802.11n1–4802.11ac, 802.11ax, 802.11be1–8

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of receive chains for OFDM standards. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmfrequencyband__string-rfmxwlanmxofdmfrequencyband.html language=enus -->
## TOPIC 00022: SetOfdmFrequencyBand(string, RFmxWlanMXOfdmFrequencyBand)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmfrequencyband__string-rfmxwlanmxofdmfrequencyband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmfrequencyband__string-rfmxwlanmxofdmfrequencyband.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmFrequencyBand(string selectorString, RFmxWlanMXOfdmFrequencyBand value)RemarksThis metho

### SetOfdmFrequencyBand(string, RFmxWlanMXOfdmFrequencyBand)

Sets the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in *IEEE Standard 802.11n – 2009* .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmFrequencyBand(string selectorString, RFmxWlanMXOfdmFrequencyBand value)

#### Remarks

This method sets the value of [OfdmFrequencyBand](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 2.4 GHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmFrequencyBand | Specifies the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmltfsize__string-rfmxwlanmxofdmltfsize.html language=enus -->
## TOPIC 00023: SetOfdmLtfSize(string, RFmxWlanMXOfdmLtfSize)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmltfsize__string-rfmxwlanmxofdmltfsize.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmltfsize__string-rfmxwlanmxofdmltfsize.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the LTF symbol size. This method is applicable only for 802.11ax, 802.11be, and 802.11bn signals. For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False.SyntaxNamespace: NationalInstruments

### SetOfdmLtfSize(string, RFmxWlanMXOfdmLtfSize)

Sets the LTF symbol size. This method is applicable only for 802.11ax, 802.11be, and 802.11bn signals. For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmLtfSize(string selectorString, RFmxWlanMXOfdmLtfSize value)

#### Remarks

This method sets the value of [OfdmLtfSize](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [LtfSize4x](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmltfsize.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmLtfSize | Specifies the LTF symbol size. This method is applicable only for 802.11ax, 802.11be, and 802.11bn signals. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofltfsymbols__string-int.html language=enus -->
## TOPIC 00024: SetOfdmNumberOfLtfSymbols(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofltfsymbols__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofltfsymbols__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmNumberOfLtfSymbols(string selectorString, int value)RemarksThis method sets the value of OfdmNumberOfLtfSymbol

### SetOfdmNumberOfLtfSymbols(string, int)

Sets the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmNumberOfLtfSymbols(string selectorString, int value)

#### Remarks

This method sets the value of [OfdmNumberOfLtfSymbols](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The valid values are 1, 2, 4, 6, and 8. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofspacetimestreams__string-int.html language=enus -->
## TOPIC 00025: SetOfdmNumberOfSpaceTimeStreams(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofspacetimestreams__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofspacetimestreams__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of space time streams. This method is applicable when you set the OFDMHeaderDecodingEnabled method to False for 802.11n, 802.11ac, 802.11ax, and 802.11be standards or when PPDU Type is TB for 802.11ax, 802.11be, or 802.11bn standards. SyntaxNamespace: NationalInstruments.RFmx.WlanMXp

### SetOfdmNumberOfSpaceTimeStreams(string, int)

Sets the number of space time streams. This method is applicable when you set the OFDMHeaderDecodingEnabled method to **False** for 802.11n, 802.11ac, 802.11ax, and 802.11be standards or when PPDU Type is TB for 802.11ax, 802.11be, or 802.11bn standards.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmNumberOfSpaceTimeStreams(string selectorString, int value)

#### Remarks

This method sets the value of [OfdmNumberOfSpaceTimeStreams](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the user number. Example: "user0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | int | Specifies the number of space time streams. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofusers__string-int.html language=enus -->
## TOPIC 00026: SetOfdmNumberOfUsers(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofusers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmnumberofusers__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of users in a multi-user (MU) PPDU. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmNumberOfUsers(string selectorString, int value)RemarksThis method sets the value of OfdmNumberOfUsers attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstri

### SetOfdmNumberOfUsers(string, int)

Sets the number of users in a multi-user (MU) PPDU.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmNumberOfUsers(string selectorString, int value)

#### Remarks

This method sets the value of [OfdmNumberOfUsers](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of users in a multi-user (MU) PPDU. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmphaserotationcoefficient3__string-rfmxwlanmxofdmphaserotationcoefficient3.html language=enus -->
## TOPIC 00027: SetOfdmPhaseRotationCoefficient3(string, RFmxWlanMXOfdmPhaseRotationCoefficient3)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmphaserotationcoefficient3__string-rfmxwlanmxofdmphaserotationcoefficient3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmphaserotationcoefficient3__string-rfmxwlanmxofdmphaserotationcoefficient3.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmPhaseRotationCoefficient3(string selectorString, RFmxWlanMXOfdmPhaseRotationCoefficient3 value)RemarksThis method sets the value of OfdmPhaseRotationCo

### SetOfdmPhaseRotationCoefficient3(string, RFmxWlanMXOfdmPhaseRotationCoefficient3)

Sets the phase rotation coefficient 3 as defined in *IEEE Standard P802.11be/D7.0* .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmPhaseRotationCoefficient3(string selectorString, RFmxWlanMXOfdmPhaseRotationCoefficient3 value)

#### Remarks

This method sets the value of [OfdmPhaseRotationCoefficient3](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is -1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmPhaseRotationCoefficient3 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmpreamblepuncturingenabled__string-rfmxwlanmxofdmpreamblepuncturingenabled.html language=enus -->
## TOPIC 00028: SetOfdmPreamblePuncturingEnabled(string, RFmxWlanMXOfdmPreamblePuncturingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmpreamblepuncturingenabled__string-rfmxwlanmxofdmpreamblepuncturingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmpreamblepuncturingenabled__string-rfmxwlanmxofdmpreamblepuncturingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmPreamblePuncturingEnabled(string selectorString, RFmxWlanMXOfdmPreamblePuncturingEnabled value)RemarksThis method sets the v

### SetOfdmPreamblePuncturingEnabled(string, RFmxWlanMXOfdmPreamblePuncturingEnabled)

Sets whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmPreamblePuncturingEnabled(string selectorString, RFmxWlanMXOfdmPreamblePuncturingEnabled value)

#### Remarks

This method sets the value of [OfdmPreamblePuncturingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmpreamblepuncturingenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmPreamblePuncturingEnabled | Specifies whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmprefecpaddingfactor__string-int.html language=enus -->
## TOPIC 00029: SetOfdmPreFecPaddingFactor(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmprefecpaddingfactor__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmprefecpaddingfactor__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmPreFecPaddingFactor(string selectorString, int value)RemarksThis method sets the value of

### SetOfdmPreFecPaddingFactor(string, int)

Sets the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmPreFecPaddingFactor(string selectorString, int value)

#### Remarks

This method sets the value of [OfdmPreFecPaddingFactor](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmspacetimestreamoffset__string-int.html language=enus -->
## TOPIC 00030: SetOfdmSpaceTimeStreamOffset(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmspacetimestreamoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setofdmspacetimestreamoffset__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the space time stream offset. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetOfdmSpaceTimeStreamOffset(string selectorString, int value)RemarksThis method sets the value of OfdmSpaceTimeStreamOffset attribute.The default value is 0.ParametersNameTypeDescriptionselectorStringstrin

### SetOfdmSpaceTimeStreamOffset(string, int)

Sets the space time stream offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetOfdmSpaceTimeStreamOffset(string selectorString, int value)

#### Remarks

This method sets the value of [OfdmSpaceTimeStreamOffset](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the user number. Example: "user0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | int | Specifies the space time stream offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setstandard__string-rfmxwlanmxstandard.html language=enus -->
## TOPIC 00031: SetStandard(string, RFmxWlanMXStandard)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setstandard__string-rfmxwlanmxstandard.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setstandard__string-rfmxwlanmxstandard.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the signal under analysis as defined in IEEE Standard 802.11 . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetStandard(string selectorString, RFmxWlanMXStandard value)RemarksThis method sets the value of Standard attribute.The default value is 802.11a/g.ParametersNameTypeDescript

### SetStandard(string, RFmxWlanMXStandard)

Sets the signal under analysis as defined in *IEEE Standard 802.11* .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetStandard(string selectorString, RFmxWlanMXStandard value)

#### Remarks

This method sets the value of [Standard](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 802.11a/g.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXStandard | Specifies the signal under analysis as defined in IEEE Standard 802.11 . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html language=enus -->
## TOPIC 00032: SetTriggerType(string, RFmxWlanMXTriggerType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetTriggerType(string selectorString, RFmxWlanMXTriggerType value)RemarksThis method sets the value of TriggerType attribute.The default value is IQPowerEdge .ParametersNameTypeDescriptionselectorStringstringPass an em

### SetTriggerType(string, RFmxWlanMXTriggerType)

Sets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetTriggerType(string selectorString, RFmxWlanMXTriggerType value)

#### Remarks

This method sets the value of [TriggerType](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [IQPowerEdge](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggertype.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXTriggerType | Specifies the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-signalconfigurationname.html language=enus -->
## TOPIC 00033: SignalConfigurationName

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-signalconfigurationname.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-signalconfigurationname.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the signal configuration name. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic string SignalConfigurationName { get; }RemarksReturns a string representing the signal configuration name

### SignalConfigurationName

Gets the signal configuration name.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public string SignalConfigurationName { get; }

#### Remarks

Returns a string representing the signal configuration name

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-signalconfigurationtype.html language=enus -->
## TOPIC 00034: SignalConfigurationType

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-signalconfigurationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-signalconfigurationtype.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxWlanMX. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic Type SignalConfigurationType { get; }RemarksReturns the type of signal configuration object.

### SignalConfigurationType

Gets the Type object for RFmxWlanMX.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public Type SignalConfigurationType { get; }

#### Remarks

Returns the type of signal configuration object.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-txp.html language=enus -->
## TOPIC 00035: Txp

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-txp.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWlanMXTxp instance that represents the TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic RFmxWlanMXTxp Txp { get; }

### Txp

Gets the [RFmxWlanMXTxp](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxp.html) instance that represents the TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public [RFmxWlanMXTxp](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxp.html) Txp { get; }

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00036: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the

### WaitForMeasurementComplete(string, double)

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMX Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmx.html language=enus -->
## TOPIC 00037: RFmxWlanMX Class

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmx.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class which is used to identify and control WLAN signal configuration. Derives fromISignalConfigurationIDisposableSyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic class RFmxWlanMX : ISignalConfiguration, IDisposablePropertiesNameDescriptionDsssModAccGets the RFmxWlanMXDsssModAcc

### RFmxWlanMX Class

Defines a root class which is used to identify and control WLAN signal configuration.

#### Derives from

- ISignalConfiguration
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public class RFmxWlanMX : ISignalConfiguration, IDisposable

#### Properties

| Name | Description |
| --- | --- |
| DsssModAcc | Gets the RFmxWlanMXDsssModAcc instance that represents the DSSSModAcc measurement. |
| IsDisposed | Gets a value that indicates whether the signal has been disposed. |
| OfdmModAcc | Gets the RFmxWlanMXOfdmModAcc instance that represents the OFDMModAcc measurement. |
| PowerRamp | Gets the RFmxWlanMXPowerRamp instance that represents the PowerRamp measurement. |
| Sem | Gets the RFmxWlanMXSem instance that represents the SEM measurement. |
| SignalConfigurationName | Gets the signal configuration name. |
| SignalConfigurationType | Gets the Type object for RFmxWlanMX. |
| Txp | Gets the RFmxWlanMXTxp instance that represents the TXP measurement. |

#### Methods

| Name | Description |
| --- | --- |
| AbortMeasurements(string) | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
| AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long) | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the property node. Use this method only if the Recommended Acquisition Type method value is either IQ or IQorSpectral . When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx WLAN Commit method. |
| AnalyzeNWaveformsIQ(string, string, ComplexWaveform< ComplexSingle >[], bool) | Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either IQ or IQorSpectral. When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx WLAN Commit method. |
| AnalyzeNWaveformsSpectrum(string, string, Spectrum< float >[], bool) | Performs the enabled measurements on the spectrum(s) that you specify in the spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either spectral or IQorSpectral. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmxWLAN Commit method. |
| AnalyzeSpectrum1Waveform(string, string, Spectrum< float >, bool, long) | Performs the enabled measurements on the spectrum that you specify in the spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the property node. Use this method only if the Recommended Acquisition Type method value is either spectral or IQorSpectral . Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmxWLAN Commit method. |
| AutoDetectSignal(string, double) | Automatically detects the standard, channel bandwidth, and burst length of the input signal, and writes the NationalInstruments.RFmx.WlanMX.RFmxWlanMX.GetDetectedStandard(string,NationalInstruments.RFmx.WlanMX.RFmxWlanMXStandard@) , GetDetectedChannelBandwidth(string, out double) , and GetDetectedBurstLength(string, out double) methods. You must configure the SetReferenceLevel(string, double) method before calling this method. If the peak power level of the input is unknown, you can call the AutoLevel(string, double) method to configure the Reference Level method after you set the SetStandard(string, RFmxWlanMXStandard) and SetChannelBandwidth(string, double) methods to values corresponding to maximum expected channel bandwidth. |
| AutoDetectSignalAnalysisOnly(string, ComplexWaveform< ComplexSingle >) | Automatically detects the standard, channel bandwidth, and burst length on the I/Q complex waveform that you specify in IQ Parameter, and writes the NationalInstruments.RFmx.WlanMX.RFmxWlanMX.GetDetectedStandard(string,NationalInstruments.RFmx.WlanMX.RFmxWlanMXStandard@) , GetDetectedChannelBandwidth(string, out double) , and GetDetectedBurstLength(string, out double) methods. |
| AutoLevel(string, double) | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(string, double) method. Use this method to help calculate an approximate setting for the reference level. |
| CheckMeasurementStatus(string, out bool) | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| ClearAllNamedResults(string) | Clears all results for the current signal instance. |
| ClearNamedResult(string) | Clears a result instance specified by the result name in the selectorString parameter. |
| CloneSignalConfiguration(string, out RFmxWlanMX) | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
| Commit(string) | Commits settings to the hardware. Calling this method is optional. RFmxWLAN commits settings to the hardware when you call the Initiate(string, string) method. |
| ConfigureChannelBandwidth(string, double) | Configures the channel bandwidth. |
| ConfigureDigitalEdgeTrigger(string, string, RFmxWlanMXDigitalEdgeTriggerEdge, double, bool) | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. On a MIMO session, this VI configures the digital edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port. Spectral measurements are sometimes implemented with multiple acquisitions and therefore will require that digital triggers are sent for each acquisition. Multiple factors, including the desired span versus the realtime bandwidth of the hardware, affect the number of acquisitions. RFmx recommends repeating the generation until the measurement is completed in order to ensure that all the acquisitions are triggered. |
| ConfigureExternalAttenuation(string, double) | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure external attenuation for each port. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| ConfigureFrequency(string, double) | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. On a MIMO session, use "segment(n)" as the selector string to configure this method. |
| ConfigureFrequencyArray(string, double[]) | Configures a list of expected carrier frequencies of the RF signal to acquire. The signal analyzers tune to these frequencies based on the value you configure for the SetNumberOfFrequencySegments(string, int) method. |
| ConfigureIQPowerEdgeTrigger(string, string, RFmxWlanMXIQPowerEdgeTriggerSlope, double, double, RFmxWlanMXTriggerMinimumQuietTimeMode, double, RFmxWlanMXIQPowerEdgeTriggerLevelType, bool) | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. On a MIMO session, configures the IQ Power edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst. |
| ConfigureNumberOfFrequencySegmentsAndReceiveChains(string, int, int) | Configures the number of frequency segments and receive chains. |
| ConfigureReferenceLevel(string, double) | Configures the reference level, which represents the maximum expected power of an RF input signal. On a MIMO session, use "port::(deviceName)/(channelNumber)" as the selector string to configure reference level for each port. |
| ConfigureSelectedPortsMultiple(string, string[]) | Configures the selected ports to each segment/chain based on the values you set in SetNumberOfFrequencySegments(string, int) and SetNumberOfReceiveChains(string, int) methods. |
| ConfigureSoftwareEdgeTrigger(string, double, bool) | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| ConfigureStandard(string, RFmxWlanMXStandard) | Configures the IEEE 802.11 standard for the signal under analysis. |
| DeleteSignalConfiguration() | Deletes an instance of a signal. |
| DisableTrigger(string) | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
| Dispose() | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
| GetAllNamedResultNames(string, out string[], out bool) | Gets the named result names of the signal that you specify in the selectorString parameter. |
| GetAttributeBool(string, int, out bool) | Gets the value of a Bool attribute. |
| GetAttributeDouble(string, int, out double) | Gets the value of a Double attribute. |
| GetAttributeInt(string, int, out int) | Gets the value of an RFmx 32-bit integer (int32) attribute. |
| GetAttributeLong(string, int, out long) | Gets the value of an RFmx 64-bit integer (int64) attribute. |
| GetAttributeString(string, int, out string) | Gets the value of a of an RFmx string. |
| GetAutoLevelInitialReferenceLevel(string, out double) | Gets the initial reference level which the AutoLevel(string, double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| GetCenterFrequency(string, out double) | Gets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. On a MIMO session, use segment(n) along with a named or default signal instance as the selector string to configure this method. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| GetChannelBandwidth(string, out double) | Gets the channel spacing as defined under section 3.1 of IEEE Standard 802.11–2016 (pp. 130) . This value is specified in Hz. |
| GetDetectedBurstLength(string, out double) | Gets the duration of the packet detected by the AutoDetectSignal(string, double) function. The value is expressed in seconds. |
| GetDetectedChannelBandwidth(string, out double) | Gets the channel bandwidth detected by the AutoDetectSignal(string, double) . The value is expressed in Hz. |
| GetDetectedStandard(string, out int) | This method is obsoleted. Use NationalInstruments.RFmx.WlanMX.RFmxWlanMX.GetDetectedStandard(string,NationalInstruments.RFmx.WlanMX.RFmxWlanMXStandard@) instead. |
| GetDetectedStandard(string, out RFmxWlanMXStandard) | Gets the standard detected by the AutoDetectSignal(string, double) function. |
| GetDigitalEdgeTriggerEdge(string, out RFmxWlanMXDigitalEdgeTriggerEdge) | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . |
| GetDigitalEdgeTriggerSource(string, out string) | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is configured to "segment0/chain0" and is considered as the master port. |
| GetError(out int, out string) | Gets the latest error code and description. |
| GetErrorString(int, out string) | Converts the status code returned by an RFmxWLAN function into a string. |
| GetExternalAttenuation(string, out double) | Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help . On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| GetIQPowerEdgeTriggerLevel(string, out double) | Gets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxWlanMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute . |
| GetIQPowerEdgeTriggerLevelType(string, out RFmxWlanMXIQPowerEdgeTriggerLevelType) | Gets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . |
| GetIQPowerEdgeTriggerSlope(string, out RFmxWlanMXIQPowerEdgeTriggerSlope) | Gets whether the device asserts the trigger when the signal power is rising or falling. |
| GetIQPowerEdgeTriggerSource(string, out string) | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . On a MIMO session, configures the IQ Power edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port. |
| GetLimitedConfigurationChange(string, out RFmxWlanMXLimitedConfigurationChange) | Gets the set of properties that are considered by RFmx in the locked signal configuration state. |
| GetNumberOfFrequencySegments(string, out int) | Gets the number of frequency segments for 802.11ac and 802.11ax signals. |
| GetNumberOfReceiveChains(string, out int) | Gets the number of receive chains for OFDM standards. |
| GetOfdm2xLdpcEnabled(string, out RFmxWlanMXOfdm2xLdpcEnabled) | Gets whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. |
| GetOfdmAutoPhaseRotationDetectionEnabled(string, out RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled) | Gets whether to enable auto detection of phase rotation coefficients. |
| GetOfdmAutoPpduTypeDetectionEnabled(string, out RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) | Gets whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement. |
| GetOfdmDcmEnabled(string, out RFmxWlanMXOfdmDcmEnabled) | Gets whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. |
| GetOfdmDistributionBandwidth(string, out double) | Gets the bandwidth across which RU subcarriers are distributed, when you set >OFDM RU Type method to dRU. |
| GetOfdmEhtSigCompressionEnabled(string, out RFmxWlanMXOfdmEhtSigCompressionEnabled) |  |
| GetOfdmFecCodingType(string, out RFmxWlanMXOfdmFecCodingType) | Gets the type of forward error correction (FEC) coding used. |
| GetOfdmFrequencyBand(string, out RFmxWlanMXOfdmFrequencyBand) | Gets the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |
| GetOfdmFrequencySegmentIndex(string, out int) | Gets the frequency segment index to be analyzed in an 80+80 MHz 802.11ax signal. You must set this method to either of the valid values when you want to analyze one of the two segments. |
| GetOfdmGuardIntervalType(string, out RFmxWlanMXOfdmGuardIntervalType) | Gets the size of the guard interval of OFDM symbols. |
| GetOfdmHeaderDecodingEnabled(string, out RFmxWlanMXOfdmHeaderDecodingEnabled) | Gets whether to enable the decoding of the header fields in the PPDU. |
| GetOfdmIMPilotsEnabled(string, out RFmxWlanMXOfdmIMPilotsEnabled) | Gets whether inteference mitigating pilots are present in 802.11bn MU PPDU signals. |
| GetOfdmLdpcExtraSymbolSegment(string, out int) | Gets the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU. |
| GetOfdmLtfSize(string, out RFmxWlanMXOfdmLtfSize) | Gets the LTF symbol size. This method is applicable only for 802.11ax, 802.11be, and 802.11bn signals. |
| GetOfdmMcsIndex(string, out int) | Gets the modulation and coding scheme (MCS) index or the data rate when you set the SetOfdmHeaderDecodingEnabled(string, RFmxWlanMXOfdmHeaderDecodingEnabled) method to False . |
| GetOfdmMUMimoLtfModeEnabled(string, out RFmxWlanMXOfdmMUMimoLtfModeEnabled) | Gets whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. |
| GetOfdmNumberOfEhtSigSymbols(string, out int) |  |
| GetOfdmNumberOfHESigBSymbols(string, out int) | Gets the number of HE-SIG-B symbols. |
| GetOfdmNumberOfLtfSymbols(string, out int) | Gets the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. |
| GetOfdmNumberOfSigSymbols(string, out int) | Gets the number of SIG symbols. This method is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. |
| GetOfdmNumberOfSpaceTimeStreams(string, out int) | Gets the number of space time streams. This method is applicable when you set the OFDMHeaderDecodingEnabled method to False for 802.11n, 802.11ac, 802.11ax, and 802.11be standards or when PPDU Type is TB for 802.11ax, 802.11be, or 802.11bn standards. |
| GetOfdmNumberOfUsers(string, out int) | Gets the number of users in a multi-user (MU) PPDU. |
| GetOfdmPEDisambiguity(string, out int) | Gets the packet extension disambiguity information. |
| GetOfdmPhaseRotationCoefficient1(string, out RFmxWlanMXOfdmPhaseRotationCoefficient1) | Gets the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0 . |
| GetOfdmPhaseRotationCoefficient2(string, out RFmxWlanMXOfdmPhaseRotationCoefficient2) | Gets the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0 . |
| GetOfdmPhaseRotationCoefficient3(string, out RFmxWlanMXOfdmPhaseRotationCoefficient3) | Gets the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 . |
| GetOfdmPpduType(string, out RFmxWlanMXOfdmPpduType) | Gets the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . |
| GetOfdmPreamblePuncturingBitmap(string, out long) | Gets the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits. |
| GetOfdmPreamblePuncturingEnabled(string, out RFmxWlanMXOfdmPreamblePuncturingEnabled) | Gets whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured. |
| GetOfdmPreFecPaddingFactor(string, out int) | Gets the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. |
| GetOfdmRUOffsetMruIndex(string, out int) | Gets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of IEEE P802.11bn/D1.3 . |
| GetOfdmRUSize(string, out int) | Gets the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals. |
| GetOfdmRUType(string, out RFmxWlanMXOfdmRUType) | Gets whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). |
| GetOfdmScramblerSeed(string, out int) | Gets the scrambler seed for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
| GetOfdmSigCompressionEnabled(string, out RFmxWlanMXOfdmSigCompressionEnabled) | Gets whether to enable SIG compression. This method is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. |
| GetOfdmSpaceTimeStreamOffset(string, out int) | Gets the space time stream offset. |
| GetOfdmStbcEnabled(string, out RFmxWlanMXOfdmStbcEnabled) | Gets whether space-time block coding is enabled. This method is applicable only for 802.11ax TB PPDU. |
| GetOfdmTransmitPowerClass(string, out RFmxWlanMXOfdmTransmitPowerClass) | Gets the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11p . |
| GetOfdmUnequalModulationEnabled(string, out RFmxWlanMXOfdmUnequalModulationEnabled) | Gets whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals. |
| GetOfdmUnequalModulationPatternIndex(string, out int) | Gets the unequal modulation pattern for the user. Valid values are between 0 and number of space time streams-1. |
| GetReferenceLevel(string, out double) | Gets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| GetReferenceLevelHeadroom(string, out double) | Gets the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
| GetResultFetchTimeout(string, out double) | Gets the time, in seconds, to wait before results are available in the RFmxWLAN_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete. |
| GetSampleClockRateFactor(string, out double) | Gets the factor by which the sample clock rate is multiplied at the transmitter to generate a signal compressed in the frequency domain and expanded in the time domain. |
| GetSelectedPorts(string, out string) | Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| GetStandard(string, out RFmxWlanMXStandard) | Gets the signal under analysis as defined in IEEE Standard 802.11 . |
| GetTriggerDelay(string, out double) | Gets the trigger delay time. This value is expressed in seconds. |
| GetTriggerGateEnabled(string, out RFmxWlanMXTriggerGateEnabled) | Enables time-domain gating of the acquired signal for SEM measurement. |
| GetTriggerGateLength(string, out double) | Gets the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled) method to True . |
| GetTriggerMinimumQuietTimeDuration(string, out double) | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| GetTriggerMinimumQuietTimeMode(string, out RFmxWlanMXTriggerMinimumQuietTimeMode) | Gets whether the measurement computes the minimum quiet time used for triggering. |
| GetTriggerType(string, out RFmxWlanMXTriggerType) | Gets the trigger type. |
| GetWarning(out int, out string) | Gets the latest warning code and description. |
| Initiate(string, string) | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the property node. To get the status of measurements, use the WaitForMeasurementComplete(string, double) method or CheckMeasurementStatus(string, out bool) method. |
| ResetAttribute(string, RFmxWlanMXPropertyId) | Resets the attribute to its default value. |
| ResetToDefault(string) | Resets a signal to the default values. |
| SelectMeasurements(string, RFmxWlanMXMeasurementTypes, bool) | Specifies the measurements that you want to enable. |
| SendSoftwareEdgeTrigger() | Sends a trigger to the device when you use the RFmxWLAN_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. |
| SetAttributeBool(string, int, bool) | Sets the value of a Bool attribute. |
| SetAttributeDouble(string, int, double) | Sets the value of a Double attribute. |
| SetAttributeInt(string, int, int) | Sets the value of a Int attribute. |
| SetAttributeLong(string, int, long) | Sets the value of a Long attribute. |
| SetAttributeString(string, int, string) | Sets the value of a String attribute. |
| SetAutoLevelInitialReferenceLevel(string, double) | Sets the initial reference level which the AutoLevel(string, double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| SetCenterFrequency(string, double) | Sets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. On a MIMO session, use segment(n) along with a named or default signal instance as the selector string to configure this method. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| SetChannelBandwidth(string, double) | Sets the channel spacing as defined under section 3.1 of IEEE Standard 802.11–2016 (pp. 130) . This value is specified in Hz. |
| SetDigitalEdgeTriggerEdge(string, RFmxWlanMXDigitalEdgeTriggerEdge) | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . |
| SetDigitalEdgeTriggerSource(string, string) | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is configured to "segment0/chain0" and is considered as the master port. |
| SetExternalAttenuation(string, double) | Sets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help . On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| SetIQPowerEdgeTriggerLevel(string, double) | Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxWlanMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute . |
| SetIQPowerEdgeTriggerLevelType(string, RFmxWlanMXIQPowerEdgeTriggerLevelType) | Sets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . |
| SetIQPowerEdgeTriggerSlope(string, RFmxWlanMXIQPowerEdgeTriggerSlope) | Sets whether the device asserts the trigger when the signal power is rising or falling. |
| SetIQPowerEdgeTriggerSource(string, string) | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . On a MIMO session, configures the IQ Power edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port. |
| SetLimitedConfigurationChange(string, RFmxWlanMXLimitedConfigurationChange) | Sets the set of properties that are considered by RFmx in the locked signal configuration state. |
| SetNumberOfFrequencySegments(string, int) | Sets the number of frequency segments for 802.11ac and 802.11ax signals. |
| SetNumberOfReceiveChains(string, int) | Sets the number of receive chains for OFDM standards. |
| SetOfdm2xLdpcEnabled(string, RFmxWlanMXOfdm2xLdpcEnabled) | Sets whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. |
| SetOfdmAutoPhaseRotationDetectionEnabled(string, RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled) | Sets whether to enable auto detection of phase rotation coefficients. |
| SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) | Sets whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement. |
| SetOfdmDcmEnabled(string, RFmxWlanMXOfdmDcmEnabled) | Sets whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. |
| SetOfdmDistributionBandwidth(string, double) | Sets the bandwidth across which RU subcarriers are distributed, when you set >OFDM RU Type method to dRU. |
| SetOfdmEhtSigCompressionEnabled(string, RFmxWlanMXOfdmEhtSigCompressionEnabled) |  |
| SetOfdmFecCodingType(string, RFmxWlanMXOfdmFecCodingType) | Sets the type of forward error correction (FEC) coding used. |
| SetOfdmFrequencyBand(string, RFmxWlanMXOfdmFrequencyBand) | Sets the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |
| SetOfdmFrequencySegmentIndex(string, int) | Sets the frequency segment index to be analyzed in an 80+80 MHz 802.11ax signal. You must set this method to either of the valid values when you want to analyze one of the two segments. |
| SetOfdmGuardIntervalType(string, RFmxWlanMXOfdmGuardIntervalType) | Sets the size of the guard interval of OFDM symbols. |
| SetOfdmHeaderDecodingEnabled(string, RFmxWlanMXOfdmHeaderDecodingEnabled) | Sets whether to enable the decoding of the header fields in the PPDU. |
| SetOfdmIMPilotsEnabled(string, RFmxWlanMXOfdmIMPilotsEnabled) | Sets whether inteference mitigating pilots are present in 802.11bn MU PPDU signals. |
| SetOfdmLdpcExtraSymbolSegment(string, int) | Sets the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU. |
| SetOfdmLtfSize(string, RFmxWlanMXOfdmLtfSize) | Sets the LTF symbol size. This method is applicable only for 802.11ax, 802.11be, and 802.11bn signals. For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False. |
| SetOfdmMcsIndex(string, int) | Sets the modulation and coding scheme (MCS) index or the data rate when you set the SetOfdmHeaderDecodingEnabled(string, RFmxWlanMXOfdmHeaderDecodingEnabled) method to False . |
| SetOfdmMUMimoLtfModeEnabled(string, RFmxWlanMXOfdmMUMimoLtfModeEnabled) | Sets whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. |
| SetOfdmNumberOfEhtSigSymbols(string, int) |  |
| SetOfdmNumberOfHESigBSymbols(string, int) | Sets the number of HE-SIG-B symbols. |
| SetOfdmNumberOfLtfSymbols(string, int) | Sets the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. |
| SetOfdmNumberOfSigSymbols(string, int) | Sets the number of SIG symbols. This method is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. |
| SetOfdmNumberOfSpaceTimeStreams(string, int) | Sets the number of space time streams. This method is applicable when you set the OFDMHeaderDecodingEnabled method to False for 802.11n, 802.11ac, 802.11ax, and 802.11be standards or when PPDU Type is TB for 802.11ax, 802.11be, or 802.11bn standards. |
| SetOfdmNumberOfUsers(string, int) | Sets the number of users in a multi-user (MU) PPDU. |
| SetOfdmPEDisambiguity(string, int) | Sets the packet extension disambiguity information. |
| SetOfdmPhaseRotationCoefficient1(string, RFmxWlanMXOfdmPhaseRotationCoefficient1) | Sets the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0 . |
| SetOfdmPhaseRotationCoefficient2(string, RFmxWlanMXOfdmPhaseRotationCoefficient2) | Sets the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0 . |
| SetOfdmPhaseRotationCoefficient3(string, RFmxWlanMXOfdmPhaseRotationCoefficient3) | Sets the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 . |
| SetOfdmPpduType(string, RFmxWlanMXOfdmPpduType) | Sets the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . |
| SetOfdmPreamblePuncturingBitmap(string, long) | Sets the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits. |
| SetOfdmPreamblePuncturingEnabled(string, RFmxWlanMXOfdmPreamblePuncturingEnabled) | Sets whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured. |
| SetOfdmPreFecPaddingFactor(string, int) | Sets the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. |
| SetOfdmRUOffsetMruIndex(string, int) | Sets the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of IEEE P802.11bn/D1.3 . |
| SetOfdmRUSize(string, int) | Sets the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals. |
| SetOfdmRUType(string, RFmxWlanMXOfdmRUType) | Sets whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). |
| SetOfdmScramblerSeed(string, int) | Sets the scrambler seed for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
| SetOfdmSigCompressionEnabled(string, RFmxWlanMXOfdmSigCompressionEnabled) | Sets whether to enable SIG compression. This method is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. |
| SetOfdmSpaceTimeStreamOffset(string, int) | Sets the space time stream offset. |
| SetOfdmStbcEnabled(string, RFmxWlanMXOfdmStbcEnabled) | Sets whether space-time block coding is enabled. This method is applicable only for 802.11ax TB PPDU. |
| SetOfdmTransmitPowerClass(string, RFmxWlanMXOfdmTransmitPowerClass) | Sets the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11p . |
| SetOfdmUnequalModulationEnabled(string, RFmxWlanMXOfdmUnequalModulationEnabled) | Sets whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals. |
| SetOfdmUnequalModulationPatternIndex(string, int) | Sets the unequal modulation pattern for the user. Valid values are between 0 and number of space time streams-1. |
| SetReferenceLevel(string, double) | Sets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| SetReferenceLevelHeadroom(string, double) | Sets the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
| SetResultFetchTimeout(string, double) | Sets the time, in seconds, to wait before results are available in the RFmxWLAN_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete. |
| SetSampleClockRateFactor(string, double) | Sets the factor by which the sample clock rate is multiplied at the transmitter to generate a signal compressed in the frequency domain and expanded in the time domain. For example, a 40 MHz signal can be compressed to 20 MHz in the frequency domain if the sample clock rate is reduced to half at the transmitter. In this case, you must set this method to 0.5 to demodulate the signal. |
| SetSelectedPorts(string, string) | Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. On a MIMO session, this method specifies one of the initialized devices. Use "port::deviceName/channelNumber" as the format for the selected port. To perform a MIMO measurement, you must configure the selected ports method for the configured number of segments and chains. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::deviceName/channelNumber/instrPort". Example:port::myrfsa1/0/if1 |
| SetStandard(string, RFmxWlanMXStandard) | Sets the signal under analysis as defined in IEEE Standard 802.11 . |
| SetTriggerDelay(string, double) | Sets the trigger delay time. This value is expressed in seconds. |
| SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled) | Enables time-domain gating of the acquired signal for SEM measurement. |
| SetTriggerGateLength(string, double) | Sets the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled) method to True . |
| SetTriggerMinimumQuietTimeDuration(string, double) | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| SetTriggerMinimumQuietTimeMode(string, RFmxWlanMXTriggerMinimumQuietTimeMode) | Sets whether the measurement computes the minimum quiet time used for triggering. |
| SetTriggerType(string, RFmxWlanMXTriggerType) | Sets the trigger type. |
| WaitForMeasurementComplete(string, double) | Waits for the specified number for seconds for all the measurements to complete. |
| BuildChainString(string, int) | Creates a chain string. |
| BuildGateString(string, int) | Creates the gate string to use as the selector string. |
| BuildOffsetString(string, int) | Creates the offset string to use as the selector string. |
| BuildResultString(string) | Creates selector string for use with configuration or fetch. |
| BuildSegmentString(string, int) | Creates a segment string. |
| BuildStreamString(string, int) | Creates the stream string. |
| BuildUserString(string, int) | Creates the user string to use as the selector string. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pfi0.html language=enus -->
## TOPIC 00038: Pfi0

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pfi0.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PFI 0. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string Pfi0

### Pfi0

The signal is exported to the PFI 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string Pfi0

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pfi1.html language=enus -->
## TOPIC 00039: Pfi1

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pfi1.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI 1. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string Pfi1

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00040: PxieDStarBLine

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxiedstarbline.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxieDStarBLine

### PxieDStarBLine

The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxieDStarBLine

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxistarline.html language=enus -->
## TOPIC 00041: PxiStarLine

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxistarline.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI star trigger line. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiStarLine

### PxiStarLine

The signal is exported to the PXI star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiStarLine

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline0.html language=enus -->
## TOPIC 00042: PxiTriggerLine0

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline0.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine0

### PxiTriggerLine0

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine0

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00043: PxiTriggerLine1

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline1.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

The signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00044: PxiTriggerLine2

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline2.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

The signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00045: PxiTriggerLine3

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline3.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

The signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline4.html language=enus -->
## TOPIC 00046: PxiTriggerLine4

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline4.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine4

### PxiTriggerLine4

The signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine4

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00047: PxiTriggerLine5

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline5.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00048: PxiTriggerLine6

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline6.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00049: PxiTriggerLine7

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-pxitriggerline7.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-timerevent.html language=enus -->
## TOPIC 00050: TimerEvent

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants-timerevent.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public const string TimerEvent

Parent topic:

RFmxWlanMXConstants Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants.html language=enus -->
## TOPIC 00051: RFmxWlanMXConstants Class

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxconstants.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic class RFmxWlanMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 0. Pfi1The signal is exported to the PXI 1. PulseI

### RFmxWlanMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public class RFmxWlanMXConstants

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

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00052: RFmxWlanMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdigitaledgetriggeredge.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asserts

### RFmxWlanMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxWlanMXTriggerType)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggertype.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc-configuration.html language=enus -->
## TOPIC 00053: Configuration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc-configuration.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWlanMXDsssModAccConfiguration instance that provides methods to configure the DSSSModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic RFmxWlanMXDsssModAccConfiguration Configuration { get; }

### Configuration

Gets the [RFmxWlanMXDsssModAccConfiguration](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration.html) instance that provides methods to configure the DSSSModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public [RFmxWlanMXDsssModAccConfiguration](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration.html) Configuration { get; }

Parent topic:

RFmxWlanMXDsssModAcc Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc-results.html language=enus -->
## TOPIC 00054: Results

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc-results.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWlanMXDsssModAccResults instance that provides methods to fetch and read the DSSSModAcc measurement results. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic RFmxWlanMXDsssModAccResults Results { get; }

### Results

Gets the [RFmxWlanMXDsssModAccResults](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults.html) instance that provides methods to fetch and read the DSSSModAcc measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public [RFmxWlanMXDsssModAccResults](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults.html) Results { get; }

Parent topic:

RFmxWlanMXDsssModAcc Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc.html language=enus -->
## TOPIC 00055: RFmxWlanMXDsssModAcc Class

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodacc.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the DSSSModAcc measurement. Derives fromRFmxWlanMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic class RFmxWlanMXDsssModAcc : RFmxWlanMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxWlanMXDsssModAccConfiguration instance that provides methods to configure th

### RFmxWlanMXDsssModAcc Class

Represents the DSSSModAcc measurement.

#### Derives from

- RFmxWlanMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public class RFmxWlanMXDsssModAcc : RFmxWlanMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxWlanMXDsssModAccConfiguration instance that provides methods to configure the DSSSModAcc measurement. |
| Results | Gets the RFmxWlanMXDsssModAccResults instance that provides methods to fetch and read the DSSSModAcc measurement results. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccacquisitionlengthmode.html language=enus -->
## TOPIC 00056: RFmxWlanMXDsssModAccAcquisitionLengthMode Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccacquisitionlengthmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccacquisitionlengthmode.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccAcquisitionLengthModeMembersNameValueDescriptionManual0Uses the acquisition length specified

### RFmxWlanMXDsssModAccAcquisitionLengthMode Enumeration

Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccAcquisitionLengthMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | Uses the acquisition length specified by the SetAcquisitionLength(string, double) method. |
| Auto | 1 | Computes the acquisition length based on the SetMeasurementOffset(string, int) method and the SetMaximumMeasurementLength(string, int) method. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccaveragingenabled.html language=enus -->
## TOPIC 00057: RFmxWlanMXDsssModAccAveragingEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccaveragingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for DSSSModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccAveragingEnabledMembersNameValueDescriptionFalse0Performs measurement on a single acquisition. True1Measurement uses the SetAveragingCount(string, int) me

### RFmxWlanMXDsssModAccAveragingEnabled Enumeration

Specifies whether to enable averaging for DSSSModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Performs measurement on a single acquisition. |
| True | 1 | Measurement uses the SetAveragingCount(string, int) method for the number of acquisitions using which the results are averaged. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccburststartdetectionenabled.html language=enus -->
## TOPIC 00058: RFmxWlanMXDsssModAccBurstStartDetectionEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccburststartdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccburststartdetectionenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement detects the rising edge of a burst in the acquired waveform. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccBurstStartDetectionEnabledMembersNameValueDescriptionFalse0Disables detection of a rising edge of the burst in the acquired w

### RFmxWlanMXDsssModAccBurstStartDetectionEnabled Enumeration

Specifies whether the measurement detects the rising edge of a burst in the acquired waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccBurstStartDetectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables detection of a rising edge of the burst in the acquired waveform for measurement. |
| True | 1 | Enables detection of a rising edge of the burst in the acquired waveform for measurement. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccchipclockerrorcorrectionenabled.html language=enus -->
## TOPIC 00059: RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccchipclockerrorcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccchipclockerrorcorrectionenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable chip clock error correction. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabledMembersNameValueDescriptionFalse0Disables the chip clock error correction. True1Enables the chip clock error correction.

### RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled Enumeration

Specifies whether to enable chip clock error correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the chip clock error correction. |
| True | 1 | Enables the chip clock error correction. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureacquisitionlength__string-rfmxwlanmxdsssmodaccacquisitionlengthmode-double.html language=enus -->
## TOPIC 00060: ConfigureAcquisitionLength(string, RFmxWlanMXDsssModAccAcquisitionLengthMode, double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureacquisitionlength__string-rfmxwlanmxdsssmodaccacquisitionlengthmode-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureacquisitionlength__string-rfmxwlanmxdsssmodaccacquisitionlengthmode-double.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the acquisitionLength parameter and the acquisitionLengthMode parameter of the acquired waveform for the measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ConfigureAcquisitionLength(string selectorString, RFmxWlanMXDsssModAccAcquisitionLengthMode acquisitionLengthMod

### ConfigureAcquisitionLength(string, RFmxWlanMXDsssModAccAcquisitionLengthMode, double)

Configures the *acquisitionLength* parameter and the *acquisitionLengthMode* parameter of the acquired waveform for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ConfigureAcquisitionLength(string selectorString, RFmxWlanMXDsssModAccAcquisitionLengthMode acquisitionLengthMode, double acquisitionLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| acquisitionLengthMode | RFmxWlanMXDsssModAccAcquisitionLengthMode | Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc methods. |
| acquisitionLength | double | Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the acquisitionLengthMode parameter to Manual . This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureaveraging__string-rfmxwlanmxdsssmodaccaveragingenabled-int.html language=enus -->
## TOPIC 00061: ConfigureAveraging(string, RFmxWlanMXDsssModAccAveragingEnabled, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureaveraging__string-rfmxwlanmxdsssmodaccaveragingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureaveraging__string-rfmxwlanmxdsssmodaccaveragingenabled-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ConfigureAveraging(string selectorString, RFmxWlanMXDsssModAccAveragingEnabled averagingEnabled, int averagingCount)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal n

### ConfigureAveraging(string, RFmxWlanMXDsssModAccAveragingEnabled, int)

Configures averaging for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ConfigureAveraging(string selectorString, RFmxWlanMXDsssModAccAveragingEnabled averagingEnabled, int averagingCount)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxWlanMXDsssModAccAveragingEnabled | Specifies whether to enable averaging for DSSSModAcc measurements. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureevmunit__string-rfmxwlanmxdsssmodaccevmunit.html language=enus -->
## TOPIC 00062: ConfigureEvmUnit(string, RFmxWlanMXDsssModAccEvmUnit)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureevmunit__string-rfmxwlanmxdsssmodaccevmunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-configureevmunit__string-rfmxwlanmxdsssmodaccevmunit.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures EVM unit for the measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ConfigureEvmUnit(string selectorString, RFmxWlanMXDsssModAccEvmUnit evmUnit)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the sign

### ConfigureEvmUnit(string, RFmxWlanMXDsssModAccEvmUnit)

Configures EVM unit for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ConfigureEvmUnit(string selectorString, RFmxWlanMXDsssModAccEvmUnit evmUnit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| evmUnit | RFmxWlanMXDsssModAccEvmUnit | Specifies the unit for the EVM results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getdatadecodingenabled__string-out.html language=enus -->
## TOPIC 00063: GetDataDecodingEnabled(string, out RFmxWlanMXDsssModAccDataDecodingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getdatadecodingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getdatadecodingenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetDataDecodingEnabled(string selectorString, out RFmxWlanMXDsssModAccDataDecodingEnabled value)RemarksThis method gets the value of DsssModAcc

### GetDataDecodingEnabled(string, out RFmxWlanMXDsssModAccDataDecodingEnabled)

Gets whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetDataDecodingEnabled(string selectorString, out RFmxWlanMXDsssModAccDataDecodingEnabled value)

#### Remarks

This method gets the value of [DsssModAccDataDecodingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccdatadecodingenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXDsssModAccDataDecodingEnabled | Upon return, contains whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getequalizationenabled__string-out.html language=enus -->
## TOPIC 00064: GetEqualizationEnabled(string, out RFmxWlanMXDsssModAccEqualizationEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getequalizationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getequalizationenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetEqualizationEnabled(string selectorS

### GetEqualizationEnabled(string, out RFmxWlanMXDsssModAccEqualizationEnabled)

Gets whether to enable equalization. The *IEEE Standard 802.11-2016* does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetEqualizationEnabled(string selectorString, out RFmxWlanMXDsssModAccEqualizationEnabled value)

#### Remarks

This method gets the value of [DsssModAccEqualizationEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccequalizationenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXDsssModAccEqualizationEnabled | Upon return, contains whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getfrequencyerrorcorrectionenabled__string-out.html language=enus -->
## TOPIC 00065: GetFrequencyErrorCorrectionEnabled(string, out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getfrequencyerrorcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getfrequencyerrorcorrectionenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable frequency error correction. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetFrequencyErrorCorrectionEnabled(string selectorString, out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled value)RemarksThis method gets the value of DsssModAccFrequencyErrorCorrectio

### GetFrequencyErrorCorrectionEnabled(string, out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled)

Gets whether to enable frequency error correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetFrequencyErrorCorrectionEnabled(string selectorString, out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled value)

#### Remarks

This method gets the value of [DsssModAccFrequencyErrorCorrectionEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccfrequencyerrorcorrectionenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled | Upon return, contains whether to enable frequency error correction. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getpowercustomgatestarttime__string-out.html language=enus -->
## TOPIC 00066: GetPowerCustomGateStartTime(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getpowercustomgatestarttime__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getpowercustomgatestarttime__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start time of the custom power gate. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetPowerCustomGateStartTime(string selectorString, out double value)RemarksThis method gets the value of DsssModAccPowerCustomGateStartTime attribute.A value o

### GetPowerCustomGateStartTime(string, out double)

Gets the start time of the custom power gate. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetPowerCustomGateStartTime(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccPowerCustomGateStartTime](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.A value of 0 indicates that the start time is the start of the PPDU. The default value is 0 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the gate number. Example: "gate0". You can use the BuildGateString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the start time of the custom power gate. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getpowermeasurementenabled__string-out.html language=enus -->
## TOPIC 00067: GetPowerMeasurementEnabled(string, out RFmxWlanMXDsssModAccPowerMeasurementEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getpowermeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-getpowermeasurementenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether power measurement is performed. This measurement computes power of various fields in the PPDU. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetPowerMeasurementEnabled(string selectorString, out RFmxWlanMXDsssModAccPowerMeasurementEnabled value)RemarksThis method gets the v

### GetPowerMeasurementEnabled(string, out RFmxWlanMXDsssModAccPowerMeasurementEnabled)

Gets whether power measurement is performed. This measurement computes power of various fields in the PPDU.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetPowerMeasurementEnabled(string selectorString, out RFmxWlanMXDsssModAccPowerMeasurementEnabled value)

#### Remarks

This method gets the value of [DsssModAccPowerMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpowermeasurementenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXDsssModAccPowerMeasurementEnabled | Upon return, contains whether power measurement is performed. This measurement computes power of various fields in the PPDU. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setacquisitionlengthmode__string-rfmxwlanmxdsssmodaccacquisitionlengthmode.html language=enus -->
## TOPIC 00068: SetAcquisitionLengthMode(string, RFmxWlanMXDsssModAccAcquisitionLengthMode)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setacquisitionlengthmode__string-rfmxwlanmxdsssmodaccacquisitionlengthmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setacquisitionlengthmode__string-rfmxwlanmxdsssmodaccacquisitionlengthmode.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetAcquisitionLengthMode(string selectorString, RFmxWlanMXDsssModAccAcquisitionLengthMode value)RemarksThis method set

### SetAcquisitionLengthMode(string, RFmxWlanMXDsssModAccAcquisitionLengthMode)

Sets whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetAcquisitionLengthMode(string selectorString, RFmxWlanMXDsssModAccAcquisitionLengthMode value)

#### Remarks

This method sets the value of [DsssModAccAcquisitionLengthMode](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccacquisitionlengthmode.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXDsssModAccAcquisitionLengthMode | Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setdatadecodingenabled__string-rfmxwlanmxdsssmodaccdatadecodingenabled.html language=enus -->
## TOPIC 00069: SetDataDecodingEnabled(string, RFmxWlanMXDsssModAccDataDecodingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setdatadecodingenabled__string-rfmxwlanmxdsssmodaccdatadecodingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setdatadecodingenabled__string-rfmxwlanmxdsssmodaccdatadecodingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetDataDecodingEnabled(string selectorString, RFmxWlanMXDsssModAccDataDecodingEnabled value)RemarksThis method sets the value of DsssModAccData

### SetDataDecodingEnabled(string, RFmxWlanMXDsssModAccDataDecodingEnabled)

Sets whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetDataDecodingEnabled(string selectorString, RFmxWlanMXDsssModAccDataDecodingEnabled value)

#### Remarks

This method sets the value of [DsssModAccDataDecodingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccdatadecodingenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXDsssModAccDataDecodingEnabled | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setequalizationenabled__string-rfmxwlanmxdsssmodaccequalizationenabled.html language=enus -->
## TOPIC 00070: SetEqualizationEnabled(string, RFmxWlanMXDsssModAccEqualizationEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setequalizationenabled__string-rfmxwlanmxdsssmodaccequalizationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setequalizationenabled__string-rfmxwlanmxdsssmodaccequalizationenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetEqualizationEnabled(string selectorS

### SetEqualizationEnabled(string, RFmxWlanMXDsssModAccEqualizationEnabled)

Sets whether to enable equalization. The *IEEE Standard 802.11-2016* does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetEqualizationEnabled(string selectorString, RFmxWlanMXDsssModAccEqualizationEnabled value)

#### Remarks

This method sets the value of [DsssModAccEqualizationEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccequalizationenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXDsssModAccEqualizationEnabled | Specifies whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setevmunit__string-rfmxwlanmxdsssmodaccevmunit.html language=enus -->
## TOPIC 00071: SetEvmUnit(string, RFmxWlanMXDsssModAccEvmUnit)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setevmunit__string-rfmxwlanmxdsssmodaccevmunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setevmunit__string-rfmxwlanmxdsssmodaccevmunit.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the unit for the EVM results. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetEvmUnit(string selectorString, RFmxWlanMXDsssModAccEvmUnit value)RemarksThis method sets the value of DsssModAccEvmUnit attribute.The default value is Percentage .ParametersNameTypeDescriptionselectorStr

### SetEvmUnit(string, RFmxWlanMXDsssModAccEvmUnit)

Sets the unit for the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetEvmUnit(string selectorString, RFmxWlanMXDsssModAccEvmUnit value)

#### Remarks

This method sets the value of [DsssModAccEvmUnit](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [Percentage](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccevmunit.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXDsssModAccEvmUnit | Specifies the unit for the EVM results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setpowercustomgatestoptime__string-double.html language=enus -->
## TOPIC 00072: SetPowerCustomGateStopTime(string, double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setpowercustomgatestoptime__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setpowercustomgatestoptime__string-double.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the stop time for the custom power gate. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetPowerCustomGateStopTime(string selectorString, double value)RemarksThis method sets the value of DsssModAccPowerCustomGateStopTime attribute.The default val

### SetPowerCustomGateStopTime(string, double)

Sets the stop time for the custom power gate. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetPowerCustomGateStopTime(string selectorString, double value)

#### Remarks

This method sets the value of [DsssModAccPowerCustomGateStopTime](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 10 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the gate number. Example: "gate0". You can use the BuildGateString(string, int) method to build the selector string. |
| value | double | Specifies the stop time for the custom power gate. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setspectruminverted__string-rfmxwlanmxdsssmodaccspectruminverted.html language=enus -->
## TOPIC 00073: SetSpectrumInverted(string, RFmxWlanMXDsssModAccSpectrumInverted)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setspectruminverted__string-rfmxwlanmxdsssmodaccspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration-setspectruminverted__string-rfmxwlanmxdsssmodaccspectruminverted.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the measured signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetSpectrumInverted(string selectorString, RFmxWlanMXDsssModAccSpectrumInverted value)RemarksThis method sets the value of DsssModAccSpectrumInverted attribute.The default value i

### SetSpectrumInverted(string, RFmxWlanMXDsssModAccSpectrumInverted)

Sets whether the spectrum of the measured signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetSpectrumInverted(string selectorString, RFmxWlanMXDsssModAccSpectrumInverted value)

#### Remarks

This method sets the value of [DsssModAccSpectrumInverted](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccspectruminverted.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXDsssModAccSpectrumInverted | Specifies whether the spectrum of the measured signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration.html language=enus -->
## TOPIC 00074: RFmxWlanMXDsssModAccConfiguration Class

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccconfiguration.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the DSSSModAcc measurement. Derives fromRFmxWlanMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic class RFmxWlanMXDsssModAccConfiguration : RFmxWlanMXSubObjectMethodsNameDescriptionConfigureAcquisitionLength(string, RFmxWlanMXDsssModAccAcquisitionLengthM

### RFmxWlanMXDsssModAccConfiguration Class

Provides methods to configure the DSSSModAcc measurement.

#### Derives from

- RFmxWlanMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public class RFmxWlanMXDsssModAccConfiguration : RFmxWlanMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAcquisitionLength(string, RFmxWlanMXDsssModAccAcquisitionLengthMode, double) | Configures the acquisitionLength parameter and the acquisitionLengthMode parameter of the acquired waveform for the measurement. |
| ConfigureAveraging(string, RFmxWlanMXDsssModAccAveragingEnabled, int) | Configures averaging for the measurement. |
| ConfigureEvmUnit(string, RFmxWlanMXDsssModAccEvmUnit) | Configures EVM unit for the measurement. |
| ConfigureMeasurementLength(string, int, int) | Configures the measurement offset and the maximum measurement length for the DSSSModAcc measurement. |
| ConfigurePowerMeasurementCustomGateArray(string, double[], double[]) | Configures the custom gate start and stop times for power measurement. |
| ConfigurePowerMeasurementEnabled(string, RFmxWlanMXDsssModAccPowerMeasurementEnabled) | Configures whether power measurement is enabled for the DSSSModAcc measurement. |
| ConfigurePowerMeasurementNumberOfCustomGates(string, int) | Configures the number of custom gates for power measurement. |
| GetAcquisitionLength(string, out double) | Gets the length of the waveform to be acquired for the DSSSModAcc measurement when you set the SetAcquisitionLengthMode(string, RFmxWlanMXDsssModAccAcquisitionLengthMode) method to Manual . This value is expressed in seconds. |
| GetAcquisitionLengthMode(string, out RFmxWlanMXDsssModAccAcquisitionLengthMode) | Gets whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable all the traces computed by DSSSModAcc measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXDsssModAccAveragingEnabled) method to True . |
| GetAveragingEnabled(string, out RFmxWlanMXDsssModAccAveragingEnabled) | Gets whether to enable averaging for DSSSModAcc measurement. |
| GetBurstStartDetectionEnabled(string, out RFmxWlanMXDsssModAccBurstStartDetectionEnabled) | Gets whether the measurement detects the rising edge of a burst in the acquired waveform. |
| GetChipClockErrorCorrectionEnabled(string, out RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled) | Gets whether to enable chip clock error correction. |
| GetDataDecodingEnabled(string, out RFmxWlanMXDsssModAccDataDecodingEnabled) | Gets whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
| GetEqualizationEnabled(string, out RFmxWlanMXDsssModAccEqualizationEnabled) | Gets whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |
| GetEvmUnit(string, out RFmxWlanMXDsssModAccEvmUnit) | Gets the unit for the EVM results. |
| GetFrequencyErrorCorrectionEnabled(string, out RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled) | Gets whether to enable frequency error correction. |
| GetIQOriginOffsetCorrectionEnabled(string, out RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled) | Gets whether to enable I/Q origin offset correction. |
| GetMaximumMeasurementLength(string, out int) | Gets the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016 . |
| GetMeasurementOffset(string, out int) | Gets the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for DSSSModAcc measurement. |
| GetPowerCustomGateStartTime(string, out double) | Gets the start time of the custom power gate. This value is expressed in seconds. |
| GetPowerCustomGateStopTime(string, out double) | Gets the stop time for the custom power gate. This value is expressed in seconds. |
| GetPowerMeasurementEnabled(string, out RFmxWlanMXDsssModAccPowerMeasurementEnabled) | Gets whether power measurement is performed. This measurement computes power of various fields in the PPDU. |
| GetPowerNumberOfCustomGates(string, out int) | Gets the number of custom gates used for power measurement. |
| GetPulseShapingFilterParameter(string, out double) | Gets the value of the filter roll-off when you set the Pulse Shaping Filter Type method to Raised Cosine or Root Raised Cosine. This method is ignored if you set the Pulse Shaping Filter Type method to Rectangular. |
| GetPulseShapingFilterType(string, out RFmxWlanMXDsssModAccPulseShapingFilterType) | Gets the type of pulse shaping filter used at the transmitter. This method is ignored when you set the SetEqualizationEnabled(string, RFmxWlanMXDsssModAccEqualizationEnabled) method to True . |
| GetSpectrumInverted(string, out RFmxWlanMXDsssModAccSpectrumInverted) | Gets whether the spectrum of the measured signal is inverted. |
| SetAcquisitionLength(string, double) | Sets the length of the waveform to be acquired for the DSSSModAcc measurement when you set the SetAcquisitionLengthMode(string, RFmxWlanMXDsssModAccAcquisitionLengthMode) method to Manual . This value is expressed in seconds. |
| SetAcquisitionLengthMode(string, RFmxWlanMXDsssModAccAcquisitionLengthMode) | Sets whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable all the traces computed by DSSSModAcc measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXDsssModAccAveragingEnabled) method to True . |
| SetAveragingEnabled(string, RFmxWlanMXDsssModAccAveragingEnabled) | Sets whether to enable averaging for DSSSModAcc measurement. |
| SetBurstStartDetectionEnabled(string, RFmxWlanMXDsssModAccBurstStartDetectionEnabled) | Sets whether the measurement detects the rising edge of a burst in the acquired waveform. |
| SetChipClockErrorCorrectionEnabled(string, RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled) | Sets whether to enable chip clock error correction. |
| SetDataDecodingEnabled(string, RFmxWlanMXDsssModAccDataDecodingEnabled) | Sets whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
| SetEqualizationEnabled(string, RFmxWlanMXDsssModAccEqualizationEnabled) | Sets whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |
| SetEvmUnit(string, RFmxWlanMXDsssModAccEvmUnit) | Sets the unit for the EVM results. |
| SetFrequencyErrorCorrectionEnabled(string, RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled) | Sets whether to enable frequency error correction. |
| SetIQOriginOffsetCorrectionEnabled(string, RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled) | Sets whether to enable I/Q origin offset correction. |
| SetMaximumMeasurementLength(string, int) | Sets the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016 . |
| SetMeasurementOffset(string, int) | Sets the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for DSSSModAcc measurement. |
| SetPowerCustomGateStartTime(string, double) | Sets the start time of the custom power gate. This value is expressed in seconds. |
| SetPowerCustomGateStopTime(string, double) | Sets the stop time for the custom power gate. This value is expressed in seconds. |
| SetPowerMeasurementEnabled(string, RFmxWlanMXDsssModAccPowerMeasurementEnabled) | Sets whether power measurement is performed. This measurement computes power of various fields in the PPDU. |
| SetPowerNumberOfCustomGates(string, int) | Sets the number of custom gates used for power measurement. |
| SetPulseShapingFilterParameter(string, double) | Sets the value of the filter roll-off when you set the Pulse Shaping Filter Type method to Raised Cosine or Root Raised Cosine. This method is ignored if you set the Pulse Shaping Filter Type method to Rectangular. |
| SetPulseShapingFilterType(string, RFmxWlanMXDsssModAccPulseShapingFilterType) | Sets the type of pulse shaping filter used at the transmitter. This method is ignored when you set the SetEqualizationEnabled(string, RFmxWlanMXDsssModAccEqualizationEnabled) method to True . |
| SetSpectrumInverted(string, RFmxWlanMXDsssModAccSpectrumInverted) | Sets whether the spectrum of the measured signal is inverted. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccdatadecodingenabled.html language=enus -->
## TOPIC 00075: RFmxWlanMXDsssModAccDataDecodingEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccdatadecodingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccdatadecodingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccDataDecodingEnabledMembersNameValueDescriptionFalse0Disables data decoding. True1Enables data decoding.

### RFmxWlanMXDsssModAccDataDecodingEnabled Enumeration

Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccDataDecodingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables data decoding. |
| True | 1 | Enables data decoding. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccevmunit.html language=enus -->
## TOPIC 00076: RFmxWlanMXDsssModAccEvmUnit Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccevmunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccevmunit.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for the EVM results. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccEvmUnitMembersNameValueDescriptionPercentage0Returns the EVM results as a percentage. dB1Returns the EVM results in dB.

### RFmxWlanMXDsssModAccEvmUnit Enumeration

Specifies the unit for the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccEvmUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Percentage | 0 | Returns the EVM results as a percentage. |
| dB | 1 | Returns the EVM results in dB. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpayloadheadercrcstatus.html language=enus -->
## TOPIC 00077: RFmxWlanMXDsssModAccPayloadHeaderCrcStatus Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpayloadheadercrcstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpayloadheadercrcstatus.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016 . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccPayloadHeaderCrcStatusMembersNameValueDescriptionFail0Returns that the header

### RFmxWlanMXDsssModAccPayloadHeaderCrcStatus Enumeration

Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of *IEEE Standard 802.11 2016* .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccPayloadHeaderCrcStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | Returns that the header CRC failed. |
| Pass | 1 | Returns that the header CRC passed. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpowermeasurementenabled.html language=enus -->
## TOPIC 00078: RFmxWlanMXDsssModAccPowerMeasurementEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpowermeasurementenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpowermeasurementenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccPowerMeasurementEnabledMembersNameValueDescriptionFalse0Disables power measurement. True1Enables power meas

### RFmxWlanMXDsssModAccPowerMeasurementEnabled Enumeration

Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccPowerMeasurementEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables power measurement. |
| True | 1 | Enables power measurement. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpreambletype.html language=enus -->
## TOPIC 00079: RFmxWlanMXDsssModAccPreambleType Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpreambletype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccpreambletype.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected preamble type of the acquired burst. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXDsssModAccPreambleTypeMembersNameValueDescriptionLong0Indicates that the PPDU has a long PHY preamble and header. Short1Indicates that the PPDU has a short PHY preamble and

### RFmxWlanMXDsssModAccPreambleType Enumeration

Returns the detected preamble type of the acquired burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXDsssModAccPreambleType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Long | 0 | Indicates that the PPDU has a long PHY preamble and header. |
| Short | 1 | Indicates that the PPDU has a short PHY preamble and header. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getchipclockerrormean__string-out.html language=enus -->
## TOPIC 00080: GetChipClockErrorMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getchipclockerrormean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getchipclockerrormean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the chip clock error of the transmitter. This value is expressed in parts per million (ppm). SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetChipClockErrorMean(string selectorString, out double value)RemarksThis method gets the value of DsssModAccResultsChipClockErrorMean attribut

### GetChipClockErrorMean(string, out double)

Gets the chip clock error of the transmitter. This value is expressed in parts per million (ppm).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetChipClockErrorMean(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsChipClockErrorMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the chip clock error of the transmitter. This value is expressed in parts per million (ppm). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getcustomgateaveragepowermean__string-out.html language=enus -->
## TOPIC 00081: GetCustomGateAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getcustomgateaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getcustomgateaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the custom gate. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetCustomGateAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of DsssModAccResultsCustomGateAveragePowerMean attribute.Param

### GetCustomGateAveragePowerMean(string, out double)

Gets the average power of the custom gate. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetCustomGateAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsCustomGateAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and gate number. Example: "gate0", "result::r1/gate0". You can use the BuildGateString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the custom gate. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getiqgainimbalancemean__string-out.html language=enus -->
## TOPIC 00082: GetIQGainImbalanceMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getiqgainimbalancemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getiqgainimbalancemean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q gain imbalance. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetIQGainImbalanceMean(string selectorString, out double value)RemarksThis method gets the value of DsssModAccResultsIQGainImbalanceMean attribute.ParametersNameTypeDescriptionselec

### GetIQGainImbalanceMean(string, out double)

Gets the I/Q gain imbalance. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetIQGainImbalanceMean(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsIQGainImbalanceMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q gain imbalance. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpeakevm802_11_2016maximum__string-out.html language=enus -->
## TOPIC 00083: GetPeakEvm802_11_2016Maximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpeakevm802_11_2016maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpeakevm802_11_2016maximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak EVM of the burst. This value is expressed as a percentage or in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetPeakEvm802_11_2016Maximum(string selectorString, out double value)RemarksThis method gets the value of DsssModAccResultsPeakEvm802_11_2016Maximum attribute.

### GetPeakEvm802_11_2016Maximum(string, out double)

Gets the peak EVM of the burst. This value is expressed as a percentage or in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetPeakEvm802_11_2016Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsPeakEvm802_11_2016Maximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak EVM of the burst. This value is expressed as a percentage or in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpreamblepeakpowermaximum__string-out.html language=enus -->
## TOPIC 00084: GetPreamblePeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpreamblepeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpreamblepeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the preamble field of the PPDU. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetPreamblePeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of DsssModAccResultsPreamblePeakPowerMaximum attribu

### GetPreamblePeakPowerMaximum(string, out double)

Gets the peak power of the preamble field of the PPDU. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetPreamblePeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsPreamblePeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak power of the preamble field of the PPDU. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpsducrcstatus__string-out.html language=enus -->
## TOPIC 00085: GetPsduCrcStatus(string, out RFmxWlanMXDsssModAccPsduCrcStatus)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpsducrcstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getpsducrcstatus__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetPsduCrcStatus(string selectorString, out RFmxWlanMXDsssModAccPsduCrcStatus value)RemarksThis method gets the value of Ds

### GetPsduCrcStatus(string, out RFmxWlanMXDsssModAccPsduCrcStatus)

Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetPsduCrcStatus(string selectorString, out RFmxWlanMXDsssModAccPsduCrcStatus value)

#### Remarks

This method gets the value of [DsssModAccResultsPsduCrcStatus](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, number and Signal number. Example: "Signal0", "result::r1/Signal0" or "result::r1/Signal0/0". |
| value | out RFmxWlanMXDsssModAccPsduCrcStatus | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getrmsmagnitudeerrormean__string-out.html language=enus -->
## TOPIC 00086: GetRmsMagnitudeErrorMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getrmsmagnitudeerrormean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getrmsmagnitudeerrormean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetRmsMagnitudeErrorMean(string selectorS

### GetRmsMagnitudeErrorMean(string, out double)

Gets the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetRmsMagnitudeErrorMean(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsRmsMagnitudeErrorMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getrmsphaseerrormean__string-out.html language=enus -->
## TOPIC 00087: GetRmsPhaseErrorMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getrmsphaseerrormean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxdsssmodaccresults-getrmsphaseerrormean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetRmsPhaseErrorMean

### GetRmsPhaseErrorMean(string, out double)

Gets the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetRmsPhaseErrorMean(string selectorString, out double value)

#### Remarks

This method gets the value of [DsssModAccResultsRmsPhaseErrorMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXDsssModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00088: RFmxWlanMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXIQPowerEdge

### RFmxWlanMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxWlanMXTriggerType)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-settriggertype__string-rfmxwlanmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtriggertype.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The IQ Power Edge Level method is relative to the value of the SetReferenceLevel(string, double) method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmautophaserotationdetectionenabled.html language=enus -->
## TOPIC 00089: RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmautophaserotationdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmautophaserotationdetectionenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables auto detection of phase rotation coefficients. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabledMembersNameValueDescriptionFalse0Specifies that auto detection of phase rotation coefficient is disabled. True1Specifies that auto detecti

### RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled Enumeration

Enables auto detection of phase rotation coefficients.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmAutoPhaseRotationDetectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that auto detection of phase rotation coefficient is disabled. |
| True | 1 | Specifies that auto detection of phase rotation coefficient is enabled. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmfeccodingtype.html language=enus -->
## TOPIC 00090: RFmxWlanMXOfdmFecCodingType Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmfeccodingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmfeccodingtype.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of forward error correction (FEC) coding used. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmFecCodingTypeMembersNameValueDescriptionBcc0The FEC coding type used is binary convolutional code (BCC). Ldpc1The FEC coding type used is low-density parity che

### RFmxWlanMXOfdmFecCodingType Enumeration

Specifies the type of forward error correction (FEC) coding used.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmFecCodingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Bcc | 0 | The FEC coding type used is binary convolutional code (BCC). |
| Ldpc | 1 | The FEC coding type used is low-density parity check (LDPC). |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccamplitudetrackingenabled.html language=enus -->
## TOPIC 00091: RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccamplitudetrackingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccamplitudetrackingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccAmplitudeTrackingEnabledMembersNameValueDescriptionFalse0Amplitude tracking is disabled. True1Amplitude tracking is enabled.

### RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled Enumeration

Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Amplitude tracking is disabled. |
| True | 1 | Amplitude tracking is enabled. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccautolevelallowoverflow.html language=enus -->
## TOPIC 00092: RFmxWlanMXOfdmModAccAutoLevelAllowOverflow Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccautolevelallowoverflow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccautolevelallowoverflow.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccAutoLevelAllowOverflowMembersNameValueDescriptionFalse0Disables searching for the optim

### RFmxWlanMXOfdmModAccAutoLevelAllowOverflow Enumeration

Specifies whether the [AutoLevel(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-autolevel__string-double.html) function should search for the optimum reference levels while allowing ADC overflow.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccAutoLevelAllowOverflow

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables searching for the optimum reference levels while allowing ADC overflow. |
| True | 1 | Enables searching for the optimum reference levels while allowing ADC overflow. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html language=enus -->
## TOPIC 00093: RFmxWlanMXOfdmModAccAveragingEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for OFDMModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement uses the value of the SetAver

### RFmxWlanMXOfdmModAccAveragingEnabled Enumeration

Specifies whether to enable averaging for OFDMModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement uses the value of the SetAveragingCount(string, int) method as the number of acquisitions over which the results are averaged. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-configureaveraging__string-rfmxwlanmxofdmmodaccaveragingenabled-int.html language=enus -->
## TOPIC 00094: ConfigureAveraging(string, RFmxWlanMXOfdmModAccAveragingEnabled, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-configureaveraging__string-rfmxwlanmxofdmmodaccaveragingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-configureaveraging__string-rfmxwlanmxofdmmodaccaveragingenabled-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ConfigureAveraging(string selectorString, RFmxWlanMXOfdmModAccAveragingEnabled averagingEnabled, int averagingCount)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal n

### ConfigureAveraging(string, RFmxWlanMXOfdmModAccAveragingEnabled, int)

Configures averaging for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ConfigureAveraging(string selectorString, RFmxWlanMXOfdmModAccAveragingEnabled averagingEnabled, int averagingCount)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxWlanMXOfdmModAccAveragingEnabled | Specifies whether to enable averaging for OFDMModAcc measurements. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-configurecommonclocksourceenabled__string-rfmxwlanmxofdmmodacccommonclocksourceenabled.html language=enus -->
## TOPIC 00095: ConfigureCommonClockSourceEnabled(string, RFmxWlanMXOfdmModAccCommonClockSourceEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-configurecommonclocksourceenabled__string-rfmxwlanmxofdmmodacccommonclocksourceenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-configurecommonclocksourceenabled__string-rfmxwlanmxofdmmodacccommonclocksourceenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the transmitter uses the same reference clock signal for generating the RF carrier and for the symbol clock. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ConfigureCommonClockSourceEnabled(string selectorString, RFmxWlanMXOfdmModAccCommonClockSourceEnabled commonClock

### ConfigureCommonClockSourceEnabled(string, RFmxWlanMXOfdmModAccCommonClockSourceEnabled)

Configures whether the transmitter uses the same reference clock signal for generating the RF carrier and for the symbol clock.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ConfigureCommonClockSourceEnabled(string selectorString, RFmxWlanMXOfdmModAccCommonClockSourceEnabled commonClockSourceEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| commonClockSourceEnabled | RFmxWlanMXOfdmModAccCommonClockSourceEnabled | Specifies if the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getautolevelallowoverflow__string-out.html language=enus -->
## TOPIC 00096: GetAutoLevelAllowOverflow(string, out RFmxWlanMXOfdmModAccAutoLevelAllowOverflow)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getautolevelallowoverflow__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getautolevelallowoverflow__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetAutoLevelAllowOverflow(string selectorString, out RFmxWlanMXOfdmModAccAutoLevelAllowOverflow value)RemarksThis

### GetAutoLevelAllowOverflow(string, out RFmxWlanMXOfdmModAccAutoLevelAllowOverflow)

Gets whether the [AutoLevel(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-autolevel__string-double.html) function should search for the optimum reference levels while allowing ADC overflow.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetAutoLevelAllowOverflow(string selectorString, out RFmxWlanMXOfdmModAccAutoLevelAllowOverflow value)

#### Remarks

This method gets the value of [OfdmModAccAutoLevelAllowOverflow](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccautolevelallowoverflow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmModAccAutoLevelAllowOverflow | Upon return, contains whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getchannelestimationltfaveragingenabled__string-out.html language=enus -->
## TOPIC 00097: GetChannelEstimationLtfAveragingEnabled(string, out RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getchannelestimationltfaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getchannelestimationltfaveragingenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetChannelEstimationLtfAveragingEnabled(string selectorString, out RFmxWlanMX

### GetChannelEstimationLtfAveragingEnabled(string, out RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled)

Gets whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetChannelEstimationLtfAveragingEnabled(string selectorString, out RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled value)

#### Remarks

This method gets the value of [OfdmModAccChannelEstimationLtfAveragingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccchannelestimationltfaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled | Upon return, contains whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getiqquadratureerrorcorrectionenabled__string-out.html language=enus -->
## TOPIC 00098: GetIQQuadratureErrorCorrectionEnabled(string, out RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getiqquadratureerrorcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getiqquadratureerrorcorrectionenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable I/Q quadrature error correction. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetIQQuadratureErrorCorrectionEnabled(string selectorString, out RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled value)RemarksThis method gets the value of OfdmModAccIQQuadrature

### GetIQQuadratureErrorCorrectionEnabled(string, out RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled)

Gets whether to enable I/Q quadrature error correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetIQQuadratureErrorCorrectionEnabled(string selectorString, out RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled value)

#### Remarks

This method gets the value of [OfdmModAccIQQuadratureErrorCorrectionEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodacciqquadratureerrorcorrectionenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled | Upon return, contains whether to enable I/Q quadrature error correction. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnoisecompensationinputpowercheckenabled__string-out.html language=enus -->
## TOPIC 00099: GetNoiseCompensationInputPowerCheckEnabled(string, out RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnoisecompensationinputpowercheckenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnoisecompensationinputpowercheckenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNoiseCompensationInputPowerCheckEnabled(string selectorString, out RFmxWlanMXOfdmModAccNo

### GetNoiseCompensationInputPowerCheckEnabled(string, out RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled)

Gets whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNoiseCompensationInputPowerCheckEnabled(string selectorString, out RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled value)

#### Remarks

This method gets the value of [OfdmModAccNoiseCompensationInputPowerCheckEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccnoisecompensationinputpowercheckenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled | Upon return, contains whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnoisecompensationreferencelevelcoercionlimit__string-out.html language=enus -->
## TOPIC 00100: GetNoiseCompensationReferenceLevelCoercionLimit(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnoisecompensationreferencelevelcoercionlimit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnoisecompensationreferencelevelcoercionlimit__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference level coercion limit for noise compensation. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNoiseCompensationReferenceLevelCoercionLimit(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccNoiseCompen

### GetNoiseCompensationReferenceLevelCoercionLimit(string, out double)

Gets the reference level coercion limit for noise compensation. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNoiseCompensationReferenceLevelCoercionLimit(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccNoiseCompensationReferenceLevelCoercionLimit](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 0.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the reference level coercion limit for noise compensation. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00101: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the OFDMModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of OfdmModAccNumberOfAnalysisThreads attribute.The defa

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the OFDMModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [OfdmModAccNumberOfAnalysisThreads](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the OFDMModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getpowercustomgatestoptime__string-out.html language=enus -->
## TOPIC 00102: GetPowerCustomGateStopTime(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getpowercustomgatestoptime__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getpowercustomgatestoptime__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop time of the custom power gate, and must be greater than the corresponding SetPowerCustomGateStartTime(string, double) method. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetPowerCustomGateStopTime(string selectorString, out double valu

### GetPowerCustomGateStopTime(string, out double)

Gets the stop time of the custom power gate, and must be greater than the corresponding [SetPowerCustomGateStartTime(string, double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setpowercustomgatestarttime__string-double.html) method. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetPowerCustomGateStopTime(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccPowerCustomGateStopTime](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 10 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the gate number. Example: "gate0". You can use the BuildGateString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the stop time of the custom power gate, and must be greater than the corresponding SetPowerCustomGateStartTime(string, double) method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getsymbolclockerrorcorrectionenabled__string-out.html language=enus -->
## TOPIC 00103: GetSymbolClockErrorCorrectionEnabled(string, out RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getsymbolclockerrorcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-getsymbolclockerrorcorrectionenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable symbol clock error correction. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetSymbolClockErrorCorrectionEnabled(string selectorString, out RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled value)RemarksThis method gets the value of OfdmModAccSymbolClockError

### GetSymbolClockErrorCorrectionEnabled(string, out RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled)

Gets whether to enable symbol clock error correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetSymbolClockErrorCorrectionEnabled(string selectorString, out RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled value)

#### Remarks

This method gets the value of [OfdmModAccSymbolClockErrorCorrectionEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccsymbolclockerrorcorrectionenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled | Upon return, contains whether to enable symbol clock error correction. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setchannelestimationltfaveragingenabled__string-rfmxwlanmxofdmmodaccchannelestimationltfaveragingenabled.html language=enus -->
## TOPIC 00104: SetChannelEstimationLtfAveragingEnabled(string, RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setchannelestimationltfaveragingenabled__string-rfmxwlanmxofdmmodaccchannelestimationltfaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setchannelestimationltfaveragingenabled__string-rfmxwlanmxofdmmodaccchannelestimationltfaveragingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetChannelEstimationLtfAveragingEnabled(string selectorString, RFmxWlanMXOfdm

### SetChannelEstimationLtfAveragingEnabled(string, RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled)

Sets whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetChannelEstimationLtfAveragingEnabled(string selectorString, RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled value)

#### Remarks

This method sets the value of [OfdmModAccChannelEstimationLtfAveragingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccchannelestimationltfaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmModAccChannelEstimationLtfAveragingEnabled | Specifies whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setevmreferencedatasymbolsmode__string-rfmxwlanmxofdmmodaccevmreferencedatasymbolsmode.html language=enus -->
## TOPIC 00105: SetEvmReferenceDataSymbolsMode(string, RFmxWlanMXOfdmModAccEvmReferenceDataSymbolsMode)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setevmreferencedatasymbolsmode__string-rfmxwlanmxofdmmodaccevmreferencedatasymbolsmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setevmreferencedatasymbolsmode__string-rfmxwlanmxofdmmodaccevmreferencedatasymbolsmode.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetEvmReferenceDataSymbolsMode(string selectorString, RFmxWlanMXOfdmModAccEvmReferenceData

### SetEvmReferenceDataSymbolsMode(string, RFmxWlanMXOfdmModAccEvmReferenceDataSymbolsMode)

Sets whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetEvmReferenceDataSymbolsMode(string selectorString, RFmxWlanMXOfdmModAccEvmReferenceDataSymbolsMode value)

#### Remarks

This method sets the value of [OfdmModAccEvmReferenceDataSymbolsMode](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [AcquiredWaveform](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccevmreferencedatasymbolsmode.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmModAccEvmReferenceDataSymbolsMode | Specifies whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setiqimpairmentspersubcarrierenabled__string-rfmxwlanmxofdmmodacciqimpairmentspersubcarrierenabled.html language=enus -->
## TOPIC 00106: SetIQImpairmentsPerSubcarrierEnabled(string, RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setiqimpairmentspersubcarrierenabled__string-rfmxwlanmxofdmmodacciqimpairmentspersubcarrierenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setiqimpairmentspersubcarrierenabled__string-rfmxwlanmxofdmmodacciqimpairmentspersubcarrierenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to estimate I/Q impairments independently for each subcarrier. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetIQImpairmentsPerSubcarrierEnabled(string selectorString, RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled value)RemarksThis method sets the value of OfdmModA

### SetIQImpairmentsPerSubcarrierEnabled(string, RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled)

Sets whether to estimate I/Q impairments independently for each subcarrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetIQImpairmentsPerSubcarrierEnabled(string selectorString, RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled value)

#### Remarks

This method sets the value of [OfdmModAccIQImpairmentsPerSubcarrierEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodacciqimpairmentspersubcarrierenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled | Specifies whether to estimate I/Q impairments independently for each subcarrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setiqtimingskewcorrectionenabled__string-rfmxwlanmxofdmmodacciqtimingskewcorrectionenabled.html language=enus -->
## TOPIC 00107: SetIQTimingSkewCorrectionEnabled(string, RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setiqtimingskewcorrectionenabled__string-rfmxwlanmxofdmmodacciqtimingskewcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setiqtimingskewcorrectionenabled__string-rfmxwlanmxofdmmodacciqtimingskewcorrectionenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable I/Q timing skew correction. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetIQTimingSkewCorrectionEnabled(string selectorString, RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled value)RemarksThis method sets the value of OfdmModAccIQTimingSkewCorrectionEnabled a

### SetIQTimingSkewCorrectionEnabled(string, RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled)

Sets whether to enable I/Q timing skew correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetIQTimingSkewCorrectionEnabled(string selectorString, RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled value)

#### Remarks

This method sets the value of [OfdmModAccIQTimingSkewCorrectionEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodacciqtimingskewcorrectionenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled | Specifies whether to enable I/Q timing skew correction. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00108: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable OFDMModAcc measurement for OFDM based standards. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of OfdmModAccMeasurementEnabled attribute.The default value is FALSE.Parameters

### SetMeasurementEnabled(string, bool)

Sets whether to enable OFDMModAcc measurement for OFDM based standards.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [OfdmModAccMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable OFDMModAcc measurement for OFDM based standards. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setreferencedataconstellationidentifier__string-string.html language=enus -->
## TOPIC 00109: SetReferenceDataConstellationIdentifier(string, string)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setreferencedataconstellationidentifier__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setreferencedataconstellationidentifier__string-string.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Identifies the reference files used for combined signal demodulation. The value of this method must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccC

### SetReferenceDataConstellationIdentifier(string, string)

Identifies the reference files used for combined signal demodulation. The value of this method must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if [SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setcombinedsignaldemodulationenabled__string-rfmxwlanmxofdmmodacccombinedsignaldemodulationenabled.html) is set to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodacccombinedsignaldemodulationenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetReferenceDataConstellationIdentifier(string selectorString, string value)

#### Remarks

This method sets the value of [OfdmModAccReferenceDataConstellationIdentifier](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute. The default value is "" (empty string).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Identifies the reference files used for combined signal demodulation. The value of this method must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccimpilotsenabled.html language=enus -->
## TOPIC 00110: RFmxWlanMXOfdmModAccIMPilotsEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccimpilotsenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccimpilotsenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether interference mitigating pilots are present. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccIMPilotsEnabledMembersNameValueDescriptionFalse0Indicates that interference mitigating pilots are absent. True1Indicates that interference mitigating pilots are

### RFmxWlanMXOfdmModAccIMPilotsEnabled Enumeration

Returns whether interference mitigating pilots are present.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccIMPilotsEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Indicates that interference mitigating pilots are absent. |
| True | 1 | Indicates that interference mitigating pilots are present. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccphaserotationcoefficient1.html language=enus -->
## TOPIC 00111: RFmxWlanMXOfdmModAccPhaseRotationCoefficient1 Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccphaserotationcoefficient1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccphaserotationcoefficient1.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccPhaseRotationCoefficient1MembersNameValueDescriptionPlusOne0Specifies that phase rotation coefficient 1 is +1. MinusOne1Specifies tha

### RFmxWlanMXOfdmModAccPhaseRotationCoefficient1 Enumeration

Specifies the phase rotation coefficient 1 as defined in *IEEE Standard P802.11be/D7.0*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccPhaseRotationCoefficient1

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PlusOne | 0 | Specifies that phase rotation coefficient 1 is +1. |
| MinusOne | 1 | Specifies that phase rotation coefficient 1 is -1. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchchainrmsevmpersubcarriermeantrace__string-double-ref.html language=enus -->
## TOPIC 00112: FetchChainRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchchainrmsevmpersubcarriermeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchchainrmsevmpersubcarriermeantrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain RMS EVM per subcarrier trace. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the chain RMS EVM per subcarrier computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to

### FetchChainRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the chain RMS EVM per subcarrier trace. When you set the [SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setaveragingenabled__string-rfmxwlanmxofdmmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html) , this method returns the mean of the chain RMS EVM per subcarrier computed for each averaging count. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchChainRmsEvmPerSubcarrierMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > chainRmsEvmPerSubcarrierMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| chainRmsEvmPerSubcarrierMean | ref AnalogWaveform< float > | Upon return, contains the chain RMS EVM per subcarrier trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchcommonpiloterrortrace__string-double-ref-ref.html language=enus -->
## TOPIC 00113: FetchCommonPilotErrorTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchcommonpiloterrortrace__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchcommonpiloterrortrace__string-double-ref-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the common pilot error magnitude and phase traces. Use "segment(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchCommonPilotErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > commonPilotErr

### FetchCommonPilotErrorTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the common pilot error magnitude and phase traces. 
 Use "segment(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchCommonPilotErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > commonPilotErrorMagnitude, ref AnalogWaveform< float > commonPilotErrorPhase)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and segment number. Example: "segment0" "result::r1/segment0" You can use the BuildSegmentString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| commonPilotErrorMagnitude | ref AnalogWaveform< float > | Upon return, contains the common pilot error magnitude trace. Common pilot error for an OFDM symbol is the correlation of the received pilot subcarrier BPSK symbols with their ideal values. This trace represents the magnitude of the common pilot error for each OFDM symbol. |
| commonPilotErrorPhase | ref AnalogWaveform< float > | Upon return, contains the common pilot error phase trace. Common pilot error for an OFDM symbol is the correlation of the received pilot subcarrier BPSK symbols with their ideal values. This trace represents the phase of the common pilot error for each OFDM symbol. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdatapeakpower__string-double-out.html language=enus -->
## TOPIC 00114: FetchDataPeakPower(string, double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdatapeakpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdatapeakpower__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the data field. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchDataPeakPower(string selectorString, double timeout, out double dataPeakPowerMaximum)ParametersNameTypeDescript

### FetchDataPeakPower(string, double, out double)

Fetches the peak power of the data field. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchDataPeakPower(string selectorString, double timeout, out double dataPeakPowerMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| dataPeakPowerMaximum | out double | Upon return, contains the peak power of the data field. This value is expressed in dBm. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns an array of the maximum of the data peak power results computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodedehtsigbitstrace__string-double-ref.html language=enus -->
## TOPIC 00115: FetchDecodedEhtSigBitsTrace(string, double, ref int[])

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodedehtsigbitstrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodedehtsigbitstrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded EHT-SIG bits trace. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchDecodedEhtSigBitsTrace(string selectorString, double timeout, ref int[] decodedEhtSigBits)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name

### FetchDecodedEhtSigBitsTrace(string, double, ref int[])

Fetches the decoded EHT-SIG bits trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchDecodedEhtSigBitsTrace(string selectorString, double timeout, ref int[] decodedEhtSigBits)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| decodedEhtSigBits | ref int[] | Upon return, contains the array of bits in the EHT-SIG field of the 802.11be waveform for all 80 MHz subblocks. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodedelrsigbitstrace__string-double-ref.html language=enus -->
## TOPIC 00116: FetchDecodedElrSigBitsTrace(string, double, ref int[])

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodedelrsigbitstrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodedelrsigbitstrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchDecodedElrSigBitsTrace(string selectorString, double timeout, ref int[] decodedElrSigBits)

### FetchDecodedElrSigBitsTrace(string, double, ref int[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchDecodedElrSigBitsTrace(string selectorString, double timeout, ref int[] decodedElrSigBits)

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodeduhrsigbitstrace__string-double-ref.html language=enus -->
## TOPIC 00117: FetchDecodedUhrSigBitsTrace(string, double, ref int[])

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodeduhrsigbitstrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchdecodeduhrsigbitstrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchDecodedUhrSigBitsTrace(string selectorString, double timeout, ref int[] decodedUhrSigBits)

### FetchDecodedUhrSigBitsTrace(string, double, ref int[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchDecodedUhrSigBitsTrace(string selectorString, double timeout, ref int[] decodedUhrSigBits)

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchevmsubcarrierindices__string-double-ref.html language=enus -->
## TOPIC 00118: FetchEvmSubcarrierIndices(string, double, ref int[])

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchevmsubcarrierindices__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchevmsubcarrierindices__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of subcarrier indices for which the EVM results are computed. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchEvmSubcarrierIndices(string selectorString, double timeout, ref int[] subcarrierIndices)ParametersNameTypeDescriptionselectorStringstringSpecifies a selecto

### FetchEvmSubcarrierIndices(string, double, ref int[])

Fetches the array of subcarrier indices for which the EVM results are computed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchEvmSubcarrierIndices(string selectorString, double timeout, ref int[] subcarrierIndices)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| subcarrierIndices | ref int[] | Upon return, contains an array of subcarrier indices for which the EVM results are computed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchfrequencyerrormean__string-double-out.html language=enus -->
## TOPIC 00119: FetchFrequencyErrorMean(string, double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchfrequencyerrormean__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchfrequencyerrormean__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier frequency error of the transmitter. Use "segment(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchFrequencyErrorMean(string selectorString, double timeout, out double frequencyErrorMean)ParametersNameType

### FetchFrequencyErrorMean(string, double, out double)

Fetches the carrier frequency error of the transmitter. 
 Use "segment(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchFrequencyErrorMean(string selectorString, double timeout, out double frequencyErrorMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and segment number. Example: "segment0" "result::r1/segment0" You can use the BuildSegmentString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| frequencyErrorMean | out double | Upon return, contains the carrier frequency error of the transmitter. This value is expressed in Hz. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the carrier frequency error results computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchgroupdelaymeantrace__string-double-ref.html language=enus -->
## TOPIC 00120: FetchGroupDelayMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchgroupdelaymeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchgroupdelaymeantrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the group delay trace computed for each averaging count. Use "segment(n)/cha

### FetchGroupDelayMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the [SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setaveragingenabled__string-rfmxwlanmxofdmmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html) , this method returns the mean of the group delay trace computed for each averaging count. 
 Use "segment(n)/chain(k)/stream(l)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchGroupDelayMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > groupDelayMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, chain number, and stream number. Example: "segment0/chain0/stream0" "result::r1/segment0/chain0/stream0" You can use the BuildStreamString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| groupDelayMean | ref AnalogWaveform< float > | Upon return, contains the group delay mean trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchguardintervaltype__string-double-out.html language=enus -->
## TOPIC 00121: FetchGuardIntervalType(string, double, out RFmxWlanMXOfdmGuardIntervalType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchguardintervaltype__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchguardintervaltype__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the guard interval type. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchGuardIntervalType(string selectorString, double timeout, out RFmxWlanMXOfdmGuardIntervalType guardIntervalType)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of t

### FetchGuardIntervalType(string, double, out RFmxWlanMXOfdmGuardIntervalType)

Fetches the guard interval type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchGuardIntervalType(string selectorString, double timeout, out RFmxWlanMXOfdmGuardIntervalType guardIntervalType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| guardIntervalType | out RFmxWlanMXOfdmGuardIntervalType | Upon return, contains the size of the guard interval of OFDM symbols. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqgainimbalancepersubcarriermeantrace__string-double-ref.html language=enus -->
## TOPIC 00122: FetchIQGainImbalancePerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqgainimbalancepersubcarriermeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqgainimbalancepersubcarriermeantrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q gain imbalance per subcarrier trace. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the I/Q gain imbalance computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to read

### FetchIQGainImbalancePerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the I/Q gain imbalance per subcarrier trace. When you set the [SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setaveragingenabled__string-rfmxwlanmxofdmmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html) , this method returns the mean of the I/Q gain imbalance computed for each averaging count. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchIQGainImbalancePerSubcarrierMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > iqGainImbalancePerSubcarrierMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| iqGainImbalancePerSubcarrierMean | ref AnalogWaveform< float > | Upon return, contains the I/Q gain imbalance per subcarrier trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqimpairments__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00123: FetchIQImpairments(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqimpairments__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqimpairments__string-double-out-out-out-out-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q Impairment results for the OFDMModAcc measurement. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchIQImpairments(string selectorString, double timeout, out double relativeIQOriginOffset

### FetchIQImpairments(string, double, out double, out double, out double, out double, out double)

Fetches the I/Q Impairment results for the OFDMModAcc measurement. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchIQImpairments(string selectorString, double timeout, out double relativeIQOriginOffsetMean, out double iqGainImbalanceMean, out double iqQuadratureErrorMean, out double absoluteIQOriginOffsetMean, out double iqTimingSkewMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| relativeIQOriginOffsetMean | out double | Upon return, contains the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the relative I/Q origin offset computed for each averaging count. This value is expressed in dB. |
| iqGainImbalanceMean | out double | Upon return, contains the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. When you set the OFDMModAccAveragingEnabled method to True , this method returns the mean of the I/Q gain imbalance computed for each averaging count. This value is expressed in dB. |
| iqQuadratureErrorMean | out double | Upon return, contains the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. When you set the OFDMModAccAveragingEnabled method to True , this method returns the I/Q quadrature error computed for each averaging count. This value is expressed in degrees. |
| absoluteIQOriginOffsetMean | out double | Upon return, contains the absolute I/Q origin offset, which is the power of the DC subcarrier. When you set the OFDMModAccAveragingEnabled method to True , this method returns the mean of the absolute I/Q origin offset computed for each averaging count. This value is expressed in dBm. |
| iqTimingSkewMean | out double | Upon return, contains the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. When you set the OFDMModAccAveragingEnabled method to True , this method returns the mean of the I/Q timing skew computed for each averaging count. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqquadratureerrorpersubcarriermeantrace__string-double-ref.html language=enus -->
## TOPIC 00124: FetchIQQuadratureErrorPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqquadratureerrorpersubcarriermeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchiqquadratureerrorpersubcarriermeantrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q quadrature error per subcarrier trace. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the I/Q quadrature error computed for each averaging count. Use "segment(n)/chain(k)" as the selector string to r

### FetchIQQuadratureErrorPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the I/Q quadrature error per subcarrier trace. When you set the [SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setaveragingenabled__string-rfmxwlanmxofdmmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html) , this method returns the mean of the I/Q quadrature error computed for each averaging count. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchIQQuadratureErrorPerSubcarrierMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > iqQuadratureErrorPerSubcarrierMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| iqQuadratureErrorPerSubcarrierMean | ref AnalogWaveform< float > | Upon return, contains the I/Q quadrature error per subcarrier trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchlsigparitycheckstatus__string-double-out.html language=enus -->
## TOPIC 00125: FetchLSigParityCheckStatus(string, double, out RFmxWlanMXOfdmModAccLSigParityCheckStatus)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchlsigparitycheckstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchlsigparitycheckstatus__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the L-SIG parity check status. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchLSigParityCheckStatus(string selectorString, double timeout, out RFmxWlanMXOfdmModAccLSigParityCheckStatus lSigParityCheckStatus)ParametersNameTypeDescriptionselectorStringstringSpecifies a selecto

### FetchLSigParityCheckStatus(string, double, out RFmxWlanMXOfdmModAccLSigParityCheckStatus)

Fetches the L-SIG parity check status.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchLSigParityCheckStatus(string selectorString, double timeout, out RFmxWlanMXOfdmModAccLSigParityCheckStatus lSigParityCheckStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| lSigParityCheckStatus | out RFmxWlanMXOfdmModAccLSigParityCheckStatus | Upon return, contains whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchltfsize__string-double-out.html language=enus -->
## TOPIC 00126: FetchLtfSize(string, double, out RFmxWlanMXOfdmLtfSize)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchltfsize__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchltfsize__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchLtfSize(string selectorString, double timeout, out RFmxWlanMXOfdmLtfSize ltfSize)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string com

### FetchLtfSize(string, double, out RFmxWlanMXOfdmLtfSize)

Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchLtfSize(string selectorString, double timeout, out RFmxWlanMXOfdmLtfSize ltfSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| ltfSize | out RFmxWlanMXOfdmLtfSize | Upon return, contains the HE-LTF or EHT-LTF size. This result is applicable only to 802.11ax and 802.11be signals. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchmcsindex__string-double-out.html language=enus -->
## TOPIC 00127: FetchMcsIndex(string, double, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchmcsindex__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchmcsindex__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the MCS index. Use "user(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchMcsIndex(string selectorString, double timeout, out int mcsIndex)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string

### FetchMcsIndex(string, double, out int)

Fetches the MCS index. 
 Use "user(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchMcsIndex(string selectorString, double timeout, out int mcsIndex)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and user number. If you do not specify the result name, the default result instance is used. Example: "user0" "result::r1/user0" You can use the BuildUserString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| mcsIndex | out int | Upon return, contains the MCS index or the data rate. The MCS index or data rate for various standard signals are decoded as follows: |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofhesigbsymbols__string-double-out.html language=enus -->
## TOPIC 00128: FetchNumberOfHESigBSymbols(string, double, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofhesigbsymbols__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofhesigbsymbols__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of HE-SIG-B symbols. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchNumberOfHESigBSymbols(string selectorString, double timeout, out int numberOfHESigBSymbols)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result nam

### FetchNumberOfHESigBSymbols(string, double, out int)

Fetches the number of HE-SIG-B symbols.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchNumberOfHESigBSymbols(string selectorString, double timeout, out int numberOfHESigBSymbols)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| numberOfHESigBSymbols | out int | Upon return, contains the number of HE-SIG-B symbols. This result is applicable for 802.11ax MU PPDU signals, and is decoded from the HE-SIG-A field. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofspacetimestreams__string-double-out.html language=enus -->
## TOPIC 00129: FetchNumberOfSpaceTimeStreams(string, double, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofspacetimestreams__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofspacetimestreams__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of space time streams. Use "user(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchNumberOfSpaceTimeStreams(string selectorString, double timeout, out int numberOfSpaceTimeStreams)ParametersNameTypeDescript

### FetchNumberOfSpaceTimeStreams(string, double, out int)

Fetches the number of space time streams. 
 Use "user(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchNumberOfSpaceTimeStreams(string selectorString, double timeout, out int numberOfSpaceTimeStreams)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and user number. If you do not specify the result name, the default result instance is used. Example: "user0" "result::r1/user0" You can use the BuildUserString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| numberOfSpaceTimeStreams | out int | Upon return, contains the number of space time streams. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofsymbolsused__string-double-out.html language=enus -->
## TOPIC 00130: FetchNumberOfSymbolsUsed(string, double, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofsymbolsused__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofsymbolsused__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of OFDM symbols used for EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchNumberOfSymbolsUsed(string selectorString, double timeout, out int numberOfSymbolsUsed)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising

### FetchNumberOfSymbolsUsed(string, double, out int)

Fetches the number of OFDM symbols used for EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchNumberOfSymbolsUsed(string selectorString, double timeout, out int numberOfSymbolsUsed)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| numberOfSymbolsUsed | out int | Upon return, contains the number of OFDM symbols used by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofusers__string-double-out.html language=enus -->
## TOPIC 00131: FetchNumberOfUsers(string, double, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofusers__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchnumberofusers__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of users. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchNumberOfUsers(string selectorString, double timeout, out int numberOfUsers)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you do not specify th

### FetchNumberOfUsers(string, double, out int)

Fetches the number of users.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchNumberOfUsers(string selectorString, double timeout, out int numberOfUsers)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| numberOfUsers | out int | Upon return, contains the number of users which is derived for the following standards. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpeaveragepower__string-double-out.html language=enus -->
## TOPIC 00132: FetchPEAveragePower(string, double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpeaveragepower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpeaveragepower__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the packet extension field. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchPEAveragePower(string selectorString, double timeout, out double peAveragePowerMean)ParametersNa

### FetchPEAveragePower(string, double, out double)

Fetches the average power of the packet extension field. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchPEAveragePower(string selectorString, double timeout, out double peAveragePowerMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| peAveragePowerMean | out double | Upon return, contains the average power of the packet extension field. This parameter is applicable for 802.11ax signals. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the packet extension field average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpeduration__string-double-out.html language=enus -->
## TOPIC 00133: FetchPEDuration(string, double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpeduration__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpeduration__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the duration of the packet extension field. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchPEDuration(string selectorString, double timeout, out double peDuration)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If y

### FetchPEDuration(string, double, out double)

Fetches the duration of the packet extension field.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchPEDuration(string selectorString, double timeout, out double peDuration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| peDuration | out double | Upon return, contains the duration of the packet extension field for the 802.11ax and 802.11be signals. This parameter is applicable only when you set the SetOfdmHeaderDecodingEnabled(string, RFmxWlanMXOfdmHeaderDecodingEnabled) method to True . This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchppdupeakpower__string-double-out.html language=enus -->
## TOPIC 00134: FetchPpduPeakPower(string, double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchppdupeakpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchppdupeakpower__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the PPDU. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchPpduPeakPower(string selectorString, double timeout, out double ppduPeakPowerMaximum)ParametersNameTypeDescriptionsel

### FetchPpduPeakPower(string, double, out double)

Fetches the peak power of the PPDU. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchPpduPeakPower(string selectorString, double timeout, out double ppduPeakPowerMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| ppduPeakPowerMaximum | out double | Upon return, contains the peak power of the PPDU. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the maximum of the PPDU peak power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpreambleaveragepowers802_11ax__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00135: FetchPreambleAveragePowers802_11ax(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpreambleaveragepowers802_11ax__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchpreambleaveragepowers802_11ax__string-double-out-out-out-out-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11ax specific preamble fields. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchPreambleAveragePowers802_11ax(string selectorString, double timeout, out double rlSig

### FetchPreambleAveragePowers802_11ax(string, double, out double, out double, out double, out double, out double)

Fetches the average power of the 802.11ax specific preamble fields. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchPreambleAveragePowers802_11ax(string selectorString, double timeout, out double rlSigAveragePowerMean, out double heSigAAveragePowerMean, out double heSigBAveragePowerMean, out double heStfAveragePowerMean, out double heLtfAveragePowerMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| rlSigAveragePowerMean | out double | Upon return, contains the average power of the RL-SIG field. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the RL-SIG field average power results computed for each averaging count. This value is expressed in dBm. |
| heSigAAveragePowerMean | out double | Upon return, contains the average power of the HE-SIG-A field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the HE-SIG-A field average power results computed for each averaging count. This value is expressed in dBm. |
| heSigBAveragePowerMean | out double | Upon return, contains the average power of the HE-SIG-B field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the HE-SIG-B field average power results computed for each averaging count. This value is expressed in dBm. |
| heStfAveragePowerMean | out double | Upon return, contains the average power of the HE-STF field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the HE-STF average power results computed for each averaging count. This value is expressed in dBm. |
| heLtfAveragePowerMean | out double | Upon return, contains the average power of the HE-LTF field. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the HE-LTF average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchsymbolchainevmpersubcarriertrace__string-double-int-ref.html language=enus -->
## TOPIC 00136: FetchSymbolChainEvmPerSubcarrierTrace(string, double, int, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchsymbolchainevmpersubcarriertrace__string-double-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchsymbolchainevmpersubcarriertrace__string-double-int-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchSymbolChainEvmPerSu

### FetchSymbolChainEvmPerSubcarrierTrace(string, double, int, ref AnalogWaveform< float >)

Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchSymbolChainEvmPerSubcarrierTrace(string selectorString, double timeout, int symbolIndex, ref AnalogWaveform< float > symbolChainEvmPerSubcarrier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| symbolIndex | int | Specifies the symbol index for which to fetch the trace. |
| symbolChainEvmPerSubcarrier | ref AnalogWaveform< float > | Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchsymbolstreamevmpersubcarriertrace__string-double-int-ref.html language=enus -->
## TOPIC 00137: FetchSymbolStreamEvmPerSubcarrierTrace(string, double, int, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchsymbolstreamevmpersubcarriertrace__string-double-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchsymbolstreamevmpersubcarriertrace__string-double-int-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream EVM per subcarrier trace for a symbol. Use "segment(n)/stream(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchSymbolStreamEvmPerSubcarrierTrace(string selectorString, double timeout, int symbolIndex, ref

### FetchSymbolStreamEvmPerSubcarrierTrace(string, double, int, ref AnalogWaveform< float >)

Fetches the stream EVM per subcarrier trace for a symbol. 
 Use "segment(n)/stream(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchSymbolStreamEvmPerSubcarrierTrace(string selectorString, double timeout, int symbolIndex, ref AnalogWaveform< float > symbolStreamEvmPerSubcarrier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and stream number. If you do not specify the result name, the default result instance is used. Example: "segment0/stream0" "result::r1/segment0/stream0" You can use the BuildStreamString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| symbolIndex | int | Specifies the symbol index for which to fetch the trace. |
| symbolStreamEvmPerSubcarrier | ref AnalogWaveform< float > | Upon return, contains the stream EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchunusedtoneerror__string-double-out-out.html language=enus -->
## TOPIC 00138: FetchUnusedToneError(string, double, out double, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchunusedtoneerror__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchunusedtoneerror__string-double-out-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error margin results. Refer to Unused Tone Error Measurement for more information. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchUnusedToneError(string selectorString, double

### FetchUnusedToneError(string, double, out double, out int)

Fetches the unused tone error margin results. 
 Refer to Unused Tone Error Measurement for more information. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchUnusedToneError(string selectorString, double timeout, out double unusedToneErrorMargin, out int unusedToneErrorMarginRUIndex)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| unusedToneErrorMargin | out double | Upon return, contains the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB. |
| unusedToneErrorMarginRUIndex | out int | Upon return, contains the 26-tone RU index corresponding to the unusedToneErrorMargin parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchunusedtoneerrormarginperru__string-double-ref.html language=enus -->
## TOPIC 00139: FetchUnusedToneErrorMarginPerRU(string, double, ref double[])

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchunusedtoneerrormarginperru__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchunusedtoneerrormarginperru__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error margin result per RU. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchUnusedToneErrorMarginPerRU(string selectorString, double timeout, ref double[] unusedToneErrorMarginP

### FetchUnusedToneErrorMarginPerRU(string, double, ref double[])

Fetches the unused tone error margin result per RU. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchUnusedToneErrorMarginPerRU(string selectorString, double timeout, ref double[] unusedToneErrorMarginPerRU)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| unusedToneErrorMarginPerRU | ref double[] | Upon return, contains an array of unused tone error margin per RU, which is the difference between the unused tone error mask and the unused tone error for each RU. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserpower__string-double-out.html language=enus -->
## TOPIC 00140: FetchUserPower(string, double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserpower__string-double-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the user power. Use "user(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchUserPower(string selectorString, double timeout, out double userPowerMean)ParametersNameTypeDescriptionselectorStringstringSpecifies a select

### FetchUserPower(string, double, out double)

Fetches the user power. 
 Use "user(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchUserPower(string selectorString, double timeout, out double userPowerMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and user number. If you do not specify the result name, the default result instance is used. Example: "user0" "result::r1/user0" You can use the BuildUserString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| userPowerMean | out double | Upon return, contains the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the user power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreamdatarmsevmpersymbolmeantrace__string-double-ref.html language=enus -->
## TOPIC 00141: FetchUserStreamDataRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreamdatarmsevmpersymbolmeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreamdatarmsevmpersymbolmeantrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this method returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. Use "user(n)/stre

### FetchUserStreamDataRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the [SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccconfiguration-setaveragingenabled__string-rfmxwlanmxofdmmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingenabled.html) , this method returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. 
 Use "user(n)/stream(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchUserStreamDataRmsEvmPerSymbolMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > userStreamDataRmsEvmPerSymbolMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0" "result::r1/user0/stream0" You can use the BuildStreamString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| userStreamDataRmsEvmPerSymbolMean | ref AnalogWaveform< float > | Upon return, contains the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the Averaging Enabled method to True , this parameter returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreampilotrmsevmpersymbolmeantrace__string-double-ref.html language=enus -->
## TOPIC 00142: FetchUserStreamPilotRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreampilotrmsevmpersymbolmeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreampilotrmsevmpersymbolmeantrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user. Use "user(n)/stream(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchUserStreamPilotRmsEvmPerSymbolMeanTrace(string selectorString, double timeout,

### FetchUserStreamPilotRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user. 
 Use "user(n)/stream(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchUserStreamPilotRmsEvmPerSymbolMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > userStreamPilotRmsEvmPerSymbolMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0" "result::r1/user0/stream0" You can use the BuildStreamString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| userStreamPilotRmsEvmPerSymbolMean | ref AnalogWaveform< float > | Upon return, contains the stream pilot-subcarriers RMS EVM per symbol trace for each user. When you set the Averaging Enabled method to true , this parameter returns the mean of the user stream pilot RMS EVM per symbol computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreamrmsevm__string-double-out-out-out.html language=enus -->
## TOPIC 00143: FetchUserStreamRmsEvm(string, double, out double, out double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreamrmsevm__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-fetchuserstreamrmsevm__string-double-out-out-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM results for the specified user. Use "user(n)/stream(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchUserStreamRmsEvm(string selectorString, double timeout, out double userStreamRmsEvmMean, out dou

### FetchUserStreamRmsEvm(string, double, out double, out double, out double)

Fetches the stream RMS EVM results for the specified user. 
 Use "user(n)/stream(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchUserStreamRmsEvm(string selectorString, double timeout, out double userStreamRmsEvmMean, out double userStreamDataRmsEvmMean, out double userStreamPilotRmsEvmMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, user number, and stream number. If you do not specify the result name, the default result instance is used. Example: "user0/stream0" "result::r1/user0/stream0" You can use the BuildStreamString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| userStreamRmsEvmMean | out double | Upon return, contains the RMS EVM of all subcarriers in all OFDM symbols for the specified user. When you set the SetEvmUnit(string, RFmxWlanMXOfdmModAccEvmUnit) method to Percentage , the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit method to dB , the measurement returns this result in dB. When you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True , this parameter returns the mean of the user stream RMS EVM computed for each averaging count. |
| userStreamDataRmsEvmMean | out double | Upon return, contains the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. When you set the SetEvmUnit(string, RFmxWlanMXOfdmModAccEvmUnit) method to Percentage , the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit method to dB , the measurement returns this result in dB. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the user stream data RMS EVM computed for each averaging count. |
| userStreamPilotRmsEvmMean | out double | Upon return, contains the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. When you set the SetEvmUnit(string, RFmxWlanMXOfdmModAccEvmUnit) method to Percentage , the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit method to dB , the measurement returns this result in dB. When you set the OFDMModAccAveragingEnabled method to True , this parameter returns the mean of the user stream pilot RMS EVM computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-get2xldpcenabled__string-out.html language=enus -->
## TOPIC 00144: Get2xLdpcEnabled(string, out RFmxWlanMXOfdmModAcc2xLdpcEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-get2xldpcenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-get2xldpcenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether 2xLDPC is enabled for a specified user. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int Get2xLdpcEnabled(string selectorString, out RFmxWlanMXOfdmModAcc2xLdpcEnabled value)RemarksThis method gets the value of OfdmModAccResults2xLdpcEnabled attribute.ParametersNameTypeDescript

### Get2xLdpcEnabled(string, out RFmxWlanMXOfdmModAcc2xLdpcEnabled)

Gets whether 2xLDPC is enabled for a specified user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int Get2xLdpcEnabled(string selectorString, out RFmxWlanMXOfdmModAcc2xLdpcEnabled value)

#### Remarks

This method gets the value of [OfdmModAccResults2xLdpcEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and User number. Example: "User0", "result::r1/User0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out RFmxWlanMXOfdmModAcc2xLdpcEnabled | Upon return, contains whether 2xLDPC is enabled for a specified user. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getchainstreamcrosspowermean__string-out.html language=enus -->
## TOPIC 00145: GetChainStreamCrossPowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getchainstreamcrosspowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getchainstreamcrosspowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stream cross power. The cross power for chain 'k' stream 'm' is the power contribution of stream 'm' in chain 'k'. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetChainStreamCrossPowerMean(string selectorString, out double value)RemarksThis metho

### GetChainStreamCrossPowerMean(string, out double)

Gets the stream cross power. The cross power for chain 'k' stream 'm' is the power contribution of stream 'm' in chain 'k'. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetChainStreamCrossPowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsChainStreamCrossPowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Stream number, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Stream0/Chain0". You can use the BuildStreamString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the stream cross power. The cross power for chain k stream m is the power contribution of stream m in chain k. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcompositepilotrmsevmmean__string-out.html language=enus -->
## TOPIC 00146: GetCompositePilotRmsEvmMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcompositepilotrmsevmmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcompositepilotrmsevmmean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetCompositePilotRmsEvmMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsCompositeP

### GetCompositePilotRmsEvmMean(string, out double)

Gets the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetCompositePilotRmsEvmMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsCompositePilotRmsEvmMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcompositermsevmmean__string-out.html language=enus -->
## TOPIC 00147: GetCompositeRmsEvmMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcompositermsevmmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcompositermsevmmean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetCompositeRmsEvmMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsCompositeRmsEvmMe

### GetCompositeRmsEvmMean(string, out double)

Gets the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetCompositeRmsEvmMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsCompositeRmsEvmMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcrosspowermean__string-out.html language=enus -->
## TOPIC 00148: GetCrossPowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcrosspowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getcrosspowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetCrossPowerMean(string selectorString, out double value)RemarksThis method gets the v

### GetCrossPowerMean(string, out double)

Gets the cross power. The cross power for chain *x* is the power contribution from streams other than stream *x* in the chain. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetCrossPowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsCrossPowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdatapeakpowermaximum__string-out.html language=enus -->
## TOPIC 00149: GetDataPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdatapeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdatapeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the data field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetDataPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsDataPeakPowerMaximum attribute.ParametersNameTypeDes

### GetDataPeakPowerMaximum(string, out double)

Gets the peak power of the data field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetDataPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsDataPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the data field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdcmenabled__string-out.html language=enus -->
## TOPIC 00150: GetDcmEnabled(string, out RFmxWlanMXOfdmModAccDcmEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdcmenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdcmenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether DCM is enabled for a specified user. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetDcmEnabled(string selectorString, out RFmxWlanMXOfdmModAccDcmEnabled value)RemarksThis method gets the value of OfdmModAccResultsDcmEnabled attribute.ParametersNameTypeDescriptionselectorS

### GetDcmEnabled(string, out RFmxWlanMXOfdmModAccDcmEnabled)

Gets whether DCM is enabled for a specified user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetDcmEnabled(string selectorString, out RFmxWlanMXOfdmModAccDcmEnabled value)

#### Remarks

This method gets the value of [OfdmModAccResultsDcmEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and User number. Example: "User0", "result::r1/User0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out RFmxWlanMXOfdmModAccDcmEnabled | Upon return, contains whether DCM is enabled for a specified user. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdistributionbandwidth__string-out.html language=enus -->
## TOPIC 00151: GetDistributionBandwidth(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdistributionbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getdistributionbandwidth__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetDistributionBandwidth(string selectorString, out double value)

### GetDistributionBandwidth(string, out double)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetDistributionBandwidth(string selectorString, out double value)

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getehtsigpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00152: GetEhtSigPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getehtsigpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getehtsigpeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the EHT-SIG field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetEhtSigPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsEhtSigPeakPowerMaximum attribute.ParametersName

### GetEhtSigPeakPowerMaximum(string, out double)

Gets the peak power of the EHT-SIG field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetEhtSigPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsEhtSigPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the EHT-SIG field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getfeccodingtype__string-out.html language=enus -->
## TOPIC 00153: GetFecCodingType(string, out RFmxWlanMXOfdmModAccFecCodingType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getfeccodingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getfeccodingtype__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FEC coding type for a specified user. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetFecCodingType(string selectorString, out RFmxWlanMXOfdmModAccFecCodingType value)RemarksThis method gets the value of OfdmModAccResultsFecCodingType attribute.ParametersNameTypeDescriptionsel

### GetFecCodingType(string, out RFmxWlanMXOfdmModAccFecCodingType)

Gets the FEC coding type for a specified user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetFecCodingType(string selectorString, out RFmxWlanMXOfdmModAccFecCodingType value)

#### Remarks

This method gets the value of [OfdmModAccResultsFecCodingType](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and User number. Example: "User0", "result::r1/User0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out RFmxWlanMXOfdmModAccFecCodingType | Upon return, contains the FEC coding type for a specified user. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getfrequencyerrormean__string-out.html language=enus -->
## TOPIC 00154: GetFrequencyErrorMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getfrequencyerrormean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getfrequencyerrormean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier frequency error of the transmitter. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetFrequencyErrorMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsFrequencyErrorMean attribute.ParametersNa

### GetFrequencyErrorMean(string, out double)

Gets the carrier frequency error of the transmitter. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetFrequencyErrorMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsFrequencyErrorMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Segment number. Example: "Segment0", "result::r1/Segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier frequency error of the transmitter. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethesigbaveragepowermean__string-out.html language=enus -->
## TOPIC 00155: GetHESigBAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethesigbaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethesigbaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the HE-SIG-B field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetHESigBAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsHESigBAveragePowerMean attribute.Parameters

### GetHESigBAveragePowerMean(string, out double)

Gets the average power of the HE-SIG-B field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetHESigBAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsHESigBAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the HE-SIG-B field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethesigbpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00156: GetHESigBPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethesigbpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethesigbpeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the HE-SIG-B field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetHESigBPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsHESigBPeakPowerMaximum attribute.ParametersNam

### GetHESigBPeakPowerMaximum(string, out double)

Gets the peak power of the HE-SIG-B field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetHESigBPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsHESigBPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the HE-SIG-B field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethteltfaveragepowermean__string-out.html language=enus -->
## TOPIC 00157: GetHTEltfAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethteltfaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethteltfaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the HT-ELTF field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetHTEltfAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsHTEltfAveragePowerMean attribute.ParametersN

### GetHTEltfAveragePowerMean(string, out double)

Gets the average power of the HT-ELTF field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetHTEltfAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsHTEltfAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the HT-ELTF field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethtgfstfaveragepowermean__string-out.html language=enus -->
## TOPIC 00158: GetHTGFStfAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethtgfstfaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-gethtgfstfaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the HT-GF-STF. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetHTGFStfAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsHTGFStfAveragePowerMean attribute.ParametersNam

### GetHTGFStfAveragePowerMean(string, out double)

Gets the average power of the HT-GF-STF. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetHTGFStfAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsHTGFStfAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the HT-GF-STF. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getimpilotsenabled__string-out.html language=enus -->
## TOPIC 00159: GetIMPilotsEnabled(string, out RFmxWlanMXOfdmModAccIMPilotsEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getimpilotsenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getimpilotsenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether interference mitigating pilots are present. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetIMPilotsEnabled(string selectorString, out RFmxWlanMXOfdmModAccIMPilotsEnabled value)RemarksThis method gets the value of OfdmModAccResultsIMPilotsEnabled attribute.ParametersNameTy

### GetIMPilotsEnabled(string, out RFmxWlanMXOfdmModAccIMPilotsEnabled)

Gets whether interference mitigating pilots are present.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetIMPilotsEnabled(string selectorString, out RFmxWlanMXOfdmModAccIMPilotsEnabled value)

#### Remarks

This method gets the value of [OfdmModAccResultsIMPilotsEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxWlanMXOfdmModAccIMPilotsEnabled | Upon return, contains whether interference mitigating pilots are present. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlsigparitycheckstatus__string-out.html language=enus -->
## TOPIC 00160: GetLSigParityCheckStatus(string, out RFmxWlanMXOfdmModAccLSigParityCheckStatus)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlsigparitycheckstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlsigparitycheckstatus__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetLSigParityCheckStatus(string selectorString, out RFmxWlanM

### GetLSigParityCheckStatus(string, out RFmxWlanMXOfdmModAccLSigParityCheckStatus)

Gets whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetLSigParityCheckStatus(string selectorString, out RFmxWlanMXOfdmModAccLSigParityCheckStatus value)

#### Remarks

This method gets the value of [OfdmModAccResultsLSigParityCheckStatus](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxWlanMXOfdmModAccLSigParityCheckStatus | Upon return, contains whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlsigpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00161: GetLSigPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlsigpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlsigpeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetLSigPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsLSigPeakPowerMaximum attribute.Parameters

### GetLSigPeakPowerMaximum(string, out double)

Gets the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetLSigPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsLSigPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlstfaveragepowermean__string-out.html language=enus -->
## TOPIC 00162: GetLStfAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlstfaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlstfaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the L-STF or STF field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetLStfAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsLStfAveragePowerMean attribute.Parameters

### GetLStfAveragePowerMean(string, out double)

Gets the average power of the L-STF or STF field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetLStfAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsLStfAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the L-STF or STF field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlstfpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00163: GetLStfPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlstfpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getlstfpeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the L-STF or STF field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetLStfPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsLStfPeakPowerMaximum attribute.ParametersNam

### GetLStfPeakPowerMaximum(string, out double)

Gets the peak power of the L-STF or STF field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetLStfPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsLStfPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the L-STF or STF field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getltfsize__string-out.html language=enus -->
## TOPIC 00164: GetLtfSize(string, out RFmxWlanMXOfdmLtfSize)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getltfsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getltfsize__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the HE-LTF size, EHT-LTF or UHR-LTF size when you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11ax or Standard802_11be or Standard802_11bn , respectively. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetLtfSize(string selectorString, out RFmxWlanMXOfdmLtf

### GetLtfSize(string, out RFmxWlanMXOfdmLtfSize)

Gets the HE-LTF size, EHT-LTF or UHR-LTF size when you set the [SetStandard(string, RFmxWlanMXStandard)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setstandard__string-rfmxwlanmxstandard.html) method to [Standard802_11ax](nationalinstruments-rfmx-wlanmx-rfmxwlanmxstandard.html) or [Standard802_11be](nationalinstruments-rfmx-wlanmx-rfmxwlanmxstandard.html) or [Standard802_11bn](nationalinstruments-rfmx-wlanmx-rfmxwlanmxstandard.html) , respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetLtfSize(string selectorString, out RFmxWlanMXOfdmLtfSize value)

#### Remarks

This method gets the value of [OfdmModAccResultsLtfSize](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxWlanMXOfdmLtfSize | Upon return, contains the HE-LTF size, EHT-LTF or UHR-LTF size when you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11ax or Standard802_11be or Standard802_11bn , respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getnumberofsigsymbols__string-out.html language=enus -->
## TOPIC 00165: GetNumberOfSigSymbols(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getnumberofsigsymbols__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getnumberofsigsymbols__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfSigSymbols(string selectorString, out int value)

### GetNumberOfSigSymbols(string, out int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfSigSymbols(string selectorString, out int value)

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getrutype__string-out.html language=enus -->
## TOPIC 00166: GetRUType(string, out RFmxWlanMXOfdmModAccRUType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getrutype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getrutype__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetRUType(string selectorString, out RFmxWlanMXOfdmModAccRUType value)

### GetRUType(string, out RFmxWlanMXOfdmModAccRUType)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetRUType(string selectorString, out RFmxWlanMXOfdmModAccRUType value)

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunequalmodulationenabled__string-out.html language=enus -->
## TOPIC 00167: GetUnequalModulationEnabled(string, out RFmxWlanMXOfdmModAccUnequalModulationEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunequalmodulationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunequalmodulationenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether unequal modulation is enabled for a specified user. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUnequalModulationEnabled(string selectorString, out RFmxWlanMXOfdmModAccUnequalModulationEnabled value)RemarksThis method gets the value of OfdmModAccResultsUnequalModulatio

### GetUnequalModulationEnabled(string, out RFmxWlanMXOfdmModAccUnequalModulationEnabled)

Gets whether unequal modulation is enabled for a specified user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUnequalModulationEnabled(string selectorString, out RFmxWlanMXOfdmModAccUnequalModulationEnabled value)

#### Remarks

This method gets the value of [OfdmModAccResultsUnequalModulationEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and User number. Example: "User0", "result::r1/User0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out RFmxWlanMXOfdmModAccUnequalModulationEnabled | Upon return, contains whether unequal modulation is enabled for a specified user. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunequalmodulationpatternindex__string-out.html language=enus -->
## TOPIC 00168: GetUnequalModulationPatternIndex(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunequalmodulationpatternindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunequalmodulationpatternindex__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets unequal modulation pattern for a specified user. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUnequalModulationPatternIndex(string selectorString, out int value)RemarksThis method gets the value of OfdmModAccResultsUnequalModulationPatternIndex attribute.ParametersNameTypeDescr

### GetUnequalModulationPatternIndex(string, out int)

Gets unequal modulation pattern for a specified user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUnequalModulationPatternIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [OfdmModAccResultsUnequalModulationPatternIndex](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and User number. Example: "User0", "result::r1/User0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out int | Upon return, contains unequal modulation pattern for a specified user. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunusedtoneerrormarginruindex__string-out.html language=enus -->
## TOPIC 00169: GetUnusedToneErrorMarginRUIndex(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunusedtoneerrormarginruindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunusedtoneerrormarginruindex__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 26-tone RU index corresponding to the GetUnusedToneErrorMargin(string, out double) result. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUnusedToneErrorMarginRUIndex(string selectorString, out int value)RemarksThis method gets the value of OfdmModAccResultsUnusedToneErrorMar

### GetUnusedToneErrorMarginRUIndex(string, out int)

Gets the 26-tone RU index corresponding to the [GetUnusedToneErrorMargin(string, out double)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getunusedtoneerrormargin__string-out.html) result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUnusedToneErrorMarginRUIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [OfdmModAccResultsUnusedToneErrorMarginRUIndex](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the 26-tone RU index corresponding to the GetUnusedToneErrorMargin(string, out double) result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigaveragepowermean__string-out.html language=enus -->
## TOPIC 00170: GetUSigAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the U-SIG field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUSigAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsUSigAveragePowerMean attribute.ParametersNameTyp

### GetUSigAveragePowerMean(string, out double)

Gets the average power of the U-SIG field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUSigAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsUSigAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the U-SIG field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigcrcstatus__string-out.html language=enus -->
## TOPIC 00171: GetUSigCrcStatus(string, out RFmxWlanMXOfdmModAccUSigCrcStatus)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigcrcstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigcrcstatus__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be or the 802.11bn waveform. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUSigCrcStatus(string selectorString, out RFmxWlanMXOfdmModAccUSigCrcStatus value)RemarksThis method gets the value of

### GetUSigCrcStatus(string, out RFmxWlanMXOfdmModAccUSigCrcStatus)

Gets whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be or the 802.11bn waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUSigCrcStatus(string selectorString, out RFmxWlanMXOfdmModAccUSigCrcStatus value)

#### Remarks

This method gets the value of [OfdmModAccResultsUSigCrcStatus](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxWlanMXOfdmModAccUSigCrcStatus | Upon return, contains whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be or the 802.11bn waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00172: GetUSigPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigpeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the U-SIG field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUSigPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsUSigPeakPowerMaximum attribute.ParametersNameTypeDe

### GetUSigPeakPowerMaximum(string, out double)

Gets the peak power of the U-SIG field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUSigPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsUSigPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the U-SIG field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigrmsevmmean__string-out.html language=enus -->
## TOPIC 00173: GetUSigRmsEvmMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigrmsevmmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getusigrmsevmmean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetUSigRmsEvmMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsUSigRmsEvmMean attribute.P

### GetUSigRmsEvmMean(string, out double)

Gets the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetUSigRmsEvmMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsUSigRmsEvmMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getvhtstfaveragepowermean__string-out.html language=enus -->
## TOPIC 00174: GetVhtStfAveragePowerMean(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getvhtstfaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getvhtstfaveragepowermean__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the VHT-STF field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetVhtStfAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsVhtStfAveragePowerMean attribute.ParametersN

### GetVhtStfAveragePowerMean(string, out double)

Gets the average power of the VHT-STF field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetVhtStfAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsVhtStfAveragePowerMean](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power of the VHT-STF field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getvhtstfpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00175: GetVhtStfPeakPowerMaximum(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getvhtstfpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccresults-getvhtstfpeakpowermaximum__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power of the VHT-STF field. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetVhtStfPeakPowerMaximum(string selectorString, out double value)RemarksThis method gets the value of OfdmModAccResultsVhtStfPeakPowerMaximum attribute.ParametersName

### GetVhtStfPeakPowerMaximum(string, out double)

Gets the peak power of the VHT-STF field. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetVhtStfPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [OfdmModAccResultsVhtStfPeakPowerMaximum](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Segment number. Example: "Segment0", "result::r1/Segment0" or "result::r1/Segment0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power of the VHT-STF field. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXOfdmModAccResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccrutype.html language=enus -->
## TOPIC 00176: RFmxWlanMXOfdmModAccRUType Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccrutype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccrutype.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccRUTypeMembersNameValueDescriptionRru0Dru1

### RFmxWlanMXOfdmModAccRUType Enumeration

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccRUType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rru | 0 |  |
| Dru | 1 |  |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccsigbcrcstatus.html language=enus -->
## TOPIC 00177: RFmxWlanMXOfdmModAccSigBCrcStatus Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccsigbcrcstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccsigbcrcstatus.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccSigBCrcStatusMembersNameValueDescriptionNotApplicable-1Returns that the SIG-B CRC is invalid for the c

### RFmxWlanMXOfdmModAccSigBCrcStatus Enumeration

Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccSigBCrcStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NotApplicable | -1 | Returns that the SIG-B CRC is invalid for the current waveform. |
| Fail | 0 | Returns that the SIG-B CRC failed. |
| Pass | 1 | Returns that the SIG-B CRC passed. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccunequalmodulationenabled.html language=enus -->
## TOPIC 00178: RFmxWlanMXOfdmModAccUnequalModulationEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccunequalmodulationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccunequalmodulationenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether unequal modulation is enabled for a specified user. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmModAccUnequalModulationEnabledMembersNameValueDescriptionFalse0Indicates that unequal modulation is disabled for the specified user. True1Indicates that unequ

### RFmxWlanMXOfdmModAccUnequalModulationEnabled Enumeration

Returns whether unequal modulation is enabled for a specified user.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccUnequalModulationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Indicates that unequal modulation is disabled for the specified user. |
| True | 1 | Indicates that unequal modulation is enabled for the specified user. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccvectoraveragingphasealignmentenabled.html language=enus -->
## TOPIC 00179: RFmxWlanMXOfdmModAccVectorAveragingPhaseAlignmentEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccvectoraveragingphasealignmentenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccvectoraveragingphasealignmentenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXO

### RFmxWlanMXOfdmModAccVectorAveragingPhaseAlignmentEnabled Enumeration

Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the [OfdmModAccAveragingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) method to **True** , when you set the [OfdmModAccAveragingCount](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) method to a value greater than 1, and when you set the [RFmxWlanMXOfdmModAccAveragingType](nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmodaccaveragingtype.html) method to **Vector** . You can set this method to **False** when there is no phase offset between the acquired I/Q data of all averaging counts.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmModAccVectorAveragingPhaseAlignmentEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables phase alignment for the acquired I/Q data across multiple acquisitions. |
| True | 1 | Enables phase alignment for the acquired I/Q data across multiple acquisitions. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmumimoltfmodeenabled.html language=enus -->
## TOPIC 00180: RFmxWlanMXOfdmMUMimoLtfModeEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmumimoltfmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmmumimoltfmodeenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmMUMimoLtfModeEnabledMembersNameValueDescriptionFalse0Specifies that the LTF sequence uses single stream pilots

### RFmxWlanMXOfdmMUMimoLtfModeEnabled Enumeration

Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmMUMimoLtfModeEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that the LTF sequence uses single stream pilots. |
| True | 1 | Specifies that the LTF sequence is HE masked. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmtransmitpowerclass.html language=enus -->
## TOPIC 00181: RFmxWlanMXOfdmTransmitPowerClass Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmtransmitpowerclass.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmtransmitpowerclass.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11p . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmTransmitPowerClassMembersNameValue

### RFmxWlanMXOfdmTransmitPowerClass Enumeration

Specifies the STA transmit power classification as defined in annexture D.2.2 of *IEEE Standard 802.11–2016* , if you set the [SetStandard(string, RFmxWlanMXStandard)](nationalinstruments-rfmx-wlanmx-rfmxwlanmx-setstandard__string-rfmxwlanmxstandard.html) method to [Standard802_11p](nationalinstruments-rfmx-wlanmx-rfmxwlanmxstandard.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmTransmitPowerClass

#### Members

| Name | Value | Description |
| --- | --- | --- |
| A | 0 | Maximum STA Transmit Power is 1 mW. |
| B | 1 | Maximum STA Transmit Power is 10 mW. |
| C | 2 | Maximum STA Transmit Power is 100 mW. |
| D | 3 | Maximum STA Transmit Power is 760 mW. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmunequalmodulationenabled.html language=enus -->
## TOPIC 00182: RFmxWlanMXOfdmUnequalModulationEnabled Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmunequalmodulationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxofdmunequalmodulationenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXOfdmUnequalModulationEnabledMembersNameValueDescriptionFalse0Specifies that Unequal Modulation is disabled. True1Specifies t

### RFmxWlanMXOfdmUnequalModulationEnabled Enumeration

Specifies whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXOfdmUnequalModulationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that Unequal Modulation is disabled. |
| True | 1 | Specifies that Unequal Modulation is enabled. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getacquisitionlength__string-out.html language=enus -->
## TOPIC 00183: GetAcquisitionLength(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getacquisitionlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getacquisitionlength__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetAcquisitionLength(string selectorString, out double value)RemarksThis method gets the value of PowerRampAcquisitionLength at

### GetAcquisitionLength(string, out double)

Gets the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetAcquisitionLength(string selectorString, out double value)

#### Remarks

This method gets the value of [PowerRampAcquisitionLength](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1 millisecond.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00184: GetAveragingCount(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled) method to True . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingenabled__string-rfmxwlanmxpowerrampaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampaveragingenabled.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [PowerRampAveragingCount](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled) method to True . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00185: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of PowerRampMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionsele

### GetMeasurementEnabled(string, out bool)

Gets whether to enable PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [PowerRampMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00186: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of PowerRampNumberOfAnalysisThreads attribute.The default va

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [PowerRampNumberOfAnalysisThreads](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00187: SetAveragingCount(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled) method to True . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of Pow

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingenabled__string-rfmxwlanmxpowerrampaveragingenabled.html) method to [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampaveragingenabled.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [PowerRampAveragingCount](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled) method to True . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingenabled__string-rfmxwlanmxpowerrampaveragingenabled.html language=enus -->
## TOPIC 00188: SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingenabled__string-rfmxwlanmxpowerrampaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setaveragingenabled__string-rfmxwlanmxpowerrampaveragingenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets if averaging is enabled for PowerRamp measurements. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetAveragingEnabled(string selectorString, RFmxWlanMXPowerRampAveragingEnabled value)RemarksThis method sets the value of PowerRampAveragingEnabled attribute.The default value is False

### SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled)

Sets if averaging is enabled for PowerRamp measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetAveragingEnabled(string selectorString, RFmxWlanMXPowerRampAveragingEnabled value)

#### Remarks

This method sets the value of [PowerRampAveragingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampaveragingenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXPowerRampAveragingEnabled | Specifies if averaging is enabled for PowerRamp measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00189: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of PowerRampMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselector

### SetMeasurementEnabled(string, bool)

Sets whether to enable PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [PowerRampMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00190: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of PowerRampNumberOfAnalysisThreads attribute.The default value

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [PowerRampNumberOfAnalysisThreads](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampresults.html language=enus -->
## TOPIC 00191: RFmxWlanMXPowerRampResults Class

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpowerrampresults.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the PowerRamp measurement results. Derives fromRFmxWlanMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic class RFmxWlanMXPowerRampResults : RFmxWlanMXSubObjectMethodsNameDescriptionFetchFallTrace(string, double, ref AnalogWaveform< float >, ref Anal

### RFmxWlanMXPowerRampResults Class

Provides methods to fetch and read the PowerRamp measurement results.

#### Derives from

- RFmxWlanMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public class RFmxWlanMXPowerRampResults : RFmxWlanMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchFallTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Returns the raw, processed, thresholding and power reference waveforms at the end of a burst. |
| FetchMeasurement(string, double, out double, out double) | Returns the PowerRamp rise time and fall time. |
| FetchRiseTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Returns the raw, processed, threshold and power-reference traces at the beginning of a burst. |
| GetFallTimeMean(string, out double) | Gets the power-ramp fall time of the burst. This value is expressed in seconds. |
| GetRiseTimeMean(string, out double) | Gets the power-ramp rise time of the burst. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html language=enus -->
## TOPIC 00192: RFmxWlanMXPropertyId Enumeration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic enum RFmxWlanMXPropertyIdMembersNameValueDescriptionSelectedPorts10489853Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port

### RFmxWlanMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public enum RFmxWlanMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SelectedPorts | 10489853 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| CenterFrequency | 10485761 | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. On a MIMO session, use segment(n) along with a named or default signal instance as the selector string to configure this method. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| ReferenceLevel | 10485762 | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals. |
| ExternalAttenuation | 10485763 | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help . |
| ReferenceLevelHeadroom | 10489852 | Specifies the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| TriggerType | 10485764 | Specifies the trigger type. |
| DigitalEdgeTriggerSource | 10485765 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . On a MIMO session, this method configures the digital edge trigger on the master port. By default, the Selected Ports method is configured to "segment0/chain0" and is considered as the master port. |
| DigitalEdgeTriggerEdge | 10485766 | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to DigitalEdge . |
| IQPowerEdgeTriggerSource | 10485767 | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . On a MIMO session, configures the IQ Power edge trigger on the master port. By default, the selected port configured to segment0/chain0 is considered as master port. |
| IQPowerEdgeTriggerLevel | 10485768 | Specifies the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxWlanMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute . |
| IQPowerEdgeTriggerLevelType | 10489855 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxWlanMXTriggerType) method to IQPowerEdge . |
| IQPowerEdgeTriggerSlope | 10485769 | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
| TriggerDelay | 10485770 | Specifies the trigger delay time. This value is expressed in seconds. |
| TriggerMinimumQuietTimeMode | 10485771 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 10485772 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| TriggerGateEnabled | 10485802 | Enables time-domain gating of the acquired signal for SEM measurement. |
| TriggerGateLength | 10485803 | Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the SetTriggerGateEnabled(string, RFmxWlanMXTriggerGateEnabled) method to True . |
| Standard | 10485773 | Specifies the signal under analysis as defined in IEEE Standard 802.11 . |
| ChannelBandwidth | 10485774 | Specifies the channel spacing as defined under section 3.1 of IEEE Standard 802.11–2016 (pp. 130) . This value is specified in Hz. |
| NumberOfFrequencySegments | 10485775 | Specifies the number of frequency segments for 802.11ac and 802.11ax signals. |
| NumberOfReceiveChains | 10485776 | Specifies the number of receive chains for OFDM standards. |
| OfdmFrequencySegmentIndex | 10485780 | Specifies the frequency segment index to be analyzed in an 80+80 MHz 802.11ax signal. You must set this method to either of the valid values when you want to analyze one of the two segments. |
| OfdmTransmitPowerClass | 10485781 | Specifies the STA transmit power classification as defined in annexture D.2.2 of IEEE Standard 802.11–2016 , if you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11p . |
| OfdmFrequencyBand | 10485782 | Specifies the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n – 2009 . |
| OfdmAutoPpduTypeDetectionEnabled | 10485799 | Specifies whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement. |
| OfdmPpduType | 10485783 | Specifies the PPDU type when you set the SetOfdmAutoPpduTypeDetectionEnabled(string, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) method to False . |
| OfdmHeaderDecodingEnabled | 10485800 | Specifies whether to enable the decoding of the header fields in the PPDU. |
| OfdmSigCompressionEnabled | 10485818 |  |
| OfdmNumberOfUsers | 10485784 | Specifies the number of users in a multi-user (MU) PPDU. |
| OfdmMcsIndex | 10485785 | Specifies the modulation and coding scheme (MCS) index or the data rate when you set the SetOfdmHeaderDecodingEnabled(string, RFmxWlanMXOfdmHeaderDecodingEnabled) method to False . |
| OfdmScramblerSeed | 10485821 | Specifies the scrambler seed for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
| OfdmFecCodingType | 10485810 | Specifies the type of forward error correction (FEC) coding used. |
| OfdmRUSize | 10485786 | Specifies the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals. |
| OfdmRUOffsetMruIndex | 10485787 | Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of IEEE P802.11bn/D1.3 . |
| OfdmRUType | 10485823 | Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). |
| OfdmDistributionBandwidth | 10485824 | Specifies the bandwidth across which RU subcarriers are distributed, when you set >OFDM RU Type method to dRU. |
| OfdmGuardIntervalType | 10485788 | Specifies the size of the guard interval of OFDM symbols. |
| OfdmLtfSize | 10485789 | Specifies the LTF symbol size. This method is applicable only for 802.11ax, 802.11be, and 802.11bn signals. For 802.11ax Trigger-based PPDU, you must always configure this method. For other signals, you must configure this method, if OFDMHeaderDecodingEnabled is False. |
| OfdmPreFecPaddingFactor | 10485811 | Specifies the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. |
| OfdmLdpcExtraSymbolSegment | 10485812 | Specifies the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU. |
| OfdmPEDisambiguity | 10485809 | Specifies the packet extension disambiguity information. |
| OfdmStbcEnabled | 10485813 | Specifies whether space-time block coding is enabled. This method is applicable only for 802.11ax TB PPDU. |
| OfdmNumberOfSpaceTimeStreams | 10485790 | Specifies the number of space time streams. |
| OfdmSpaceTimeStreamOffset | 10485791 | Specifies the space time stream offset. |
| OfdmNumberOfHESigBSymbols | 10485792 | Specifies the number of HE-SIG-B symbols. |
| OfdmNumberOfSigSymbols | 10485819 | Specifies the number of SIG symbols. This method is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. |
| OfdmDcmEnabled | 10485793 | Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. |
| Ofdm2xLdpcEnabled | 10485825 | Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. |
| OfdmIMPilotsEnabled | 10485826 | Specifies whether inteference mitigating pilots are present in 802.11bn MU PPDU signals. |
| OfdmUnequalModulationEnabled | 10485827 | Specifies whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals. |
| OfdmUnequalModulationPatternIndex | 10485828 | Specifies the unequal modulation pattern for the user. Valid values are between 0 and number of space time streams-1. |
| OfdmNumberOfLtfSymbols | 10485794 | Specifies the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. |
| OfdmMUMimoLtfModeEnabled | 10485801 | Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. |
| OfdmPreamblePuncturingEnabled | 10485807 | Specifies whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured. |
| OfdmPreamblePuncturingBitmap | 10485808 | Specifies the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits. |
| OfdmAutoPhaseRotationDetectionEnabled | 10485820 | Specifies whether to enable auto detection of phase rotation coefficients. |
| OfdmPhaseRotationCoefficient1 | 10485815 | Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0 . |
| OfdmPhaseRotationCoefficient2 | 10485816 | Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0 . |
| OfdmPhaseRotationCoefficient3 | 10485817 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 . |
| DetectedStandard | 10485777 | Returns the standard detected by the AutoDetectSignal(string, double) function. |
| DetectedChannelBandwidth | 10485778 | Returns the channel bandwidth detected by the AutoDetectSignal(string, double) . The value is expressed in Hz. |
| DetectedBurstLength | 10485779 | Returns the duration of the packet detected by the AutoDetectSignal(string, double) function. The value is expressed in seconds. |
| DsssModAccMeasurementEnabled | 10498058 | Specifies whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016 . |
| DsssModAccAcquisitionLengthMode | 10498059 | Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. |
| DsssModAccAcquisitionLength | 10498060 | Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the SetAcquisitionLengthMode(string, RFmxWlanMXDsssModAccAcquisitionLengthMode) method to Manual . This value is expressed in seconds. |
| DsssModAccMeasurementOffset | 10498061 | Specifies the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips. |
| DsssModAccMaximumMeasurementLength | 10498062 | Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. |
| DsssModAccPulseShapingFilterType | 10498063 | Specifies the type of pulse shaping filter used at the transmitter. This method is ignored when you set the SetEqualizationEnabled(string, RFmxWlanMXDsssModAccEqualizationEnabled) method to True . |
| DsssModAccPulseShapingFilterParameter | 10498064 | Specifies the value of the filter roll-off when you set the Pulse Shaping Filter Type method to Raised Cosine or Root Raised Cosine. This method is ignored if you set the Pulse Shaping Filter Type method to Rectangular. |
| DsssModAccEqualizationEnabled | 10498065 | Specifies whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation. |
| DsssModAccBurstStartDetectionEnabled | 10498170 | Specifies whether the measurement detects the rising edge of a burst in the acquired waveform. |
| DsssModAccEvmUnit | 10498066 | Specifies the unit for the EVM results. |
| DsssModAccPowerMeasurementEnabled | 10498067 | Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU. |
| DsssModAccPowerNumberOfCustomGates | 10498068 | Specifies the number of custom gates used for power measurement. |
| DsssModAccPowerCustomGateStartTime | 10498069 | Specifies the start time of the custom power gate. This value is expressed in seconds. |
| DsssModAccPowerCustomGateStopTime | 10498070 | Specifies the stop time for the custom power gate. This value is expressed in seconds. |
| DsssModAccFrequencyErrorCorrectionEnabled | 10498092 | Specifies whether to enable frequency error correction. |
| DsssModAccChipClockErrorCorrectionEnabled | 10498093 | Specifies whether to enable chip clock error correction. |
| DsssModAccIQOriginOffsetCorrectionEnabled | 10498094 | Specifies whether to enable I/Q origin offset correction. |
| DsssModAccSpectrumInverted | 10498171 | Specifies whether the spectrum of the measured signal is inverted. |
| DsssModAccDataDecodingEnabled | 10498172 | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
| DsssModAccAveragingEnabled | 10498095 | Specifies whether to enable averaging for DSSSModAcc measurement. |
| DsssModAccAveragingCount | 10498096 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXDsssModAccAveragingEnabled) method to True . |
| DsssModAccAllTracesEnabled | 10498097 | Specifies whether to enable all the traces computed by DSSSModAcc measurement. |
| DsssModAccNumberOfAnalysisThreads | 10498161 | Specifies the maximum number of threads used for parallelism for DSSSModAcc measurement. |
| DsssModAccResultsRmsEvmMean | 10498098 | Returns the RMS EVM of the burst. This value is expressed as a percentage or in dB. |
| DsssModAccResultsPeakEvm802_11_2016Mean | 10498108 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
| DsssModAccResultsPeakEvm802_11_2016Maximum | 10498109 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
| DsssModAccResultsPeakEvm802_11_2007Mean | 10498101 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
| DsssModAccResultsPeakEvm802_11_2007Maximum | 10498102 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
| DsssModAccResultsPeakEvm802_11_1999Mean | 10498099 | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. |
| DsssModAccResultsPeakEvm802_11_1999Maximum | 10498100 | Returns the peak EVM of the burst. This value is expressed as percentage or in dB. |
| DsssModAccResultsNumberOfChipsUsed | 10498125 | Returns the number of chips used for the DSSSModAcc measurement. |
| DsssModAccResultsFrequencyErrorMean | 10498126 | Returns the carrier frequency error of the transmitter. This value is expressed in Hz. |
| DsssModAccResultsChipClockErrorMean | 10498130 | Returns the chip clock error of the transmitter. This value is expressed in parts per million (ppm). |
| DsssModAccResultsIQGainImbalanceMean | 10498131 | Returns the I/Q gain imbalance. This value is expressed in dB. |
| DsssModAccResultsIQQuadratureErrorMean | 10498135 | Returns the I/Q quadrature error. This value is expressed in degrees. |
| DsssModAccResultsIQOriginOffsetMean | 10498139 | Returns the I/Q origin offset. This value is expressed in dB. |
| DsssModAccResultsRmsMagnitudeErrorMean | 10498146 | Returns the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage. |
| DsssModAccResultsRmsPhaseErrorMean | 10498147 | Returns the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees. |
| DsssModAccResultsPreambleAveragePowerMean | 10498162 | Returns the average power of the preamble field of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsPreamblePeakPowerMaximum | 10498163 | Returns the peak power of the preamble field of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsHeaderAveragePowerMean | 10498164 | Returns the average power of the header field of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsHeaderPeakPowerMaximum | 10498165 | Returns the peak power of the header field of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsDataAveragePowerMean | 10498166 | Returns the average power of the data field of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsDataPeakPowerMaximum | 10498167 | Returns the peak power of the data field of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsPpduAveragePowerMean | 10498168 | Returns the average power of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsPpduPeakPowerMaximum | 10498169 | Returns the peak power of the PPDU. This value is expressed in dBm. |
| DsssModAccResultsCustomGateAveragePowerMean | 10498110 | Returns the average power of the custom gate. This value is expressed in dBm. |
| DsssModAccResultsCustomGatePeakPowerMaximum | 10498111 | Returns the peak power of the custom gate. This value is expressed in dBm. |
| DsssModAccResultsDataModulationFormat | 10498152 | Returns the data modulation format results of the analyzed waveform. |
| DsssModAccResultsPayloadLength | 10498153 | Returns the payload length of the acquired burst. This value is expressed in bytes. |
| DsssModAccResultsPreambleType | 10498154 | Returns the detected preamble type of the acquired burst. |
| DsssModAccResultsLockedClocksBit | 10498156 | Returns the value of the locked clocks bit in the Long PHY SERVICE field. |
| DsssModAccResultsHeaderCrcStatus | 10498157 | Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016 . |
| DsssModAccResultsPsduCrcStatus | 10498158 | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
| OfdmModAccMeasurementEnabled | 10502144 | Specifies whether to enable OFDMModAcc measurement for OFDM based standards. |
| OfdmModAccAveragingEnabled | 10502146 | Specifies whether to enable averaging for OFDMModAcc measurements. |
| OfdmModAccAveragingCount | 10502147 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXOfdmModAccAveragingEnabled) method to True . |
| OfdmModAccAveragingType | 10502316 | Specifies the averaging type for the OFDMModAcc measurement. This method is considered only when you set the OfdmModAccAveragingEnabled method to True and when you set the OfdmModAccAveragingCount method to a value greater than 1. |
| OfdmModAccVectorAveragingTimeAlignmentEnabled | 10502317 | Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXOfdmModAccAveragingType method to Vector . You can set this method to False when there is no time offset between the acquired I/Q data of all averaging counts. |
| OfdmModAccVectorAveragingPhaseAlignmentEnabled | 10502318 | Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. This method is considered only when you set the OfdmModAccAveragingEnabled method to True , when you set the OfdmModAccAveragingCount method to a value greater than 1, and when you set the RFmxWlanMXOfdmModAccAveragingType method to Vector . You can set this method to False when there is no phase offset between the acquired I/Q data of all averaging counts. |
| OfdmModAccMeasurementMode | 10502246 | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement. |
| OfdmModAccEvmReferenceDataSymbolsMode | 10502291 | Specifies whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation. |
| OfdmModAccEvmUnit | 10502152 | Specifies the unit for EVM results. |
| OfdmModAccAcquisitionLengthMode | 10502153 | Specifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc properties. |
| OfdmModAccAcquisitionLength | 10502154 | Specifies the length of the waveform to be acquired for the OFDMModAcc measurement, when you set the SetAcquisitionLengthMode(string, RFmxWlanMXOfdmModAccAcquisitionLengthMode) method to Manual . This value is expressed in seconds. |
| OfdmModAccMeasurementOffset | 10502155 | Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols. |
| OfdmModAccMaximumMeasurementLength | 10502156 | Specifies the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols. |
| OfdmModAccCombinedSignalDemodulationEnabled | 10502346 | Specifies whether to enable demodulation of the signal that is formed by combining signals from multiple transmitter chains. |
| OfdmModAccReferenceDataConstellationIdentifier | 10502347 | Identifies the reference files used for combined signal demodulation. The value of this method must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
| OfdmModAccBurstStartDetectionEnabled | 10502277 | Specifies whether the measurement detects a rising edge of a burst in the acquired waveform. |
| OfdmModAccFrequencyErrorEstimationMethod | 10502270 | Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal. |
| OfdmModAccCommonClockSourceEnabled | 10502157 | Specifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock. |
| OfdmModAccCommonPilotErrorScalingReference | 10502353 | Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE. |
| OfdmModAccAmplitudeTrackingEnabled | 10502158 | Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol. |
| OfdmModAccPhaseTrackingEnabled | 10502159 | Specifies whether to enable pilot-based common phase error correction per OFDM data symbol. |
| OfdmModAccSymbolClockErrorCorrectionEnabled | 10502160 | Specifies whether to enable symbol clock error correction. |
| OfdmModAccSpectrumInverted | 10502266 | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
| OfdmModAccChannelEstimationType | 10502161 | Specifies the fields in the PPDU used to estimate the channel frequency response. |
| OfdmModAccChannelEstimationInterpolationType | 10502250 | Specifies the interpolation type and/or smoothing type used on the channel estimates. |
| OfdmModAccChannelEstimationSmoothingLength | 10502251 | Specifies the length of the triangular-weighted moving window across subcarriers that is used for averaging the channel estimate. |
| OfdmModAccChannelEstimationRelativeDelaySpread | 10502327 | Specifies the expected channel delay spread relative to the OFDM symbol length. |
| OfdmModAccChannelEstimationLtfAveragingEnabled | 10502368 | Specifies whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This method is only applicable for 11ax, 11be and 11bn standards. |
| OfdmModAccChannelEstimationLLtfEnabled | 10502279 | Specifies whether to use the legacy channel estimation field for combining with the reference channel frequency response. |
| OfdmModAccPowerMeasurementEnabled | 10502167 | Specifies whether power measurements are performed. |
| OfdmModAccPowerNumberOfCustomGates | 10502168 | Specifies the number of custom gates for power measurement. |
| OfdmModAccPowerCustomGateStartTime | 10502169 | Specifies the start time of the custom power gate. This value is expressed in seconds. |
| OfdmModAccPowerCustomGateStopTime | 10502170 | Specifies the stop time of the custom power gate, and must be greater than the corresponding SetPowerCustomGateStartTime(string, double) method. This value is expressed in seconds. |
| OfdmModAccChannelMatrixPowerEnabled | 10502285 | Specifies whether the channel frequency response matrix power measurements are enabled. This enables cross-power measurements for MIMO signals and user-power measurements for MU signals. |
| OfdmModAccIQImpairmentsEstimationEnabled | 10502267 | Specifies whether to enable the estimation of I/Q gain imbalance, I/Q quadrature error, and I/Q timing skew impairments. |
| OfdmModAccIQImpairmentsModel | 10502171 | Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. |
| OfdmModAccIQGainImbalanceCorrectionEnabled | 10502172 | Specifies whether to enable I/Q gain imbalance correction. |
| OfdmModAccIQQuadratureErrorCorrectionEnabled | 10502173 | Specifies whether to enable I/Q quadrature error correction. |
| OfdmModAccIQTimingSkewCorrectionEnabled | 10502174 | Specifies whether to enable I/Q timing skew correction. |
| OfdmModAccIQImpairmentsPerSubcarrierEnabled | 10502271 | Specifies whether to estimate I/Q impairments independently for each subcarrier. |
| OfdmModAccUnusedToneErrorMaskReference | 10502252 | Specifies the reference used to create the unused tone error mask for the 802.11ax, 802.11be or 802.11bn TB PPDU signals. |
| OfdmModAccDataDecodingEnabled | 10502283 | Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). |
| OfdmModAccNoiseCompensationEnabled | 10502247 | Specifies whether the contribution of the instrument noise is compensated for EVM computation. |
| OfdmModAccNoiseCompensationInputPowerCheckEnabled | 10502248 | Specifies whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |
| OfdmModAccNoiseCompensationReferenceLevelCoercionLimit | 10502249 | Specifies the reference level coercion limit for noise compensation. This value is expressed in dB. |
| OfdmModAccOptimizeDynamicRangeForEvmEnabled | 10502268 | Specifies whether to optimize the analyzer's dynamic range for the EVM measurement. |
| OfdmModAccOptimizeDynamicRangeForEvmMargin | 10502269 | Specifies the margin above the reference level you specify when you set the SetOptimizeDynamicRangeForEvmEnabled(string, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled) method to True . This value is expressed in dB. |
| OfdmModAccAutoLevelAllowOverflow | 10502321 | Specifies whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |
| OfdmModAccAllTracesEnabled | 10502149 | Specifies whether to enable all the traces computed by the OFDMModAcc measurement. |
| OfdmModAccNumberOfAnalysisThreads | 10502148 | Specifies the maximum number of threads used for parallelism for the OFDMModAcc measurement. |
| OfdmModAccResultsCompositeRmsEvmMean | 10502254 | Returns the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set OFDMModAccAveragingEnabled method to True, this method returns the mean of RMS EVM results for the specified user that is computed for each averaging count. |
| OfdmModAccResultsCompositeDataRmsEvmMean | 10502255 | Returns the RMS EVM of data-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of data RMS EVM results computed for each averaging count. |
| OfdmModAccResultsCompositePilotRmsEvmMean | 10502256 | Returns the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method is set to True, this method returns the mean of pilot RMS EVM results computed for each averaging count. |
| OfdmModAccResultsStreamRmsEvmMean | 10502260 | Returns the stream RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of Stream RMS EVM results computed for each averaging count. |
| OfdmModAccResultsStreamRmsEvmMaximum | 10502294 | This enum value has been deprecated. |
| OfdmModAccResultsStreamRmsEvmMinimum | 10502295 | This enum value has been deprecated. |
| OfdmModAccResultsStreamDataRmsEvmMean | 10502261 | Returns the stream RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of Stream Data RMS EVM results computed for each averaging count. |
| OfdmModAccResultsStreamPilotRmsEvmMean | 10502262 | Returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of stream Pilot RMS EVM results computed for each averaging count. |
| OfdmModAccResultsChainRmsEvmMean | 10502257 | Returns the chain RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of chain RMS EVM results computed for each averaging count. |
| OfdmModAccResultsChainRmsEvmMaximum | 10502296 | This enum value has been deprecated. |
| OfdmModAccResultsChainRmsEvmMinimum | 10502297 | This enum value has been deprecated. |
| OfdmModAccResultsChainDataRmsEvmMean | 10502258 | Returns the chain RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of data chain RMS EVM results computed for each averaging count. |
| OfdmModAccResultsChainPilotRmsEvmMean | 10502259 | Returns the chain RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of pilot chain RMS EVM results computed for each averaging count. |
| OfdmModAccResultsUserStreamRmsEvmMean | 10502263 | Returns the RMS EVM of all subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. This result is applicable for MU PPDU. When you set OFDMModAccAveragingEnabled method to True, this method returns the mean of User Stream RMS EVM results for the specified user that is computed for each averaging count. |
| OfdmModAccResultsUserStreamRmsEvmMaximum | 10502298 | This enum value has been deprecated. |
| OfdmModAccResultsUserStreamRmsEvmMinimum | 10502299 | This enum value has been deprecated. |
| OfdmModAccResultsUserStreamDataRmsEvmMean | 10502264 | Returns the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. This result is applicable for MU PPDU. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of data RMS EVM results for the specified user that is computed for each averaging count. |
| OfdmModAccResultsUserStreamPilotRmsEvmMean | 10502265 | Returns the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB. This result is applicable for MU PPDU. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of pilot RMS EVM results for the specified user that is computed for each averaging count. |
| OfdmModAccResultsLSigRmsEvmMean | 10502331 | Returns the RMS EVM of subcarriers in the L-SIG symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsSigRmsEvmMean | 10502332 | Returns the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsSigBRmsEvmMean | 10502333 | Returns the RMS EVM of subcarriers in the SIG-B symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsUSigRmsEvmMean | 10502334 | Returns the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsEhtSigRmsEvmMean | 10502335 | Returns the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsUhrSigRmsEvmMean | 10502354 | Returns the RMS EVM of subcarriers in the UHR-SIG symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsElrSigRmsEvmMean | 10502356 | Returns the RMS EVM of subcarriers in the ELR-SIG symbol. This value is expressed as a percentage or in dB. |
| OfdmModAccResultsLStfAveragePowerMean | 10502202 | Returns the average power of the L-STF or STF field. This value is expressed in dBm. |
| OfdmModAccResultsLStfPeakPowerMaximum | 10502203 | Returns the peak power of the L-STF or STF field. This value is expressed in dBm. |
| OfdmModAccResultsLLtfAveragePowerMean | 10502204 | Returns the average power of the L-LTF or LTF field. This value is expressed in dBm. |
| OfdmModAccResultsLLtfPeakPowerMaximum | 10502205 | Returns the peak power of the L-LTF or LTF field. This value is expressed in dBm. |
| OfdmModAccResultsLSigAveragePowerMean | 10502206 | Returns the average power of the L-SIG or SIGNAL field. This value is expressed in dBm. |
| OfdmModAccResultsLSigPeakPowerMaximum | 10502207 | Returns the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm. |
| OfdmModAccResultsRLSigAveragePowerMean | 10502208 | Returns the average power of the RL-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsRLSigPeakPowerMaximum | 10502209 | Returns the peak power of the RL-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsHTSigAveragePowerMean | 10502210 | Returns the average power of the HT-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsHTSigPeakPowerMaximum | 10502211 | Returns the peak power of the HT-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsVhtSigAAveragePowerMean | 10502212 | Returns the average power of the VHT-SIG-A field. This value is expressed in dBm. |
| OfdmModAccResultsVhtSigAPeakPowerMaximum | 10502213 | Returns the peak power of the VHT-SIG-A field. This value is expressed in dBm. |
| OfdmModAccResultsHESigAAveragePowerMean | 10502214 | Returns the average power of the HE-SIG-A field. This value is expressed in dBm. |
| OfdmModAccResultsHESigAPeakPowerMaximum | 10502215 | Returns the peak power of the HE-SIG-A field. This value is expressed in dBm. |
| OfdmModAccResultsUSigAveragePowerMean | 10502336 | Returns the average power of the U-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsUSigPeakPowerMaximum | 10502337 | Returns the peak power of the U-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsElrMarkAveragePowerMean | 10502366 | Returns the average power of the ELR-MARK field. This value is expressed in dBm. |
| OfdmModAccResultsElrMarkPeakPowerMaximum | 10502367 | Returns the peak power of the ELR-MARK field. This value is expressed in dBm. |
| OfdmModAccResultsVhtSigBAveragePowerMean | 10502216 | Returns the average power of the VHT-SIG-B field. This value is expressed in dBm. |
| OfdmModAccResultsVhtSigBPeakPowerMaximum | 10502217 | Returns the peak power of the VHT-SIG-B field. This value is expressed in dBm. |
| OfdmModAccResultsHESigBAveragePowerMean | 10502218 | Returns the average power of the HE-SIG-B field. This value is expressed in dBm. |
| OfdmModAccResultsHESigBPeakPowerMaximum | 10502219 | Returns the peak power of the HE-SIG-B field. This value is expressed in dBm. |
| OfdmModAccResultsEhtSigAveragePowerMean | 10502338 | Returns the average power of the EHT-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsEhtSigPeakPowerMaximum | 10502339 | Returns the peak power of the EHT-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsUhrSigAveragePowerMean | 10502362 | Returns the average power of the UHR-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsUhrSigPeakPowerMaximum | 10502363 | Returns the peak power of the UHR-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsElrSigAveragePowerMean | 10502364 | Returns the average power of the ELR-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsElrSigPeakPowerMaximum | 10502365 | Returns the peak power of the ELR-SIG field. This value is expressed in dBm. |
| OfdmModAccResultsHTStfAveragePowerMean | 10502220 | Returns the average power of the HT-STF field. This value is expressed in dBm. |
| OfdmModAccResultsHTStfPeakPowerMaximum | 10502221 | Returns the peak power of the HT-STF field. This value is expressed in dBm. |
| OfdmModAccResultsHTGFStfAveragePowerMean | 10502222 | Returns the average power of the HT-GF-STF. This value is expressed in dBm. |
| OfdmModAccResultsHTGFStfPeakPowerMaximum | 10502223 | Returns the peak power of the HT-GF-STF. This value is expressed in dBm. |
| OfdmModAccResultsVhtStfAveragePowerMean | 10502224 | Returns the average power of the VHT-STF field. This value is expressed in dBm. |
| OfdmModAccResultsVhtStfPeakPowerMaximum | 10502225 | Returns the peak power of the VHT-STF field. This value is expressed in dBm. |
| OfdmModAccResultsHEStfAveragePowerMean | 10502226 | Returns the average power of the HE-STF field. This value is expressed in dBm. |
| OfdmModAccResultsHEStfPeakPowerMaximum | 10502227 | Returns the peak power of the HE-STF field. This value is expressed in dBm. |
| OfdmModAccResultsEhtStfAveragePowerMean | 10502340 | Returns the average power of the EHT-STF field. This value is expressed in dBm. |
| OfdmModAccResultsEhtStfPeakPowerMaximum | 10502341 | Returns the peak power of the EHT-STF field. This value is expressed in dBm. |
| OfdmModAccResultsUhrStfAveragePowerMean | 10502358 | Returns the average power of the UHR-STF field. This value is expressed in dBm. |
| OfdmModAccResultsUhrStfPeakPowerMaximum | 10502359 | Returns the peak power of the UHR-STF field. This value is expressed in dBm. |
| OfdmModAccResultsHTDltfAveragePowerMean | 10502228 | Returns the average power of the HT-DLTF. This value is expressed in dBm. |
| OfdmModAccResultsHTDltfPeakPowerMaximum | 10502229 | Returns the peak power of the HT-DLTF field. This value is expressed in dBm. |
| OfdmModAccResultsHTEltfAveragePowerMean | 10502230 | Returns the average power of the HT-ELTF field. This value is expressed in dBm. |
| OfdmModAccResultsHTEltfPeakPowerMaximum | 10502231 | Returns the peak power of the HT-ELTF field. This value is expressed in dBm. |
| OfdmModAccResultsVhtLtfAveragePowerMean | 10502232 | Returns the average power of the VHT-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsVhtLtfPeakPowerMaximum | 10502233 | Returns the peak power of the VHT-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsHELtfAveragePowerMean | 10502234 | Returns the average power of the HE-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsHELtfPeakPowerMaximum | 10502235 | Returns the peak power of the HE-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsEhtLtfAveragePowerMean | 10502342 | Returns the average power of the EHT-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsEhtLtfPeakPowerMaximum | 10502343 | Returns the peak power of the EHT-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsUhrLtfAveragePowerMean | 10502360 | Returns the average power of the UHR-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsUhrLtfPeakPowerMaximum | 10502361 | Returns the peak power of the UHR-LTF field. This value is expressed in dBm. |
| OfdmModAccResultsDataAveragePowerMean | 10502236 | Returns the average power of the data field. This value is expressed in dBm. |
| OfdmModAccResultsDataPeakPowerMaximum | 10502237 | Returns the peak power of the data field. This value is expressed in dBm. |
| OfdmModAccResultsPEAveragePowerMean | 10502238 | Returns the average power of the packet extension field. This value is expressed in dBm. |
| OfdmModAccResultsPEPeakPowerMaximum | 10502239 | Returns the peak power of the packet extension field. This value is expressed in dBm. |
| OfdmModAccResultsPpduAveragePowerMean | 10502240 | Returns the average power of the PPDU. This value is expressed in dBm. |
| OfdmModAccResultsPpduPeakPowerMaximum | 10502241 | Returns the peak power of the PPDU. This value is expressed in dBm. |
| OfdmModAccResultsCustomGateAveragePowerMean | 10502242 | Returns the average power of the custom gate. This value is expressed in dBm. |
| OfdmModAccResultsCustomGatePeakPowerMaximum | 10502243 | Returns the peak power of the custom gate. This value is expressed in dBm. |
| OfdmModAccResultsCrossPowerMean | 10502286 | Returns the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. This value is expressed in dB. |
| OfdmModAccResultsChainStreamCrossPowerMean | 10502376 | Returns the stream cross power. The cross power for chain 'k' stream 'm' is the power contribution of stream 'm' in chain 'k'. This value is expressed in dB. |
| OfdmModAccResultsUserPowerMean | 10502287 | Returns the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. This value is expressed in dBm. When you set the OFDMModAccAveragingEnabled method to True, this method returns the mean of chain RMS EVM results computed for each averaging count. |
| OfdmModAccResultsUserPowerMaximum | 10502300 | This enum value has been deprecated. |
| OfdmModAccResultsUserPowerMinimum | 10502301 | This enum value has been deprecated. |
| OfdmModAccResultsStreamPowerMean | 10502348 | Returns average stream power across iterations for combined signal demodulation. This is applicable only if SetCombinedSignalDemodulationEnabled(string, RFmxWlanMXOfdmModAccCombinedSignalDemodulationEnabled) is set to True. |
| OfdmModAccResultsSpectralFlatnessMargin | 10502179 | Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB. |
| OfdmModAccResultsSpectralFlatnessMarginMaximum | 10502302 | This enum value has been deprecated. |
| OfdmModAccResultsSpectralFlatnessMarginMinimum | 10502303 | This enum value has been deprecated. |
| OfdmModAccResultsSpectralFlatnessMarginSubcarrierIndex | 10502180 | Returns the subcarrier index corresponding to the GetSpectralFlatnessMargin(string, out double) result. |
| OfdmModAccResultsUnusedToneErrorMargin | 10502181 | Returns the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB. |
| OfdmModAccResultsUnusedToneErrorMarginRUIndex | 10502182 | Returns the 26-tone RU index corresponding to the GetUnusedToneErrorMargin(string, out double) result. |
| OfdmModAccResultsBurstStartTimeMean | 10502320 | Returns the absolute time corresponding to the detected start of the analyzed burst. The start time is computed with respect to the initial time value of the acquired waveform. This value is expressed in seconds. |
| OfdmModAccResultsNumberOfSymbolsUsed | 10502166 | Returns the number of OFDM symbols used by the measurement. |
| OfdmModAccResultsNoiseCompensationApplied | 10502183 | Returns whether the noise compensation is applied. |
| OfdmModAccResultsFrequencyErrorMean | 10502184 | Returns the carrier frequency error of the transmitter. This value is expressed in Hz. |
| OfdmModAccResultsFrequencyErrorMaximum | 10502304 | This enum value has been deprecated. |
| OfdmModAccResultsFrequencyErrorMinimum | 10502305 | This enum value has been deprecated. |
| OfdmModAccResultsFrequencyErrorCcdf10Percent | 10502185 | Returns the 10% point of Complementary Cumulative Distribution Function (CCDF) of the absolute frequency error. This value is expressed in Hz. |
| OfdmModAccResultsSymbolClockErrorMean | 10502186 | Returns the symbol clock error of the transmitter. |
| OfdmModAccResultsSymbolClockErrorMaximum | 10502306 | This enum value has been deprecated. |
| OfdmModAccResultsSymbolClockErrorMinimum | 10502307 | This enum value has been deprecated. |
| OfdmModAccResultsRelativeIQOriginOffsetMean | 10502187 | Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB. |
| OfdmModAccResultsRelativeIQOriginOffsetMaximum | 10502308 | This enum value has been deprecated. |
| OfdmModAccResultsRelativeIQOriginOffsetMinimum | 10502309 | This enum value has been deprecated. |
| OfdmModAccResultsAbsoluteIQOriginOffsetMean | 10502188 | Returns the absolute I/Q origin offset, which is the power of the DC subcarrier. This value is expressed in dBm. |
| OfdmModAccResultsIQGainImbalanceMean | 10502189 | Returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. This value is expressed in dB. |
| OfdmModAccResultsIQGainImbalanceMaximum | 10502310 | This enum value has been deprecated. |
| OfdmModAccResultsIQGainImbalanceMinimum | 10502311 | This enum value has been deprecated. |
| OfdmModAccResultsIQQuadratureErrorMean | 10502190 | Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees. |
| OfdmModAccResultsIQQuadratureErrorMaximum | 10502312 | This enum value has been deprecated. |
| OfdmModAccResultsIQQuadratureErrorMinimum | 10502313 | This enum value has been deprecated. |
| OfdmModAccResultsIQTimingSkewMean | 10502191 | Returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds. |
| OfdmModAccResultsRmsCommonPhaseErrorMean | 10502192 | Returns the RMS common phase error. |
| OfdmModAccResultsRmsCommonPilotErrorMean | 10502253 | Returns the RMS common pilot error. This value is expressed as a percentage. |
| OfdmModAccResultsPpduType | 10502193 | Returns the PPDU type of the measured signal. |
| OfdmModAccResultsMcsIndex | 10502194 | Returns the MCS index or the data rate of the measured signal. |
| OfdmModAccResultsAggregation | 10502345 | Returns the value of the Aggregation field as decoded from the high-throughput signal (HT-SIG) field of 802.11n signal. |
| OfdmModAccResultsFecCodingType | 10502314 | Returns the FEC coding type for a specified user. |
| OfdmModAccResultsRUSize | 10502195 | Returns the RU or the MRU size. |
| OfdmModAccResultsRUOffsetMruIndex | 10502196 | Returns the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 . |
| OfdmModAccResultsRUType | 10502369 |  |
| OfdmModAccResultsDistributionBandwidth | 10502370 |  |
| OfdmModAccResultsNumberOfUsers | 10502197 | Returns the number of users. |
| OfdmModAccResultsNumberOfHESigBSymbols | 10502198 | Returns the number of HE-SIG-B symbols. |
| OfdmModAccResultsNumberOfSigSymbols | 10502375 |  |
| OfdmModAccResultsGuardIntervalType | 10502199 | Returns the size of the guard interval of OFDM symbols. |
| OfdmModAccResultsLtfSize | 10502200 | Returns the HE-LTF size, EHT-LTF or UHR-LTF size when you set the SetStandard(string, RFmxWlanMXStandard) method to Standard802_11ax or Standard802_11be or Standard802_11bn , respectively. |
| OfdmModAccResultsNumberOfSpaceTimeStreams | 10502201 | Returns the number of space time streams. |
| OfdmModAccResultsSpaceTimeStreamOffset | 10502288 | Returns the space time stream offset. This method is applicable only to 802.11ac, 802.11ax, 802.11be, and 802.11bn signals. |
| OfdmModAccResultsDcmEnabled | 10502315 | Returns whether DCM is enabled for a specified user. |
| OfdmModAccResults2xLdpcEnabled | 10502371 | Returns whether 2xLDPC is enabled for a specified user. |
| OfdmModAccResultsIMPilotsEnabled | 10502372 | Returns whether interference mitigating pilots are present. |
| OfdmModAccResultsUnequalModulationEnabled | 10502373 | Returns whether unequal modulation is enabled for a specified user. |
| OfdmModAccResultsUnequalModulationPatternIndex | 10502374 | Returns unequal modulation pattern for a specified user. |
| OfdmModAccResultsLSigParityCheckStatus | 10502280 | Returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms. |
| OfdmModAccResultsSigCrcStatus | 10502281 | Returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. |
| OfdmModAccResultsSigBCrcStatus | 10502282 | Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. |
| OfdmModAccResultsUSigCrcStatus | 10502289 | Returns whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be or the 802.11bn waveform. |
| OfdmModAccResultsEhtSigCrcStatus | 10502290 | Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform. |
| OfdmModAccResultsUhrSigCrcStatus | 10502355 | Returns whether the cyclic redundancy check (CRC) has passed for the UHR-SIG field of the 802.11bn waveform. |
| OfdmModAccResultsElrSigCrcStatus | 10502357 | Returns whether the cyclic redundancy check (CRC) has passed for the ELR-SIG field of the 802.11bn waveform. |
| OfdmModAccResultsPsduCrcStatus | 10502284 | Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. |
| OfdmModAccResultsScramblerSeed | 10502344 | Returns the detected initial state of the scrambler, which is used to scramble the data bits in the device under test (DUT). RFmx uses the same seed to descramble the received bit-sequence. |
| OfdmModAccResultsPEDuration | 10502293 | Returns the duration of the packet extension field for the 802.11ax, 802.11be and 802.11bn signals. This value is expressed in seconds. |
| OfdmModAccResultsPhaseRotationCoefficient1 | 10502328 | Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0. |
| OfdmModAccResultsPhaseRotationCoefficient2 | 10502329 | Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0. |
| OfdmModAccResultsPhaseRotationCoefficient3 | 10502330 | Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0. |
| SemMeasurementEnabled | 10506240 | Specifies whether to enable the spectral emission mask (SEM) measurement. |
| SemMaskType | 10506242 | Specifies whether the mask used for the SEM measurement is defined either as per the standard or as specified by you. |
| SemCarrierIntegrationBandwidth | 10506245 | Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz. |
| SemNumberOfOffsets | 10506246 | Specifies the number of offset segments for the SEM measurement when you set the SetMaskType(string, RFmxWlanMXSemMaskType) method to Custom . |
| SemOffsetStartFrequency | 10506247 | Specifies the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. |
| SemOffsetStopFrequency | 10506248 | Specifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |
| SemOffsetSideband | 10506249 | Specifies whether the offset segment is present on one side or on both sides of the carrier. |
| SemOffsetRelativeLimitStart | 10506250 | Specifies the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. |
| SemOffsetRelativeLimitStop | 10506251 | Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
| SemSpanAuto | 10506252 | Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. |
| SemSpan | 10506253 | Specifies the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz. |
| SemSweepTimeAuto | 10506257 | Specifies whether the sweep time for the SEM measurement is computed automatically or is configured by you. |
| SemSweepTimeInterval | 10506258 | Specifies the sweep time for the SEM measurement. This value is expressed in seconds. |
| SemAveragingEnabled | 10506259 | Specifies whether to enable averaging for the SEM measurement. |
| SemAveragingCount | 10506260 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXSemAveragingEnabled) method to True . |
| SemAveragingType | 10506261 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
| SemAmplitudeCorrectionType | 10506262 | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| SemAllTracesEnabled | 10506263 | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| SemNumberOfAnalysisThreads | 10506264 | Specifies the maximum number of threads used for parallelism for SEM measurement. |
| SemResultsMeasurementStatus | 10506267 | Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. |
| SemResultsCarrierAbsoluteIntegratedPower | 10506268 | Returns the average power of the carrier channel over the bandwidth indicated by the GetCarrierIntegrationBandwidth(string, out double) method. This value is expressed in dBm. |
| SemResultsCarrierAbsolutePeakPower | 10506270 | Returns the peak power in the carrier channel over the bandwidth indicated by the GetCarrierIntegrationBandwidth(string, out double) method. This value is expressed in dBm. SEM mask level is determined by this result. |
| SemResultsCarrierPeakFrequency | 10506271 | Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. |
| SemResultsLowerOffsetMeasurementStatus | 10506273 | Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. |
| SemResultsLowerOffsetAbsoluteIntegratedPower | 10506274 | Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm. |
| SemResultsLowerOffsetRelativeIntegratedPower | 10506275 | Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
| SemResultsLowerOffsetAbsolutePeakPower | 10506276 | Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. |
| SemResultsLowerOffsetRelativePeakPower | 10506277 | Returns the peak power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
| SemResultsLowerOffsetPeakFrequency | 10506278 | Returns the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz. |
| SemResultsLowerOffsetMargin | 10506279 | Returns the margin from the SEM measurement mask for the lower (negative) offset. This value is expressed in dB. |
| SemResultsLowerOffsetMarginAbsolutePower | 10506280 | Returns the power level of the spectrum corresponding to the result of the GetLowerOffsetMargin(string, out double) method. This value is expressed in dBm. |
| SemResultsLowerOffsetMarginRelativePower | 10506281 | Returns the power level of the spectrum corresponding to the result of the GetLowerOffsetMargin(string, out double) method. This value is expressed in dB. |
| SemResultsLowerOffsetMarginFrequency | 10506282 | Returns the frequency of the spectrum corresponding to the result of the GetLowerOffsetMargin(string, out double) method. This value is expressed in Hz. |
| SemResultsUpperOffsetMeasurementStatus | 10506283 | Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment. |
| SemResultsUpperOffsetAbsoluteIntegratedPower | 10506284 | Returns the average power of the offset (positive) offset channel over the bandwidth determined by the start and stop frequencies of the offset channel. This value is expressed in dBm. |
| SemResultsUpperOffsetRelativeIntegratedPower | 10506285 | Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
| SemResultsUpperOffsetAbsolutePeakPower | 10506286 | Returns the peak power of the offset (positive) offset segment. This value is expressed in dBm. |
| SemResultsUpperOffsetRelativePeakPower | 10506287 | Returns the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB. |
| SemResultsUpperOffsetPeakFrequency | 10506288 | Returns the frequency at which the peak power occurs in the offset (positive) channel. This value is expressed in Hz. |
| SemResultsUpperOffsetMargin | 10506289 | Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB. |
| SemResultsUpperOffsetMarginAbsolutePower | 10506290 | Returns the power level of the spectrum corresponding to the result of the GetUpperOffsetMargin(string, out double) method. This value is expressed in dBm. |
| SemResultsUpperOffsetMarginRelativePower | 10506291 | Returns the power level of the spectrum corresponding to the result of the GetUpperOffsetMargin(string, out double) method. This value is expressed in dB. |
| SemResultsUpperOffsetMarginFrequency | 10506292 | Returns the frequency of the spectrum corresponding to the result of the GetUpperOffsetMargin(string, out double) method. This value is expressed in Hz. |
| TxpMeasurementEnabled | 10489856 | Specifies whether to enable the transmit power (TXP) measurement. |
| TxpMaximumMeasurementInterval | 10489858 | Specifies the maximum measurement interval. This value is expressed in seconds. |
| TxpBurstDetectionEnabled | 10489859 | Specifies whether the measurement detects the start and the end of a WLAN packet automatically. |
| TxpAveragingEnabled | 10489860 | Specifies whether to enable averaging for the TXP measurement. |
| TxpAveragingCount | 10489861 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXTxpAveragingEnabled) method to True . |
| TxpAllTracesEnabled | 10489862 | Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
| TxpNumberOfAnalysisThreads | 10489863 | Specifies the maximum number of threads used for parallelism for TXP measurement. |
| TxpResultsAveragePowerMean | 10489865 | Returns the average power of the acquired signal. This value is expressed in dBm. |
| TxpResultsAveragePowerMaximum | 10489877 | This enum value has been deprecated. |
| TxpResultsAveragePowerMinimum | 10489878 | This enum value has been deprecated. |
| TxpResultsPeakPowerMean | 10489879 | This enum value has been deprecated. |
| TxpResultsPeakPowerMaximum | 10489873 | Returns the peak power of the acquired signal. This value is expressed in dBm. |
| TxpResultsPeakPowerMinimum | 10489880 | This enum value has been deprecated. |
| PowerRampMeasurementEnabled | 10493962 | Specifies whether to enable PowerRamp measurement. |
| PowerRampAcquisitionLength | 10493964 | Specifies the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds. |
| PowerRampAveragingEnabled | 10493972 | Specifies if averaging is enabled for PowerRamp measurements. |
| PowerRampAveragingCount | 10493973 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWlanMXPowerRampAveragingEnabled) method to True . |
| PowerRampAllTracesEnabled | 10493974 | Specifies whether to enable all the traces computed by the PowerRamp measurement. |
| PowerRampNumberOfAnalysisThreads | 10493975 | Specifies the maximum number of threads used for parallelism for PowerRamp measurement. |
| PowerRampResultsRiseTimeMean | 10493976 | Returns the power-ramp rise time of the burst. This value is expressed in seconds. |
| PowerRampResultsFallTimeMean | 10493977 | Returns the power-ramp fall time of the burst. This value is expressed in seconds. |
| AutoLevelInitialReferenceLevel | 10485796 | Specifies the initial reference level which the AutoLevel(string, double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| SampleClockRateFactor | 10485814 | Specifies the factor by which the sample clock rate is multiplied at the transmitter to generate a signal compressed in the frequency domain and expanded in the time domain. |
| LimitedConfigurationChange | 10485797 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| ResultFetchTimeout | 10534912 | Specifies the time, in seconds, to wait before results are available in the RFmxWLAN_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete. |
| OfdmModAccResultsHELtfSize | 10502200 | This enum value has been deprecated. |
| OfdmHELtfSize | 10485789 | This enum value has been deprecated. |
| OfdmNumberHELtfSymbols | 10485794 | This enum value has been deprecated. |
| OfdmRUOffset | 10485787 | This enum value has been deprecated. |
| OfdmModAccResultsRUOffset | 10502196 | This enum value has been deprecated. |
| OfdmModAccChannelEstimationSmoothingEnabled | 10502250 | This enum value has been deprecated. |
| OfdmEhtSigCompressionEnabled | 10485818 | Specifies whether to enable EHT-SIG compression. This method is applicable only for 802.11be MU PPDU signals. |
| OfdmNumberOfEhtSigSymbols | 10485819 |  |

Parent topic:

NationalInstruments.RFmx.WlanMX

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsem-configuration.html language=enus -->
## TOPIC 00193: Configuration

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsem-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsem-configuration.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWlanMXSemConfiguration instance that provides methods to configure the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic RFmxWlanMXSemConfiguration Configuration { get; }

### Configuration

Gets the [RFmxWlanMXSemConfiguration](nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration.html) instance that provides methods to configure the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public [RFmxWlanMXSemConfiguration](nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration.html) Configuration { get; }

Parent topic:

RFmxWlanMXSem Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00194: GetAveragingEnabled(string, out RFmxWlanMXSemAveragingEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetAveragingEnabled(string selectorString, out RFmxWlanMXSemAveragingEnabled value)RemarksThis method gets the value of SemAveragingEnabled attribute.The default value is False .Param

### GetAveragingEnabled(string, out RFmxWlanMXSemAveragingEnabled)

Gets whether to enable averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxWlanMXSemAveragingEnabled value)

#### Remarks

This method gets the value of [SemAveragingEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemaveragingenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXSemAveragingEnabled | Upon return, contains whether to enable averaging for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00195: GetAveragingType(string, out RFmxWlanMXSemAveragingType)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetAveragingType(string selectorString, out RFmxWlanMXSemAveragingType value)RemarksThis method gets the value of SemAve

### GetAveragingType(string, out RFmxWlanMXSemAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetAveragingType(string selectorString, out RFmxWlanMXSemAveragingType value)

#### Remarks

This method gets the value of [SemAveragingType](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemaveragingtype.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWlanMXSemAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00196: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the spectral emission mask (SEM) measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SemMeasurementEnabled attribute.The default value is FALSE.ParametersNameTy

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the spectral emission mask (SEM) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SemMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the spectral emission mask (SEM) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00197: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of SemNumberOfAnalysisThreads attribute.The default value is 1.Par

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [SemNumberOfAnalysisThreads](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getoffsetstopfrequency__string-out.html language=enus -->
## TOPIC 00198: GetOffsetStopFrequency(string, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getoffsetstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-getoffsetstopfrequency__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetOffsetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of SemOffsetStopFrequency attribute.

### GetOffsetStopFrequency(string, out double)

Gets the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetOffsetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetStopFrequency](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 11 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number and segment number. Example: "segment0" or "segment0/offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-setnumberofoffsets__string-int.html language=enus -->
## TOPIC 00199: SetNumberOfOffsets(string, int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-setnumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-setnumberofoffsets__string-int.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of offset segments for the SEM measurement when you set the SetMaskType(string, RFmxWlanMXSemMaskType) method to Custom . SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetNumberOfOffsets(string selectorString, int value)RemarksThis method sets the value of SemNumberOfOff

### SetNumberOfOffsets(string, int)

Sets the number of offset segments for the SEM measurement when you set the [SetMaskType(string, RFmxWlanMXSemMaskType)](nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemconfiguration-setmasktype__string-rfmxwlanmxsemmasktype.html) method to [Custom](nationalinstruments-rfmx-wlanmx-rfmxwlanmxsemmasktype.html) .

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetNumberOfOffsets(string selectorString, int value)

#### Remarks

This method sets the value of [SemNumberOfOffsets](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | int | Specifies the number of offset segments for the SEM measurement when you set the SetMaskType(string, RFmxWlanMXSemMaskType) method to Custom . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-configuremaximummeasurementinterval__string-double.html language=enus -->
## TOPIC 00200: ConfigureMaximumMeasurementInterval(string, double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-configuremaximummeasurementinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-configuremaximummeasurementinterval__string-double.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the maximum measurement interval for the TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int ConfigureMaximumMeasurementInterval(string selectorString, double maximumMeasurementInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The sign

### ConfigureMaximumMeasurementInterval(string, double)

Configures the maximum measurement interval for the TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int ConfigureMaximumMeasurementInterval(string selectorString, double maximumMeasurementInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| maximumMeasurementInterval | double | Specifies the maximum measurement interval. This value is expressed in seconds. When you set the SetBurstDetectionEnabled(string, RFmxWlanMXTxpBurstDetectionEnabled) method to True , the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00201: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of TxpAllTracesEnabled attribute.The default value

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [TxpAllTracesEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the TXP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00202: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the transmit power (TXP) measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of TxpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescri

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the transmit power (TXP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [TxpMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the transmit power (TXP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00203: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of TxpNumberOfAnalysisThreads attribute.The default value is 1.Par

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [TxpNumberOfAnalysisThreads](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for TXP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-setburstdetectionenabled__string-rfmxwlanmxtxpburstdetectionenabled.html language=enus -->
## TOPIC 00204: SetBurstDetectionEnabled(string, RFmxWlanMXTxpBurstDetectionEnabled)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-setburstdetectionenabled__string-rfmxwlanmxtxpburstdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-setburstdetectionenabled__string-rfmxwlanmxtxpburstdetectionenabled.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement detects the start and the end of a WLAN packet automatically. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetBurstDetectionEnabled(string selectorString, RFmxWlanMXTxpBurstDetectionEnabled value)RemarksThis method sets the value of TxpBurstDetectionEnabled

### SetBurstDetectionEnabled(string, RFmxWlanMXTxpBurstDetectionEnabled)

Sets whether the measurement detects the start and the end of a WLAN packet automatically.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetBurstDetectionEnabled(string selectorString, RFmxWlanMXTxpBurstDetectionEnabled value)

#### Remarks

This method sets the value of [TxpBurstDetectionEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpburstdetectionenabled.html) .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWlanMXTxpBurstDetectionEnabled | Specifies whether the measurement detects the start and the end of a WLAN packet automatically. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00205: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the transmit power (TXP) measurement. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of TxpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptio

### SetMeasurementEnabled(string, bool)

Sets whether to enable the transmit power (TXP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [TxpMeasurementEnabled](nationalinstruments-rfmx-wlanmx-rfmxwlanmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the transmit power (TXP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults-fetchmeasurement__string-double-out-out.html language=enus -->
## TOPIC 00206: FetchMeasurement(string, double, out double, out double)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults-fetchmeasurement__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults-fetchmeasurement__string-double-out-out.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power and the peak power of the signal over which power measurements are performed. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchMeasurement(string selectorString, double timeout

### FetchMeasurement(string, double, out double, out double)

Returns the average power and the peak power of the signal over which power measurements are performed. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchMeasurement(string selectorString, double timeout, out double averagePowerMean, out double peakPowerMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| averagePowerMean | out double | Upon return, contains the average power of the acquired signal. This value is expressed in dBm. When you set the SetAveragingEnabled(string, RFmxWlanMXTxpAveragingEnabled) method to True , this parameter returns the mean of the average power computed for each averaging count. |
| peakPowerMaximum | out double | Upon return, contains the peak power of the acquired signal. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True , this parameter returns the maximum of the peak power computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults-fetchpowertrace__string-double-ref.html language=enus -->
## TOPIC 00207: FetchPowerTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults-fetchpowertrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults-fetchpowertrace__string-double-ref.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power versus time trace. Use "segment(n)/chain(k)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)ParametersNameTypeDescriptionsel

### FetchPowerTrace(string, double, ref AnalogWaveform< float >)

Returns the power versus time trace. 
 Use "segment(n)/chain(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, segment number, and chain number. If you do not specify the result name, the default result instance is used. Example: "segment0/chain0" "result::r1/segment0/chain0" You can use the BuildChainString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. This value is expressed in seconds. |
| power | ref AnalogWaveform< float > | Upon return, contains the power versus time trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWlanMXTxpResults Class

<!--NI_TOPIC bundle=rfmxwlan-dotnet-api-ref path=nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults.html language=enus -->
## TOPIC 00208: RFmxWlanMXTxpResults Class

- bundle_id: `rfmxwlan-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wlanmx-rfmxwlanmxtxpresults.html
- document_id: `rfmxwlan-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the TXP measurement results. Derives fromRFmxWlanMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WlanMXpublic class RFmxWlanMXTxpResults : RFmxWlanMXSubObjectMethodsNameDescriptionFetchMeasurement(string, double, out double, out double)Returns the average powe

### RFmxWlanMXTxpResults Class

Provides methods to fetch and read the TXP measurement results.

#### Derives from

- RFmxWlanMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WlanMX](nationalinstruments-rfmx-wlanmx.html)

public class RFmxWlanMXTxpResults : RFmxWlanMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMeasurement(string, double, out double, out double) | Returns the average power and the peak power of the signal over which power measurements are performed. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
| FetchPowerTrace(string, double, ref AnalogWaveform< float >) | Returns the power versus time trace. Use "segment(n)/chain(k)" as the selector string to read results from this method. |
| GetAveragePowerMean(string, out double) | Gets the average power of the acquired signal. This value is expressed in dBm. |
| GetPeakPowerMaximum(string, out double) | Gets the peak power of the acquired signal. This value is expressed in dBm. |

Parent topic:

NationalInstruments.RFmx.WlanMX
