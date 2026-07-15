# NI DOCUMENT BUNDLE: rfmx-for-bluetooth-test-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-for-bluetooth-test-dotnet start=1 end=106 -->
<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/14f9b133-b20d-7b1e-71e6-d5d0efa42ef9.htm language=enus -->
## TOPIC 00001: rfmxbtdotnet/html/14f9b133-b20d-7b1e-71e6-d5d0efa42ef9.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/14f9b133-b20d-7b1e-71e6-d5d0efa42ef9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/14f9b133-b20d-7b1e-71e6-d5d0efa42ef9.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXPowerRampBurstSynchronizationType Enumeration

RFmxBTMXPowerRampBurstSynchronizationType Enumeration

Specifies the type of synchronization used for detecting the start of packet in the PowerRamp measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXPowerRampBurstSynchronizationType
```

```text
Public Enumeration RFmxBTMXPowerRampBurstSynchronizationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
|  | Preamble | 1 | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
|  | SyncWord | 2 | Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm language=enus -->
## TOPIC 00002: rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/1a6a63ad-9cda-e5c7-6791-0a3676df3d87.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeConfiguration.SetAveragingCount Method

RFmxBTMXFrequencyRangeConfigurationSetAveragingCount Method

SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

FrequencyRangeAveragingCount

##### See Also

###### Reference

RFmxBTMXFrequencyRangeConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/203782a2-1b31-6662-5948-9cb0e8d43e2a.htm language=enus -->
## TOPIC 00003: rfmxbtdotnet/html/203782a2-1b31-6662-5948-9cb0e8d43e2a.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/203782a2-1b31-6662-5948-9cb0e8d43e2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/203782a2-1b31-6662-5948-9cb0e8d43e2a.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetEdrDpskAveragePowerMean Method

RFmxBTMXTxpResultsGetEdrDpskAveragePowerMean Method

Gets the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetEdrDpskAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetEdrDpskAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsEdrDpskAveragePowerMean

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/25f28f81-b627-aa02-d895-0d71811a77e8.htm language=enus -->
## TOPIC 00004: rfmxbtdotnet/html/25f28f81-b627-aa02-d895-0d71811a77e8.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/25f28f81-b627-aa02-d895-0d71811a77e8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/25f28f81-b627-aa02-d895-0d71811a77e8.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXChannelSoundingPacketFormat Enumeration

RFmxBTMXChannelSoundingPacketFormat Enumeration

SetPacketType(String, RFmxBTMXPacketType)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXChannelSoundingPacketFormat
```

```text
Public Enumeration RFmxBTMXChannelSoundingPacketFormat
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Sync | 0 | Specifies that the LE-CS packet contains only SYNC portion. |
|  | CSTone | 1 | Specifies that the LE-CS packet contains only CS Tone. |
|  | CSToneAfterSync | 2 | Specifies that the CS Tone portion is at the end of the LE-CS packet. |
|  | CSToneBeforeSync | 3 | Specifies that the CS Tone portion is at the beginning of the LE-CS packet |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/276911d4-ff18-c660-c335-d52a36481484.htm language=enus -->
## TOPIC 00005: rfmxbtdotnet/html/276911d4-ff18-c660-c335-d52a36481484.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/276911d4-ff18-c660-c335-d52a36481484.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/276911d4-ff18-c660-c335-d52a36481484.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.CloneSignalConfiguration Method

RFmxBTMXCloneSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int CloneSignalConfiguration(
	string newSignalName,
	out RFmxBTMX signalConfiguration
)
```

```text
Public Function CloneSignalConfiguration ( 
	newSignalName As String,
	<OutAttribute> ByRef signalConfiguration As RFmxBTMX
) As Integer
```

###### Parameters

- **newSignalName**
  - Type: SystemString Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName"
- **signalConfiguration**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXUpon return, contains a new BT signal instance.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm language=enus -->
## TOPIC 00006: rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/28a8c3cd-ba1b-edb6-a375-91237c67a7b7.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetCenterFrequency Method

RFmxBTMXSetCenterFrequency Method

Sets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCenterFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetCenterFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

###### Return Value

Int32

##### Remarks

CenterFrequency

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/2bce6be0-12fa-3d02-e374-f66f40272e0e.htm language=enus -->
## TOPIC 00007: rfmxbtdotnet/html/2bce6be0-12fa-3d02-e374-f66f40272e0e.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/2bce6be0-12fa-3d02-e374-f66f40272e0e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/2bce6be0-12fa-3d02-e374-f66f40272e0e.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ConfigureRF Method

RFmxBTMXConfigureRF Method

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **centerFrequency**
  - Type: SystemDouble Specifies the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. The value is expressed in Hz. The default of this method is hardware dependent.
- **referenceLevel**
  - Type: SystemDouble Specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent.
- **externalAttenuation**
  - Type: SystemDouble Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/37400dfb-9034-c07c-12f9-485e521f891d.htm language=enus -->
## TOPIC 00008: rfmxbtdotnet/html/37400dfb-9034-c07c-12f9-485e521f891d.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/37400dfb-9034-c07c-12f9-485e521f891d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/37400dfb-9034-c07c-12f9-485e521f891d.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.GetNumberOfAnalysisThreads Method

RFmxBTMXTwentydBBandwidthConfigurationGetNumberOfAnalysisThreads Method

Gets the maximum number of threads used for parallelism for the 20dB bandwidth measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfAnalysisThreads(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfAnalysisThreads ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the maximum number of threads used for parallelism for the 20dB bandwidth measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/37aef6d8-5b06-c46a-156f-d83f7c3617c1.htm language=enus -->
## TOPIC 00009: rfmxbtdotnet/html/37aef6d8-5b06-c46a-156f-d83f7c3617c1.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/37aef6d8-5b06-c46a-156f-d83f7c3617c1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/37aef6d8-5b06-c46a-156f-d83f7c3617c1.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetAttributeBool Method

RFmxBTMXSetAttributeBool Method

Sets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeBool(
	string selectorString,
	int attributeIdentifier,
	bool value
)
```

```text
Public Function SetAttributeBool ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemBooleanSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/37f46814-8546-219a-4fa6-afb018bdf4dd.htm language=enus -->
## TOPIC 00010: rfmxbtdotnet/html/37f46814-8546-219a-4fa6-afb018bdf4dd.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/37f46814-8546-219a-4fa6-afb018bdf4dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/37f46814-8546-219a-4fa6-afb018bdf4dd.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ConfigurePayloadBitPattern Method

RFmxBTMXConfigurePayloadBitPattern Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigurePayloadBitPattern(
	string selectorString,
	RFmxBTMXPayloadBitPattern payloadBitPattern
)
```

```text
Public Function ConfigurePayloadBitPattern ( 
	selectorString As String,
	payloadBitPattern As RFmxBTMXPayloadBitPattern
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **payloadBitPattern**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXPayloadBitPattern Specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/38135eb3-abb3-3826-5e77-3959b34500a0.htm language=enus -->
## TOPIC 00011: rfmxbtdotnet/html/38135eb3-abb3-3826-5e77-3959b34500a0.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/38135eb3-abb3-3826-5e77-3959b34500a0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/38135eb3-abb3-3826-5e77-3959b34500a0.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchCSDetrendedPhaseTrace Method

RFmxBTMXModAccResultsFetchCSDetrendedPhaseTrace Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCSDetrendedPhaseTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> csDetrendedPhase
)
```

```text
Public Function FetchCSDetrendedPhaseTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef csDetrendedPhase As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **csDetrendedPhase**
  - Type: NationalInstrumentsAnalogWaveformSingleUpon return, contains the zero-mean detrended phase versus time trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/399d07c9-8634-9c68-25a2-23288e4ec8e7.htm language=enus -->
## TOPIC 00012: rfmxbtdotnet/html/399d07c9-8634-9c68-25a2-23288e4ec8e7.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/399d07c9-8634-9c68-25a2-23288e4ec8e7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/399d07c9-8634-9c68-25a2-23288e4ec8e7.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetAllNamedResultNames Method

RFmxBTMXGetAllNamedResultNames Method

Gets the named result names of the signal that you specify in the selectorString parameter.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAllNamedResultNames(
	string selectorString,
	out string[] resultNames,
	out bool defaultResultExists
)
```

```text
Public Function GetAllNamedResultNames ( 
	selectorString As String,
	<OutAttribute> ByRef resultNames As String(),
	<OutAttribute> ByRef defaultResultExists As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **resultNames**
  - Type: SystemString Returns an array of result names.
- **defaultResultExists**
  - Type: SystemBooleanUpon return, indicates whether the default result exists.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/39af901e-19af-c0d2-f095-348ecda509d8.htm language=enus -->
## TOPIC 00013: rfmxbtdotnet/html/39af901e-19af-c0d2-f095-348ecda509d8.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/39af901e-19af-c0d2-f095-348ecda509d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/39af901e-19af-c0d2-f095-348ecda509d8.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXIQPowerEdgeTriggerSlope Enumeration

RFmxBTMXIQPowerEdgeTriggerSlope Enumeration

SetTriggerType(String, RFmxBTMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXIQPowerEdgeTriggerSlope
```

```text
Public Enumeration RFmxBTMXIQPowerEdgeTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 0 | The trigger asserts when the signal power is rising. |
|  | Falling | 1 | The trigger asserts when the signal power is falling. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/41652f2b-606b-2fc5-31b2-4142c14b4d59.htm language=enus -->
## TOPIC 00014: rfmxbtdotnet/html/41652f2b-606b-2fc5-31b2-4142c14b4d59.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/41652f2b-606b-2fc5-31b2-4142c14b4d59.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/41652f2b-606b-2fc5-31b2-4142c14b4d59.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetPeakPowerMaximum Method

RFmxBTMXTxpResultsGetPeakPowerMaximum Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakPowerMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakPowerMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsPeakPowerMaximum

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/41be8e4c-405c-a31e-240a-65e7f86a9d18.htm language=enus -->
## TOPIC 00015: rfmxbtdotnet/html/41be8e4c-405c-a31e-240a-65e7f86a9d18.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/41be8e4c-405c-a31e-240a-65e7f86a9d18.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/41be8e4c-405c-a31e-240a-65e7f86a9d18.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ConfigureReferenceLevel Method

RFmxBTMXConfigureReferenceLevel Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureReferenceLevel(
	string selectorString,
	double referenceLevel
)
```

```text
Public Function ConfigureReferenceLevel ( 
	selectorString As String,
	referenceLevel As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **referenceLevel**
  - Type: SystemDouble Specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/4476290d-3243-d804-0440-da9903bcedcc.htm language=enus -->
## TOPIC 00016: rfmxbtdotnet/html/4476290d-3243-d804-0440-da9903bcedcc.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/4476290d-3243-d804-0440-da9903bcedcc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/4476290d-3243-d804-0440-da9903bcedcc.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetDigitalEdgeTriggerEdge Method

RFmxBTMXSetDigitalEdgeTriggerEdge Method

SetTriggerType(String, RFmxBTMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerEdge(
	string selectorString,
	RFmxBTMXDigitalEdgeTriggerEdge value
)
```

