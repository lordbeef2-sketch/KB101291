# NI DOCUMENT BUNDLE: rfmx-cdma2k-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-cdma2k-dotnet start=1 end=108 -->
<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0315ec9e-4dba-bbbb-bcbc-a3efda8534e7.htm language=enus -->
## TOPIC 00001: rfmxcdma2kdotnet/html/0315ec9e-4dba-bbbb-bcbc-a3efda8534e7.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0315ec9e-4dba-bbbb-bcbc-a3efda8534e7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0315ec9e-4dba-bbbb-bcbc-a3efda8534e7.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SetWalshCodeLength Method

RFmxCdma2kMXSetWalshCodeLength Method

SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode)

UserDefined

"channel(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetWalshCodeLength(
	string selectorString,
	int value
)
```

```text
Public Function SetWalshCodeLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the channel number. Example: "channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value Int32**
  - Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This method is used only when you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method.

###### Return Value

Int32

##### Remarks

WalshCodeLength

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/070bcd4e-8ff2-0f8c-9bd6-0d2b71f105b2.htm language=enus -->
## TOPIC 00002: rfmxcdma2kdotnet/html/070bcd4e-8ff2-0f8c-9bd6-0d2b71f105b2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/070bcd4e-8ff2-0f8c-9bd6-0d2b71f105b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/070bcd4e-8ff2-0f8c-9bd6-0d2b71f105b2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.FetchLowerOffsetPower Method

RFmxCdma2kMXSemResultsFetchLowerOffsetPower Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLowerOffsetPower(
	string selectorString,
	double timeout,
	out double absoluteIntegratedPower,
	out double relativeIntegratedPower,
	out double absolutePeakPower,
	out double peakFrequency,
	out double relativePeakPower
)
```

```text
Public Function FetchLowerOffsetPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef absoluteIntegratedPower As Double,
	<OutAttribute> ByRef relativeIntegratedPower As Double,
	<OutAttribute> ByRef absolutePeakPower As Double,
	<OutAttribute> ByRef peakFrequency As Double,
	<OutAttribute> ByRef relativePeakPower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absoluteIntegratedPower Double**
  - Upon return, contains the lower (negative) offset segment power measured.
- **relativeIntegratedPower Double**
  - Upon return, contains the power in the lower (negative) offset segment relative to the carrier absolute integrated power.
- **absolutePeakPower Double**
  - Upon return, contains the peak power measured in the lower (negative) offset segment. The power is measured in dBm.
- **peakFrequency Double**
  - Upon return, contains the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz.
- **relativePeakPower Double**
  - Upon return, contains the peak power in the lower (negative) offset segment relative to the carrier absolute integrated power.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/07c3cc07-5685-5e06-e59f-84faaa36bde1.htm language=enus -->
## TOPIC 00003: rfmxcdma2kdotnet/html/07c3cc07-5685-5e06-e59f-84faaa36bde1.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/07c3cc07-5685-5e06-e59f-84faaa36bde1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/07c3cc07-5685-5e06-e59f-84faaa36bde1.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.GetLowerOffsetMarginFrequency Method

RFmxCdma2kMXSemResultsGetLowerOffsetMarginFrequency Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetMarginFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetMarginFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetMarginFrequency

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/09d60e0a-6618-559c-6543-d8c44f0c6478.htm language=enus -->
## TOPIC 00004: rfmxcdma2kdotnet/html/09d60e0a-6618-559c-6543-d8c44f0c6478.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/09d60e0a-6618-559c-6543-d8c44f0c6478.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/09d60e0a-6618-559c-6543-d8c44f0c6478.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.ConfigureRF Method

RFmxCdma2kMXConfigureRF Method

