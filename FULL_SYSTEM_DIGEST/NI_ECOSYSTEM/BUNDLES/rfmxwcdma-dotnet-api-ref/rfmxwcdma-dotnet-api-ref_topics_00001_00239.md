# NI DOCUMENT BUNDLE: rfmxwcdma-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwcdma-dotnet-api-ref start=1 end=239 -->
<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxwcdmamxextension-getwcdmasignalconfiguration__this-string.html language=enus -->
## TOPIC 00001: GetWcdmaSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxwcdmamxextension-getwcdmasignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxwcdmamxextension-getwcdmasignalconfiguration__this-string.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a WCDMA signal configuration for specified signal name. Existing WCDMA signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxWcdmaMX GetWcdmaSignalConfiguration(this RFmxInstrMX instrSession, string signalName)Par

### GetWcdmaSignalConfiguration(this RFmxInstrMX, string)

Creates a WCDMA signal configuration for specified signal name. Existing WCDMA signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxWcdmaMX](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx.html) GetWcdmaSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxWcdmaMX.

Parent topic:

RFmxWcdmaMXExtension Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-clearallnamedresults__string.html language=enus -->
## TOPIC 00002: ClearAllNamedResults(string)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-clearallnamedresults__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-clearallnamedresults__string.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the current signal instance.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ClearAllNamedResults(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is us

### ClearAllNamedResults(string)