```text
Public Function SetDigitalEdgeTriggerEdge ( 
	selectorString As String,
	value As RFmxBTMXDigitalEdgeTriggerEdge
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXDigitalEdgeTriggerEdge Specifies the active edge for the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerEdge

Rising

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/459fffb9-26fa-db72-8eff-0224a00cbbe0.htm language=enus -->
## TOPIC 00017: rfmxbtdotnet/html/459fffb9-26fa-db72-8eff-0224a00cbbe0.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/459fffb9-26fa-db72-8eff-0224a00cbbe0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/459fffb9-26fa-db72-8eff-0224a00cbbe0.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAcc Methods

RFmxBTMXModAcc Methods

The [RFmxBTMXModAcc](fc9291b0-3730-2815-e62b-7e4b38c1bf55.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXModAcc Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/4b668001-afe8-24f0-013b-68a66fcf5a18.htm language=enus -->
## TOPIC 00018: rfmxbtdotnet/html/4b668001-afe8-24f0-013b-68a66fcf5a18.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/4b668001-afe8-24f0-013b-68a66fcf5a18.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/4b668001-afe8-24f0-013b-68a66fcf5a18.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetAttributeBool Method

RFmxBTMXGetAttributeBool Method

Gets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeBool(
	string selectorString,
	int attributeIdentifier,
	out bool value
)
```

```text
Public Function GetAttributeBool ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemBooleanUpon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/4f10f94e-0211-d178-64e8-7c9bf28cde3b.htm language=enus -->
## TOPIC 00019: rfmxbtdotnet/html/4f10f94e-0211-d178-64e8-7c9bf28cde3b.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/4f10f94e-0211-d178-64e8-7c9bf28cde3b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/4f10f94e-0211-d178-64e8-7c9bf28cde3b.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetChannelSoundingPhaseMeasurementPeriod Method

RFmxBTMXSetChannelSoundingPhaseMeasurementPeriod Method

SetPacketType(String, RFmxBTMXPacketType)

SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChannelSoundingPhaseMeasurementPeriod(
	string selectorString,
	double value
)
```

```text
Public Function SetChannelSoundingPhaseMeasurementPeriod ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC.

###### Return Value

Int32

##### Remarks

ChannelSoundingPhaseMeasurementPeriod

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/505493d9-9480-1c18-84e0-6eb6f7d9c616.htm language=enus -->
## TOPIC 00020: rfmxbtdotnet/html/505493d9-9480-1c18-84e0-6eb6f7d9c616.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/505493d9-9480-1c18-84e0-6eb6f7d9c616.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/505493d9-9480-1c18-84e0-6eb6f7d9c616.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.SetOffsetChannelMode Method

RFmxBTMXAcpConfigurationSetOffsetChannelMode Method

Sets which offset channels are used for the measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetChannelMode(
	string selectorString,
	RFmxBTMXAcpOffsetChannelMode value
)
```

```text
Public Function SetOffsetChannelMode ( 
	selectorString As String,
	value As RFmxBTMXAcpOffsetChannelMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXAcpOffsetChannelModeSpecifies which offset channels are used for the measurement.

###### Return Value

Int32

##### Remarks

AcpOffsetChannelMode

Symmetric

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/516cb387-0b4d-7bd7-e106-026055d1e641.htm language=enus -->
## TOPIC 00021: rfmxbtdotnet/html/516cb387-0b4d-7bd7-e106-026055d1e641.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/516cb387-0b4d-7bd7-e106-026055d1e641.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/516cb387-0b4d-7bd7-e106-026055d1e641.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum Method

RFmxBTMXTxpResultsGetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

TxpResultsLECteReferencePeriodPeakAbsolutePowerDeviationMaximum

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/52570995-9637-4c22-3b1f-cc25dbc751c7.htm language=enus -->
## TOPIC 00022: rfmxbtdotnet/html/52570995-9637-4c22-3b1f-cc25dbc751c7.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/52570995-9637-4c22-3b1f-cc25dbc751c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/52570995-9637-4c22-3b1f-cc25dbc751c7.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetIQOriginOffsetMean Method

RFmxBTMXModAccResultsGetIQOriginOffsetMean Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOriginOffsetMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQOriginOffsetMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the I/Q origin offset estimated over the EDR portion of the EDR packets. This value is expressed in dB. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the I/Q origin offset values computed for each averaging count.

###### Return Value

Int32

##### Remarks

ModAccResultsIQOriginOffsetMean

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/52585930-92ec-7780-ad55-8443519d033a.htm language=enus -->
## TOPIC 00023: rfmxbtdotnet/html/52585930-92ec-7780-ad55-8443519d033a.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/52585930-92ec-7780-ad55-8443519d033a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/52585930-92ec-7780-ad55-8443519d033a.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccConfiguration.GetIQOriginOffsetCorrectionEnabled Method

RFmxBTMXModAccConfigurationGetIQOriginOffsetCorrectionEnabled Method

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOriginOffsetCorrectionEnabled(
	string selectorString,
	out RFmxBTMXModAccIQOriginOffsetCorrectionEnabled value
)
```

```text
Public Function GetIQOriginOffsetCorrectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXModAccIQOriginOffsetCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXModAccIQOriginOffsetCorrectionEnabled Upon return, contains whether to enable the I/Q origin offset correction for EDR packets. If you set this method to True, the DEVM results are computed after correcting for the I/Q origin offset.

###### Return Value

Int32

##### Remarks

ModAccIQOriginOffsetCorrectionEnabled

False

##### See Also

###### Reference

RFmxBTMXModAccConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/528dad18-44cf-cff7-9b03-deefeed04f57.htm language=enus -->
## TOPIC 00024: rfmxbtdotnet/html/528dad18-44cf-cff7-9b03-deefeed04f57.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/528dad18-44cf-cff7-9b03-deefeed04f57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/528dad18-44cf-cff7-9b03-deefeed04f57.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults Methods

RFmxBTMXTxpResults Methods

The [RFmxBTMXTxpResults](b0e22d32-88c5-b4e0-2e34-4e55baf6b2dc.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchEdrPowers | Fetches TXP measurement results for enhanced data rate (EDR) packets. |
|  | FetchLECteReferencePeriodPowers | Fetches the transmit power (TXP) measurement over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
|  | FetchLECteTransmitSlotPowers | Fetches the transmit power (TXP) measurement over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
|  | FetchLECteTransmitSlotPowersArray | Fetches an array of transmit power (TXP) measurement over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
|  | FetchPowers | Fetches TXP measurement results. These results are valid for all packets. |
|  | FetchPowerTrace | Fetches the power versus time trace. |
|  | GetAveragePowerMaximum | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetAveragePowerMean | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count. |
|  | GetAveragePowerMinimum | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetEdrDpskAveragePowerMean | Gets the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetEdrDpskGfskAveragePowerRatioMean | Gets the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |
|  | GetEdrGfskAveragePowerMean | Gets the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLECSPhaseMeasurementPeriodAveragePowerMean |  |
|  | GetLECteReferencePeriodAveragePowerMean | Gets the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum | Gets the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | GetLECteTransmitSlotAveragePowerMean | Gets the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum | Gets the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | GetPeakPowerMaximum | Gets the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm. |
|  | GetPeakToAveragePowerRatioMaximum | Gets the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/52b71bda-4c39-37e6-db31-de0256a80a94.htm language=enus -->
## TOPIC 00025: rfmxbtdotnet/html/52b71bda-4c39-37e6-db31-de0256a80a94.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/52b71bda-4c39-37e6-db31-de0256a80a94.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/52b71bda-4c39-37e6-db31-de0256a80a94.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeResults.GetLowFrequency Method

RFmxBTMXFrequencyRangeResultsGetLowFrequency Method

Gets the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

FrequencyRangeResultsLowFrequency

##### See Also

###### Reference

RFmxBTMXFrequencyRangeResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm language=enus -->
## TOPIC 00026: rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/53afef6a-adcb-5f09-3b64-d150d93024a6.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetIQPowerEdgeTriggerSource Method

RFmxBTMXGetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxBTMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetIQPowerEdgeTriggerSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemString Upon return, contains the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/570f825a-a231-7974-1a4d-57e4c1897207.htm language=enus -->
## TOPIC 00027: rfmxbtdotnet/html/570f825a-a231-7974-1a4d-57e4c1897207.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/570f825a-a231-7974-1a4d-57e4c1897207.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/570f825a-a231-7974-1a4d-57e4c1897207.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeResults.FetchMeasurement Method

RFmxBTMXFrequencyRangeResultsFetchMeasurement Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurement(
	string selectorString,
	double timeout,
	out double highFrequency,
	out double lowFrequency
)
```

```text
Public Function FetchMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef highFrequency As Double,
	<OutAttribute> ByRef lowFrequency As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **highFrequency**
  - Type: SystemDouble Upon return, contains the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz.
- **lowFrequency**
  - Type: SystemDouble Upon return, contains the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXFrequencyRangeResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/578e08cb-388a-4899-13cc-99918a2d5e9d.htm language=enus -->
## TOPIC 00028: rfmxbtdotnet/html/578e08cb-388a-4899-13cc-99918a2d5e9d.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/578e08cb-388a-4899-13cc-99918a2d5e9d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/578e08cb-388a-4899-13cc-99918a2d5e9d.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetTriggerDelay Method

RFmxBTMXGetTriggerDelay Method

Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerDelay(
	string selectorString,
	out double value
)
```

```text
Public Function GetTriggerDelay ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples.

###### Return Value

Int32

##### Remarks

TriggerDelay

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5792f524-7a79-261f-6e4b-39a4e84b5c93.htm language=enus -->
## TOPIC 00029: rfmxbtdotnet/html/5792f524-7a79-261f-6e4b-39a4e84b5c93.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5792f524-7a79-261f-6e4b-39a4e84b5c93.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5792f524-7a79-261f-6e4b-39a4e84b5c93.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ConfigureChannelNumber Method

RFmxBTMXConfigureChannelNumber Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureChannelNumber(
	string selectorString,
	int channelNumber
)
```

```text
Public Function ConfigureChannelNumber ( 
	selectorString As String,
	channelNumber As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **channelNumber**
  - Type: SystemInt32 Specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification. This parameter is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm language=enus -->
## TOPIC 00030: rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/586db288-f5f9-35d2-de4c-efa119bdcc54.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthResults.GetBandwidth Method

RFmxBTMXTwentydBBandwidthResultsGetBandwidth Method

Gets the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthResultsBandwidth

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/58dffd5f-c5b8-9cbe-8bed-44f89d1512d3.htm language=enus -->
## TOPIC 00031: rfmxbtdotnet/html/58dffd5f-c5b8-9cbe-8bed-44f89d1512d3.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/58dffd5f-c5b8-9cbe-8bed-44f89d1512d3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/58dffd5f-c5b8-9cbe-8bed-44f89d1512d3.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.GetMeasurementEnabled Method

RFmxBTMXAcpConfigurationGetMeasurementEnabled Method

Gets whether to enable the ACP measurement.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanUpon return, contains whether to enable the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpMeasurementEnabled

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm language=enus -->
## TOPIC 00032: rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5a869f24-082f-d34d-28ca-28d1a2b59f07.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXExtension.GetBTSignalConfiguration Method

RFmxBTMXExtensionGetBTSignalConfiguration Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | GetBTSignalConfiguration(RFmxInstrMX) | Creates a new default BT signal configuration if it doesn't exist; otherwise, it returns the existing default BT signal configuration. |
|  | GetBTSignalConfiguration(RFmxInstrMX, String) | Creates a BT signal configuration for specified signal name. Existing BT signal configuration is returned if specified signal name exists. |

Top

##### See Also

###### Reference

RFmxBTMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm language=enus -->
## TOPIC 00033: rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5ab22f7a-e049-b6f2-b6a8-dd86d550bee9.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.AbortMeasurements Method

RFmxBTMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int AbortMeasurements(
	string selectorString
)
```