selectorString

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRF(
	string selectorString,
	double centerFrequency,
	double referenceLevel,
	double externalAttenuation
)
```

```text
Public Function ConfigureRF ( 
	selectorString As String,
	centerFrequency As Double,
	referenceLevel As Double,
	externalAttenuation As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **centerFrequency Double**
  - Specifies the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency.
- **referenceLevel Double**
  - Specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- **externalAttenuation Double**
  - Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0acf44e8-85e6-cf52-239f-9e46a6726c87.htm language=enus -->
## TOPIC 00005: rfmxcdma2kdotnet/html/0acf44e8-85e6-cf52-239f-9e46a6726c87.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0acf44e8-85e6-cf52-239f-9e46a6726c87.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0acf44e8-85e6-cf52-239f-9e46a6726c87.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXObw Methods

RFmxCdma2kMXObw Methods

The [RFmxCdma2kMXObw](2775fcba-0884-1b0b-b204-43001e8aa4ab.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxCdma2kMXObw Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0b5bbc7d-1259-7b0c-3fa7-44b66b3a8010.htm language=enus -->
## TOPIC 00006: rfmxcdma2kdotnet/html/0b5bbc7d-1259-7b0c-3fa7-44b66b3a8010.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0b5bbc7d-1259-7b0c-3fa7-44b66b3a8010.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0b5bbc7d-1259-7b0c-3fa7-44b66b3a8010.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.ConfigureUserDefinedChannel Method

RFmxCdma2kMXConfigureUserDefinedChannel Method

userDefined

"channel(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUserDefinedChannel(
	string selectorString,
	int walshCodeLength,
	int walshCodeNumber,
	RFmxCdma2kMXBranch branch
)
```

```text
Public Function ConfigureUserDefinedChannel ( 
	selectorString As String,
	walshCodeLength As Integer,
	walshCodeNumber As Integer,
	branch As RFmxCdma2kMXBranch
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of channel number.
- **walshCodeLength Int32**
  - Specifies the Walsh code length of a specific user-defined channel.
- **walshCodeNumber Int32**
  - Specifies the Walsh code number of a specific user-defined channel.
- **branch RFmxCdma2kMXBranch**
  - Specifies the branch on which a specific user-defined channel is mapped.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0bd61aad-5ba6-392e-e839-caca334f63c9.htm language=enus -->
## TOPIC 00007: rfmxcdma2kdotnet/html/0bd61aad-5ba6-392e-e839-caca334f63c9.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0bd61aad-5ba6-392e-e839-caca334f63c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0bd61aad-5ba6-392e-e839-caca334f63c9.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpResults.FetchOffsetMeasurement Method

RFmxCdma2kMXAcpResultsFetchOffsetMeasurement Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchOffsetMeasurement(
	string selectorString,
	double timeout,
	out double lowerRelativePower,
	out double upperRelativePower,
	out double lowerAbsolutePower,
	out double upperAbsolutePower
)
```

```text
Public Function FetchOffsetMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef lowerRelativePower As Double,
	<OutAttribute> ByRef upperRelativePower As Double,
	<OutAttribute> ByRef lowerAbsolutePower As Double,
	<OutAttribute> ByRef upperAbsolutePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **lowerRelativePower Double**
  - Upon return, contains the lower offset channel power measured relative to the carrier absolute power. This value is expressed in dB.
- **upperRelativePower Double**
  - Upon return, contains the upper offset channel power measured relative to the carrier absolute power. This value is expressed in dB.
- **lowerAbsolutePower Double**
  - Upon return, contains the lower offset channel absolute power.
- **upperAbsolutePower Double**
  - Upon return, contains the upper offset channel absolute power.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXAcpResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0bf4a67e-baa8-738a-4266-20ed6e07f65c.htm language=enus -->
## TOPIC 00008: rfmxcdma2kdotnet/html/0bf4a67e-baa8-738a-4266-20ed6e07f65c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0bf4a67e-baa8-738a-4266-20ed6e07f65c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0bf4a67e-baa8-738a-4266-20ed6e07f65c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccResults.FetchNumberOfDetectedChannels Method

RFmxCdma2kMXModAccResultsFetchNumberOfDetectedChannels Method

SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode)

UserDefined

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchNumberOfDetectedChannels(
	string selectorString,
	double timeout,
	out int numberOfDetectedChannels
)
```

```text
Public Function FetchNumberOfDetectedChannels ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef numberOfDetectedChannels As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **numberOfDetectedChannels Int32**
  - Upon return, contains the total number of detected channels.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXModAccResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0c3df10f-dd71-5e07-acc4-b69bb8387927.htm language=enus -->
## TOPIC 00009: rfmxcdma2kdotnet/html/0c3df10f-dd71-5e07-acc4-b69bb8387927.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0c3df10f-dd71-5e07-acc4-b69bb8387927.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0c3df10f-dd71-5e07-acc4-b69bb8387927.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.GetIQPowerEdgeTriggerLevel Method

RFmxCdma2kMXGetIQPowerEdgeTriggerLevel Method

SetIQPowerEdgeTriggerLevelType(String, RFmxCdma2kMXIQPowerEdgeTriggerLevelType)

Relative

Absolute

SetTriggerType(String, RFmxCdma2kMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQPowerEdgeTriggerLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(String, RFmxCdma2kMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevel

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0c86c855-216b-9f81-5088-46501a5ab03c.htm language=enus -->
## TOPIC 00010: rfmxcdma2kdotnet/html/0c86c855-216b-9f81-5088-46501a5ab03c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0c86c855-216b-9f81-5088-46501a5ab03c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0c86c855-216b-9f81-5088-46501a5ab03c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAcc.Configuration Property

RFmxCdma2kMXModAccConfiguration Property

RFmxCdma2kMXModAccConfiguration

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxCdma2kMXModAccConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxCdma2kMXModAccConfiguration
	Get
```

###### Property Value

RFmxCdma2kMXModAccConfiguration

##### See Also

###### Reference

RFmxCdma2kMXModAcc Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0eb5913c-04c8-090c-85a1-4d3d6a464451.htm language=enus -->
## TOPIC 00011: rfmxcdma2kdotnet/html/0eb5913c-04c8-090c-85a1-4d3d6a464451.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0eb5913c-04c8-090c-85a1-4d3d6a464451.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0eb5913c-04c8-090c-85a1-4d3d6a464451.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSlotPhaseConfiguration.SetReceiveFilterEnabled Method

RFmxCdma2kMXSlotPhaseConfigurationSetReceiveFilterEnabled Method

Sets whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReceiveFilterEnabled(
	string selectorString,
	RFmxCdma2kMXSlotPhaseReceiveFilterEnabled value
)
```

```text
Public Function SetReceiveFilterEnabled ( 
	selectorString As String,
	value As RFmxCdma2kMXSlotPhaseReceiveFilterEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXSlotPhaseReceiveFilterEnabled**
  - Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered.

###### Return Value

Int32

##### Remarks

SlotPhaseReceiveFilterEnabled

True

##### See Also

###### Reference

RFmxCdma2kMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0f6a0ee9-4ec7-f35b-80e9-bc54d8fe4e28.htm language=enus -->
## TOPIC 00012: rfmxcdma2kdotnet/html/0f6a0ee9-4ec7-f35b-80e9-bc54d8fe4e28.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0f6a0ee9-4ec7-f35b-80e9-bc54d8fe4e28.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0f6a0ee9-4ec7-f35b-80e9-bc54d8fe4e28.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.GetUpperOffsetMarginFrequency Method

RFmxCdma2kMXSemResultsGetUpperOffsetMarginFrequency Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetMarginFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetMarginFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMarginFrequency

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0f77608b-8e09-8260-cc36-da5d176ff211.htm language=enus -->
## TOPIC 00013: rfmxcdma2kdotnet/html/0f77608b-8e09-8260-cc36-da5d176ff211.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0f77608b-8e09-8260-cc36-da5d176ff211.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0f77608b-8e09-8260-cc36-da5d176ff211.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemConfiguration.SetAveragingCount Method

RFmxCdma2kMXSemConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingCount(
	string selectorString,
	int value
)
```

```text
Public Function SetAveragingCount ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

SemAveragingCount

##### See Also

###### Reference

RFmxCdma2kMXSemConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/0fb8cb98-82cf-18be-40e7-ab96fb364217.htm language=enus -->
## TOPIC 00014: rfmxcdma2kdotnet/html/0fb8cb98-82cf-18be-40e7-ab96fb364217.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/0fb8cb98-82cf-18be-40e7-ab96fb364217.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/0fb8cb98-82cf-18be-40e7-ab96fb364217.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXObw Properties

RFmxCdma2kMXObw Properties

The [RFmxCdma2kMXObw](2775fcba-0884-1b0b-b204-43001e8aa4ab.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxCdma2kMXObwConfiguration instance that provides methods to configure the OBW measurement |
|  | Results | Gets the RFmxCdma2kMXObwResults instance that provides methods to fetch and read the OBW measurement results. |

Top

##### See Also

###### Reference

RFmxCdma2kMXObw Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/113594ea-bfa0-1a18-7052-97677ab838f9.htm language=enus -->
## TOPIC 00015: rfmxcdma2kdotnet/html/113594ea-bfa0-1a18-7052-97677ab838f9.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/113594ea-bfa0-1a18-7052-97677ab838f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/113594ea-bfa0-1a18-7052-97677ab838f9.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SetIQPowerEdgeTriggerSource Method

RFmxCdma2kMXSetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxCdma2kMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerSource(
	string selectorString,
	string value
)
```

```text
Public Function SetIQPowerEdgeTriggerSource ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/14350596-6dc9-0536-b264-47298de7ba1c.htm language=enus -->
## TOPIC 00016: rfmxcdma2kdotnet/html/14350596-6dc9-0536-b264-47298de7ba1c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/14350596-6dc9-0536-b264-47298de7ba1c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/14350596-6dc9-0536-b264-47298de7ba1c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpConfiguration.GetAveragingCount Method

RFmxCdma2kMXChpConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxCdma2kMXChpAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingCount(
	string selectorString,
	out int value
)
```

```text
Public Function GetAveragingCount ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXChpAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ChpAveragingCount

##### See Also

###### Reference

RFmxCdma2kMXChpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/168978ac-1df6-b67f-33d6-9eb811f07dd6.htm language=enus -->
## TOPIC 00017: rfmxcdma2kdotnet/html/168978ac-1df6-b67f-33d6-9eb811f07dd6.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/168978ac-1df6-b67f-33d6-9eb811f07dd6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/168978ac-1df6-b67f-33d6-9eb811f07dd6.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SetReferenceLevelHeadroom Method

RFmxCdma2kMXSetReferenceLevelHeadroom Method

Default values

Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReferenceLevelHeadroom(
	string selectorString,
	double value
)
```

```text
Public Function SetReferenceLevelHeadroom ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

###### Return Value

Int32

##### Remarks

ReferenceLevelHeadroom

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/19c9a709-0c49-f7da-2466-5c09685a2c82.htm language=enus -->
## TOPIC 00018: rfmxcdma2kdotnet/html/19c9a709-0c49-f7da-2466-5c09685a2c82.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/19c9a709-0c49-f7da-2466-5c09685a2c82.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/19c9a709-0c49-f7da-2466-5c09685a2c82.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.GetUpperOffsetRelativePeakPower Method

RFmxCdma2kMXSemResultsGetUpperOffsetRelativePeakPower Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetRelativePeakPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetRelativePeakPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetRelativePeakPower

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/25661016-74f7-399a-ec36-117a933522bc.htm language=enus -->
## TOPIC 00019: rfmxcdma2kdotnet/html/25661016-74f7-399a-ec36-117a933522bc.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/25661016-74f7-399a-ec36-117a933522bc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/25661016-74f7-399a-ec36-117a933522bc.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpConfiguration.SetRbwFilterType Method

RFmxCdma2kMXChpConfigurationSetRbwFilterType Method

Sets the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxCdma2kMXChpRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxCdma2kMXChpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXChpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

ChpRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxCdma2kMXChpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/25f61bfd-caf0-e03d-0aa1-d62dde68dd57.htm language=enus -->
## TOPIC 00020: rfmxcdma2kdotnet/html/25f61bfd-caf0-e03d-0aa1-d62dde68dd57.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/25f61bfd-caf0-e03d-0aa1-d62dde68dd57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/25f61bfd-caf0-e03d-0aa1-d62dde68dd57.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSlotPowerConfiguration Methods

RFmxCdma2kMXSlotPowerConfiguration Methods

The [RFmxCdma2kMXSlotPowerConfiguration](b441eab1-76a0-07bc-a9ad-4b2c181fd1ff.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureSynchronizationModeAndInterval | Configures the synchronizationMode, measurementOffset, and measurementLength parameters for the SlotPower measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the SlotPower measurement. |
|  | GetMeasurementLength | Gets the duration of the SlotPower measurement. This value is expressed in slots. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |
|  | GetReceiveFilterEnabled | Gets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |
|  | GetSpectrumInverted | Gets whether the spectrum of the signal is inverted. |
|  | GetSynchronizationMode | Gets whether the measurement is performed from the frame or slot boundary. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetMeasurementEnabled | Sets whether to enable the SlotPower measurement. |
|  | SetMeasurementLength | Sets the duration of the SlotPower measurement. This value is expressed in slots. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |
|  | SetReceiveFilterEnabled | Sets whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |
|  | SetSpectrumInverted | Sets whether the spectrum of the signal is inverted. |
|  | SetSynchronizationMode | Sets whether the measurement is performed from the frame or slot boundary. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxCdma2kMXSlotPowerConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2631fab3-04fe-4e37-40bd-ce0f22d7b737.htm language=enus -->
## TOPIC 00021: rfmxcdma2kdotnet/html/2631fab3-04fe-4e37-40bd-ce0f22d7b737.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2631fab3-04fe-4e37-40bd-ce0f22d7b737.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2631fab3-04fe-4e37-40bd-ce0f22d7b737.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXConstants.PxieDStarBLine Field

RFmxCdma2kMXConstantsPxieDStarBLine Field

The trigger is received on the PXIe DStar B trigger line.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxieDStarBLine = "PXIe_DStarB"
```

```text
Public Const PxieDStarBLine As String = "PXIe_DStarB"
```

###### Field Value

String

##### See Also

###### Reference

RFmxCdma2kMXConstants Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2743a897-3dd3-e328-efca-414b1430cde6.htm language=enus -->
## TOPIC 00022: rfmxcdma2kdotnet/html/2743a897-3dd3-e328-efca-414b1430cde6.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2743a897-3dd3-e328-efca-414b1430cde6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2743a897-3dd3-e328-efca-414b1430cde6.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled Enumeration

RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled Enumeration

Specifies whether to remove the I/Q gain imbalance before an EVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled
```

```text
Public Enumeration RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q gain imbalance is not removed before the EVM measurement. |
| True | 1 | I/Q gain imbalance is removed before the EVM measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2775fcba-0884-1b0b-b204-43001e8aa4ab.htm language=enus -->
## TOPIC 00023: rfmxcdma2kdotnet/html/2775fcba-0884-1b0b-b204-43001e8aa4ab.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2775fcba-0884-1b0b-b204-43001e8aa4ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2775fcba-0884-1b0b-b204-43001e8aa4ab.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXObw Class

RFmxCdma2kMXObw Class

Represents the OBW measurement.

##### Inheritance Hierarchy

RFmxCdma2kMXSubObject

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxCdma2kMXObw : RFmxCdma2kMXSubObject
```

```text
Public NotInheritable Class RFmxCdma2kMXObw
	Inherits RFmxCdma2kMXSubObject
```

The RFmxCdma2kMXObw type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxCdma2kMXObwConfiguration instance that provides methods to configure the OBW measurement |
|  | Results | Gets the RFmxCdma2kMXObwResults instance that provides methods to fetch and read the OBW measurement results. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/277cb62f-83c7-afa7-5dc5-e3c5e5a95601.htm language=enus -->
## TOPIC 00024: rfmxcdma2kdotnet/html/277cb62f-83c7-afa7-5dc5-e3c5e5a95601.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/277cb62f-83c7-afa7-5dc5-e3c5e5a95601.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/277cb62f-83c7-afa7-5dc5-e3c5e5a95601.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SlotPower Property

RFmxCdma2kMXSlotPower Property

RFmxCdma2kMXSlotPower

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxCdma2kMXSlotPower SlotPower { get; }
```

```text
Public ReadOnly Property SlotPower As RFmxCdma2kMXSlotPower
	Get
```

###### Property Value

RFmxCdma2kMXSlotPower

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/28c4a0e8-b9df-c3ee-dc32-b1ec4998463d.htm language=enus -->
## TOPIC 00025: rfmxcdma2kdotnet/html/28c4a0e8-b9df-c3ee-dc32-b1ec4998463d.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/28c4a0e8-b9df-c3ee-dc32-b1ec4998463d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/28c4a0e8-b9df-c3ee-dc32-b1ec4998463d.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration.SetReceiveFilterEnabled Method

RFmxCdma2kMXCdaConfigurationSetReceiveFilterEnabled Method

Sets whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReceiveFilterEnabled(
	string selectorString,
	RFmxCdma2kMXCdaReceiveFilterEnabled value
)
```

```text
Public Function SetReceiveFilterEnabled ( 
	selectorString As String,
	value As RFmxCdma2kMXCdaReceiveFilterEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXCdaReceiveFilterEnabled**
  - Specifies whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered.

###### Return Value

Int32

##### Remarks

CdaReceiveFilterEnabled

True

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2951b14f-6465-5ad5-b88b-bf5c33356a95.htm language=enus -->
## TOPIC 00026: rfmxcdma2kdotnet/html/2951b14f-6465-5ad5-b88b-bf5c33356a95.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2951b14f-6465-5ad5-b88b-bf5c33356a95.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2951b14f-6465-5ad5-b88b-bf5c33356a95.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.SetFftOverlapMode Method

RFmxCdma2kMXAcpConfigurationSetFftOverlapMode Method

Sets how the FFT overlap is applied to the acquired samples.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftOverlapMode(
	string selectorString,
	RFmxCdma2kMXAcpFftOverlapMode value
)
```

```text
Public Function SetFftOverlapMode ( 
	selectorString As String,
	value As RFmxCdma2kMXAcpFftOverlapMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXAcpFftOverlapMode**
  - Specifies how the FFT overlap is applied to the acquired samples.

###### Return Value

Int32

##### Remarks

AcpFftOverlapMode

Disabled

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2a6aaea7-da3f-00a3-c818-e3ecc61bc2cc.htm language=enus -->
## TOPIC 00027: rfmxcdma2kdotnet/html/2a6aaea7-da3f-00a3-c818-e3ecc61bc2cc.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2a6aaea7-da3f-00a3-c818-e3ecc61bc2cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2a6aaea7-da3f-00a3-c818-e3ecc61bc2cc.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXExtension Class

RFmxCdma2kMXExtension Class

Provides extension methods to create CDMA2k signal configuration. These methods are added to RFmxInstrMX class.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxCdma2kMXExtension
```

```text
<ExtensionAttribute>
Public NotInheritable Class RFmxCdma2kMXExtension
```

The RFmxCdma2kMXExtension type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetCdma2kSignalConfiguration(RFmxInstrMX) | Creates a new default CDMA2k signal configuration if it doesn't exist; otherwise, it returns the existing default CDMA2k signal configuration. |
|  | GetCdma2kSignalConfiguration(RFmxInstrMX, String) | Creates a CDMA2k signal configuration for specified signal name. Existing CDMA2k signal configuration is returned if specified signal name exists. |

Top

##### Remarks

For more information about RFmx Instruments, refer to the RFmx Instruments Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2b2877f6-a541-bd81-dc05-a9dd3ef9d58f.htm language=enus -->
## TOPIC 00028: rfmxcdma2kdotnet/html/2b2877f6-a541-bd81-dc05-a9dd3ef9d58f.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2b2877f6-a541-bd81-dc05-a9dd3ef9d58f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2b2877f6-a541-bd81-dc05-a9dd3ef9d58f.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemAveragingType Enumeration

RFmxCdma2kMXSemAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXSemAveragingType
```

```text
Public Enumeration RFmxCdma2kMXSemAveragingType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2cf1f9e0-16cb-b582-d150-9541ad82609a.htm language=enus -->
## TOPIC 00029: rfmxcdma2kdotnet/html/2cf1f9e0-16cb-b582-d150-9541ad82609a.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2cf1f9e0-16cb-b582-d150-9541ad82609a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2cf1f9e0-16cb-b582-d150-9541ad82609a.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccSpectrumInverted Enumeration

RFmxCdma2kMXModAccSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXModAccSpectrumInverted
```

```text
Public Enumeration RFmxCdma2kMXModAccSpectrumInverted
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measured spectrum is not inverted. |
| True | 1 | The measured spectrum is inverted. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2cf2d946-292e-dc3f-900b-2d96e33edea2.htm language=enus -->
## TOPIC 00030: rfmxcdma2kdotnet/html/2cf2d946-292e-dc3f-900b-2d96e33edea2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2cf2d946-292e-dc3f-900b-2d96e33edea2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2cf2d946-292e-dc3f-900b-2d96e33edea2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXExtension Methods

RFmxCdma2kMXExtension Methods

The [RFmxCdma2kMXExtension](2a6aaea7-da3f-00a3-c818-e3ecc61bc2cc.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetCdma2kSignalConfiguration(RFmxInstrMX) | Creates a new default CDMA2k signal configuration if it doesn't exist; otherwise, it returns the existing default CDMA2k signal configuration. |
|  | GetCdma2kSignalConfiguration(RFmxInstrMX, String) | Creates a CDMA2k signal configuration for specified signal name. Existing CDMA2k signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxCdma2kMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2e3f8666-861c-2171-ad98-44e8667a224a.htm language=enus -->
## TOPIC 00031: rfmxcdma2kdotnet/html/2e3f8666-861c-2171-ad98-44e8667a224a.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2e3f8666-861c-2171-ad98-44e8667a224a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2e3f8666-861c-2171-ad98-44e8667a224a.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.GetMeasurementStatus Method

RFmxCdma2kMXSemResultsGetMeasurementStatus Method

Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxCdma2kMXSemMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxCdma2kMXSemMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value RFmxCdma2kMXSemMeasurementStatus**
  - Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.

###### Return Value

Int32

##### Remarks

SemResultsMeasurementStatus

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2ee234a3-aeaf-d39b-620e-3ccaea33c457.htm language=enus -->
## TOPIC 00032: rfmxcdma2kdotnet/html/2ee234a3-aeaf-d39b-620e-3ccaea33c457.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2ee234a3-aeaf-d39b-620e-3ccaea33c457.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2ee234a3-aeaf-d39b-620e-3ccaea33c457.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.ResetAttribute Method

RFmxCdma2kMXResetAttribute Method

Resets the attribute to its default value.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ResetAttribute(
	string selectorString,
	RFmxCdma2kMXPropertyId attributeId
)
```

```text
Public Function ResetAttribute ( 
	selectorString As String,
	attributeId As RFmxCdma2kMXPropertyId
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2K Help for more information about configuring the selector string.
- **attributeId RFmxCdma2kMXPropertyId**
  - Specifies an attribute identifier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2ef8ad91-bd72-3726-b6fb-9ce3bd61fd22.htm language=enus -->
## TOPIC 00033: rfmxcdma2kdotnet/html/2ef8ad91-bd72-3726-b6fb-9ce3bd61fd22.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2ef8ad91-bd72-3726-b6fb-9ce3bd61fd22.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2ef8ad91-bd72-3726-b6fb-9ce3bd61fd22.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmConfiguration.GetAveragingEnabled Method

RFmxCdma2kMXQevmConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the QEVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxCdma2kMXQevmAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxCdma2kMXQevmAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXQevmAveragingEnabled**
  - Upon return, contains whether to enable averaging for the QEVM measurement.

###### Return Value

Int32

##### Remarks

QevmAveragingEnabled

False

##### See Also

###### Reference

RFmxCdma2kMXQevmConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2ef90bf7-76bd-eada-1f38-46e7ab8f8dc1.htm language=enus -->
## TOPIC 00034: rfmxcdma2kdotnet/html/2ef90bf7-76bd-eada-1f38-46e7ab8f8dc1.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2ef90bf7-76bd-eada-1f38-46e7ab8f8dc1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2ef90bf7-76bd-eada-1f38-46e7ab8f8dc1.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration.GetMeasurementEnabled Method

RFmxCdma2kMXCdaConfigurationGetMeasurementEnabled Method

Gets whether to enable the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetMeasurementEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the code domain analysis (CDA) measurement.

###### Return Value

Int32

##### Remarks

CdaMeasurementEnabled

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2f2750ab-6448-ba48-9b63-dba37de80e43.htm language=enus -->
## TOPIC 00035: rfmxcdma2kdotnet/html/2f2750ab-6448-ba48-9b63-dba37de80e43.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2f2750ab-6448-ba48-9b63-dba37de80e43.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2f2750ab-6448-ba48-9b63-dba37de80e43.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.ConfigureRadioConfiguration Method

RFmxCdma2kMXConfigureRadioConfiguration Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRadioConfiguration(
	string selectorString,
	RFmxCdma2kMXRadioConfiguration radioConfiguration
)
```

```text
Public Function ConfigureRadioConfiguration ( 
	selectorString As String,
	radioConfiguration As RFmxCdma2kMXRadioConfiguration
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **radioConfiguration RFmxCdma2kMXRadioConfiguration**
  - Specifies the radio configuration of the CDMA2k signal to be analyzed.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/2f890193-265a-0567-4496-a2f0cfa31889.htm language=enus -->
## TOPIC 00036: rfmxcdma2kdotnet/html/2f890193-265a-0567-4496-a2f0cfa31889.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/2f890193-265a-0567-4496-a2f0cfa31889.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/2f890193-265a-0567-4496-a2f0cfa31889.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.FetchUpperOffsetMarginArray Method

RFmxCdma2kMXSemResultsFetchUpperOffsetMarginArray Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUpperOffsetMarginArray(
	string selectorString,
	double timeout,
	ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[] measurementStatus,
	ref double[] margin,
	ref double[] marginFrequency,
	ref double[] marginAbsolutePower,
	ref double[] marginRelativePower
)
```

```text
Public Function FetchUpperOffsetMarginArray ( 
	selectorString As String,
	timeout As Double,
	ByRef measurementStatus As RFmxCdma2kMXSemUpperOffsetMeasurementStatus(),
	ByRef margin As Double(),
	ByRef marginFrequency As Double(),
	ByRef marginAbsolutePower As Double(),
	ByRef marginRelativePower As Double()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus RFmxCdma2kMXSemUpperOffsetMeasurementStatus**
  - Upon return, contains the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard.
- **margin Double**
  - Upon return, contains the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).
- **marginFrequency Double**
  - Upon return, contains the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz.
- **marginAbsolutePower Double**
  - Upon return, contains the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm.
- **marginRelativePower Double**
  - Upon return, contains the array of powers at which the margin occurred in each upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/306c7a0d-a567-1a68-7639-72bc18920776.htm language=enus -->
## TOPIC 00037: rfmxcdma2kdotnet/html/306c7a0d-a567-1a68-7639-72bc18920776.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/306c7a0d-a567-1a68-7639-72bc18920776.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/306c7a0d-a567-1a68-7639-72bc18920776.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration.SetMeasurementEnabled Method

RFmxCdma2kMXCdaConfigurationSetMeasurementEnabled Method

Sets whether to enable the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementEnabled(
	string selectorString,
	bool value
)
```

```text
Public Function SetMeasurementEnabled ( 
	selectorString As String,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Specifies whether to enable the code domain analysis (CDA) measurement.

###### Return Value

Int32

##### Remarks

CdaMeasurementEnabled

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/308b8b64-63c0-bf25-317e-78a4d67b3368.htm language=enus -->
## TOPIC 00038: rfmxcdma2kdotnet/html/308b8b64-63c0-bf25-317e-78a4d67b3368.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/308b8b64-63c0-bf25-317e-78a4d67b3368.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/308b8b64-63c0-bf25-317e-78a4d67b3368.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.GetAutoLevelInitialReferenceLevel Method

RFmxCdma2kMXGetAutoLevelInitialReferenceLevel Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoLevelInitialReferenceLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetAutoLevelInitialReferenceLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.The default value is 30 dBm.

###### Return Value

Int32

##### Remarks

AutoLevelInitialReferenceLevel

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/34535c6e-62c9-5d33-4f86-497653822a1e.htm language=enus -->
## TOPIC 00039: rfmxcdma2kdotnet/html/34535c6e-62c9-5d33-4f86-497653822a1e.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/34535c6e-62c9-5d33-4f86-497653822a1e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/34535c6e-62c9-5d33-4f86-497653822a1e.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpResults.GetCarrierAbsolutePower Method

RFmxCdma2kMXChpResultsGetCarrierAbsolutePower Method

Gets the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

ChpResultsCarrierAbsolutePower

##### See Also

###### Reference

RFmxCdma2kMXChpResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/34b658a6-bace-0fef-5bfb-7c447f6db82d.htm language=enus -->
## TOPIC 00040: rfmxcdma2kdotnet/html/34b658a6-bace-0fef-5bfb-7c447f6db82d.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/34b658a6-bace-0fef-5bfb-7c447f6db82d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/34b658a6-bace-0fef-5bfb-7c447f6db82d.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SetLinkDirection Method

RFmxCdma2kMXSetLinkDirection Method

Sets the link direction of the received signal.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLinkDirection(
	string selectorString,
	RFmxCdma2kMXLinkDirection value
)
```

```text
Public Function SetLinkDirection ( 
	selectorString As String,
	value As RFmxCdma2kMXLinkDirection
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXLinkDirection**
  - Specifies the link direction of the received signal.

###### Return Value

Int32

##### Remarks

LinkDirection

Uplink

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/35c1063c-eb99-66a2-f601-de3374d55def.htm language=enus -->
## TOPIC 00041: rfmxcdma2kdotnet/html/35c1063c-eb99-66a2-f601-de3374d55def.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/35c1063c-eb99-66a2-f601-de3374d55def.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/35c1063c-eb99-66a2-f601-de3374d55def.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.GetRadioConfiguration Method

RFmxCdma2kMXGetRadioConfiguration Method

Gets the radio configuration for the channel.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRadioConfiguration(
	string selectorString,
	out RFmxCdma2kMXRadioConfiguration value
)
```

```text
Public Function GetRadioConfiguration ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxCdma2kMXRadioConfiguration
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXRadioConfiguration**
  - Upon return, contains the radio configuration for the channel.

###### Return Value

Int32

##### Remarks

RadioConfiguration

RC3

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/37a1f462-5322-dc2b-4c1a-e8d90b8af852.htm language=enus -->
## TOPIC 00042: rfmxcdma2kdotnet/html/37a1f462-5322-dc2b-4c1a-e8d90b8af852.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/37a1f462-5322-dc2b-4c1a-e8d90b8af852.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/37a1f462-5322-dc2b-4c1a-e8d90b8af852.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpConfiguration.SetSweepTimeInterval Method

RFmxCdma2kMXChpConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxCdma2kMXChpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSweepTimeInterval(
	string selectorString,
	double value
)
```

```text
Public Function SetSweepTimeInterval ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ChpSweepTimeInterval

##### See Also

###### Reference

RFmxCdma2kMXChpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/3aa08374-c7c4-d506-666b-cf8bc048610d.htm language=enus -->
## TOPIC 00043: rfmxcdma2kdotnet/html/3aa08374-c7c4-d506-666b-cf8bc048610d.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/3aa08374-c7c4-d506-666b-cf8bc048610d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/3aa08374-c7c4-d506-666b-cf8bc048610d.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SetWalshCodeNumber Method

RFmxCdma2kMXSetWalshCodeNumber Method

SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode)

UserDefined

"channel(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetWalshCodeNumber(
	string selectorString,
	int value
)
```

```text
Public Function SetWalshCodeNumber ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the channel number. Example: "channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value Int32**
  - Specifies the Walsh code number of a specific user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method.

###### Return Value

Int32

##### Remarks

WalshCodeNumber

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/3b1402e1-e7b7-6518-4bd2-1118b040859a.htm language=enus -->
## TOPIC 00044: rfmxcdma2kdotnet/html/3b1402e1-e7b7-6518-4bd2-1118b040859a.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/3b1402e1-e7b7-6518-4bd2-1118b040859a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/3b1402e1-e7b7-6518-4bd2-1118b040859a.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaIQOffsetRemovalEnabled Enumeration

RFmxCdma2kMXCdaIQOffsetRemovalEnabled Enumeration

Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXCdaIQOffsetRemovalEnabled
```

```text
Public Enumeration RFmxCdma2kMXCdaIQOffsetRemovalEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q offset is not removed before the CDA measurement. |
| True | 1 | I/Q offset is removed before the CDA measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/3d23bd78-b9af-0a89-fe58-16a2db7eee98.htm language=enus -->
## TOPIC 00045: rfmxcdma2kdotnet/html/3d23bd78-b9af-0a89-fe58-16a2db7eee98.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/3d23bd78-b9af-0a89-fe58-16a2db7eee98.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/3d23bd78-b9af-0a89-fe58-16a2db7eee98.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmAveragingEnabled Enumeration

RFmxCdma2kMXQevmAveragingEnabled Enumeration

Specifies whether to enable averaging for the QEVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXQevmAveragingEnabled
```

```text
Public Enumeration RFmxCdma2kMXQevmAveragingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The averaging is disabled for the measurement. |
| True | 1 | The averaging is enabled for the measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/3dc027f3-fe04-b978-a703-35fe30b62454.htm language=enus -->
## TOPIC 00046: rfmxcdma2kdotnet/html/3dc027f3-fe04-b978-a703-35fe30b62454.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/3dc027f3-fe04-b978-a703-35fe30b62454.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/3dc027f3-fe04-b978-a703-35fe30b62454.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.GetRbwFilterAutoBandwidth Method

RFmxCdma2kMXAcpConfigurationGetRbwFilterAutoBandwidth Method

Gets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterAutoBandwidth(
	string selectorString,
	out RFmxCdma2kMXAcpRbwAutoBandwidth value
)
```

```text
Public Function GetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxCdma2kMXAcpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXAcpRbwAutoBandwidth**
  - Upon return, contains whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

AcpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/40b7af19-8e6f-4979-c91e-a719b2b2e1fe.htm language=enus -->
## TOPIC 00047: rfmxcdma2kdotnet/html/40b7af19-8e6f-4979-c91e-a719b2b2e1fe.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/40b7af19-8e6f-4979-c91e-a719b2b2e1fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/40b7af19-8e6f-4979-c91e-a719b2b2e1fe.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpConfiguration Class

RFmxCdma2kMXChpConfiguration Class

Provides methods to configure the CHP measurement

##### Inheritance Hierarchy

RFmxCdma2kMXSubObject

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxCdma2kMXChpConfiguration : RFmxCdma2kMXSubObject
```

```text
Public NotInheritable Class RFmxCdma2kMXChpConfiguration
	Inherits RFmxCdma2kMXSubObject
```

The RFmxCdma2kMXChpConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the CHP measurement. |
|  | ConfigureRbwFilter | Configures the RBW filter. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXChpAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the CHP measurement. |
|  | GetAveragingType(String, RFmxCdma2kMXChpAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
|  | GetAveragingType(String, RFmxCdma2kMXSemAveragingType) | Obsolete. Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIntegrationBandwidth | Gets the CHP carrier integration bandwidth. This value is expressed in Hz. |
|  | GetMeasurementEnabled | Gets whether to enable the CHP measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the CHP measurement. |
|  | GetRbwFilterAutoBandwidth | Gets whether the measurement computes the RBW. |
|  | GetRbwFilterBandwidth | Gets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | GetRbwFilterType | Gets the shape of the digital RBW filter. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXChpAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the CHP measurement. |
|  | SetAveragingType(String, RFmxCdma2kMXChpAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
|  | SetAveragingType(String, RFmxCdma2kMXSemAveragingType) | Obsolete. Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the CHP measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the CHP measurement. |
|  | SetRbwFilterAutoBandwidth | Sets whether the measurement computes the RBW. |
|  | SetRbwFilterBandwidth | Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
|  | SetRbwFilterType | Sets the shape of the digital RBW filter. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/45f0c089-203d-eecc-acf2-172a4a8b9201.htm language=enus -->
## TOPIC 00048: rfmxcdma2kdotnet/html/45f0c089-203d-eecc-acf2-172a4a8b9201.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/45f0c089-203d-eecc-acf2-172a4a8b9201.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/45f0c089-203d-eecc-acf2-172a4a8b9201.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXPropertyId Enumeration

RFmxCdma2kMXPropertyId Enumeration

Specifies all the attribute identifiers.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXPropertyId
```

```text
Public Enumeration RFmxCdma2kMXPropertyId
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| CenterFrequency | 6,291,457 | Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. |
| ReferenceLevel | 6,291,458 | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ExternalAttenuation | 6,291,459 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| TriggerType | 6,291,460 | Specifies the trigger type. |
| DigitalEdgeTriggerSource | 6,291,461 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to DigitalEdge. |
| DigitalEdgeTriggerEdge | 6,291,462 | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to DigitalEdge. |
| IQPowerEdgeTriggerSource | 6,291,463 | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerLevel | 6,291,464 | Specifies the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(String, RFmxCdma2kMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerSlope | 6,291,465 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |
| TriggerDelay | 6,291,466 | Specifies the trigger delay time. This value is expressed in seconds. |
| TriggerMinimumQuietTimeMode | 6,291,467 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 6,291,468 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxCdma2kMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| LinkDirection | 6,291,469 | Specifies the link direction of the received signal. |
| BandClass | 6,291,472 | Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0. |
| RadioConfiguration | 6,291,473 | Specifies the radio configuration for the channel. |
| ChannelConfigurationMode | 6,291,474 | Specifies whether to detect the channels automatically or to use a specified channel configuration. |
| NumberOfChannels | 6,291,478 | Specifies the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined. |
| WalshCodeLength | 6,291,479 | Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This method is used only when you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method. |
| WalshCodeNumber | 6,291,480 | Specifies the Walsh code number of a specific user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method. |
| Branch | 6,291,481 | Specifies the branch on which a specific user-defined channel is mapped. This method is used only when you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method. |
| UplinkSpreadingLongCodeMask | 6,291,486 | Specifies the long code mask for reverse link spreading. |
| DownlinkSpreadingPNOffset | 6,291,488 | Specified the PN offset in increments of 64 chips for forward link. |
| ReferenceLevelHeadroom | 6,295,548 | Specifies the margin RFmx adds to the Reference Level method. |
| SelectedPorts | 6,295,549 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstrMX.GetAvailablePorts Method to get the valid port names. |
| IQPowerEdgeTriggerLevelType | 6,295,551 | Specifies the reference for the IQ Power Edge Level Type method. This method is used only when you set the SetTriggerType(String, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |
| AcpMeasurementEnabled | 6,295,552 | Specifies whether to enable the ACP measurement. |
| AcpCarrierIntegrationBandwidth | 6,295,557 | Returns the ACP carrier integration bandwidth. This value is expressed in Hz. |
| AcpNumberOfOffsets | 6,295,560 | Specifies the number of offset channels. |
| AcpOffsetFrequency | 6,295,562 | Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. |
| AcpOffsetIntegrationBandwidth | 6,295,566 | Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. |
| AcpMeasurementMethod | 6,295,570 | Specifies the method for performing the ACP measurement. |
| AcpNumberOfAnalysisThreads | 6,295,572 | Specifies the maximum number of threads used for parallelism for the ACP measurement. |
| AcpAveragingCount | 6,295,573 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXAcpAveragingEnabled) method to True. |
| AcpAveragingEnabled | 6,295,574 | Specifies whether to enable averaging for the ACP measurement. |
| AcpAveragingType | 6,295,576 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
| AcpRbwFilterAutoBandwidth | 6,295,579 | Specifies whether the measurement computes the RBW. |
| AcpRbwFilterBandwidth | 6,295,580 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| AcpRbwFilterType | 6,295,581 | Specifies the shape of the digital RBW filter. |
| AcpSweepTimeAuto | 6,295,582 | Specifies whether the measurement computes the sweep time. |
| AcpSweepTimeInterval | 6,295,583 | Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |
| AcpNoiseCompensationEnabled | 6,295,584 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| AcpAllTracesEnabled | 6,295,585 | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| AcpResultsCarrierAbsolutePower | 6,295,590 | Returns the absolute measured carrier power. This value is expressed in dBm. |
| AcpResultsLowerOffsetAbsolutePower | 6,295,596 | Returns the absolute measured lower offset channel power. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| AcpResultsLowerOffsetRelativePower | 6,295,597 | Returns the lower offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| AcpResultsUpperOffsetAbsolutePower | 6,295,602 | Returns the absolute measured upper offset channel power. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| AcpResultsUpperOffsetRelativePower | 6,295,603 | Returns the upper offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| AcpIFOutputPowerOffsetAuto | 6,295,604 | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is used only if you set the SetMeasurementMethod(String, RFmxCdma2kMXAcpMeasurementMethod) method to DynamicRange. |
| AcpNearIFOutputPowerOffset | 6,295,605 | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxCdma2kMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(String, RFmxCdma2kMXAcpIFOutputPowerOffsetAuto) method to False. |
| AcpFarIFOutputPowerOffset | 6,295,606 | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxCdma2kMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(String, RFmxCdma2kMXAcpIFOutputPowerOffsetAuto) method to False. |
| AcpSequentialFftSize | 6,295,608 | Specifies the FFT size, when you set the SetMeasurementMethod(String, RFmxCdma2kMXAcpMeasurementMethod) method to SequentialFft. |
| AcpFftOverlapMode | 6,295,609 | Specifies how the FFT overlap is applied to the acquired samples. |
| AcpFftOverlap | 6,295,610 | Returns the number of samples to overlap between consecutive chunks while performing FFT. This value is expressed as a percentage of Sequential FFT Size when you set the ACP Measurement Method to Sequential FFT. |
| ChpMeasurementEnabled | 6,303,744 | Specifies whether to enable the CHP measurement. |
| ChpIntegrationBandwidth | 6,303,746 | Returns the CHP carrier integration bandwidth. This value is expressed in Hz. |
| ChpNumberOfAnalysisThreads | 6,303,747 | Specifies the maximum number of threads used for parallelism for the CHP measurement. |
| ChpAveragingCount | 6,303,750 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXChpAveragingEnabled) method to True. |
| ChpAveragingEnabled | 6,303,751 | Specifies whether to enable averaging for the CHP measurement. |
| ChpAveragingType | 6,303,753 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
| ChpRbwFilterAutoBandwidth | 6,303,756 | Specifies whether the measurement computes the RBW. |
| ChpRbwFilterBandwidth | 6,303,757 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| ChpRbwFilterType | 6,303,758 | Specifies the shape of the digital RBW filter. |
| ChpSweepTimeAuto | 6,303,761 | Specifies whether the measurement computes the sweep time. |
| ChpSweepTimeInterval | 6,303,762 | Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
| ChpAllTracesEnabled | 6,303,764 | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| ChpResultsCarrierAbsolutePower | 6,303,765 | Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. |
| ObwMeasurementEnabled | 6,316,032 | Specifies whether to enable the OBW measurement. |
| ObwNumberOfAnalysisThreads | 6,316,035 | Specifies the maximum number of threads used for parallelism for the OBW measurement. |
| ObwSpan | 6,316,036 | Returns the frequency span of the OBW measurement. This value is expressed in Hz. |
| ObwAveragingCount | 6,316,038 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXObwAveragingEnabled) method to True. |
| ObwAveragingEnabled | 6,316,039 | Specifies whether to enable averaging for the OBW measurement. |
| ObwAveragingType | 6,316,041 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| ObwRbwFilterAutoBandwidth | 6,316,044 | Specifies whether the measurement computes the RBW. |
| ObwRbwFilterBandwidth | 6,316,045 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| ObwRbwFilterType | 6,316,046 | Specifies the shape of the digital RBW filter. |
| ObwSweepTimeAuto | 6,316,047 | Specifies whether the measurement computes the sweep time. |
| ObwSweepTimeInterval | 6,316,048 | Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |
| ObwAllTracesEnabled | 6,316,050 | Specifies whether to enable the traces to be stored and retrieved after performing the OBW. |
| ObwResultsOccupiedBandwidth | 6,316,051 | Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. |
| ObwResultsAbsolutePower | 6,316,052 | Returns the absolute power measured in the OBW. This value is expressed in dBm. |
| ObwResultsStartFrequency | 6,316,053 | Returns the start frequency of the OBW. This value is expressed in Hz. |
| ObwResultsStopFrequency | 6,316,054 | Returns the stop frequency of the OBW. This value is expressed in Hz. |
| SemMeasurementEnabled | 6,324,224 | Specifies whether to enable the SEM measurement. |
| SemCarrierIntegrationBandwidth | 6,324,229 | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. |
| SemNumberOfOffsets | 6,324,235 | Returns the number of SEM offset segments. |
| SemOffsetBandwidthIntegral | 6,324,236 | Returns the bandwidth integral for a specific offset segment. |
| SemOffsetStartFrequency | 6,324,244 | Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| SemOffsetStopFrequency | 6,324,245 | Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| SemOffsetRbwFilterBandwidth | 6,324,247 | Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. |
| SemOffsetRbwFilterType | 6,324,248 | Returns the type of RBW filter used to sweep the offset segment. |
| SemNumberOfAnalysisThreads | 6,324,253 | Specifies the maximum number of threads used for parallelism for the SEM measurement. |
| SemAveragingCount | 6,324,254 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled) method to True. |
| SemAveragingEnabled | 6,324,255 | Specifies whether to enable averaging for the SEM measurement. |
| SemAveragingType | 6,324,257 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
| SemSweepTimeAuto | 6,324,261 | Specifies whether the measurement computes the sweep time. |
| SemSweepTimeInterval | 6,324,262 | Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| SemAllTracesEnabled | 6,324,263 | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| SemResultsMeasurementStatus | 6,324,265 | Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. |
| SemResultsCarrierAbsoluteIntegratedPower | 6,324,269 | Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. |
| SemResultsLowerOffsetAbsoluteIntegratedPower | 6,324,276 | Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetRelativeIntegratedPower | 6,324,277 | Returns the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetAbsolutePeakPower | 6,324,278 | Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetRelativePeakPower | 6,324,279 | Returns the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetPeakFrequency | 6,324,280 | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetMargin | 6,324,281 | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetMarginAbsolutePower | 6,324,282 | Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetMarginRelativePower | 6,324,283 | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetMarginFrequency | 6,324,284 | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsLowerOffsetMeasurementStatus | 6,324,285 | Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetAbsoluteIntegratedPower | 6,324,289 | Returns the power measured in the upper (positive) offset segment. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetRelativeIntegratedPower | 6,324,290 | Returns the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetAbsolutePeakPower | 6,324,291 | Returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetRelativePeakPower | 6,324,292 | Returns the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetPeakFrequency | 6,324,293 | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetMargin | 6,324,294 | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetMarginAbsolutePower | 6,324,295 | Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetMarginRelativePower | 6,324,296 | Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetMarginFrequency | 6,324,297 | Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |
| SemResultsUpperOffsetMeasurementStatus | 6,324,298 | Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result. |
| ResultFetchTimeout | 6,340,608 | Specifies the time to wait before results are available. This value is expressed in seconds.Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete before fetching the measurement. |
| AutoLevelInitialReferenceLevel | 6,344,704 | Specifies the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.The default value is 30 dBm. |
| LimitedConfigurationChange | 6,344,707 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| ModAccMeasurementEnabled | 6,361,088 | Specifies whether to enable the modulation accuracy (ModAcc) measurement. |
| ModAccSynchronizationMode | 6,361,093 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| ModAccMeasurementOffset | 6,361,094 | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXModAccSynchronizationMode) method. This value is expressed in slots. |
| ModAccMeasurementLength | 6,361,095 | Specifies the duration of the modulation accuracy (ModAcc) measurement. This value is expressed in slots. |
| ModAccIQOffsetRemovalEnabled | 6,361,096 | Specifies whether to remove the I/Q offset before an EVM measurement. |
| ModAccSpectrumInverted | 6,361,097 | Specifies whether the spectrum of the signal is inverted. |
| ModAccMultiCarrierFilterEnabled | 6,361,104 | Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers. |
| ModAccAllTracesEnabled | 6,361,109 | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
| ModAccResultsRmsEvm | 6,361,120 | Returns the RMS EVM of the composite signal. This value is expressed as a percentage. |
| ModAccResultsPeakEvm | 6,361,121 | Returns the peak EVM of the composite signal. This value is expressed as a percentage. |
| ModAccResultsRmsMagnitudeError | 6,361,122 | Returns the RMS magnitude error of the composite signal. This value is expressed as a percentage. |
| ModAccResultsRmsPhaseError | 6,361,123 | Returns the RMS phase error of the composite signal. This value is expressed in degrees. |
| ModAccResultsIQOriginOffset | 6,361,124 | Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. |
| ModAccResultsIQGainImbalance | 6,361,125 | Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. |
| ModAccResultsIQQuadratureError | 6,361,126 | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |
| ModAccResultsFrequencyError | 6,361,127 | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
| ModAccResultsRho | 6,361,128 | Returns the correlation of the received signal with the reference signal normalized by the signal power. The value of Rho is between 0 and 1.0, inclusive. A value of 1.0 indicates that the received signal and the reference signal are perfectly correlated. |
| ModAccResultsPeakCde | 6,361,129 | Returns the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 16 is used. The CDEs are computed separately for I and Q branches. |
| ModAccResultsPeakCdeWalshCodeNumber | 6,361,131 | Returns the Walsh code number corresponding to the value that the GetPeakCde(String, Double) method returns. |
| ModAccResultsPeakActiveCde | 6,361,132 | Returns the maximum value among the code domain errors (CDEs) for all active channels. This value is expressed in dB. The active CDEs are computed by projecting the descrambled error vector onto the codes of each active channel. The active CDE is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. |
| ModAccResultsPeakActiveCdeWalshCodeLength | 6,361,133 | Returns the Walsh code length of the channel corresponding to the value that the GetPeakActiveCde(String, Double) method returns. |
| ModAccResultsPeakActiveCdeWalshCodeNumber | 6,361,135 | Returns the Walsh code number of the channel corresponding to the value that the GetPeakActiveCde(String, Double) method returns. |
| ModAccResultsSlotTimingError | 6,361,136 | Returns the measured timing error from the beginning of the acquisition to the location of the first slot acquired. This value is expressed in seconds. |
| ModAccResultsChipRateError | 6,361,139 | Returns the chip rate error. This value is expressed in parts per million (ppm). |
| ModAccResultsNumberOfDetectedChannels | 6,361,140 | Returns the total number of detected channels. If you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the number of configured channels. |
| ModAccResultsDetectedWalshCodeLength | 6,361,141 | Returns the Walsh code length of the detected channel. If you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the Walsh code length of the configured channel.Use "channel(n)" as the Selector Strings to read this method. |
| ModAccResultsDetectedWalshCodeNumber | 6,361,142 | Returns the Walsh code number of the detected channel. If you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the Walsh code number of the configured channel.Use "channel(n)" as the Selector Strings to read this method. |
| ModAccResultsDetectedBranch | 6,361,143 | Returns the branch of the detected channel. If you set the SetChannelConfigurationMode(String, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the branch of the configured channel.Use "channel(n)" as the Selector Strings to read this method. |
| ModAccResultsPeakCdeBranch | 6,361,144 | Returns the branch corresponding to the value that the GetPeakCde(String, Double) method returns. |
| ModAccResultsPeakActiveCdeBranch | 6,361,145 | Returns the branch of the channel corresponding to the value that the GetPeakActiveCde(String, Double) method returns. |
| ModAccIQGainImbalanceRemovalEnabled | 6,361,249 | Specifies whether to remove the I/Q gain imbalance before an EVM measurement. |
| ModAccIQQuadratureErrorRemovalEnabled | 6,361,250 | Specifies whether to remove the I/Q quadrature error before an EVM measurement. |
| ModAccReceiveFilterEnabled | 6,361,251 | Specifies whether to enable the received filter for the ModAcc measurement. For RC1/2, this property refers to the band-limiting filter specified in the Chapter 6.4.2.1 of 3GPP2 C.S0011-E. For RC3/4, this property refers to the complementary filter specified in the Chapter 6.4.2.2 of 3GPP2 C.S0011-E. |
| QevmMeasurementEnabled | 6,365,184 | Specifies whether to enable the QEVM measurement. |
| QevmMeasurementLength | 6,365,186 | Specifies the number of chips used for a single measurement. |
| QevmAveragingEnabled | 6,365,187 | Specifies whether to enable averaging for the QEVM measurement. |
| QevmAveragingCount | 6,365,188 | Specifies the number of measurements used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXQevmAveragingEnabled) method to True. |
| QevmSpectrumInverted | 6,365,189 | Specifies whether the spectrum of the signal is inverted. |
| QevmIQOffsetRemovalEnabled | 6,365,190 | Specifies whether to remove I/Q offset before QEVM measurement. |
| QevmIQGainImbalanceRemovalEnabled | 6,365,191 | Specifies whether to remove I/Q gain imbalance before QEVM measurement. |
| QevmIQQuadratureErrorRemovalEnabled | 6,365,192 | Specifies whether to remove I/Q quadrature error before QEVM measurement. |
| QevmReceiveFilterEnabled | 6,365,193 | Specifies whether to enable the received filter for the QEVM measurement. |
| QevmAllTracesEnabled | 6,365,194 | Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |
| QevmNumberOfAnalysisThreads | 6,365,195 | Specifies the maximum number of threads used for parallelism for the QEVM measurement. |
| QevmResultsMeanRmsEvm | 6,365,197 | Returns the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. |
| QevmResultsMaximumRmsEvm | 6,365,198 | Returns the maximum RMS EVM of the received signal. This value is expressed as a percentage. |
| QevmResultsMeanPeakEvm | 6,365,199 | Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage. |
| QevmResultsMaximumPeakEvm | 6,365,200 | Returns the maximum peak EVM of the received signal. This value is expressed as a percentage. |
| QevmResultsMeanMagnitudeError | 6,365,201 | Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage. |
| QevmResultsMaximumMagnitudeError | 6,365,202 | Returns the maximum magnitude error of the received signal. This value is expressed as a percentage. |
| QevmResultsMeanPhaseError | 6,365,203 | Returns the mean averaged phase error of the received signal. This value is expressed in degrees. |
| QevmResultsMaximumPhaseError | 6,365,204 | Returns the maximum phase error of the received signal. This value is expressed in degrees. |
| QevmResultsMeanFrequencyError | 6,365,205 | Returns the mean averaged frequency error of the received signal. This value is expressed in Hz. |
| QevmResultsMaximumFrequencyError | 6,365,206 | Returns the maximum frequency error of the received signal. This value is expressed in Hz. |
| QevmResultsMeanIQOriginOffset | 6,365,207 | Returns the mean averaged origin offset of the received signal. This value is expressed in dB. |
| QevmResultsMaximumIQOriginOffset | 6,365,208 | Returns the maximum origin offset of the received signal. This value is expressed in dB. |
| QevmResultsMeanIQGainImbalance | 6,365,209 | Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. |
| QevmResultsMaximumIQGainImbalance | 6,365,210 | Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. |
| QevmResultsMeanIQQuadratureError | 6,365,211 | Returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| QevmResultsMaximumIQQuadratureError | 6,365,212 | Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| QevmResultsMeanChipRateError | 6,365,213 | Returns the mean chip rate error. This value is expressed in parts per million (ppm). |
| QevmResultsMaximumChipRateError | 6,365,214 | Returns the maximum chip rate error. This value is expressed in parts per million (ppm). |
| CdaMeasurementEnabled | 6,369,280 | Specifies whether to enable the code domain analysis (CDA) measurement. |
| CdaSynchronizationMode | 6,369,282 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| CdaMeasurementOffset | 6,369,283 | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. |
| CdaMeasurementLength | 6,369,284 | Specifies the duration of code domain measurement. This value is expressed in slots. |
| CdaBaseSpreadingFactor | 6,369,285 | Specifies the base spreading factor used to calculate the code domain power traces. |
| CdaMeasurementChannelWalshCodeLength | 6,369,286 | Specifies the Walsh code length of a channel subject to channel specific analysis. |
| CdaMeasurementChannelWalshCodeNumber | 6,369,287 | Specifies the Walsh code number of a channel subject to channel specific analysis. |
| CdaMeasurementChannelBranch | 6,369,288 | Specifies the branch of a channel subject to channel specific analysis. |
| CdaPowerUnit | 6,369,289 | Specifies the measurement unit of the measured code domain power results. |
| CdaSpectrumInverted | 6,369,290 | Specifies whether the spectrum of the signal is inverted. |
| CdaIQOffsetRemovalEnabled | 6,369,291 | Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
| CdaIQGainImbalanceRemovalEnabled | 6,369,292 | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
| CdaIQQuadratureErrorRemovalEnabled | 6,369,293 | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
| CdaReceiveFilterEnabled | 6,369,294 | Specifies whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered. |
| CdaAllTracesEnabled | 6,369,295 | Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |
| CdaResultsRmsSymbolEvm | 6,369,298 | Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| CdaResultsPeakSymbolEvm | 6,369,299 | Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| CdaResultsRmsSymbolMagnitudeError | 6,369,300 | Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |
| CdaResultsRmsSymbolPhaseError | 6,369,301 | Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |
| CdaResultsMeanSymbolPower | 6,369,302 | Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dB, and in dBm, when you set the CDA Pwr Unit method to dBm. |
| CdaResultsTotalPower | 6,369,303 | Returns the mean power of the received signal. This value is expressed in dBm. |
| CdaResultsTotalActivePower | 6,369,304 | Returns the sum of the powers of all active code channels. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsMeanActivePower | 6,369,305 | Returns the average power of all active code channels. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsPeakActivePower | 6,369,306 | Returns the maximum power among all active code channels. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsMeanInactivePower | 6,369,307 | Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsPeakInactivePower | 6,369,308 | Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsIMeanActivePower | 6,369,309 | Returns the average power of all active code channels measured on the I-branch. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsIPeakInactivePower | 6,369,310 | Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsQMeanActivePower | 6,369,311 | Returns the average power of all active code channels measured on the Q-branch. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsQPeakInactivePower | 6,369,312 | Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |
| CdaResultsMeanPilotPower | 6,369,313 | Returns the mean power of the R-PICH.Returns the mean power value in dB, when you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dB.Returns the mean power value in dBm, when you set the CDA Pwr Unit method to dBm. |
| CdaResultsIQOriginOffset | 6,369,314 | Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. |
| CdaResultsIQGainImbalance | 6,369,315 | Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. |
| CdaResultsIQQuadratureError | 6,369,316 | Returns the I/Q quadrature error of the composite signal averaged over all measured slots. This value is expressed in degrees. |
| CdaResultsFrequencyError | 6,369,317 | Returns the frequency error. This value is expressed in Hz. |
| CdaResultsChipRateError | 6,369,318 | Returns the chip rate error. This value is expressed in parts per million (ppm). |
| SlotPowerMeasurementEnabled | 6,373,376 | Specifies whether to enable the SlotPower measurement. |
| SlotPowerSynchronizationMode | 6,373,378 | Specifies whether the measurement is performed from the frame or slot boundary. |
| SlotPowerMeasurementOffset | 6,373,379 | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXSlotPowerSynchronizationMode) method. This value is expressed in slots. |
| SlotPowerMeasurementLength | 6,373,380 | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |
| SlotPowerSpectrumInverted | 6,373,381 | Specifies whether the spectrum of the signal is inverted. |
| SlotPowerReceiveFilterEnabled | 6,373,382 | Specifies whether to enable the received filter for the SlotPower measurement. Use this method to disable the filter, if the received signal is already filtered. |
| SlotPhaseMeasurementEnabled | 6,377,472 | Specifies whether to enable the SlotPhase measurement. |
| SlotPhaseSynchronizationMode | 6,377,474 | Specifies whether the measurement is performed from the frame or slot boundary. |
| SlotPhaseMeasurementOffset | 6,377,475 | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXSlotPhaseSynchronizationMode) method. This value is expressed in slots. |
| SlotPhaseMeasurementLength | 6,377,476 | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |
| SlotPhaseSpectrumInverted | 6,377,477 | Specifies whether the spectrum of the signal is inverted. |
| SlotPhaseReceiveFilterEnabled | 6,377,478 | Specifies whether to enable the received filter for the SlotPhase measurement. Use this method to disable the filter, if the received signal is already filtered. |
| SlotPhaseTransientDuration | 6,377,479 | Specifies the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. |
| SlotPhaseAllTracesEnabled | 6,377,480 | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| SlotPhaseResultsMaximumPhaseDiscontinuity | 6,377,483 | Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/46262cfc-1876-e5b6-a622-0195262573d2.htm language=enus -->
## TOPIC 00049: rfmxcdma2kdotnet/html/46262cfc-1876-e5b6-a622-0195262573d2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/46262cfc-1876-e5b6-a622-0195262573d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/46262cfc-1876-e5b6-a622-0195262573d2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration.SetIQQuadratureErrorRemovalEnabled Method

RFmxCdma2kMXCdaConfigurationSetIQQuadratureErrorRemovalEnabled Method

Sets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQQuadratureErrorRemovalEnabled(
	string selectorString,
	RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled value
)
```

```text
Public Function SetIQQuadratureErrorRemovalEnabled ( 
	selectorString As String,
	value As RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled**
  - Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.

###### Return Value

Int32

##### Remarks

CdaIQQuadratureErrorRemovalEnabled

False

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/465134ec-bf37-3728-6566-f5be9d27b668.htm language=enus -->
## TOPIC 00050: rfmxcdma2kdotnet/html/465134ec-bf37-3728-6566-f5be9d27b668.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/465134ec-bf37-3728-6566-f5be9d27b668.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/465134ec-bf37-3728-6566-f5be9d27b668.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSlotPhaseResults.GetMaximumPhaseDiscontinuity Method

RFmxCdma2kMXSlotPhaseResultsGetMaximumPhaseDiscontinuity Method

Gets the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumPhaseDiscontinuity(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumPhaseDiscontinuity ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

SlotPhaseResultsMaximumPhaseDiscontinuity

##### See Also

###### Reference

RFmxCdma2kMXSlotPhaseResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/46e40c86-e6f2-3a9d-2398-66e6bbd900aa.htm language=enus -->
## TOPIC 00051: rfmxcdma2kdotnet/html/46e40c86-e6f2-3a9d-2398-66e6bbd900aa.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/46e40c86-e6f2-3a9d-2398-66e6bbd900aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/46e40c86-e6f2-3a9d-2398-66e6bbd900aa.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.SetRbwFilterBandwidth Method

RFmxCdma2kMXAcpConfigurationSetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXAcpRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetRbwFilterBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxCdma2kMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpRbwFilterBandwidth

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/480bf9fe-470b-94f4-86dc-0621dfbe9561.htm language=enus -->
## TOPIC 00052: rfmxcdma2kdotnet/html/480bf9fe-470b-94f4-86dc-0621dfbe9561.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/480bf9fe-470b-94f4-86dc-0621dfbe9561.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/480bf9fe-470b-94f4-86dc-0621dfbe9561.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemConfiguration Class

RFmxCdma2kMXSemConfiguration Class

Provides methods to configure the SEM measurement

##### Inheritance Hierarchy

RFmxCdma2kMXSubObject

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxCdma2kMXSemConfiguration : RFmxCdma2kMXSubObject
```

```text
Public NotInheritable Class RFmxCdma2kMXSemConfiguration
	Inherits RFmxCdma2kMXSubObject
```

The RFmxCdma2kMXSemConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the SEM measurement. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the SEM measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
|  | GetCarrierIntegrationBandwidth | Gets the SEM carrier integration bandwidth. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the SEM measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the SEM measurement. |
|  | GetNumberOfOffsets | Gets the number of SEM offset segments. |
|  | GetOffsetBandwidthIntegral | Gets the bandwidth integral for a specific offset segment. |
|  | GetOffsetRbwFilterBandwidth | Gets the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. |
|  | GetOffsetRbwFilterType | Gets the type of RBW filter used to sweep the offset segment. |
|  | GetOffsetStartFrequency | Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | GetOffsetStopFrequency | Gets the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the SEM measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the SEM measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the SEM measurement. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/488c4541-8b86-42ad-2dae-b4009730a4fe.htm language=enus -->
## TOPIC 00053: rfmxcdma2kdotnet/html/488c4541-8b86-42ad-2dae-b4009730a4fe.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/488c4541-8b86-42ad-2dae-b4009730a4fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/488c4541-8b86-42ad-2dae-b4009730a4fe.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.Commit Method

RFmxCdma2kMXCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int Commit(
	string selectorString
)
```

```text
Public Function Commit ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/502398ec-526c-f9c8-6857-f8d2efa29493.htm language=enus -->
## TOPIC 00054: rfmxcdma2kdotnet/html/502398ec-526c-f9c8-6857-f8d2efa29493.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/502398ec-526c-f9c8-6857-f8d2efa29493.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/502398ec-526c-f9c8-6857-f8d2efa29493.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.DeleteSignalConfiguration Method

RFmxCdma2kMXDeleteSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int DeleteSignalConfiguration()
```

```text
Public Function DeleteSignalConfiguration As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/50933ecf-cbd7-e3a1-d620-215e9a6f52dc.htm language=enus -->
## TOPIC 00055: rfmxcdma2kdotnet/html/50933ecf-cbd7-e3a1-d620-215e9a6f52dc.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/50933ecf-cbd7-e3a1-d620-215e9a6f52dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/50933ecf-cbd7-e3a1-d620-215e9a6f52dc.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.SetRbwFilterType Method

RFmxCdma2kMXAcpConfigurationSetRbwFilterType Method

Sets the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxCdma2kMXAcpRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxCdma2kMXAcpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXAcpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

AcpRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/5112b573-2577-009e-2d76-b403c6de700d.htm language=enus -->
## TOPIC 00056: rfmxcdma2kdotnet/html/5112b573-2577-009e-2d76-b403c6de700d.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/5112b573-2577-009e-2d76-b403c6de700d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/5112b573-2577-009e-2d76-b403c6de700d.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.ConfigureUplinkSpreading Method

RFmxCdma2kMXConfigureUplinkSpreading Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUplinkSpreading(
	string selectorString,
	long uplinkSpreadingLongCodeMask
)
```

```text
Public Function ConfigureUplinkSpreading ( 
	selectorString As String,
	uplinkSpreadingLongCodeMask As Long
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **uplinkSpreadingLongCodeMask Int64**
  - Specifies the long code mask for uplink spreading. This number is a 42-bit binary number, represented as a 64-bit integer.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/5ac81d6e-d6e1-42e3-93db-79f29b3944da.htm language=enus -->
## TOPIC 00057: rfmxcdma2kdotnet/html/5ac81d6e-d6e1-42e3-93db-79f29b3944da.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/5ac81d6e-d6e1-42e3-93db-79f29b3944da.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/5ac81d6e-d6e1-42e3-93db-79f29b3944da.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemConfiguration.GetOffsetBandwidthIntegral Method

RFmxCdma2kMXSemConfigurationGetOffsetBandwidthIntegral Method

Gets the bandwidth integral for a specific offset segment.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetBandwidthIntegral(
	string selectorString,
	out int value
)
```

```text
Public Function GetOffsetBandwidthIntegral ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Int32**
  - Upon return, contains the bandwidth integral for a specific offset segment.

###### Return Value

Int32

##### Remarks

SemOffsetBandwidthIntegral

##### See Also

###### Reference

RFmxCdma2kMXSemConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/5cbbd2fc-383c-437a-7d07-62d5494df96e.htm language=enus -->
## TOPIC 00058: rfmxcdma2kdotnet/html/5cbbd2fc-383c-437a-7d07-62d5494df96e.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/5cbbd2fc-383c-437a-7d07-62d5494df96e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/5cbbd2fc-383c-437a-7d07-62d5494df96e.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX Properties

RFmxCdma2kMX Properties

The [RFmxCdma2kMX](85756beb-6394-def4-d0e6-f0cc71ff64e1.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Acp | Gets the RFmxCdma2kMXAcp instance that represents the ACP measurement. |
|  | Cda | Gets the RFmxCdma2kMXCda instance that represents the CDA measurement. |
|  | Chp | Gets the RFmxCdma2kMXChp instance that represents the CHP measurement. |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | ModAcc | Gets the RFmxCdma2kMXModAcc instance that represents the ModAcc measurement. |
|  | Obw | Gets the RFmxCdma2kMXObw instance that represents the OBW measurement. |
|  | Qevm | Gets the RFmxCdma2kMXQevm instance that represents the QEVM measurement. |
|  | Sem | Gets the RFmxCdma2kMXSem instance that represents the SEM measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxCdma2kMX. |
|  | SlotPhase | Gets the RFmxCdma2kMXSlotPhase instance that represents the SlotPhase measurement. |
|  | SlotPower | Gets the RFmxCdma2kMXSlotPower instance that represents the SlotPower measurement. |

Top

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/5e2d9f44-5df0-8a62-f7e7-94fca590b996.htm language=enus -->
## TOPIC 00059: rfmxcdma2kdotnet/html/5e2d9f44-5df0-8a62-f7e7-94fca590b996.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/5e2d9f44-5df0-8a62-f7e7-94fca590b996.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/5e2d9f44-5df0-8a62-f7e7-94fca590b996.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXObwRbwFilterType Enumeration

RFmxCdma2kMXObwRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXObwRbwFilterType
```

```text
Public Enumeration RFmxCdma2kMXObwRbwFilterType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a Flat response is applied. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/60aa21ee-4b73-dd60-594e-2e1bb91c3a42.htm language=enus -->
## TOPIC 00060: rfmxcdma2kdotnet/html/60aa21ee-4b73-dd60-594e-2e1bb91c3a42.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/60aa21ee-4b73-dd60-594e-2e1bb91c3a42.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/60aa21ee-4b73-dd60-594e-2e1bb91c3a42.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration Methods

RFmxCdma2kMXCdaConfiguration Methods

The [RFmxCdma2kMXCdaConfiguration](bfeede2b-1f40-8585-b542-26abcd791b39.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureMeasurementChannel | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
|  | ConfigurePowerUnit | Configures the powerUnit parameter for the code domain power results, except for the totalPower parameter. |
|  | ConfigureSynchronizationModeAndInterval | Configures the synchronizationMode, measurementOffset, and measurementLength parameters for the code domain analysis (CDA) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |
|  | GetBaseSpreadingFactor | Gets the base spreading factor used to calculate the code domain power traces. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetIQGainImbalanceRemovalEnabled | Gets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
|  | GetIQOffsetRemovalEnabled | Gets whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
|  | GetIQQuadratureErrorRemovalEnabled | Gets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
|  | GetMeasurementChannelBranch | Gets the Walsh branch of a channel subject to channel specific analysis. |
|  | GetMeasurementChannelWalshCodeLength | Gets the Walsh code length of a channel subject to channel specific analysis. |
|  | GetMeasurementChannelWalshCodeNumber | Gets the Walsh code number of a channel subject to channel specific analysis. |
|  | GetMeasurementEnabled | Gets whether to enable the code domain analysis (CDA) measurement. |
|  | GetMeasurementLength | Gets the duration of code domain measurement. This value is expressed in slots. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. |
|  | GetPowerUnit | Gets the measurement unit of the measured code domain power results. |
|  | GetReceiveFilterEnabled | Gets whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered. |
|  | GetSpectrumInverted | Gets whether the spectrum of the signal is inverted. |
|  | GetSynchronizationMode | Gets whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |
|  | SetBaseSpreadingFactor | Sets the base spreading factor used to calculate the code domain power traces. |
|  | SetIQGainImbalanceRemovalEnabled | Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
|  | SetIQOffsetRemovalEnabled | Sets whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
|  | SetIQQuadratureErrorRemovalEnabled | Sets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
|  | SetMeasurementChannelBranch | Sets the Walsh branch of a channel subject to channel specific analysis. |
|  | SetMeasurementChannelWalshCodeLength | Sets the Walsh code length of a channel subject to channel specific analysis. |
|  | SetMeasurementChannelWalshCodeNumber | Sets the Walsh code number of a channel subject to channel specific analysis. |
|  | SetMeasurementEnabled | Sets whether to enable the code domain analysis (CDA) measurement. |
|  | SetMeasurementLength | Sets the duration of code domain measurement. This value is expressed in slots. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. |
|  | SetPowerUnit | Sets the measurement unit of the measured code domain power results. |
|  | SetReceiveFilterEnabled | Sets whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered. |
|  | SetSpectrumInverted | Sets whether the spectrum of the signal is inverted. |
|  | SetSynchronizationMode | Sets whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/60e43452-5f5f-6ea8-c7be-3cc53e8a94a2.htm language=enus -->
## TOPIC 00061: rfmxcdma2kdotnet/html/60e43452-5f5f-6ea8-c7be-3cc53e8a94a2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/60e43452-5f5f-6ea8-c7be-3cc53e8a94a2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/60e43452-5f5f-6ea8-c7be-3cc53e8a94a2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.FetchLowerOffsetMargin Method

RFmxCdma2kMXSemResultsFetchLowerOffsetMargin Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLowerOffsetMargin(
	string selectorString,
	double timeout,
	out RFmxCdma2kMXSemLowerOffsetMeasurementStatus measurementStatus,
	out double margin,
	out double marginFrequency,
	out double marginAbsolutePower,
	out double marginRelativePower
)
```

```text
Public Function FetchLowerOffsetMargin ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxCdma2kMXSemLowerOffsetMeasurementStatus,
	<OutAttribute> ByRef margin As Double,
	<OutAttribute> ByRef marginFrequency As Double,
	<OutAttribute> ByRef marginAbsolutePower As Double,
	<OutAttribute> ByRef marginRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus RFmxCdma2kMXSemLowerOffsetMeasurementStatus**
  - Upon return, contains the lower offset measurement status based on measurement limits and the failure criteria specified by the standard.
- **margin Double**
  - Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).
- **marginFrequency Double**
  - Upon return, contains the frequency at which the margin occurred in the lower (negative) offset. This value is expressed in Hz.
- **marginAbsolutePower Double**
  - Upon return, contains the power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.
- **marginRelativePower Double**
  - Upon return, contains the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/62c4159a-f2ab-6439-a432-f354726d8657.htm language=enus -->
## TOPIC 00062: rfmxcdma2kdotnet/html/62c4159a-f2ab-6439-a432-f354726d8657.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/62c4159a-f2ab-6439-a432-f354726d8657.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/62c4159a-f2ab-6439-a432-f354726d8657.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SetSelectedPorts Method

RFmxCdma2kMXSetSelectedPorts Method

Valid values

Default values

Supported devices: PXIe-5820/5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSelectedPorts(
	string selectorString,
	string value
)
```

```text
Public Function SetSelectedPorts ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the instrument port to be used by the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/633b1ceb-8352-9740-9368-175f0bfeab97.htm language=enus -->
## TOPIC 00063: rfmxcdma2kdotnet/html/633b1ceb-8352-9740-9368-175f0bfeab97.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/633b1ceb-8352-9740-9368-175f0bfeab97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/633b1ceb-8352-9740-9368-175f0bfeab97.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpConfiguration.ConfigureRbwFilter Method

RFmxCdma2kMXChpConfigurationConfigureRbwFilter Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRbwFilter(
	string selectorString,
	RFmxCdma2kMXChpRbwAutoBandwidth rbwAuto,
	double rbw,
	RFmxCdma2kMXChpRbwFilterType rbwFilterType
)
```

```text
Public Function ConfigureRbwFilter ( 
	selectorString As String,
	rbwAuto As RFmxCdma2kMXChpRbwAutoBandwidth,
	rbw As Double,
	rbwFilterType As RFmxCdma2kMXChpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rbwAuto RFmxCdma2kMXChpRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW.
- **rbw Double**
  - Specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the rbwAuto parameter to False. This value is expressed in Hz.
- **rbwFilterType RFmxCdma2kMXChpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXChpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/70da260f-def6-4b12-a500-f1ee7e91062c.htm language=enus -->
## TOPIC 00064: rfmxcdma2kdotnet/html/70da260f-def6-4b12-a500-f1ee7e91062c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/70da260f-def6-4b12-a500-f1ee7e91062c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/70da260f-def6-4b12-a500-f1ee7e91062c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXExtension.GetCdma2kSignalConfiguration(RFmxInstrMX) Method

RFmxCdma2kMXExtensionGetCdma2kSignalConfiguration(RFmxInstrMX) Method

Creates a new default CDMA2k signal configuration if it doesn't exist; otherwise, it returns the
 existing default CDMA2k signal configuration.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxCdma2kMX GetCdma2kSignalConfiguration(
	this RFmxInstrMX instrSession
)
```

```text
<ExtensionAttribute>
Public Shared Function GetCdma2kSignalConfiguration ( 
	instrSession As RFmxInstrMX
) As RFmxCdma2kMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an instr session.

###### Return Value

RFmxCdma2kMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxCdma2kMXExtension Class

GetCdma2kSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/70f08291-33a6-54c8-c531-c5fd7f927504.htm language=enus -->
## TOPIC 00065: rfmxcdma2kdotnet/html/70f08291-33a6-54c8-c531-c5fd7f927504.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/70f08291-33a6-54c8-c531-c5fd7f927504.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/70f08291-33a6-54c8-c531-c5fd7f927504.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXExtension.GetCdma2kSignalConfiguration(RFmxInstrMX, String) Method

RFmxCdma2kMXExtensionGetCdma2kSignalConfiguration(RFmxInstrMX, String) Method

Creates a CDMA2k signal configuration for specified signal name. Existing CDMA2k signal configuration is
 returned if specified signal name exists.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxCdma2kMX GetCdma2kSignalConfiguration(
	this RFmxInstrMX instrSession,
	string signalName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetCdma2kSignalConfiguration ( 
	instrSession As RFmxInstrMX,
	signalName As String
) As RFmxCdma2kMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an RFmxInstr session.
- **signalName String**
  - Specifies a signal name.

###### Return Value

RFmxCdma2kMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxCdma2kMXExtension Class

GetCdma2kSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/715aa65c-1651-9d62-3deb-79ed6f5434c2.htm language=enus -->
## TOPIC 00066: rfmxcdma2kdotnet/html/715aa65c-1651-9d62-3deb-79ed6f5434c2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/715aa65c-1651-9d62-3deb-79ed6f5434c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/715aa65c-1651-9d62-3deb-79ed6f5434c2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccReceiveFilterEnabled Enumeration

RFmxCdma2kMXModAccReceiveFilterEnabled Enumeration

Specifies whether to enable the received filter for the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXModAccReceiveFilterEnabled
```

```text
Public Enumeration RFmxCdma2kMXModAccReceiveFilterEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables received filtering for the ModAcc measurement. |
| True | 1 | Enables received filtering for the ModAcc measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/71b49fe9-53c0-d0e0-f4af-80d001f7ce5a.htm language=enus -->
## TOPIC 00067: rfmxcdma2kdotnet/html/71b49fe9-53c0-d0e0-f4af-80d001f7ce5a.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/71b49fe9-53c0-d0e0-f4af-80d001f7ce5a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/71b49fe9-53c0-d0e0-f4af-80d001f7ce5a.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled Enumeration

RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled Enumeration

Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled
```

```text
Public Enumeration RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q gain imbalance is not removed before the CDA measurement. |
| True | 1 | I/Q gain imbalance is removed before the CDA measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/73188005-54c7-92a5-b677-bb6adcacd578.htm language=enus -->
## TOPIC 00068: rfmxcdma2kdotnet/html/73188005-54c7-92a5-b677-bb6adcacd578.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/73188005-54c7-92a5-b677-bb6adcacd578.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/73188005-54c7-92a5-b677-bb6adcacd578.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmResults.FetchIQImpairments Method

RFmxCdma2kMXQevmResultsFetchIQImpairments Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchIQImpairments(
	string selectorString,
	double timeout,
	out double meanIQOriginOffset,
	out double meanIQGainImbalance,
	out double meanIQQuadratureError,
	out double maximumIQOriginOffset,
	out double maximumIQGainImbalance,
	out double maximumIQQuadratureError
)
```

```text
Public Function FetchIQImpairments ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanIQOriginOffset As Double,
	<OutAttribute> ByRef meanIQGainImbalance As Double,
	<OutAttribute> ByRef meanIQQuadratureError As Double,
	<OutAttribute> ByRef maximumIQOriginOffset As Double,
	<OutAttribute> ByRef maximumIQGainImbalance As Double,
	<OutAttribute> ByRef maximumIQQuadratureError As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanIQOriginOffset Double**
  - Upon return, contains the mean averaged origin offset of the received signal. This value is expressed in dB.
- **meanIQGainImbalance Double**
  - Upon return, contains the mean I/Q gain imbalance of the received signal. This value is expressed in dB.
- **meanIQQuadratureError Double**
  - Upon return, contains the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.
- **maximumIQOriginOffset Double**
  - Upon return, contains the maximum origin offset of the received signal. This value is expressed in dB.
- **maximumIQGainImbalance Double**
  - Upon return, contains the maximum I/Q gain imbalance of the received signal. This value is expressed in dB.
- **maximumIQQuadratureError Double**
  - Upon return, contains the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXQevmResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/7683902d-6ee0-4561-98d2-14d7de71a773.htm language=enus -->
## TOPIC 00069: rfmxcdma2kdotnet/html/7683902d-6ee0-4561-98d2-14d7de71a773.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/7683902d-6ee0-4561-98d2-14d7de71a773.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/7683902d-6ee0-4561-98d2-14d7de71a773.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSlotPhaseSpectrumInverted Enumeration

RFmxCdma2kMXSlotPhaseSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXSlotPhaseSpectrumInverted
```

```text
Public Enumeration RFmxCdma2kMXSlotPhaseSpectrumInverted
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measured spectrum is not inverted. |
| True | 1 | The measured spectrum is inverted. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/77402303-9e31-9c6d-5fbe-04433722101f.htm language=enus -->
## TOPIC 00070: rfmxcdma2kdotnet/html/77402303-9e31-9c6d-5fbe-04433722101f.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/77402303-9e31-9c6d-5fbe-04433722101f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/77402303-9e31-9c6d-5fbe-04433722101f.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcp Class

RFmxCdma2kMXAcp Class

Represents the ACP measurement.

##### Inheritance Hierarchy

RFmxCdma2kMXSubObject

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxCdma2kMXAcp : RFmxCdma2kMXSubObject
```

```text
Public NotInheritable Class RFmxCdma2kMXAcp
	Inherits RFmxCdma2kMXSubObject
```

The RFmxCdma2kMXAcp type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxCdma2kMXAcpConfiguration instance that provides methods to configure the ACP measurement |
|  | Results | Gets the RFmxCdma2kMXAcpResults instance that provides methods to fetch and read the ACP measurement results. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/793e3b71-3ec6-5114-0d05-fb6ff14b44a1.htm language=enus -->
## TOPIC 00071: rfmxcdma2kdotnet/html/793e3b71-3ec6-5114-0d05-fb6ff14b44a1.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/793e3b71-3ec6-5114-0d05-fb6ff14b44a1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/793e3b71-3ec6-5114-0d05-fb6ff14b44a1.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXRadioConfiguration Enumeration

RFmxCdma2kMXRadioConfiguration Enumeration

Specifies the radio configuration for the channel.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXRadioConfiguration
```

```text
Public Enumeration RFmxCdma2kMXRadioConfiguration
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| RC1 | 0 | If SetLinkDirection(String, RFmxCdma2kMXLinkDirection) method is set to Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and reverse supplemental code channels (R-SCCHs).If Link Direction method is set to Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |
| RC2 | 1 | If Link Direction method is set to Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and R-SCCHs.If Link Direction method is set to Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |
| RC3 | 2 | If Link Direction method is set to Uplink, Radio configuration 3 includes BPSK, R-FCH, and reverse supplemental channels (R-SCHs).If Link Direction method is set to Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |
| RC4 | 3 | If Link Direction method is set to Uplink, Radio configuration 4 includes BPSK, R-FCH, and R-SCHs.If Link Direction method is set to Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |
| RC5 | 4 | If Link Direction method is set to Uplink, Radio configuration 5 is not supported and gives invalid results.If Link Direction method is set to Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/799d8b7c-fd99-9861-1730-4d1efe2f43a7.htm language=enus -->
## TOPIC 00072: rfmxcdma2kdotnet/html/799d8b7c-fd99-9861-1730-4d1efe2f43a7.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/799d8b7c-fd99-9861-1730-4d1efe2f43a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/799d8b7c-fd99-9861-1730-4d1efe2f43a7.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaResults.GetRmsSymbolEvm Method

RFmxCdma2kMXCdaResultsGetRmsSymbolEvm Method

Gets the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsSymbolEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsSymbolEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

CdaResultsRmsSymbolEvm

##### See Also

###### Reference

RFmxCdma2kMXCdaResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/79dafc9d-59a7-67c0-55a9-d301163078ad.htm language=enus -->
## TOPIC 00073: rfmxcdma2kdotnet/html/79dafc9d-59a7-67c0-55a9-d301163078ad.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/79dafc9d-59a7-67c0-55a9-d301163078ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/79dafc9d-59a7-67c0-55a9-d301163078ad.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.GetReferenceLevel Method

RFmxCdma2kMXGetReferenceLevel Method

pk-pk

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReferenceLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetReferenceLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

ReferenceLevel

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/7c3f4b6d-5f23-229a-d200-22f02d733a4f.htm language=enus -->
## TOPIC 00074: rfmxcdma2kdotnet/html/7c3f4b6d-5f23-229a-d200-22f02d733a4f.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/7c3f4b6d-5f23-229a-d200-22f02d733a4f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/7c3f4b6d-5f23-229a-d200-22f02d733a4f.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmReceiveFilterEnabled Enumeration

RFmxCdma2kMXQevmReceiveFilterEnabled Enumeration

Specifies whether to enable the received filter for the QEVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXQevmReceiveFilterEnabled
```

```text
Public Enumeration RFmxCdma2kMXQevmReceiveFilterEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables received filtering for the QEVM measurement. |
| True | 1 | Enables received filtering for the QEVM measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/7d5b3eb3-5992-aa67-0eaf-cdb02f73e3ce.htm language=enus -->
## TOPIC 00075: rfmxcdma2kdotnet/html/7d5b3eb3-5992-aa67-0eaf-cdb02f73e3ce.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/7d5b3eb3-5992-aa67-0eaf-cdb02f73e3ce.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/7d5b3eb3-5992-aa67-0eaf-cdb02f73e3ce.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled Enumeration

RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled Enumeration

Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled
```

```text
Public Enumeration RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q quadrature error is not removed before the CDA measurement. |
| True | 1 | I/Q quadrature error is removed before the CDA measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/80d4f943-d821-7f38-adde-a32db27732f2.htm language=enus -->
## TOPIC 00076: rfmxcdma2kdotnet/html/80d4f943-d821-7f38-adde-a32db27732f2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/80d4f943-d821-7f38-adde-a32db27732f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/80d4f943-d821-7f38-adde-a32db27732f2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaResults.FetchSymbolMagnitudeErrorTrace Method

RFmxCdma2kMXCdaResultsFetchSymbolMagnitudeErrorTrace Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSymbolMagnitudeErrorTrace(
	string selectorString,
	double timeout,
	ref float[] symbolMagnitudeError
)
```

```text
Public Function FetchSymbolMagnitudeErrorTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef symbolMagnitudeError As Single()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **symbolMagnitudeError Single**
  - Upon return, contains the trace of the symbol magnitude errors of the corrected composite signal. This value is expressed as a percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXCdaResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/83209c89-17f8-5644-217c-de3844b967b0.htm language=enus -->
## TOPIC 00077: rfmxcdma2kdotnet/html/83209c89-17f8-5644-217c-de3844b967b0.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/83209c89-17f8-5644-217c-de3844b967b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/83209c89-17f8-5644-217c-de3844b967b0.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.ConfigureNumberOfOffsets Method

RFmxCdma2kMXAcpConfigurationConfigureNumberOfOffsets Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfOffsets(
	string selectorString,
	int numberOfOffsets
)
```

```text
Public Function ConfigureNumberOfOffsets ( 
	selectorString As String,
	numberOfOffsets As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **numberOfOffsets Int32**
  - Specifies the number of offset channels.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/88197678-5b28-06e3-cf2d-0a3a4ca0f2d3.htm language=enus -->
## TOPIC 00078: rfmxcdma2kdotnet/html/88197678-5b28-06e3-cf2d-0a3a4ca0f2d3.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/88197678-5b28-06e3-cf2d-0a3a4ca0f2d3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/88197678-5b28-06e3-cf2d-0a3a4ca0f2d3.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccResults.FetchPhaseErrorTrace Method

RFmxCdma2kMXModAccResultsFetchPhaseErrorTrace Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPhaseErrorTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> phaseError
)
```

```text
Public Function FetchPhaseErrorTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef phaseError As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **phaseError AnalogWaveformSingle**
  - Upon return, contains the trace of phase errors of the corrected composite signal. This value is expressed in degrees.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXModAccResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8c571fa9-ae13-b137-9127-9e12985fccac.htm language=enus -->
## TOPIC 00079: rfmxcdma2kdotnet/html/8c571fa9-ae13-b137-9127-9e12985fccac.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8c571fa9-ae13-b137-9127-9e12985fccac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8c571fa9-ae13-b137-9127-9e12985fccac.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaResults.GetChipRateError Method

RFmxCdma2kMXCdaResultsGetChipRateError Method

Gets the chip rate error. This value is expressed in parts per million (ppm).

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChipRateError(
	string selectorString,
	out double value
)
```

```text
Public Function GetChipRateError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the chip rate error. This value is expressed in parts per million (ppm).

###### Return Value

Int32

##### Remarks

CdaResultsChipRateError

##### See Also

###### Reference

RFmxCdma2kMXCdaResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8cb5e827-7833-569d-7bbf-15488f9b94cd.htm language=enus -->
## TOPIC 00080: rfmxcdma2kdotnet/html/8cb5e827-7833-569d-7bbf-15488f9b94cd.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8cb5e827-7833-569d-7bbf-15488f9b94cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8cb5e827-7833-569d-7bbf-15488f9b94cd.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccConfiguration.GetMeasurementEnabled Method

RFmxCdma2kMXModAccConfigurationGetMeasurementEnabled Method

Gets whether to enable the modulation accuracy (ModAcc) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetMeasurementEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the modulation accuracy (ModAcc) measurement.

###### Return Value

Int32

##### Remarks

ModAccMeasurementEnabled

##### See Also

###### Reference

RFmxCdma2kMXModAccConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8cd6f706-8173-bbbb-3958-fea095f11cd2.htm language=enus -->
## TOPIC 00081: rfmxcdma2kdotnet/html/8cd6f706-8173-bbbb-3958-fea095f11cd2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8cd6f706-8173-bbbb-3958-fea095f11cd2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8cd6f706-8173-bbbb-3958-fea095f11cd2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.ConfigureChannelConfigurationMode Method

RFmxCdma2kMXConfigureChannelConfigurationMode Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureChannelConfigurationMode(
	string selectorString,
	RFmxCdma2kMXChannelConfigurationMode channelConfigurationMode
)
```

```text
Public Function ConfigureChannelConfigurationMode ( 
	selectorString As String,
	channelConfigurationMode As RFmxCdma2kMXChannelConfigurationMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **channelConfigurationMode RFmxCdma2kMXChannelConfigurationMode**
  - Specifies whether to detect the channels automatically or to use a specified channel configuration.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8ddf82ea-45a5-985c-f140-74480c903505.htm language=enus -->
## TOPIC 00082: rfmxcdma2kdotnet/html/8ddf82ea-45a5-985c-f140-74480c903505.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8ddf82ea-45a5-985c-f140-74480c903505.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8ddf82ea-45a5-985c-f140-74480c903505.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXConstants.PxiStarLine Field

RFmxCdma2kMXConstantsPxiStarLine Field

The signal is exported to the PXI star trigger line.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiStarLine = "PXI_STAR"
```

```text
Public Const PxiStarLine As String = "PXI_STAR"
```

###### Field Value

String

##### See Also

###### Reference

RFmxCdma2kMXConstants Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8e1f38f7-276c-76bd-2fcc-eb72bd7a4b8d.htm language=enus -->
## TOPIC 00083: rfmxcdma2kdotnet/html/8e1f38f7-276c-76bd-2fcc-eb72bd7a4b8d.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8e1f38f7-276c-76bd-2fcc-eb72bd7a4b8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8e1f38f7-276c-76bd-2fcc-eb72bd7a4b8d.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemResults.FetchUpperOffsetMargin Method

RFmxCdma2kMXSemResultsFetchUpperOffsetMargin Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUpperOffsetMargin(
	string selectorString,
	double timeout,
	out RFmxCdma2kMXSemUpperOffsetMeasurementStatus measurementStatus,
	out double margin,
	out double marginFrequency,
	out double marginAbsolutePower,
	out double marginRelativePower
)
```

```text
Public Function FetchUpperOffsetMargin ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxCdma2kMXSemUpperOffsetMeasurementStatus,
	<OutAttribute> ByRef margin As Double,
	<OutAttribute> ByRef marginFrequency As Double,
	<OutAttribute> ByRef marginAbsolutePower As Double,
	<OutAttribute> ByRef marginRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus RFmxCdma2kMXSemUpperOffsetMeasurementStatus**
  - Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard.
- **margin Double**
  - Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).
- **marginFrequency Double**
  - Upon return, contains the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.
- **marginAbsolutePower Double**
  - Upon return, contains the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.
- **marginRelativePower Double**
  - Upon return, contains the power at which the margin occurred in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXSemResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8e556808-37e4-1686-4c6b-1f7bd06115fd.htm language=enus -->
## TOPIC 00084: rfmxcdma2kdotnet/html/8e556808-37e4-1686-4c6b-1f7bd06115fd.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8e556808-37e4-1686-4c6b-1f7bd06115fd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8e556808-37e4-1686-4c6b-1f7bd06115fd.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.SignalConfigurationType Property

RFmxCdma2kMXSignalConfigurationType Property

Type

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public Type SignalConfigurationType { get; }
```

```text
Public ReadOnly Property SignalConfigurationType As Type
	Get
```

###### Property Value

Type

###### Implements

ISignalConfiguration.SignalConfigurationType

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8ea1b724-d011-b600-d216-7127d66b341c.htm language=enus -->
## TOPIC 00085: rfmxcdma2kdotnet/html/8ea1b724-d011-b600-d216-7127d66b341c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8ea1b724-d011-b600-d216-7127d66b341c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8ea1b724-d011-b600-d216-7127d66b341c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.GetDownlinkSpreadingPNOffset Method

RFmxCdma2kMXGetDownlinkSpreadingPNOffset Method

Specified the PN offset in increments of 64 chips for forward link.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDownlinkSpreadingPNOffset(
	string selectorString,
	out int value
)
```

```text
Public Function GetDownlinkSpreadingPNOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specified the PN offset in increments of 64 chips for forward link.

###### Return Value

Int32

##### Remarks

DownlinkSpreadingPNOffset

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8ed12200-a8c7-8f96-ddf1-844862541f7c.htm language=enus -->
## TOPIC 00086: rfmxcdma2kdotnet/html/8ed12200-a8c7-8f96-ddf1-844862541f7c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8ed12200-a8c7-8f96-ddf1-844862541f7c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8ed12200-a8c7-8f96-ddf1-844862541f7c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccResults.GetIQGainImbalance Method

RFmxCdma2kMXModAccResultsGetIQGainImbalance Method

Gets the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQGainImbalance(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQGainImbalance ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsIQGainImbalance

##### See Also

###### Reference

RFmxCdma2kMXModAccResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8edcca7d-c722-8c55-1cb3-73ff363ad354.htm language=enus -->
## TOPIC 00087: rfmxcdma2kdotnet/html/8edcca7d-c722-8c55-1cb3-73ff363ad354.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8edcca7d-c722-8c55-1cb3-73ff363ad354.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8edcca7d-c722-8c55-1cb3-73ff363ad354.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcp Properties

RFmxCdma2kMXAcp Properties

The [RFmxCdma2kMXAcp](77402303-9e31-9c6d-5fbe-04433722101f.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxCdma2kMXAcpConfiguration instance that provides methods to configure the ACP measurement |
|  | Results | Gets the RFmxCdma2kMXAcpResults instance that provides methods to fetch and read the ACP measurement results. |

Top

##### See Also

###### Reference

RFmxCdma2kMXAcp Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8f4e6d25-c76c-5b62-0962-ee82923c3a28.htm language=enus -->
## TOPIC 00088: rfmxcdma2kdotnet/html/8f4e6d25-c76c-5b62-0962-ee82923c3a28.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8f4e6d25-c76c-5b62-0962-ee82923c3a28.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8f4e6d25-c76c-5b62-0962-ee82923c3a28.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.GetSweepTimeInterval Method

RFmxCdma2kMXAcpConfigurationGetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxCdma2kMXAcpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetSweepTimeInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXAcpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

AcpSweepTimeInterval

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8f6a13c2-c166-c4c1-5a3d-757617d775e5.htm language=enus -->
## TOPIC 00089: rfmxcdma2kdotnet/html/8f6a13c2-c166-c4c1-5a3d-757617d775e5.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8f6a13c2-c166-c4c1-5a3d-757617d775e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8f6a13c2-c166-c4c1-5a3d-757617d775e5.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.ConfigureRbwFilter Method

RFmxCdma2kMXAcpConfigurationConfigureRbwFilter Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureRbwFilter(
	string selectorString,
	RFmxCdma2kMXAcpRbwAutoBandwidth rbwAuto,
	double rbw,
	RFmxCdma2kMXAcpRbwFilterType rbwFilterType
)
```

```text
Public Function ConfigureRbwFilter ( 
	selectorString As String,
	rbwAuto As RFmxCdma2kMXAcpRbwAutoBandwidth,
	rbw As Double,
	rbwFilterType As RFmxCdma2kMXAcpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **rbwAuto RFmxCdma2kMXAcpRbwAutoBandwidth**
  - Specifies whether the measurement computes the RBW.
- **rbw Double**
  - Specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the rbwAuto parameter to False. This value is expressed in Hz.
- **rbwFilterType RFmxCdma2kMXAcpRbwFilterType**
  - Specifies the shape of the digital RBW filter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/8faa5e31-03e9-e702-7b91-caf640e95ba4.htm language=enus -->
## TOPIC 00090: rfmxcdma2kdotnet/html/8faa5e31-03e9-e702-7b91-caf640e95ba4.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/8faa5e31-03e9-e702-7b91-caf640e95ba4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/8faa5e31-03e9-e702-7b91-caf640e95ba4.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSemConfiguration Methods

RFmxCdma2kMXSemConfiguration Methods

The [RFmxCdma2kMXSemConfiguration](480bf9fe-470b-94f4-86dc-0621dfbe9561.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the SEM measurement. |
|  | ConfigureSweepTime | Configures the sweep time. |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the SEM measurement. |
|  | GetAveragingType | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
|  | GetCarrierIntegrationBandwidth | Gets the SEM carrier integration bandwidth. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMeasurementEnabled | Gets whether to enable the SEM measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the SEM measurement. |
|  | GetNumberOfOffsets | Gets the number of SEM offset segments. |
|  | GetOffsetBandwidthIntegral | Gets the bandwidth integral for a specific offset segment. |
|  | GetOffsetRbwFilterBandwidth | Gets the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. |
|  | GetOffsetRbwFilterType | Gets the type of RBW filter used to sweep the offset segment. |
|  | GetOffsetStartFrequency | Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | GetOffsetStopFrequency | Gets the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
|  | GetSweepTimeAuto | Gets whether the measurement computes the sweep time. |
|  | GetSweepTimeInterval | Gets the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXSemAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the SEM measurement. |
|  | SetAveragingType | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the SEM measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the SEM measurement. |
|  | SetSweepTimeAuto | Sets whether the measurement computes the sweep time. |
|  | SetSweepTimeInterval | Sets the sweep time when you set the SetSweepTimeAuto(String, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxCdma2kMXSemConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/903ab796-05f9-72fa-b017-c7d5d99f5332.htm language=enus -->
## TOPIC 00091: rfmxcdma2kdotnet/html/903ab796-05f9-72fa-b017-c7d5d99f5332.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/903ab796-05f9-72fa-b017-c7d5d99f5332.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/903ab796-05f9-72fa-b017-c7d5d99f5332.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXObwResults.FetchMeasurement Method

RFmxCdma2kMXObwResultsFetchMeasurement Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurement(
	string selectorString,
	double timeout,
	out double occupiedBandwidth,
	out double absolutePower,
	out double startFrequency,
	out double stopFrequency
)
```

```text
Public Function FetchMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef occupiedBandwidth As Double,
	<OutAttribute> ByRef absolutePower As Double,
	<OutAttribute> ByRef startFrequency As Double,
	<OutAttribute> ByRef stopFrequency As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **occupiedBandwidth Double**
  - Upon return, contains the occupied bandwidth. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency
- **absolutePower Double**
  - Upon return, contains the total integrated power of the spectrum acquired by the OBW measurement. This value is expressed in dBm.
- **startFrequency Double**
  - Upon return, contains the start frequency of the OBW. This value is expressed in Hz.
- **stopFrequency Double**
  - Upon return, contains the stop frequency of the OBW. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXObwResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/9192488f-ab1d-09a9-77cd-7e732b8b5dcb.htm language=enus -->
## TOPIC 00092: rfmxcdma2kdotnet/html/9192488f-ab1d-09a9-77cd-7e732b8b5dcb.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/9192488f-ab1d-09a9-77cd-7e732b8b5dcb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/9192488f-ab1d-09a9-77cd-7e732b8b5dcb.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmConfiguration.SetAllTracesEnabled Method

RFmxCdma2kMXQevmConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAllTracesEnabled(
	string selectorString,
	bool value
)
```

```text
Public Function SetAllTracesEnabled ( 
	selectorString As String,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

###### Return Value

Int32

##### Remarks

QevmAllTracesEnabled

##### See Also

###### Reference

RFmxCdma2kMXQevmConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/921c7651-75c9-96cd-833a-ce9bbc16d252.htm language=enus -->
## TOPIC 00093: rfmxcdma2kdotnet/html/921c7651-75c9-96cd-833a-ce9bbc16d252.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/921c7651-75c9-96cd-833a-ce9bbc16d252.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/921c7651-75c9-96cd-833a-ce9bbc16d252.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmConfiguration.GetAllTracesEnabled Method

RFmxCdma2kMXQevmConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllTracesEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetAllTracesEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

###### Return Value

Int32

##### Remarks

QevmAllTracesEnabled

##### See Also

###### Reference

RFmxCdma2kMXQevmConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/957db533-eb9e-b609-6357-ced3d6a47887.htm language=enus -->
## TOPIC 00094: rfmxcdma2kdotnet/html/957db533-eb9e-b609-6357-ced3d6a47887.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/957db533-eb9e-b609-6357-ced3d6a47887.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/957db533-eb9e-b609-6357-ced3d6a47887.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSlotPhaseResults.FetchMaximumPhaseDiscontinuity Method

RFmxCdma2kMXSlotPhaseResultsFetchMaximumPhaseDiscontinuity Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMaximumPhaseDiscontinuity(
	string selectorString,
	double timeout,
	out double maximumPhaseDiscontinuity
)
```

```text
Public Function FetchMaximumPhaseDiscontinuity ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef maximumPhaseDiscontinuity As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout Double**
  - Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **maximumPhaseDiscontinuity Double**
  - Upon return, contains the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXSlotPhaseResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/99d701b7-180e-4e96-1424-963908956adc.htm language=enus -->
## TOPIC 00095: rfmxcdma2kdotnet/html/99d701b7-180e-4e96-1424-963908956adc.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/99d701b7-180e-4e96-1424-963908956adc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/99d701b7-180e-4e96-1424-963908956adc.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.CalculateFrequencyFromChannelNumber Method

RFmxCdma2kMXCalculateFrequencyFromChannelNumber Method

**Note: This API is now obsolete.**

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This function has been obsoleted")]
public static int CalculateFrequencyFromChannelNumber(
	RFmxCdma2kMXLinkDirection linkDirection,
	int bandclass,
	int channelNumber,
	out double centerFrequency
)
```

```text
<ObsoleteAttribute("This function has been obsoleted")>
Public Shared Function CalculateFrequencyFromChannelNumber ( 
	linkDirection As RFmxCdma2kMXLinkDirection,
	bandclass As Integer,
	channelNumber As Integer,
	<OutAttribute> ByRef centerFrequency As Double
) As Integer
```

###### Parameters

- **linkDirection RFmxCdma2kMXLinkDirection**
  - Specifies the direction for which the frequency is calculated. Only uplink is supported.
- **bandclass Int32**
  - Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0.
- **channelNumber Int32**
  - Specifies the channel number used to build the selector string.
- **centerFrequency Double**
  - Upon return, contains the center frequency calculated according to linkDirection, bandClass, and channelNumber. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/9c714807-9b9b-1055-d222-14cd230b52f2.htm language=enus -->
## TOPIC 00096: rfmxcdma2kdotnet/html/9c714807-9b9b-1055-d222-14cd230b52f2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/9c714807-9b9b-1055-d222-14cd230b52f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/9c714807-9b9b-1055-d222-14cd230b52f2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpResults.GetLowerOffsetAbsolutePower Method

RFmxCdma2kMXAcpResultsGetLowerOffsetAbsolutePower Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the absolute measured lower offset channel power. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

###### Return Value

Int32

##### Remarks

AcpResultsLowerOffsetAbsolutePower

##### See Also

###### Reference

RFmxCdma2kMXAcpResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/9d03a3e2-513d-dfb4-5241-786325f5d216.htm language=enus -->
## TOPIC 00097: rfmxcdma2kdotnet/html/9d03a3e2-513d-dfb4-5241-786325f5d216.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/9d03a3e2-513d-dfb4-5241-786325f5d216.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/9d03a3e2-513d-dfb4-5241-786325f5d216.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXObwConfiguration.SetAveragingCount Method

RFmxCdma2kMXObwConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxCdma2kMXObwAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingCount(
	string selectorString,
	int value
)
```

```text
Public Function SetAveragingCount ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxCdma2kMXObwAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

ObwAveragingCount

##### See Also

###### Reference

RFmxCdma2kMXObwConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a1b5dc89-0566-7612-7f63-8cefed319959.htm language=enus -->
## TOPIC 00098: rfmxcdma2kdotnet/html/a1b5dc89-0566-7612-7f63-8cefed319959.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a1b5dc89-0566-7612-7f63-8cefed319959.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a1b5dc89-0566-7612-7f63-8cefed319959.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXConstants Class

RFmxCdma2kMXConstants Class

Specifies constants for I/O terminals.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxCdma2kMXConstants
```

```text
Public NotInheritable Class RFmxCdma2kMXConstants
```

The RFmxCdma2kMXConstants type exposes the following members.

##### Fields

|  | Name | Description |
| --- | --- | --- |
|  | Pfi0 | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. |
|  | Pfi1 | The signal is exported to the PXI trigger line 0. |
|  | PxieDStarBLine | The trigger is received on the PXIe DStar B trigger line. |
|  | PxiStarLine | The signal is exported to the PXI star trigger line. |
|  | PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
|  | PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
|  | PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
|  | PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
|  | PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
|  | PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
|  | PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
|  | PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
|  | TimerEvent | The trigger is received from the timer event. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a1f344c9-da4d-8717-c89d-700c5bad1d76.htm language=enus -->
## TOPIC 00099: rfmxcdma2kdotnet/html/a1f344c9-da4d-8717-c89d-700c5bad1d76.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a1f344c9-da4d-8717-c89d-700c5bad1d76.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a1f344c9-da4d-8717-c89d-700c5bad1d76.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXChpConfiguration.GetMeasurementEnabled Method

RFmxCdma2kMXChpConfigurationGetMeasurementEnabled Method

Gets whether to enable the CHP measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementEnabled(
	string selectorString,
	out bool value
)
```

```text
Public Function GetMeasurementEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Boolean**
  - Upon return, contains whether to enable the CHP measurement.

###### Return Value

Int32

##### Remarks

ChpMeasurementEnabled

##### See Also

###### Reference

RFmxCdma2kMXChpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a3273701-9e33-8c27-0b19-502774e8182b.htm language=enus -->
## TOPIC 00100: rfmxcdma2kdotnet/html/a3273701-9e33-8c27-0b19-502774e8182b.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a3273701-9e33-8c27-0b19-502774e8182b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a3273701-9e33-8c27-0b19-502774e8182b.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmResults Methods

RFmxCdma2kMXQevmResults Methods

The [RFmxCdma2kMXQevmResults](b89d2cab-a025-2a5c-ac63-0f5803173ccc.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchConstellationTrace | Returns the complex chips of the corrected received signal for the QEVM measurement. |
|  | FetchEvm | Returns the EVM value and related measurement values of the QEVM measurement. |
|  | FetchEvmTrace | Returns the EVM trace of the last averaging iteration. |
|  | FetchIQImpairments | Returns the measured I/Q impairments. |
|  | FetchMagnitudeErrorTrace | Returns the magnitude error trace of the last averaging iteration. |
|  | FetchPhaseErrorTrace | Returns the phase error trace of the last averaging iteration. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetMaximumChipRateError | Gets the maximum chip rate error. This value is expressed in parts per million (ppm). |
|  | GetMaximumFrequencyError | Gets the maximum frequency error of the received signal. This value is expressed in Hz. |
|  | GetMaximumIQGainImbalance | Gets the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. |
|  | GetMaximumIQOriginOffset | Gets the maximum origin offset of the received signal. This value is expressed in dB. |
|  | GetMaximumIQQuadratureError | Gets the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
|  | GetMaximumMagnitudeError | Gets the maximum magnitude error of the received signal. This value is expressed as a percentage. |
|  | GetMaximumPeakEvm | Gets the maximum peak EVM of the received signal. This value is expressed as a percentage. |
|  | GetMaximumPhaseError | Gets the maximum phase error of the received signal. This value is expressed in degrees. |
|  | GetMaximumRmsEvm | Gets the maximum RMS EVM of the received signal. This value is expressed as a percentage. |
|  | GetMeanChipRateError | Gets the mean chip rate error. This value is expressed in parts per million (ppm). |
|  | GetMeanFrequencyError | Gets the mean averaged frequency error of the received signal. This value is expressed in Hz. |
|  | GetMeanIQGainImbalance | Gets the mean I/Q gain imbalance of the received signal. This value is expressed in dB. |
|  | GetMeanIQOriginOffset | Gets the mean averaged origin offset of the received signal. This value is expressed in dB. |
|  | GetMeanIQQuadratureError | Gets the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
|  | GetMeanMagnitudeError | Gets the mean averaged magnitude error of the received signal. This value is expressed as a percentage. |
|  | GetMeanPeakEvm | Gets the mean averaged peak EVM of the received signal. This value is expressed as a percentage. |
|  | GetMeanPhaseError | Gets the mean averaged phase error of the received signal. This value is expressed in degrees. |
|  | GetMeanRmsEvm | Gets the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

RFmxCdma2kMXQevmResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a4fbea10-2fcd-4f5f-25ba-6c1b4bd8b974.htm language=enus -->
## TOPIC 00101: rfmxcdma2kdotnet/html/a4fbea10-2fcd-4f5f-25ba-6c1b4bd8b974.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a4fbea10-2fcd-4f5f-25ba-6c1b4bd8b974.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a4fbea10-2fcd-4f5f-25ba-6c1b4bd8b974.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaResults.GetMeanSymbolPower Method

RFmxCdma2kMXCdaResultsGetMeanSymbolPower Method

SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit)

dB

dBm

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanSymbolPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanSymbolPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Double**
  - Upon return, contains the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the SetPowerUnit(String, RFmxCdma2kMXCdaPowerUnit) method to dB, and in dBm, when you set the CDA Pwr Unit method to dBm.

###### Return Value

Int32

##### Remarks

CdaResultsMeanSymbolPower

##### See Also

###### Reference

RFmxCdma2kMXCdaResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a5eeccbf-77a4-d889-a730-157393f6f34c.htm language=enus -->
## TOPIC 00102: rfmxcdma2kdotnet/html/a5eeccbf-77a4-d889-a730-157393f6f34c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a5eeccbf-77a4-d889-a730-157393f6f34c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a5eeccbf-77a4-d889-a730-157393f6f34c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXModAccResults.GetPeakCdeWalshCodeNumber Method

RFmxCdma2kMXModAccResultsGetPeakCdeWalshCodeNumber Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakCdeWalshCodeNumber(
	string selectorString,
	out int value
)
```

```text
Public Function GetPeakCdeWalshCodeNumber ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value Int32**
  - Upon return, contains the Walsh code number corresponding to the value that the GetPeakCde(String, Double) method returns.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakCdeWalshCodeNumber

##### See Also

###### Reference

RFmxCdma2kMXModAccResults Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a88bbd9c-6b7d-bc51-6a4d-5635629d0e4d.htm language=enus -->
## TOPIC 00103: rfmxcdma2kdotnet/html/a88bbd9c-6b7d-bc51-6a4d-5635629d0e4d.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a88bbd9c-6b7d-bc51-6a4d-5635629d0e4d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a88bbd9c-6b7d-bc51-6a4d-5635629d0e4d.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXSlotPhaseConfiguration.SetSpectrumInverted Method

RFmxCdma2kMXSlotPhaseConfigurationSetSpectrumInverted Method

Sets whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSpectrumInverted(
	string selectorString,
	RFmxCdma2kMXSlotPhaseSpectrumInverted value
)
```

```text
Public Function SetSpectrumInverted ( 
	selectorString As String,
	value As RFmxCdma2kMXSlotPhaseSpectrumInverted
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXSlotPhaseSpectrumInverted**
  - Specifies whether the spectrum of the signal is inverted.

###### Return Value

Int32

##### Remarks

SlotPhaseSpectrumInverted

False

##### See Also

###### Reference

RFmxCdma2kMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a971ba2d-47d2-0bfb-27f1-2a55307d3452.htm language=enus -->
## TOPIC 00104: rfmxcdma2kdotnet/html/a971ba2d-47d2-0bfb-27f1-2a55307d3452.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a971ba2d-47d2-0bfb-27f1-2a55307d3452.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a971ba2d-47d2-0bfb-27f1-2a55307d3452.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMX.Obw Property

RFmxCdma2kMXObw Property

RFmxCdma2kMXObw

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxCdma2kMXObw Obw { get; }
```

```text
Public ReadOnly Property Obw As RFmxCdma2kMXObw
	Get
```

###### Property Value

RFmxCdma2kMXObw

##### See Also

###### Reference

RFmxCdma2kMX Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/a9de469c-9b3e-7ad9-2f5a-22cf0a0f863c.htm language=enus -->
## TOPIC 00105: rfmxcdma2kdotnet/html/a9de469c-9b3e-7ad9-2f5a-22cf0a0f863c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/a9de469c-9b3e-7ad9-2f5a-22cf0a0f863c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/a9de469c-9b3e-7ad9-2f5a-22cf0a0f863c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXQevmConfiguration.SetNumberOfAnalysisThreads Method

RFmxCdma2kMXQevmConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the QEVM measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfAnalysisThreads(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfAnalysisThreads ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the maximum number of threads used for parallelism for the QEVM measurement.

###### Return Value

Int32

##### Remarks

QevmNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxCdma2kMXQevmConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/aaf33c66-ab7b-57da-a3b5-2d887ce4c368.htm language=enus -->
## TOPIC 00106: rfmxcdma2kdotnet/html/aaf33c66-ab7b-57da-a3b5-2d887ce4c368.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/aaf33c66-ab7b-57da-a3b5-2d887ce4c368.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/aaf33c66-ab7b-57da-a3b5-2d887ce4c368.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXAcpConfiguration.GetOffsetIntegrationBandwidth Method

RFmxCdma2kMXAcpConfigurationGetOffsetIntegrationBandwidth Method

Gets the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetIntegrationBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetIntegrationBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpOffsetIntegrationBandwidth

##### See Also

###### Reference

RFmxCdma2kMXAcpConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/ab60f4e9-2286-0c71-c461-b4c772ae417c.htm language=enus -->
## TOPIC 00107: rfmxcdma2kdotnet/html/ab60f4e9-2286-0c71-c461-b4c772ae417c.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/ab60f4e9-2286-0c71-c461-b4c772ae417c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/ab60f4e9-2286-0c71-c461-b4c772ae417c.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration.GetIQOffsetRemovalEnabled Method

RFmxCdma2kMXCdaConfigurationGetIQOffsetRemovalEnabled Method

Gets whether to remove I/Q offset before the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOffsetRemovalEnabled(
	string selectorString,
	out RFmxCdma2kMXCdaIQOffsetRemovalEnabled value
)
```

```text
Public Function GetIQOffsetRemovalEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxCdma2kMXCdaIQOffsetRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxCdma2kMXCdaIQOffsetRemovalEnabled**
  - Upon return, contains whether to remove I/Q offset before the code domain analysis (CDA) measurement.

###### Return Value

Int32

##### Remarks

CdaIQOffsetRemovalEnabled

False

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-cdma2k-dotnet path=rfmxcdma2kdotnet/html/abe3765a-20c7-889e-fc32-34c877210fe2.htm language=enus -->
## TOPIC 00108: rfmxcdma2kdotnet/html/abe3765a-20c7-889e-fc32-34c877210fe2.htm

- bundle_id: `rfmx-cdma2k-dotnet`
- source_path: `rfmxcdma2kdotnet/html/abe3765a-20c7-889e-fc32-34c877210fe2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-dotnet/raw/resource/enus/rfmxcdma2kdotnet/html/abe3765a-20c7-889e-fc32-34c877210fe2.htm
- document_id: `rfmx-cdma2k-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxCdma2kMXCdaConfiguration.ConfigureMeasurementChannel Method

RFmxCdma2kMXCdaConfigurationConfigureMeasurementChannel Method

Namespace:

NationalInstruments.RFmx.Cdma2kMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementChannel(
	string selectorString,
	int walshCodeLength,
	int walshCodeNumber,
	RFmxCdma2kMXCdaMeasurementChannelBranch branch
)
```

```text
Public Function ConfigureMeasurementChannel ( 
	selectorString As String,
	walshCodeLength As Integer,
	walshCodeNumber As Integer,
	branch As RFmxCdma2kMXCdaMeasurementChannelBranch
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **walshCodeLength Int32**
  - Specifies the Walsh code length of a channel subject to channel specific analysis.
- **walshCodeNumber Int32**
  - Specifies the Walsh code number of a channel subject to channel specific analysis.
- **branch RFmxCdma2kMXCdaMeasurementChannelBranch**
  - Specifies the branch of a channel subject to channel specific analysis.

###### Return Value

Int32

##### See Also

###### Reference

RFmxCdma2kMXCdaConfiguration Class

NationalInstruments.RFmx.Cdma2kMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