Clears all results for the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ClearAllNamedResults(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureband__string-int.html language=enus -->
## TOPIC 00003: ConfigureBand(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureband__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureband__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Universal Mobile Telecommunications System (UMTS) operating band.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureBand(string selectorString, int band)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creatin

### ConfigureBand(string, int)

Configures the Universal Mobile Telecommunications System (UMTS) operating band.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureBand(string selectorString, int band)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| band | int | Specifies the UMTS operation band. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurecarrierfrequencyarray__string-double_arr1.html language=enus -->
## TOPIC 00004: ConfigureCarrierFrequencyArray(string, double[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurecarrierfrequencyarray__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurecarrierfrequencyarray__string-double_arr1.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the center frequencies of the carriers, relative to the RF center frequency.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureCarrierFrequencyArray(string selectorString, double[] carrierFrequency)ParametersNameTypeDescriptionselectorStringstringPass an empt

### ConfigureCarrierFrequencyArray(string, double[])

Configures an array of the center frequencies of the carriers, relative to the RF center frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureCarrierFrequencyArray(string selectorString, double[] carrierFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| carrierFrequency | double[] | Specifies an array of the center frequencies of the carriers, relative to the RF center frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurefrequencyuarfcn__string-int-int-int.html language=enus -->
## TOPIC 00005: ConfigureFrequencyUarfcn(string, int, int, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurefrequencyuarfcn__string-int-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurefrequencyuarfcn__string-int-int-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureFrequencyUarfcn(string selectorString, int linkDirection, in

### ConfigureFrequencyUarfcn(string, int, int, int)

Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureFrequencyUarfcn(string selectorString, int linkDirection, int band, int uarfcn)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| linkDirection | int | Specifies the link direction. |
| band | int | Specifies the UMTS operation band. |
| uarfcn | int | Specifies the UTRA absolute radio frequency channel number (UARFCN). UARFCN has to be updated according to the band for the uplink, as defined by the general UARFCNs in Table 4.2: UTRA Absolute Radio Frequency Channel Number in the 3GPP TS 34.121-1 specification, version 11.5.0. Otherwise, UARFCN is coerced to the top or bottom UARFCN of the selected band, depending on which is nearer. The center frequency then corresponds to this coerced UARFCN as defined by carrier frequencies in Table 4.1: UARFCN definition (general) of the 3GPP TS 34.121-1 specification, version 11.5.0. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurenumberofchannels__string-int.html language=enus -->
## TOPIC 00006: ConfigureNumberOfChannels(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurenumberofchannels__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurenumberofchannels__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of user-defined channels for the measurement. This method is used when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to UserDefined. Call this method before you call the RFmxWCDMA_CfgUserDefinedChannelArray method or the ConfigureUs

### ConfigureNumberOfChannels(string, int)

Configures the number of user-defined channels for the measurement. This method is used when you set the [SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setchannelconfigurationmode__string-rfmxwcdmamxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html). Call this method before you call the RFmxWCDMA_CfgUserDefinedChannelArray method or the [ConfigureUserDefinedChannel(string, int, int, RFmxWcdmaMXModulationType, RFmxWcdmaMXBranch)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannel__string-int-int-rfmxwcdmamxmodulationtype-rfmxwcdmamxbranch.html) method. 
 Use "carrier(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureNumberOfChannels(string selectorString, int numberOfChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of carrier number. Example: "carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| numberOfChannels | int | Specifies the number of user-defined channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurerf__string-double-double-double.html language=enus -->
## TOPIC 00007: ConfigureRF(string, double, double, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurerf__string-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configurerf__string-double-double-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF methods of the signal specified by the selector string.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureRF(string selectorString, double centerFrequency, double referenceLevel, double externalAttenuation)ParametersNameTypeDescriptionselectorStringstringPass an e

### ConfigureRF(string, double, double, double)

Configures the RF methods of the signal specified by the selector string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureRF(string selectorString, double centerFrequency, double referenceLevel, double externalAttenuation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| centerFrequency | double | Specifies the center frequency of the acquired RF signal for a single carrier. For multicarrier measurements, the parameter specifies the reference frequency for the values in the SetCarrierFrequency(string, double) method. This value is expressed in Hz. |
| referenceLevel | double | Specifies the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| externalAttenuation | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuplinktestmodel__string-rfmxwcdmamxuplinktestmodel.html language=enus -->
## TOPIC 00008: ConfigureUplinkTestModel(string, RFmxWcdmaMXUplinkTestModel)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuplinktestmodel__string-rfmxwcdmamxuplinktestmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuplinktestmodel__string-rfmxwcdmamxuplinktestmodel.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the uplink test model. Use "carrier(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureUplinkTestModel(string selectorString, RFmxWcdmaMXUplinkTestModel uplinkTestModel)ParametersNameTypeDescriptionselectorStringstringS

### ConfigureUplinkTestModel(string, RFmxWcdmaMXUplinkTestModel)

Configures the uplink test model. 
 Use "carrier(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureUplinkTestModel(string selectorString, RFmxWcdmaMXUplinkTestModel uplinkTestModel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of carrier number. Example: "carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| uplinkTestModel | RFmxWcdmaMXUplinkTestModel | Specifies the uplink test model when the user sets the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R(n), where n is the oldest release number with a given set of channel configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannel__string-int-int-rfmxwcdmamxmodulationtype-rfmxwcdmamxbranch.html language=enus -->
## TOPIC 00009: ConfigureUserDefinedChannel(string, int, int, RFmxWcdmaMXModulationType, RFmxWcdmaMXBranch)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannel__string-int-int-rfmxwcdmamxmodulationtype-rfmxwcdmamxbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannel__string-int-int-rfmxwcdmamxmodulationtype-rfmxwcdmamxbranch.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this method, you must configure the SetNumberOfChannels(string, int) method with the appropriate number of channels. Use "carrier(k)/channel(n)" as the selector string to configu

### ConfigureUserDefinedChannel(string, int, int, RFmxWcdmaMXModulationType, RFmxWcdmaMXBranch)

Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this method, you must configure the [SetNumberOfChannels(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setnumberofchannels__string-int.html) method with the appropriate number of channels. 
 Use "carrier(k)/channel(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureUserDefinedChannel(string selectorString, int spreadingFactor, int spreadingCode, RFmxWcdmaMXModulationType modulationType, RFmxWcdmaMXBranch branch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, carrier number, and channel number. Example: "carrier0/channel0" You can use the BuildChannelString(string, int) method to build the selector string. |
| spreadingFactor | int | Specifies the spreading factor of the channel. |
| spreadingCode | int | Specifies the spreading code of the channel. |
| modulationType | RFmxWcdmaMXModulationType | Specifies the modulation type of the channel. |
| branch | RFmxWcdmaMXBranch | Specifies the branch on which the data is modulated. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxwcdmamxmodulationtype_arr1-rfmxwcdmamxbranch_arr1.html language=enus -->
## TOPIC 00010: ConfigureUserDefinedChannelArray(string, int[], int[], RFmxWcdmaMXModulationType[], RFmxWcdmaMXBranch[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxwcdmamxmodulationtype_arr1-rfmxwcdmamxbranch_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-configureuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxwcdmamxmodulationtype_arr1-rfmxwcdmamxbranch_arr1.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this method, you must configure the SetNumberOfChannels(string, int) method with the appropriate number of user-defined channels. Use "carrier(n)" as the selector st

### ConfigureUserDefinedChannelArray(string, int[], int[], RFmxWcdmaMXModulationType[], RFmxWcdmaMXBranch[])

Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this method, you must configure the [SetNumberOfChannels(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setnumberofchannels__string-int.html) method with the appropriate number of user-defined channels. 
 Use "carrier(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureUserDefinedChannelArray(string selectorString, int[] spreadingFactor, int[] spreadingCode, RFmxWcdmaMXModulationType[] modulationType, RFmxWcdmaMXBranch[] branch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of carrier number. Example: "carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| spreadingFactor | int[] | Specifies an array of spreading factor of the channels. |
| spreadingCode | int[] | Specifies an array of spreading code of the channels. |
| modulationType | RFmxWcdmaMXModulationType[] | Specifies an array of modulation types of the channels. |
| branch | RFmxWcdmaMXBranch[] | Specifies an array of branches on which the data is modulated in the channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-disabletrigger__string.html language=enus -->
## TOPIC 00011: DisableTrigger(string)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-disabletrigger__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-disabletrigger__string.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int DisableTrigger(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an

### DisableTrigger(string)

Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int DisableTrigger(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getattributeint__string-int-out.html language=enus -->
## TOPIC 00012: GetAttributeInt(string, int, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getattributeint__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getattributeint__string-int-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of an RFmx 32-bit integer (int32) attribute. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being

### GetAttributeInt(string, int, out int)

Gets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx WCDMA Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out int | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getdigitaledgetriggersource__string-out.html language=enus -->
## TOPIC 00013: GetDigitalEdgeTriggerSource(string, out string)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getdigitaledgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getdigitaledgetriggersource__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal for the digital edge trigger. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetDigitalEdgeTriggerSource(string selectorString, out string value)RemarksThis method gets the value of DigitalEdgeTriggerSource attribute.The default value is RFMXWCDMA_VAL_PFI0_STR.P

### GetDigitalEdgeTriggerSource(string, out string)

Gets the source terminal for the digital edge trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetDigitalEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is RFMXWCDMA_VAL_PFI0_STR.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the source terminal for the digital edge trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggerminimumquiettimeduration__string-out.html language=enus -->
## TOPIC 00014: GetTriggerMinimumQuietTimeDuration(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggerminimumquiettimeduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggerminimumquiettimeduration__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetTriggerMinimumQuietTimeDuration(string selectorString, out double value)RemarksThis

### GetTriggerMinimumQuietTimeDuration(string, out double)

Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetTriggerMinimumQuietTimeDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggerminimumquiettimemode__string-out.html language=enus -->
## TOPIC 00015: GetTriggerMinimumQuietTimeMode(string, out RFmxWcdmaMXTriggerMinimumQuietTimeMode)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggerminimumquiettimemode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggerminimumquiettimemode__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetTriggerMinimumQuietTimeMode(string selectorString, out RFmxWcdmaMXTriggerMinimumQuietTimeMode value)RemarksThis method gets the value of TriggerMinimumQuie

### GetTriggerMinimumQuietTimeMode(string, out RFmxWcdmaMXTriggerMinimumQuietTimeMode)

Gets whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetTriggerMinimumQuietTimeMode(string selectorString, out RFmxWcdmaMXTriggerMinimumQuietTimeMode value)

#### Remarks

This method gets the value of [TriggerMinimumQuietTimeMode](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Manual](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggerminimumquiettimemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXTriggerMinimumQuietTimeMode | Upon return, contains whether the measurement computes the minimum quiet time used for triggering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggertype__string-out.html language=enus -->
## TOPIC 00016: GetTriggerType(string, out RFmxWcdmaMXTriggerType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-gettriggertype__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetTriggerType(string selectorString, out RFmxWcdmaMXTriggerType value)RemarksThis method gets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empt

### GetTriggerType(string, out RFmxWcdmaMXTriggerType)

Gets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetTriggerType(string selectorString, out RFmxWcdmaMXTriggerType value)

#### Remarks

This method gets the value of [TriggerType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXTriggerType | Upon return, contains the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getuplinkscramblingcode__string-out.html language=enus -->
## TOPIC 00017: GetUplinkScramblingCode(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getuplinkscramblingcode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getuplinkscramblingcode__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the scrambling code for the uplink channel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUplinkScramblingCode(string selectorString, out int value)RemarksThis method gets the value of UplinkScramblingCode attribute.The default value is 0. Valid values are 0 to 16,777,215.Param

### GetUplinkScramblingCode(string, out int)

Gets the scrambling code for the uplink channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUplinkScramblingCode(string selectorString, out int value)

#### Remarks

This method gets the value of [UplinkScramblingCode](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0. Valid values are 0 to 16,777,215.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the scrambling code for the uplink channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getuplinktestmodel__string-out.html language=enus -->
## TOPIC 00018: GetUplinkTestModel(string, out RFmxWcdmaMXUplinkTestModel)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getuplinktestmodel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-getuplinktestmodel__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the uplink test model when the user sets the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUplinkTestModel(string selectorString, out RFmxWcdmaMXUplinkTestModel value)RemarksThis metho

### GetUplinkTestModel(string, out RFmxWcdmaMXUplinkTestModel)

Gets the uplink test model when the user sets the [SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setchannelconfigurationmode__string-rfmxwcdmamxchannelconfigurationmode.html) method to [TestModel](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUplinkTestModel(string selectorString, out RFmxWcdmaMXUplinkTestModel value)

#### Remarks

This method gets the value of [UplinkTestModel](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is R6 C.2.1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxWcdmaMXUplinkTestModel | Upon return, contains the uplink test model when the user sets the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-obw.html language=enus -->
## TOPIC 00019: Obw

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-obw.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXObw instance that represents the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXObw Obw { get; }

### Obw

Gets the [RFmxWcdmaMXObw](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobw.html) instance that represents the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXObw](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobw.html) Obw { get; }

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-resetattribute__string-rfmxwcdmamxpropertyid.html language=enus -->
## TOPIC 00020: ResetAttribute(string, RFmxWcdmaMXPropertyId)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-resetattribute__string-rfmxwcdmamxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-resetattribute__string-rfmxwcdmamxpropertyid.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ResetAttribute(string selectorString, RFmxWcdmaMXPropertyId attributeId)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the property being reset. Refer to the Usi

### ResetAttribute(string, RFmxWcdmaMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ResetAttribute(string selectorString, RFmxWcdmaMXPropertyId attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2K Help for more information about configuring the selector string. |
| attributeId | RFmxWcdmaMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-resettodefault__string.html language=enus -->
## TOPIC 00021: ResetToDefault(string)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-resettodefault__string.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used.ReturnsReturns t

### ResetToDefault(string)

Resets a signal to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00022: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-sendsoftwareedgetrigger.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxWCDMA_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You config

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the RFmxWCDMA_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. 
 This method returns an error in the following situations: 
 You configure an invalid trigger. You have not previously called the RFmxWCDMA Initiate method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SendSoftwareEdgeTrigger()

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00023: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setattributebool__string-int-bool.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a

### SetAttributeBool(string, int, bool)

Sets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx WCDMA Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setattributestring__string-int-string.html language=enus -->
## TOPIC 00024: SetAttributeString(string, int, string)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setattributestring__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setattributestring__string-int-string.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a String attribute. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAttributeString(string selectorString, int attributeIdentifier, string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the U

### SetAttributeString(string, int, string)

Sets the value of a String attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAttributeString(string selectorString, int attributeIdentifier, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx WCDMA Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | string | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setexternalattenuation__string-double.html language=enus -->
## TOPIC 00025: SetExternalAttenuation(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setexternalattenuation__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetExternalAttenuation(string selectorString, double value)RemarksThis method sets the value of ExternalAttenu

### SetExternalAttenuation(string, double)

Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetExternalAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [ExternalAttenuation](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setreferencelevelheadroom__string-double.html language=enus -->
## TOPIC 00026: SetReferenceLevelHeadroom(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setreferencelevelheadroom__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setreferencelevelheadroom__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal

### SetReferenceLevelHeadroom(string, double)

Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the SNR by reducing the reference level headroom. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetReferenceLevelHeadroom(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setspreadingcode__string-int.html language=enus -->
## TOPIC 00027: SetSpreadingCode(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setspreadingcode__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setspreadingcode__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the spreading code of the channel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetSpreadingCode(string selectorString, int value)RemarksThis method sets the value of SpreadingCode attribute.The default value is 0. Valid values are 0 to (Spreading factor - 1).ParametersNameTypeDe

### SetSpreadingCode(string, int)

Sets the spreading code of the channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetSpreadingCode(string selectorString, int value)

#### Remarks

This method sets the value of [SpreadingCode](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0. Valid values are 0 to (Spreading factor - 1).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the channel number and carrier number. Example: "carrier0" or "carrier0/channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | int | Specifies the spreading code of the channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setspreadingfactor__string-int.html language=enus -->
## TOPIC 00028: SetSpreadingFactor(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setspreadingfactor__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setspreadingfactor__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the spreading factor of the channel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetSpreadingFactor(string selectorString, int value)RemarksThis method sets the value of SpreadingFactor attribute.The default value is 256. Valid values are 2, 4, 8,16, 32, 64, 128, and 256.Paramet

### SetSpreadingFactor(string, int)

Sets the spreading factor of the channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetSpreadingFactor(string selectorString, int value)

#### Remarks

This method sets the value of [SpreadingFactor](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 256. Valid values are 2, 4, 8,16, 32, 64, 128, and 256.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the channel number and carrier number. Example: "carrier0" or "carrier0/channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | int | Specifies the spreading factor of the channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-settriggerminimumquiettimeduration__string-double.html language=enus -->
## TOPIC 00029: SetTriggerMinimumQuietTimeDuration(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-settriggerminimumquiettimeduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-settriggerminimumquiettimeduration__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetTriggerMinimumQuietTimeDuration(string selectorString, double value)RemarksThis met

### SetTriggerMinimumQuietTimeDuration(string, double)

Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetTriggerMinimumQuietTimeDuration(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-settriggertype__string-rfmxwcdmamxtriggertype.html language=enus -->
## TOPIC 00030: SetTriggerType(string, RFmxWcdmaMXTriggerType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-settriggertype__string-rfmxwcdmamxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-settriggertype__string-rfmxwcdmamxtriggertype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetTriggerType(string selectorString, RFmxWcdmaMXTriggerType value)RemarksThis method sets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empty st

### SetTriggerType(string, RFmxWcdmaMXTriggerType)

Sets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetTriggerType(string selectorString, RFmxWcdmaMXTriggerType value)

#### Remarks

This method sets the value of [TriggerType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXTriggerType | Specifies the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setuplinkscramblingtype__string-rfmxwcdmamxuplinkscramblingtype.html language=enus -->
## TOPIC 00031: SetUplinkScramblingType(string, RFmxWcdmaMXUplinkScramblingType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setuplinkscramblingtype__string-rfmxwcdmamxuplinkscramblingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setuplinkscramblingtype__string-rfmxwcdmamxuplinkscramblingtype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of scrambling to use for the measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetUplinkScramblingType(string selectorString, RFmxWcdmaMXUplinkScramblingType value)RemarksThis method sets the value of UplinkScramblingType attribute.The default value is Long.Param

### SetUplinkScramblingType(string, RFmxWcdmaMXUplinkScramblingType)

Sets the type of scrambling to use for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetUplinkScramblingType(string selectorString, RFmxWcdmaMXUplinkScramblingType value)

#### Remarks

This method sets the value of [UplinkScramblingType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Long](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinkscramblingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxWcdmaMXUplinkScramblingType | Specifies the type of scrambling to use for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMX Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacp-results.html language=enus -->
## TOPIC 00032: Results

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacp-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacp-results.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXAcpResults instance that provides methods to fetch and read the ACP measurement results. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXAcpResults Results { get; }

### Results

Gets the [RFmxWcdmaMXAcpResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults.html) instance that provides methods to fetch and read the ACP measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXAcpResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults.html) Results { get; }

Parent topic:

RFmxWcdmaMXAcp Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-configureaveraging__string-rfmxwcdmamxacpaveragingenabled-int-rfmxwcdmamxacpaveragingtype.html language=enus -->
## TOPIC 00033: ConfigureAveraging(string, RFmxWcdmaMXAcpAveragingEnabled, int, RFmxWcdmaMXAcpAveragingType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-configureaveraging__string-rfmxwcdmamxacpaveragingenabled-int-rfmxwcdmamxacpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-configureaveraging__string-rfmxwcdmamxacpaveragingenabled-int-rfmxwcdmamxacpaveragingtype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureAveraging(string selectorString, RFmxWcdmaMXAcpAveragingEnabled averagingEnabled, int averagingCount, RFmxWcdmaMXAcpAveragingType averagingType)ParametersNameTypeDescriptionselectorStrin

### ConfigureAveraging(string, RFmxWcdmaMXAcpAveragingEnabled, int, RFmxWcdmaMXAcpAveragingType)

Configures averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureAveraging(string selectorString, RFmxWcdmaMXAcpAveragingEnabled averagingEnabled, int averagingCount, RFmxWcdmaMXAcpAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxWcdmaMXAcpAveragingEnabled | Specifies whether to enable averaging of the spectrum for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxWcdmaMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-configureoffsetpowerreference__string-rfmxwcdmamxacpoffsetpowerreferencecarrier-int.html language=enus -->
## TOPIC 00034: ConfigureOffsetPowerReference(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-configureoffsetpowerreference__string-rfmxwcdmamxacpoffsetpowerreferencecarrier-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-configureoffsetpowerreference__string-rfmxwcdmamxacpoffsetpowerreferencecarrier-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power reference to use for measuring the relative power of the offset channel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureOffsetPowerReference(string selectorString, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier offsetPowerReferenceCarrier, int offsetPowerReferen

### ConfigureOffsetPowerReference(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier, int)

Configures the power reference to use for measuring the relative power of the offset channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureOffsetPowerReference(string selectorString, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier offsetPowerReferenceCarrier, int offsetPowerReferenceSpecific)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| offsetPowerReferenceCarrier | RFmxWcdmaMXAcpOffsetPowerReferenceCarrier | Specifies the carrier to use as the power reference to measure offset channel relative power. |
| offsetPowerReferenceSpecific | int | Specifies the index of the carrier to be used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the offsetPowerReferenceCarrier parameter to Specific. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00035: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of AcpAllTracesEnabled attribute.The default valu

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getfarifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00036: GetFarIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getfarifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getfarifoutputpoweroffset__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetFarIFOutputPowerOf

### GetFarIFOutputPowerOffset(string, out double)

Gets the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetFarIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpFarIFOutputPowerOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getfftoverlapmode__string-out.html language=enus -->
## TOPIC 00037: GetFftOverlapMode(string, out RFmxWcdmaMXAcpFftOverlapMode)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getfftoverlapmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getfftoverlapmode__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets how overlapping is applied when computing the FFT of the acquired samples. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetFftOverlapMode(string selectorString, out RFmxWcdmaMXAcpFftOverlapMode value)RemarksThis method gets the value of AcpFftOverlapMode attribute.The default val

### GetFftOverlapMode(string, out RFmxWcdmaMXAcpFftOverlapMode)

Gets how overlapping is applied when computing the FFT of the acquired samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetFftOverlapMode(string selectorString, out RFmxWcdmaMXAcpFftOverlapMode value)

#### Remarks

This method gets the value of [AcpFftOverlapMode](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpfftoverlapmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXAcpFftOverlapMode | Upon return, shows how overlapping is applied when computing the FFT of the acquired samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getifoutputpoweroffsetauto__string-out.html language=enus -->
## TOPIC 00038: GetIFOutputPowerOffsetAuto(string, out RFmxWcdmaMXAcpIFOutputPowerOffsetAuto)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getifoutputpoweroffsetauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-getifoutputpoweroffsetauto__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetIFOutputPowerOffsetAuto(string selectorString, out RFmxWcdmaMXAcpIFOutputPowerOffsetAuto v

### GetIFOutputPowerOffsetAuto(string, out RFmxWcdmaMXAcpIFOutputPowerOffsetAuto)

Gets whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetIFOutputPowerOffsetAuto(string selectorString, out RFmxWcdmaMXAcpIFOutputPowerOffsetAuto value)

#### Remarks

This method gets the value of [AcpIFOutputPowerOffsetAuto](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.This property is used only if you set the ACP Meas Method property to Dynamic Range. The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpifoutputpoweroffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXAcpIFOutputPowerOffsetAuto | Upon return, contains whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setaveragingenabled__string-rfmxwcdmamxacpaveragingenabled.html language=enus -->
## TOPIC 00039: SetAveragingEnabled(string, RFmxWcdmaMXAcpAveragingEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setaveragingenabled__string-rfmxwcdmamxacpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setaveragingenabled__string-rfmxwcdmamxacpaveragingenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAveragingEnabled(string selectorString, RFmxWcdmaMXAcpAveragingEnabled value)RemarksThis method sets the value of AcpAveragingEnabled attribute.The default value is False.Paramete

### SetAveragingEnabled(string, RFmxWcdmaMXAcpAveragingEnabled)

Sets whether to enable averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAveragingEnabled(string selectorString, RFmxWcdmaMXAcpAveragingEnabled value)

#### Remarks

This method sets the value of [AcpAveragingEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setfarifoutputpoweroffset__string-double.html language=enus -->
## TOPIC 00040: SetFarIFOutputPowerOffset(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setfarifoutputpoweroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setfarifoutputpoweroffset__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetFarIFOutputPowerOf

### SetFarIFOutputPowerOffset(string, double)

Sets the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetFarIFOutputPowerOffset(string selectorString, double value)

#### Remarks

This method sets the value of [AcpFarIFOutputPowerOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setfftoverlapmode__string-rfmxwcdmamxacpfftoverlapmode.html language=enus -->
## TOPIC 00041: SetFftOverlapMode(string, RFmxWcdmaMXAcpFftOverlapMode)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setfftoverlapmode__string-rfmxwcdmamxacpfftoverlapmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setfftoverlapmode__string-rfmxwcdmamxacpfftoverlapmode.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets how overlapping is applied when computing the FFT of the acquired samples. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetFftOverlapMode(string selectorString, RFmxWcdmaMXAcpFftOverlapMode value)RemarksThis method sets the value of AcpFftOverlapMode attribute.The default value i

### SetFftOverlapMode(string, RFmxWcdmaMXAcpFftOverlapMode)

Sets how overlapping is applied when computing the FFT of the acquired samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetFftOverlapMode(string selectorString, RFmxWcdmaMXAcpFftOverlapMode value)

#### Remarks

This method sets the value of [AcpFftOverlapMode](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpfftoverlapmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXAcpFftOverlapMode | Specifies how overlapping is applied when computing the FFT of the acquired samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxwcdmamxacpifoutputpoweroffsetauto.html language=enus -->
## TOPIC 00042: SetIFOutputPowerOffsetAuto(string, RFmxWcdmaMXAcpIFOutputPowerOffsetAuto)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxwcdmamxacpifoutputpoweroffsetauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxwcdmamxacpifoutputpoweroffsetauto.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetIFOutputPowerOffsetAuto(string selectorString, RFmxWcdmaMXAcpIFOutputPowerOffsetAuto value

### SetIFOutputPowerOffsetAuto(string, RFmxWcdmaMXAcpIFOutputPowerOffsetAuto)

Sets whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetIFOutputPowerOffsetAuto(string selectorString, RFmxWcdmaMXAcpIFOutputPowerOffsetAuto value)

#### Remarks

This method sets the value of [AcpIFOutputPowerOffsetAuto](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.This property is used only if you set the ACP Meas Method property to Dynamic Range. The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpifoutputpoweroffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setmeasurementmethod__string-rfmxwcdmamxacpmeasurementmethod.html language=enus -->
## TOPIC 00043: SetMeasurementMethod(string, RFmxWcdmaMXAcpMeasurementMethod)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setmeasurementmethod__string-rfmxwcdmamxacpmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setmeasurementmethod__string-rfmxwcdmamxacpmeasurementmethod.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the method for performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementMethod(string selectorString, RFmxWcdmaMXAcpMeasurementMethod value)RemarksThis method sets the value of AcpMeasurementMethod attribute.The default value is Normal.Parameters

### SetMeasurementMethod(string, RFmxWcdmaMXAcpMeasurementMethod)

Sets the method for performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementMethod(string selectorString, RFmxWcdmaMXAcpMeasurementMethod value)

#### Remarks

This method sets the value of [AcpMeasurementMethod](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Normal](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxacprbwautobandwidth.html language=enus -->
## TOPIC 00044: SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXAcpRbwAutoBandwidth)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxacprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxacprbwautobandwidth.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRbwFilterAutoBandwidth(string selectorString, RFmxWcdmaMXAcpRbwAutoBandwidth value)RemarksThis method sets the value of AcpRbwFilterAutoBandwidth attribute.The default value is True.Paramete

### SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXAcpRbwAutoBandwidth)

Sets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRbwFilterAutoBandwidth(string selectorString, RFmxWcdmaMXAcpRbwAutoBandwidth value)

#### Remarks

This method sets the value of [AcpRbwFilterAutoBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacprbwautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsequentialfftsize__string-int.html language=enus -->
## TOPIC 00045: SetSequentialFftSize(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsequentialfftsize__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsequentialfftsize__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of bins to use for FFT computation when the SetMeasurementMethod(string, RFmxWcdmaMXAcpMeasurementMethod) method is set to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetSequentialFftSize(string selectorString, int value)RemarksThis method sets the valu

### SetSequentialFftSize(string, int)

Sets the number of bins to use for FFT computation when the [SetMeasurementMethod(string, RFmxWcdmaMXAcpMeasurementMethod)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setmeasurementmethod__string-rfmxwcdmamxacpmeasurementmethod.html) method is set to [SequentialFft](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetSequentialFftSize(string selectorString, int value)

#### Remarks

This method sets the value of [AcpSequentialFftSize](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 512.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of bins to use for FFT computation when the SetMeasurementMethod(string, RFmxWcdmaMXAcpMeasurementMethod) method is set to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeauto__string-rfmxwcdmamxacpsweeptimeauto.html language=enus -->
## TOPIC 00046: SetSweepTimeAuto(string, RFmxWcdmaMXAcpSweepTimeAuto)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeauto__string-rfmxwcdmamxacpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeauto__string-rfmxwcdmamxacpsweeptimeauto.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetSweepTimeAuto(string selectorString, RFmxWcdmaMXAcpSweepTimeAuto value)RemarksThis method sets the value of AcpSweepTimeAuto attribute.The default value is True.ParametersNameTypeDesc

### SetSweepTimeAuto(string, RFmxWcdmaMXAcpSweepTimeAuto)

Sets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetSweepTimeAuto(string selectorString, RFmxWcdmaMXAcpSweepTimeAuto value)

#### Remarks

This method sets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00047: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of Ac

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxWcdmaMXAcpSweepTimeAuto)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setsweeptimeauto__string-rfmxwcdmamxacpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [AcpSweepTimeInterval](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 666.66666700000007 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpmeasurementmethod.html language=enus -->
## TOPIC 00048: RFmxWcdmaMXAcpMeasurementMethod Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpmeasurementmethod.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method for performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXAcpMeasurementMethodMembersNameValueDescriptionNormal0The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this met

### RFmxWcdmaMXAcpMeasurementMethod Enumeration

Specifies the method for performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXAcpMeasurementMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| DynamicRange | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range.Supported Devices: PXIe-5665/5668R. |
| SequentialFft | 2 | The ACP measurement acquires I/Q samples specified by the SetSweepTimeInterval(string, double) method. These samples are divided into smaller chunks. The size of each chunk is defined by the SetSequentialFftSize(string, int) method, and FFT is computed for each of these chunks. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Use this method to optimize for speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following methods have limited support when you set the RFmxWcdmaMXAcpConfiguration.ConfigureMeasurementMethod method to SequentialFft.The RFmxWcdmaMXAcpConfiguration.SetRbwFilterAutoBandwidth method will only support True value. The RFmxWcdmaMXAcpConfiguration.SetRbwFilterType method will only support FftBased value. The RFmxWcdmaMXAcpConfiguration.SetSweepTimeAuto method will only support False value. The RFmxWcdmaMXAcpConfiguration.SetAveragingCount method will only support a value of greater than or equal to 1. The RFmxWcdmaMXAcpConfiguration.SetNumberOfAnalysisThreads method will only support a value greater than or equal to 1. The RFmxWcdmaMXAcpConfiguration.SetAmplitudeCorrectionType Method will only support a value of RFCenterFrequency. Note: For multi-span FFT, the averaging count should be 1. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpnoisecompensationenabled.html language=enus -->
## TOPIC 00049: RFmxWcdmaMXAcpNoiseCompensationEnabled Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpnoisecompensationenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXAcpNoiseCompensationEnabledMembersNameValueDescriptionFalse0Disables compensation of the channel powers for the

### RFmxWcdmaMXAcpNoiseCompensationEnabled Enumeration

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXAcpNoiseCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| True | 1 | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpoffsetpowerreferencecarrier.html language=enus -->
## TOPIC 00050: RFmxWcdmaMXAcpOffsetPowerReferenceCarrier Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpoffsetpowerreferencecarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpoffsetpowerreferencecarrier.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier used as the power reference to measure the offset channel relative power. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXAcpOffsetPowerReferenceCarrierMembersNameValueDescriptionClosest0The measurement uses the carrier power closest to the center freque

### RFmxWcdmaMXAcpOffsetPowerReferenceCarrier Enumeration

Specifies the carrier used as the power reference to measure the offset channel relative power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXAcpOffsetPowerReferenceCarrier

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Closest | 0 | The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. |
| Highest | 1 | The measurement uses the highest measured active carrier power as the power reference. |
| Composite | 2 | The measurement uses total measured active carrier power as the power reference. |
| Specific | 3 | The measurement uses the power measured in the carrier with index specified by the SetOffsetPowerReferenceSpecific(string, int) method as the power reference. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-fetchcarriermeasurementarray__string-double-ref-ref.html language=enus -->
## TOPIC 00051: FetchCarrierMeasurementArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-fetchcarriermeasurementarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-fetchcarriermeasurementarray__string-double-ref-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the GetTotalCarrierPower(string, out double) method.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchCarrierMeasurementArray(string selectorString, doubl

### FetchCarrierMeasurementArray(string, double, ref double[], ref double[])

Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the [GetTotalCarrierPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-gettotalcarrierpower__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchCarrierMeasurementArray(string selectorString, double timeout, ref double[] absolutePower, ref double[] relativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| absolutePower | ref double[] | Upon return, contains an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and SetCarrierFrequency(string, double) methods. This value is expressed in dBm. |
| relativePower | ref double[] | Upon return, contains an array of carrier power values relative to the total active carrier power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-fetchoffsetmeasurement__string-double-out-out-out-out.html language=enus -->
## TOPIC 00052: FetchOffsetMeasurement(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-fetchoffsetmeasurement__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-fetchoffsetmeasurement__string-double-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. Use "offset(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int Fetch

### FetchOffsetMeasurement(string, double, out double, out double, out double, out double)

Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. 
 Use "offset(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchOffsetMeasurement(string selectorString, double timeout, out double lowerRelativePower, out double upperRelativePower, out double lowerAbsolutePower, out double upperAbsolutePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. Example: "offset0" "result::r1/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| lowerRelativePower | out double | Upon return, contains the offset channel power measured relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method. |
| upperRelativePower | out double | Upon return, contains the upper offset channel power measured relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method. This value is expressed in dB. |
| lowerAbsolutePower | out double | Upon return, contains the lower offset channel power. |
| upperAbsolutePower | out double | Upon return, contains the upper offset channel power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getcarrierrelativepower__string-out.html language=enus -->
## TOPIC 00053: GetCarrierRelativePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getcarrierrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getcarrierrelativepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetCarrierRelativePower(string selectorString, out double value)RemarksThis method gets the value of AcpResultsCarrierRelativePow

### GetCarrierRelativePower(string, out double)

Gets the carrier power relative to the [GetTotalCarrierPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-gettotalcarrierpower__string-out.html).This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetCarrierRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsCarrierRelativePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.Use "carrier(k)" as the selector string to read this result.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getloweroffsetabsolutepower__string-out.html language=enus -->
## TOPIC 00054: GetLowerOffsetAbsolutePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getloweroffsetabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getloweroffsetabsolutepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower offset channel power. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetAbsolutePower(string selectorString, out double value)RemarksThis method gets the value of AcpResultsLowerOffsetAbsolutePower attribute.ParametersNameTypeDes

### GetLowerOffsetAbsolutePower(string, out double)

Gets the lower offset channel power. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsLowerOffsetAbsolutePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the lower offset channel power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getloweroffsetrelativepower__string-out.html language=enus -->
## TOPIC 00055: GetLowerOffsetRelativePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getloweroffsetrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getloweroffsetrelativepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetRelati

### GetLowerOffsetRelativePower(string, out double)

Gets the lower offset channel power relative to the power of the carrier(s) that you specify in the [SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setoffsetpowerreferencecarrier__string-rfmxwcdmamxacpoffsetpowerreferencecarrier.html) method.This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsLowerOffsetRelativePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the lower offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-gettotalcarrierpower__string-out.html language=enus -->
## TOPIC 00056: GetTotalCarrierPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-gettotalcarrierpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-gettotalcarrierpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(string, out double) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. SyntaxNamespace: Nation

### GetTotalCarrierPower(string, out double)

Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the [GetCarrierAbsolutePower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getcarrierabsolutepower__string-out.html) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetTotalCarrierPower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsTotalCarrierPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(string, out double) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getupperoffsetabsolutepower__string-out.html language=enus -->
## TOPIC 00057: GetUpperOffsetAbsolutePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getupperoffsetabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getupperoffsetabsolutepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper offset channel power.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUpperOffsetAbsolutePower(string selectorString, out double value)RemarksThis method gets the value of AcpResultsUpperOffsetAbsolutePower attribute.ParametersNameTypeDesc

### GetUpperOffsetAbsolutePower(string, out double)

Gets the upper offset channel power.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUpperOffsetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsUpperOffsetAbsolutePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the upper offset channel power.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getupperoffsetrelativepower__string-out.html language=enus -->
## TOPIC 00058: GetUpperOffsetRelativePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getupperoffsetrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults-getupperoffsetrelativepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUpperOffsetRelati

### GetUpperOffsetRelativePower(string, out double)

Gets the upper offset channel power relative to the power of the carrier(s) that you specify in the [SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpconfiguration-setoffsetpowerreferencecarrier__string-rfmxwcdmamxacpoffsetpowerreferencecarrier.html) method.This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUpperOffsetRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsUpperOffsetRelativePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the upper offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXAcpResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults.html language=enus -->
## TOPIC 00059: RFmxWcdmaMXAcpResults Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxacpresults.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the ACP measurement results. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXAcpResults : RFmxWcdmaMXSubObjectMethodsNameDescriptionFetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >)Fetches

### RFmxWcdmaMXAcpResults Class

Provides methods to fetch and read the ACP measurement results.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXAcpResults : RFmxWcdmaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >) | Fetches the absolute powers trace for the ACP measurement. |
| FetchCarrierMeasurement(string, double, out double, out double) | Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power. Use "carrier(n)" as the selector string to configure this method. |
| FetchCarrierMeasurementArray(string, double, ref double[], ref double[]) | Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the GetTotalCarrierPower(string, out double) method. |
| FetchOffsetMeasurement(string, double, out double, out double, out double, out double) | Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. Use "offset(n)" as the selector string to configure this method. |
| FetchOffsetMeasurementArray(string, double, ref double[], ref double[], ref double[], ref double[]) | Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method. |
| FetchRelativePowersTrace(string, double, int, ref Spectrum< float >) | Fetches the relative powers trace for the ACP measurement. |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for the ACP measurement. |
| FetchTotalCarrierPower(string, double, out double) | Fetches the total carrier power for the ACP measurement. |
| GetCarrierAbsolutePower(string, out double) | Gets the carrier power.This value is expressed in dBm. |
| GetCarrierRelativePower(string, out double) | Gets the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. |
| GetLowerOffsetAbsolutePower(string, out double) | Gets the lower offset channel power. This value is expressed in dBm. |
| GetLowerOffsetRelativePower(string, out double) | Gets the lower offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |
| GetTotalCarrierPower(string, out double) | Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(string, out double) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |
| GetUpperOffsetAbsolutePower(string, out double) | Gets the upper offset channel power.This value is expressed in dBm. |
| GetUpperOffsetRelativePower(string, out double) | Gets the upper offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcda-results.html language=enus -->
## TOPIC 00060: Results

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcda-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcda-results.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXCdaResults instance that provides methods to fetch and read the CDA measurement results. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXCdaResults Results { get; }

### Results

Gets the [RFmxWcdmaMXCdaResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults.html) instance that provides methods to fetch and read the CDA measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXCdaResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults.html) Results { get; }

Parent topic:

RFmxWcdmaMXCda Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcda.html language=enus -->
## TOPIC 00061: RFmxWcdmaMXCda Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcda.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the CDA measurement. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXCda : RFmxWcdmaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxWcdmaMXCdaConfiguration instance that provides methods to configure the CDA measuremen

### RFmxWcdmaMXCda Class

Represents the CDA measurement.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXCda : RFmxWcdmaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxWcdmaMXCdaConfiguration instance that provides methods to configure the CDA measurement. |
| Results | Gets the RFmxWcdmaMXCdaResults instance that provides methods to fetch and read the CDA measurement results. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-configuremeasurementchannel__string-int-int-rfmxwcdmamxcdameasurementchannelmodulationtype-rfmxwcdmamxcdameasurementchannelbranch.html language=enus -->
## TOPIC 00062: ConfigureMeasurementChannel(string, int, int, RFmxWcdmaMXCdaMeasurementChannelModulationType, RFmxWcdmaMXCdaMeasurementChannelBranch)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-configuremeasurementchannel__string-int-int-rfmxwcdmamxcdameasurementchannelmodulationtype-rfmxwcdmamxcdameasurementchannelbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-configuremeasurementchannel__string-int-int-rfmxwcdmamxcdameasurementchannelmodulationtype-rfmxwcdmamxcdameasurementchannelbranch.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureMeasurementChannel(string selectorString, int spreadingFactor, int spreadingCode, RFmxWcdmaMXCdaMeasurementChannelModulation

### ConfigureMeasurementChannel(string, int, int, RFmxWcdmaMXCdaMeasurementChannelModulationType, RFmxWcdmaMXCdaMeasurementChannelBranch)

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureMeasurementChannel(string selectorString, int spreadingFactor, int spreadingCode, RFmxWcdmaMXCdaMeasurementChannelModulationType modulationType, RFmxWcdmaMXCdaMeasurementChannelBranch branch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| spreadingFactor | int | Specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| spreadingCode | int | Specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| modulationType | RFmxWcdmaMXCdaMeasurementChannelModulationType | Specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| branch | RFmxWcdmaMXCdaMeasurementChannelBranch | Specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementchannelspreadingfactor__string-out.html language=enus -->
## TOPIC 00063: GetMeasurementChannelSpreadingFactor(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementchannelspreadingfactor__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementchannelspreadingfactor__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementChannelSpreadingFactor(string selectorString, out int value)RemarksThis method gets the value of Cd

### GetMeasurementChannelSpreadingFactor(string, out int)

Gets the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementChannelSpreadingFactor(string selectorString, out int value)

#### Remarks

This method gets the value of [CdaMeasurementChannelSpreadingFactor](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00064: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of CdaMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStr

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [CdaMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00065: GetMeasurementLength(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the code domain measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of CdaMeasurementLength attribute.The default value is 1. Valid

### GetMeasurementLength(string, out int)

Gets the duration of the code domain measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [CdaMeasurementLength](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 1. Valid values are [1, (15 - CDA Measurement Offset)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the code domain measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00066: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces after performing the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of CdaAllTracesEnabled attribute.The default value is FALSE.ParametersNameTypeDe

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces after performing the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [CdaAllTracesEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces after performing the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxcdaiqoffsetremovalenabled.html language=enus -->
## TOPIC 00067: SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXCdaIQOffsetRemovalEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxcdaiqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxcdaiqoffsetremovalenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q offset before the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetIQOffsetRemovalEnabled(string selectorString, RFmxWcdmaMXCdaIQOffsetRemovalEnabled value)RemarksThis method sets the value of CdaIQOffsetRemovalEnabled attribute.The defau

### SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXCdaIQOffsetRemovalEnabled)

Sets whether to remove the I/Q offset before the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetIQOffsetRemovalEnabled(string selectorString, RFmxWcdmaMXCdaIQOffsetRemovalEnabled value)

#### Remarks

This method sets the value of [CdaIQOffsetRemovalEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaiqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXCdaIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementchannelmodulationtype__string-rfmxwcdmamxcdameasurementchannelmodulationtype.html language=enus -->
## TOPIC 00068: SetMeasurementChannelModulationType(string, RFmxWcdmaMXCdaMeasurementChannelModulationType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementchannelmodulationtype__string-rfmxwcdmamxcdameasurementchannelmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementchannelmodulationtype__string-rfmxwcdmamxcdameasurementchannelmodulationtype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementChannelModulationType(string selectorString, RFmxWcdmaMXCdaMeasurementChannelModulationType value)Re

### SetMeasurementChannelModulationType(string, RFmxWcdmaMXCdaMeasurementChannelModulationType)

Sets the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementChannelModulationType(string selectorString, RFmxWcdmaMXCdaMeasurementChannelModulationType value)

#### Remarks

This method sets the value of [CdaMeasurementChannelModulationType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is BPSK/QPSK.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXCdaMeasurementChannelModulationType | Specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00069: SetMeasurementLength(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the code domain measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of CdaMeasurementLength attribute.The default value is 1. Valid valu

### SetMeasurementLength(string, int)

Sets the duration of the code domain measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [CdaMeasurementLength](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 1. Valid values are [1, (15 - CDA Measurement Offset)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the code domain measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00070: SetMeasurementOffset(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXCdaSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasureme

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxWcdmaMXCdaSynchronizationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setsynchronizationmode__string-rfmxwcdmamxcdasynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [CdaMeasurementOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0. Valid values are [0, (15 - CDA Measurement Length)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXCdaSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html language=enus -->
## TOPIC 00071: SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement unit of all power results, except GetTotalPower(string, out double). SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetPowerUnit(string selectorString, RFmxWcdmaMXCdaPowerUnit value)RemarksThis method sets the value of CdaPowerUnit attribute.The default value is dB.

### SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit)

Sets the measurement unit of all power results, except [GetTotalPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetPowerUnit(string selectorString, RFmxWcdmaMXCdaPowerUnit value)

#### Remarks

This method sets the value of [CdaPowerUnit](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [dB](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXCdaPowerUnit | Specifies the measurement unit of all power results, except GetTotalPower(string, out double). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html language=enus -->
## TOPIC 00072: RFmxWcdmaMXCdaPowerUnit Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement unit of all power results, except GetTotalPower(string, out double). SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXCdaPowerUnitMembersNameValueDescriptiondB0Specifies the power relative to the total power. dBm1Specifies the absolute power measured.

### RFmxWcdmaMXCdaPowerUnit Enumeration

Specifies the measurement unit of all power results, except [GetTotalPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXCdaPowerUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| dB | 0 | Specifies the power relative to the total power. |
| dBm | 1 | Specifies the absolute power measured. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-fetchsymbolevm__string-double-out-out-out-out-out-out.html language=enus -->
## TOPIC 00073: FetchSymbolEvm(string, double, out double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-fetchsymbolevm__string-double-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-fetchsymbolevm__string-double-out-out-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchSymbolEvm(string selectorString, double timeout, out double

### FetchSymbolEvm(string, double, out double, out double, out double, out double, out double, out double)

Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchSymbolEvm(string selectorString, double timeout, out double rmsSymbolEvm, out double peakSymbolEvm, out double rmsSymbolMagnitudeError, out double rmsSymbolPhaseError, out double meanSymbolPower, out double chipRateError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| rmsSymbolEvm | out double | Upon return, contains the RMS EVM for the measurement channel. This value is expressed as a percentage. |
| peakSymbolEvm | out double | Upon return, contains the peak EVM for the measurement channel. This value is expressed as a percentage. |
| rmsSymbolMagnitudeError | out double | Upon return, contains the RMS magnitude error for the measurement channel. This value is expressed as a percentage. |
| rmsSymbolPhaseError | out double | Upon return, contains the RMS phase error for the measurement channel. This value is expressed in degrees. |
| meanSymbolPower | out double | Upon return, contains the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. |
| chipRateError | out double | Upon return, contains the chip rate error of the composite signal. This value is expressed in ppm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getmeanactivepower__string-out.html language=enus -->
## TOPIC 00074: GetMeanActivePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getmeanactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getmeanactivepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average of all the active channel powers. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB

### GetMeanActivePower(string, out double)

Gets the average of all the active channel powers. If you set the [SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html), the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [GetTotalPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html) method. This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeanActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsMeanActivePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average of all the active channel powers. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getmeaninactivepower__string-out.html language=enus -->
## TOPIC 00075: GetMeanInactivePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getmeaninactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getmeaninactivepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average code power among the set of inactive channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) metho

### GetMeanInactivePower(string, out double)

Gets the average code power among the set of inactive channels in the code domain. If you set the [SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html), the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [GetTotalPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html) method. This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeanInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsMeanInactivePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average code power among the set of inactive channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getpeakactivepower__string-out.html language=enus -->
## TOPIC 00076: GetPeakActivePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getpeakactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getpeakactivepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the largest code power among the set of active channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method.

### GetPeakActivePower(string, out double)

Gets the largest code power among the set of active channels in the code domain. If you set the [SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html), the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [GetTotalPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html) method. This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetPeakActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsPeakActivePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the largest code power among the set of active channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getpeakinactivepower__string-out.html language=enus -->
## TOPIC 00077: GetPeakInactivePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getpeakinactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getpeakinactivepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the largest code power among the set of inactive channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) metho

### GetPeakInactivePower(string, out double)

Gets the largest code power among the set of inactive channels in the code domain. If you set the [SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaconfiguration-setpowerunit__string-rfmxwcdmamxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdapowerunit.html), the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [GetTotalPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html) method. This value is expressed in dB or dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetPeakInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsPeakInactivePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the largest code power among the set of inactive channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getrmssymbolphaseerror__string-out.html language=enus -->
## TOPIC 00078: GetRmsSymbolPhaseError(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getrmssymbolphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-getrmssymbolphaseerror__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS phase error for the measurement channel. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetRmsSymbolPhaseError(string selectorString, out double value)RemarksThis method gets the value of CdaResultsRmsSymbolPhaseError attribute.Parameters

### GetRmsSymbolPhaseError(string, out double)

Gets the RMS phase error for the measurement channel. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetRmsSymbolPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsRmsSymbolPhaseError](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS phase error for the measurement channel. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html language=enus -->
## TOPIC 00079: GetTotalPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaresults-gettotalpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetTotalPower(string selectorString, out double value)RemarksThis method gets the value of CdaResultsTotalPo

### GetTotalPower(string, out double)

Gets the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetTotalPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsTotalPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaspectruminverted.html language=enus -->
## TOPIC 00080: RFmxWcdmaMXCdaSpectrumInverted Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxcdaspectruminverted.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXCdaSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxWcdmaMXCdaSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXCdaSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00081: GetRbwFilterAutoBandwidth(string, out RFmxWcdmaMXChpRbwAutoBandwidth)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfilterautobandwidth__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetRbwFilterAutoBandwidth(string selectorString, out RFmxWcdmaMXChpRbwAutoBandwidth value)RemarksThis method gets the value of ChpRbwFilterAutoBandwidth attribute.The default value is True.Para

### GetRbwFilterAutoBandwidth(string, out RFmxWcdmaMXChpRbwAutoBandwidth)

Gets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetRbwFilterAutoBandwidth(string selectorString, out RFmxWcdmaMXChpRbwAutoBandwidth value)

#### Remarks

This method gets the value of [ChpRbwFilterAutoBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXChpRbwAutoBandwidth | Upon return, contains whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00082: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType) method to Gaussian or Flat. This v

### GetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter used to sweep the acquired signal when you set the [SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxchprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html). This method is valid only if you set the [SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfiltertype__string-rfmxwcdmamxchprbwfiltertype.html) method to [Gaussian](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html) or [Flat](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpRbwFilterBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 50 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00083: GetRbwFilterType(string, out RFmxWcdmaMXChpRbwFilterType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetRbwFilterType(string selectorString, out RFmxWcdmaMXChpRbwFilterType value)RemarksThis method gets the value of ChpRbwFilterType attribute.The default value is FftBased.ParametersNameTypeDescript

### GetRbwFilterType(string, out RFmxWcdmaMXChpRbwFilterType)

Gets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetRbwFilterType(string selectorString, out RFmxWcdmaMXChpRbwFilterType value)

#### Remarks

This method gets the value of [ChpRbwFilterType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [FftBased](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXChpRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00084: GetSweepTimeAuto(string, out RFmxWcdmaMXChpSweepTimeAuto)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetSweepTimeAuto(string selectorString, out RFmxWcdmaMXChpSweepTimeAuto value)RemarksThis method gets the value of ChpSweepTimeAuto attribute.The default value is True.ParametersNameType

### GetSweepTimeAuto(string, out RFmxWcdmaMXChpSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxWcdmaMXChpSweepTimeAuto value)

#### Remarks

This method gets the value of [ChpSweepTimeAuto](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXChpSweepTimeAuto | Upon return, contains whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxchpamplitudecorrectiontype.html language=enus -->
## TOPIC 00085: SetAmplitudeCorrectionType(string, RFmxWcdmaMXChpAmplitudeCorrectionType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxchpamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxchpamplitudecorrectiontype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: NationalInstr

### SetAmplitudeCorrectionType(string, RFmxWcdmaMXChpAmplitudeCorrectionType)

Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxWcdmaMXChpAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [ChpAmplitudeCorrectionType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXChpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00086: SetAveragingCount(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXChpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of ChpAvera

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxWcdmaMXChpAveragingEnabled)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingenabled__string-rfmxwcdmamxchpaveragingenabled.html) method to [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ChpAveragingCount](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXChpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingenabled__string-rfmxwcdmamxchpaveragingenabled.html language=enus -->
## TOPIC 00087: SetAveragingEnabled(string, RFmxWcdmaMXChpAveragingEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingenabled__string-rfmxwcdmamxchpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setaveragingenabled__string-rfmxwcdmamxchpaveragingenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAveragingEnabled(string selectorString, RFmxWcdmaMXChpAveragingEnabled value)RemarksThis method sets the value of ChpAveragingEnabled attribute.The default value is False.Paramete

### SetAveragingEnabled(string, RFmxWcdmaMXChpAveragingEnabled)

Sets whether to enable averaging for the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAveragingEnabled(string selectorString, RFmxWcdmaMXChpAveragingEnabled value)

#### Remarks

This method sets the value of [ChpAveragingEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxchprbwautobandwidth.html language=enus -->
## TOPIC 00088: SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxchprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxchprbwautobandwidth.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRbwFilterAutoBandwidth(string selectorString, RFmxWcdmaMXChpRbwAutoBandwidth value)RemarksThis method sets the value of ChpRbwFilterAutoBandwidth attribute.The default value is True.Paramete

### SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth)

Sets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRbwFilterAutoBandwidth(string selectorString, RFmxWcdmaMXChpRbwAutoBandwidth value)

#### Remarks

This method sets the value of [ChpRbwFilterAutoBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00089: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType) method to Gaussian or Flat. This v

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the [SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxchprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html). This method is valid only if you set the [SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfiltertype__string-rfmxwcdmamxchprbwfiltertype.html) method to [Gaussian](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html) or [Flat](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [ChpRbwFilterBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 50 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfiltertype__string-rfmxwcdmamxchprbwfiltertype.html language=enus -->
## TOPIC 00090: SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfiltertype__string-rfmxwcdmamxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchpconfiguration-setrbwfiltertype__string-rfmxwcdmamxchprbwfiltertype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRbwFilterType(string selectorString, RFmxWcdmaMXChpRbwFilterType value)RemarksThis method sets the value of ChpRbwFilterType attribute.The default value is FftBased.ParametersNameTypeDescriptions

### SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType)

Sets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRbwFilterType(string selectorString, RFmxWcdmaMXChpRbwFilterType value)

#### Remarks

This method sets the value of [ChpRbwFilterType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [FftBased](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html language=enus -->
## TOPIC 00091: RFmxWcdmaMXChpRbwAutoBandwidth Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwautobandwidth.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXChpRbwAutoBandwidthMembersNameValueDescriptionFalse0The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. True1The measurement comp

### RFmxWcdmaMXChpRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXChpRbwAutoBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. |
| True | 1 | The measurement computes the RBW. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html language=enus -->
## TOPIC 00092: RFmxWcdmaMXChpRbwFilterType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchprbwfiltertype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXChpRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is applied. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW filter with a flat response

### RFmxWcdmaMXChpRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXChpRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is applied. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi0.html language=enus -->
## TOPIC 00093: DioPfi0

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi0.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string DioPfi0

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi3.html language=enus -->
## TOPIC 00094: DioPfi3

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi3.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string DioPfi3

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi4.html language=enus -->
## TOPIC 00095: DioPfi4

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi4.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string DioPfi4

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi5.html language=enus -->
## TOPIC 00096: DioPfi5

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi5.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string DioPfi5

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi6.html language=enus -->
## TOPIC 00097: DioPfi6

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi6.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string DioPfi6

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi7.html language=enus -->
## TOPIC 00098: DioPfi7

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-diopfi7.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string DioPfi7

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-pfi1.html language=enus -->
## TOPIC 00099: Pfi1

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-pfi1.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string Pfi1

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-pulsein.html language=enus -->
## TOPIC 00100: PulseIn

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxconstants-pulsein.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public const string PulseIn

Parent topic:

RFmxWcdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxmodacciqoffsetremovalenabled.html language=enus -->
## TOPIC 00101: SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXModAccIQOffsetRemovalEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxmodacciqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxmodacciqoffsetremovalenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q offset before the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetIQOffsetRemovalEnabled(string selectorString, RFmxWcdmaMXModAccIQOffsetRemovalEnabled value)RemarksThis method sets the value of ModAccIQOffsetRemovalEnabled attribute.

### SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXModAccIQOffsetRemovalEnabled)

Sets whether to remove the I/Q offset before the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetIQOffsetRemovalEnabled(string selectorString, RFmxWcdmaMXModAccIQOffsetRemovalEnabled value)

#### Remarks

This method sets the value of [ModAccIQOffsetRemovalEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodacciqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00102: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of ModAccMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorS

### SetMeasurementEnabled(string, bool)

Sets whether to enable the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ModAccMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setrrcfilterenabled__string-rfmxwcdmamxmodaccrrcfilterenabled.html language=enus -->
## TOPIC 00103: SetRrcFilterEnabled(string, RFmxWcdmaMXModAccRrcFilterEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setrrcfilterenabled__string-rfmxwcdmamxmodaccrrcfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration-setrrcfilterenabled__string-rfmxwcdmamxmodaccrrcfilterenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRrcFilterEnabled(string selectorString, RFmxWcdmaMXModAccRrcFilterEnabled value)RemarksThis method sets the valu

### SetRrcFilterEnabled(string, RFmxWcdmaMXModAccRrcFilterEnabled)

Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRrcFilterEnabled(string selectorString, RFmxWcdmaMXModAccRrcFilterEnabled value)

#### Remarks

This method sets the value of [ModAccRrcFilterEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccrrcfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXModAccRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration.html language=enus -->
## TOPIC 00104: RFmxWcdmaMXModAccConfiguration Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccconfiguration.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ModAcc measurement. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXModAccConfiguration : RFmxWcdmaMXSubObjectMethodsNameDescriptionConfigureReferenceWaveform(string, ComplexWaveform< ComplexSingle >)Configure

### RFmxWcdmaMXModAccConfiguration Class

Provides methods to configure the ModAcc measurement.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXModAccConfiguration : RFmxWcdmaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureReferenceWaveform(string, ComplexWaveform< ComplexSingle >) | Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements.This method is used only when you set the SetSynchronizationMode(string, RFmxWcdmaMXModAccSynchronizationMode) method to Marker. |
| ConfigureSynchronizationModeAndInterval(string, RFmxWcdmaMXModAccSynchronizationMode, int, int) | Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. |
| GetIQGainImbalanceRemovalEnabled(string, out RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled) | Gets whether to remove I/Q gain imbalance before the ModAcc Measurement. |
| GetIQOffsetRemovalEnabled(string, out RFmxWcdmaMXModAccIQOffsetRemovalEnabled) | Gets whether to remove the I/Q offset before the ModAcc measurement. |
| GetIQQuadratureErrorRemovalEnabled(string, out RFmxWcdmaMXModAccIQQuadratureErrorRemovalEnabled) | Gets whether to remove the I/Q quadrature error before the ModAcc measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the ModAcc measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of the ModAcc measurement. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXModAccSynchronizationMode) method. |
| GetRrcFilterEnabled(string, out RFmxWcdmaMXModAccRrcFilterEnabled) | Gets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| GetSpectrumInverted(string, out RFmxWcdmaMXModAccSpectrumInverted) | Gets whether the spectrum of the signal is inverted. |
| GetSynchronizationMode(string, out RFmxWcdmaMXModAccSynchronizationMode) | Gets whether the measurement is performed from the frame, slot, or symbol boundary. |
| GetTransientRemovalEnabled(string, out RFmxWcdmaMXModAccTransientRemovalEnabled) | Gets whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. |
| SetIQGainImbalanceRemovalEnabled(string, RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled) | Sets whether to remove I/Q gain imbalance before the ModAcc Measurement. |
| SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXModAccIQOffsetRemovalEnabled) | Sets whether to remove the I/Q offset before the ModAcc measurement. |
| SetIQQuadratureErrorRemovalEnabled(string, RFmxWcdmaMXModAccIQQuadratureErrorRemovalEnabled) | Sets whether to remove the I/Q quadrature error before the ModAcc measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the ModAcc measurement. |
| SetMeasurementLength(string, int) | Sets the duration of the ModAcc measurement. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXModAccSynchronizationMode) method. |
| SetRrcFilterEnabled(string, RFmxWcdmaMXModAccRrcFilterEnabled) | Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| SetSpectrumInverted(string, RFmxWcdmaMXModAccSpectrumInverted) | Sets whether the spectrum of the signal is inverted. |
| SetSynchronizationMode(string, RFmxWcdmaMXModAccSynchronizationMode) | Sets whether the measurement is performed from the frame, slot, or symbol boundary. |
| SetTransientRemovalEnabled(string, RFmxWcdmaMXModAccTransientRemovalEnabled) | Sets whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccdetectedbranch.html language=enus -->
## TOPIC 00105: RFmxWcdmaMXModAccDetectedBranch Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccdetectedbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccdetectedbranch.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch of the detected channel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXModAccDetectedBranchMembersNameValueDescriptionI0The signal is modulated on the in-phase branch. Q1The signal is modulated on the quadrature-phase branch. IAndQ2The signal is complex m

### RFmxWcdmaMXModAccDetectedBranch Enumeration

Returns the branch of the detected channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXModAccDetectedBranch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| I | 0 | The signal is modulated on the in-phase branch. |
| Q | 1 | The signal is modulated on the quadrature-phase branch. |
| IAndQ | 2 | The signal is complex modulated. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchdetectedchannel__string-double-out-out-out-out.html language=enus -->
## TOPIC 00106: FetchDetectedChannel(string, double, out int, out int, out RFmxWcdmaMXModAccDetectedModulationType, out RFmxWcdmaMXModAccDetectedBranch)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchdetectedchannel__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchdetectedchannel__string-double-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement. Use "carrier(n)/channel(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchDetectedChann

### FetchDetectedChannel(string, double, out int, out int, out RFmxWcdmaMXModAccDetectedModulationType, out RFmxWcdmaMXModAccDetectedBranch)

Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement. 
 Use "carrier(n)/channel(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchDetectedChannel(string selectorString, double timeout, out int detectedSpreadingFactor, out int detectedSpreadingCode, out RFmxWcdmaMXModAccDetectedModulationType detectedModulationType, out RFmxWcdmaMXModAccDetectedBranch detectedBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, carrier number, and channel number. If you do not specify the result name, the default result instance is used. Example: "carrier0/channel0" "result::r1/carrier0/channel0" You can use the BuildChannelString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| detectedSpreadingFactor | out int | Upon return, contains the spreading factors of the detected channels when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns the spreading factor of the configured channel of a carrier. |
| detectedSpreadingCode | out int | Upon return, contains the spreading code of the detected channels when you set the Channel Configuration Mode method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns the spreading code of the configured channel of a carrier. |
| detectedModulationType | out RFmxWcdmaMXModAccDetectedModulationType | Upon return, the modulation types of the detected channels, when you set the Channel Configuration Mode method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns the spreading code of the configured channel of a carrier. |
| detectedBranch | out RFmxWcdmaMXModAccDetectedBranch | Upon return, contains the branch of the detected channels when you set the Channel Configuration Mode method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns the branch of the configured channel of a carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchdetectedchannelarray__string-double-ref-ref-ref-ref.html language=enus -->
## TOPIC 00107: FetchDetectedChannelArray(string, double, ref int[], ref int[], ref RFmxWcdmaMXModAccDetectedModulationType[], ref RFmxWcdmaMXModAccDetectedBranch[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchdetectedchannelarray__string-double-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchdetectedchannelarray__string-double-ref-ref-ref-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to AutoDetect for the ModAcc measureme

### FetchDetectedChannelArray(string, double, ref int[], ref int[], ref RFmxWcdmaMXModAccDetectedModulationType[], ref RFmxWcdmaMXModAccDetectedBranch[])

Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the [SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setchannelconfigurationmode__string-rfmxwcdmamxchannelconfigurationmode.html) method to [AutoDetect](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html) for the ModAcc measurement. When you set the Channel Configuration Mode method to [UserDefined](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html) or [TestModel](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html), it returns the corresponding results for the configured channels of all the carriers. 
 Use "carrier(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchDetectedChannelArray(string selectorString, double timeout, ref int[] detectedSpreadingFactor, ref int[] detectedSpreadingCode, ref RFmxWcdmaMXModAccDetectedModulationType[] detectedModulationType, ref RFmxWcdmaMXModAccDetectedBranch[] detectedBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and carrier number. If you do not specify the result name, the default result instance is used. Example: "carrier0" "result::r1/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| detectedSpreadingFactor | ref int[] | Upon return, contains an array of spreading factors of the detected channels, when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns an array of spreading factors of the configured channels. |
| detectedSpreadingCode | ref int[] | Upon return, contains an array of spreading codes of the detected channels, when you set the Channel Configuration Mode method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns an array of spreading codes of the configured channels. |
| detectedModulationType | ref RFmxWcdmaMXModAccDetectedModulationType[] | Upon return, contains an array of the modulation types of the detected channels, when you set the Channel Configuration Mode method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns the spreading code of the configured channel of a carrier. |
| detectedBranch | ref RFmxWcdmaMXModAccDetectedBranch[] | Upon return, contains an array of branches of the detected channels when you set the Channel Configuration Mode method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, the measurement returns an array of branches of the configured channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchmulticarrieriqimpairments__string-double-out-out-out.html language=enus -->
## TOPIC 00108: FetchMulticarrierIQImpairments(string, double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchmulticarrieriqimpairments__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchmulticarrieriqimpairments__string-double-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q impairments for a multicarrier signal.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchMulticarrierIQImpairments(string selectorString, double timeout, out double multicarrierIQOriginOffset, out double multicarrierIQGainImbalance, out double multicarrierIQQuadratureEr

### FetchMulticarrierIQImpairments(string, double, out double, out double, out double)

Fetches the I/Q impairments for a multicarrier signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchMulticarrierIQImpairments(string selectorString, double timeout, out double multicarrierIQOriginOffset, out double multicarrierIQGainImbalance, out double multicarrierIQQuadratureError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| multicarrierIQOriginOffset | out double | Upon return, contains the estimated I/Q origin offset of the multicarrier signal when the SetTransmitterArchitecture(string, RFmxWcdmaMXTransmitterArchitecture) method is set to LOPerBand. This value is expressed in dB. This result is useful when the LO is at the center of the multicarrier signal. |
| multicarrierIQGainImbalance | out double | Upon return, contains NaN. This parameter has been added for future use. |
| multicarrierIQQuadratureError | out double | Upon return, contains NaN. This parameter has been added for future use. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchpeakactivecde__string-double-out-out-out-out.1.html language=enus -->
## TOPIC 00109: FetchPeakActiveCde(string, double, out double, out int, out int, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchpeakactivecde__string-double-out-out-out-out.1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchpeakactivecde__string-double-out-out-out-out.1.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak value among the code domain errors (CDEs) of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. Use "carrier(n)" as the selector string to read results from this method.SyntaxNames

### FetchPeakActiveCde(string, double, out double, out int, out int, out int)

Fetches the peak value among the code domain errors (CDEs) of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. 
 Use "carrier(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchPeakActiveCde(string selectorString, double timeout, out double peakActiveCde, out int peakActiveCdeSpreadingFactor, out int peakActiveCdeCode, out int peakActiveCdeBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and carrier number. If you do not specify the result name, the default result instance is used. Example: "carrier0" "result::r1/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| peakActiveCde | out double | Upon return, contains the maximum value among the active code domain errors for a carrier. This value is expressed in dB. |
| peakActiveCdeSpreadingFactor | out int | Upon return, contains the spreading factor of the channel corresponding to the value of the peakActiveCDE parameter for a carrier. |
| peakActiveCdeCode | out int | Upon return, contains the spreading code of the channel corresponding to the value of the peakActiveCDE parameter for a carrier. |
| peakActiveCdeBranch | out int | Upon return, contains the branch of the channel corresponding to the value of the peakActiveCDE parameter for a carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchrcde__string-double-out-out-out-out.1.html language=enus -->
## TOPIC 00110: FetchRcde(string, double, out double, out int, out int, out RFmxWcdmaMXModAccPeakRcdeBranch)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchrcde__string-double-out-out-out-out.1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchrcde__string-double-out-out-out-out.1.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. Use "carrier(n)" as the selector string to read results from this method.SyntaxNamespa

### FetchRcde(string, double, out double, out int, out int, out RFmxWcdmaMXModAccPeakRcdeBranch)

Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. 
 Use "carrier(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchRcde(string selectorString, double timeout, out double peakRcde, out int peakRcdeSpreadingFactor, out int peakRcdeCode, out RFmxWcdmaMXModAccPeakRcdeBranch peakRcdeBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and carrier number. If you do not specify the result name, the default result instance is used. Example: "carrier0" "result::r1/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| peakRcde | out double | Upon return, contains the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB. |
| peakRcdeSpreadingFactor | out int | Upon return, contains the spreading factor of the channel corresponding to the value of the peakRCDE parameter for a carrier. |
| peakRcdeCode | out int | Upon return, contains the spreading code of the channel corresponding to the value of the peakRCDE parameter for a carrier. |
| peakRcdeBranch | out RFmxWcdmaMXModAccPeakRcdeBranch | Upon return, contains the branch of the channel corresponding to the value of the peakRCDE parameter for a carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchrcdearray__string-double-ref-ref-ref-ref.html language=enus -->
## TOPIC 00111: FetchRcdeArray(string, double, ref double[], ref int[], ref int[], ref RFmxWcdmaMXModAccPeakRcdeBranch[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchrcdearray__string-double-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-fetchrcdearray__string-double-ref-ref-ref-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches arrays of peak relative CDE values of the active channels, of the carriers and the corresponding code numbers, spreading factors, and branches. Each element in these arrays corresponds to the peak value among the relative code domain errors of all the active channels in each carrier.SyntaxNa

### FetchRcdeArray(string, double, ref double[], ref int[], ref int[], ref RFmxWcdmaMXModAccPeakRcdeBranch[])

Fetches arrays of peak relative CDE values of the active channels, of the carriers and the corresponding code numbers, spreading factors, and branches. Each element in these arrays corresponds to the peak value among the relative code domain errors of all the active channels in each carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchRcdeArray(string selectorString, double timeout, ref double[] peakRcde, ref int[] peakRcdeSpreadingFactor, ref int[] peakRcdeCode, ref RFmxWcdmaMXModAccPeakRcdeBranch[] peakRcdeBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| peakRcde | ref double[] | Upon return, contains the array of maximum value among the relative code domain errors (RCDEs) for all active channels. This value is expressed in dB. |
| peakRcdeSpreadingFactor | ref int[] | Upon return, contains the array of spreading factors of the channel corresponding to the value of the peakRCDE parameter. |
| peakRcdeCode | ref int[] | Upon return, contains the array of spreading codes of the channel corresponding to the value of the peakRCDE parameter. |
| peakRcdeBranch | ref RFmxWcdmaMXModAccPeakRcdeBranch[] | Upon return, contains the array of branches of the channel corresponding to the value of the peakRCDE parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getnumberofdetectedchannels__string-out.html language=enus -->
## TOPIC 00112: GetNumberOfDetectedChannels(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getnumberofdetectedchannels__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getnumberofdetectedchannels__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of detected channels when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, this method returns the number of configured channels. SyntaxNamespace: N

### GetNumberOfDetectedChannels(string, out int)

Gets the number of detected channels when you set the [SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setchannelconfigurationmode__string-rfmxwcdmamxchannelconfigurationmode.html) method to [AutoDetect](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html). If you set the Channel Configuration Mode method to [UserDefined](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html) or [TestModel](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html), this method returns the number of configured channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetNumberOfDetectedChannels(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsNumberOfDetectedChannels](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of detected channels when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, this method returns the number of configured channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getpeakrcdebranch__string-out.html language=enus -->
## TOPIC 00113: GetPeakRcdeBranch(string, out RFmxWcdmaMXModAccPeakRcdeBranch)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getpeakrcdebranch__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getpeakrcdebranch__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the branch of the channel corresponding to the value of the GetPeakRcde(string, out double) method for a carrier. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetPeakRcdeBranch(string selectorString, out RFmxWcdmaMXModAccPeakRcdeBranch value)RemarksThis method gets the value of M

### GetPeakRcdeBranch(string, out RFmxWcdmaMXModAccPeakRcdeBranch)

Gets the branch of the channel corresponding to the value of the [GetPeakRcde(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxmodaccresults-getpeakrcde__string-out.html) method for a carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetPeakRcdeBranch(string selectorString, out RFmxWcdmaMXModAccPeakRcdeBranch value)

#### Remarks

This method gets the value of [ModAccResultsPeakRcdeBranch](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxWcdmaMXModAccPeakRcdeBranch | Upon return, contains the branch of the channel corresponding to the value of the GetPeakRcde(string, out double) method for a carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwamplitudecorrectiontype.html language=enus -->
## TOPIC 00114: RFmxWcdmaMXObwAmplitudeCorrectionType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwamplitudecorrectiontype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: National

### RFmxWcdmaMXObwAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXObwAmplitudeCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-configuresweeptime__string-rfmxwcdmamxobwsweeptimeauto-double.html language=enus -->
## TOPIC 00115: ConfigureSweepTime(string, RFmxWcdmaMXObwSweepTimeAuto, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-configuresweeptime__string-rfmxwcdmamxobwsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-configuresweeptime__string-rfmxwcdmamxobwsweeptimeauto-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureSweepTime(string selectorString, RFmxWcdmaMXObwSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is

### ConfigureSweepTime(string, RFmxWcdmaMXObwSweepTimeAuto, double)

Configures the sweep time interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureSweepTime(string selectorString, RFmxWcdmaMXObwSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxWcdmaMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00116: GetAmplitudeCorrectionType(string, out RFmxWcdmaMXObwAmplitudeCorrectionType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: NationalInstr

### GetAmplitudeCorrectionType(string, out RFmxWcdmaMXObwAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxWcdmaMXObwAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [ObwAmplitudeCorrectionType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXObwAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxobwamplitudecorrectiontype.html language=enus -->
## TOPIC 00117: SetAmplitudeCorrectionType(string, RFmxWcdmaMXObwAmplitudeCorrectionType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxobwamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxobwamplitudecorrectiontype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: NationalInstr

### SetAmplitudeCorrectionType(string, RFmxWcdmaMXObwAmplitudeCorrectionType)

Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxWcdmaMXObwAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [ObwAmplitudeCorrectionType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXObwAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setaveragingenabled__string-rfmxwcdmamxobwaveragingenabled.html language=enus -->
## TOPIC 00118: SetAveragingEnabled(string, RFmxWcdmaMXObwAveragingEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setaveragingenabled__string-rfmxwcdmamxobwaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setaveragingenabled__string-rfmxwcdmamxobwaveragingenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAveragingEnabled(string selectorString, RFmxWcdmaMXObwAveragingEnabled value)RemarksThis method sets the value of ObwAveragingEnabled attribute.The default value is False.Paramete

### SetAveragingEnabled(string, RFmxWcdmaMXObwAveragingEnabled)

Sets whether to enable averaging for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAveragingEnabled(string selectorString, RFmxWcdmaMXObwAveragingEnabled value)

#### Remarks

This method sets the value of [ObwAveragingEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXObwAveragingEnabled | Specifies whether to enable averaging for the OBW measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00119: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of ObwMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStrings

### SetMeasurementEnabled(string, bool)

Sets whether to enable the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ObwMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the OBW measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00120: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXObwRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXObwRbwFilterType) method to Gaussian or Flat. This v

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the [SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXObwRbwAutoBandwidth)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfilterautobandwidth__string-rfmxwcdmamxobwrbwautobandwidth.html) method to [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwautobandwidth.html). This method is valid only if you set the [SetRbwFilterType(string, RFmxWcdmaMXObwRbwFilterType)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfiltertype__string-rfmxwcdmamxobwrbwfiltertype.html) method to [Gaussian](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwfiltertype.html) or [Flat](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwfiltertype.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [ObwRbwFilterBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 30 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXObwRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXObwRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfiltertype__string-rfmxwcdmamxobwrbwfiltertype.html language=enus -->
## TOPIC 00121: SetRbwFilterType(string, RFmxWcdmaMXObwRbwFilterType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfiltertype__string-rfmxwcdmamxobwrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwconfiguration-setrbwfiltertype__string-rfmxwcdmamxobwrbwfiltertype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRbwFilterType(string selectorString, RFmxWcdmaMXObwRbwFilterType value)RemarksThis method sets the value of ObwRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDescriptions

### SetRbwFilterType(string, RFmxWcdmaMXObwRbwFilterType)

Sets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRbwFilterType(string selectorString, RFmxWcdmaMXObwRbwFilterType value)

#### Remarks

This method sets the value of [ObwRbwFilterType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwautobandwidth.html language=enus -->
## TOPIC 00122: RFmxWcdmaMXObwRbwAutoBandwidth Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwautobandwidth.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXObwRbwAutoBandwidthMembersNameValueDescriptionFalse0The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. True1The measurement uses

### RFmxWcdmaMXObwRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXObwRbwAutoBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. |
| True | 1 | The measurement uses an RBW value of 30 kHz. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwfiltertype.html language=enus -->
## TOPIC 00123: RFmxWcdmaMXObwRbwFilterType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwrbwfiltertype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXObwRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is applied. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW filter with a flat response

### RFmxWcdmaMXObwRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXObwRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is applied. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-fetchmeasurement__string-double-out-out-out-out.html language=enus -->
## TOPIC 00124: FetchMeasurement(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-fetchmeasurement__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-fetchmeasurement__string-double-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchMeasurement(string selectorString, double timeout, out double occupiedBandwidth, out double abso

### FetchMeasurement(string, double, out double, out double, out double, out double)

Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchMeasurement(string selectorString, double timeout, out double occupiedBandwidth, out double absolutePower, out double startFrequency, out double stopFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| occupiedBandwidth | out double | Upon return, contains the bandwidth containing 99% of the total integrated power of the acquired signal, around the center of the carriers. |
| absolutePower | out double | Upon return, contains the carrier power integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
| startFrequency | out double | Upon return, contains the start frequency of the occupiedBandwidth parameter. |
| stopFrequency | out double | Upon return, contains the stop frequency of the occupiedBandwidth parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-fetchspectrum__string-double-ref.html language=enus -->
## TOPIC 00125: FetchSpectrum(string, double, ref Spectrum< float >)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-fetchspectrum__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-fetchspectrum__string-double-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the OBW measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name

### FetchSpectrum(string, double, ref Spectrum< float >)

Fetches the spectrum used for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| spectrum | ref Spectrum< float > | Upon return, contains the trace of power levels in the spectral domain. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-getstopfrequency__string-out.html language=enus -->
## TOPIC 00126: GetStopFrequency(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-getstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults-getstopfrequency__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the occupied bandwidth.This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of ObwResultsStopFrequency attribute.ParametersNameTypeDescriptionse

### GetStopFrequency(string, out double)

Gets the stop frequency of the occupied bandwidth.This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsStopFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the stop frequency of the occupied bandwidth.This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXObwResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults.html language=enus -->
## TOPIC 00127: RFmxWcdmaMXObwResults Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwresults.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the OBW measurement results. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXObwResults : RFmxWcdmaMXSubObjectMethodsNameDescriptionFetchMeasurement(string, double, out double, out double, out double, out dou

### RFmxWcdmaMXObwResults Class

Provides methods to fetch and read the OBW measurement results.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXObwResults : RFmxWcdmaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMeasurement(string, double, out double, out double, out double, out double) | Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power. |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for the OBW measurement. |
| GetAbsolutePower(string, out double) | Gets the total integrated power of the acquired signal.This value is expressed in dBm. |
| GetOccupiedBandwidth(string, out double) | Gets the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers.This value is expressed in Hz. |
| GetStartFrequency(string, out double) | Gets the start frequency of the occupied bandwidth.This value is expressed in Hz. |
| GetStopFrequency(string, out double) | Gets the stop frequency of the occupied bandwidth.This value is expressed in Hz. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwsweeptimeauto.html language=enus -->
## TOPIC 00128: RFmxWcdmaMXObwSweepTimeAuto Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxobwsweeptimeauto.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXObwSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The measur

### RFmxWcdmaMXObwSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXObwSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses a sweep time value of one slot duration. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html language=enus -->
## TOPIC 00129: RFmxWcdmaMXPropertyId Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXPropertyIdMembersNameValueDescriptionAcpAllTracesEnabled5247009Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. AcpAveragingCount524

### RFmxWcdmaMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AcpAllTracesEnabled | 5247009 | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| AcpAveragingCount | 5246997 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXAcpAveragingEnabled) to True. |
| AcpAveragingEnabled | 5246998 | Specifies whether to enable averaging for the ACP measurement. |
| AcpAveragingType | 5247000 | Specifies the averaging type for averaging the spectrum of multiple acquisitions. The averaged spectrum is used for ACP measurement. |
| AcpFarIFOutputPowerOffset | 5247030 | Specifies the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB. |
| AcpIFOutputPowerOffsetAuto | 5247028 | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |
| AcpMeasurementEnabled | 5246976 | Specifies whether to enable the ACP measurement. |
| AcpMeasurementMethod | 5246994 | Specifies the method for performing the ACP measurement. |
| AcpNearIFOutputPowerOffset | 5247029 | Specifies the power offset to use to adjust the IF output power level for offset channels near the carrier channel. Adjusting the IF output power level improves the dynamic range. This value is expressed in dB. |
| AcpNoiseCompensationEnabled | 5247008 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. |
| AcpNumberOfAnalysisThreads | 5246996 | Specifies the maximum number of threads used for parallelism for the ACP measurement. |
| AcpNumberOfOffsets | 5246984 | Specifies the number of offset channels. |
| AcpOffsetPowerReferenceCarrier | 5246988 | Specifies the carrier used as the power reference to measure the offset channel relative power. |
| AcpOffsetPowerReferenceSpecific | 5246989 | Specifies the index of the reference carrier. |
| AcpRbwFilterAutoBandwidth | 5247003 | Specifies whether the measurement computes the RBW. |
| AcpRbwFilterBandwidth | 5247004 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXAcpRbwAutoBandwidth) method to False.This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXAcpRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz. |
| AcpRbwFilterType | 5247005 | Specifies the shape of the digital RBW filter. |
| AcpResultsCarrierAbsolutePower | 5247014 | Returns the carrier power.This value is expressed in dBm. |
| AcpResultsCarrierRelativePower | 5247015 | Returns the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. |
| AcpResultsLowerOffsetAbsolutePower | 5247020 | Returns the lower offset channel power. This value is expressed in dBm. |
| AcpResultsLowerOffsetRelativePower | 5247021 | Returns the lower offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |
| AcpResultsTotalCarrierPower | 5247010 | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(string, out double) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |
| AcpResultsUpperOffsetAbsolutePower | 5247026 | Returns the upper offset channel power.This value is expressed in dBm. |
| AcpResultsUpperOffsetRelativePower | 5247027 | Returns the upper offset channel power relative to the power of the carrier(s) that you specify in the SetOffsetPowerReferenceCarrier(string, RFmxWcdmaMXAcpOffsetPowerReferenceCarrier) method.This value is expressed in dB. |
| AcpSweepTimeAuto | 5247006 | Specifies whether the measurement computes the sweep time. |
| AcpSweepTimeInterval | 5247007 | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |
| AutoLevelInitialReferenceLevel | 5296128 | Specifies the initial reference level that the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal.This value is expressed in dBm. |
| Band | 5242912 | Specifies the Universal Mobile Telecommunications System (UMTS) operation band. |
| Branch | 5242904 | Specifies the branch on which the data is modulated in the channel. |
| CarrierFrequency | 5242895 | Specifies the center frequency of the carrier, relative to the RF SetCenterFrequency(string, double).This value is expressed in Hz. |
| CenterFrequency | 5242881 | For a single-carrier measurement, this method specifies the center frequency of the acquired RF signal.For multi-carrier measurements, this method specifies the reference frequency for the values in the SetCarrierFrequency(string, double) method. This value is expressed in Hz. |
| ChannelConfigurationMode | 5242896 | Specifies the channel configuration mode. |
| ChpAllTracesEnabled | 5255188 | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| ChpAveragingCount | 5255174 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXChpAveragingEnabled) method to True. |
| ChpAveragingEnabled | 5255175 | Specifies whether to enable averaging for the CHP measurement. |
| ChpAveragingType | 5255177 | Specifies the averaging type for averaging the spectrum of multiple acquisitions. |
| ChpMeasurementEnabled | 5255168 | Specifies whether to enable the CHP measurement. |
| ChpNumberOfAnalysisThreads | 5255171 | Specifies the maximum number of threads used for parallelism for the CHP measurement. |
| ChpRbwFilterAutoBandwidth | 5255180 | Specifies whether the measurement computes the RBW. |
| ChpRbwFilterBandwidth | 5255181 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXChpRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXChpRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz. |
| ChpRbwFilterType | 5255182 | Specifies the shape of the digital RBW filter. |
| ChpResultsCarrierAbsolutePower | 5255189 | Returns the carrier power integrated over a bandwidth of 5 MHz. |
| ChpResultsCarrierRelativePower | 5255193 | Returns the carrier power relative to the value of the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| ChpResultsTotalCarrierPower | 5255192 | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the GetCarrierAbsolutePower(string, out double) method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |
| ChpSweepTimeAuto | 5255185 | Specifies whether the measurement computes the sweep time. |
| ChpSweepTimeInterval | 5255186 | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
| DigitalEdgeTriggerEdge | 5242886 | Specifies the active edge for the trigger. |
| DigitalEdgeTriggerSource | 5242885 | Specifies the source terminal for the digital edge trigger. |
| ExternalAttenuation | 5242883 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
| IQPowerEdgeTriggerLevel | 5242888 | Specifies the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxWcdmaMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. |
| IQPowerEdgeTriggerLevelType | 5246975 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. |
| IQPowerEdgeTriggerSlope | 5242889 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. |
| IQPowerEdgeTriggerSource | 5242887 | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxWcdmaMXTriggerType) method to IQPowerEdge. |
| ModAccAllTracesEnabled | 5312520 | Specifies whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. |
| ModAccDownlinkTimingChannelSpreadingFactor | 5312521 | This enum value has been deprecated. |
| ModAccDownlinkTimingChannelCode | 5312522 | This enum value has been deprecated. |
| ModAccIQOffsetRemovalEnabled | 5312518 | Specifies whether to remove the I/Q offset before the ModAcc measurement. |
| ModAccMeasurementEnabled | 5312512 | Specifies whether to enable the ModAcc measurement. |
| ModAccMeasurementLength | 5312516 | Specifies the duration of the ModAcc measurement. This value is expressed in slots. |
| ModAccSynchronizationMode | 5312514 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| ModAccMeasurementOffset | 5312515 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXModAccSynchronizationMode) method. |
| ModAccResultsChipRateError | 5312536 | Returns the chip rate error of the composite signal.This value is expressed in ppm. |
| ModAccResultsDetectedBranch | 5312553 | Returns the branch of the detected channel. |
| ModAccResultsDetectedModulationType | 5312552 | Returns the modulation type of the detected channel. |
| ModAccResultsDetectedSpreadingCode | 5312551 | Returns the spreading code of the detected channel. |
| ModAccResultsDetectedSpreadingFactor | 5312550 | Returns the spreading factor of the detected channel. |
| ModAccResultsFrequencyError | 5312535 | Returns the frequency offset of the composite signal.This value is expressed in Hz. |
| ModAccResultsIQOriginOffset | 5312534 | Returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
| ModAccResultsNumberOfDetectedChannels | 5312549 | Returns the number of detected channels when you set the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to AutoDetect. If you set the Channel Configuration Mode method to UserDefined or TestModel, this method returns the number of configured channels. |
| ModAccResultsPeakActiveCde | 5312540 | Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB. |
| ModAccResultsPeakActiveCdeBranch | 5312555 | Returns the branch of the channel corresponding to the value of the GetPeakActiveCde(string, out double) method for a carrier. |
| ModAccResultsPschPower | 5312543 | This enum value has been deprecated. |
| ModAccResultsSschPower | 5312544 | This enum value has been deprecated. |
| ModAccResultsDpchTimingOffset | 5312545 | This enum value has been deprecated. |
| ModAccResultsPeakActiveCdeCode | 5312542 | Returns the spreading code of the channel corresponding to the value of the GetPeakActiveCde(string, out double) method for a carrier. |
| ModAccResultsPeakActiveCdeSpreadingFactor | 5312541 | Returns the spreading factor of the channel corresponding to the value of the GetPeakActiveCde(string, out double) method for a carrier. |
| ModAccResultsPeakCde | 5312537 | Returns the maximum code domain error value (CDE).This value is expressed in dB. |
| ModAccResultsPeakCdeBranch | 5312554 | Returns the branch corresponding to the value of the GetPeakCde(string, out double) method. |
| ModAccResultsPeakCdeCode | 5312539 | Returns the spreading code corresponding to the value of the GetPeakCde(string, out double) method. |
| ModAccResultsPeakEvm | 5312530 | Returns the peak EVM of the composite signal.This value is expressed as a percentage. |
| ModAccResultsPeakRcde | 5312546 | Returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB. |
| ModAccResultsPeakRcdeBranch | 5312556 | Returns the branch of the channel corresponding to the value of the GetPeakRcde(string, out double) method for a carrier. |
| ModAccResultsPeakRcdeCode | 5312548 | Returns the spreading code of the channel corresponding to the value of the GetPeakRcde(string, out double) method for a carrier. |
| ModAccResultsPeakRcdeSpreadingFactor | 5312547 | Returns the spreading factor of the channel corresponding to the value of the GetPeakRcde(string, out double) method for a carrier. |
| ModAccResultsRho | 5312533 | Returns the figure of merit used to characterize the modulation accuracy composite code domain signal. It refers to the fraction of the total power that can be correlated to the correct active channels in the detected reference signal. |
| ModAccResultsRmsEvm | 5312529 | Returns the RMS EVM of the composite signal.This value is expressed as a percentage. |
| ModAccResultsRmsMagnitudeError | 5312531 | Returns the RMS magnitude error of the composite signal.This value is expressed as a percentage. |
| ModAccResultsRmsPhaseError | 5312532 | Returns the RMS phase error of the composite signal.This value is expressed in degrees. |
| ModAccSpectrumInverted | 5312517 | Specifies whether the spectrum of the signal is inverted. |
| ModAccTransientRemovalEnabled | 5312519 | Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |
| ModulationType | 5242903 | Specifies the modulation type for the channel. |
| NumberOfCarriers | 5242894 | Specifies the number of carriers. |
| NumberOfChannels | 5242900 | Specifies the number of user-defined channels. |
| ObwAllTracesEnabled | 5267474 | Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. |
| ObwAveragingCount | 5267462 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXObwAveragingEnabled) method to True. |
| ObwAveragingEnabled | 5267463 | Specifies whether to enable averaging for the OBW measurement. |
| ObwAveragingType | 5267465 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| ObwMeasurementEnabled | 5267456 | Specifies whether to enable the OBW measurement. |
| ObwNumberOfAnalysisThreads | 5267459 | Specifies the maximum number of threads used for parallelism for the OBW measurement. |
| ObwRbwFilterAutoBandwidth | 5267468 | Specifies whether the measurement computes the RBW. |
| ObwRbwFilterBandwidth | 5267469 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxWcdmaMXObwRbwAutoBandwidth) method to False. This method is valid only if you set the SetRbwFilterType(string, RFmxWcdmaMXObwRbwFilterType) method to Gaussian or Flat. This value is expressed in Hz. |
| ObwRbwFilterType | 5267470 | Specifies the shape of the digital RBW filter. |
| ObwResultsAbsolutePower | 5267476 | Returns the total integrated power of the acquired signal.This value is expressed in dBm. |
| ObwResultsOccupiedBandwidth | 5267475 | Returns the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers.This value is expressed in Hz. |
| ObwResultsStartFrequency | 5267477 | Returns the start frequency of the occupied bandwidth.This value is expressed in Hz. |
| ObwResultsStopFrequency | 5267478 | Returns the stop frequency of the occupied bandwidth.This value is expressed in Hz. |
| ObwSweepTimeAuto | 5267471 | Specifies whether the measurement computes the sweep time. |
| ObwSweepTimeInterval | 5267472 | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |
| ReferenceLevel | 5242882 | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ResultFetchTimeout | 5292032 | Specifies the time to wait before results are available in the RFmxWCDMA_PropertyNode.This value is expressed in seconds. |
| SemAllTracesEnabled | 5275687 | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| SemAveragingCount | 5275678 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXSemAveragingEnabled) method to True. |
| SemAveragingEnabled | 5275679 | Specifies whether to enable averaging for the SEM measurement. |
| SemAveragingType | 5275681 | Specifies the averaging type for averaging multiple spectrum acquisitions. |
| SemMeasurementEnabled | 5275648 | Specifies whether to enable the SEM measurement. |
| SemNumberOfAnalysisThreads | 5275677 | Specifies the maximum number of threads used for parallelism for the SEM measurement. |
| SemResultsCarrierRelativeIntegratedPower | 5275694 | Returns the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. |
| SemResultsCarrierAbsoluteIntegratedPower | 5275693 | Returns the carrier power. This value is expressed in dBm. |
| SemResultsCarrierAbsolutePeakPower | 5275695 | Returns the peak power in the carrier channel.This value is expressed in dBm. |
| SemResultsCarrierPeakFrequency | 5275696 | Returns the frequency at which the peak power is observed in the carrier channel.This value is expressed in Hz. |
| SemResultsLowerOffsetMargin | 5275705 | Returns the margin of the lower offset segment.This value is expressed in dB. |
| SemResultsLowerOffsetMarginAbsolutePower | 5275706 | Returns the power at the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in dBm. |
| SemResultsLowerOffsetMarginFrequency | 5275708 | Returns the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in Hz. |
| SemResultsLowerOffsetMarginRelativePower | 5275707 | Returns the power at the frequency corresponding to the value of the GetLowerOffsetMargin(string, out double) method and relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |
| SemResultsLowerOffsetMeasurementStatus | 5275709 | Indicates the measurement status based on the GetLowerOffsetMargin(string, out double) method. |
| SemResultsLowerOffsetAbsolutePeakPower | 5275702 | Returns the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm. |
| SemResultsLowerOffsetPeakFrequency | 5275704 | Returns the frequency at which the peak power is observed in the lower offset segment.This value is expressed in Hz. |
| SemResultsLowerOffsetRelativePeakPower | 5275703 | Returns the peak power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| SemResultsLowerOffsetAbsoluteIntegratedPower | 5275700 | Returns the power measured in the lower, or negative, offset segment.This value is expressed in dBm. |
| SemResultsLowerOffsetRelativeIntegratedPower | 5275701 | Returns the power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| SemResultsMeasurementStatus | 5275689 | Indicates the overall SEM measurement status, based on the value of the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetUpperOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemUpperOffsetMeasurementStatus@) properties. |
| SemResultsTotalCarrierPower | 5275688 | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |
| SemResultsUpperOffsetMargin | 5275718 | Returns the margin of the upper offset segment.This value is expressed in dB. |
| SemResultsUpperOffsetMarginAbsolutePower | 5275719 | Returns the power at the frequency corresponding to the GetUpperOffsetMargin(string, out double) method.This value is expressed in dBm. |
| SemResultsUpperOffsetMarginFrequency | 5275721 | Returns the frequency corresponding to the GetUpperOffsetMargin(string, out double) method. This value is expressed in Hz. |
| SemResultsUpperOffsetMarginRelativePower | 5275720 | Returns the power at the frequency corresponding to the value of the GetUpperOffsetMargin(string, out double) method relative to the value of the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |
| SemResultsUpperOffsetMeasurementStatus | 5275722 | Indicates the measurement status based on the GetUpperOffsetMargin(string, out double) method. |
| SemResultsUpperOffsetAbsolutePeakPower | 5275715 | Returns the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm. |
| SemResultsUpperOffsetPeakFrequency | 5275717 | Returns the frequency at which the peak power is observed in the upper offset segment.This value is expressed in Hz. |
| SemResultsUpperOffsetRelativePeakPower | 5275716 | Returns the peak power measured in the upper, or positive, offset segment relative to the value of the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| SemResultsUpperOffsetAbsoluteIntegratedPower | 5275713 | Returns the power measured in the upper, or positive, offset segment.This value is expressed in dBm. |
| SemResultsUpperOffsetRelativeIntegratedPower | 5275714 | Returns the power measured in the upper, or positive, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| SemSweepTimeAuto | 5275685 | Specifies whether the measurement computes the sweep time. |
| SemSweepTimeInterval | 5275686 | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXSemSweepTimeAuto) method to False.This value is expressed in seconds. |
| SpreadingCode | 5242902 | Specifies the spreading code of the channel. |
| SpreadingFactor | 5242901 | Specifies the spreading factor of the channel. |
| TriggerDelay | 5242890 | Specifies the trigger delay time. This value is expressed in seconds. |
| TriggerMinimumQuietTimeDuration | 5242892 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| LinkDirection | 5242893 | Specifies the link direction of the units under test. The unit under test is either the base station or the user equipment. |
| TriggerMinimumQuietTimeMode | 5242891 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerType | 5242884 | Specifies the trigger type. |
| UplinkScramblingCode | 5242908 | Specifies the scrambling code for the uplink channel. |
| UplinkScramblingType | 5242907 | Specifies the type of scrambling to use for the measurement. |
| UplinkTestModel | 5242905 | Specifies the uplink test model when the user sets the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. |
| DownlinkTestModel | 5242906 | This enum value has been deprecated. |
| DownlinkScramblingType | 5242909 | This enum value has been deprecated. |
| DownlinkScramblingPrimaryCode | 5242910 | This enum value has been deprecated. |
| DownlinkScramblingSecondaryCode | 5242911 | This enum value has been deprecated. |
| ModAccIQGainImbalanceRemovalEnabled | 5312572 | Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. |
| ModAccIQQuadratureErrorRemovalEnabled | 5312573 | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. |
| ModAccRrcFilterEnabled | 5312571 | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| ModAccResultsIQGainImbalance | 5312557 | Returns the I/Q gain imbalance of the composite signal of a carrier. This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. |
| ModAccResultsIQQuadratureError | 5312558 | Returns the I/Q quadrature error of the composite signal of a carrier. This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. |
| AcpCarrierIntegrationBandwidth | 5246981 | Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. |
| AcpOffsetFrequency | 5246986 | Returns the center frequency of the offset channel, relative to the center frequency of the carrier(s). This value is expressed in Hz. |
| AcpOffsetIntegrationBandwidth | 5246990 | Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz. |
| ChpCarrierIntegrationBandwidth | 5255170 | Returns the frequency range, over which the measurement integrates the power. This value is expressed in Hz. |
| ObwSpan | 5267460 | Returns the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz. |
| SemCarrierIntegrationBandwidth | 5275653 | Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. |
| SemNumberOfOffsets | 5275659 | Returns the number of offset segments. |
| SemOffsetStartFrequency | 5275668 | Returns the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. |
| SemOffsetStopFrequency | 5275669 | Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. |
| SemOffsetRbwFilterBandwidth | 5275671 | Returns the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz. |
| SemOffsetRbwFilterType | 5275672 | Returns the shape of the digital RBW filter. |
| SemOffsetBandwidthIntegral | 5275660 | Returns the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. |
| QevmMeasurementEnabled | 5316608 | Specifies whether to enable the QPSK EVM measurement. |
| QevmMeasurementLength | 5316611 | Specifies the duration of the QEVM measurement. This value is expressed in chips. |
| QevmAveragingEnabled | 5316613 | Specifies whether to enable averaging for the QEVM measurement. |
| QevmAveragingCount | 5316614 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled) method to True. |
| QevmSpectrumInverted | 5316615 | Specifies whether the spectrum of the signal is inverted. |
| QevmIQOffsetRemovalEnabled | 5316616 | Specifies whether to remove the I/Q offset before the QEVM measurement. |
| QevmRrcFilterEnabled | 5316619 | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| QevmAllTracesEnabled | 5316620 | Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |
| QevmNumberOfAnalysisThreads | 5316621 | Specifies the maximum number of threads used for parallelism for the QEVM measurement. |
| QevmResultsMeanRmsEvm | 5316622 | Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. |
| QevmResultsMaximumRmsEvm | 5316623 | Returns the maximum value of the RMS EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. |
| QevmResultsMeanPeakEvm | 5316624 | Returns the mean of peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the peak EVMs over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. |
| QevmResultsMaximumPeakEvm | 5316625 | Returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. |
| QevmResultsMeanMagnitudeError | 5316626 | Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |
| QevmResultsMaximumMagnitudeError | 5316627 | Returns the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |
| QevmResultsMeanPhaseError | 5316628 | Returns the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. |
| QevmResultsMaximumPhaseError | 5316629 | Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. |
| QevmResultsMeanFrequencyError | 5316630 | Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. |
| QevmResultsMaximumFrequencyError | 5316631 | Returns the maximum value of the frequency errors for a QPSK signal. This value is expressed in Hz.This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. |
| QevmResultsMeanIQOriginOffset | 5316632 | Returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
| QevmResultsMaximumIQOriginOffset | 5316633 | Returns the maximum value of the I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The I/Q Origin Offset is the amount of DC component present in the I/Q signal being measured. |
| QevmResultsMeanChipRateError | 5316634 | Returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver. |
| QevmResultsMaximumChipRateError | 5316635 | Returns the maximum chip rate error value for a QPSK signal. This value is expressed in ppm. This value is obtained over all averaging iterations. The number of acquisitions is specified by the SetAveragingCount(string, int) method.The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver. |
| SlotPhaseMeasurementEnabled | 5324800 | Specifies whether to enable the SlotPhase measurement. |
| SlotPhaseSynchronizationMode | 5324802 | Specifies whether the measurement is performed from the frame or the slot boundary. |
| SlotPhaseMeasurementOffset | 5324803 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode) method. |
| SlotPhaseMeasurementLength | 5324804 | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |
| SlotPhaseSpectrumInverted | 5324807 | Specifies whether the signal spectrum is inverted. |
| SlotPhaseTransientRemovalEnabled | 5324808 | Specifies whether the SlotPhase measurement excludes 25 microseconds from the start and end of each slot while computing the linear-fit chip phase error, which is used to compute phase discontinuities at the slot boundaries. |
| SlotPhaseRrcFilterEnabled | 5324809 | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| SlotPhaseAllTracesEnabled | 5324812 | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| SlotPhaseResultsMaximumPhaseDiscontinuity | 5324814 | Returns the maximum of all the measured phase discontinuity values at the slot boundaries. |
| SlotPhaseResultsDiscontinuityCountGreaterThanLimit1 | 5324815 | Returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |
| SlotPhaseResultsDiscontinuityCountGreaterThanLimit2 | 5324816 | Returns the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |
| SlotPhaseResultsDiscontinuityMinimumDistance | 5324817 | Returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. |
| LimitedConfigurationChange | 5296131 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| CdaMeasurementEnabled | 5328896 | Specifies whether to enable the CDA measurement. |
| CdaSynchronizationMode | 5328898 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| CdaMeasurementOffset | 5328899 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXCdaSynchronizationMode) method. |
| CdaMeasurementLength | 5328900 | Specifies the duration of the code domain measurement. This value is expressed in slots. |
| CdaMeasurementChannelSpreadingFactor | 5328905 | Specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| CdaMeasurementChannelSpreadingCode | 5328906 | Specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| CdaMeasurementChannelModulationType | 5328907 | Specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| CdaMeasurementChannelBranch | 5328908 | Specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| CdaPowerUnit | 5328909 | Specifies the measurement unit of all power results, except GetTotalPower(string, out double). |
| CdaSpectrumInverted | 5328901 | Specifies whether the spectrum of the signal is inverted. |
| CdaIQOffsetRemovalEnabled | 5328902 | Specifies whether to remove the I/Q offset before the CDA measurement. |
| CdaRrcFilterEnabled | 5328903 | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| CdaAllTracesEnabled | 5328917 | Specifies whether to enable the traces after performing the CDA measurement. |
| CdaResultsRmsSymbolEvm | 5328919 | Returns the RMS EVM for the measurement channel. This value is expressed as a percentage. |
| CdaResultsPeakSymbolEvm | 5328920 | Returns the peak EVM for the measurement channel. This value is expressed as a percentage. |
| CdaResultsRmsSymbolMagnitudeError | 5328921 | Returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage. |
| CdaResultsRmsSymbolPhaseError | 5328922 | Returns the RMS phase error for the measurement channel. This value is expressed in degrees. |
| CdaResultsMeanSymbolPower | 5328924 | Returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. |
| CdaResultsChipRateError | 5328941 | Returns the chip rate error of the composite signal. This value is expressed in ppm. |
| CdaResultsTotalPower | 5328923 | Returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. |
| CdaResultsTotalActivePower | 5328927 | Returns the sum of all the active channel powers. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsMeanActivePower | 5328930 | Returns the average of all the active channel powers. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsPeakActivePower | 5328929 | Returns the largest code power among the set of active channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsMeanInactivePower | 5328932 | Returns the average code power among the set of inactive channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsPeakInactivePower | 5328931 | Returns the largest code power among the set of inactive channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsIMeanActivePower | 5328937 | Returns the average code power among the set of active in-phase channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsQMeanActivePower | 5328938 | Returns the average code power among the set of active quadrature-phase channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsIPeakInactivePower | 5328939 | Returns the largest code power among the set of inactive in-phase channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| CdaResultsQPeakInactivePower | 5328940 | Returns the largest code power among the set of inactive quadrature-phase channels in the code domain. If you set the SetPowerUnit(string, RFmxWcdmaMXCdaPowerUnit) method to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the GetTotalPower(string, out double) method. This value is expressed in dB or dBm. |
| SlotPowerMeasurementEnabled | 5332992 | Specifies whether to enable the SlotPower measurement. |
| SlotPowerSynchronizationMode | 5332999 | Specifies whether the measurement is performed from the frame or slot boundary. |
| SlotPowerMeasurementOffset | 5332994 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXSlotPowerSynchronizationMode) method. |
| SlotPowerMeasurementLength | 5332995 | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |
| SlotPowerSpectrumInverted | 5332996 | Specifies whether the spectrum of the signal is inverted. |
| SlotPowerRrcFilterEnabled | 5332997 | Specifies whether to enable the RRC filter. |
| ModAccResultsMultiCarrierIQOriginOffset | 5312559 | Returns the estimated I/Q origin offset of the multicarrier signal when the SetTransmitterArchitecture(string, RFmxWcdmaMXTransmitterArchitecture) method is set to LOPerBand. This value is expressed in dB. |
| AcpAmplitudeCorrectionType | 5247032 | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| AcpSequentialFftSize | 5247033 | Specifies the number of bins to use for FFT computation when the SetMeasurementMethod(string, RFmxWcdmaMXAcpMeasurementMethod) method is set to SequentialFft. |
| ChpAmplitudeCorrectionType | 5255195 | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| ObwAmplitudeCorrectionType | 5267482 | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| SemAmplitudeCorrectionType | 5275724 | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| TransmitterArchitecture | 5296129 | Specifies the RF architecture at the transmitter for a multicarrier signal. |
| SelectedPorts | 5246973 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstrMX.GetAvailablePorts Method to get the valid port names. |
| ReferenceLevelHeadroom | 5246972 | Specifies the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| AcpFftOverlapMode | 5247034 | Specifies how overlapping is applied when computing the FFT of the acquired samples. |
| AcpFftOverlap | 5247035 | Returns the number of samples to overlap between consecutive chunks while performing FFT. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm-configuration.html language=enus -->
## TOPIC 00130: Configuration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm-configuration.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXQevmConfiguration instance that provides methods to configure the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXQevmConfiguration Configuration { get; }

### Configuration

Gets the [RFmxWcdmaMXQevmConfiguration](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration.html) instance that provides methods to configure the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXQevmConfiguration](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration.html) Configuration { get; }

Parent topic:

RFmxWcdmaMXQevm Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm-results.html language=enus -->
## TOPIC 00131: Results

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm-results.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXQevmResults instance that provides methods to fetch and read the QEVM measurement results. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXQevmResults Results { get; }

### Results

Gets the [RFmxWcdmaMXQevmResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults.html) instance that provides methods to fetch and read the QEVM measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXQevmResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults.html) Results { get; }

Parent topic:

RFmxWcdmaMXQevm Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm.html language=enus -->
## TOPIC 00132: RFmxWcdmaMXQevm Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevm.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the QEVM measurement. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXQevm : RFmxWcdmaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxWcdmaMXQevmConfiguration instance that provides methods to configure the QEVM measur

### RFmxWcdmaMXQevm Class

Represents the QEVM measurement.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXQevm : RFmxWcdmaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxWcdmaMXQevmConfiguration instance that provides methods to configure the QEVM measurement. |
| Results | Gets the RFmxWcdmaMXQevmResults instance that provides methods to fetch and read the QEVM measurement results. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html language=enus -->
## TOPIC 00133: RFmxWcdmaMXQevmAveragingEnabled Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXQevmAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The QEVM measurement uses the value of the SetAverag

### RFmxWcdmaMXQevmAveragingEnabled Enumeration

Specifies whether to enable averaging for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXQevmAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The QEVM measurement uses the value of the SetAveragingCount(string, int) method as the number of acquisitions over which the QEVM measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-configureaveraging__string-rfmxwcdmamxqevmaveragingenabled-int.html language=enus -->
## TOPIC 00134: ConfigureAveraging(string, RFmxWcdmaMXQevmAveragingEnabled, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-configureaveraging__string-rfmxwcdmamxqevmaveragingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-configureaveraging__string-rfmxwcdmamxqevmaveragingenabled-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the QEVM measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureAveraging(string selectorString, RFmxWcdmaMXQevmAveragingEnabled averagingEnabled, int averagingCount)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal n

### ConfigureAveraging(string, RFmxWcdmaMXQevmAveragingEnabled, int)

Configures averaging for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureAveraging(string selectorString, RFmxWcdmaMXQevmAveragingEnabled averagingEnabled, int averagingCount)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxWcdmaMXQevmAveragingEnabled | Specifies whether to enable averaging for the QEVM measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-configuremeasurementlength__string-int.html language=enus -->
## TOPIC 00135: ConfigureMeasurementLength(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-configuremeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-configuremeasurementlength__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement length of the QEVM measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureMeasurementLength(string selectorString, int measurementLength)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when cre

### ConfigureMeasurementLength(string, int)

Configures the measurement length of the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureMeasurementLength(string selectorString, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementLength | int | Specifies the duration of the QEVM measurement. The value is expressed in chips. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00136: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of QevmAllTracesEnabled attribute.The default va

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [QevmAllTracesEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00137: GetAveragingCount(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of Qev

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingenabled__string-rfmxwcdmamxqevmaveragingenabled.html) method to [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [QevmAveragingCount](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00138: GetAveragingEnabled(string, out RFmxWcdmaMXQevmAveragingEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAveragingEnabled(string selectorString, out RFmxWcdmaMXQevmAveragingEnabled value)RemarksThis method gets the value of QevmAveragingEnabled attribute.The default value is False.P

### GetAveragingEnabled(string, out RFmxWcdmaMXQevmAveragingEnabled)

Gets whether to enable averaging for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAveragingEnabled(string selectorString, out RFmxWcdmaMXQevmAveragingEnabled value)

#### Remarks

This method gets the value of [QevmAveragingEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXQevmAveragingEnabled | Upon return, contains whether to enable averaging for the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getiqoffsetremovalenabled__string-out.html language=enus -->
## TOPIC 00139: GetIQOffsetRemovalEnabled(string, out RFmxWcdmaMXQevmIQOffsetRemovalEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getiqoffsetremovalenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getiqoffsetremovalenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to remove the I/Q offset before the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetIQOffsetRemovalEnabled(string selectorString, out RFmxWcdmaMXQevmIQOffsetRemovalEnabled value)RemarksThis method gets the value of QevmIQOffsetRemovalEnabled attribute.Th

### GetIQOffsetRemovalEnabled(string, out RFmxWcdmaMXQevmIQOffsetRemovalEnabled)

Gets whether to remove the I/Q offset before the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetIQOffsetRemovalEnabled(string selectorString, out RFmxWcdmaMXQevmIQOffsetRemovalEnabled value)

#### Remarks

This method gets the value of [QevmIQOffsetRemovalEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmiqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXQevmIQOffsetRemovalEnabled | Upon return, contains whether to remove the I/Q offset before the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00140: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the QPSK EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of QevmMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselec

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the QPSK EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [QevmMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the QPSK EVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00141: GetMeasurementLength(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the QEVM measurement. This value is expressed in chips. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of QevmMeasurementLength attribute.The default value is 2560. NI recomm

### GetMeasurementLength(string, out int)

Gets the duration of the QEVM measurement. This value is expressed in chips.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [QevmMeasurementLength](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 2560. NI recommends that you set this property to n * 512, where the value of n can range from 1 to 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the QEVM measurement. This value is expressed in chips. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00142: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of QevmNumberOfAnalysisThreads attribute.The number of threa

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [QevmNumberOfAnalysisThreads](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getrrcfilterenabled__string-out.html language=enus -->
## TOPIC 00143: GetRrcFilterEnabled(string, out RFmxWcdmaMXQevmRrcFilterEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getrrcfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getrrcfilterenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetRrcFilterEnabled(string selectorString, out RFmxWcdmaMXQevmRrcFilterEnabled value)RemarksThis method gets the va

### GetRrcFilterEnabled(string, out RFmxWcdmaMXQevmRrcFilterEnabled)

Gets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetRrcFilterEnabled(string selectorString, out RFmxWcdmaMXQevmRrcFilterEnabled value)

#### Remarks

This method gets the value of [QevmRrcFilterEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmrrcfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXQevmRrcFilterEnabled | Upon return, contains whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00144: GetSpectrumInverted(string, out RFmxWcdmaMXQevmSpectrumInverted)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetSpectrumInverted(string selectorString, out RFmxWcdmaMXQevmSpectrumInverted value)RemarksThis method gets the value of QevmSpectrumInverted attribute.The default value is False.Paramet

### GetSpectrumInverted(string, out RFmxWcdmaMXQevmSpectrumInverted)

Gets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetSpectrumInverted(string selectorString, out RFmxWcdmaMXQevmSpectrumInverted value)

#### Remarks

This method gets the value of [QevmSpectrumInverted](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXQevmSpectrumInverted | Upon return, contains whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00145: SetAveragingCount(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of QevmAve

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingenabled__string-rfmxwcdmamxqevmaveragingenabled.html) method to [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [QevmAveragingCount](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingenabled__string-rfmxwcdmamxqevmaveragingenabled.html language=enus -->
## TOPIC 00146: SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingenabled__string-rfmxwcdmamxqevmaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingenabled__string-rfmxwcdmamxqevmaveragingenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAveragingEnabled(string selectorString, RFmxWcdmaMXQevmAveragingEnabled value)RemarksThis method sets the value of QevmAveragingEnabled attribute.The default value is False.Param

### SetAveragingEnabled(string, RFmxWcdmaMXQevmAveragingEnabled)

Sets whether to enable averaging for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAveragingEnabled(string selectorString, RFmxWcdmaMXQevmAveragingEnabled value)

#### Remarks

This method sets the value of [QevmAveragingEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXQevmAveragingEnabled | Specifies whether to enable averaging for the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxqevmiqoffsetremovalenabled.html language=enus -->
## TOPIC 00147: SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXQevmIQOffsetRemovalEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxqevmiqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setiqoffsetremovalenabled__string-rfmxwcdmamxqevmiqoffsetremovalenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q offset before the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetIQOffsetRemovalEnabled(string selectorString, RFmxWcdmaMXQevmIQOffsetRemovalEnabled value)RemarksThis method sets the value of QevmIQOffsetRemovalEnabled attribute.The de

### SetIQOffsetRemovalEnabled(string, RFmxWcdmaMXQevmIQOffsetRemovalEnabled)

Sets whether to remove the I/Q offset before the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetIQOffsetRemovalEnabled(string selectorString, RFmxWcdmaMXQevmIQOffsetRemovalEnabled value)

#### Remarks

This method sets the value of [QevmIQOffsetRemovalEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmiqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXQevmIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00148: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the QPSK EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of QevmMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorS

### SetMeasurementEnabled(string, bool)

Sets whether to enable the QPSK EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [QevmMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the QPSK EVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00149: SetMeasurementLength(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the QEVM measurement. This value is expressed in chips. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of QevmMeasurementLength attribute.The default value is 2560. NI recommends

### SetMeasurementLength(string, int)

Sets the duration of the QEVM measurement. This value is expressed in chips.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [QevmMeasurementLength](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 2560. NI recommends that you set this property to n * 512, where the value of n can range from 1 to 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the QEVM measurement. This value is expressed in chips. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00150: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of QevmNumberOfAnalysisThreads attribute.The number of threads c

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [QevmNumberOfAnalysisThreads](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setrrcfilterenabled__string-rfmxwcdmamxqevmrrcfilterenabled.html language=enus -->
## TOPIC 00151: SetRrcFilterEnabled(string, RFmxWcdmaMXQevmRrcFilterEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setrrcfilterenabled__string-rfmxwcdmamxqevmrrcfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setrrcfilterenabled__string-rfmxwcdmamxqevmrrcfilterenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRrcFilterEnabled(string selectorString, RFmxWcdmaMXQevmRrcFilterEnabled value)RemarksThis method sets the value

### SetRrcFilterEnabled(string, RFmxWcdmaMXQevmRrcFilterEnabled)

Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRrcFilterEnabled(string selectorString, RFmxWcdmaMXQevmRrcFilterEnabled value)

#### Remarks

This method sets the value of [QevmRrcFilterEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmrrcfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXQevmRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-fetchevm__string-double-out-out-out-out-out-out.html language=enus -->
## TOPIC 00152: FetchEvm(string, double, out double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-fetchevm__string-double-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-fetchevm__string-double-out-out-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchEvm(string selectorString, double

### FetchEvm(string, double, out double, out double, out double, out double, out double, out double)

Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchEvm(string selectorString, double timeout, out double meanRmsEvm, out double maximumPeakEvm, out double meanFrequencyError, out double meanMagnitudeError, out double meanPhaseError, out double meanChipRateError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsEvm | out double | Upon return, contains the mean of the RMS EVM values for a QPSK signal. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. This value is expressed as a percentage. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. |
| maximumPeakEvm | out double | Upon return, contains the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. |
| meanFrequencyError | out double | Upon return, contains the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. |
| meanMagnitudeError | out double | Upon return, contains the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |
| meanPhaseError | out double | Upon return, contains the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. |
| meanChipRateError | out double | Upon return, contains the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-fetchevmtrace__string-double-ref.html language=enus -->
## TOPIC 00153: FetchEvmTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-fetchevmtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-fetchevmtrace__string-double-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace for the QEVM measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name.

### FetchEvmTrace(string, double, ref AnalogWaveform< float >)

Fetches the EVM trace for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| evm | ref AnalogWaveform< float > | Upon return, contains the trace of error vector magnitude of the QPSK corrected signal for the last acquisition. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximumiqoriginoffset__string-out.html language=enus -->
## TOPIC 00154: GetMaximumIQOriginOffset(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximumiqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximumiqoriginoffset__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of the I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The I/Q Origin Offset is the amount of DC componen

### GetMaximumIQOriginOffset(string, out double)

Gets the maximum value of the I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method.The I/Q Origin Offset is the amount of DC component present in the I/Q signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMaximumIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumIQOriginOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum value of the I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The I/Q Origin Offset is the amount of DC component present in the I/Q signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximummagnitudeerror__string-out.html language=enus -->
## TOPIC 00155: GetMaximumMagnitudeError(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximummagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximummagnitudeerror__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The magnitude error of a chip is the

### GetMaximumMagnitudeError(string, out double)

Gets the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMaximumMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumMagnitudeError](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximumpeakevm__string-out.html language=enus -->
## TOPIC 00156: GetMaximumPeakEvm(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximumpeakevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmaximumpeakevm__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The EVM of a chip is the magnitude of the vecto

### GetMaximumPeakEvm(string, out double)

Gets the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMaximumPeakEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumPeakEvm](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanfrequencyerror__string-out.html language=enus -->
## TOPIC 00157: GetMeanFrequencyError(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanfrequencyerror__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The frequency err

### GetMeanFrequencyError(string, out double)

Gets the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeanFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanFrequencyError](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeaniqoriginoffset__string-out.html language=enus -->
## TOPIC 00158: GetMeanIQOriginOffset(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeaniqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeaniqoriginoffset__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The I/Q origin offset is

### GetMeanIQOriginOffset(string, out double)

Gets the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method.The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeanIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanIQOriginOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB.This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanmagnitudeerror__string-out.html language=enus -->
## TOPIC 00159: GetMeanMagnitudeError(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanmagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanmagnitudeerror__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The magnitu

### GetMeanMagnitudeError(string, out double)

Gets the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeanMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanMagnitudeError](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanphaseerror__string-out.html language=enus -->
## TOPIC 00160: GetMeanPhaseError(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmresults-getmeanphaseerror__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method.

### GetMeanPhaseError(string, out double)

Gets the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the [SetAveragingCount(string, int)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmconfiguration-setaveragingcount__string-int.html) method. The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeanPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanPhaseError](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage.This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the SetAveragingCount(string, int) method. The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXQevmResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmspectruminverted.html language=enus -->
## TOPIC 00161: RFmxWcdmaMXQevmSpectrumInverted Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxqevmspectruminverted.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXQevmSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxWcdmaMXQevmSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXQevmSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem-configuration.html language=enus -->
## TOPIC 00162: Configuration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem-configuration.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXSemConfiguration instance that provides methods to configure the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXSemConfiguration Configuration { get; }

### Configuration

Gets the [RFmxWcdmaMXSemConfiguration](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration.html) instance that provides methods to configure the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXSemConfiguration](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration.html) Configuration { get; }

Parent topic:

RFmxWcdmaMXSem Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem-results.html language=enus -->
## TOPIC 00163: Results

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem-results.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxWcdmaMXSemResults instance that provides methods to fetch and read the SEM measurement results. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic RFmxWcdmaMXSemResults Results { get; }

### Results

Gets the [RFmxWcdmaMXSemResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults.html) instance that provides methods to fetch and read the SEM measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public [RFmxWcdmaMXSemResults](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults.html) Results { get; }

Parent topic:

RFmxWcdmaMXSem Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem.html language=enus -->
## TOPIC 00164: RFmxWcdmaMXSem Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsem.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SEM measurement. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXSem : RFmxWcdmaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxWcdmaMXSemConfiguration instance that provides methods to configure the SEM measuremen

### RFmxWcdmaMXSem Class

Represents the SEM measurement.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXSem : RFmxWcdmaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxWcdmaMXSemConfiguration instance that provides methods to configure the SEM measurement. |
| Results | Gets the RFmxWcdmaMXSemResults instance that provides methods to fetch and read the SEM measurement results. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemamplitudecorrectiontype.html language=enus -->
## TOPIC 00165: RFmxWcdmaMXSemAmplitudeCorrectionType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemamplitudecorrectiontype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: National

### RFmxWcdmaMXSemAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXSemAmplitudeCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemaveragingtype.html language=enus -->
## TOPIC 00166: RFmxWcdmaMXSemAveragingType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemaveragingtype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXSemAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor

### RFmxWcdmaMXSemAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXSemAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-configureaveraging__string-rfmxwcdmamxsemaveragingenabled-int-rfmxwcdmamxsemaveragingtype.html language=enus -->
## TOPIC 00167: ConfigureAveraging(string, RFmxWcdmaMXSemAveragingEnabled, int, RFmxWcdmaMXSemAveragingType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-configureaveraging__string-rfmxwcdmamxsemaveragingenabled-int-rfmxwcdmamxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-configureaveraging__string-rfmxwcdmamxsemaveragingenabled-int-rfmxwcdmamxsemaveragingtype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureAveraging(string selectorString, RFmxWcdmaMXSemAveragingEnabled averagingEnabled, int averagingCount, RFmxWcdmaMXSemAveragingType averagingType)ParametersNameTypeDescriptionselectorStrin

### ConfigureAveraging(string, RFmxWcdmaMXSemAveragingEnabled, int, RFmxWcdmaMXSemAveragingType)

Configures averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureAveraging(string selectorString, RFmxWcdmaMXSemAveragingEnabled averagingEnabled, int averagingCount, RFmxWcdmaMXSemAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxWcdmaMXSemAveragingEnabled | Specifies whether to enable averaging of the spectrum for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxWcdmaMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-configuresweeptime__string-rfmxwcdmamxsemsweeptimeauto-double.html language=enus -->
## TOPIC 00168: ConfigureSweepTime(string, RFmxWcdmaMXSemSweepTimeAuto, double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-configuresweeptime__string-rfmxwcdmamxsemsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-configuresweeptime__string-rfmxwcdmamxsemsweeptimeauto-double.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureSweepTime(string selectorString, RFmxWcdmaMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is

### ConfigureSweepTime(string, RFmxWcdmaMXSemSweepTimeAuto, double)

Configures the sweep time interval.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureSweepTime(string selectorString, RFmxWcdmaMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxWcdmaMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00169: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SemAllTracesEnabled attribute.The default valu

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SemAllTracesEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00170: GetAmplitudeCorrectionType(string, out RFmxWcdmaMXSemAmplitudeCorrectionType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: NationalInstr

### GetAmplitudeCorrectionType(string, out RFmxWcdmaMXSemAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxWcdmaMXSemAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [SemAmplitudeCorrectionType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXSemAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00171: GetAveragingCount(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXSemAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of SemA

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxWcdmaMXSemAveragingEnabled)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setaveragingenabled__string-rfmxwcdmamxsemaveragingenabled.html) method to [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [SemAveragingCount](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxWcdmaMXSemAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00172: GetAveragingEnabled(string, out RFmxWcdmaMXSemAveragingEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAveragingEnabled(string selectorString, out RFmxWcdmaMXSemAveragingEnabled value)RemarksThis method gets the value of SemAveragingEnabled attribute.The default value is False.Para

### GetAveragingEnabled(string, out RFmxWcdmaMXSemAveragingEnabled)

Gets whether to enable averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAveragingEnabled(string selectorString, out RFmxWcdmaMXSemAveragingEnabled value)

#### Remarks

This method gets the value of [SemAveragingEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXSemAveragingEnabled | Upon return, contains whether to enable averaging for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00173: GetAveragingType(string, out RFmxWcdmaMXSemAveragingType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAveragingType(string selectorString, out RFmxWcdmaMXSemAveragingType value)RemarksThis method gets the value of SemAveragingType attribute.The default value is Rms.Par

### GetAveragingType(string, out RFmxWcdmaMXSemAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAveragingType(string selectorString, out RFmxWcdmaMXSemAveragingType value)

#### Remarks

This method gets the value of [SemAveragingType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXSemAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00174: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of SemCarrierIntegrati

### GetCarrierIntegrationBandwidth(string, out double)

Gets the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [SemCarrierIntegrationBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00175: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SemMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStr

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SemMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00176: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of SemNumberOfAnalysisThreads attribute.The default value is

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [SemNumberOfAnalysisThreads](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getnumberofoffsets__string-out.html language=enus -->
## TOPIC 00177: GetNumberOfOffsets(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getnumberofoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getnumberofoffsets__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of offset segments. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetNumberOfOffsets(string selectorString, out int value)RemarksThis method gets the value of SemNumberOfOffsets attribute.ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal

### GetNumberOfOffsets(string, out int)

Gets the number of offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetNumberOfOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [SemNumberOfOffsets](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of offset segments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetbandwidthintegral__string-out.html language=enus -->
## TOPIC 00178: GetOffsetBandwidthIntegral(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetbandwidthintegral__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetbandwidthintegral__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetOffsetBandwidthIntegral(string selectorString, out int value)RemarksThis method gets the value of SemOffsetBandwidthIntegral attr

### GetOffsetBandwidthIntegral(string, out int)

Gets the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetOffsetBandwidthIntegral(string selectorString, out int value)

#### Remarks

This method gets the value of [SemOffsetBandwidthIntegral](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.If this property returns a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00179: GetOffsetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetrbwfilterbandwidth__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetOffsetRbwFilterBandwidth(string selectorString, out double value)RemarksThis method gets the value of SemOffsetRbwFilterBandwi

### GetOffsetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetOffsetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetRbwFilterBandwidth](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetrbwfiltertype__string-out.html language=enus -->
## TOPIC 00180: GetOffsetRbwFilterType(string, out RFmxWcdmaMXSemOffsetRbwFilterType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetrbwfiltertype__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetOffsetRbwFilterType(string selectorString, out RFmxWcdmaMXSemOffsetRbwFilterType value)RemarksThis method gets the value of SemOffsetRbwFilterType attribute.ParametersNameTypeDescriptionselectorS

### GetOffsetRbwFilterType(string, out RFmxWcdmaMXSemOffsetRbwFilterType)

Gets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetOffsetRbwFilterType(string selectorString, out RFmxWcdmaMXSemOffsetRbwFilterType value)

#### Remarks

This method gets the value of [SemOffsetRbwFilterType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxWcdmaMXSemOffsetRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetstartfrequency__string-out.html language=enus -->
## TOPIC 00181: GetOffsetStartFrequency(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetstartfrequency__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetOffsetStartFrequency(string selectorString, out double value)RemarksThis method gets the value of SemOffset

### GetOffsetStartFrequency(string, out double)

Gets the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetOffsetStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetStartFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetstopfrequency__string-out.html language=enus -->
## TOPIC 00182: GetOffsetStopFrequency(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getoffsetstopfrequency__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetOffsetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of SemOffsetSt

### GetOffsetStopFrequency(string, out double)

Gets the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetOffsetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetStopFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00183: GetSweepTimeAuto(string, out RFmxWcdmaMXSemSweepTimeAuto)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetSweepTimeAuto(string selectorString, out RFmxWcdmaMXSemSweepTimeAuto value)RemarksThis method gets the value of SemSweepTimeAuto attribute.The default value is True.ParametersNameType

### GetSweepTimeAuto(string, out RFmxWcdmaMXSemSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxWcdmaMXSemSweepTimeAuto value)

#### Remarks

This method gets the value of [SemSweepTimeAuto](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXSemSweepTimeAuto | Upon return, contains whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00184: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXSemSweepTimeAuto) method to False.This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method gets the value of

### GetSweepTimeInterval(string, out double)

Gets the sweep time when you set the [SetSweepTimeAuto(string, RFmxWcdmaMXSemSweepTimeAuto)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setsweeptimeauto__string-rfmxwcdmamxsemsweeptimeauto.html) method to [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemsweeptimeauto.html).This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [SemSweepTimeInterval](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 666.66666700000007 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time when you set the SetSweepTimeAuto(string, RFmxWcdmaMXSemSweepTimeAuto) method to False.This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00185: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SemAllTracesEnabled attribute.The default value is

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SemAllTracesEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxsemamplitudecorrectiontype.html language=enus -->
## TOPIC 00186: SetAmplitudeCorrectionType(string, RFmxWcdmaMXSemAmplitudeCorrectionType)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxsemamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemconfiguration-setamplitudecorrectiontype__string-rfmxwcdmamxsemamplitudecorrectiontype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. SyntaxNamespace: NationalInstr

### SetAmplitudeCorrectionType(string, RFmxWcdmaMXSemAmplitudeCorrectionType)

Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxWcdmaMXSemAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [SemAmplitudeCorrectionType](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXSemAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00187: FetchLowerOffsetMarginArray(string, double, ref RFmxWcdmaMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total ca

### FetchLowerOffsetMarginArray(string, double, ref RFmxWcdmaMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchLowerOffsetMarginArray(string selectorString, double timeout, ref RFmxWcdmaMXSemLowerOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxWcdmaMXSemLowerOffsetMeasurementStatus[] | Indicates an array of measurement status values based on the values of the SEM Results Lower Offset Margin method corresponding to each lower offset segment. |
| margin | ref double[] | Upon return, contains an array of margins of the lower offset segments. This value is expressed in dB. |
| marginFrequency | ref double[] | Upon return, contains an array of frequencies at which the margins occurred in the lower, or negative, offset segments This value is expressed in Hz. |
| marginAbsolutePower | ref double[] | Upon return, contains an array of powers at which the margins occurred in the lower, or negative, offset segment. |
| marginRelativePower | ref double[] | Upon return, contains an array of powers at which the margins occurred in the lower, or negative, offset segments relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00188: FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power. Use "offset(n)" as the selector string to read result

### FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power. 
 Use "offset(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchLowerOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. Example: "offset0" "result::r1/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the power measured in the lower, or negative, offset segment. This value is expressed in dBm. |
| relativeIntegratedPower | out double | Upon return, contains the power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method. |
| absolutePeakPower | out double | Upon return, contains the peak power measured in the lower, or negative, offset segment. This value is expressed in dBm. |
| peakFrequency | out double | Upon return, contains the frequency corresponding to the lower offset segment peak power. This value is expressed in Hz. |
| relativePeakPower | out double | Upon return, contains the peak power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchmeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00189: FetchMeasurementStatus(string, double, out RFmxWcdmaMXSemMeasurementStatus)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchmeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchmeasurementstatus__string-double-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the 3GPP TS 34.121-1 specification, version 11.5.0, release 11. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic

### FetchMeasurementStatus(string, double, out RFmxWcdmaMXSemMeasurementStatus)

Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the *3GPP TS 34.121-1* specification, version 11.5.0, release 11.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchMeasurementStatus(string selectorString, double timeout, out RFmxWcdmaMXSemMeasurementStatus measurementStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxWcdmaMXSemMeasurementStatus | Indicates the overall SEM measurement status based on the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetUpperOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemUpperOffsetMeasurementStatus@) methods. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00190: FetchUpperOffsetMarginArray(string, double, ref RFmxWcdmaMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relati

### FetchUpperOffsetMarginArray(string, double, ref RFmxWcdmaMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxWcdmaMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxWcdmaMXSemUpperOffsetMeasurementStatus[] | Upon return, contains an array of measurement status values based on the values of the GetUpperOffsetMargin(string, out double) method corresponding to each upper offset segment. |
| margin | ref double[] | Upon return, contains an array of margins of the upper offset segments. |
| marginFrequency | ref double[] | Upon return, contains an array of frequencies corresponding to the SEM Results Upper Offset Margin method. This value is expressed in Hz. |
| marginAbsolutePower | ref double[] | Upon return, contains an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin method. This value is expressed in dBm. |
| marginRelativePower | ref double[] | Upon return, contains an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin method, relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00191: FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power. Use "offset(n)" as the selector string to read results

### FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power. 
 Use "offset(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchUpperOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. Example: "offset0" "result::r1/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the power measured in the upper, or positive, offset segment. This value is expressed in dBm. |
| relativeIntegratedPower | out double | Upon return, contains the power measured in the upper, or positive, offset segment relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |
| absolutePeakPower | out double | Upon return, contains an array of peak power values measured in the lower, or negative, offset segments This value is expressed in dBm. |
| peakFrequency | out double | Upon return, contains the frequency corresponding to the upper offset segment peak power. This value is expressed in Hz. |
| relativePeakPower | out double | Upon return, contains the peak power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00192: FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. A

### FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchUpperOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref double[] peakFrequency, ref double[] relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | ref double[] | Upon return, contains an array of the powers measured in the upper, or positive, offset segments. This value is expressed in dBm. |
| relativeIntegratedPower | ref double[] | Upon return, contains an array of powers measured in the upper, or positive, offset segments relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |
| absolutePeakPower | ref double[] | Upon return, contains an array of peak power values measured in the upper, or positive, offset segments. This value is expressed in dBm. |
| peakFrequency | ref double[] | Upon return, contains an array of frequencies at which the peak power is observed in the upper, or positive, offset segments. This value is expressed in Hz. |
| relativePeakPower | ref double[] | Upon return, contains an array of peak power values measured in the upper, or positive, offset segments relative to the SEM Results Total Carrier Pwr method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00193: GetCarrierAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierabsoluteintegratedpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier power. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetCarrierAbsoluteIntegratedPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsCarrierAbsoluteIntegratedPower attribute.ParametersNameTypeDesc

### GetCarrierAbsoluteIntegratedPower(string, out double)

Gets the carrier power. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetCarrierAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierAbsoluteIntegratedPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00194: GetCarrierAbsolutePeakPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierabsolutepeakpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power in the carrier channel.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetCarrierAbsolutePeakPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsCarrierAbsolutePeakPower attribute.ParametersNameT

### GetCarrierAbsolutePeakPower(string, out double)

Gets the peak power in the carrier channel.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetCarrierAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierAbsolutePeakPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power in the carrier channel.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierpeakfrequency__string-out.html language=enus -->
## TOPIC 00195: GetCarrierPeakFrequency(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierpeakfrequency__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power is observed in the carrier channel.This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetCarrierPeakFrequency(string selectorString, out double value)RemarksThis method gets the value of SemResultsCarrierPeakFrequency

### GetCarrierPeakFrequency(string, out double)

Gets the frequency at which the peak power is observed in the carrier channel.This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetCarrierPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierPeakFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power is observed in the carrier channel.This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00196: GetCarrierRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getcarrierrelativeintegratedpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetCarrierRelativeIntegratedPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsCarrierR

### GetCarrierRelativeIntegratedPower(string, out double)

Gets the carrier power relative to the [GetTotalCarrierPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html).This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetCarrierRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierRelativeIntegratedPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00197: GetLowerOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the lower, or negative, offset segment.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsLowerOffsetAbsolu

### GetLowerOffsetAbsoluteIntegratedPower(string, out double)

Gets the power measured in the lower, or negative, offset segment.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the lower, or negative, offset segment.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00198: GetLowerOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetabsolutepeakpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetAbsolutePeakPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsLowerOffsetAbsolut

### GetLowerOffsetAbsolutePeakPower(string, out double)

Gets the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsolutePeakPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html language=enus -->
## TOPIC 00199: GetLowerOffsetMargin(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin of the lower offset segment.This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetMargin(string selectorString, out double value)RemarksThis method gets the value of SemResultsLowerOffsetMargin attribute.ParametersNameTypeDescription

### GetLowerOffsetMargin(string, out double)

Gets the margin of the lower offset segment.This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMargin](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the margin of the lower offset segment.This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00200: GetLowerOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginabsolutepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetMarginAbsolutePower(string selectorString, out double value)RemarksThis method gets the value

### GetLowerOffsetMarginAbsolutePower(string, out double)

Gets the power at the frequency corresponding to the [GetLowerOffsetMargin(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html) method.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginAbsolutePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginfrequency__string-out.html language=enus -->
## TOPIC 00201: GetLowerOffsetMarginFrequency(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginfrequency__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetMarginFrequency(string selectorString, out double value)RemarksThis method gets the value of SemResultsLowe

### GetLowerOffsetMarginFrequency(string, out double)

Gets the frequency corresponding to the [GetLowerOffsetMargin(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html) method.This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetMarginFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00202: GetLowerOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmarginrelativepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at the frequency corresponding to the value of the GetLowerOffsetMargin(string, out double) method and relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetMarginRelati

### GetLowerOffsetMarginRelativePower(string, out double)

Gets the power at the frequency corresponding to the value of the [GetLowerOffsetMargin(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html) method and relative to the [GetTotalCarrierPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html) method. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginRelativePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at the frequency corresponding to the value of the GetLowerOffsetMargin(string, out double) method and relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00203: GetLowerOffsetMeasurementStatus(string, out RFmxWcdmaMXSemLowerOffsetMeasurementStatus)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmeasurementstatus__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status based on the GetLowerOffsetMargin(string, out double) method. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxWcdmaMXSemLowerOffsetMeasurementStatus value)RemarksThis method gets the value of

### GetLowerOffsetMeasurementStatus(string, out RFmxWcdmaMXSemLowerOffsetMeasurementStatus)

Indicates the measurement status based on the [GetLowerOffsetMargin(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetmargin__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxWcdmaMXSemLowerOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMeasurementStatus](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxWcdmaMXSemLowerOffsetMeasurementStatus | Indicates the measurement status based on the GetLowerOffsetMargin(string, out double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00204: GetLowerOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetpeakfrequency__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power is observed in the lower offset segment.This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetPeakFrequency(string selectorString, out double value)RemarksThis method gets the value of SemResultsLowerOffset

### GetLowerOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power is observed in the lower offset segment.This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetPeakFrequency](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power is observed in the lower offset segment.This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00205: GetLowerOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetRelativeIntegratedPower(string selectorString, out double value)R

### GetLowerOffsetRelativeIntegratedPower(string, out double)

Gets the power measured in the lower, or negative, offset segment relative to the [GetTotalCarrierPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html) method.This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativeIntegratedPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00206: GetLowerOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getloweroffsetrelativepeakpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetLowerOffsetRelativePeakPower(string selectorString, out double value)Re

### GetLowerOffsetRelativePeakPower(string, out double)

Gets the peak power measured in the lower, or negative, offset segment relative to the [GetTotalCarrierPower(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html) method.This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetLowerOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativePeakPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getmeasurementstatus__string-out.html language=enus -->
## TOPIC 00207: GetMeasurementStatus(string, out RFmxWcdmaMXSemMeasurementStatus)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getmeasurementstatus__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall SEM measurement status, based on the value of the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemR

### GetMeasurementStatus(string, out RFmxWcdmaMXSemMeasurementStatus)

Indicates the overall SEM measurement status, based on the value of the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetUpperOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemUpperOffsetMeasurementStatus@) properties.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementStatus(string selectorString, out RFmxWcdmaMXSemMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsMeasurementStatus](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxWcdmaMXSemMeasurementStatus | Indicates the overall SEM measurement status, based on the value of the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetUpperOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemUpperOffsetMeasurementStatus@) properties. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html language=enus -->
## TOPIC 00208: GetTotalCarrierPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-gettotalcarrierpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RF

### GetTotalCarrierPower(string, out double)

Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetTotalCarrierPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsTotalCarrierPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00209: GetUpperOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the upper, or positive, offset segment.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsUpperOffsetAbsolu

### GetUpperOffsetAbsoluteIntegratedPower(string, out double)

Gets the power measured in the upper, or positive, offset segment.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the upper, or positive, offset segment.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00210: GetUpperOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetabsolutepeakpower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUpperOffsetAbsolutePeakPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsUpperOffsetAbsolut

### GetUpperOffsetAbsolutePeakPower(string, out double)

Gets the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUpperOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsolutePeakPower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00211: GetUpperOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetmarginabsolutepower__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at the frequency corresponding to the GetUpperOffsetMargin(string, out double) method.This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetUpperOffsetMarginAbsolutePower(string selectorString, out double value)RemarksThis method gets the value

### GetUpperOffsetMarginAbsolutePower(string, out double)

Gets the power at the frequency corresponding to the [GetUpperOffsetMargin(string, out double)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults-getupperoffsetmargin__string-out.html) method.This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetUpperOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginAbsolutePower](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at the frequency corresponding to the GetUpperOffsetMargin(string, out double) method.This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSemResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults.html language=enus -->
## TOPIC 00212: RFmxWcdmaMXSemResults Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsemresults.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SEM measurement results. Derives fromRFmxWcdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXSemResults : RFmxWcdmaMXSubObjectMethodsNameDescriptionFetchCarrierMeasurement(string, double, out double, out double)Fetches the a

### RFmxWcdmaMXSemResults Class

Provides methods to fetch and read the SEM measurement results.

#### Derives from

- RFmxWcdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXSemResults : RFmxWcdmaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchCarrierMeasurement(string, double, out double, out double) | Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power. Use "carrier(n)" as the selector string to read results from this method. |
| FetchCarrierMeasurementArray(string, double, ref double[], ref double[]) | Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power. |
| FetchLowerOffsetMargin(string, double, out RFmxWcdmaMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double) | Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. Use "offset(n)" as the selector string to read results from this method. |
| FetchLowerOffsetMarginArray(string, double, ref RFmxWcdmaMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double) | Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power. Use "offset(n)" as the selector string to read results from this method. |
| FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| FetchMeasurementStatus(string, double, out RFmxWcdmaMXSemMeasurementStatus) | Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the 3GPP TS 34.121-1 specification, version 11.5.0, release 11. |
| FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >) | Fetches the spectrum used for the SEM measurement. |
| FetchTotalCarrierPower(string, double, out double) | Fetches the total carrier power for the SEM measurement. |
| FetchUpperOffsetMargin(string, double, out RFmxWcdmaMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double) | Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power. Use "offset(n)" as the selector string to read results from this method. |
| FetchUpperOffsetMarginArray(string, double, ref RFmxWcdmaMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double) | Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power. Use "offset(n)" as the selector string to read results from this method. |
| FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power. |
| GetCarrierAbsoluteIntegratedPower(string, out double) | Gets the carrier power. This value is expressed in dBm. |
| GetCarrierAbsolutePeakPower(string, out double) | Gets the peak power in the carrier channel.This value is expressed in dBm. |
| GetCarrierPeakFrequency(string, out double) | Gets the frequency at which the peak power is observed in the carrier channel.This value is expressed in Hz. |
| GetCarrierRelativeIntegratedPower(string, out double) | Gets the carrier power relative to the GetTotalCarrierPower(string, out double).This value is expressed in dB. |
| GetLowerOffsetAbsoluteIntegratedPower(string, out double) | Gets the power measured in the lower, or negative, offset segment.This value is expressed in dBm. |
| GetLowerOffsetAbsolutePeakPower(string, out double) | Gets the peak power measured in the lower, or negative, offset segment.This value is expressed in dBm. |
| GetLowerOffsetMargin(string, out double) | Gets the margin of the lower offset segment.This value is expressed in dB. |
| GetLowerOffsetMarginAbsolutePower(string, out double) | Gets the power at the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in dBm. |
| GetLowerOffsetMarginFrequency(string, out double) | Gets the frequency corresponding to the GetLowerOffsetMargin(string, out double) method.This value is expressed in Hz. |
| GetLowerOffsetMarginRelativePower(string, out double) | Gets the power at the frequency corresponding to the value of the GetLowerOffsetMargin(string, out double) method and relative to the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |
| GetLowerOffsetMeasurementStatus(string, out RFmxWcdmaMXSemLowerOffsetMeasurementStatus) | Indicates the measurement status based on the GetLowerOffsetMargin(string, out double) method. |
| GetLowerOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power is observed in the lower offset segment.This value is expressed in Hz. |
| GetLowerOffsetRelativeIntegratedPower(string, out double) | Gets the power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| GetLowerOffsetRelativePeakPower(string, out double) | Gets the peak power measured in the lower, or negative, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| GetMeasurementStatus(string, out RFmxWcdmaMXSemMeasurementStatus) | Indicates the overall SEM measurement status, based on the value of the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetUpperOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemUpperOffsetMeasurementStatus@) properties. |
| GetTotalCarrierPower(string, out double) | Gets the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr method. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. |
| GetUpperOffsetAbsoluteIntegratedPower(string, out double) | Gets the power measured in the upper, or positive, offset segment.This value is expressed in dBm. |
| GetUpperOffsetAbsolutePeakPower(string, out double) | Gets the peak power measured in the upper, or positive, offset segment.This value is expressed in dBm. |
| GetUpperOffsetMargin(string, out double) | Gets the margin of the upper offset segment.This value is expressed in dB. |
| GetUpperOffsetMarginAbsolutePower(string, out double) | Gets the power at the frequency corresponding to the GetUpperOffsetMargin(string, out double) method.This value is expressed in dBm. |
| GetUpperOffsetMarginFrequency(string, out double) | Gets the frequency corresponding to the GetUpperOffsetMargin(string, out double) method. This value is expressed in Hz. |
| GetUpperOffsetMarginRelativePower(string, out double) | Gets the power at the frequency corresponding to the value of the GetUpperOffsetMargin(string, out double) method relative to the value of the GetTotalCarrierPower(string, out double) method. This value is expressed in dB. |
| GetUpperOffsetMeasurementStatus(string, out RFmxWcdmaMXSemUpperOffsetMeasurementStatus) | Indicates the measurement status based on the GetUpperOffsetMargin(string, out double) method. |
| GetUpperOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power is observed in the upper offset segment.This value is expressed in Hz. |
| GetUpperOffsetRelativeIntegratedPower(string, out double) | Gets the power measured in the upper, or positive, offset segment relative to the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |
| GetUpperOffsetRelativePeakPower(string, out double) | Gets the peak power measured in the upper, or positive, offset segment relative to the value of the GetTotalCarrierPower(string, out double) method.This value is expressed in dB. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxwcdmamxslotphasesynchronizationmode-int-int.html language=enus -->
## TOPIC 00213: ConfigureSynchronizationModeAndInterval(string, RFmxWcdmaMXSlotPhaseSynchronizationMode, int, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxwcdmamxslotphasesynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-configuresynchronizationmodeandinterval__string-rfmxwcdmamxslotphasesynchronizationmode-int-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxWcdmaMXSlotPhaseSynchronizationMode synchronizationMode,

### ConfigureSynchronizationModeAndInterval(string, RFmxWcdmaMXSlotPhaseSynchronizationMode, int, int)

Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxWcdmaMXSlotPhaseSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxWcdmaMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the synchronizationMode parameter. |
| measurementLength | int | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00214: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseAllTracesEnabled attribute.The

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseAllTracesEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00215: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SlotPhaseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptio

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SlotPhase measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementlength__string-out.html language=enus -->
## TOPIC 00216: GetMeasurementLength(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementlength__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMeasurementLength(string selectorString, out int value)RemarksThis method gets the value of SlotPhaseMeasurementLength attribute.The default value is 15. T

### GetMeasurementLength(string, out int)

Gets the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementLength(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 15. The valid values are any value greater than or equal to 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00217: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetMea

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setsynchronizationmode__string-rfmxwcdmamxslotphasesynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0. The valid values are any value greater than or equal to 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getrrcfilterenabled__string-out.html language=enus -->
## TOPIC 00218: GetRrcFilterEnabled(string, out RFmxWcdmaMXSlotPhaseRrcFilterEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getrrcfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getrrcfilterenabled__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetRrcFilterEnabled(string selectorString, out RFmxWcdmaMXSlotPhaseRrcFilterEnabled value)RemarksThis method gets t

### GetRrcFilterEnabled(string, out RFmxWcdmaMXSlotPhaseRrcFilterEnabled)

Gets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetRrcFilterEnabled(string selectorString, out RFmxWcdmaMXSlotPhaseRrcFilterEnabled value)

#### Remarks

This method gets the value of [SlotPhaseRrcFilterEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaserrcfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXSlotPhaseRrcFilterEnabled | Upon return, contains whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00219: GetSpectrumInverted(string, out RFmxWcdmaMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetSpectrumInverted(string selectorString, out RFmxWcdmaMXSlotPhaseSpectrumInverted value)RemarksThis method gets the value of SlotPhaseSpectrumInverted attribute.The default value is False.Para

### GetSpectrumInverted(string, out RFmxWcdmaMXSlotPhaseSpectrumInverted)

Gets whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetSpectrumInverted(string selectorString, out RFmxWcdmaMXSlotPhaseSpectrumInverted value)

#### Remarks

This method gets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxWcdmaMXSlotPhaseSpectrumInverted | Upon return, contains whether the signal spectrum is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setmeasurementlength__string-int.html language=enus -->
## TOPIC 00220: SetMeasurementLength(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setmeasurementlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setmeasurementlength__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration of the SlotPhase measurement. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMeasurementLength(string selectorString, int value)RemarksThis method sets the value of SlotPhaseMeasurementLength attribute.The default value is 15. The v

### SetMeasurementLength(string, int)

Sets the duration of the SlotPhase measurement. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementLength(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementLength](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 15. The valid values are any value greater than or equal to 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00221: SetMeasurementOffset(string, int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode) method. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetMea

### SetMeasurementOffset(string, int)

Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setsynchronizationmode__string-rfmxwcdmamxslotphasesynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SlotPhaseMeasurementOffset](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is 0. The valid values are any value greater than or equal to 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxWcdmaMXSlotPhaseSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setrrcfilterenabled__string-rfmxwcdmamxslotphaserrcfilterenabled.html language=enus -->
## TOPIC 00222: SetRrcFilterEnabled(string, RFmxWcdmaMXSlotPhaseRrcFilterEnabled)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setrrcfilterenabled__string-rfmxwcdmamxslotphaserrcfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setrrcfilterenabled__string-rfmxwcdmamxslotphaserrcfilterenabled.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetRrcFilterEnabled(string selectorString, RFmxWcdmaMXSlotPhaseRrcFilterEnabled value)RemarksThis method sets the v

### SetRrcFilterEnabled(string, RFmxWcdmaMXSlotPhaseRrcFilterEnabled)

Sets whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetRrcFilterEnabled(string selectorString, RFmxWcdmaMXSlotPhaseRrcFilterEnabled value)

#### Remarks

This method sets the value of [SlotPhaseRrcFilterEnabled](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaserrcfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXSlotPhaseRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setspectruminverted__string-rfmxwcdmamxslotphasespectruminverted.html language=enus -->
## TOPIC 00223: SetSpectrumInverted(string, RFmxWcdmaMXSlotPhaseSpectrumInverted)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setspectruminverted__string-rfmxwcdmamxslotphasespectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseconfiguration-setspectruminverted__string-rfmxwcdmamxslotphasespectruminverted.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the signal spectrum is inverted. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int SetSpectrumInverted(string selectorString, RFmxWcdmaMXSlotPhaseSpectrumInverted value)RemarksThis method sets the value of SlotPhaseSpectrumInverted attribute.The default value is False.Paramete

### SetSpectrumInverted(string, RFmxWcdmaMXSlotPhaseSpectrumInverted)

Sets whether the signal spectrum is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int SetSpectrumInverted(string selectorString, RFmxWcdmaMXSlotPhaseSpectrumInverted value)

#### Remarks

This method sets the value of [SlotPhaseSpectrumInverted](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphasespectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxWcdmaMXSlotPhaseSpectrumInverted | Specifies whether the signal spectrum is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseConfiguration Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html language=enus -->
## TOPIC 00224: FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchchipphaseerrorlinearfittrace__string-double-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error linear fit trace for the SlotPhase measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchChipPhaseErrorLinearFitTrace(string selectorString, double timeout, ref AnalogWaveform< float > chipPhaseErrorLinearFit)ParametersNameTypeDescriptionselectorSt

### FetchChipPhaseErrorLinearFitTrace(string, double, ref AnalogWaveform< float >)

Fetches the chip phase error linear fit trace for the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchChipPhaseErrorLinearFitTrace(string selectorString, double timeout, ref AnalogWaveform< float > chipPhaseErrorLinearFit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| chipPhaseErrorLinearFit | ref AnalogWaveform< float > | Upon return, contains the linear-fit of the chip phase error after excluding 25 micro seconds at the start and end of each slot. The linear-fit is then extrapolated to the nearest slot boundaries on either side. The exclusion and extrapolation can be disabled if you set the SetTransientRemovalEnabled(string, RFmxWcdmaMXSlotPhaseTransientRemovalEnabled) method to False. This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling method and the RfmxInstr Frequency Settling Units method, to allow more time for the LO to settle. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchmeasurement__string-double-out-out-out-out.html language=enus -->
## TOPIC 00225: FetchMeasurement(string, double, out double, out int, out int, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchmeasurement__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchmeasurement__string-double-out-out-out-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchMeasurement(string selectorString, double timeout, out double maxim

### FetchMeasurement(string, double, out double, out int, out int, out int)

Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchMeasurement(string selectorString, double timeout, out double maximumPhaseDiscontinuity, out int discontinuityCountGreaterThanLimit1, out int discontinuityCountGreaterThanLimit2, out int discontinuityMinimumDistance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| maximumPhaseDiscontinuity | out double | Upon return, contains the maximum of all the measured phase discontinuity values at the slot boundaries. This value is expressed in degrees. |
| discontinuityCountGreaterThanLimit1 | out int | Upon return, contains the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |
| discontinuityCountGreaterThanLimit2 | out int | Upon return, contains the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |
| discontinuityMinimumDistance | out int | Upon return, contains the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. If there are no phase discontinuity values greater than Limit 1, or if there is only one phase discontinuity value greater than Limit 1, this result is not valid. In such a case, -1 is reported as the result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchphasediscontinuities__string-double-ref.html language=enus -->
## TOPIC 00226: FetchPhaseDiscontinuities(string, double, ref double[])

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchphasediscontinuities__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-fetchphasediscontinuities__string-double-ref.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity values for the slot phase measurement.SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] slotPhaseDiscontinuity)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector

### FetchPhaseDiscontinuities(string, double, ref double[])

Fetches the phase discontinuity values for the slot phase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int FetchPhaseDiscontinuities(string selectorString, double timeout, ref double[] slotPhaseDiscontinuity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| slotPhaseDiscontinuity | ref double[] | Upon return, contains the difference between the first extrapolated linear chip phase of the current slot and the last extrapolated linear chip phase of the preceding slot. The extrapolation is for the exclusion period of 25us on either side of the slot boundary. If you set the SetTransientRemovalEnabled(string, RFmxWcdmaMXSlotPhaseTransientRemovalEnabled) method to False, this parameter returns the difference between the first and last linear chip phase, at each slot boundary. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuitycountgreaterthanlimit1__string-out.html language=enus -->
## TOPIC 00227: GetDiscontinuityCountGreaterThanLimit1(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuitycountgreaterthanlimit1__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuitycountgreaterthanlimit1__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetDiscontinuityCountGreaterThanLimit1(string selectorString, out int value)RemarksThis method gets th

### GetDiscontinuityCountGreaterThanLimit1(string, out int)

Gets the number of times the phase discontinuity values exceed the *Limit 1* value for the acquired signal. *Limit 1* is fixed at 36 degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetDiscontinuityCountGreaterThanLimit1(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseResultsDiscontinuityCountGreaterThanLimit1](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuitycountgreaterthanlimit2__string-out.html language=enus -->
## TOPIC 00228: GetDiscontinuityCountGreaterThanLimit2(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuitycountgreaterthanlimit2__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuitycountgreaterthanlimit2__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetDiscontinuityCountGreaterThanLimit2(string selectorString, out int value)RemarksThis method gets th

### GetDiscontinuityCountGreaterThanLimit2(string, out int)

Gets the number of times the phase discontinuity values exceed the *Limit 2* value for the acquired signal. *Limit 2* is fixed at 66 degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetDiscontinuityCountGreaterThanLimit2(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseResultsDiscontinuityCountGreaterThanLimit2](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuityminimumdistance__string-out.html language=enus -->
## TOPIC 00229: GetDiscontinuityMinimumDistance(string, out int)

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuityminimumdistance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphaseresults-getdiscontinuityminimumdistance__string-out.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic int GetDiscontinuityMinimumDistance(string selectorString, out int value)Remar

### GetDiscontinuityMinimumDistance(string, out int)

Gets the minimum distance between two phase discontinuity measurements exceeding the *Limit 1* value. *Limit 1* is fixed at 36 degrees. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public int GetDiscontinuityMinimumDistance(string selectorString, out int value)

#### Remarks

This method gets the value of [SlotPhaseResultsDiscontinuityMinimumDistance](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxpropertyid.html) attribute.If there are no phase discontinuity values greater than Limit 1, or if there is only one phase discontinuity value greater than Limit 1, this result is not valid. In such a case, -1 is reported as the result.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxWcdmaMXSlotPhaseResults Class

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphasesynchronizationmode.html language=enus -->
## TOPIC 00230: RFmxWcdmaMXSlotPhaseSynchronizationMode Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphasesynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotphasesynchronizationmode.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXSlotPhaseSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of

### RFmxWcdmaMXSlotPhaseSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXSlotPhaseSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the SetMeasurementLength(string, int) method starting at SetMeasurementOffset(string, int) slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length method starting at SlotPhase Meas Offset slots from the slot boundary. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotpowerspectruminverted.html language=enus -->
## TOPIC 00231: RFmxWcdmaMXSlotPowerSpectrumInverted Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotpowerspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotpowerspectruminverted.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXSlotPowerSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxWcdmaMXSlotPowerSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXSlotPowerSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotpowersynchronizationmode.html language=enus -->
## TOPIC 00232: RFmxWcdmaMXSlotPowerSynchronizationMode Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotpowersynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxslotpowersynchronizationmode.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXSlotPowerSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the number of slo

### RFmxWcdmaMXSlotPowerSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXSlotPowerSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length method starting at SetMeasurementOffset(string, int) slots from the frame boundary. |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length method starting at SlotPower Measurement Offset slots from the slot boundary. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsubobject.html language=enus -->
## TOPIC 00233: RFmxWcdmaMXSubObject Class

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsubobject.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxsubobject.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents members that are common to all sub-object of RFmxWcdmaMX classes. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic class RFmxWcdmaMXSubObjectThread SafetyAny public static members of this type are thread safe. Any instance members are not guaranteed to be thread saf

### RFmxWcdmaMXSubObject Class

Represents members that are common to all sub-object of RFmxWcdmaMX classes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public class RFmxWcdmaMXSubObject

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtransmitterarchitecture.html language=enus -->
## TOPIC 00234: RFmxWcdmaMXTransmitterArchitecture Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtransmitterarchitecture.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtransmitterarchitecture.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RF architecture at the transmitter for a multicarrier signal. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXTransmitterArchitectureMembersNameValueDescriptionLOPerCarrier0Specifies that the transmitter has one LO at the center of each carrier. The IQ Origin Of

### RFmxWcdmaMXTransmitterArchitecture Enumeration

Specifies the RF architecture at the transmitter for a multicarrier signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXTransmitterArchitecture

#### Members

| Name | Value | Description |
| --- | --- | --- |
| LOPerCarrier | 0 | Specifies that the transmitter has one LO at the center of each carrier. The IQ Origin Offset result is an estimate of the I/Q origin offset of each carrier. |
| LOPerBand | 1 | Specifies that the transmitter has one LO at the center of all the carriers in the band. The Multicarrier IQ Origin Offset result is an estimate of the I/Q origin offset for the LO per Band architecture. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00235: RFmxWcdmaMXTriggerMinimumQuietTimeMode Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggerminimumquiettimemode.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXTriggerMinimumQuietTimeModeMembersNameValueDescriptionManual0The minimum quiet time for triggering is the value of the SetTriggerMinimumQuiet

### RFmxWcdmaMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXTriggerMinimumQuietTimeMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(string, double) method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggertype.html language=enus -->
## TOPIC 00236: RFmxWcdmaMXTriggerType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxtriggertype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXTriggerTypeMembersNameValueDescriptionNone0No Reference Trigger is configured. DigitalEdge1The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is spe

### RFmxWcdmaMXTriggerType Enumeration

Specifies the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(string, string) method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSlope(string, RFmxWcdmaMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinkscramblingtype.html language=enus -->
## TOPIC 00237: RFmxWcdmaMXUplinkScramblingType Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinkscramblingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinkscramblingtype.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of scrambling to use for the measurement. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXUplinkScramblingTypeMembersNameValueDescriptionLong0A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11,

### RFmxWcdmaMXUplinkScramblingType Enumeration

Specifies the type of scrambling to use for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXUplinkScramblingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Long | 0 | A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Short | 1 | A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinktestmodel.html language=enus -->
## TOPIC 00238: RFmxWcdmaMXUplinkTestModel Enumeration

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinktestmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxuplinktestmodel.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the uplink test model when the user sets the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. SyntaxNamespace: NationalInstruments.RFmx.WcdmaMXpublic enum RFmxWcdmaMXUplinkTestModelMembersNameValueDescriptionR6C_2_10The UL R6 C.2.1 configuration

### RFmxWcdmaMXUplinkTestModel Enumeration

Specifies the uplink test model when the user sets the [SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode)](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamx-setchannelconfigurationmode__string-rfmxwcdmamxchannelconfigurationmode.html) method to [TestModel](nationalinstruments-rfmx-wcdmamx-rfmxwcdmamxchannelconfigurationmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.WcdmaMX](nationalinstruments-rfmx-wcdmamx.html)

public enum RFmxWcdmaMXUplinkTestModel

#### Members

| Name | Value | Description |
| --- | --- | --- |
| R6C_2_1 | 0 | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_2 | 1 | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_3 | 2 | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_4 | 3 | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_2_5 | 4 | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6C_10_1_4_Subtest1 | 5 | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest2 | 6 | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest3 | 7 | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest4 | 8 | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest5 | 9 | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6C_10_1_4_Subtest6 | 10 | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7C_10_1_4_Subtest1 | 11 | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_10_1_4_Subtest2 | 12 | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_10_1_4_Subtest3 | 13 | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_10_1_4_Subtest4 | 14 | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest1 | 0xF | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest2 | 0x10 | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest3 | 17 | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest4 | 18 | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7C_11_1_3_Subtest5 | 19 | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8C_11_1_3_Subtest1 | 20 | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R8C_11_1_3_Subtest2 | 21 | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_3_Subtest3 | 22 | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_3_Subtest4 | 23 | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_3_Subtest5 | 24 | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8C_11_1_4_Subtest1 | 25 | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |

Parent topic:

NationalInstruments.RFmx.WcdmaMX

<!--NI_TOPIC bundle=rfmxwcdma-dotnet-api-ref path=nationalinstruments-rfmx-wcdmamx.html language=enus -->
## TOPIC 00239: NationalInstruments.RFmx.WcdmaMX

- bundle_id: `rfmxwcdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-wcdmamx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-wcdmamx.html
- document_id: `rfmxwcdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxWcdmaMXDefines a root class which is used to identify and control WCDMA signal configuration. RFmxWcdmaMXAcpRepresents the ACP measurement. RFmxWcdmaMXAcpConfigurationProvides methods to configure the ACP measurement. RFmxWcdmaMXAcpResultsProvides methods to fetch and read

### NationalInstruments.RFmx.WcdmaMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxWcdmaMX | Defines a root class which is used to identify and control WCDMA signal configuration. |
| RFmxWcdmaMXAcp | Represents the ACP measurement. |
| RFmxWcdmaMXAcpConfiguration | Provides methods to configure the ACP measurement. |
| RFmxWcdmaMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
| RFmxWcdmaMXCda | Represents the CDA measurement. |
| RFmxWcdmaMXCdaConfiguration | Provides methods to configure the CDA measurement. |
| RFmxWcdmaMXCdaResults | Provides methods to fetch and read the CDA measurement results. |
| RFmxWcdmaMXChp | Represents the CHP measurement. |
| RFmxWcdmaMXChpConfiguration | Provides methods to configure the CHP measurement. |
| RFmxWcdmaMXChpResults | Provides methods to fetch and read the CHP measurement results. |
| RFmxWcdmaMXConstants | Specifies constants for I/O terminals. |
| RFmxWcdmaMXModAcc | Represents the ModAcc measurement. |
| RFmxWcdmaMXModAccConfiguration | Provides methods to configure the ModAcc measurement. |
| RFmxWcdmaMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
| RFmxWcdmaMXObw | Represents the OBW measurement. |
| RFmxWcdmaMXObwConfiguration | Provides methods to configure the OBW measurement. |
| RFmxWcdmaMXObwResults | Provides methods to fetch and read the OBW measurement results. |
| RFmxWcdmaMXQevm | Represents the QEVM measurement. |
| RFmxWcdmaMXQevmConfiguration | Provides methods to configure the QEVM measurement. |
| RFmxWcdmaMXQevmResults | Provides methods to fetch and read the QEVM measurement results. |
| RFmxWcdmaMXSem | Represents the SEM measurement. |
| RFmxWcdmaMXSemConfiguration | Provides methods to configure the SEM measurement. |
| RFmxWcdmaMXSemResults | Provides methods to fetch and read the SEM measurement results. |
| RFmxWcdmaMXSlotPhase | Represents the SlotPhase measurement. |
| RFmxWcdmaMXSlotPhaseConfiguration | Provides methods to configure the SlotPhase measurement. |
| RFmxWcdmaMXSlotPhaseResults | Provides methods to fetch and read the SlotPhase measurement results. |
| RFmxWcdmaMXSlotPower | Represents the SlotPower measurement. |
| RFmxWcdmaMXSlotPowerConfiguration | Provides methods to configure the SlotPower measurement. |
| RFmxWcdmaMXSlotPowerResults | Provides methods to fetch and read the SlotPower measurement results. |
| RFmxWcdmaMXSubObject | Represents members that are common to all sub-object of RFmxWcdmaMX classes. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxWcdmaMXAcpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| RFmxWcdmaMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
| RFmxWcdmaMXAcpAveragingType | Specifies the averaging type for averaging the spectrum of multiple acquisitions. The averaged spectrum is used for ACP measurement. |
| RFmxWcdmaMXAcpFftOverlapMode | Specifies how overlapping is applied when computing the FFT of the acquired samples. The default value is Disabled. |
| RFmxWcdmaMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |
| RFmxWcdmaMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |
| RFmxWcdmaMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxWcdmaMXAcpOffsetPowerReferenceCarrier | Specifies the carrier used as the power reference to measure the offset channel relative power. |
| RFmxWcdmaMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxWcdmaMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxWcdmaMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxWcdmaMXBranch | Specifies the branch on which the data is modulated in the channel. |
| RFmxWcdmaMXCdaIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the CDA measurement. |
| RFmxWcdmaMXCdaMeasurementChannelBranch | Specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| RFmxWcdmaMXCdaMeasurementChannelModulationType | Specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| RFmxWcdmaMXCdaPowerUnit | Specifies the measurement unit of all power results, except GetTotalPower(string, out double). |
| RFmxWcdmaMXCdaRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| RFmxWcdmaMXCdaSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxWcdmaMXCdaSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| RFmxWcdmaMXChannelConfigurationMode | Specifies the channel configuration mode. |
| RFmxWcdmaMXChpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| RFmxWcdmaMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |
| RFmxWcdmaMXChpAveragingType | Specifies the averaging type for averaging the spectrum of multiple acquisitions. |
| RFmxWcdmaMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxWcdmaMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxWcdmaMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxWcdmaMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. |
| RFmxWcdmaMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. |
| RFmxWcdmaMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. |
| RFmxWcdmaMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| RFmxWcdmaMXLinkDirection | Specifies the direction for which the frequency is calculated. |
| RFmxWcdmaMXMeasurementTypes | Specifies the type of measurement. |
| RFmxWcdmaMXModAccDetectedBranch | Returns the branch of the detected channel. |
| RFmxWcdmaMXModAccDetectedModulationType | Returns the modulation type of the detected channel. |
| RFmxWcdmaMXModAccIQGainImbalanceRemovalEnabled | Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. |
| RFmxWcdmaMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the ModAcc measurement. |
| RFmxWcdmaMXModAccIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. |
| RFmxWcdmaMXModAccPeakActiveCdeBranch | Returns the branch of the channel corresponding to the value of the GetPeakActiveCde(string, out double) method for a carrier. |
| RFmxWcdmaMXModAccPeakCdeBranch | Returns the branch corresponding to the value of the GetPeakCde(string, out double) method. |
| RFmxWcdmaMXModAccPeakRcdeBranch | Returns the branch of the channel corresponding to the value of the GetPeakRcde(string, out double) method for a carrier. |
| RFmxWcdmaMXModAccRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| RFmxWcdmaMXModAccSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxWcdmaMXModAccSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| RFmxWcdmaMXModAccTransientRemovalEnabled | Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |
| RFmxWcdmaMXModulationType | Specifies the modulation type for the channel. |
| RFmxWcdmaMXObwAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| RFmxWcdmaMXObwAveragingEnabled | Specifies whether to enable averaging for the OBW measurement. |
| RFmxWcdmaMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| RFmxWcdmaMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxWcdmaMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxWcdmaMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxWcdmaMXPropertyId | Specifies all the attribute identifiers. |
| RFmxWcdmaMXQevmAveragingEnabled | Specifies whether to enable averaging for the QEVM measurement. |
| RFmxWcdmaMXQevmIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the QEVM measurement. |
| RFmxWcdmaMXQevmRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| RFmxWcdmaMXQevmSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxWcdmaMXSemAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuation function to configure the external attenuation table. |
| RFmxWcdmaMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |
| RFmxWcdmaMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. |
| RFmxWcdmaMXSemLowerOffsetMeasurementStatus | Indicates the measurement status based on the GetLowerOffsetMargin(string, out double) method. |
| RFmxWcdmaMXSemMeasurementStatus | Indicates the overall SEM measurement status, based on the value of the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetLowerOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemLowerOffsetMeasurementStatus@) and the NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemResults.GetUpperOffsetMeasurementStatus(string,NationalInstruments.RFmx.WcdmaMX.RFmxWcdmaMXSemUpperOffsetMeasurementStatus@) properties. |
| RFmxWcdmaMXSemOffsetRbwFilterType | Returns the shape of the digital RBW filter. |
| RFmxWcdmaMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| RFmxWcdmaMXSemUpperOffsetMeasurementStatus | Indicates the measurement status based on the GetUpperOffsetMargin(string, out double) method. |
| RFmxWcdmaMXSlotPhaseRrcFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
| RFmxWcdmaMXSlotPhaseSpectrumInverted | Specifies whether the signal spectrum is inverted. |
| RFmxWcdmaMXSlotPhaseSynchronizationMode | Specifies whether the measurement is performed from the frame or the slot boundary. |
| RFmxWcdmaMXSlotPhaseTransientRemovalEnabled | Specifies whether the SlotPhase measurement excludes 25 microseconds from the start and end of each slot while computing the linear-fit chip phase error, which is used to compute phase discontinuities at the slot boundaries. |
| RFmxWcdmaMXSlotPowerRrcFilterEnabled | Specifies whether to enable the RRC filter. |
| RFmxWcdmaMXSlotPowerSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
| RFmxWcdmaMXSlotPowerSynchronizationMode | Specifies whether the measurement is performed from the frame or slot boundary. |
| RFmxWcdmaMXTransmitterArchitecture | Specifies the RF architecture at the transmitter for a multicarrier signal. |
| RFmxWcdmaMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxWcdmaMXTriggerType | Specifies the trigger type. |
| RFmxWcdmaMXUplinkScramblingType | Specifies the type of scrambling to use for the measurement. |
| RFmxWcdmaMXUplinkTestModel | Specifies the uplink test model when the user sets the SetChannelConfigurationMode(string, RFmxWcdmaMXChannelConfigurationMode) method to TestModel. |

#### Delegates

None