```text
Public Function AbortMeasurements ( 
	selectorString As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm language=enus -->
## TOPIC 00034: rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5acedadf-8901-a15a-14a0-252e4fcd98a9.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.GetAveragingEnabled Method

RFmxBTMXAcpConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxBTMXAcpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXAcpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXAcpAveragingEnabledUpon return, contains whether to enable averaging for the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpAveragingEnabled

False

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm language=enus -->
## TOPIC 00035: rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5ba43ecd-6648-5db7-cb01-663bda83cf1a.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.ConfigureDataRate Method

RFmxBTMXConfigureDataRate Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDataRate(
	string selectorString,
	int dataRate
)
```

```text
Public Function ConfigureDataRate ( 
	selectorString As String,
	dataRate As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **dataRate**
  - Type: SystemInt32Specifies the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This parameter is applicable to the LE/LE-CS packet types.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5c2a8378-8ed8-984c-aa0d-d4156105c9ca.htm language=enus -->
## TOPIC 00036: rfmxbtdotnet/html/5c2a8378-8ed8-984c-aa0d-d4156105c9ca.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5c2a8378-8ed8-984c-aa0d-d4156105c9ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5c2a8378-8ed8-984c-aa0d-d4156105c9ca.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SignalConfigurationName Property

RFmxBTMXSignalConfigurationName Property

Gets the signal configuration name.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public string SignalConfigurationName { get; }
```

```text
Public ReadOnly Property SignalConfigurationName As String
	Get
```

###### Property Value

String

###### Implements

ISignalConfiguration.SignalConfigurationName

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm language=enus -->
## TOPIC 00037: rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5e112855-0442-181a-f08d-e863d8dad434.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetReferenceLevel Method

RFmxBTMXGetReferenceLevel Method

Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

ReferenceLevel

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm language=enus -->
## TOPIC 00038: rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5e1f3690-0109-29aa-0aa3-90e3ac7c4ded.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.ConfigureAveraging Method

RFmxBTMXTwentydBBandwidthConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxBTMXTwentydBBandwidthAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxBTMXTwentydBBandwidthAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXTwentydBBandwidthAveragingEnabledSpecifies whether to enable averaging for 20dBBandwidth measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/5fe029da-24ae-532c-a066-e12cdf181584.htm language=enus -->
## TOPIC 00039: rfmxbtdotnet/html/5fe029da-24ae-532c-a066-e12cdf181584.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/5fe029da-24ae-532c-a066-e12cdf181584.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/5fe029da-24ae-532c-a066-e12cdf181584.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccConfiguration.SetNumberOfAnalysisThreads Method

RFmxBTMXModAccConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

###### Return Value

Int32

##### Remarks

ModAccNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxBTMXModAccConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/606bdb72-7995-21df-9891-3fb89193f5cb.htm language=enus -->
## TOPIC 00040: rfmxbtdotnet/html/606bdb72-7995-21df-9891-3fb89193f5cb.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/606bdb72-7995-21df-9891-3fb89193f5cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/606bdb72-7995-21df-9891-3fb89193f5cb.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults Methods

RFmxBTMXModAccResults Methods

