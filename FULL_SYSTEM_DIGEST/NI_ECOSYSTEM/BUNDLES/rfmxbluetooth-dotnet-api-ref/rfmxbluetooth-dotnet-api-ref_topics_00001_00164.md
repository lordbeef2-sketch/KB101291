# NI DOCUMENT BUNDLE: rfmxbluetooth-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxbluetooth-dotnet-api-ref start=1 end=164 -->
<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-autodetectsignal__string-double.html language=enus -->
## TOPIC 00001: AutoDetectSignal(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-autodetectsignal__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-autodetectsignal__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects the Bluetooth packet and returns the detected packet type, data rate, packet format and payload length.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int AutoDetectSignal(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The si

### AutoDetectSignal(string, double)

Detects the Bluetooth packet and returns the detected packet type, data rate, packet format and payload length.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int AutoDetectSignal(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-autolevel__string-double-out.html language=enus -->
## TOPIC 00002: AutoLevel(string, double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-autolevel__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-autolevel__string-double-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(string, double) method. Use this method to help calculate an approximate setting for the reference level.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int AutoLevel(string selectorStr

### AutoLevel(string, double, out double)

Examines the input signal to calculate the peak power level and sets it as the value of the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-btmx-rfmxbtmx-setreferencelevel__string-double.html) method. Use this method to help calculate an approximate setting for the reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int AutoLevel(string selectorString, double measurementInterval, out double referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level method does not use any trigger for acquisition. It ignores the user-configured trigger methods. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | out double | Upon return, contains the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-buildslotstring__string-int.html language=enus -->
## TOPIC 00003: BuildSlotString(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-buildslotstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-buildslotstring__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string for use with the TXP configuration or fetch methods and methods. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic static string BuildSlotString(string selectorString, int slotNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising

### BuildSlotString(string, int)

Creates a selector string for use with the TXP configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public static string BuildSlotString(string selectorString, int slotNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| slotNumber | int | Specifies the slot number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-checkmeasurementstatus__string-out.html language=enus -->
## TOPIC 00004: CheckMeasurementStatus(string, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-checkmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-checkmeasurementstatus__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int CheckMeasurementStatus(string selectorString, out bool is

### CheckMeasurementStatus(string, out bool)

Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int CheckMeasurementStatus(string selectorString, out bool isDone)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| isDone | out bool | True if the measurement is complete; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-configuredatarate__string-int.html language=enus -->
## TOPIC 00005: ConfigureDataRate(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-configuredatarate__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-configuredatarate__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the data rate of the low energy (LE) or low energy - channel sounding (LE-CS) packet to be measured.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigureDataRate(string selectorString, int dataRate)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The sig

### ConfigureDataRate(string, int)

Configures the data rate of the low energy (LE) or low energy - channel sounding (LE-CS) packet to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigureDataRate(string selectorString, int dataRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| dataRate | int | Specifies the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This parameter is applicable to the LE/LE-CS packet types. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-configuredigitaledgetrigger__string-string-rfmxbtmxdigitaledgetriggeredge-double-bool.html language=enus -->
## TOPIC 00006: ConfigureDigitalEdgeTrigger(string, string, RFmxBTMXDigitalEdgeTriggerEdge, double, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-configuredigitaledgetrigger__string-string-rfmxbtmxdigitaledgetriggeredge-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-configuredigitaledgetrigger__string-string-rfmxbtmxdigitaledgetriggeredge-double-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigureDigitalEdgeTrigger(string selectorString, string digitalEdgeTriggerSource, RFmxBTMXDigitalEdgeTriggerEdge digitalEdgeTriggerE

### ConfigureDigitalEdgeTrigger(string, string, RFmxBTMXDigitalEdgeTriggerEdge, double, bool)

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigureDigitalEdgeTrigger(string selectorString, string digitalEdgeTriggerSource, RFmxBTMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge, double triggerDelay, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| digitalEdgeTriggerSource | string | Specifies the source terminal for the RFmxBTMXConstants. |
| digitalEdgeTriggerEdge | RFmxBTMXDigitalEdgeTriggerEdge | Specifies the trigger edge to detect. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| enableTrigger | bool | Specifies whether to enable the trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-configureiqpoweredgetrigger__string-string-rfmxbtmxiqpoweredgetriggerslope-double-double-rfmxbtmxtriggerminimumquiettimemode-double-rfmxbtmxiqpowe...d17e915.html language=enus -->
## TOPIC 00007: ConfigureIQPowerEdgeTrigger(string, string, RFmxBTMXIQPowerEdgeTriggerSlope, double, double, RFmxBTMXTriggerMinimumQuietTimeMode, double, RFmxBTMXIQPowerEdgeTriggerLevelType, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-configureiqpoweredgetrigger__string-string-rfmxbtmxiqpoweredgetriggerslope-double-double-rfmxbtmxtriggerminimumquiettimemode-double-rfmxbtmxiqpowe...d17e915.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-configureiqpoweredgetrigger__string-string-rfmxbtmxiqpoweredgetriggerslope-double-double-rfmxbtmxtriggerminimumquiettimemode-double-rfmxbtmxiqpowe...d17e915.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxBTMXIQPow

### ConfigureIQPowerEdgeTrigger(string, string, RFmxBTMXIQPowerEdgeTriggerSlope, double, double, RFmxBTMXTriggerMinimumQuietTimeMode, double, RFmxBTMXIQPowerEdgeTriggerLevelType, bool)

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxBTMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope, double iqPowerEdgeTriggerLevel, double triggerDelay, RFmxBTMXTriggerMinimumQuietTimeMode triggerMinimumQuietTimeMode, double triggerMinimumQuietTimeDuration, RFmxBTMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| iqPowerEdgeTriggerSource | string | Specifies the channel from which the device monitors the trigger. |
| iqPowerEdgeTriggerSlope | RFmxBTMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| iqPowerEdgeTriggerLevel | double | Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| triggerMinimumQuietTimeMode | RFmxBTMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| triggerMinimumQuietTimeDuration | double | Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(string, RFmxBTMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level. |
| iqPowerEdgeTriggerLevelType | RFmxBTMXIQPowerEdgeTriggerLevelType | Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. |
| enableTrigger | bool | Specifies whether the trigger is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-configurepayloadbitpattern__string-rfmxbtmxpayloadbitpattern.html language=enus -->
## TOPIC 00008: ConfigurePayloadBitPattern(string, RFmxBTMXPayloadBitPattern)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-configurepayloadbitpattern__string-rfmxbtmxpayloadbitpattern.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-configurepayloadbitpattern__string-rfmxbtmxpayloadbitpattern.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the bit pattern present in the payload of the packet.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigurePayloadBitPattern(string selectorString, RFmxBTMXPayloadBitPattern payloadBitPattern)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal nam

### ConfigurePayloadBitPattern(string, RFmxBTMXPayloadBitPattern)

Configures the bit pattern present in the payload of the packet.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigurePayloadBitPattern(string selectorString, RFmxBTMXPayloadBitPattern payloadBitPattern)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| payloadBitPattern | RFmxBTMXPayloadBitPattern | Specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-configurepayloadlength__string-rfmxbtmxpayloadlengthmode-int.html language=enus -->
## TOPIC 00009: ConfigurePayloadLength(string, RFmxBTMXPayloadLengthMode, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-configurepayloadlength__string-rfmxbtmxpayloadlengthmode-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-configurepayloadlength__string-rfmxbtmxpayloadlengthmode-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the payloadLengthMode and Auto parameters that decide the length of the payload to be used for the measurement.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigurePayloadLength(string selectorString, RFmxBTMXPayloadLengthMode payloadLengthMode, int payloadLength)ParametersNa

### ConfigurePayloadLength(string, RFmxBTMXPayloadLengthMode, int)

Configures the *payloadLengthMode* and [Auto](nationalinstruments-rfmx-btmx-rfmxbtmxpayloadlengthmode.html) parameters that decide the length of the payload to be used for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigurePayloadLength(string selectorString, RFmxBTMXPayloadLengthMode payloadLengthMode, int payloadLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| payloadLengthMode | RFmxBTMXPayloadLengthMode | Specifies the payload length mode of the signal to be measured. The payloadLengthMode and Auto parameters decide the length of the payload to be used for measurement. |
| payloadLength | int | Specifies the payload length of BR, EDR, LE and LE-CS packet, and the payload zone length of LE-HDT packet, in bytes. The parameter is applicable only when you set the payloadLengthMode parameter to Manual. This parameter returns the payload length or payload zone length used for measurement if you set the Payload Length Mode parameter to Auto. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-configurereferencelevel__string-double.html language=enus -->
## TOPIC 00010: ConfigureReferenceLevel(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-configurereferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-configurereferencelevel__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level which represents the maximum expected power of an RF input signal.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigureReferenceLevel(string selectorString, double referenceLevel)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The si

### ConfigureReferenceLevel(string, double)

Configures the reference level which represents the maximum expected power of an RF input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigureReferenceLevel(string selectorString, double referenceLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceLevel | double | Specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getattributebool__string-int-out.html language=enus -->
## TOPIC 00011: GetAttributeBool(string, int, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getattributebool__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getattributebool__string-int-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to the Using

### GetAttributeBool(string, int, out bool)

Gets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out bool | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getattributestring__string-int-out.html language=enus -->
## TOPIC 00012: GetAttributeString(string, int, out string)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getattributestring__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getattributestring__string-int-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a of an RFmx string. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAttributeString(string selectorString, int attributeIdentifier, out string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to th

### GetAttributeString(string, int, out string)

Gets the value of a of an RFmx string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAttributeString(string selectorString, int attributeIdentifier, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out string | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getbdaddresslap__string-out.html language=enus -->
## TOPIC 00013: GetBDAddressLap(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getbdaddresslap__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getbdaddresslap__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetBDAddressLap(string selectorString, out int value)RemarksThis method gets the value of BDAddressLap attribute.The default value is 0.ParametersNameTypeDescr

### GetBDAddressLap(string, out int)

Gets the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetBDAddressLap(string selectorString, out int value)

#### Remarks

This method gets the value of [BDAddressLap](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingphasemeasurementperiod__string-out.html language=enus -->
## TOPIC 00014: GetChannelSoundingPhaseMeasurementPeriod(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingphasemeasurementperiod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingphasemeasurementperiod__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC.

### GetChannelSoundingPhaseMeasurementPeriod(string, out double)

Gets the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to LE-CS and the [SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat)](nationalinstruments-rfmx-btmx-rfmxbtmx-setchannelsoundingpacketformat__string-rfmxbtmxchannelsoundingpacketformat.html) method to any value other than SYNC.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetChannelSoundingPhaseMeasurementPeriod(string selectorString, out double value)

#### Remarks

This method gets the value of [ChannelSoundingPhaseMeasurementPeriod](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10 us.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingsyncsequence__string-out.html language=enus -->
## TOPIC 00015: GetChannelSoundingSyncSequence(string, out RFmxBTMXChannelSoundingSyncSequence)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingsyncsequence__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingsyncsequence__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS To

### GetChannelSoundingSyncSequence(string, out RFmxBTMXChannelSoundingSyncSequence)

Gets the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to LE-CS and the [SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat)](nationalinstruments-rfmx-btmx-rfmxbtmx-setchannelsoundingpacketformat__string-rfmxbtmxchannelsoundingpacketformat.html) method to any value other than CS Tone.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetChannelSoundingSyncSequence(string selectorString, out RFmxBTMXChannelSoundingSyncSequence value)

#### Remarks

This method gets the value of [ChannelSoundingSyncSequence](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is None.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXChannelSoundingSyncSequence | Upon return, contains the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingtoneextensionslot__string-out.html language=enus -->
## TOPIC 00016: GetChannelSoundingToneExtensionSlot(string, out RFmxBTMXChannelSoundingToneExtensionSlot)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingtoneextensionslot__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getchannelsoundingtoneextensionslot__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYN

### GetChannelSoundingToneExtensionSlot(string, out RFmxBTMXChannelSoundingToneExtensionSlot)

Gets whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to LE-CS and the [SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat)](nationalinstruments-rfmx-btmx-rfmxbtmx-setchannelsoundingpacketformat__string-rfmxbtmxchannelsoundingpacketformat.html) method to any value other than SYNC.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetChannelSoundingToneExtensionSlot(string selectorString, out RFmxBTMXChannelSoundingToneExtensionSlot value)

#### Remarks

This method gets the value of [ChannelSoundingToneExtensionSlot](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is Disabled.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXChannelSoundingToneExtensionSlot | Upon return, contains whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getcteslotduration__string-out.html language=enus -->
## TOPIC 00017: GetCteSlotDuration(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getcteslotduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getcteslotduration__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. SyntaxNamespace: National

### GetCteSlotDuration(string, out double)

Gets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfArrival](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) or [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetCteSlotDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [CteSlotDuration](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 0.000001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the length of the transmit slots and sampling slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getdatarate__string-out.html language=enus -->
## TOPIC 00018: GetDataRate(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getdatarate__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getdatarate__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the data rate of the LE, LE-CS or LE-HDT packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable only to LE, LE-CS or LE-HDT packet type. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetDataRate(string selectorString, out int valu

### GetDataRate(string, out int)

Gets the data rate of the LE, LE-CS or LE-HDT packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable only to LE, LE-CS or LE-HDT packet type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetDataRate(string selectorString, out int value)

#### Remarks

This method gets the value of [DataRate](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 1M.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the data rate of the LE, LE-CS or LE-HDT packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable only to LE, LE-CS or LE-HDT packet type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getdetecteddatarate__string-out.html language=enus -->
## TOPIC 00019: GetDetectedDataRate(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getdetecteddatarate__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getdetecteddatarate__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE and LE-HDT. This method can be queried only after calling the RFmxBT Auto Detect Signal function. SyntaxNamespace: NationalInstruments.RFmx.

### GetDetectedDataRate(string, out int)

Gets the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE and LE-HDT. This method can be queried only after calling the RFmxBT Auto Detect Signal function.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetDetectedDataRate(string selectorString, out int value)

#### Remarks

This method gets the value of [DetectedDataRate](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is Not Applicable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE and LE-HDT. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getdetectedpackettype__string-out.html language=enus -->
## TOPIC 00020: GetDetectedPacketType(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getdetectedpackettype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getdetectedpackettype__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the packet type detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetDetectedPacketType(string selectorString, out int value)RemarksThis method gets t

### GetDetectedPacketType(string, out int)

Gets the packet type detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetDetectedPacketType(string selectorString, out int value)

#### Remarks

This method gets the value of [DetectedPacketType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is Unknown.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the packet type detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getdirectionfindingmode__string-out.html language=enus -->
## TOPIC 00021: GetDirectionFindingMode(string, out RFmxBTMXDirectionFindingMode)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getdirectionfindingmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getdirectionfindingmode__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mode of direction finding. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetDirectionFindingMode(string selectorString, out RFmxBTMXDirectionFindingMode value)RemarksThis method gets the value of DirectionFindingMode attribute.The default value is Disabled.ParametersNameTypeDescr

### GetDirectionFindingMode(string, out RFmxBTMXDirectionFindingMode)

Gets the mode of direction finding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetDirectionFindingMode(string selectorString, out RFmxBTMXDirectionFindingMode value)

#### Remarks

This method gets the value of [DirectionFindingMode](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXDirectionFindingMode | Upon return, contains the mode of direction finding. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-geterror__out-out.html language=enus -->
## TOPIC 00022: GetError(out int, out string)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-geterror__out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout stringUpon return, contains the la

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-geterrorstring__int-out.html language=enus -->
## TOPIC 00023: GetErrorString(int, out string)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-geterrorstring__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-geterrorstring__int-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the status code returned by an RFmxBT function into a string. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetErrorString(int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeintSpecifies an error or warning code.errorDescriptionout stringUpon return,

### GetErrorString(int, out string)

Converts the status code returned by an RFmxBT function into a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetErrorString(int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | int | Specifies an error or warning code. |
| errorDescription | out string | Upon return, contains the error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getexternalattenuation__string-out.html language=enus -->
## TOPIC 00024: GetExternalAttenuation(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getexternalattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getexternalattenuation__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetExternalAttenuation(string selectorString, out double value)RemarksThis method gets the value of ExternalAtt

### GetExternalAttenuation(string, out double)

Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetExternalAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [ExternalAttenuation](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-gethighdatathroughputpacketformat__string-out.html language=enus -->
## TOPIC 00025: GetHighDataThroughputPacketFormat(string, out RFmxBTMXHighDataThroughputPacketFormat)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-gethighdatathroughputpacketformat__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-gethighdatathroughputpacketformat__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetHighDataThroughputPacketFormat(string selectorString, out RFmxBTMXHigh

### GetHighDataThroughputPacketFormat(string, out RFmxBTMXHighDataThroughputPacketFormat)

Gets the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetHighDataThroughputPacketFormat(string selectorString, out RFmxBTMXHighDataThroughputPacketFormat value)

#### Remarks

This method gets the value of [HighDataThroughputPacketFormat](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Format0](nationalinstruments-rfmx-btmx-rfmxbtmxhighdatathroughputpacketformat.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXHighDataThroughputPacketFormat | Upon return, contains the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getnumberofblockrepetitionsequences__string-out.html language=enus -->
## TOPIC 00026: GetNumberOfBlockRepetitionSequences(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getnumberofblockrepetitionsequences__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getnumberofblockrepetitionsequences__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetNumberOfBlockRepetitionSequences(string selectorString, out int value)

### GetNumberOfBlockRepetitionSequences(string, out int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetNumberOfBlockRepetitionSequences(string selectorString, out int value)

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getpayloadlength__string-out.html language=enus -->
## TOPIC 00027: GetPayloadLength(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getpayloadlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getpayloadlength__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the payload length of BR, EDR, LE and LE-CS packet, and the payload zone length of LE-HDT packet, in bytes. This method is applicable only when you set the SetPayloadLengthMode(string, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length or payload zone length use

### GetPayloadLength(string, out int)

Gets the payload length of BR, EDR, LE and LE-CS packet, and the payload zone length of LE-HDT packet, in bytes. This method is applicable only when you set the [SetPayloadLengthMode(string, RFmxBTMXPayloadLengthMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpayloadlengthmode__string-rfmxbtmxpayloadlengthmode.html) method to [Manual](nationalinstruments-rfmx-btmx-rfmxbtmxpayloadlengthmode.html). This method returns the payload length or payload zone length used for measurement if you set the Payload Length Mode method to [Auto](nationalinstruments-rfmx-btmx-rfmxbtmxpayloadlengthmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPayloadLength(string selectorString, out int value)

#### Remarks

This method gets the value of [PayloadLength](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the payload length of BR, EDR, LE and LE-CS packet, and the payload zone length of LE-HDT packet, in bytes. This method is applicable only when you set the SetPayloadLengthMode(string, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length or payload zone length used for measurement if you set the Payload Length Mode method to Auto. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-gettriggerdelay__string-out.html language=enus -->
## TOPIC 00028: GetTriggerDelay(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-gettriggerdelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-gettriggerdelay__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetTriggerDelay(string selectorStrin

### GetTriggerDelay(string, out double)

Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetTriggerDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerDelay](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-gettriggertype__string-out.html language=enus -->
## TOPIC 00029: GetTriggerType(string, out RFmxBTMXTriggerType)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-gettriggertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-gettriggertype__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of trigger to be used for signal acquisition. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetTriggerType(string selectorString, out RFmxBTMXTriggerType value)RemarksThis method gets the value of TriggerType attribute.The default value is IQPowerEdge.ParametersNameTypeDescr

### GetTriggerType(string, out RFmxBTMXTriggerType)

Gets the type of trigger to be used for signal acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetTriggerType(string selectorString, out RFmxBTMXTriggerType value)

#### Remarks

This method gets the value of [TriggerType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [IQPowerEdge](nationalinstruments-rfmx-btmx-rfmxbtmxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXTriggerType | Upon return, contains the type of trigger to be used for signal acquisition. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getvhdtmodeenabled__string-out.html language=enus -->
## TOPIC 00030: GetVhdtModeEnabled(string, out RFmxBTMXVhdtModeEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getvhdtmodeenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getvhdtmodeenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetVhdtModeEnabled(string selectorString, out RFmxBTMXVhdtModeEnabled value)

### GetVhdtModeEnabled(string, out RFmxBTMXVhdtModeEnabled)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetVhdtModeEnabled(string selectorString, out RFmxBTMXVhdtModeEnabled value)

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-getzadoffchuindex__string-out.html language=enus -->
## TOPIC 00031: GetZadoffChuIndex(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-getzadoffchuindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-getzadoffchuindex__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. SyntaxNamespace: NationalInstruments.RFmx.

### GetZadoffChuIndex(string, out int)

Gets Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetZadoffChuIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [ZadoffChuIndex](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 7.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-resettodefault__string.html language=enus -->
## TOPIC 00032: ResetToDefault(string)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-resettodefault__string.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used.ReturnsReturns the

### ResetToDefault(string)

Resets a signal to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setctelength__string-double.html language=enus -->
## TOPIC 00033: SetCteLength(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setctelength__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setctelength__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. SyntaxNamespace: N

### SetCteLength(string, double)

Sets the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to either [AngleOfArrival](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) or [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetCteLength(string selectorString, double value)

#### Remarks

This method sets the value of [CteLength](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 160 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setcteslotduration__string-double.html language=enus -->
## TOPIC 00034: SetCteSlotDuration(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setcteslotduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setcteslotduration__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. SyntaxNamespace: National

### SetCteSlotDuration(string, double)

Sets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfArrival](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) or [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetCteSlotDuration(string selectorString, double value)

#### Remarks

This method sets the value of [CteSlotDuration](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 0.000001.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the length of the transmit slots and sampling slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setdigitaledgetriggersource__string-string.html language=enus -->
## TOPIC 00035: SetDigitalEdgeTriggerSource(string, string)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setdigitaledgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setdigitaledgetriggersource__string-string.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetDigitalEdgeTriggerSource(string selectorString, string value)RemarksThis met

### SetDigitalEdgeTriggerSource(string, string)

Sets the source terminal for the digital edge trigger. This method is used only when you set the [SetTriggerType(string, RFmxBTMXTriggerType)](nationalinstruments-rfmx-btmx-rfmxbtmx-settriggertype__string-rfmxbtmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-btmx-rfmxbtmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetDigitalEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-sethighdatathroughputpacketformat__string-rfmxbtmxhighdatathroughputpacketformat.html language=enus -->
## TOPIC 00036: SetHighDataThroughputPacketFormat(string, RFmxBTMXHighDataThroughputPacketFormat)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-sethighdatathroughputpacketformat__string-rfmxbtmxhighdatathroughputpacketformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-sethighdatathroughputpacketformat__string-rfmxbtmxhighdatathroughputpacketformat.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetHighDataThroughputPacketFormat(string selectorString, RFmxBTMXHighData

### SetHighDataThroughputPacketFormat(string, RFmxBTMXHighDataThroughputPacketFormat)

Sets the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetHighDataThroughputPacketFormat(string selectorString, RFmxBTMXHighDataThroughputPacketFormat value)

#### Remarks

This method sets the value of [HighDataThroughputPacketFormat](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Format0](nationalinstruments-rfmx-btmx-rfmxbtmxhighdatathroughputpacketformat.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXHighDataThroughputPacketFormat | Specifies the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setnumberofblockrepetitionsequences__string-int.html language=enus -->
## TOPIC 00037: SetNumberOfBlockRepetitionSequences(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setnumberofblockrepetitionsequences__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setnumberofblockrepetitionsequences__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetNumberOfBlockRepetitionSequences(string selectorString, int value)

### SetNumberOfBlockRepetitionSequences(string, int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetNumberOfBlockRepetitionSequences(string selectorString, int value)

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html language=enus -->
## TOPIC 00038: SetPacketType(string, RFmxBTMXPacketType)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of the Bluetooth packet to be measured. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetPacketType(string selectorString, RFmxBTMXPacketType value)RemarksThis method sets the value of PacketType attribute.The default value is PacketTypeDH1.ParametersNameTypeDescriptionselec

### SetPacketType(string, RFmxBTMXPacketType)

Sets the type of the Bluetooth packet to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetPacketType(string selectorString, RFmxBTMXPacketType value)

#### Remarks

This method sets the value of [PacketType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [PacketTypeDH1](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXPacketType | Specifies the type of the Bluetooth packet to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setreferencelevel__string-double.html language=enus -->
## TOPIC 00039: SetReferenceLevel(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setreferencelevel__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetReferenceLevel(string selectorString, double value)RemarksThis method

### SetReferenceLevel(string, double)

Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetReferenceLevel(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevel](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setvhdtmodeenabled__string-rfmxbtmxvdhtmodeenabled.html language=enus -->
## TOPIC 00040: SetVhdtModeEnabled(string, RFmxBTMXVdhtModeEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setvhdtmodeenabled__string-rfmxbtmxvdhtmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setvhdtmodeenabled__string-rfmxbtmxvdhtmodeenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetVhdtModeEnabled(string selectorString, RFmxBTMXVdhtModeEnabled value)

### SetVhdtModeEnabled(string, RFmxBTMXVdhtModeEnabled)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetVhdtModeEnabled(string selectorString, RFmxBTMXVdhtModeEnabled value)

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-setzadoffchuindex__string-int.html language=enus -->
## TOPIC 00041: SetZadoffChuIndex(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-setzadoffchuindex__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-setzadoffchuindex__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. SyntaxNamespace: NationalInstruments.RFmx.

### SetZadoffChuIndex(string, int)

Sets Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetZadoffChuIndex(string selectorString, int value)

#### Remarks

This method sets the value of [ZadoffChuIndex](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 7.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-txp.html language=enus -->
## TOPIC 00042: Txp

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-txp.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxBTMXTxp instance that represents the TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic RFmxBTMXTxp Txp { get; }

### Txp

Gets the [RFmxBTMXTxp](nationalinstruments-rfmx-btmx-rfmxbtmxtxp.html) instance that represents the TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public [RFmxBTMXTxp](nationalinstruments-rfmx-btmx-rfmxbtmxtxp.html) Txp { get; }

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00043: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the res

### WaitForMeasurementComplete(string, double)

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMX Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpaveragingenabled.html language=enus -->
## TOPIC 00044: RFmxBTMXAcpAveragingEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXAcpAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement uses the SetAveragingCount(string, int) meth

### RFmxBTMXAcpAveragingEnabled Enumeration

Specifies whether to enable averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXAcpAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement uses the SetAveragingCount(string, int) method as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-configureoffsetchannelmode__string-rfmxbtmxacpoffsetchannelmode.html language=enus -->
## TOPIC 00045: ConfigureOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-configureoffsetchannelmode__string-rfmxbtmxacpoffsetchannelmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-configureoffsetchannelmode__string-rfmxbtmxacpoffsetchannelmode.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset channels used for the adjacent channel power (ACP) measurement.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigureOffsetChannelMode(string selectorString, RFmxBTMXAcpOffsetChannelMode offsetChannelMode)ParametersNameTypeDescriptionselectorStringstringPass an empt

### ConfigureOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode)

Configures the offset channels used for the adjacent channel power (ACP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigureOffsetChannelMode(string selectorString, RFmxBTMXAcpOffsetChannelMode offsetChannelMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| offsetChannelMode | RFmxBTMXAcpOffsetChannelMode | Specifies which offset channels are used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00046: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of AcpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorString

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [AcpMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getoffsetchannelmode__string-out.html language=enus -->
## TOPIC 00047: GetOffsetChannelMode(string, out RFmxBTMXAcpOffsetChannelMode)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getoffsetchannelmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getoffsetchannelmode__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets which offset channels are used for the measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetOffsetChannelMode(string selectorString, out RFmxBTMXAcpOffsetChannelMode value)RemarksThis method gets the value of AcpOffsetChannelMode attribute.The default value is Symmetric.Para

### GetOffsetChannelMode(string, out RFmxBTMXAcpOffsetChannelMode)

Gets which offset channels are used for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetOffsetChannelMode(string selectorString, out RFmxBTMXAcpOffsetChannelMode value)

#### Remarks

This method gets the value of [AcpOffsetChannelMode](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Symmetric](nationalinstruments-rfmx-btmx-rfmxbtmxacpoffsetchannelmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXAcpOffsetChannelMode | Upon return, contains which offset channels are used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getoffsetfrequency__string-out.html language=enus -->
## TOPIC 00048: GetOffsetFrequency(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getoffsetfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-getoffsetfrequency__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetOffsetFrequency(string selectorString, out double value)RemarksThis method gets the value of AcpOffsetFrequency attribu

### GetOffsetFrequency(string, out double)

Gets the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetOffsetFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpOffsetFrequency](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 1 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00049: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable all traces for the adjacent channel power (ACP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of AcpAllTracesEnabled attribute.The default value is FALSE.Parameters

### SetAllTracesEnabled(string, bool)

Sets whether to enable all traces for the adjacent channel power (ACP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable all traces for the adjacent channel power (ACP) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setaveragingenabled__string-rfmxbtmxacpaveragingenabled.html language=enus -->
## TOPIC 00050: SetAveragingEnabled(string, RFmxBTMXAcpAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setaveragingenabled__string-rfmxbtmxacpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setaveragingenabled__string-rfmxbtmxacpaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingEnabled(string selectorString, RFmxBTMXAcpAveragingEnabled value)RemarksThis method sets the value of AcpAveragingEnabled attribute.The default value is False.ParametersName

### SetAveragingEnabled(string, RFmxBTMXAcpAveragingEnabled)

Sets whether to enable averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingEnabled(string selectorString, RFmxBTMXAcpAveragingEnabled value)

#### Remarks

This method sets the value of [AcpAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxacpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00051: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of AcpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStringstri

### SetMeasurementEnabled(string, bool)

Sets whether to enable the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [AcpMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpoffsetchannelmode.html language=enus -->
## TOPIC 00052: RFmxBTMXAcpOffsetChannelMode Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpoffsetchannelmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpoffsetchannelmode.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which offset channels are used for the measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXAcpOffsetChannelModeMembersNameValueDescriptionSymmetric0Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on

### RFmxBTMXAcpOffsetChannelMode Enumeration

Specifies which offset channels are used for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXAcpOffsetChannelMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Symmetric | 0 | Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on either side of the reference channel is specified by the SetNumberOfOffsets(string, int) method. In symmetric mode, the Center Frequency method specifies the frequency of the reference channel, expressed in Hz. |
| InBand | 1 | Specifies that the measurement is performed over all the channels as specified by the standard. For BR and EDR packets, 79 channels starting from 2.402GHz to 2.48GHz are used for the measurement. For LE packets, 81 channels starting from 2.401GHz to 2.481GHz are used for the measurement. In In-band mode, the Center Frequency method specifies the frequency of acquisition which must be equal to 2.441GHz. Configure the SetChannelNumber(string, int) method to specify the frequency of the reference channel. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpresults-fetchabsolutepowertrace__string-double-ref.html language=enus -->
## TOPIC 00053: FetchAbsolutePowerTrace(string, double, ref Spectrum< float >)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpresults-fetchabsolutepowertrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpresults-fetchabsolutepowertrace__string-double-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute power trace for ACP measurement.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchAbsolutePowerTrace(string selectorString, double timeout, ref Spectrum< float > absolutePower)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of

### FetchAbsolutePowerTrace(string, double, ref Spectrum< float >)

Fetches the absolute power trace for ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchAbsolutePowerTrace(string selectorString, double timeout, ref Spectrum< float > absolutePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absolutePower | ref Spectrum< float > | Upon return, contains the absolute power trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxacpresults-fetchmeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00054: FetchMeasurementStatus(string, double, out RFmxBTMXAcpResultsMeasurementStatus)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxacpresults-fetchmeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxacpresults-fetchmeasurementstatus__string-double-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall ACP measurement status based on the measurement limits as defined by the standard if you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method is not valid if you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method

### FetchMeasurementStatus(string, double, out RFmxBTMXAcpResultsMeasurementStatus)

Fetches the overall ACP measurement status based on the measurement limits as defined by the standard if you set the [SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode)](nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setoffsetchannelmode__string-rfmxbtmxacpoffsetchannelmode.html) method to [InBand](nationalinstruments-rfmx-btmx-rfmxbtmxacpoffsetchannelmode.html). This method is not valid if you set the [SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode)](nationalinstruments-rfmx-btmx-rfmxbtmxacpconfiguration-setoffsetchannelmode__string-rfmxbtmxacpoffsetchannelmode.html) method to [Symmetric](nationalinstruments-rfmx-btmx-rfmxbtmxacpoffsetchannelmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchMeasurementStatus(string selectorString, double timeout, out RFmxBTMXAcpResultsMeasurementStatus measurementStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxBTMXAcpResultsMeasurementStatus | Upon return, contains the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. Refer to NationalInstruments.RFmx.BTMX.RFmxBTMXAcpResults.GetMeasurementStatus(string,NationalInstruments.RFmx.BTMX.RFmxBTMXAcpResultsMeasurementStatus@) method for more information about measurement status. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXAcpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxautopreambledetectionenabled.html language=enus -->
## TOPIC 00055: RFmxBTMXAutoPreambleDetectionEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxautopreambledetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxautopreambledetectionenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the auto-detection of preamble field in the packet. When AutoPreamble Detection Enabled method is set to True, the measurement auto detects the LTS field of the PacketTypeLEHdt packet and ignores SetZadoffChuIndex(string, int) method. This method is applicable only when y

### RFmxBTMXAutoPreambleDetectionEnabled Enumeration

Specifies whether to enable the auto-detection of preamble field in the packet. When AutoPreamble Detection Enabled method is set to True, the measurement auto detects the LTS field of the [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html) packet and ignores [SetZadoffChuIndex(string, int)](nationalinstruments-rfmx-btmx-rfmxbtmx-setzadoffchuindex__string-int.html) method. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXAutoPreambleDetectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that the measurement does not perform auto-detection on the preamble of the packet. |
| True | 1 | Specifies that the measurement auto detects the LTS field of the LE-HDT packet and ignores SetZadoffChuIndex(string, int) method. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi0.html language=enus -->
## TOPIC 00056: DioPfi0

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi0.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi0

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi1.html language=enus -->
## TOPIC 00057: DioPfi1

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi1.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi1

### DioPfi1

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi1

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi2.html language=enus -->
## TOPIC 00058: DioPfi2

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi2.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi2

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi3.html language=enus -->
## TOPIC 00059: DioPfi3

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi3.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi3

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi4.html language=enus -->
## TOPIC 00060: DioPfi4

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi4.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi4

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi5.html language=enus -->
## TOPIC 00061: DioPfi5

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi5.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi5

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi6.html language=enus -->
## TOPIC 00062: DioPfi6

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi6.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi6

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi7.html language=enus -->
## TOPIC 00063: DioPfi7

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-diopfi7.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string DioPfi7

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pulsein.html language=enus -->
## TOPIC 00064: PulseIn

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pulsein.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string PulseIn

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00065: PxiTriggerLine5

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline5.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00066: PxiTriggerLine6

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline6.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00067: PxiTriggerLine7

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-pxitriggerline7.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants-timerevent.html language=enus -->
## TOPIC 00068: TimerEvent

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants-timerevent.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public const string TimerEvent

Parent topic:

RFmxBTMXConstants Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxconstants.html language=enus -->
## TOPIC 00069: RFmxBTMXConstants Class

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxconstants.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.BTMXpublic class RFmxBTMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 0. Pfi1The signal is exported to the PXI 1. PulseInPxi

### RFmxBTMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public class RFmxBTMXConstants

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

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrange.html language=enus -->
## TOPIC 00070: RFmxBTMXFrequencyRange Class

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrange.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the FrequencyRange measurement. Derives fromRFmxBTMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.BTMXpublic class RFmxBTMXFrequencyRange : RFmxBTMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxBTMXFrequencyRangeConfiguration instance that provides methods to configure

### RFmxBTMXFrequencyRange Class

Represents the FrequencyRange measurement.

#### Derives from

- RFmxBTMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public class RFmxBTMXFrequencyRange : RFmxBTMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxBTMXFrequencyRangeConfiguration instance that provides methods to configure the FrequencyRange measurement. |
| Results | Gets the RFmxBTMXFrequencyRangeResults instance that provides methods to fetch and read the FrequencyRange measurement results. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeaveragingenabled.html language=enus -->
## TOPIC 00071: RFmxBTMXFrequencyRangeAveragingEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the FrequencyRange measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXFrequencyRangeAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The FrequencyRange measurement uses th

### RFmxBTMXFrequencyRangeAveragingEnabled Enumeration

Specifies whether to enable averaging for the FrequencyRange measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXFrequencyRangeAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The FrequencyRange measurement uses the SetAveragingCount(string, int) method as the number of acquisitions over which the FrequencyRange measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00072: GetAveragingEnabled(string, out RFmxBTMXFrequencyRangeAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the FrequencyRange measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingEnabled(string selectorString, out RFmxBTMXFrequencyRangeAveragingEnabled value)RemarksThis method gets the value of FrequencyRangeAveragingEnabled attribute.The

### GetAveragingEnabled(string, out RFmxBTMXFrequencyRangeAveragingEnabled)

Gets whether to enable averaging for the FrequencyRange measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxBTMXFrequencyRangeAveragingEnabled value)

#### Remarks

This method gets the value of [FrequencyRangeAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXFrequencyRangeAveragingEnabled | Upon return, contains whether to enable averaging for the FrequencyRange measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00073: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. This measurement is valid only for basic rate (BR) packets. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetMeasurementEnabled(string selectorString, out bo

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the *Bluetooth Test Specification RF.TS.p33*. This measurement is valid only for basic rate (BR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [FrequencyRangeMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. This measurement is valid only for basic rate (BR) packets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00074: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system re

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [FrequencyRangeNumberOfAnalysisThreads](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getspan__string-out.html language=enus -->
## TOPIC 00075: GetSpan(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getspan__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-getspan__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10

### GetSpan(string, out double)

Gets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the *Bluetooth Test Specification RF.TS.p33*. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetSpan(string selectorString, out double value)

#### Remarks

This method gets the value of [FrequencyRangeSpan](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00076: SetAveragingCount(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of Fre

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxBTMXFrequencyRangeAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setaveragingenabled__string-rfmxbtmxfrequencyrangeaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [FrequencyRangeAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00077: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. This measurement is valid only for basic rate (BR) packets. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetMeasurementEnabled(string selectorString, bool v

### SetMeasurementEnabled(string, bool)

Sets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the *Bluetooth Test Specification RF.TS.p33*. This measurement is valid only for basic rate (BR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [FrequencyRangeMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. This measurement is valid only for basic rate (BR) packets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setspan__string-double.html language=enus -->
## TOPIC 00078: SetSpan(string, double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setspan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxfrequencyrangeconfiguration-setspan__string-double.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10

### SetSpan(string, double)

Sets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the *Bluetooth Test Specification RF.TS.p33*. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetSpan(string selectorString, double value)

#### Remarks

This method sets the value of [FrequencyRangeSpan](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXFrequencyRangeConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxhighdatathroughputpacketformat.html language=enus -->
## TOPIC 00079: RFmxBTMXHighDataThroughputPacketFormat Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxhighdatathroughputpacketformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxhighdatathroughputpacketformat.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXHighDataThroughputPacketFormatMembersNameValueDescriptionSh

### RFmxBTMXHighDataThroughputPacketFormat Enumeration

Specifies the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the [SetPacketType(string, RFmxBTMXPacketType)](nationalinstruments-rfmx-btmx-rfmxbtmx-setpackettype__string-rfmxbtmxpackettype.html) method to [PacketTypeLEHdt](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXHighDataThroughputPacketFormat

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ShortFormat | 0 | Specifies that the HDT packet format is Short Format. This packet consists of preamble and control header field. |
| Format0 | 1 | Specifies that the HDT packet format is Format0. This packet consists of preamble, control header, PDU header and payload field. The maximum payload length is 510 bytes. |
| Format1 | 2 | Specifies that the HDT packet format is Format1. This packet format is similar to the Format0 but its payload zone consists of multiple blocks and the maximum payload length per payload is 8191 bytes. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00080: RFmxBTMXIQPowerEdgeTriggerSlope Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxiqpoweredgetriggerslope.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) m

### RFmxBTMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the [SetTriggerType(string, RFmxBTMXTriggerType)](nationalinstruments-rfmx-btmx-rfmxbtmx-settriggertype__string-rfmxbtmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-btmx-rfmxbtmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXIQPowerEdgeTriggerSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccburstsynchronizationtype.html language=enus -->
## TOPIC 00081: RFmxBTMXModAccBurstSynchronizationType Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccburstsynchronizationtype.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of synchronization used for detecting the start of packet in ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXModAccBurstSynchronizationTypeMembersNameValueDescriptionNone0Specifies that the measurement does not perform synchronization to detec

### RFmxBTMXModAccBurstSynchronizationType Enumeration

Specifies the type of synchronization used for detecting the start of packet in ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXModAccBurstSynchronizationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble | 1 | Specifies that the measurement uses the preamble field to detect the start of the packet. |
| SyncWord | 2 | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the SetBDAddressLap(string, int) method. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00082: GetAveragingCount(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of ModAccA

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getfrequencytrackingenabled__string-out.html language=enus -->
## TOPIC 00083: GetFrequencyTrackingEnabled(string, out RFmxBTMXModAccFrequencyTrackingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getfrequencytrackingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getfrequencytrackingenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetFrequency

### GetFrequencyTrackingEnabled(string, out RFmxBTMXModAccFrequencyTrackingEnabled)

Gets whether to enable frequency tracking for LE- HDT packet. If you set this method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html), the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetFrequencyTrackingEnabled(string selectorString, out RFmxBTMXModAccFrequencyTrackingEnabled value)

#### Remarks

This method gets the value of [ModAccFrequencyTrackingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXModAccFrequencyTrackingEnabled | Upon return, contains whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getiqmismatchcorrectionenabled__string-out.html language=enus -->
## TOPIC 00084: GetIQMismatchCorrectionEnabled(string, out RFmxBTMXModAccIQMismatchCorrectionEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getiqmismatchcorrectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-getiqmismatchcorrectionenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetIQMismatchCorrectionEnabled(string selectorS

### GetIQMismatchCorrectionEnabled(string, out RFmxBTMXModAccIQMismatchCorrectionEnabled)

Gets whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html), the EVM results are computed after correcting for the IQ gain imbalance and quadrature error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetIQMismatchCorrectionEnabled(string selectorString, out RFmxBTMXModAccIQMismatchCorrectionEnabled value)

#### Remarks

This method gets the value of [ModAccIQMismatchCorrectionEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXModAccIQMismatchCorrectionEnabled | Upon return, contains whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html language=enus -->
## TOPIC 00085: SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingEnabled(string selectorString, RFmxBTMXModAccAveragingEnabled value)RemarksThis method sets the value of ModAccAveragingEnabled attribute.The default value is False.Para

### SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)

Sets whether to enable averaging for the ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingEnabled(string selectorString, RFmxBTMXModAccAveragingEnabled value)

#### Remarks

This method sets the value of [ModAccAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXModAccAveragingEnabled | Specifies whether to enable averaging for the ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setfrequencytrackingenabled__string-rfmxbtmxmodaccfrequencytrackingenabled.html language=enus -->
## TOPIC 00086: SetFrequencyTrackingEnabled(string, RFmxBTMXModAccFrequencyTrackingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setfrequencytrackingenabled__string-rfmxbtmxmodaccfrequencytrackingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setfrequencytrackingenabled__string-rfmxbtmxmodaccfrequencytrackingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetFrequency

### SetFrequencyTrackingEnabled(string, RFmxBTMXModAccFrequencyTrackingEnabled)

Sets whether to enable frequency tracking for LE- HDT packet. If you set this method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html), the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetFrequencyTrackingEnabled(string selectorString, RFmxBTMXModAccFrequencyTrackingEnabled value)

#### Remarks

This method sets the value of [ModAccFrequencyTrackingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXModAccFrequencyTrackingEnabled | Specifies whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setiqmismatchcorrectionenabled__string-rfmxbtmxmodacciqmismatchcorrectionenabled.html language=enus -->
## TOPIC 00087: SetIQMismatchCorrectionEnabled(string, RFmxBTMXModAccIQMismatchCorrectionEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setiqmismatchcorrectionenabled__string-rfmxbtmxmodacciqmismatchcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setiqmismatchcorrectionenabled__string-rfmxbtmxmodacciqmismatchcorrectionenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetIQMismatchCorrectionEnabled(string selectorS

### SetIQMismatchCorrectionEnabled(string, RFmxBTMXModAccIQMismatchCorrectionEnabled)

Sets whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html), the EVM results are computed after correcting for the IQ gain imbalance and quadrature error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetIQMismatchCorrectionEnabled(string selectorString, RFmxBTMXModAccIQMismatchCorrectionEnabled value)

#### Remarks

This method sets the value of [ModAccIQMismatchCorrectionEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXModAccIQMismatchCorrectionEnabled | Specifies whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html language=enus -->
## TOPIC 00088: RFmxBTMXModAccFrequencyTrackingEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccfrequencytrackingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBT

### RFmxBTMXModAccFrequencyTrackingEnabled Enumeration

Specifies whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXModAccFrequencyTrackingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the frequency tracking for LE-HDT packets. |
| True | 1 | Enables the frequency tracking for LE-HDT packets. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html language=enus -->
## TOPIC 00089: RFmxBTMXModAccIQMismatchCorrectionEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodacciqmismatchcorrectionenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXModAccIQMismatchCorrectionEnabled

### RFmxBTMXModAccIQMismatchCorrectionEnabled Enumeration

Specifies whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXModAccIQMismatchCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the IQ mismatch correction for LE-HDT packets. |
| True | 1 | Enables the IQ mismatch correction for LE-HDT packets. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdevmphaseerror__string-double-out-out.html language=enus -->
## TOPIC 00090: FetchDevmPhaseError(string, double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdevmphaseerror__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdevmphaseerror__string-double-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchDevmPhaseError(string selectorString, double timeout, out double averageRmsPhaseErrorMean, out double peakRmsPhaseErrorMaximum)Param

### FetchDevmPhaseError(string, double, out double, out double)

Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchDevmPhaseError(string selectorString, double timeout, out double averageRmsPhaseErrorMean, out double peakRmsPhaseErrorMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| averageRmsPhaseErrorMean | out double | Upon return, contains the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
| peakRmsPhaseErrorMaximum | out double | Upon return, contains the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf1__string-double-out-out.html language=enus -->
## TOPIC 00091: FetchDf1(string, double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf1__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf1__string-double-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchDf1(string selectorString, double timeout, out double df1avgMaximum, out double df1avgMinimum)ParametersNameTypeDescr

### FetchDf1(string, double, out double, out double)

Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchDf1(string selectorString, double timeout, out double df1avgMaximum, out double df1avgMinimum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| df1avgMaximum | out double | Upon return, contains the df1avg value computed on the signal. This value is expressed in Hz. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df1avg results computed for each averaging count. |
| df1avgMinimum | out double | Upon return, contains the df1avg value computed on the signal. This value is expressed in Hz. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf2maxtrace__string-double-ref-ref.html language=enus -->
## TOPIC 00092: FetchDf2maxTrace(string, double, ref float[], ref float[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf2maxtrace__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf2maxtrace__string-double-ref-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the df2max versus the time trace. This method is valid only for basic rate (BR) and low energy (LE) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchDf2maxTrace(string selectorString, double timeout, ref float[] time, ref float[] df2max)ParametersNameTypeDescriptionselec

### FetchDf2maxTrace(string, double, ref float[], ref float[])

Fetches the df2max versus the time trace. This method is valid only for basic rate (BR) and low energy (LE) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchDf2maxTrace(string selectorString, double timeout, ref float[] time, ref float[] df2max)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| time | ref float[] | Upon return, contains the array of time instances at which the df2max values are computed. This value is expressed in seconds. |
| df2max | ref float[] | Upon return, contains the array of df2max values computed over the packet at each time instance. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf4avgtrace__string-double-ref-ref.html language=enus -->
## TOPIC 00093: FetchDf4avgTrace(string, double, ref float[], ref float[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf4avgtrace__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchdf4avgtrace__string-double-ref-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the df4avg versus the time trace. This function is valid only for LE-CS Packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchDf4avgTrace(string selectorString, double timeout, ref float[] time, ref float[] df4avg)ParametersNameTypeDescriptionselectorStringstringSpecifies a s

### FetchDf4avgTrace(string, double, ref float[], ref float[])

Fetches the df4avg versus the time trace. This function is valid only for LE-CS Packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchDf4avgTrace(string selectorString, double timeout, ref float[] time, ref float[] df4avg)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| time | ref float[] | Upon return, contains the array of time instances at which the df4avg values are computed. This value is expressed in seconds. |
| df4avg | ref float[] | Upon return, contains the array of df4avg values computed over the packet at each time instance. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchevmpersymboltrace__string-double-ref.html language=enus -->
## TOPIC 00094: FetchEvmPerSymbolTrace(string, double, ref float[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchevmpersymboltrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchevmpersymboltrace__string-double-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. This method is valid only for LE-HDT packet.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchEvmPerSymbolTrace(string selectorString, double timeout, ref float[] evmPerSymbol)P

### FetchEvmPerSymbolTrace(string, double, ref float[])

Fetches the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. This method is valid only for LE-HDT packet.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchEvmPerSymbolTrace(string selectorString, double timeout, ref float[] evmPerSymbol)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| evmPerSymbol | ref float[] | Upon return, contains the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. The values are expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrorbr__string-double-out-out-out.html language=enus -->
## TOPIC 00095: FetchFrequencyErrorBR(string, double, out double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrorbr__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrorbr__string-double-out-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for basic rate (BR) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchFrequencyErrorBR(string selectorString, double timeout, out double initialFrequencyErrorMaximum, out double peakFrequencyDriftMaximum, out double peakFrequencyDriftRateM

### FetchFrequencyErrorBR(string, double, out double, out double, out double)

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchFrequencyErrorBR(string selectorString, double timeout, out double initialFrequencyErrorMaximum, out double peakFrequencyDriftMaximum, out double peakFrequencyDriftRateMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| initialFrequencyErrorMaximum | out double | Upon return, contains the initial frequency error value computed on the preamble of the BR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, value corresponding to the maximum of absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyDriftMaximum | out double | Upon return, contains the peak frequency drift value computed on the BR packet. When you set the ModAcc Averaging Enabled method to SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyDriftRateMaximum | out double | Upon return, contains the peak frequency drift rate value computed on the BR packet. When you set the ModAcc Averaging Enabled method to SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerroredr__string-double-out-out-out.html language=enus -->
## TOPIC 00096: FetchFrequencyErrorEdr(string, double, out double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerroredr__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerroredr__string-double-out-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchFrequencyErrorEdr(string selectorString, double timeout, out double headerFrequencyErrorWiMaximum, out double peakFrequencyErrorWiPlusW0Maximum, out d

### FetchFrequencyErrorEdr(string, double, out double, out double, out double)

Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchFrequencyErrorEdr(string selectorString, double timeout, out double headerFrequencyErrorWiMaximum, out double peakFrequencyErrorWiPlusW0Maximum, out double peakFrequencyErrorW0Maximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| headerFrequencyErrorWiMaximum | out double | Upon return, contains the frequency error value computed on the header of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyErrorWiPlusW0Maximum | out double | Upon return, contains the peak frequency error value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyErrorW0Maximum | out double | Upon return, contains the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrortracele__string-double-ref-ref.html language=enus -->
## TOPIC 00097: FetchFrequencyErrorTraceLE(string, double, ref float[], ref float[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrortracele__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrortracele__string-double-ref-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchFrequencyErrorTraceLE(string selectorString, double timeout, ref float[] time, ref float[] frequencyError)ParametersNameTypeDesc

### FetchFrequencyErrorTraceLE(string, double, ref float[], ref float[])

Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchFrequencyErrorTraceLE(string selectorString, double timeout, ref float[] time, ref float[] frequencyError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| time | ref float[] | Upon return, contains an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. |
| frequencyError | ref float[] | Returns the array of frequency errors computed over the packet. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrorwiplusw0traceedr__string-double-ref-ref.html language=enus -->
## TOPIC 00098: FetchFrequencyErrorWiPlusW0TraceEdr(string, double, ref float[], ref float[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrorwiplusw0traceedr__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchfrequencyerrorwiplusw0traceedr__string-double-ref-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchFrequencyErrorWiPlusW0TraceEdr(string selectorString, double timeout, ref float[] time, ref float[] frequencyErrorWiPlusW0)ParametersNameTypeDescriptionselector

### FetchFrequencyErrorWiPlusW0TraceEdr(string, double, ref float[], ref float[])

Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchFrequencyErrorWiPlusW0TraceEdr(string selectorString, double timeout, ref float[] time, ref float[] frequencyErrorWiPlusW0)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| time | ref float[] | Upon return, contains an array of time instances corresponding to the start of the 50us blocks of the EDR portion of EDR packet at which the frequency error values are computed. This value is expressed in seconds. |
| frequencyErrorWiPlusW0 | ref float[] | Returns the array of frequency errors wi+w0 computed over the packet. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchrmsdevmtrace__string-double-ref.html language=enus -->
## TOPIC 00099: FetchRmsDevmTrace(string, double, ref float[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchrmsdevmtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-fetchrmsdevmtrace__string-double-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This method is valid only for enhanced data rate (EDR) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchRmsDevmTrace(string selectorString, double timeout, ref float[] rmsDevm)ParametersNameTypeDescri

### FetchRmsDevmTrace(string, double, ref float[])

Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This method is valid only for enhanced data rate (EDR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchRmsDevmTrace(string selectorString, double timeout, ref float[] rmsDevm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| rmsDevm | ref float[] | Upon return, contains the array of RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. This value is expressed in percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-get99percentdevm__string-out.html language=enus -->
## TOPIC 00100: Get99PercentDevm(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-get99percentdevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-get99percentdevm__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int Get99PercentDevm(string selectorString, out double value)RemarksThis me

### Get99PercentDevm(string, out double)

Gets the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int Get99PercentDevm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResults99PercentDevm](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getaveragermsmagnitudeerrormean__string-out.html language=enus -->
## TOPIC 00101: GetAverageRmsMagnitudeErrorMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getaveragermsmagnitudeerrormean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getaveragermsmagnitudeerrormean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging cou

### GetAverageRmsMagnitudeErrorMean(string, out double)

Gets the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAverageRmsMagnitudeErrorMean(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsAverageRmsMagnitudeErrorMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getfractionaltimeoffsetmean__string-out.html language=enus -->
## TOPIC 00102: GetFractionalTimeOffsetMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getfractionaltimeoffsetmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getfractionaltimeoffsetmean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetFractionalTimeOffsetMean(string selectorString, out double value)

### GetFractionalTimeOffsetMean(string, out double)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetFractionalTimeOffsetMean(string selectorString, out double value)

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getfrequencyerrorw0plusw1maximum__string-out.html language=enus -->
## TOPIC 00103: GetFrequencyErrorW0PlusW1Maximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getfrequencyerrorw0plusw1maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getfrequencyerrorw0plusw1maximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total frequency error for the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute frequency error values computed for each averaging count. This value is expressed in Hz.

### GetFrequencyErrorW0PlusW1Maximum(string, out double)

Gets the total frequency error for the LE-HDT packet. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns a value corresponding to the maximum of the absolute frequency error values computed for each averaging count. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetFrequencyErrorW0PlusW1Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsFrequencyErrorW0PlusW1Maximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the total frequency error for the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute frequency error values computed for each averaging count. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getiqgainimbalancemean__string-out.html language=enus -->
## TOPIC 00104: GetIQGainImbalanceMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getiqgainimbalancemean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getiqgainimbalancemean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the IQ gain imbalance estimated over preamble portion of the LE-HDT packets. This value is expressed in dB. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the IQ gain imbalance values computed for each averaging count. SyntaxN

### GetIQGainImbalanceMean(string, out double)

Gets the IQ gain imbalance estimated over preamble portion of the LE-HDT packets. This value is expressed in dB. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns the mean of the IQ gain imbalance values computed for each averaging count.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetIQGainImbalanceMean(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsIQGainImbalanceMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the IQ gain imbalance estimated over preamble portion of the LE-HDT packets. This value is expressed in dB. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the IQ gain imbalance values computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpayloadfrequencyerrorw1maximum__string-out.html language=enus -->
## TOPIC 00105: GetPayloadFrequencyErrorW1Maximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpayloadfrequencyerrorw1maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpayloadfrequencyerrorw1maximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency error value computed on the payload portion of the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute payload frequency error values computed for each averaging

### GetPayloadFrequencyErrorW1Maximum(string, out double)

Gets the frequency error value computed on the payload portion of the LE-HDT packet. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns a value corresponding to the maximum of the absolute payload frequency error values computed for each averaging count. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPayloadFrequencyErrorW1Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPayloadFrequencyErrorW1Maximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the frequency error value computed on the payload portion of the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute payload frequency error values computed for each averaging count. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpeakrmsmagnitudeerrormaximum__string-out.html language=enus -->
## TOPIC 00106: GetPeakRmsMagnitudeErrorMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpeakrmsmagnitudeerrormaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpeakrmsmagnitudeerrormaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.

### GetPeakRmsMagnitudeErrorMaximum(string, out double)

Gets the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPeakRmsMagnitudeErrorMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPeakRmsMagnitudeErrorMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpeakrmsphaseerrormaximum__string-out.html language=enus -->
## TOPIC 00107: GetPeakRmsPhaseErrorMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpeakrmsphaseerrormaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpeakrmsphaseerrormaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This

### GetPeakRmsPhaseErrorMaximum(string, out double)

Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPeakRmsPhaseErrorMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPeakRmsPhaseErrorMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpercentageofsymbolsbelow99percentdevmlimit__string-out.html language=enus -->
## TOPIC 00108: GetPercentageOfSymbolsBelow99PercentDevmLimit(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpercentageofsymbolsbelow99percentdevmlimit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpercentageofsymbolsbelow99percentdevmlimit__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification RF.TS.p33. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnab

### GetPercentageOfSymbolsBelow99PercentDevmLimit(string, out double)

Gets the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the *Bluetooth Test Specification RF.TS.p33*. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it computes this result using the symbol differential EVM (DEVM) values from all averaging counts. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPercentageOfSymbolsBelow99PercentDevmLimit(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPercentageOfSymbolsBelow99PercentDevmLimit](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification v5.1.0. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the symbol differential EVM (DEVM) values from all averaging counts. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpreamblefrequencyerrorw0maximum__string-out.html language=enus -->
## TOPIC 00109: GetPreambleFrequencyErrorW0Maximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpreamblefrequencyerrorw0maximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodaccresults-getpreamblefrequencyerrorw0maximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency error value computed on the preamble portion of the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute preamble frequency error values computed for each averagi

### GetPreambleFrequencyErrorW0Maximum(string, out double)

Gets the frequency error value computed on the preamble portion of the LE-HDT packet. When you set the [SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccconfiguration-setaveragingenabled__string-rfmxbtmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodaccaveragingenabled.html), it returns a value corresponding to the maximum of the absolute preamble frequency error values computed for each averaging count. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPreambleFrequencyErrorW0Maximum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPreambleFrequencyErrorW0Maximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the frequency error value computed on the preamble portion of the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute preamble frequency error values computed for each averaging count. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModAccResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumburstsynchronizationtype.html language=enus -->
## TOPIC 00110: RFmxBTMXModSpectrumBurstSynchronizationType Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumburstsynchronizationtype.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXModSpectrumBurstSynchronizationTypeMembersNameValueDescriptionNone0Specifies that the measurement does not perform synchroniz

### RFmxBTMXModSpectrumBurstSynchronizationType Enumeration

Specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXModSpectrumBurstSynchronizationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble | 1 | Specifies that the measurement uses the preamble field to detect the start of the packet. |
| SyncWord | 2 | Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00111: GetAveragingCount(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the ModSpectrumAveragingEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of ModSpectrumAveragingCount attribute.The

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [ModSpectrumAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [ModSpectrumAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the ModSpectrumAveragingEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModSpectrumConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00112: GetAveragingEnabled(string, out RFmxBTMXModSpectrumAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for ModSpectrum measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingEnabled(string selectorString, out RFmxBTMXModSpectrumAveragingEnabled value)RemarksThis method gets the value of ModSpectrumAveragingEnabled attribute.The default valu

### GetAveragingEnabled(string, out RFmxBTMXModSpectrumAveragingEnabled)

Gets whether to enable averaging for ModSpectrum measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxBTMXModSpectrumAveragingEnabled value)

#### Remarks

This method gets the value of [ModSpectrumAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXModSpectrumAveragingEnabled | Upon return, contains whether to enable averaging for ModSpectrum measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModSpectrumConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00113: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxmodspectrumconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable all the traces used for ModSpectrum measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of ModSpectrumAllTracesEnabled attribute.The default value is FALSE.ParametersName

### SetAllTracesEnabled(string, bool)

Sets whether to enable all the traces used for ModSpectrum measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ModSpectrumAllTracesEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable all the traces used for ModSpectrum measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXModSpectrumConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampaveragingenabled.html language=enus -->
## TOPIC 00114: RFmxBTMXPowerRampAveragingEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXPowerRampAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement uses the PowerRampAveragingCount met

### RFmxBTMXPowerRampAveragingEnabled Enumeration

Specifies whether to enable averaging for PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXPowerRampAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement uses the PowerRampAveragingCount method as the number of acquisitions over which the PowerRamp measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00115: GetAveragingEnabled(string, out RFmxBTMXPowerRampAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingEnabled(string selectorString, out RFmxBTMXPowerRampAveragingEnabled value)RemarksThis method gets the value of PowerRampAveragingEnabled attribute.The default value is Fa

### GetAveragingEnabled(string, out RFmxBTMXPowerRampAveragingEnabled)

Gets whether to enable averaging for PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxBTMXPowerRampAveragingEnabled value)

#### Remarks

This method gets the value of [PowerRampAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXPowerRampAveragingEnabled | Upon return, contains whether to enable averaging for PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getburstsynchronizationtype__string-out.html language=enus -->
## TOPIC 00116: GetBurstSynchronizationType(string, out RFmxBTMXPowerRampBurstSynchronizationType)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getburstsynchronizationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getburstsynchronizationtype__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of synchronization used for detecting the start of packet in the PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetBurstSynchronizationType(string selectorString, out RFmxBTMXPowerRampBurstSynchronizationType value)RemarksThis method gets the value of P

### GetBurstSynchronizationType(string, out RFmxBTMXPowerRampBurstSynchronizationType)

Gets the type of synchronization used for detecting the start of packet in the PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetBurstSynchronizationType(string selectorString, out RFmxBTMXPowerRampBurstSynchronizationType value)

#### Remarks

This method gets the value of [PowerRampBurstSynchronizationType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Preamble](nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampburstsynchronizationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXPowerRampBurstSynchronizationType | Upon return, contains the type of synchronization used for detecting the start of packet in the PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00117: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of PowerRampMeasurementEnabled attri

### GetMeasurementEnabled(string, out bool)

Gets whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [PowerRampMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00118: SetAveragingCount(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the PowerRampAveragingEnabledmethod to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of PowerRampAveragingCount attribute.The default

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [PowerRampAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html)method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [PowerRampAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the PowerRampAveragingEnabled method to True . |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setaveragingenabled__string-rfmxbtmxpowerrampaveragingenabled.html language=enus -->
## TOPIC 00119: SetAveragingEnabled(string, RFmxBTMXPowerRampAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setaveragingenabled__string-rfmxbtmxpowerrampaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setaveragingenabled__string-rfmxbtmxpowerrampaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for PowerRamp measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingEnabled(string selectorString, RFmxBTMXPowerRampAveragingEnabled value)RemarksThis method sets the value of PowerRampAveragingEnabled attribute.The default value is False.

### SetAveragingEnabled(string, RFmxBTMXPowerRampAveragingEnabled)

Sets whether to enable averaging for PowerRamp measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingEnabled(string selectorString, RFmxBTMXPowerRampAveragingEnabled value)

#### Remarks

This method sets the value of [PowerRampAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXPowerRampAveragingEnabled | Specifies whether to enable averaging for PowerRamp measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00120: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpowerrampconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of PowerRampMeasurementEnabled attribute

### SetMeasurementEnabled(string, bool)

Sets whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [PowerRampMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXPowerRampConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html language=enus -->
## TOPIC 00121: RFmxBTMXPropertyId Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXPropertyIdMembersNameValueDescriptionSelectedPorts11538429Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port name

### RFmxBTMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SelectedPorts | 11538429 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| CenterFrequency | 11534337 | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| ReferenceLevel | 11534338 | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ExternalAttenuation | 11534339 | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
| ReferenceLevelHeadroom | 11538428 | Specifies the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| TriggerType | 11534340 | Specifies the type of trigger to be used for signal acquisition. |
| DigitalEdgeTriggerSource | 11534341 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to DigitalEdge. |
| DigitalEdgeTriggerEdge | 11534342 | Specifies the active edge for the trigger. This method is valid only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to DigitalEdge. |
| IQPowerEdgeTriggerSource | 11534343 | Specifies the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerLevel | 11534344 | Specifies the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. |
| IQPowerEdgeTriggerLevelType | 11538431 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerSlope | 11534345 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to IQPowerEdge. |
| TriggerDelay | 11534346 | Specifies the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
| TriggerMinimumQuietTimeMode | 11534347 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 11534348 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| PacketType | 11534349 | Specifies the type of the Bluetooth packet to be measured. |
| DataRate | 11534350 | Specifies the data rate of the LE, LE-CS or LE-HDT packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable only to LE, LE-CS or LE-HDT packet type. |
| BandwidthBitPeriodProduct | 11534388 | Specifies the bandwidth bit period product of GFSK modulation for LE-CS packet type. |
| BDAddressLap | 11534351 | Specifies the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |
| AccessAddress | 11534353 | Specifies the 32-bit LE access address. |
| PayloadBitPattern | 11534354 | Specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. Refer to the Payload Bit Pattern property that lists the measurements that are applicable for different payload bit patterns. |
| PayloadLengthMode | 11534355 | Specifies the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(string, int) properties decide the length of the payload to be used for measurement. |
| PayloadLength | 11534356 | Specifies the payload length of BR, EDR, LE and LE-CS packet, and the payload zone length of LE-HDT packet, in bytes. This method is applicable only when you set the SetPayloadLengthMode(string, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length or payload zone length used for measurement if you set the Payload Length Mode method to Auto. |
| DirectionFindingMode | 11534380 | Specifies the mode of direction finding. |
| CteLength | 11534381 | Specifies the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |
| CteSlotDuration | 11534382 | Specifies the length of the transmit slots and sampling slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
| CteNumberOfTransmitSlots | 11534383 | Returns the number of transmit slots in the constant time extension portion of the generated LE packet. This method is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
| ChannelSoundingPacketFormat | 11534384 | Specifies the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS. |
| ChannelSoundingSyncSequence | 11534385 | Specifies the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
| ChannelSoundingPhaseMeasurementPeriod | 11534386 | Specifies the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
| ChannelSoundingToneExtensionSlot | 11534387 | Specifies whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
| ChannelSoundingNumberOfAntennaPath | 11534390 | Specifies the number of antenna paths for the generated LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
| ChannelSoundingAntennaSwitchTime | 11534389 | Specifies the Channel Sounding Antenna Switch Time for the LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
| AutoPreambleDetectionEnabled | 11534402 | Specifies whether to enable the auto-detection of preamble field in the packet. When AutoPreamble Detection Enabled method is set to True, the measurement auto detects the LTS field of the PacketTypeLEHdt packet and ignores SetZadoffChuIndex(string, int) method. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |
| ZadoffChuIndex | 11534393 | Specifies Zadoff-Chu Index for the Long Training Sequence in the preamble. Input to the Zadoff-Chu Index method must be in the range of [1 - 16]. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |
| HighDataThroughputPacketFormat | 11534392 | Specifies the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |
| VhdtModeEnabled | 11534400 |  |
| NumberOfBlockRepetitionSequences | 11534401 |  |
| ChannelNumber | 11534359 | Specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
| DetectedPacketType | 11534361 | Returns the packet type detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| DetectedDataRate | 11534378 | Returns the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| DetectedPayloadLength | 11534379 | Returns the payload length detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| DetectedPacketFormat | 11534403 | Returns the LE High Data Throughput (LE HDT) packet format detected by the RFmxBT Auto Detect Signal function. This method returns a valid packet format only if the Detected Packet Type method returns LE-HDT. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
| ModAccMeasurementEnabled | 11550720 | Specifies whether to enable the ModAcc measurements. You can use this method to determine the modulation quality of the bluetooth transmitter. |
| ModAccBurstSynchronizationType | 11550763 | Specifies the type of synchronization used for detecting the start of packet in ModAcc measurement. |
| ModAccIQOriginOffsetCorrectionEnabled | 11550723 | Specifies whether to enable the I/Q origin offset correction for EDR and LE-HDT packets. If you set this method to True, the DEVM and EVM results are computed after correcting for the I/Q origin offset. |
| ModAccIQMismatchCorrectionEnabled | 11550781 | Specifies whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. |
| ModAccFrequencyTrackingEnabled | 11550784 | Specifies whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. |
| ModAccAveragingEnabled | 11550724 | Specifies whether to enable averaging for the ModAcc measurements. |
| ModAccAveragingCount | 11550725 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True. |
| ModAccAllTracesEnabled | 11550726 | Specifies whether to enable all the traces computed by ModAcc measurements. |
| ModAccNumberOfAnalysisThreads | 11550727 | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| ModAccResultsDf1avgMean | 11550729 | Returns the df1avg value computed on the signal. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df1avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf1avgMaximum | 11550730 | Returns the df1avg value computed on the signal. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf1avgMinimum | 11550731 | Returns the df1avg value computed on the signal. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPeakDf1maxMaximum | 11550732 | Returns the peak df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df1max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsMinimumDf1maxMinimum | 11550733 | Returns the minimum df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df1max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPercentageOfSymbolsAboveDf1maxThreshold | 11550764 | Returns the percentage of symbols with df1max values that are greater than the df1max threshold defined by the standard. This result is valid only for the LE packet with a data rate of 125 Kbps. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df1max values from all averaging counts. This value expressed as a percentage. |
| ModAccResultsDf2avgMean | 11550734 | Returns the df2avg value computed on the signal. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf2avgMaximum | 11550735 | Returns the df2avg value computed on the signal. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsDf2avgMinimum | 11550736 | Returns the df2avg value computed on the signal. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPeakDf2maxMaximum | 11550737 | Returns the peak df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df2max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsMinimumDf2maxMinimum | 11550738 | Returns the minimum df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df2max results computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPercentageOfSymbolsAboveDf2maxThreshold | 11550739 | Returns the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. |
| ModAccResultsDf3avgMean | 11550772 | Returns the df3avg value computed on the signal. When you set the ModAccAveragingEnabled method to True, it returns the mean of the df3avg results computed for each averaging count. This value is expressed in Hz. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
| ModAccResultsPercentageOfSymbolsAboveDf4avgThreshold | 11550773 | Returns the percentage of symbols with df4avg values that are greater than the df4avg threshold defined by the standard. When you set the ModAccAveragingEnabled method to True, it computes this result using the df4avg values from all averaging counts. This value is expressed as a percentage. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
| ModAccResultsBRInitialFrequencyErrorMaximum | 11550740 | Returns the initial frequency error value computed on the preamble portion of the BR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsBRPeakFrequencyDriftMaximum | 11550741 | Returns the peak frequency drift value computed on the BR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsBRPeakFrequencyDriftRateMaximum | 11550742 | Returns the peak frequency drift rate value computed on the BR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsEdrHeaderFrequencyErrorWiMaximum | 11550743 | Returns the frequency error value computed on the header of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsEdrPeakFrequencyErrorWiPlusW0Maximum | 11550744 | Returns the peak frequency error value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsEdrPeakFrequencyErrorW0Maximum | 11550745 | Returns the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum absolute of the peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEInitialFrequencyErrorMaximum | 11550769 | Returns the initial frequency error value computed on the preamble portion of the LE or LE-CS packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEPeakFrequencyErrorMaximum | 11550746 | When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to Disabled, it returns the peak frequency error value computed on the LE/LE-CS packet. When you set the Direction Finding Mode method to AngleOfArrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of absolute the peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEInitialFrequencyDriftMaximum | 11550747 | Returns the initial frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEPeakFrequencyDriftMaximum | 11550748 | Returns the peak frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsLEPeakFrequencyDriftRateMaximum | 11550749 | Returns the peak frequency drift rate value computed on the LE packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPreambleFrequencyErrorW0Maximum | 11550778 | Returns the frequency error value computed on the preamble portion of the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute preamble frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPayloadFrequencyErrorW1Maximum | 11550779 | Returns the frequency error value computed on the payload portion of the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute payload frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsFrequencyErrorW0PlusW1Maximum | 11550780 | Returns the total frequency error for the LE-HDT packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute frequency error values computed for each averaging count. This value is expressed in Hz. |
| ModAccResultsPeakRmsDevmMaximum | 11550750 | Returns the peak of the RMS differential EVM (DEVM) values computed on each 50us block of the EDR portion of the EDR packet. When you set SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the aboslute peak RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
| ModAccResultsRmsDevmMean | 11550751 | Returns the RMS differential EVM (DEVM) value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the absolute mean of the RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
| ModAccResultsPeakDevmMaximum | 11550752 | Returns the peak of the differential EVM (DEVM) values computed on symbols in the EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak symbol differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
| ModAccResults99PercentDevm | 11550753 | Returns the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage. |
| ModAccResultsPercentageOfSymbolsBelow99PercentDevmLimit | 11550754 | Returns the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification RF.TS.p33.. This value is expressed as a percentage. |
| ModAccResultsAverageRmsMagnitudeErrorMean | 11550765 | Returns the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage. |
| ModAccResultsPeakRmsMagnitudeErrorMaximum | 11550766 | Returns the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.This value is expressed as a percentage. |
| ModAccResultsAverageRmsPhaseErrorMean | 11550767 | Return the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
| ModAccResultsPeakRmsPhaseErrorMaximum | 11550768 | Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |
| ModAccResultsPreambleRmsEvmMean | 11550774 | Returns the RMS EVM value computed on the preamble portion of the LE-HDT packet. When you set the ModAccAveragingEnabled method to True, it returns the mean of the RMS EVM values computed for each averaging count. This value is expressed in dB. This result is valid only for LE-HDT packet. |
| ModAccResultsControlHeaderRmsEvmMean | 11550775 | Returns the RMS EVM value computed on the control header portion of the LE-HDT packet. When you set the ModAccAveragingEnabled method to True, it returns the mean of the RMS EVM values computed for each averaging count. This value is expressed in dB. This result is valid only for LE-HDT packet. |
| ModAccResultsPayloadRmsEvmMean | 11550776 | Returns the RMS EVM value computed on the payload portion including the payload header of the LE-HDT packet. When you set the ModAccAveragingEnabled method to True, it returns the mean of the RMS EVM values computed for each averaging count. This value is expressed in dB. This result is valid only for LE-HDT packet. |
| ModAccResultsIQOriginOffsetMean | 11550755 | Returns the I/Q origin offset estimated over the EDR portion of the EDR packets and preamble portion of the LE-HDT packets. This value is expressed in dB. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the I/Q origin offset values computed for each averaging count. |
| ModAccResultsIQGainImbalanceMean | 11550782 | Returns the IQ gain imbalance estimated over preamble portion of the LE-HDT packets. This value is expressed in dB. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the IQ gain imbalance values computed for each averaging count. |
| ModAccResultsQuadratureErrorMean | 11550783 | Returns the quadrature error estimated over preamble portion of the LE-HDT packets. This value is expressed in degree. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the quadrature error values computed for each averaging count. |
| ModAccResultsClockDriftMean | 11550770 | Returns the clock drift estimated over the LE-CS packet. This value is expressed in ppm. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the clock drift values computed for each averaging count. |
| ModAccResultsPreambleStartTimeMean | 11550771 | Returns the start time of the preamble of LE-CS packet. This value is expressed in seconds. When you set the SetAveragingEnabled(string, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the preamble start time values computed for each averaging count. |
| ModAccResultsFractionalTimeOffsetMean | 11550777 |  |
| AcpMeasurementEnabled | 11554816 | Specifies whether to enable the ACP measurement. |
| AcpOffsetChannelMode | 11554818 | Specifies which offset channels are used for the measurement. |
| AcpNumberOfOffsets | 11554819 | Specifies the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. This method also returns the actual number of offsets used in the ACP measurement when you set the ACP Offset Channel Mode method to InBand. |
| AcpOffsetFrequency | 11554820 | Returns the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz. |
| AcpReferenceChannelBandwidthMode | 11554838 | This enum value has been deprecated. |
| AcpReferenceChannelBandwidth | 11554837 | This enum value has been deprecated. |
| AcpBurstSynchronizationType | 11554834 | Specifies the type of synchronization used for detecting the start of the EDR packet in the adjacent channel power (ACP) measurement. |
| AcpAveragingEnabled | 11554821 | Specifies whether to enable averaging for the ACP measurement. |
| AcpAveragingCount | 11554822 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXAcpAveragingEnabled) method to True. |
| AcpAllTracesEnabled | 11554823 | Specifies whether to enable all traces for the adjacent channel power (ACP) measurements. |
| AcpNumberOfAnalysisThreads | 11554824 | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
| AcpResultsMeasurementStatus | 11554826 | Indicates the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
| AcpResultsReferenceChannelPower | 11554827 | Returns the power measured over the bandwidth as defined in the Bluetooth standard defined test cases: ACP, EDR In-Band Emission, and LE In-Band Emission at the transmit channel. This value is expressed in dBm. |
| AcpResultsLowerOffsetAbsolutePower | 11554828 | Returns the absolute power measured in the lower offset channel. This value is expressed in dBm. |
| AcpResultsLowerOffsetRelativePower | 11554829 | Returns the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| AcpResultsLowerOffsetMargin | 11554830 | Returns the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the ACP Offset Channel Mode method to Symmetric. |
| AcpResultsUpperOffsetAbsolutePower | 11554831 | Returns the absolute power measured in the upper offset channel. This value is expressed in dBm. |
| AcpResultsUpperOffsetRelativePower | 11554832 | Returns the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| AcpResultsUpperOffsetMargin | 11554833 | Returns the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the ACP Offset Channel Mode method to Symmetric. |
| TwentydBBandwidthMeasurementEnabled | 11542528 | Specifies whether to enable the 20dBBandwidth measurement specified in section 4.5.5 of the Bluetooth Test Specification RF.TS.p33. The measurement uses a span of 3 MHz internally. This measurement is valid only for basic rate (BR) packets. |
| TwentydBBandwidthAveragingEnabled | 11542530 | Specifies whether to enable averaging for the 20dBBandwidth measurement. |
| TwentydBBandwidthAveragingCount | 11542531 | Specifies the number of acquisitions used for averaging when you set the TwentydBBandwidthAveragingEnabled method to True. |
| TwentydBBandwidthAllTracesEnabled | 11542532 | Specifies whether to enable all the traces for the 20dBBandwidth measurement. |
| TwentydBBandwidthNumberOfAnalysisThreads | 11542533 | Specifies the maximum number of threads used for parallelism for the 20dB bandwidth measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| TwentydBBandwidthResultsPeakPower | 11542535 | Returns the peak power of the measured spectrum. This value is expressed in dBm. |
| TwentydBBandwidthResultsBandwidth | 11542536 | Returns the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz. |
| TwentydBBandwidthResultsHighFrequency | 11542537 | Returns the highest frequency above the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
| TwentydBBandwidthResultsLowFrequency | 11542538 | Returns the lowest frequency below the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
| FrequencyRangeMeasurementEnabled | 11546624 | Specifies whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. This measurement is valid only for basic rate (BR) packets. |
| FrequencyRangeSpan | 11546626 | Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |
| FrequencyRangeAveragingEnabled | 11546627 | Specifies whether to enable averaging for the FrequencyRange measurement. |
| FrequencyRangeAveragingCount | 11546628 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |
| FrequencyRangeAllTracesEnabled | 11546629 | Specifies whether to enable all the traces for FrequencyRange measurement. |
| FrequencyRangeNumberOfAnalysisThreads | 11546630 | Specifies the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| FrequencyRangeResultsHighFrequency | 11546632 | Returns the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
| FrequencyRangeResultsLowFrequency | 11546633 | Returns the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
| ModSpectrumMeasurementEnabled | 11595776 | Specifies whether to enable the ModSpectrum measurements.This measurement is valid only for channel sounding (CS) packets. |
| ModSpectrumBurstSynchronizationType | 11595778 | Specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. |
| ModSpectrumAveragingEnabled | 11595779 | Specifies whether to enable averaging for ModSpectrum measurements. |
| ModSpectrumAveragingCount | 11595780 | Specifies the number of acquisitions used for averaging when you set the ModSpectrumAveragingEnabled method to True. |
| ModSpectrumAllTracesEnabled | 11595781 | Specifies whether to enable all the traces used for ModSpectrum measurements. |
| ModSpectrumNumberOfAnalysisThreads | 11595782 | Specifies the maximum number of threads used for parallelism for ModSpectrum measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| ModSpectrumResultsBandwidth | 11595784 | Returns the 6 dB bandwidth of the received signal. It is computed as the difference between ModSpectrumResultsHighFrequency and ModSpectrumResultsLowFrequency . This value is expressed in Hz. |
| ModSpectrumResultsHighFrequency | 11595785 | Returns the highest frequency above the center frequency at which the transmit power drops 6dB below the peak power. This value is expressed in Hz. |
| ModSpectrumResultsLowFrequency | 11595786 | Returns the lowest frequency below the center frequency at which the transmit power drops 6 dB below the peak power. This value is expressed in Hz. |
| TxpMeasurementEnabled | 11538432 | Specifies whether to enable the transmit power (TxP) measurements. |
| TxpBurstSynchronizationType | 11538448 | Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
| TxpAveragingEnabled | 11538434 | Specifies whether to enable averaging for the transmit power (TxP) measurements. |
| TxpAveragingCount | 11538435 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. |
| TxpAllTracesEnabled | 11538436 | Specifies whether to enable all the traces used for transmit power (TxP) measurements. |
| TxpNumberOfAnalysisThreads | 11538437 | Specifies the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| TxpResultsAveragePowerMean | 11538439 | Returns the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count. |
| TxpResultsAveragePowerMaximum | 11538440 | Returns the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsAveragePowerMinimum | 11538441 | Returns the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsPeakPowerMaximum | 11538442 | Returns the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsPeakToAveragePowerRatioMaximum | 11538443 | Returns the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. For LE-HDT, PAPR is calculated using peak power calculated over active portion of burst and average power calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |
| TxpResultsEdrGfskAveragePowerMean | 11538444 | Returns the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsEdrDpskAveragePowerMean | 11538445 | Returns the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsEdrDpskGfskAveragePowerRatioMean | 11538451 | Returns the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |
| TxpResultsLECteReferencePeriodAveragePowerMean | 11538452 | Returns the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsLECteReferencePeriodPeakAbsolutePowerDeviationMaximum | 11538453 | Returns the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
| TxpResultsLECteTransmitSlotAveragePowerMean | 11538454 | Returns the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
| TxpResultsLECteTransmitSlotPeakAbsolutePowerDeviationMaximum | 11538455 | Returns the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
| TxpResultsLECSPhaseMeasurementPeriodAveragePowerMean | 11538456 | Returns the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. When you set the TxpAveragingEnabled method to True, it returns the mean of the phase measurement period average power results computed for each averaging count. This value is expressed in dBm. |
| PowerRampMeasurementEnabled | 11591680 | Specifies whether to enable PowerRamp measurements. This measurement is valid only for low energy CS (LE-CS) packets. |
| PowerRampBurstSynchronizationType | 11591682 | Specifies the type of synchronization used for detecting the start of packet in the PowerRamp measurement. |
| PowerRampAveragingEnabled | 11591685 | Specifies whether to enable averaging for PowerRamp measurement. |
| PowerRampAveragingCount | 11591686 | Specifies the number of acquisitions used for averaging when you set the PowerRampAveragingEnabled method to True. |
| PowerRampNumberOfAnalysisThreads | 11591687 | Specifies the maximum number of threads used for parallelism for PowerRamp measurement. |
| PowerRampResultsRiseTimeMean | 11591689 | Rise Time returns the rise time of the acquired signal that is the amount of time taken for the power envelope to rise from a level of 10 percent to 90 percent. When you set the PowerRampAveragingEnabled method to True, this parameter returns the mean of the rise time computed for each averaging count. This value is expressed in seconds. |
| PowerRampResultsFallTimeMean | 11591690 | Fall Time returns the fall time of the acquired signal that is the amount of time taken for the power envelope to fall from a level of 90 percent to 10 percent. When you set the PowerRampAveragingEnabled method to True,this parameter returns the mean of the fall time computed for each averaging countt. This value is expressed in seconds. |
| PowerRampResults40dBFallTimeMean | 11591691 | 40dB Fall Time returns the fall time of the acquired signal at which transmit power drops 40 dB below average power. When you set the PowerRampAveragingEnabled method to True, this parameter returns the mean of the 40dB fall time computed for each averaging count. This value is expressed in seconds. |
| LimitedConfigurationChange | 11587584 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
| AutoLevelInitialReferenceLevel | 11587585 | Specifies the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| ResultFetchTimeout | 11583488 | Specifies the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidth.html language=enus -->
## TOPIC 00122: RFmxBTMXTwentydBBandwidth Class

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidth.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the 20dBBandwidth measurement. Derives fromRFmxBTMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.BTMXpublic class RFmxBTMXTwentydBBandwidth : RFmxBTMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxBTMXTwentydBBandwidthConfiguration instance that provides methods to confi

### RFmxBTMXTwentydBBandwidth Class

Represents the 20dBBandwidth measurement.

#### Derives from

- RFmxBTMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public class RFmxBTMXTwentydBBandwidth : RFmxBTMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxBTMXTwentydBBandwidthConfiguration instance that provides methods to configure the 20dBBandwidth measurement. |
| Results | Gets the RFmxBTMXTwentydBBandwidthResults instance that provides methods to fetch and read the 20dBBandwidth measurement results. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthaveragingenabled.html language=enus -->
## TOPIC 00123: RFmxBTMXTwentydBBandwidthAveragingEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the 20dBBandwidth measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXTwentydBBandwidthAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The 20dBBandwidth measurement uses t

### RFmxBTMXTwentydBBandwidthAveragingEnabled Enumeration

Specifies whether to enable averaging for the 20dBBandwidth measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXTwentydBBandwidthAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The 20dBBandwidth measurement uses the TwentydBBandwidthAveragingCount method as the number of acquisitions over which the 20dBBandwidth measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-configureaveraging__string-rfmxbtmxtwentydbbandwidthaveragingenabled-int.html language=enus -->
## TOPIC 00124: ConfigureAveraging(string, RFmxBTMXTwentydBBandwidthAveragingEnabled, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-configureaveraging__string-rfmxbtmxtwentydbbandwidthaveragingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-configureaveraging__string-rfmxbtmxtwentydbbandwidthaveragingenabled-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the 20dBBandwidth measurement.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int ConfigureAveraging(string selectorString, RFmxBTMXTwentydBBandwidthAveragingEnabled averagingEnabled, int averagingCount)ParametersNameTypeDescriptionselectorStringstringPass an empty stri

### ConfigureAveraging(string, RFmxBTMXTwentydBBandwidthAveragingEnabled, int)

Configures averaging for the 20dBBandwidth measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int ConfigureAveraging(string selectorString, RFmxBTMXTwentydBBandwidthAveragingEnabled averagingEnabled, int averagingCount)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxBTMXTwentydBBandwidthAveragingEnabled | Specifies whether to enable averaging for 20dBBandwidth measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTwentydBBandwidthConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00125: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable all the traces for the 20dBBandwidth measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of TwentydBBandwidthAllTracesEnabled attribute.The default value is FALSE.Para

### GetAllTracesEnabled(string, out bool)

Gets whether to enable all the traces for the 20dBBandwidth measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [TwentydBBandwidthAllTracesEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable all the traces for the 20dBBandwidth measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTwentydBBandwidthConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00126: GetAveragingCount(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the TwentydBBandwidthAveragingEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of TwentydBBandwidthAveragingCount a

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [TwentydBBandwidthAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxtwentydbbandwidthaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [TwentydBBandwidthAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the TwentydBBandwidthAveragingEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTwentydBBandwidthConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxp.html language=enus -->
## TOPIC 00127: RFmxBTMXTxp Class

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxp.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the TXP measurement. Derives fromRFmxBTMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.BTMXpublic class RFmxBTMXTxp : RFmxBTMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxBTMXTxpConfiguration instance that provides methods to configure the TXP measurement. ResultsGets

### RFmxBTMXTxp Class

Represents the TXP measurement.

#### Derives from

- RFmxBTMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public class RFmxBTMXTxp : RFmxBTMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxBTMXTxpConfiguration instance that provides methods to configure the TXP measurement. |
| Results | Gets the RFmxBTMXTxpResults instance that provides methods to fetch and read the TXP measurement results. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html language=enus -->
## TOPIC 00128: RFmxBTMXTxpAveragingEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the transmit power (TxP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXTxpAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement uses the SetAveragingCount

### RFmxBTMXTxpAveragingEnabled Enumeration

Specifies whether to enable averaging for the transmit power (TxP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXTxpAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement uses the SetAveragingCount(string, int) method as the number of acquisitions over which the TXP measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00129: GetAveragingCount(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of TxpAveragi

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingenabled__string-rfmxbtmxtxpaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [TxpAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00130: GetAveragingEnabled(string, out RFmxBTMXTxpAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the transmit power (TxP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetAveragingEnabled(string selectorString, out RFmxBTMXTxpAveragingEnabled value)RemarksThis method gets the value of TxpAveragingEnabled attribute.The default value i

### GetAveragingEnabled(string, out RFmxBTMXTxpAveragingEnabled)

Gets whether to enable averaging for the transmit power (TxP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxBTMXTxpAveragingEnabled value)

#### Remarks

This method gets the value of [TxpAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXTxpAveragingEnabled | Upon return, contains whether to enable averaging for the transmit power (TxP) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getburstsynchronizationtype__string-out.html language=enus -->
## TOPIC 00131: GetBurstSynchronizationType(string, out RFmxBTMXTxpBurstSynchronizationType)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getburstsynchronizationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getburstsynchronizationtype__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetBurstSynchronizationType(string selectorString, out RFmxBTMXTxpBurstSynchronizationType value)RemarksThis method gets the value

### GetBurstSynchronizationType(string, out RFmxBTMXTxpBurstSynchronizationType)

Gets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetBurstSynchronizationType(string selectorString, out RFmxBTMXTxpBurstSynchronizationType value)

#### Remarks

This method gets the value of [TxpBurstSynchronizationType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Preamble](nationalinstruments-rfmx-btmx-rfmxbtmxtxpburstsynchronizationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxBTMXTxpBurstSynchronizationType | Upon return, contains the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00132: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the transmit power (TxP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of TxpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescrip

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the transmit power (TxP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [TxpMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the transmit power (TxP) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00133: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data ava

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [TxpNumberOfAnalysisThreads](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00134: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable all the traces used for transmit power (TxP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of TxpAllTracesEnabled attribute.The default value is FALSE.ParametersNam

### SetAllTracesEnabled(string, bool)

Sets whether to enable all the traces used for transmit power (TxP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [TxpAllTracesEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable all the traces used for transmit power (TxP) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00135: SetAveragingCount(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of TxpAveragingCo

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled)](nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingenabled__string-rfmxbtmxtxpaveragingenabled.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [TxpAveragingCount](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingenabled__string-rfmxbtmxtxpaveragingenabled.html language=enus -->
## TOPIC 00136: SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingenabled__string-rfmxbtmxtxpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setaveragingenabled__string-rfmxbtmxtxpaveragingenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the transmit power (TxP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetAveragingEnabled(string selectorString, RFmxBTMXTxpAveragingEnabled value)RemarksThis method sets the value of TxpAveragingEnabled attribute.The default value is Fa

### SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled)

Sets whether to enable averaging for the transmit power (TxP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetAveragingEnabled(string selectorString, RFmxBTMXTxpAveragingEnabled value)

#### Remarks

This method sets the value of [TxpAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXTxpAveragingEnabled | Specifies whether to enable averaging for the transmit power (TxP) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setburstsynchronizationtype__string-rfmxbtmxtxpburstsynchronizationtype.html language=enus -->
## TOPIC 00137: SetBurstSynchronizationType(string, RFmxBTMXTxpBurstSynchronizationType)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setburstsynchronizationtype__string-rfmxbtmxtxpburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setburstsynchronizationtype__string-rfmxbtmxtxpburstsynchronizationtype.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetBurstSynchronizationType(string selectorString, RFmxBTMXTxpBurstSynchronizationType value)RemarksThis method sets the value of

### SetBurstSynchronizationType(string, RFmxBTMXTxpBurstSynchronizationType)

Sets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetBurstSynchronizationType(string selectorString, RFmxBTMXTxpBurstSynchronizationType value)

#### Remarks

This method sets the value of [TxpBurstSynchronizationType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is [Preamble](nationalinstruments-rfmx-btmx-rfmxbtmxtxpburstsynchronizationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxBTMXTxpBurstSynchronizationType | Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00138: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the transmit power (TxP) measurements. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of TxpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescription

### SetMeasurementEnabled(string, bool)

Sets whether to enable the transmit power (TxP) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [TxpMeasurementEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the transmit power (TxP) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00139: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data ava

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [TxpNumberOfAnalysisThreads](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration.html language=enus -->
## TOPIC 00140: RFmxBTMXTxpConfiguration Class

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpconfiguration.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the TXP measurement. Derives fromRFmxBTMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.BTMXpublic class RFmxBTMXTxpConfiguration : RFmxBTMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxBTMXTxpAveragingEnabled, int)Configures averaging for the transm

### RFmxBTMXTxpConfiguration Class

Provides methods to configure the TXP measurement.

#### Derives from

- RFmxBTMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public class RFmxBTMXTxpConfiguration : RFmxBTMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxBTMXTxpAveragingEnabled, int) | Configures averaging for the transmit power (TXP) measurement. |
| ConfigureBurstSynchronizationType(string, RFmxBTMXTxpBurstSynchronizationType) | Configures the type of synchronization used for detecting the start of the packet in the transmit power (TXP) measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable all the traces used for transmit power (TxP) measurements. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxBTMXTxpAveragingEnabled) | Gets whether to enable averaging for the transmit power (TxP) measurements. |
| GetBurstSynchronizationType(string, out RFmxBTMXTxpBurstSynchronizationType) | Gets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the transmit power (TxP) measurements. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable all the traces used for transmit power (TxP) measurements. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) | Sets whether to enable averaging for the transmit power (TxP) measurements. |
| SetBurstSynchronizationType(string, RFmxBTMXTxpBurstSynchronizationType) | Sets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the transmit power (TxP) measurements. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchedrpowers__string-double-out-out-out.html language=enus -->
## TOPIC 00141: FetchEdrPowers(string, double, out double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchedrpowers__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchedrpowers__string-double-out-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches TXP measurement results for enhanced data rate (EDR) packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchEdrPowers(string selectorString, double timeout, out double edrGfskAveragePowerMean, out double edrDpskAveragePowerMean, out double edrDpskGfskAveragePowerRatioMean)Para

### FetchEdrPowers(string, double, out double, out double, out double)

Fetches TXP measurement results for enhanced data rate (EDR) packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchEdrPowers(string selectorString, double timeout, out double edrGfskAveragePowerMean, out double edrDpskAveragePowerMean, out double edrDpskGfskAveragePowerRatioMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| edrGfskAveragePowerMean | out double | Upon return, contains the average power of the GFSK portion of the EDR packet. When you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
| edrDpskAveragePowerMean | out double | Upon return, contains the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
| edrDpskGfskAveragePowerRatioMean | out double | Upon return, contains the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectereferenceperiodpowers__string-double-out-out.html language=enus -->
## TOPIC 00142: FetchLECteReferencePeriodPowers(string, double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectereferenceperiodpowers__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectereferenceperiodpowers__string-double-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the transmit power (TXP) measurement over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature.SyntaxNamespace: NationalInstruments.RFmx.BTMXpubli

### FetchLECteReferencePeriodPowers(string, double, out double, out double)

Fetches the transmit power (TXP) measurement over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchLECteReferencePeriodPowers(string selectorString, double timeout, out double referencePeriodAveragePowerMean, out double referencePeriodPeakAbsolutePowerDeviationMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| referencePeriodAveragePowerMean | out double | Upon return, contains the average power computed over the reference period in the CTE portion of the LE packet. When you set the TXP Averaging Enabled method to true, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
| referencePeriodPeakAbsolutePowerDeviationMaximum | out double | Upon return, contains the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. When you set the TXP Averaging Enabled method to true, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectetransmitslotpowers__string-double-out-out.html language=enus -->
## TOPIC 00143: FetchLECteTransmitSlotPowers(string, double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectetransmitslotpowers__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectetransmitslotpowers__string-double-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the transmit power (TXP) measurement over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic

### FetchLECteTransmitSlotPowers(string, double, out double, out double)

Fetches the transmit power (TXP) measurement over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchLECteTransmitSlotPowers(string selectorString, double timeout, out double transmitSlotAveragePowerMean, out double transmitSlotPeakAbsolutePowerDeviationMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| transmitSlotAveragePowerMean | out double | Upon return, contains the average power computed over each transmit slot in CTE portion of the LE packet. When you set the TXP Averaging Enabled method to true, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
| transmitSlotPeakAbsolutePowerDeviationMaximum | out double | Upon return, contains the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. When you set the TXP Averaging Enabled method to true, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectetransmitslotpowersarray__string-double-ref-ref.html language=enus -->
## TOPIC 00144: FetchLECteTransmitSlotPowersArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectetransmitslotpowersarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchlectetransmitslotpowersarray__string-double-ref-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of transmit power (TXP) measurement over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature.SyntaxNamespace: NationalInstruments.RFmx.BTM

### FetchLECteTransmitSlotPowersArray(string, double, ref double[], ref double[])

Fetches an array of transmit power (TXP) measurement over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchLECteTransmitSlotPowersArray(string selectorString, double timeout, ref double[] transmitSlotAveragePowerMean, ref double[] transmitSlotPeakAbsolutePowerDeviationMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| transmitSlotAveragePowerMean | ref double[] | Upon return, contains an array of average powers computed over every transmit slot in CTE portion of the LE packet. When you set the TXP Averaging Enabled method to true, it returns an array of mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
| transmitSlotPeakAbsolutePowerDeviationMaximum | ref double[] | Upon return, contains an array of peak absolute power deviations computed over every transmit slot in CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. When you set the TXP Averaging Enabled method to true, it returns an array of maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchpowers__string-double-out-out-out-out.html language=enus -->
## TOPIC 00145: FetchPowers(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchpowers__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchpowers__string-double-out-out-out-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches TXP measurement results. These results are valid for all packets.SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchPowers(string selectorString, double timeout, out double averagePowerMean, out double averagePowerMaximum, out double averagePowerMinimum, out double peakToAveragePo

### FetchPowers(string, double, out double, out double, out double, out double)

Fetches TXP measurement results. These results are valid for all packets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchPowers(string selectorString, double timeout, out double averagePowerMean, out double averagePowerMaximum, out double averagePowerMinimum, out double peakToAveragePowerRatioMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| averagePowerMean | out double | Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the SetAveragingEnabled(string, RFmxBTMXTxpAveragingEnabled) method to True, it returns the mean of the average power results computed for each averaging count. This value is expressed in dBm. |
| averagePowerMaximum | out double | Upon return, contains the average power computed over the measurement interval. When you set the Direction Finding Mode method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
| averagePowerMinimum | out double | Upon return, contains the average power computed over the measurement interval. When you set the Direction Finding Mode method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
| peakToAveragePowerRatioMaximum | out double | Upon return, contains the peak to average power ratio computed over the measurement interval. When you set the Direction Finding Mode method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchpowertrace__string-double-ref.html language=enus -->
## TOPIC 00146: FetchPowerTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchpowertrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-fetchpowertrace__string-double-ref.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power versus time trace. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you do

### FetchPowerTrace(string, double, ref AnalogWaveform< float >)

Fetches the power versus time trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| power | ref AnalogWaveform< float > | Upon return, contains the power versus time trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowermaximum__string-out.html language=enus -->
## TOPIC 00147: GetAveragePowerMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowermaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average powe

### GetAveragePowerMaximum(string, out double)

Gets the average power computed over the measurement interval. When you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragePowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsAveragePowerMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowermean__string-out.html language=enus -->
## TOPIC 00148: GetAveragePowerMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowermean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average powe

### GetAveragePowerMean(string, out double)

Gets the average power computed over the measurement interval. When you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsAveragePowerMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowerminimum__string-out.html language=enus -->
## TOPIC 00149: GetAveragePowerMinimum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowerminimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getaveragepowerminimum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average powe

### GetAveragePowerMinimum(string, out double)

Gets the average power computed over the measurement interval. When you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetAveragePowerMinimum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsAveragePowerMinimum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrdpskaveragepowermean__string-out.html language=enus -->
## TOPIC 00150: GetEdrDpskAveragePowerMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrdpskaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrdpskaveragepowermean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetEd

### GetEdrDpskAveragePowerMean(string, out double)

Gets the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetEdrDpskAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsEdrDpskAveragePowerMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrdpskgfskaveragepowerratiomean__string-out.html language=enus -->
## TOPIC 00151: GetEdrDpskGfskAveragePowerRatioMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrdpskgfskaveragepowerratiomean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrdpskgfskaveragepowerratiomean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB

### GetEdrDpskGfskAveragePowerRatioMean(string, out double)

Gets the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetEdrDpskGfskAveragePowerRatioMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsEdrDpskGfskAveragePowerRatioMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrgfskaveragepowermean__string-out.html language=enus -->
## TOPIC 00152: GetEdrGfskAveragePowerMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrgfskaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getedrgfskaveragepowermean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic int GetEd

### GetEdrGfskAveragePowerMean(string, out double)

Gets the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetEdrGfskAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsEdrGfskAveragePowerMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlecsphasemeasurementperiodaveragepowermean__string-out.html language=enus -->
## TOPIC 00153: GetLECSPhaseMeasurementPeriodAveragePowerMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlecsphasemeasurementperiodaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlecsphasemeasurementperiodaveragepowermean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. When you set the TxpAveragingEnabled

### GetLECSPhaseMeasurementPeriodAveragePowerMean(string, out double)

Gets the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the [PacketType](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) method to [PacketTypeLE](nationalinstruments-rfmx-btmx-rfmxbtmxpackettype.html) and the [ChannelSoundingPacketFormat](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) method to any value other than [Sync](nationalinstruments-rfmx-btmx-rfmxbtmxchannelsoundingpacketformat.html). When you set the [TxpAveragingEnabled](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) method to [True](nationalinstruments-rfmx-btmx-rfmxbtmxtxpaveragingenabled.html), it returns the mean of the phase measurement period average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetLECSPhaseMeasurementPeriodAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsLECSPhaseMeasurementPeriodAveragePowerMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. When you set the TxpAveragingEnabled method to True, it returns the mean of the phase measurement period average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectereferenceperiodaveragepowermean__string-out.html language=enus -->
## TOPIC 00154: GetLECteReferencePeriodAveragePowerMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectereferenceperiodaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectereferenceperiodaveragepowermean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns th

### GetLECteReferencePeriodAveragePowerMean(string, out double)

Gets the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html). When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetLECteReferencePeriodAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsLECteReferencePeriodAveragePowerMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectereferenceperiodpeakabsolutepowerdeviationmaximum__string-out.html language=enus -->
## TOPIC 00155: GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectereferenceperiodpeakabsolutepowerdeviationmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectereferenceperiodpeakabsolutepowerdeviationmaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindi

### GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum(string, out double)

Gets the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html). When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsLECteReferencePeriodPeakAbsolutePowerDeviationMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectetransmitslotaveragepowermean__string-out.html language=enus -->
## TOPIC 00156: GetLECteTransmitSlotAveragePowerMean(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectetransmitslotaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectetransmitslotaveragepowermean__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean

### GetLECteTransmitSlotAveragePowerMean(string, out double)

Gets the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html). When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetLECteTransmitSlotAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsLECteTransmitSlotAveragePowerMean](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectetransmitslotpeakabsolutepowerdeviationmaximum__string-out.html language=enus -->
## TOPIC 00157: GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectetransmitslotpeakabsolutepowerdeviationmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getlectetransmitslotpeakabsolutepowerdeviationmaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the

### GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum(string, out double)

Gets the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html). When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsLECteTransmitSlotPeakAbsolutePowerDeviationMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getpeakpowermaximum__string-out.html language=enus -->
## TOPIC 00158: GetPeakPowerMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getpeakpowermaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getpeakpowermaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging

### GetPeakPowerMaximum(string, out double)

Gets the peak power computed over the measurement interval. When you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPeakPowerMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsPeakPowerMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getpeaktoaveragepowerratiomaximum__string-out.html language=enus -->
## TOPIC 00159: GetPeakToAveragePowerRatioMaximum(string, out double)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getpeaktoaveragepowerratiomaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults-getpeaktoaveragepowerratiomaximum__string-out.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computati

### GetPeakToAveragePowerRatioMaximum(string, out double)

Gets the peak to average power ratio computed over the measurement interval. When you set the [SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode)](nationalinstruments-rfmx-btmx-rfmxbtmx-setdirectionfindingmode__string-rfmxbtmxdirectionfindingmode.html) method to [AngleOfDepature](nationalinstruments-rfmx-btmx-rfmxbtmxdirectionfindingmode.html) for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. For LE-HDT, PAPR is calculated using peak power calculated over active portion of burst and average power calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public int GetPeakToAveragePowerRatioMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsPeakToAveragePowerRatioMaximum](nationalinstruments-rfmx-btmx-rfmxbtmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. For LE-HDT, PAPR is calculated using peak power calculated over active portion of burst and average power calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxBTMXTxpResults Class

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults.html language=enus -->
## TOPIC 00160: RFmxBTMXTxpResults Class

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxtxpresults.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the TXP measurement results. Derives fromRFmxBTMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.BTMXpublic class RFmxBTMXTxpResults : RFmxBTMXSubObjectMethodsNameDescriptionFetchEdrPowers(string, double, out double, out double, out double)Fetches TXP measuremen

### RFmxBTMXTxpResults Class

Provides methods to fetch and read the TXP measurement results.

#### Derives from

- RFmxBTMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public class RFmxBTMXTxpResults : RFmxBTMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchEdrPowers(string, double, out double, out double, out double) | Fetches TXP measurement results for enhanced data rate (EDR) packets. |
| FetchLECteReferencePeriodPowers(string, double, out double, out double) | Fetches the transmit power (TXP) measurement over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
| FetchLECteTransmitSlotPowers(string, double, out double, out double) | Fetches the transmit power (TXP) measurement over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
| FetchLECteTransmitSlotPowersArray(string, double, ref double[], ref double[]) | Fetches an array of transmit power (TXP) measurement over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
| FetchPowers(string, double, out double, out double, out double, out double) | Fetches TXP measurement results. These results are valid for all packets. |
| FetchPowerTrace(string, double, ref AnalogWaveform< float >) | Fetches the power versus time trace. |
| GetAveragePowerMaximum(string, out double) | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
| GetAveragePowerMean(string, out double) | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count. |
| GetAveragePowerMinimum(string, out double) | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
| GetEdrDpskAveragePowerMean(string, out double) | Gets the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
| GetEdrDpskGfskAveragePowerRatioMean(string, out double) | Gets the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |
| GetEdrGfskAveragePowerMean(string, out double) | Gets the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
| GetLECSPhaseMeasurementPeriodAveragePowerMean(string, out double) | Gets the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. When you set the TxpAveragingEnabled method to True, it returns the mean of the phase measurement period average power results computed for each averaging count. This value is expressed in dBm. |
| GetLECteReferencePeriodAveragePowerMean(string, out double) | Gets the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
| GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum(string, out double) | Gets the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
| GetLECteTransmitSlotAveragePowerMean(string, out double) | Gets the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
| GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum(string, out double) | Gets the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
| GetPeakPowerMaximum(string, out double) | Gets the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm. |
| GetPeakToAveragePowerRatioMaximum(string, out double) | Gets the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(string, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. For LE-HDT, PAPR is calculated using peak power calculated over active portion of burst and average power calculated from beginning of the payload portion. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxvdhtmodeenabled.html language=enus -->
## TOPIC 00161: RFmxBTMXVdhtModeEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxvdhtmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxvdhtmodeenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXVdhtModeEnabledMembersNameValueDescriptionFalse0True1

### RFmxBTMXVdhtModeEnabled Enumeration

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXVdhtModeEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 |  |
| True | 1 |  |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx-rfmxbtmxvhdtmodeenabled.html language=enus -->
## TOPIC 00162: RFmxBTMXVhdtModeEnabled Enumeration

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx-rfmxbtmxvhdtmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx-rfmxbtmxvhdtmodeenabled.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.BTMXpublic enum RFmxBTMXVhdtModeEnabledMembersNameValueDescriptionFalse0True1

### RFmxBTMXVhdtModeEnabled Enumeration

#### Syntax

**Namespace:**[NationalInstruments.RFmx.BTMX](nationalinstruments-rfmx-btmx.html)

public enum RFmxBTMXVhdtModeEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 |  |
| True | 1 |  |

Parent topic:

NationalInstruments.RFmx.BTMX

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-btmx.html language=enus -->
## TOPIC 00163: NationalInstruments.RFmx.BTMX

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-btmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-btmx.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxBTMXDefines a root class which is used to identify and control BT signal configuration. RFmxBTMXAcpRepresents the ACP measurement. RFmxBTMXAcpConfigurationProvides methods to configure the ACP measurement. RFmxBTMXAcpResultsProvides methods to fetch and read the ACP measure

### NationalInstruments.RFmx.BTMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxBTMX | Defines a root class which is used to identify and control BT signal configuration. |
| RFmxBTMXAcp | Represents the ACP measurement. |
| RFmxBTMXAcpConfiguration | Provides methods to configure the ACP measurement. |
| RFmxBTMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
| RFmxBTMXConstants | Specifies constants for I/O terminals. |
| RFmxBTMXFrequencyRange | Represents the FrequencyRange measurement. |
| RFmxBTMXFrequencyRangeConfiguration | Provides methods to configure the FrequencyRange measurement. |
| RFmxBTMXFrequencyRangeResults | Provides methods to fetch and read the FrequencyRange measurement results. |
| RFmxBTMXModAcc | Represents the ModAcc measurement. |
| RFmxBTMXModAccConfiguration | Provides methods to configure the ModAcc measurement. |
| RFmxBTMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
| RFmxBTMXModSpectrum | Represents the ModSpectrum measurement. |
| RFmxBTMXModSpectrumConfiguration | Provides methods to configure the ModSpectrum measurement. |
| RFmxBTMXModSpectrumResults | Provides methods to fetch and read the ModSpectrum measurement results. |
| RFmxBTMXPowerRamp | Represents the PowerRamp measurement. |
| RFmxBTMXPowerRampConfiguration | Provides methods to configure the PowerRamp measurement. |
| RFmxBTMXPowerRampResults | Provides methods to fetch and read the PowerRamp measurement results. |
| RFmxBTMXSubObject | Represents members that are common to all sub-object of RFmxBTMX classes. |
| RFmxBTMXTwentydBBandwidth | Represents the 20dBBandwidth measurement. |
| RFmxBTMXTwentydBBandwidthConfiguration | Provides methods to configure the 20dBBandwidth measurement. |
| RFmxBTMXTwentydBBandwidthResults | Provides methods to fetch and read the 20dBBandwidth measurement results. |
| RFmxBTMXTxp | Represents the TXP measurement. |
| RFmxBTMXTxpConfiguration | Provides methods to configure the TXP measurement. |
| RFmxBTMXTxpResults | Provides methods to fetch and read the TXP measurement results. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxBTMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
| RFmxBTMXAcpBurstSynchronizationType | Specifies the type of synchronization used for detecting the start of the EDR packet in the adjacent channel power (ACP) measurement. |
| RFmxBTMXAcpOffsetChannelMode | Specifies which offset channels are used for the measurement. |
| RFmxBTMXAcpResultsMeasurementStatus | Indicates the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(string, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
| RFmxBTMXAutoPreambleDetectionEnabled | Specifies whether to enable the auto-detection of preamble field in the packet. When AutoPreamble Detection Enabled method is set to True, the measurement auto detects the LTS field of the PacketTypeLEHdt packet and ignores SetZadoffChuIndex(string, int) method. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |
| RFmxBTMXChannelSoundingPacketFormat | Specifies the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS. |
| RFmxBTMXChannelSoundingSyncSequence | Specifies the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
| RFmxBTMXChannelSoundingToneExtensionSlot | Specifies whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(string, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
| RFmxBTMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is valid only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to DigitalEdge. |
| RFmxBTMXDirectionFindingMode | Specifies the mode of direction finding. |
| RFmxBTMXFrequencyRangeAveragingEnabled | Specifies whether to enable averaging for the FrequencyRange measurement. |
| RFmxBTMXHighDataThroughputPacketFormat | Specifies the Higher Data Throughput (HDT) packet format. This method is applicable only when you set the SetPacketType(string, RFmxBTMXPacketType) method to PacketTypeLEHdt. |
| RFmxBTMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to IQPowerEdge. |
| RFmxBTMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxBTMXTriggerType) method to IQPowerEdge. |
| RFmxBTMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
| RFmxBTMXMeasurementTypes | Specifies the type of measurement. |
| RFmxBTMXModAccAveragingEnabled | Specifies whether to enable averaging for the ModAcc measurements. |
| RFmxBTMXModAccBurstSynchronizationType | Specifies the type of synchronization used for detecting the start of packet in ModAcc measurement. |
| RFmxBTMXModAccFrequencyTrackingEnabled | Specifies whether to enable frequency tracking for LE- HDT packet. If you set this method to True, the Control Header EVM, Payload EVM, Payload Frequency Error w1 and Frequency Error w0+w1 results are computed after frequency tracking. |
| RFmxBTMXModAccIQMismatchCorrectionEnabled | Specifies whether to enable the IQ mismatch correction for LE- HDT packet. If you set this method to True, the EVM results are computed after correcting for the IQ gain imbalance and quadrature error. |
| RFmxBTMXModAccIQOriginOffsetCorrectionEnabled | Specifies whether to enable the I/Q origin offset correction for EDR and LE-HDT packets. If you set this method to True, the DEVM and EVM results are computed after correcting for the I/Q origin offset. |
| RFmxBTMXModSpectrumAveragingEnabled | Specifies whether to enable averaging for ModSpectrum measurements. |
| RFmxBTMXModSpectrumBurstSynchronizationType | Specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. |
| RFmxBTMXPacketType | Specifies the type of the Bluetooth packet to be measured. |
| RFmxBTMXPayloadBitPattern | Specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. |
| RFmxBTMXPayloadLengthMode | Specifies the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(string, int) properties decide the length of the payload to be used for measurement. |
| RFmxBTMXPowerRampAveragingEnabled | Specifies whether to enable averaging for PowerRamp measurement. |
| RFmxBTMXPowerRampBurstSynchronizationType | Specifies the type of synchronization used for detecting the start of packet in the PowerRamp measurement. |
| RFmxBTMXPropertyId | Specifies all the attribute identifiers. |
| RFmxBTMXStandard | Specifies the standard. |
| RFmxBTMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxBTMXTriggerType | Specifies the type of trigger to be used for signal acquisition. |
| RFmxBTMXTwentydBBandwidthAveragingEnabled | Specifies whether to enable averaging for the 20dBBandwidth measurement. |
| RFmxBTMXTxpAveragingEnabled | Specifies whether to enable averaging for the transmit power (TxP) measurements. |
| RFmxBTMXTxpBurstSynchronizationType | Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
| RFmxBTMXVdhtModeEnabled |  |
| RFmxBTMXVhdtModeEnabled |  |

#### Delegates

None

<!--NI_TOPIC bundle=rfmxbluetooth-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxbtmxextension-getbtsignalconfiguration__this-string.html language=enus -->
## TOPIC 00164: GetBTSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxbluetooth-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxbtmxextension-getbtsignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxbtmxextension-getbtsignalconfiguration__this-string.html
- document_id: `rfmxbluetooth-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a BT signal configuration for specified signal name. Existing BT signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxBTMX GetBTSignalConfiguration(this RFmxInstrMX instrSession, string signalName)ParametersNameT

### GetBTSignalConfiguration(this RFmxInstrMX, string)

Creates a BT signal configuration for specified signal name. Existing BT signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxBTMX](nationalinstruments-rfmx-btmx-rfmxbtmx.html) GetBTSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxBTMX.

Parent topic:

RFmxBTMXExtension Class