The [RFmxBTMXModAccResults](5cb3463b-5de4-4d0d-e13b-d3f2c4a1ffb8.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchConstellationTrace | Fetches the demodulated symbols from the enhanced data rate (EDR) portion of the EDR packet. This method is valid only for EDR packets. |
|  | FetchCSDetrendedPhaseTrace | Fetches the zero-mean Detrended Phase (deg) versus time trace. This method is valid only for low energy CS (LE-CS) packets. |
|  | FetchCSToneTrace | Fetches the CS Tone Amplitude (dBm) versus time and CS Tone Phase (deg) versus time traces. This method is valid only for low energy CS (LE-CS) packets. |
|  | FetchDemodulatedBitTrace | Fetches the ModAcc demodulated bit trace. |
|  | FetchDevm | Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets. |
|  | FetchDevmMagnitudeError | Fetches ModAcc RMS magnitude error results. These results are valid only for enhanced data rate (EDR) packets. |
|  | FetchDevmPerSymbolTrace | Fetches the DEVM values for symbols from the enhanced data rate (EDR) portion of the EDR packet. This method is valid only for EDR packets. |
|  | FetchDevmPhaseError | Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets. |
|  | FetchDf1 | Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf1maxTrace | Fetches the df1max versus the time trace. This method is applicable only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf2 | Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf2maxTrace | Fetches the df2max versus the time trace. This method is valid only for basic rate (BR) and low energy (LE) packets. |
|  | FetchDf4avgTrace | Fetches the df4avg versus the time trace. This function is valid only for LE-CS Packets. |
|  | FetchFrequencyErrorBR | Fetches the ModAcc frequency error trace for basic rate (BR) packets. |
|  | FetchFrequencyErrorEdr | Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets. |
|  | FetchFrequencyErrorLE | Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets. |
|  | FetchFrequencyErrorTraceBR | Fetches the ModAcc frequency error trace for basic rate (BR) packets. |
|  | FetchFrequencyErrorTraceLE | Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets. |
|  | FetchFrequencyErrorWiPlusW0TraceEdr | Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets. |
|  | FetchFrequencyTrace | Fetches the frequency versus time trace. This trace is valid only for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets. |
|  | FetchRmsDevmTrace | Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This method is valid only for enhanced data rate (EDR) packets. |
|  | Get99PercentDevm | Gets the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage. |
|  | GetAverageRmsMagnitudeErrorMean | Gets the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS magnitude error values computed for each averaging count.This value is expressed as a percentage. |
|  | GetAverageRmsPhaseErrorMean | Return the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
|  | GetBRInitialFrequencyErrorMaximum | Gets the initial frequency error value computed on the preamble portion of the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetBRPeakFrequencyDriftMaximum | Gets the peak frequency drift value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | GetBRPeakFrequencyDriftRateMaximum | Gets the peak frequency drift rate value computed on the BR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
|  | GetClockDriftMean | Gets the clock drift estimated over the LE-CS packet. This value is expressed in ppm. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the clock drift values computed for each averaging count. |
|  | GetDf1avgMaximum | Gets the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf1avgMean | Gets the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df1avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf1avgMinimum | Gets the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf2avgMaximum | Gets the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf2avgMean | Gets the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf2avgMinimum | Gets the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | GetDf3avgMean | Gets the df3avg value computed on the signal. When you set the ModAccAveragingEnabled method to True, it returns the mean of the df3avg results computed for each averaging count. This value is expressed in Hz. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
|  | GetEdrHeaderFrequencyErrorWiMaximum | Gets the frequency error value computed on the header of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetEdrPeakFrequencyErrorW0Maximum | Gets the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum absolute of the peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetEdrPeakFrequencyErrorWiPlusW0Maximum | Gets the peak frequency error value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIQOriginOffsetMean | Gets the I/Q origin offset estimated over the EDR portion of the EDR packets. This value is expressed in dB. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the I/Q origin offset values computed for each averaging count. |
|  | GetLEInitialFrequencyDriftMaximum | Gets the initial frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEInitialFrequencyErrorMaximum | Gets the initial frequency error value computed on the preamble portion of the LE or LE-CS packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEPeakFrequencyDriftMaximum | Gets the peak frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEPeakFrequencyDriftRateMaximum | Gets the peak frequency drift rate value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
|  | GetLEPeakFrequencyErrorMaximum | When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to Disabled, it returns the peak frequency error value computed on the LE/LE-CS packet. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | GetMinimumDf1maxMinimum | Gets the minimum df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df1max results computed for each averaging count. This value is expressed in Hz. |
|  | GetMinimumDf2maxMinimum | Gets the minimum df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df2max results computed for each averaging count. This value is expressed in Hz. |
|  | GetPeakDevmMaximum | Gets the peak of the differential EVM (DEVM) values computed on symbols in the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of peak symbol differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
|  | GetPeakDf1maxMaximum | Gets the peak df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df1max results computed for each averaging count. This value is expressed in Hz. |
|  | GetPeakDf2maxMaximum | Gets the peak df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the peak value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak df2max results computed for each averaging count. This value is expressed in Hz. |
|  | GetPeakRmsDevmMaximum | Gets the peak of the RMS differential EVM (DEVM) values computed on each 50us block of the EDR portion of the EDR packet. When you set SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns maximum of peak RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
|  | GetPeakRmsMagnitudeErrorMaximum | Gets the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count.This value is expressed as a percentage. |
|  | GetPeakRmsPhaseErrorMaximum | Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |
|  | GetPercentageOfSymbolsAboveDf1maxThreshold | Gets the percentage of symbols with df1max values that are greater than the df1max threshold defined by the standard. This result is valid only for the LE packet with a data rate of 125 Kbps. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df1max values from all averaging counts. This value expressed as a percentage. |
|  | GetPercentageOfSymbolsAboveDf2maxThreshold | Gets the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. |
|  | GetPercentageOfSymbolsAboveDf4avgThreshold | Gets the percentage of symbols with df4avg values that are greater than the df4avg threshold defined by the standard. When you set the ModAccAveragingEnabled method to True, it computes this result using the df4avg values from all averaging counts. This value is expressed as a percentage. This result is valid only for LE-CS packet with data rate 2 Mbps and when bandwidth bit period product is set to 2. |
|  | GetPercentageOfSymbolsBelow99PercentDevmLimit | Gets the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification v5.1.0. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the symbol differential EVM (DEVM) values from all averaging counts. This value is expressed as a percentage. |
|  | GetPreambleStartTimeMean | Gets the start time of the preamble of LE-CS packet. This value is expressed in seconds. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the preamble start time values computed for each averaging count. |
|  | GetRmsDevmMean | Gets the RMS differential EVM (DEVM) value computed on the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the mean of the RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/60982fd5-d464-2df6-72ea-8b8b95b9d51c.htm language=enus -->
## TOPIC 00041: rfmxbtdotnet/html/60982fd5-d464-2df6-72ea-8b8b95b9d51c.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/60982fd5-d464-2df6-72ea-8b8b95b9d51c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/60982fd5-d464-2df6-72ea-8b8b95b9d51c.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxp.Configuration Property

RFmxBTMXTxpConfiguration Property

RFmxBTMXTxpConfiguration

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXTxpConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxBTMXTxpConfiguration
	Get
```

###### Property Value

RFmxBTMXTxpConfiguration

##### See Also

###### Reference

RFmxBTMXTxp Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm language=enus -->
## TOPIC 00042: rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/6112de94-3b75-dde6-304c-53cc4e398127.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine0 Field

RFmxBTMXConstantsPxiTriggerLine0 Field

The signal is exported to the PXI trigger line 0.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine0 = "PXI_Trig0"
```

```text
Public Const PxiTriggerLine0 As String = "PXI_Trig0"
```

###### Field Value

String

##### See Also

###### Reference

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/65986d88-5e9c-7a96-5282-c3d558046d01.htm language=enus -->
## TOPIC 00043: rfmxbtdotnet/html/65986d88-5e9c-7a96-5282-c3d558046d01.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/65986d88-5e9c-7a96-5282-c3d558046d01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/65986d88-5e9c-7a96-5282-c3d558046d01.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccConfiguration.GetAveragingEnabled Method

RFmxBTMXModAccConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the ModAcc measurements.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxBTMXModAccAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXModAccAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXModAccAveragingEnabledUpon return, contains whether to enable averaging for the ModAcc measurements.

###### Return Value

Int32

##### Remarks

ModAccAveragingEnabled

False

##### See Also

###### Reference

RFmxBTMXModAccConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm language=enus -->
## TOPIC 00044: rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/664a83ab-1002-5bc3-e52b-565688cd0243.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetChannelSoundingSyncSequence Method

RFmxBTMXSetChannelSoundingSyncSequence Method

SetPacketType(String, RFmxBTMXPacketType)

SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChannelSoundingSyncSequence(
	string selectorString,
	RFmxBTMXChannelSoundingSyncSequence value
)
```

```text
Public Function SetChannelSoundingSyncSequence ( 
	selectorString As String,
	value As RFmxBTMXChannelSoundingSyncSequence
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXChannelSoundingSyncSequenceSpecifies the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone.

###### Return Value

Int32

##### Remarks

ChannelSoundingSyncSequence

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm language=enus -->
## TOPIC 00045: rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/6aae85fa-7769-e509-5e8b-e13ae1cc0f17.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.Commit Method

RFmxBTMXCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/6e24cefe-e2bb-8238-b85a-09f2d873d975.htm language=enus -->
## TOPIC 00046: rfmxbtdotnet/html/6e24cefe-e2bb-8238-b85a-09f2d873d975.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/6e24cefe-e2bb-8238-b85a-09f2d873d975.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/6e24cefe-e2bb-8238-b85a-09f2d873d975.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetDf1avgMinimum Method

RFmxBTMXModAccResultsGetDf1avgMinimum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDf1avgMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetDf1avgMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the df1avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the df1avg results computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsDf1avgMinimum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/6ee01fa8-5edd-89b6-aa92-115f38a4d460.htm language=enus -->
## TOPIC 00047: rfmxbtdotnet/html/6ee01fa8-5edd-89b6-aa92-115f38a4d460.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/6ee01fa8-5edd-89b6-aa92-115f38a4d460.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/6ee01fa8-5edd-89b6-aa92-115f38a4d460.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetDigitalEdgeTriggerSource Method

RFmxBTMXSetDigitalEdgeTriggerSource Method

SetTriggerType(String, RFmxBTMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetDigitalEdgeTriggerSource(
	string selectorString,
	string value
)
```

```text
Public Function SetDigitalEdgeTriggerSource ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemString Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm language=enus -->
## TOPIC 00048: rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/727af8da-95e8-861d-c313-ed5590836360.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidth Methods

RFmxBTMXTwentydBBandwidth Methods

The [RFmxBTMXTwentydBBandwidth](dcc38597-ee7c-66d2-d0b4-2a13b6dffb51.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidth Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm language=enus -->
## TOPIC 00049: rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/73579cbd-4db8-dce7-a281-6f8922d49aeb.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetAveragePowerMinimum Method

RFmxBTMXTxpResultsGetAveragePowerMinimum Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragePowerMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetAveragePowerMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsAveragePowerMinimum

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm language=enus -->
## TOPIC 00050: rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/738a95ab-6093-fbd5-10ee-101a978e98db.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcp Methods

RFmxBTMXAcp Methods

The [RFmxBTMXAcp](4a4c2240-0d07-6aae-387c-51eaa8015704.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXAcp Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/78830381-a03f-68be-4a87-6a28cbe81e2f.htm language=enus -->
## TOPIC 00051: rfmxbtdotnet/html/78830381-a03f-68be-4a87-6a28cbe81e2f.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/78830381-a03f-68be-4a87-6a28cbe81e2f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/78830381-a03f-68be-4a87-6a28cbe81e2f.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetPercentageOfSymbolsBelow99PercentDevmLimit Method

RFmxBTMXModAccResultsGetPercentageOfSymbolsBelow99PercentDevmLimit Method

Bluetooth Test Specification v5.1.0

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPercentageOfSymbolsBelow99PercentDevmLimit(
	string selectorString,
	out double value
)
```

```text
Public Function GetPercentageOfSymbolsBelow99PercentDevmLimit ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the Bluetooth Test Specification v5.1.0. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it computes this result using the symbol differential EVM (DEVM) values from all averaging counts. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsPercentageOfSymbolsBelow99PercentDevmLimit

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/78f72ab9-f06e-3fdf-e0a6-6a96adc6f4ef.htm language=enus -->
## TOPIC 00052: rfmxbtdotnet/html/78f72ab9-f06e-3fdf-e0a6-6a96adc6f4ef.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/78f72ab9-f06e-3fdf-e0a6-6a96adc6f4ef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/78f72ab9-f06e-3fdf-e0a6-6a96adc6f4ef.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration Methods

RFmxBTMXTxpConfiguration Methods

The [RFmxBTMXTxpConfiguration](0c1aff01-5e2d-a775-d44a-761269756ab5.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the transmit power (TXP) measurement. |
|  | ConfigureBurstSynchronizationType | Configures the type of synchronization used for detecting the start of the packet in the transmit power (TXP) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable all the traces used for transmit power (TxP) measurements. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXTxpAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the transmit power (TxP) measurements. |
|  | GetBurstSynchronizationType | Gets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the transmit power (TxP) measurements. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable all the traces used for transmit power (TxP) measurements. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXTxpAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the transmit power (TxP) measurements. |
|  | SetBurstSynchronizationType | Sets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the transmit power (TxP) measurements. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for TXP measurement.The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/81cae154-7d9a-bbf7-32dd-04377d4c06b4.htm language=enus -->
## TOPIC 00053: rfmxbtdotnet/html/81cae154-7d9a-bbf7-32dd-04377d4c06b4.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/81cae154-7d9a-bbf7-32dd-04377d4c06b4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/81cae154-7d9a-bbf7-32dd-04377d4c06b4.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXChannelSoundingToneExtensionSlot Enumeration

RFmxBTMXChannelSoundingToneExtensionSlot Enumeration

SetPacketType(String, RFmxBTMXPacketType)

SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat)

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXChannelSoundingToneExtensionSlot
```

```text
Public Enumeration RFmxBTMXChannelSoundingToneExtensionSlot
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Disabled | 0 | Specifies that there is no transmission in the CS Tone extension slot. |
|  | Enabled | 1 | Specifies that there is transmission in the CS Tone extension slot. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm language=enus -->
## TOPIC 00054: rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/81ef6106-66c3-9c11-c865-8dde2e548e9a.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.FetchReferenceChannelPower Method

RFmxBTMXAcpResultsFetchReferenceChannelPower Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchReferenceChannelPower(
	string selectorString,
	double timeout,
	out double referenceChannelPower
)
```

```text
Public Function FetchReferenceChannelPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef referenceChannelPower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **referenceChannelPower**
  - Type: SystemDouble Upon return, contains the measured power of the reference channel. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/8335f0e8-94ac-9721-22b8-460f2b639366.htm language=enus -->
## TOPIC 00055: rfmxbtdotnet/html/8335f0e8-94ac-9721-22b8-460f2b639366.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/8335f0e8-94ac-9721-22b8-460f2b639366.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/8335f0e8-94ac-9721-22b8-460f2b639366.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetLimitedConfigurationChange Method

RFmxBTMXGetLimitedConfigurationChange Method

Gets the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLimitedConfigurationChange(
	string selectorString,
	out RFmxBTMXLimitedConfigurationChange value
)
```

```text
Public Function GetLimitedConfigurationChange ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXLimitedConfigurationChangeUpon return, contains the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic.

###### Return Value

Int32

##### Remarks

LimitedConfigurationChange

Disabled

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/860de806-6dcb-56be-ab8b-42463d374766.htm language=enus -->
## TOPIC 00056: rfmxbtdotnet/html/860de806-6dcb-56be-ab8b-42463d374766.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/860de806-6dcb-56be-ab8b-42463d374766.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/860de806-6dcb-56be-ab8b-42463d374766.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetLEInitialFrequencyErrorMaximum Method

RFmxBTMXModAccResultsGetLEInitialFrequencyErrorMaximum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLEInitialFrequencyErrorMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetLEInitialFrequencyErrorMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the initial frequency error value computed on the preamble portion of the LE or LE-CS packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns a value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsLEInitialFrequencyErrorMaximum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/8a63a1c5-eaca-ae80-789c-49fc9ea93f2c.htm language=enus -->
## TOPIC 00057: rfmxbtdotnet/html/8a63a1c5-eaca-ae80-789c-49fc9ea93f2c.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/8a63a1c5-eaca-ae80-789c-49fc9ea93f2c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/8a63a1c5-eaca-ae80-789c-49fc9ea93f2c.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetChannelNumber Method

RFmxBTMXGetChannelNumber Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetChannelNumber(
	string selectorString,
	out int value
)
```

```text
Public Function GetChannelNumber ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand.

###### Return Value

Int32

##### Remarks

ChannelNumber

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/8a76f0c9-1870-ef58-ed9d-5872acb8e506.htm language=enus -->
## TOPIC 00058: rfmxbtdotnet/html/8a76f0c9-1870-ef58-ed9d-5872acb8e506.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/8a76f0c9-1870-ef58-ed9d-5872acb8e506.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/8a76f0c9-1870-ef58-ed9d-5872acb8e506.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxieDStarBLine Field

RFmxBTMXConstantsPxieDStarBLine Field

The signal is exported to the PXIe DStar B trigger line.

Namespace:

NationalInstruments.RFmx.BTMX

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

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/8ba1ae79-5cdc-35d2-2f77-80ebaec84672.htm language=enus -->
## TOPIC 00059: rfmxbtdotnet/html/8ba1ae79-5cdc-35d2-2f77-80ebaec84672.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/8ba1ae79-5cdc-35d2-2f77-80ebaec84672.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/8ba1ae79-5cdc-35d2-2f77-80ebaec84672.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.GetLowerOffsetMargin Method

RFmxBTMXAcpResultsGetLowerOffsetMargin Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

Symmetric

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetMargin(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetMargin ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric.

###### Return Value

Int32

##### Remarks

AcpResultsLowerOffsetMargin

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm language=enus -->
## TOPIC 00060: rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/971b9cd2-fe42-3993-7f3f-a544bec8fa7e.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.GetAllTracesEnabled Method

RFmxBTMXAcpConfigurationGetAllTracesEnabled Method

Gets whether to enable all traces for the adjacent channel power (ACP) measurements.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanUpon return, contains whether to enable all traces for the adjacent channel power (ACP) measurements.

###### Return Value

Int32

##### Remarks

AcpAllTracesEnabled

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/97ce6b6e-dfb1-dd6b-fe7e-c63c03193464.htm language=enus -->
## TOPIC 00061: rfmxbtdotnet/html/97ce6b6e-dfb1-dd6b-fe7e-c63c03193464.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/97ce6b6e-dfb1-dd6b-fe7e-c63c03193464.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/97ce6b6e-dfb1-dd6b-fe7e-c63c03193464.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.SetNumberOfOffsets Method

RFmxBTMXAcpConfigurationSetNumberOfOffsets Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

Symmetric

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfOffsets(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfOffsets ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Specifies the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. This method also returns the actual number of offsets used in the ACP measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand.

###### Return Value

Int32

##### Remarks

AcpNumberOfOffsets

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm language=enus -->
## TOPIC 00062: rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/9aa30305-893f-bf34-c5bc-0f94eaacdf70.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetAttributeDouble Method

RFmxBTMXSetAttributeDouble Method

Sets the value of a Double attribute.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeDouble(
	string selectorString,
	int attributeIdentifier,
	double value
)
```

```text
Public Function SetAttributeDouble ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemDoubleSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm language=enus -->
## TOPIC 00063: rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/9ab6cf60-282d-075f-c601-446cf2d4e5f6.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchFrequencyTrace Method

RFmxBTMXModAccResultsFetchFrequencyTrace Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchFrequencyTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> frequency
)
```

```text
Public Function FetchFrequencyTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef frequency As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **frequency**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the frequency versus time trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm language=enus -->
## TOPIC 00064: rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/9bd7a680-778e-52d0-3401-cd38f8277a5e.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults Class

RFmxBTMXAcpResults Class

Provides methods to fetch and read the ACP measurement results.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXAcpResults : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXAcpResults
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXAcpResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchAbsolutePowerTrace | Fetches the absolute power trace for ACP measurement. |
|  | FetchMaskTrace | Fetches the limit with exception mask and limit without exception mask traces for ACP measurement. This method returns a valid trace only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | FetchMeasurementStatus | Fetches the overall ACP measurement status based on the measurement limits as defined by the standard if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method is not valid if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. |
|  | FetchOffsetMeasurement | Fetches the absolute powers, relative powers and margins measured in the offset channel. Use "offset(k)" as the selector string to read results from this method. |
|  | FetchOffsetMeasurementArray | Fetches the array of absolute powers, relative powers and margins measured in the offset channels. |
|  | FetchReferenceChannelPower | Returns the measured power of the reference channel. |
|  | FetchSpectrum | Fetches the spectrum used for ACP measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLowerOffsetAbsolutePower | Gets the absolute power measured in the lower offset channel. This value is expressed in dBm. |
|  | GetLowerOffsetMargin | Gets the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. |
|  | GetLowerOffsetRelativePower | Gets the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | GetMeasurementStatus | Indicates the overall measurement status based on the measurement limits specified by the standard when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | GetReferenceChannelPower | Gets the measured power of the reference channel. This value is expressed in dBm. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUpperOffsetAbsolutePower | Gets the absolute power measured in the upper offset channel. This value is expressed in dBm. |
|  | GetUpperOffsetMargin | Gets the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. This method returns NaN if you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. |
|  | GetUpperOffsetRelativePower | Gets the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm language=enus -->
## TOPIC 00065: rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/9c1f2c40-bd37-a665-93fc-6e571a07b278.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpAveragingEnabled Enumeration

RFmxBTMXAcpAveragingEnabled Enumeration

Specifies whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxBTMXAcpAveragingEnabled
```

```text
Public Enumeration RFmxBTMXAcpAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The measurement uses the SetAveragingCount(String, Int32) method as the number of acquisitions over which the ACP measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/9f9b5241-352b-1467-c22d-292db1ecc1bb.htm language=enus -->
## TOPIC 00066: rfmxbtdotnet/html/9f9b5241-352b-1467-c22d-292db1ecc1bb.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/9f9b5241-352b-1467-c22d-292db1ecc1bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/9f9b5241-352b-1467-c22d-292db1ecc1bb.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.FetchLECteReferencePeriodPowers Method

RFmxBTMXTxpResultsFetchLECteReferencePeriodPowers Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLECteReferencePeriodPowers(
	string selectorString,
	double timeout,
	out double referencePeriodAveragePowerMean,
	out double referencePeriodPeakAbsolutePowerDeviationMaximum
)
```

```text
Public Function FetchLECteReferencePeriodPowers ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef referencePeriodAveragePowerMean As Double,
	<OutAttribute> ByRef referencePeriodPeakAbsolutePowerDeviationMaximum As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **referencePeriodAveragePowerMean**
  - Type: SystemDouble Upon return, contains the average power computed over the reference period in the CTE portion of the LE packet. When you set the TXP Averaging Enabled method to true, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm.
- **referencePeriodPeakAbsolutePowerDeviationMaximum**
  - Type: SystemDouble Upon return, contains the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. When you set the TXP Averaging Enabled method to true, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a0218a9e-72f5-5ae9-bbba-1dbd413ee018.htm language=enus -->
## TOPIC 00067: rfmxbtdotnet/html/a0218a9e-72f5-5ae9-bbba-1dbd413ee018.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a0218a9e-72f5-5ae9-bbba-1dbd413ee018.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a0218a9e-72f5-5ae9-bbba-1dbd413ee018.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.FetchPowerTrace Method

RFmxBTMXTxpResultsFetchPowerTrace Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPowerTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> power
)
```

```text
Public Function FetchPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef power As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **power**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the power versus time trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a2b83d15-488a-5707-31d4-991faa0b2166.htm language=enus -->
## TOPIC 00068: rfmxbtdotnet/html/a2b83d15-488a-5707-31d4-991faa0b2166.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a2b83d15-488a-5707-31d4-991faa0b2166.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a2b83d15-488a-5707-31d4-991faa0b2166.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetLEInitialFrequencyDriftMaximum Method

RFmxBTMXModAccResultsGetLEInitialFrequencyDriftMaximum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLEInitialFrequencyDriftMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetLEInitialFrequencyDriftMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the initial frequency drift value computed on the LE packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the value corresponding to the maximum of the absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsLEInitialFrequencyDriftMaximum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a39f9ea6-5da0-f767-0805-dac0be297cef.htm language=enus -->
## TOPIC 00069: rfmxbtdotnet/html/a39f9ea6-5da0-f767-0805-dac0be297cef.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a39f9ea6-5da0-f767-0805-dac0be297cef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a39f9ea6-5da0-f767-0805-dac0be297cef.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetResultFetchTimeout Method

RFmxBTMXGetResultFetchTimeout Method

Gets the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetResultFetchTimeout(
	string selectorString,
	out double value
)
```

```text
Public Function GetResultFetchTimeout ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete.

###### Return Value

Int32

##### Remarks

ResultFetchTimeout

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a449d6fa-9f20-9315-4267-7056982939a4.htm language=enus -->
## TOPIC 00070: rfmxbtdotnet/html/a449d6fa-9f20-9315-4267-7056982939a4.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a449d6fa-9f20-9315-4267-7056982939a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a449d6fa-9f20-9315-4267-7056982939a4.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetDataRate Method

RFmxBTMXGetDataRate Method

Gets the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDataRate(
	string selectorString,
	out int value
)
```

```text
Public Function GetDataRate ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types.

###### Return Value

Int32

##### Remarks

DataRate

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm language=enus -->
## TOPIC 00071: rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a4fa9d54-57c5-4e03-ef25-faaeb6ba4c0d.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXConstants.PxiTriggerLine2 Field

RFmxBTMXConstantsPxiTriggerLine2 Field

The signal is exported to the PXI trigger line 2.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine2 = "PXI_Trig2"
```

```text
Public Const PxiTriggerLine2 As String = "PXI_Trig2"
```

###### Field Value

String

##### See Also

###### Reference

RFmxBTMXConstants Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a5cf887e-0325-2c40-d88e-f5b8df86a88f.htm language=enus -->
## TOPIC 00072: rfmxbtdotnet/html/a5cf887e-0325-2c40-d88e-f5b8df86a88f.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a5cf887e-0325-2c40-d88e-f5b8df86a88f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a5cf887e-0325-2c40-d88e-f5b8df86a88f.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.BuildSlotString Method

RFmxBTMXBuildSlotString Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildSlotString(
	string selectorString,
	int slotNumber
)
```

```text
Public Shared Function BuildSlotString ( 
	selectorString As String,
	slotNumber As Integer
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **slotNumber**
  - Type: SystemInt32 Specifies the slot number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a6f536ca-dfd9-4b01-ee77-60d5df0bf51b.htm language=enus -->
## TOPIC 00073: rfmxbtdotnet/html/a6f536ca-dfd9-4b01-ee77-60d5df0bf51b.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a6f536ca-dfd9-4b01-ee77-60d5df0bf51b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a6f536ca-dfd9-4b01-ee77-60d5df0bf51b.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetMinimumDf2maxMinimum Method

RFmxBTMXModAccResultsGetMinimumDf2maxMinimum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMinimumDf2maxMinimum(
	string selectorString,
	out double value
)
```

```text
Public Function GetMinimumDf2maxMinimum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the minimum df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the minimum value. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the minimum of the Min df2max results computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsMinimumDf2maxMinimum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a71f9012-a67b-1e58-5f5a-42c6a845d8c3.htm language=enus -->
## TOPIC 00074: rfmxbtdotnet/html/a71f9012-a67b-1e58-5f5a-42c6a845d8c3.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a71f9012-a67b-1e58-5f5a-42c6a845d8c3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a71f9012-a67b-1e58-5f5a-42c6a845d8c3.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchDf1maxTrace Method

RFmxBTMXModAccResultsFetchDf1maxTrace Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDf1maxTrace(
	string selectorString,
	double timeout,
	ref float[] time,
	ref float[] df1max
)
```

```text
Public Function FetchDf1maxTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef time As Single(),
	ByRef df1max As Single()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **time**
  - Type: SystemSingle Upon return, contains the array of time instances at which the df1max values are computed. This value is expressed in seconds.
- **df1max**
  - Type: SystemSingle Upon return, contains the array of df1max values computed over the packet at each time instance. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm language=enus -->
## TOPIC 00075: rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a848d15e-c40c-8074-da83-89c1891c1adf.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetLECteReferencePeriodAveragePowerMean Method

RFmxBTMXTxpResultsGetLECteReferencePeriodAveragePowerMean Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLECteReferencePeriodAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetLECteReferencePeriodAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsLECteReferencePeriodAveragePowerMean

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm language=enus -->
## TOPIC 00076: rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a91a3ec1-2103-d72e-b2a0-8ea63a08a5f9.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.Txp Property

RFmxBTMXTxp Property

RFmxBTMXTxp

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXTxp Txp { get; }
```

```text
Public ReadOnly Property Txp As RFmxBTMXTxp
	Get
```

###### Property Value

RFmxBTMXTxp

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a95308d5-fe6a-6984-57ed-38232c51e856.htm language=enus -->
## TOPIC 00077: rfmxbtdotnet/html/a95308d5-fe6a-6984-57ed-38232c51e856.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a95308d5-fe6a-6984-57ed-38232c51e856.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a95308d5-fe6a-6984-57ed-38232c51e856.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration.ConfigureOffsetChannelMode Method

RFmxBTMXAcpConfigurationConfigureOffsetChannelMode Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetChannelMode(
	string selectorString,
	RFmxBTMXAcpOffsetChannelMode offsetChannelMode
)
```

```text
Public Function ConfigureOffsetChannelMode ( 
	selectorString As String,
	offsetChannelMode As RFmxBTMXAcpOffsetChannelMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetChannelMode**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXAcpOffsetChannelModeSpecifies which offset channels are used for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a96e9060-b499-9b78-b7d0-1f63e9940f34.htm language=enus -->
## TOPIC 00078: rfmxbtdotnet/html/a96e9060-b499-9b78-b7d0-1f63e9940f34.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a96e9060-b499-9b78-b7d0-1f63e9940f34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a96e9060-b499-9b78-b7d0-1f63e9940f34.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.GetDf2avgMaximum Method

RFmxBTMXModAccResultsGetDf2avgMaximum Method

SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDf2avgMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetDf2avgMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the df2avg value computed on the signal. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the df2avg results computed for each averaging count. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ModAccResultsDf2avgMaximum

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm language=enus -->
## TOPIC 00079: rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/a9ee4cca-8889-4464-a5c8-d86a49cb1ae4.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetAccessAddress Method

RFmxBTMXSetAccessAddress Method

Sets the 32-bit LE access address.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAccessAddress(
	string selectorString,
	int value
)
```

```text
Public Function SetAccessAddress ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the 32-bit LE access address.

###### Return Value

Int32

##### Remarks

AccessAddress

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm language=enus -->
## TOPIC 00080: rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/aa732f1b-7911-af03-f6cf-74b9fa3d246f.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeConfiguration Class

RFmxBTMXFrequencyRangeConfiguration Class

Provides methods to configure the FrequencyRange measurement.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXFrequencyRangeConfiguration : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXFrequencyRangeConfiguration
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXFrequencyRangeConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the FrequencyRange measurement. |
|  | ConfigureSpan | Configures the span for the FrequencyRange measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable all the traces for FrequencyRange measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the FrequencyRange measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification v5.1.0. This measurement is valid only for basic rate (BR) packets. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetSpan | Gets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable all the traces for FrequencyRange measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXFrequencyRangeAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the FrequencyRange measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification v5.1.0. This measurement is valid only for basic rate (BR) packets. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetSpan | Sets the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/ac000cf2-f8a1-928f-172f-47221bc83669.htm language=enus -->
## TOPIC 00081: rfmxbtdotnet/html/ac000cf2-f8a1-928f-172f-47221bc83669.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/ac000cf2-f8a1-928f-172f-47221bc83669.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/ac000cf2-f8a1-928f-172f-47221bc83669.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetCteLength Method

RFmxBTMXGetCteLength Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfArrival

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCteLength(
	string selectorString,
	out double value
)
```

```text
Public Function GetCteLength ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature.

###### Return Value

Int32

##### Remarks

CteLength

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/ad1f371a-c1d9-0e1e-6900-e2208b23c480.htm language=enus -->
## TOPIC 00082: rfmxbtdotnet/html/ad1f371a-c1d9-0e1e-6900-e2208b23c480.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/ad1f371a-c1d9-0e1e-6900-e2208b23c480.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/ad1f371a-c1d9-0e1e-6900-e2208b23c480.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetChannelNumber Method

RFmxBTMXSetChannelNumber Method

SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode)

InBand

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetChannelNumber(
	string selectorString,
	int value
)
```

```text
Public Function SetChannelNumber ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand.

###### Return Value

Int32

##### Remarks

ChannelNumber

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/ae314103-394f-e30c-2c6a-cf977df34ed8.htm language=enus -->
## TOPIC 00083: rfmxbtdotnet/html/ae314103-394f-e30c-2c6a-cf977df34ed8.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/ae314103-394f-e30c-2c6a-cf977df34ed8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/ae314103-394f-e30c-2c6a-cf977df34ed8.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.SetIQPowerEdgeTriggerLevel Method

RFmxBTMXSetIQPowerEdgeTriggerLevel Method

Sets the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQPowerEdgeTriggerLevel(
	string selectorString,
	double value
)
```

```text
Public Function SetIQPowerEdgeTriggerLevel ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevel

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm language=enus -->
## TOPIC 00084: rfmxbtdotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.InstrMX Namespace

NationalInstruments.RFmx.InstrMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxBTMXExtension | Provides extension methods to create BT signal configuration. These methods are added to RFmxInstrMX class. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b0cf6f5e-8475-0f7e-df04-d0cdfd214413.htm language=enus -->
## TOPIC 00085: rfmxbtdotnet/html/b0cf6f5e-8475-0f7e-df04-d0cdfd214413.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b0cf6f5e-8475-0f7e-df04-d0cdfd214413.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b0cf6f5e-8475-0f7e-df04-d0cdfd214413.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTwentydBBandwidthConfiguration.GetMeasurementEnabled Method

RFmxBTMXTwentydBBandwidthConfigurationGetMeasurementEnabled Method

Bluetooth Test Specification v5.1.0

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBoolean Upon return, contains whether to enable the 20dBBandwidth measurement specified in section 4.5.5 of the Bluetooth Test Specification v5.1.0. The measurement uses a span of 3 MHz internally. This measurement is valid only for basic rate (BR) packets.

###### Return Value

Int32

##### Remarks

TwentydBBandwidthMeasurementEnabled

##### See Also

###### Reference

RFmxBTMXTwentydBBandwidthConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b0e22d32-88c5-b4e0-2e34-4e55baf6b2dc.htm language=enus -->
## TOPIC 00086: rfmxbtdotnet/html/b0e22d32-88c5-b4e0-2e34-4e55baf6b2dc.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b0e22d32-88c5-b4e0-2e34-4e55baf6b2dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b0e22d32-88c5-b4e0-2e34-4e55baf6b2dc.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults Class

RFmxBTMXTxpResults Class

Provides methods to fetch and read the TXP measurement results.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXTxpResults : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXTxpResults
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXTxpResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchEdrPowers | Fetches TXP measurement results for enhanced data rate (EDR) packets. |
|  | FetchLECteReferencePeriodPowers | Fetches the transmit power (TXP) measurement over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
|  | FetchLECteTransmitSlotPowers | Fetches the transmit power (TXP) measurement over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
|  | FetchLECteTransmitSlotPowersArray | Fetches an array of transmit power (TXP) measurement over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. |
|  | FetchPowers | Fetches TXP measurement results. These results are valid for all packets. |
|  | FetchPowerTrace | Fetches the power versus time trace. |
|  | GetAveragePowerMaximum | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetAveragePowerMean | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. This value is expressed in dBm. When you set the TXP Averaging Enabled method to True, it returns the mean of the average power results computed for each averaging count. |
|  | GetAveragePowerMinimum | Gets the average power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled method to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetEdrDpskAveragePowerMean | Gets the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetEdrDpskGfskAveragePowerRatioMean | Gets the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |
|  | GetEdrGfskAveragePowerMean | Gets the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled method to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLECSPhaseMeasurementPeriodAveragePowerMean |  |
|  | GetLECteReferencePeriodAveragePowerMean | Gets the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetLECteReferencePeriodPeakAbsolutePowerDeviationMaximum | Gets the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | GetLECteTransmitSlotAveragePowerMean | Gets the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
|  | GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum | Gets the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | GetPeakPowerMaximum | Gets the peak power computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm. |
|  | GetPeakToAveragePowerRatioMaximum | Gets the peak to average power ratio computed over the measurement interval. When you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the TXP Averaging Enabled method to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b141a549-40ab-8118-2d1b-38cc2bd692eb.htm language=enus -->
## TOPIC 00087: rfmxbtdotnet/html/b141a549-40ab-8118-2d1b-38cc2bd692eb.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b141a549-40ab-8118-2d1b-38cc2bd692eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b141a549-40ab-8118-2d1b-38cc2bd692eb.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpConfiguration Methods

RFmxBTMXAcpConfiguration Methods

The [RFmxBTMXAcpConfiguration](0f850585-6370-4d1b-c6d9-497787643b66.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the adjacent channel power (ACP) measurement. |
|  | ConfigureBurstSynchronizationType | Configures the type of synchronization used for detecting the start of the packet in the adjacent channel power (ACP) measurement. |
|  | ConfigureNumberOfOffsets | Configures the number of offsets for the adjacent channel power (ACP) measurement. |
|  | ConfigureOffsetChannelMode | Configures the offset channels used for the adjacent channel power (ACP) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable all traces for the adjacent channel power (ACP) measurements. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXAcpAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the ACP measurement. |
|  | GetBurstSynchronizationType | Gets the type of synchronization used for detecting the start of the EDR packet in the adjacent channel power (ACP) measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the ACP measurement. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
|  | GetNumberOfOffsets | Gets the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. This method also returns the actual number of offsets used in the ACP measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | GetOffsetChannelMode | Gets which offset channels are used for the measurement. |
|  | GetOffsetFrequency | Gets the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz. |
|  | GetReferenceChannelBandwidth |  |
|  | GetReferenceChannelBandwidthMode |  |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable all traces for the adjacent channel power (ACP) measurements. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxBTMXAcpAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the ACP measurement. |
|  | SetBurstSynchronizationType | Sets the type of synchronization used for detecting the start of the EDR packet in the adjacent channel power (ACP) measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the ACP measurement. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
|  | SetNumberOfOffsets | Sets the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to Symmetric. This method also returns the actual number of offsets used in the ACP measurement when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | SetOffsetChannelMode | Sets which offset channels are used for the measurement. |
|  | SetReferenceChannelBandwidth |  |
|  | SetReferenceChannelBandwidthMode |  |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxBTMXAcpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b416e41e-d2c0-aea0-7307-0f48e2c231df.htm language=enus -->
## TOPIC 00088: rfmxbtdotnet/html/b416e41e-d2c0-aea0-7307-0f48e2c231df.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b416e41e-d2c0-aea0-7307-0f48e2c231df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b416e41e-d2c0-aea0-7307-0f48e2c231df.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum Method

RFmxBTMXTxpResultsGetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum(
	string selectorString,
	out double value
)
```

```text
Public Function GetLECteTransmitSlotPeakAbsolutePowerDeviationMaximum ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

TxpResultsLECteTransmitSlotPeakAbsolutePowerDeviationMaximum

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b41907f2-4290-5c77-98a0-e4b9943786ad.htm language=enus -->
## TOPIC 00089: rfmxbtdotnet/html/b41907f2-4290-5c77-98a0-e4b9943786ad.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b41907f2-4290-5c77-98a0-e4b9943786ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b41907f2-4290-5c77-98a0-e4b9943786ad.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeResults Class

RFmxBTMXFrequencyRangeResults Class

Provides methods to fetch and read the FrequencyRange measurement results.

##### Inheritance Hierarchy

RFmxBTMXSubObject

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMXFrequencyRangeResults : RFmxBTMXSubObject
```

```text
Public NotInheritable Class RFmxBTMXFrequencyRangeResults
	Inherits RFmxBTMXSubObject
```

The RFmxBTMXFrequencyRangeResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Fetches the FrequencyRange measurement results. |
|  | FetchSpectrum | Fetches the FrequencyRange spectrum trace. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetHighFrequency | Gets the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
|  | GetLowFrequency | Gets the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b4959ee0-b5a5-f453-cbca-1449a4961380.htm language=enus -->
## TOPIC 00090: rfmxbtdotnet/html/b4959ee0-b5a5-f453-cbca-1449a4961380.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b4959ee0-b5a5-f453-cbca-1449a4961380.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b4959ee0-b5a5-f453-cbca-1449a4961380.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetDetectedDataRate Method

RFmxBTMXGetDetectedDataRate Method

Gets the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE. This method can be queried only after calling the RFmxBT Auto Detect Signal function.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectedDataRate(
	string selectorString,
	out int value
)
```

```text
Public Function GetDetectedDataRate ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE. This method can be queried only after calling the RFmxBT Auto Detect Signal function.

###### Return Value

Int32

##### Remarks

DetectedDataRate

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm language=enus -->
## TOPIC 00091: rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b500078d-f248-604d-1705-a27043423dbc.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.GetUpperOffsetAbsolutePower Method

RFmxBTMXAcpResultsGetUpperOffsetAbsolutePower Method

Gets the absolute power measured in the upper offset channel. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the absolute power measured in the upper offset channel. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AcpResultsUpperOffsetAbsolutePower

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm language=enus -->
## TOPIC 00092: rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b568f0af-2900-6f44-0170-3e48080b0de8.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAcc.Configuration Property

RFmxBTMXModAccConfiguration Property

RFmxBTMXModAccConfiguration

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxBTMXModAccConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxBTMXModAccConfiguration
	Get
```

###### Property Value

RFmxBTMXModAccConfiguration

##### See Also

###### Reference

RFmxBTMXModAcc Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b56c48fa-672d-4d1a-585b-6858d13123f9.htm language=enus -->
## TOPIC 00093: rfmxbtdotnet/html/b56c48fa-672d-4d1a-585b-6858d13123f9.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b56c48fa-672d-4d1a-585b-6858d13123f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b56c48fa-672d-4d1a-585b-6858d13123f9.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetAttributeString Method

RFmxBTMXGetAttributeString Method

Gets the value of a of an RFmx string.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeString(
	string selectorString,
	int attributeIdentifier,
	out string value
)
```

```text
Public Function GetAttributeString ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx BT Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemStringUpon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b5e2de9e-d79e-41f4-e3f3-c89b23495f06.htm language=enus -->
## TOPIC 00094: rfmxbtdotnet/html/b5e2de9e-d79e-41f4-e3f3-c89b23495f06.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b5e2de9e-d79e-41f4-e3f3-c89b23495f06.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b5e2de9e-d79e-41f4-e3f3-c89b23495f06.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetCteNumberOfTransmitSlots Method

RFmxBTMXGetCteNumberOfTransmitSlots Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfArrival

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCteNumberOfTransmitSlots(
	string selectorString,
	out int value
)
```

```text
Public Function GetCteNumberOfTransmitSlots ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the number of transmit slots in the constant time extension portion of the generated LE packet. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature.

###### Return Value

Int32

##### Remarks

CteNumberOfTransmitSlots

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b8beb6f9-740d-d631-8488-0326b6af5f6e.htm language=enus -->
## TOPIC 00095: rfmxbtdotnet/html/b8beb6f9-740d-d631-8488-0326b6af5f6e.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b8beb6f9-740d-d631-8488-0326b6af5f6e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b8beb6f9-740d-d631-8488-0326b6af5f6e.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXFrequencyRangeResults.FetchSpectrum Method

RFmxBTMXFrequencyRangeResultsFetchSpectrum Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSpectrum(
	string selectorString,
	double timeout,
	ref Spectrum<float> spectrum
)
```

```text
Public Function FetchSpectrum ( 
	selectorString As String,
	timeout As Double,
	ByRef spectrum As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **spectrum**
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the FrequencyRange spectrum trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXFrequencyRangeResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm language=enus -->
## TOPIC 00096: rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b955c9d0-50c9-21df-842a-e3481e5fe113.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX Class

RFmxBTMX Class

Defines a root class which is used to identify and control BT signal configuration.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxBTMX : ISignalConfiguration, 
	IDisposable
```

```text
Public NotInheritable Class RFmxBTMX
	Implements ISignalConfiguration, IDisposable
```

The RFmxBTMX type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Acp | Gets the RFmxBTMXAcp instance that represents the ACP measurement. |
|  | FrequencyRange | Gets the RFmxBTMXFrequencyRange instance that represents the FrequencyRange measurement. |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | ModAcc | Gets the RFmxBTMXModAcc instance that represents the ModAcc measurement. |
|  | ModSpectrum | Gets the RFmxBTMXModSpectrum instance that represents the ModSpectrum measurement. |
|  | PowerRamp | Gets the RFmxBTMXPowerRamp instance that represents the PowerRamp measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxBTMX. |
|  | TwentydBBandwidth | Gets the RFmxBTMXTwentydBBandwidth instance that represents the 20dBBandwidth measurement. |
|  | Txp | Gets the RFmxBTMXTxp instance that represents the TXP measurement. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(String, String) or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either IQ or IQorSpectral. Query the Recommended Acquisition Type method after calling the RFmxBT Commit method. |
|  | AutoDetectSignal | Detects the Bluetooth packet and returns the detected packet type, data rate, and payload length. |
|  | AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(String, Double) method. Use this method to help calculate an approximate setting for the reference level. The RFmxBT Auto Level method does the following: Resets the mixer level, mixer level offset and IF output power offset. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings. Iterates to adjust the reference level based on the input signal peak power. Uses immediate triggering and restores the trigger settings back to user setting after completing execution. You can also specify the starting reference level using the Auto Level Initial Reference Level method.When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxBT Auto Level method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method, thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildOffsetString | Creates the offset string. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSlotString | Creates a selector string for use with the TXP configuration or fetch methods and methods. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxBT commits settings to the hardware when you call the Initiate(String, String) method or any of the measurement Read methods. |
|  | ConfigureChannelNumber | Configures the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification. |
|  | ConfigureDataRate | Configures the data rate of the low energy (LE) or low energy - channel sounding (LE-CS) packet to be measured. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureDirectionFinding | Obsolete. Configures the mode of direction finding and the length of Constant tone extension field in the generated signal. |
|  | ConfigureExternalAttenuation | Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
|  | ConfigureFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
|  | ConfigureLEDirectionFinding | Configures the mode of direction finding, length of the constant tone extension field, and the duration of the switching slot in the generated signal. |
|  | ConfigurePacketType | Configures the type of Bluetooth packet to be measured. |
|  | ConfigurePayloadBitPattern | Configures the bit pattern present in the payload of the packet. |
|  | ConfigurePayloadLength | Configures the payloadLengthMode and Auto parameters that decide the length of the payload to be used for the measurement. |
|  | ConfigureReferenceLevel | Configures the reference level which represents the maximum expected power of an RF input signal. |
|  | ConfigureRF | Configures the RF methods of the signal specified by the selector string. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
|  | DeleteSignalConfiguration | Deletes an instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAccessAddress | Gets the 32-bit LE access address. |
|  | GetAllNamedResultNames | Gets the named result names of the signal that you specify in the selectorString parameter. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | GetBandwidthBitPeriodProduct | Gets the bandwidth bit period product of GFSK modulation for LE-CS packet type. |
|  | GetBDAddressLap | Gets the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |
|  | GetCenterFrequency | Gets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
|  | GetChannelNumber | Gets the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | GetChannelSoundingAntennaSwitchTime | Gets the Channel Sounding Antenna Switch Time for the LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | GetChannelSoundingNumberOfAntennaPath | Gets the number of antenna paths for the generated LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | GetChannelSoundingPacketFormat | Gets the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS. |
|  | GetChannelSoundingPhaseMeasurementPeriod | Gets the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | GetChannelSoundingSyncSequence | Gets the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
|  | GetChannelSoundingToneExtensionSlot | Gets whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | GetCteLength | Gets the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |
|  | GetCteNumberOfTransmitSlots | Gets the number of transmit slots in the constant time extension portion of the generated LE packet. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
|  | GetCteSlotDuration | Gets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
|  | GetDataRate | Gets the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types. |
|  | GetDetectedDataRate | Gets the data rate detected by the RFmxBT Auto Detect Signal function. This method returns a valid data rate only if the Detected Packet Type method returns LE. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
|  | GetDetectedPacketType |  |
|  | GetDetectedPayloadLength | Gets the payload length detected by the RFmxBT Auto Detect Signal function. This method can be queried only after calling the RFmxBT Auto Detect Signal function. |
|  | GetDigitalEdgeTriggerEdge | Gets the active edge for the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | GetDigitalEdgeTriggerSource | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | GetDirectionFindingMode | Gets the mode of direction finding. |
|  | GetErrorString | Converts the status code returned by an RFmxBT function into a string. |
|  | GetExternalAttenuation | Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIQPowerEdgeTriggerLevel | Gets the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
|  | GetPacketType | Gets the type of the Bluetooth packet to be measured. |
|  | GetPayloadBitPattern | Gets the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. |
|  | GetPayloadLength | Gets the payload length of the signal in bytes. This method is applicable only when you set the SetPayloadLengthMode(String, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length used for measurement if you set the Payload Length Mode method to Auto. |
|  | GetPayloadLengthMode | Gets the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(String, Int32) properties decide the length of the payload to be used for measurement. |
|  | GetReferenceLevel | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842. |
|  | GetResultFetchTimeout | Gets the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | GetTriggerDelay | Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | GetTriggerMinimumQuietTimeDuration | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement computes the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the type of trigger to be used for signal acquisition. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetWarning | Gets the latest warning code and description. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxBT_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configure an invalid trigger. You have not previously called the Initiate(String, String) method. |
|  | SetAccessAddress | Sets the 32-bit LE access address. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SetBandwidthBitPeriodProduct | Sets the bandwidth bit period product of GFSK modulation for LE-CS packet type. |
|  | SetBDAddressLap | Sets the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). |
|  | SetCenterFrequency | Sets the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
|  | SetChannelNumber | Sets the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This method is applicable when you enable the ACP measurement and when you set the SetOffsetChannelMode(String, RFmxBTMXAcpOffsetChannelMode) method to InBand. |
|  | SetChannelSoundingAntennaSwitchTime | Sets the Channel Sounding Antenna Switch Time for the LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | SetChannelSoundingNumberOfAntennaPath | Sets the number of antenna paths for the generated LE-CS packet. This method is applicable only when you set the PacketType method to PacketTypeLE and the ChannelSoundingPacketFormat method to any value other than Sync. |
|  | SetChannelSoundingPacketFormat | Sets the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS. |
|  | SetChannelSoundingPhaseMeasurementPeriod | Sets the Channel Sounding Phase Measurement Period for the LE-CS packet. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | SetChannelSoundingSyncSequence | Sets the type of sequence present in the SYNC portion after trailer bits. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than CS Tone. |
|  | SetChannelSoundingToneExtensionSlot | Sets whether the tone extension slot transmission is enabled after CS Tone. This method is applicable only when you set the SetPacketType(String, RFmxBTMXPacketType) method to LE-CS and the SetChannelSoundingPacketFormat(String, RFmxBTMXChannelSoundingPacketFormat) method to any value other than SYNC. |
|  | SetCteLength | Sets the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to either AngleOfArrival or AngleOfDepature. |
|  | SetCteSlotDuration | Sets the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This method is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfArrival or AngleOfDepature. |
|  | SetDataRate | Sets the data rate of the LE/LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This method is applicable to LE/LE-CS packet types. |
|  | SetDigitalEdgeTriggerEdge | Sets the active edge for the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to DigitalEdge. |
|  | SetDirectionFindingMode | Sets the mode of direction finding. |
|  | SetExternalAttenuation | Sets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. |
|  | SetIQPowerEdgeTriggerLevel | Sets the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This method is valid only when you set the SetTriggerType(String, RFmxBTMXTriggerType) method to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this method, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. |
|  | SetPacketType | Sets the type of the Bluetooth packet to be measured. |
|  | SetPayloadBitPattern | Sets the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. |
|  | SetPayloadLength | Sets the payload length of the signal in bytes. This method is applicable only when you set the SetPayloadLengthMode(String, RFmxBTMXPayloadLengthMode) method to Manual. This method returns the payload length used for measurement if you set the Payload Length Mode method to Auto. |
|  | SetPayloadLengthMode | Sets the payload length mode of the signal to be measured. The payload length mode and SetPayloadLength(String, Int32) properties decide the length of the payload to be used for measurement. |
|  | SetReferenceLevel | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842. |
|  | SetResultFetchTimeout | Sets the time, in seconds, to wait before results are available in the RFmxBT_PropertyNode. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxBT Property Node waits until the measurement is complete. |
|  | SetSelectedPorts | Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | SetTriggerDelay | Sets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | SetTriggerMinimumQuietTimeDuration | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement computes the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the type of trigger to be used for signal acquisition. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/b99c2f18-5b51-0d8d-71fd-e52ad62ce836.htm language=enus -->
## TOPIC 00097: rfmxbtdotnet/html/b99c2f18-5b51-0d8d-71fd-e52ad62ce836.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/b99c2f18-5b51-0d8d-71fd-e52ad62ce836.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/b99c2f18-5b51-0d8d-71fd-e52ad62ce836.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.Get99PercentDevm Method

RFmxBTMXModAccResultsGet99PercentDevm Method

Gets the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int Get99PercentDevm(
	string selectorString,
	out double value
)
```

```text
Public Function Get99PercentDevm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResults99PercentDevm

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/bb728347-4c6f-7834-f76b-97f429d0b1b2.htm language=enus -->
## TOPIC 00098: rfmxbtdotnet/html/bb728347-4c6f-7834-f76b-97f429d0b1b2.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/bb728347-4c6f-7834-f76b-97f429d0b1b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/bb728347-4c6f-7834-f76b-97f429d0b1b2.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetAutoLevelInitialReferenceLevel Method

RFmxBTMXGetAutoLevelInitialReferenceLevel Method

Gets the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AutoLevelInitialReferenceLevel

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/bb8738ae-f18c-c792-f9f7-91a77bb672eb.htm language=enus -->
## TOPIC 00099: rfmxbtdotnet/html/bb8738ae-f18c-c792-f9f7-91a77bb672eb.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/bb8738ae-f18c-c792-f9f7-91a77bb672eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/bb8738ae-f18c-c792-f9f7-91a77bb672eb.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration.GetAveragingEnabled Method

RFmxBTMXTxpConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the transmit power (TxP) measurements.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxBTMXTxpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXTxpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXTxpAveragingEnabledUpon return, contains whether to enable averaging for the transmit power (TxP) measurements.

###### Return Value

Int32

##### Remarks

TxpAveragingEnabled

False

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/bbc846de-ceed-0357-b6bf-f27021e443fb.htm language=enus -->
## TOPIC 00100: rfmxbtdotnet/html/bbc846de-ceed-0357-b6bf-f27021e443fb.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/bbc846de-ceed-0357-b6bf-f27021e443fb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/bbc846de-ceed-0357-b6bf-f27021e443fb.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccConfiguration.GetMeasurementEnabled Method

RFmxBTMXModAccConfigurationGetMeasurementEnabled Method

Gets whether to enable the ModAcc measurements. You can use this method to determine the modulation quality of the bluetooth transmitter.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanUpon return, contains whether to enable the ModAcc measurements. You can use this method to determine the modulation quality of the bluetooth transmitter.

###### Return Value

Int32

##### Remarks

ModAccMeasurementEnabled

##### See Also

###### Reference

RFmxBTMXModAccConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/f6845ef3-a39e-a9c9-e482-8bbe70eb0bc9.htm language=enus -->
## TOPIC 00101: rfmxbtdotnet/html/f6845ef3-a39e-a9c9-e482-8bbe70eb0bc9.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/f6845ef3-a39e-a9c9-e482-8bbe70eb0bc9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/f6845ef3-a39e-a9c9-e482-8bbe70eb0bc9.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXModAccResults.FetchDevm Method

RFmxBTMXModAccResultsFetchDevm Method

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDevm(
	string selectorString,
	double timeout,
	out double peakRmsDevmMaximum,
	out double peakDevmMaximum,
	out double ninetyninePercentDevm
)
```

```text
Public Function FetchDevm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef peakRmsDevmMaximum As Double,
	<OutAttribute> ByRef peakDevmMaximum As Double,
	<OutAttribute> ByRef ninetyninePercentDevm As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **peakRmsDevmMaximum**
  - Type: SystemDouble Upon return, contains the peak of the RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. When you set SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak RMS DEVM values computed for each averaging count. This value is expressed in percentage.
- **peakDevmMaximum**
  - Type: SystemDouble Upon return, contains the peak of the DEVM values computed on symbols in the EDR portion of the EDR packet. When you set the SetAveragingEnabled(String, RFmxBTMXModAccAveragingEnabled) method to True, it returns the maximum of the peak symbol DEVM values computed for each averaging count. This value is expressed in percentage.
- **ninetyninePercentDevm**
  - Type: SystemDouble Upon return, contains the 99th percentile of the DEVM values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed in percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxBTMXModAccResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/f6b2c343-92e2-493c-db02-c94091b5c484.htm language=enus -->
## TOPIC 00102: rfmxbtdotnet/html/f6b2c343-92e2-493c-db02-c94091b5c484.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/f6b2c343-92e2-493c-db02-c94091b5c484.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/f6b2c343-92e2-493c-db02-c94091b5c484.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration.SetAllTracesEnabled Method

RFmxBTMXTxpConfigurationSetAllTracesEnabled Method

Sets whether to enable all the traces used for transmit power (TxP) measurements.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanSpecifies whether to enable all the traces used for transmit power (TxP) measurements.

###### Return Value

Int32

##### Remarks

TxpAllTracesEnabled

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/f7074281-f9c3-6a5d-b2bb-ce62426b2e9a.htm language=enus -->
## TOPIC 00103: rfmxbtdotnet/html/f7074281-f9c3-6a5d-b2bb-ce62426b2e9a.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/f7074281-f9c3-6a5d-b2bb-ce62426b2e9a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/f7074281-f9c3-6a5d-b2bb-ce62426b2e9a.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXAcpResults.GetLowerOffsetAbsolutePower Method

RFmxBTMXAcpResultsGetLowerOffsetAbsolutePower Method

Gets the absolute power measured in the lower offset channel. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.BTMX

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

- **selectorString**
  - Type: SystemString Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the absolute power measured in the lower offset channel. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AcpResultsLowerOffsetAbsolutePower

##### See Also

###### Reference

RFmxBTMXAcpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/fd8b6cc4-c7e3-c700-d420-956782f0e904.htm language=enus -->
## TOPIC 00104: rfmxbtdotnet/html/fd8b6cc4-c7e3-c700-d420-956782f0e904.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/fd8b6cc4-c7e3-c700-d420-956782f0e904.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/fd8b6cc4-c7e3-c700-d420-956782f0e904.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMX.GetDirectionFindingMode Method

RFmxBTMXGetDirectionFindingMode Method

Gets the mode of direction finding.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDirectionFindingMode(
	string selectorString,
	out RFmxBTMXDirectionFindingMode value
)
```

```text
Public Function GetDirectionFindingMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXDirectionFindingMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXDirectionFindingModeUpon return, contains the mode of direction finding.

###### Return Value

Int32

##### Remarks

DirectionFindingMode

Disabled

##### See Also

###### Reference

RFmxBTMX Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm language=enus -->
## TOPIC 00105: rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/fead4cf1-e90e-23df-c721-4d260be902c2.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpConfiguration.GetBurstSynchronizationType Method

RFmxBTMXTxpConfigurationGetBurstSynchronizationType Method

Gets the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstSynchronizationType(
	string selectorString,
	out RFmxBTMXTxpBurstSynchronizationType value
)
```

```text
Public Function GetBurstSynchronizationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxBTMXTxpBurstSynchronizationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.BTMXRFmxBTMXTxpBurstSynchronizationTypeUpon return, contains the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

###### Return Value

Int32

##### Remarks

TxpBurstSynchronizationType

Preamble

##### See Also

###### Reference

RFmxBTMXTxpConfiguration Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dotnet path=rfmxbtdotnet/html/ffef4dfc-1059-7ce1-34b5-d57381bc6b04.htm language=enus -->
## TOPIC 00106: rfmxbtdotnet/html/ffef4dfc-1059-7ce1-34b5-d57381bc6b04.htm

- bundle_id: `rfmx-for-bluetooth-test-dotnet`
- source_path: `rfmxbtdotnet/html/ffef4dfc-1059-7ce1-34b5-d57381bc6b04.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dotnet/raw/resource/enus/rfmxbtdotnet/html/ffef4dfc-1059-7ce1-34b5-d57381bc6b04.htm
- document_id: `rfmx-for-bluetooth-test-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxBTMXTxpResults.GetLECteTransmitSlotAveragePowerMean Method

RFmxBTMXTxpResultsGetLECteTransmitSlotAveragePowerMean Method

SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode)

AngleOfDepature

Namespace:

NationalInstruments.RFmx.BTMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLECteTransmitSlotAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetLECteTransmitSlotAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the SetDirectionFindingMode(String, RFmxBTMXDirectionFindingMode) method to AngleOfDepature. When you set the TXP Averaging Enabled method to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

TxpResultsLECteTransmitSlotAveragePowerMean

##### See Also

###### Reference

RFmxBTMXTxpResults Class

NationalInstruments.RFmx.BTMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
