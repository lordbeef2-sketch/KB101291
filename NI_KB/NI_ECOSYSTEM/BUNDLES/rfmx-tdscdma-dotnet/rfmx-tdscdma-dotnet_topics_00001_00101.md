# NI DOCUMENT BUNDLE: rfmx-tdscdma-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-tdscdma-dotnet start=1 end=101 -->
<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/0149fa51-6473-73ac-d1ef-825a78a29a9b.htm language=enus -->
## TOPIC 00001: rfmxtdscdmadotnet/html/0149fa51-6473-73ac-d1ef-825a78a29a9b.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/0149fa51-6473-73ac-d1ef-825a78a29a9b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/0149fa51-6473-73ac-d1ef-825a78a29a9b.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtResults.GetSegmentMargin Method

RFmxTdscdmaMXPvtResultsGetSegmentMargin Method

Gets the power margin for an individual power versus time (PVT) measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentMargin(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentMargin ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Segment number. Example: "Segment0", "result::r1/Segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power margin for an individual power versus time (PVT) measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PvtResultsSegmentMargin

##### See Also

###### Reference

RFmxTdscdmaMXPvtResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/029e1a8d-dfa7-71f2-084f-68909afd7424.htm language=enus -->
## TOPIC 00002: rfmxtdscdmadotnet/html/029e1a8d-dfa7-71f2-084f-68909afd7424.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/029e1a8d-dfa7-71f2-084f-68909afd7424.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/029e1a8d-dfa7-71f2-084f-68909afd7424.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.SetIQGainImbalanceRemovalEnabled Method

RFmxTdscdmaMXCdaConfigurationSetIQGainImbalanceRemovalEnabled Method

Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQGainImbalanceRemovalEnabled(
	string selectorString,
	RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled value
)
```

```text
Public Function SetIQGainImbalanceRemovalEnabled ( 
	selectorString As String,
	value As RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabledSpecifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

###### Return Value

Int32

##### Remarks

CdaIQGainImbalanceRemovalEnabled

False

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/07429b1e-36f6-a808-b97b-e3603a164d59.htm language=enus -->
## TOPIC 00003: rfmxtdscdmadotnet/html/07429b1e-36f6-a808-b97b-e3603a164d59.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/07429b1e-36f6-a808-b97b-e3603a164d59.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/07429b1e-36f6-a808-b97b-e3603a164d59.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetPeakDataEvm Method

RFmxTdscdmaMXModAccResultsGetPeakDataEvm Method

Gets the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakDataEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakDataEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakDataEvm

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/0bda3a15-3b0a-6522-047f-f02530ea5424.htm language=enus -->
## TOPIC 00004: rfmxtdscdmadotnet/html/0bda3a15-3b0a-6522-047f-f02530ea5424.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/0bda3a15-3b0a-6522-047f-f02530ea5424.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/0bda3a15-3b0a-6522-047f-f02530ea5424.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSlotPowerConfiguration.SetMeasurementLength Method

RFmxTdscdmaMXSlotPowerConfigurationSetMeasurementLength Method

NI recommends you set a measurement length as a multiple of the number of slots per subframe, that is a multiple of 7. For example, when you set this property to 28 slots, the SlotPower measurement would report results for the 4 active time slots within the specified measurement length. In this example, 28 slots = 4 subframes.

The start of the measurement is determined by the RFmxTdscdmaMX.SetTriggerType method. Although all the values of the Trigger Type property are supported for this measurement, it is recommended to set the RFmxTdscdmaMX.SetTriggerType method to DigitalEdge with the following options:

- Digital trigger at the start of active slot, with the RFmxTdscdmaMX.SetTriggerDelay method set to 0 seconds.
- Digital trigger at the start of the subframe, with the RFmxTdscdmaMX.SetTriggerDelay method configured to a value which is equal to the time offset of the active time slot from the start of the subrame

If you set the active slot value to TS0, the trigger delay is 0 microseconds.

If you set the active slot value to TS1, the trigger delay is 950 microseconds.

If you set the active slot value to TS2, the trigger delay is 1625 microseconds.

If you set the active slot value to TS3, the trigger delay is 2300 microseconds.

If you set the active slot value to TS4, the trigger delay is 2975 microseconds.

If you set the active slot value to TS5, the trigger delay is 3650 microseconds.

If you set the active slot value to TS6, the trigger delay is 4325 microseconds.

If you cannot provide a digital trigger, you can set RFmxTdscdmaMX.SetTriggerType method to IQPowerEdge to ensure that the measurement starts at the start of an active time slot. To ensure this trigger works properly, NI recommends you complete the following steps:

- Set the RFmxTdscdmaMX.SetIQPowerEdgeTriggerLevel method to allow triggering for any of the power levels in the active slots
- Run the RFmx measurement just before generating your signal

If you set the RFmxTdscdmaMX.SetTriggerType method to None, the measurement will automatically detect the start of the first burst and measure the traffic slot in that position in every subframe.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementLength(
	string selectorString,
	int value
)
```

```text
Public Function SetMeasurementLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal.

###### Return Value

Int32

##### Remarks

SlotPowerMeasurementLength

##### See Also

###### Reference

RFmxTdscdmaMXSlotPowerConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/0c42e1c2-4e1a-a882-fe2e-0b8f33b2b3ab.htm language=enus -->
## TOPIC 00005: rfmxtdscdmadotnet/html/0c42e1c2-4e1a-a882-fe2e-0b8f33b2b3ab.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/0c42e1c2-4e1a-a882-fe2e-0b8f33b2b3ab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/0c42e1c2-4e1a-a882-fe2e-0b8f33b2b3ab.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtConfiguration.GetMeasurementMethod Method

RFmxTdscdmaMXPvtConfigurationGetMeasurementMethod Method

Gets the method for performing the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementMethod(
	string selectorString,
	out RFmxTdscdmaMXPvtMeasurementMethod value
)
```

```text
Public Function GetMeasurementMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXPvtMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXPvtMeasurementMethodUpon return, contains the method for performing the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtMeasurementMethod

##### See Also

###### Reference

RFmxTdscdmaMXPvtConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/0c8d90cc-75e7-686b-f53d-1dfdead32749.htm language=enus -->
## TOPIC 00006: rfmxtdscdmadotnet/html/0c8d90cc-75e7-686b-f53d-1dfdead32749.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/0c8d90cc-75e7-686b-f53d-1dfdead32749.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/0c8d90cc-75e7-686b-f53d-1dfdead32749.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaSpectrumInverted Enumeration

RFmxTdscdmaMXCdaSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXCdaSpectrumInverted
```

```text
Public Enumeration RFmxTdscdmaMXCdaSpectrumInverted
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The spectrum is not inverted. |
|  | True | 1 | The spectrum is inverted. |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/0f9341c6-2079-0303-efd1-56d54830481e.htm language=enus -->
## TOPIC 00007: rfmxtdscdmadotnet/html/0f9341c6-2079-0303-efd1-56d54830481e.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/0f9341c6-2079-0303-efd1-56d54830481e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/0f9341c6-2079-0303-efd1-56d54830481e.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetTriggerDelay Method

RFmxTdscdmaMXGetTriggerDelay Method

Gets the trigger delay time. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemDoubleUpon return, contains the trigger delay time. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TriggerDelay

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/0fc3e197-85a2-e137-11e0-abbf5f6c8097.htm language=enus -->
## TOPIC 00008: rfmxtdscdmadotnet/html/0fc3e197-85a2-e137-11e0-abbf5f6c8097.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/0fc3e197-85a2-e137-11e0-abbf5f6c8097.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/0fc3e197-85a2-e137-11e0-abbf5f6c8097.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetTriggerType Method

RFmxTdscdmaMXGetTriggerType Method

Gets the trigger type.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerType(
	string selectorString,
	out RFmxTdscdmaMXTriggerType value
)
```

```text
Public Function GetTriggerType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXTriggerType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXTriggerTypeUpon return, contains the trigger type.

###### Return Value

Int32

##### Remarks

TriggerType

IQPowerEdge

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/10289a69-a23a-074e-896f-663915096447.htm language=enus -->
## TOPIC 00009: rfmxtdscdmadotnet/html/10289a69-a23a-074e-896f-663915096447.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/10289a69-a23a-074e-896f-663915096447.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/10289a69-a23a-074e-896f-663915096447.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.SetMeasurementChannelSpreadingFactor Method

RFmxTdscdmaMXCdaConfigurationSetMeasurementChannelSpreadingFactor Method

Sets the spreading factor of the channel on which to perform the code domain analysis (CDA) measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementChannelSpreadingFactor(
	string selectorString,
	int value
)
```

```text
Public Function SetMeasurementChannelSpreadingFactor ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the spreading factor of the channel on which to perform the code domain analysis (CDA) measurement.

###### Return Value

Int32

##### Remarks

CdaMeasurementChannelSpreadingFactor

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/10b673d3-ea24-b2f5-558f-7acd35565160.htm language=enus -->
## TOPIC 00010: rfmxtdscdmadotnet/html/10b673d3-ea24-b2f5-558f-7acd35565160.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/10b673d3-ea24-b2f5-558f-7acd35565160.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/10b673d3-ea24-b2f5-558f-7acd35565160.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtResults.FetchSegmentMeasurementArray Method

RFmxTdscdmaMXPvtResultsFetchSegmentMeasurementArray Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSegmentMeasurementArray(
	string selectorString,
	double timeout,
	ref RFmxTdscdmaMXPvtSegmentStatus[] segmentStatus,
	ref double[] segmentMargin,
	ref double[] segmentMarginTime,
	ref double[] segmentMeanAbsolutePower,
	ref double[] segmentMaximumAbsolutePower,
	ref double[] segmentMinimumAbsolutePower
)
```

```text
Public Function FetchSegmentMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef segmentStatus As RFmxTdscdmaMXPvtSegmentStatus(),
	ByRef segmentMargin As Double(),
	ByRef segmentMarginTime As Double(),
	ByRef segmentMeanAbsolutePower As Double(),
	ByRef segmentMaximumAbsolutePower As Double(),
	ByRef segmentMinimumAbsolutePower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **segmentStatus**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXPvtSegmentStatus Upon return, contains an array of the measurement status values for an individual PVT measurement segment.
- **segmentMargin**
  - Type: SystemDouble Upon return, contains an array of the power margins for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB.
- **segmentMarginTime**
  - Type: SystemDouble Upon return, contains an array of the positions in time corresponding to the segmentMargin parameter. This value is expressed in seconds.
- **segmentMeanAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of the mean measured powers corresponding to the segmentMargin parameter. This value is expressed in dBm.
- **segmentMaximumAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of the maximum measured powers of an individual PVT measurement segment. This value is expressed in dBm.
- **segmentMinimumAbsolutePower**
  - Type: SystemDouble Upon return, contains an array of the minimum measured powers of an individual PVT measurement segment. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXPvtResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/10de8bc7-a06b-ef86-3bc5-ab2b70c6444a.htm language=enus -->
## TOPIC 00011: rfmxtdscdmadotnet/html/10de8bc7-a06b-ef86-3bc5-ab2b70c6444a.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/10de8bc7-a06b-ef86-3bc5-ab2b70c6444a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/10de8bc7-a06b-ef86-3bc5-ab2b70c6444a.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.SetTriggerMinimumQuietTimeDuration Method

RFmxTdscdmaMXSetTriggerMinimumQuietTimeDuration Method

SetIQPowerEdgeTriggerSlope(String, RFmxTdscdmaMXIQPowerEdgeTriggerSlope)

Rising

Falling

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerMinimumQuietTimeDuration(
	string selectorString,
	double value
)
```

```text
Public Function SetTriggerMinimumQuietTimeDuration ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level.

###### Return Value

Int32

##### Remarks

TriggerMinimumQuietTimeDuration

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/13248d42-b1ca-09f6-637b-f3366aa03167.htm language=enus -->
## TOPIC 00012: rfmxtdscdmadotnet/html/13248d42-b1ca-09f6-637b-f3366aa03167.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/13248d42-b1ca-09f6-637b-f3366aa03167.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/13248d42-b1ca-09f6-637b-f3366aa03167.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetIQOriginOffset Method

RFmxTdscdmaMXModAccResultsGetIQOriginOffset Method

Gets the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQOriginOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetIQOriginOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsIQOriginOffset

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/141a7307-9c42-333d-9fad-d0647703b78d.htm language=enus -->
## TOPIC 00013: rfmxtdscdmadotnet/html/141a7307-9c42-333d-9fad-d0647703b78d.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/141a7307-9c42-333d-9fad-d0647703b78d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/141a7307-9c42-333d-9fad-d0647703b78d.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.ConfigureAveraging Method

RFmxTdscdmaMXCdaConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxTdscdmaMXCdaAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxTdscdmaMXCdaAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXCdaAveragingEnabledSpecifies whether to enable averaging for the CDA measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/179d5380-d870-7497-f534-b090dc0e8776.htm language=enus -->
## TOPIC 00014: rfmxtdscdmadotnet/html/179d5380-d870-7497-f534-b090dc0e8776.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/179d5380-d870-7497-f534-b090dc0e8776.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/179d5380-d870-7497-f534-b090dc0e8776.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.IsDisposed Property

RFmxTdscdmaMXIsDisposed Property

Gets a value that indicates whether the signal has been disposed.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public bool IsDisposed { get; }
```

```text
Public ReadOnly Property IsDisposed As Boolean
	Get
```

###### Property Value

Boolean

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/17c2a925-1b70-f950-0915-aabe51ffef12.htm language=enus -->
## TOPIC 00015: rfmxtdscdmadotnet/html/17c2a925-1b70-f950-0915-aabe51ffef12.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/17c2a925-1b70-f950-0915-aabe51ffef12.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/17c2a925-1b70-f950-0915-aabe51ffef12.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXObwConfiguration.GetSpan Method

RFmxTdscdmaMXObwConfigurationGetSpan Method

Gets the frequency span of the OBW measurement. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpan(
	string selectorString,
	out double value
)
```

```text
Public Function GetSpan ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the frequency span of the OBW measurement. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ObwSpan

##### See Also

###### Reference

RFmxTdscdmaMXObwConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/17d17a25-7544-6ac9-c17d-34c26ec5e82e.htm language=enus -->
## TOPIC 00016: rfmxtdscdmadotnet/html/17d17a25-7544-6ac9-c17d-34c26ec5e82e.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/17d17a25-7544-6ac9-c17d-34c26ec5e82e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/17d17a25-7544-6ac9-c17d-34c26ec5e82e.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaResults.FetchCodeDomainPower Method

RFmxTdscdmaMXCdaResultsFetchCodeDomainPower Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCodeDomainPower(
	string selectorString,
	double timeout,
	out double meanTotalPower,
	out double meanTotalActivePower,
	out double meanActivePower,
	out double maximumPeakActivePower,
	out double meanInactivePower,
	out double maximumPeakInactivePower
)
```

```text
Public Function FetchCodeDomainPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanTotalPower As Double,
	<OutAttribute> ByRef meanTotalActivePower As Double,
	<OutAttribute> ByRef meanActivePower As Double,
	<OutAttribute> ByRef maximumPeakActivePower As Double,
	<OutAttribute> ByRef meanInactivePower As Double,
	<OutAttribute> ByRef maximumPeakInactivePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanTotalPower**
  - Type: SystemDouble Upon return, contains the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm.
- **meanTotalActivePower**
  - Type: SystemDouble Upon return, contains the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the SetPowerUnit(String, RFmxTdscdmaMXCdaPowerUnit) method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.
- **meanActivePower**
  - Type: SystemDouble Upon return, contains the average of the active code power measured in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.
- **maximumPeakActivePower**
  - Type: SystemDouble Upon return, contains the maximum value among all averaging iterations of the maximum active code power measured in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.
- **meanInactivePower**
  - Type: SystemDouble Upon return, contains the average of the code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.
- **maximumPeakInactivePower**
  - Type: SystemDouble Upon return, contains the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXCdaResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/17dfd10c-3ce3-fb10-6ad4-0242e2bbf375.htm language=enus -->
## TOPIC 00017: rfmxtdscdmadotnet/html/17dfd10c-3ce3-fb10-6ad4-0242e2bbf375.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/17dfd10c-3ce3-fb10-6ad4-0242e2bbf375.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/17dfd10c-3ce3-fb10-6ad4-0242e2bbf375.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpResults.FetchAbsolutePowersTrace Method

RFmxTdscdmaMXAcpResultsFetchAbsolutePowersTrace Method

Fetches the absolute powers trace for ACP measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchAbsolutePowersTrace(
	string selectorString,
	double timeout,
	int traceIndex,
	ref Spectrum<float> absolutePowersTrace
)
```

```text
Public Function FetchAbsolutePowersTrace ( 
	selectorString As String,
	timeout As Double,
	traceIndex As Integer,
	ByRef absolutePowersTrace As Spectrum(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **traceIndex**
  - Type: SystemInt32 Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets).
- **absolutePowersTrace**
  - Type: NationalInstrumentsSpectrumSingle Returns the trace of measured integrated power specified by the traceIndex parameter. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXAcpResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1803a03e-5da6-a30b-78a0-85ff322ce2ec.htm language=enus -->
## TOPIC 00018: rfmxtdscdmadotnet/html/1803a03e-5da6-a30b-78a0-85ff322ce2ec.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1803a03e-5da6-a30b-78a0-85ff322ce2ec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1803a03e-5da6-a30b-78a0-85ff322ce2ec.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaResults.GetMeanInactivePower Method

RFmxTdscdmaMXCdaResultsGetMeanInactivePower Method

SetPowerUnit(String, RFmxTdscdmaMXCdaPowerUnit)

dB

dBm

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanInactivePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanInactivePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the average code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the SetPowerUnit(String, RFmxTdscdmaMXCdaPowerUnit) method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.

###### Return Value

Int32

##### Remarks

CdaResultsMeanInactivePower

##### See Also

###### Reference

RFmxTdscdmaMXCdaResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/18162dca-f2c6-43f8-2095-45ec2b3304b1.htm language=enus -->
## TOPIC 00019: rfmxtdscdmadotnet/html/18162dca-f2c6-43f8-2095-45ec2b3304b1.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/18162dca-f2c6-43f8-2095-45ec2b3304b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/18162dca-f2c6-43f8-2095-45ec2b3304b1.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemResults.FetchLowerOffsetPower Method

RFmxTdscdmaMXSemResultsFetchLowerOffsetPower Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absoluteIntegratedPower**
  - Type: SystemDouble Upon return, contains the lower (negative) offset segment power measured. This value is expressed in dBm.
- **relativeIntegratedPower**
  - Type: SystemDouble Upon return, contains the power in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.
- **absolutePeakPower**
  - Type: SystemDouble Upon return, contains the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.
- **peakFrequency**
  - Type: SystemDouble Upon return, contains the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz.
- **relativePeakPower**
  - Type: SystemDouble Upon return, contains the peak power in the lower (negative) offset segment relative to the integrated power of the reference carrier.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXSemResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/18ac681d-6856-011e-da3e-a9bd1d114bfd.htm language=enus -->
## TOPIC 00020: rfmxtdscdmadotnet/html/18ac681d-6856-011e-da3e-a9bd1d114bfd.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/18ac681d-6856-011e-da3e-a9bd1d114bfd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/18ac681d-6856-011e-da3e-a9bd1d114bfd.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemResults.FetchMeasurementStatus Method

RFmxTdscdmaMXSemResultsFetchMeasurementStatus Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeasurementStatus(
	string selectorString,
	double timeout,
	out RFmxTdscdmaMXSemMeasurementStatus measurementStatus
)
```

```text
Public Function FetchMeasurementStatus ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef measurementStatus As RFmxTdscdmaMXSemMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXSemMeasurementStatus Upon return, contains the status of the measurement based on measurement limits and the failure criteria specified by the standard.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXSemResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/18b5b2c0-beb7-a726-4a06-20c213bfc7e3.htm language=enus -->
## TOPIC 00021: rfmxtdscdmadotnet/html/18b5b2c0-beb7-a726-4a06-20c213bfc7e3.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/18b5b2c0-beb7-a726-4a06-20c213bfc7e3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/18b5b2c0-beb7-a726-4a06-20c213bfc7e3.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.FetchPhaseErrorTrace Method

RFmxTdscdmaMXModAccResultsFetchPhaseErrorTrace Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **phaseError**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the data for a complex waveform including the start, delta, and actual values.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1a02dd3c-ffc9-7e40-ba0d-e843468f42eb.htm language=enus -->
## TOPIC 00022: rfmxtdscdmadotnet/html/1a02dd3c-ffc9-7e40-ba0d-e843468f42eb.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1a02dd3c-ffc9-7e40-ba0d-e843468f42eb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1a02dd3c-ffc9-7e40-ba0d-e843468f42eb.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.SetAttributeString Method

RFmxTdscdmaMXSetAttributeString Method

Sets the value of a String attribute.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeString(
	string selectorString,
	int attributeIdentifier,
	string value
)
```

```text
Public Function SetAttributeString ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx TDSCDMA Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemStringSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1a09d63d-4717-30d6-8911-6fa8a5bb94c0.htm language=enus -->
## TOPIC 00023: rfmxtdscdmadotnet/html/1a09d63d-4717-30d6-8911-6fa8a5bb94c0.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1a09d63d-4717-30d6-8911-6fa8a5bb94c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1a09d63d-4717-30d6-8911-6fa8a5bb94c0.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetPeakDataActiveCdeSpreadingFactor Method

RFmxTdscdmaMXModAccResultsGetPeakDataActiveCdeSpreadingFactor Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakDataActiveCdeSpreadingFactor(
	string selectorString,
	out int value
)
```

```text
Public Function GetPeakDataActiveCdeSpreadingFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemInt32 Upon return, contains the spreading factor used to retrieve the peak code domain error (CDE) of the active physical channel corresponding to the measured value of the GetMaximumPeakDataActiveCde(String, Double) method.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakDataActiveCdeSpreadingFactor

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1aa18dba-7446-bb7e-7dba-3b52b0ac809b.htm language=enus -->
## TOPIC 00024: rfmxtdscdmadotnet/html/1aa18dba-7446-bb7e-7dba-3b52b0ac809b.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1aa18dba-7446-bb7e-7dba-3b52b0ac809b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1aa18dba-7446-bb7e-7dba-3b52b0ac809b.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetPeakPilotEvm Method

RFmxTdscdmaMXModAccResultsGetPeakPilotEvm Method

Gets the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPeakPilotEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetPeakPilotEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsPeakPilotEvm

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1b393f95-d152-7700-4f7d-731248f472a5.htm language=enus -->
## TOPIC 00025: rfmxtdscdmadotnet/html/1b393f95-d152-7700-4f7d-731248f472a5.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1b393f95-d152-7700-4f7d-731248f472a5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1b393f95-d152-7700-4f7d-731248f472a5.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.TdscdmaMX Namespace

NationalInstruments.RFmx.TdscdmaMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxTdscdmaMX | Defines a root class which is used to identify and control TDSCDMA signal configuration. |
|  | RFmxTdscdmaMXAcp | Represents the ACP measurement. |
|  | RFmxTdscdmaMXAcpConfiguration | Provides methods to configure the ACP measurement |
|  | RFmxTdscdmaMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
|  | RFmxTdscdmaMXCda | Represents the CDA measurement. |
|  | RFmxTdscdmaMXCdaConfiguration | Provides methods to configure the CDA measurement |
|  | RFmxTdscdmaMXCdaResults | Provides methods to fetch and read the CDA measurement results. |
|  | RFmxTdscdmaMXChp | Represents the CHP measurement. |
|  | RFmxTdscdmaMXChpConfiguration | Provides methods to configure the CHP measurement |
|  | RFmxTdscdmaMXChpResults | Provides methods to fetch and read the CHP measurement results. |
|  | RFmxTdscdmaMXConstants | Specifies constants for I/O terminals. |
|  | RFmxTdscdmaMXModAcc | Represents the ModAcc measurement. |
|  | RFmxTdscdmaMXModAccConfiguration | Provides methods to configure the ModAcc measurement |
|  | RFmxTdscdmaMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
|  | RFmxTdscdmaMXObw | Represents the OBW measurement. |
|  | RFmxTdscdmaMXObwConfiguration | Provides methods to configure the OBW measurement |
|  | RFmxTdscdmaMXObwResults | Provides methods to fetch and read the OBW measurement results. |
|  | RFmxTdscdmaMXPvt | Represents the PVT measurement. |
|  | RFmxTdscdmaMXPvtConfiguration | Provides methods to configure the PVT measurement |
|  | RFmxTdscdmaMXPvtResults | Provides methods to fetch and read the PVT measurement results. |
|  | RFmxTdscdmaMXSem | Represents the SEM measurement. |
|  | RFmxTdscdmaMXSemConfiguration | Provides methods to configure the SEM measurement |
|  | RFmxTdscdmaMXSemResults | Provides methods to fetch and read the SEM measurement results. |
|  | RFmxTdscdmaMXSlotPower | Represents the SlotPower measurement. |
|  | RFmxTdscdmaMXSlotPowerConfiguration | Provides methods to configure the SlotPower measurement |
|  | RFmxTdscdmaMXSlotPowerResults | Provides methods to fetch and read the SlotPower measurement results. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | RFmxTdscdmaMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
|  | RFmxTdscdmaMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
|  | RFmxTdscdmaMXAcpFftOverlapMode | Specifies how overlapping is applied when computing the FFT of the acquired samples. The default value is Disabled. |
|  | RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is used only if you set the SetMeasurementMethod(String, RFmxTdscdmaMXAcpMeasurementMethod) method to DynamicRange. |
|  | RFmxTdscdmaMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |
|  | RFmxTdscdmaMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. |
|  | RFmxTdscdmaMXAcpRbwAutoBandwidth | Specifies whether the measurement calculates the RBW. |
|  | RFmxTdscdmaMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |
|  | RFmxTdscdmaMXAcpSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |
|  | RFmxTdscdmaMXCdaAveragingEnabled | Specifies whether to enable averaging for the code domain analysis (CDA) measurement. |
|  | RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
|  | RFmxTdscdmaMXCdaIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the code domain analysis (CDA) measurement. |
|  | RFmxTdscdmaMXCdaIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
|  | RFmxTdscdmaMXCdaPowerUnit | Specifies the measurement unit of the code domain power (CDP) results. |
|  | RFmxTdscdmaMXCdaRrcFilterEnabled | Specifies whether to enable the RRC filter. |
|  | RFmxTdscdmaMXCdaSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxTdscdmaMXCdaSynchronizationMode | Specifies the synchronization mode for the code domain analysis (CDA) measurement. Currently, only the Slot mode is supported. |
|  | RFmxTdscdmaMXChannelConfigurationMode | Specifies whether to detect the channels automatically or to use a specified channel configuration. |
|  | RFmxTdscdmaMXChannelType | Specifies the channel type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | RFmxTdscdmaMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |
|  | RFmxTdscdmaMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
|  | RFmxTdscdmaMXChpRbwAutoBandwidth | Specifies whether the measurement calculates the RBW. |
|  | RFmxTdscdmaMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |
|  | RFmxTdscdmaMXChpSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |
|  | RFmxTdscdmaMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
|  | RFmxTdscdmaMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | RFmxTdscdmaMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when the signal power is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | RFmxTdscdmaMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | RFmxTdscdmaMXMeasurementTypes | Specifies the type of measurement. |
|  | RFmxTdscdmaMXMidambleAutoDetectionMode | Specifies the midamble auto detection mode. |
|  | RFmxTdscdmaMXModAccAveragingEnabled | Specifies whether to enable averaging for the ModAcc measurement. |
|  | RFmxTdscdmaMXModAccDetectedModulationType | Returns the modulation type of the selected channel within the set of active channels. If the averaging is enabled, this method refers to the last averaging iteration. Use "channel(n)" as the selector string to read this result. |
|  | RFmxTdscdmaMXModAccIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement. |
|  | RFmxTdscdmaMXModAccIQOffsetRemovalEnabled | Specifies whether to remove the I/Q offset before the EVM measurement. |
|  | RFmxTdscdmaMXModAccIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. |
|  | RFmxTdscdmaMXModAccRrcFilterEnabled | Specifies whether to enable the RRC filter in the ModAcc measurement. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | RFmxTdscdmaMXModAccSlotType | Specifies the type of the time slot for the ModAcc measurement. |
|  | RFmxTdscdmaMXModAccSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxTdscdmaMXModAccSynchronizationMode | Specifies the synchronization mode for the ModAcc measurement. |
|  | RFmxTdscdmaMXModulationType | Specifies the modulation type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | RFmxTdscdmaMXObwAveragingEnabled | Specifies whether to enable averaging for the OBW measurement. |
|  | RFmxTdscdmaMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
|  | RFmxTdscdmaMXObwRbwAutoBandwidth | Specifies whether the measurement calculates the RBW. |
|  | RFmxTdscdmaMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |
|  | RFmxTdscdmaMXObwSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |
|  | RFmxTdscdmaMXPropertyId | Specifies all the attribute identifiers. |
|  | RFmxTdscdmaMXPvtAveragingEnabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. |
|  | RFmxTdscdmaMXPvtAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement. |
|  | RFmxTdscdmaMXPvtMeasurementMethod | Specifies the method for performing the power versus time (PVT) measurement. |
|  | RFmxTdscdmaMXPvtMeasurementStatus | Returns the overall status of the power versus time (PVT) measurement. |
|  | RFmxTdscdmaMXPvtRRCFilterEnabled | Specifies whether to enable the RRC filter. Use this method to disable the filter if the received signal is already RRC-filtered. |
|  | RFmxTdscdmaMXPvtSegmentStatus | Returns the measurement status for an individual power versus time (PVT) measurement segment. |
|  | RFmxTdscdmaMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |
|  | RFmxTdscdmaMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
|  | RFmxTdscdmaMXSemLowerOffsetMeasurementStatus | Indicates the lower offset segment measurement status based on the measurement limits specified by the standard. Use "offset(n)" as the selector string to read this result. |
|  | RFmxTdscdmaMXSemMeasurementStatus | Indicates the overall measurement status based on the measurement limits specified by the standard for each offset segment. |
|  | RFmxTdscdmaMXSemOffsetRbwFilterType | Returns the the type of RBW filter used to sweep the offset segment. |
|  | RFmxTdscdmaMXSemSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |
|  | RFmxTdscdmaMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status based on measurement limits specified by the standard. Use "offset(n)" as the selector string to read this result. |
|  | RFmxTdscdmaMXSlotPowerRrcFilterEnabled | Specifies whether the RRC filter should be enabled or not. |
|  | RFmxTdscdmaMXSlotPowerSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |
|  | RFmxTdscdmaMXTriggerMinimumQuietTimeMode | Specifies whether the measurement calculates the minimum quiet time used for triggering. |
|  | RFmxTdscdmaMXTriggerType | Specifies the trigger type. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1bae38dc-7f5b-6271-1892-f729e45bc000.htm language=enus -->
## TOPIC 00026: rfmxtdscdmadotnet/html/1bae38dc-7f5b-6271-1892-f729e45bc000.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1bae38dc-7f5b-6271-1892-f729e45bc000.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1bae38dc-7f5b-6271-1892-f729e45bc000.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSlotPower.Configuration Property

RFmxTdscdmaMXSlotPowerConfiguration Property

RFmxTdscdmaMXSlotPowerConfiguration

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxTdscdmaMXSlotPowerConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxTdscdmaMXSlotPowerConfiguration
	Get
```

###### Property Value

RFmxTdscdmaMXSlotPowerConfiguration

##### See Also

###### Reference

RFmxTdscdmaMXSlotPower Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1c44cb4f-dde9-5d25-bce2-975c7dc28dda.htm language=enus -->
## TOPIC 00027: rfmxtdscdmadotnet/html/1c44cb4f-dde9-5d25-bce2-975c7dc28dda.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1c44cb4f-dde9-5d25-bce2-975c7dc28dda.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1c44cb4f-dde9-5d25-bce2-975c7dc28dda.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCda.Results Property

RFmxTdscdmaMXCdaResults Property

RFmxTdscdmaMXCdaResults

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxTdscdmaMXCdaResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxTdscdmaMXCdaResults
	Get
```

###### Property Value

RFmxTdscdmaMXCdaResults

##### See Also

###### Reference

RFmxTdscdmaMXCda Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1cf1b6b1-48d8-0733-404a-5034e082cb77.htm language=enus -->
## TOPIC 00028: rfmxtdscdmadotnet/html/1cf1b6b1-48d8-0733-404a-5034e082cb77.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1cf1b6b1-48d8-0733-404a-5034e082cb77.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1cf1b6b1-48d8-0733-404a-5034e082cb77.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtConfiguration.ConfigureMeasurementMethod Method

RFmxTdscdmaMXPvtConfigurationConfigureMeasurementMethod Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementMethod(
	string selectorString,
	RFmxTdscdmaMXPvtMeasurementMethod measurementMethod
)
```

```text
Public Function ConfigureMeasurementMethod ( 
	selectorString As String,
	measurementMethod As RFmxTdscdmaMXPvtMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementMethod**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXPvtMeasurementMethodSpecifies the method used for performing the PVT measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXPvtConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1d5cde2d-bca5-f790-d2bc-61313fdb9c97.htm language=enus -->
## TOPIC 00029: rfmxtdscdmadotnet/html/1d5cde2d-bca5-f790-d2bc-61313fdb9c97.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1d5cde2d-bca5-f790-d2bc-61313fdb9c97.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1d5cde2d-bca5-f790-d2bc-61313fdb9c97.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.SetMeasurementOffset Method

RFmxTdscdmaMXCdaConfigurationSetMeasurementOffset Method

SetSynchronizationMode(String, RFmxTdscdmaMXCdaSynchronizationMode)

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementOffset(
	string selectorString,
	int value
)
```

```text
Public Function SetMeasurementOffset ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxTdscdmaMXCdaSynchronizationMode) method.

###### Return Value

Int32

##### Remarks

CdaMeasurementOffset

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/1fc3944e-f9c5-64b6-1e99-a83176791f3a.htm language=enus -->
## TOPIC 00030: rfmxtdscdmadotnet/html/1fc3944e-f9c5-64b6-1e99-a83176791f3a.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/1fc3944e-f9c5-64b6-1e99-a83176791f3a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/1fc3944e-f9c5-64b6-1e99-a83176791f3a.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetRmsDataPhaseError Method

RFmxTdscdmaMXModAccResultsGetRmsDataPhaseError Method

Gets the RMS of the data phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsDataPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsDataPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS of the data phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

ModAccResultsRmsDataPhaseError

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/20745809-b5bd-1bf7-2ab8-0f97bfc64b15.htm language=enus -->
## TOPIC 00031: rfmxtdscdmadotnet/html/20745809-b5bd-1bf7-2ab8-0f97bfc64b15.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/20745809-b5bd-1bf7-2ab8-0f97bfc64b15.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/20745809-b5bd-1bf7-2ab8-0f97bfc64b15.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemConfiguration.GetSweepTimeAuto Method

RFmxTdscdmaMXSemConfigurationGetSweepTimeAuto Method

Gets whether the measurement calculates the sweep time.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxTdscdmaMXSemSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXSemSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXSemSweepTimeAutoUpon return, contains whether the measurement calculates the sweep time.

###### Return Value

Int32

##### Remarks

SemSweepTimeAuto

True

##### See Also

###### Reference

RFmxTdscdmaMXSemConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/2081a565-2220-882e-4949-dec6c83cc848.htm language=enus -->
## TOPIC 00032: rfmxtdscdmadotnet/html/2081a565-2220-882e-4949-dec6c83cc848.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/2081a565-2220-882e-4949-dec6c83cc848.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/2081a565-2220-882e-4949-dec6c83cc848.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXConstants.PxiTriggerLine7 Field

RFmxTdscdmaMXConstantsPxiTriggerLine7 Field

The signal is exported to the PXI trigger line 7.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine7 = "PXI_Trig7"
```

```text
Public Const PxiTriggerLine7 As String = "PXI_Trig7"
```

###### Field Value

String

##### See Also

###### Reference

RFmxTdscdmaMXConstants Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/2e2a6456-d4e2-b470-2d07-094e244d419b.htm language=enus -->
## TOPIC 00033: rfmxtdscdmadotnet/html/2e2a6456-d4e2-b470-2d07-094e244d419b.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/2e2a6456-d4e2-b470-2d07-094e244d419b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/2e2a6456-d4e2-b470-2d07-094e244d419b.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetDetectedModulationType Method

RFmxTdscdmaMXModAccResultsGetDetectedModulationType Method

"channel(n)"

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDetectedModulationType(
	string selectorString,
	out RFmxTdscdmaMXModAccDetectedModulationType value
)
```

```text
Public Function GetDetectedModulationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXModAccDetectedModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Channel number. Example: "Channel0", "result::r1/Channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXModAccDetectedModulationType Upon return, contains the modulation type of the selected channel within the set of active channels. If the averaging is enabled, this method refers to the last averaging iteration. Use "channel(n)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsDetectedModulationType

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/2e40555b-219a-1896-0cdd-bf9a328b74bb.htm language=enus -->
## TOPIC 00034: rfmxtdscdmadotnet/html/2e40555b-219a-1896-0cdd-bf9a328b74bb.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/2e40555b-219a-1896-0cdd-bf9a328b74bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/2e40555b-219a-1896-0cdd-bf9a328b74bb.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.GetMeasurementEnabled Method

RFmxTdscdmaMXAcpConfigurationGetMeasurementEnabled Method

Gets whether to enable the ACP measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/31b716ee-c3b1-b201-1eb6-b3adb66c6c41.htm language=enus -->
## TOPIC 00035: rfmxtdscdmadotnet/html/31b716ee-c3b1-b201-1eb6-b3adb66c6c41.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/31b716ee-c3b1-b201-1eb6-b3adb66c6c41.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/31b716ee-c3b1-b201-1eb6-b3adb66c6c41.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetRmsPilotPhaseError Method

RFmxTdscdmaMXModAccResultsGetRmsPilotPhaseError Method

Gets the RMS of the pilot phase error, averaged over all averaging iterations. This value is expressed in degrees.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRmsPilotPhaseError(
	string selectorString,
	out double value
)
```

```text
Public Function GetRmsPilotPhaseError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS of the pilot phase error, averaged over all averaging iterations. This value is expressed in degrees.

###### Return Value

Int32

##### Remarks

ModAccResultsRmsPilotPhaseError

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/31d69ab0-5612-b6eb-ce7c-be43bd529e45.htm language=enus -->
## TOPIC 00036: rfmxtdscdmadotnet/html/31d69ab0-5612-b6eb-ce7c-be43bd529e45.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/31d69ab0-5612-b6eb-ce7c-be43bd529e45.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/31d69ab0-5612-b6eb-ce7c-be43bd529e45.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXObwResults.FetchSpectrum Method

RFmxTdscdmaMXObwResultsFetchSpectrum Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **spectrum**
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the trace of power levels in the spectral domain. This value is expressed in dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXObwResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/32a4d6ce-d37b-4c61-9ee5-282d42573233.htm language=enus -->
## TOPIC 00037: rfmxtdscdmadotnet/html/32a4d6ce-d37b-4c61-9ee5-282d42573233.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/32a4d6ce-d37b-4c61-9ee5-282d42573233.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/32a4d6ce-d37b-4c61-9ee5-282d42573233.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtResults.GetMidambleCode Method

RFmxTdscdmaMXPvtResultsGetMidambleCode Method

Gets the midamble code used for slot synchronization.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMidambleCode(
	string selectorString,
	out int value
)
```

```text
Public Function GetMidambleCode ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemInt32Upon return, contains the midamble code used for slot synchronization.

###### Return Value

Int32

##### Remarks

PvtResultsMidambleCode

##### See Also

###### Reference

RFmxTdscdmaMXPvtResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/33c985f7-1771-349b-cb47-c333a361f8d1.htm language=enus -->
## TOPIC 00038: rfmxtdscdmadotnet/html/33c985f7-1771-349b-cb47-c333a361f8d1.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/33c985f7-1771-349b-cb47-c333a361f8d1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/33c985f7-1771-349b-cb47-c333a361f8d1.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.SetRrcFilterEnabled Method

RFmxTdscdmaMXCdaConfigurationSetRrcFilterEnabled Method

Sets whether to enable the RRC filter.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRrcFilterEnabled(
	string selectorString,
	RFmxTdscdmaMXCdaRrcFilterEnabled value
)
```

```text
Public Function SetRrcFilterEnabled ( 
	selectorString As String,
	value As RFmxTdscdmaMXCdaRrcFilterEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXCdaRrcFilterEnabledSpecifies whether to enable the RRC filter.

###### Return Value

Int32

##### Remarks

CdaRrcFilterEnabled

True

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/35b38802-f4aa-b257-960b-e2ef54e23eb8.htm language=enus -->
## TOPIC 00039: rfmxtdscdmadotnet/html/35b38802-f4aa-b257-960b-e2ef54e23eb8.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/35b38802-f4aa-b257-960b-e2ef54e23eb8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/35b38802-f4aa-b257-960b-e2ef54e23eb8.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.GetAveragingType Method

RFmxTdscdmaMXAcpConfigurationGetAveragingType Method

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingType(
	string selectorString,
	out RFmxTdscdmaMXAcpAveragingType value
)
```

```text
Public Function GetAveragingType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXAcpAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXAcpAveragingTypeUpon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

###### Return Value

Int32

##### Remarks

AcpAveragingType

Rms

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/36cf4fd5-7a24-fa59-66ff-3e600ee85fda.htm language=enus -->
## TOPIC 00040: rfmxtdscdmadotnet/html/36cf4fd5-7a24-fa59-66ff-3e600ee85fda.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/36cf4fd5-7a24-fa59-66ff-3e600ee85fda.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/36cf4fd5-7a24-fa59-66ff-3e600ee85fda.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemConfiguration.GetCarrierIntegrationBandwidth Method

RFmxTdscdmaMXSemConfigurationGetCarrierIntegrationBandwidth Method

Gets the SEM carrier integration bandwidth. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCarrierIntegrationBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetCarrierIntegrationBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the SEM carrier integration bandwidth. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemCarrierIntegrationBandwidth

##### See Also

###### Reference

RFmxTdscdmaMXSemConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/38eae344-a281-1d17-455d-921b4fc6a2ca.htm language=enus -->
## TOPIC 00041: rfmxtdscdmadotnet/html/38eae344-a281-1d17-455d-921b4fc6a2ca.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/38eae344-a281-1d17-455d-921b4fc6a2ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/38eae344-a281-1d17-455d-921b4fc6a2ca.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSem Class

RFmxTdscdmaMXSem Class

Represents the SEM measurement.

##### Inheritance Hierarchy

RFmxTdscdmaMXSubObject

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxTdscdmaMXSem : RFmxTdscdmaMXSubObject
```

```text
Public NotInheritable Class RFmxTdscdmaMXSem
	Inherits RFmxTdscdmaMXSubObject
```

The RFmxTdscdmaMXSem type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxTdscdmaMXSemConfiguration instance that provides methods to configure the SEM measurement |
|  | Results | Gets the RFmxTdscdmaMXSemResults instance that provides methods to fetch and read the SEM measurement results. |

Top

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

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/3a013db0-fe03-f96c-d786-fa5516fba946.htm language=enus -->
## TOPIC 00042: rfmxtdscdmadotnet/html/3a013db0-fe03-f96c-d786-fa5516fba946.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/3a013db0-fe03-f96c-d786-fa5516fba946.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/3a013db0-fe03-f96c-d786-fa5516fba946.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtResults.GetSegmentStatus Method

RFmxTdscdmaMXPvtResultsGetSegmentStatus Method

Gets the measurement status for an individual power versus time (PVT) measurement segment.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentStatus(
	string selectorString,
	out RFmxTdscdmaMXPvtSegmentStatus value
)
```

```text
Public Function GetSegmentStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXPvtSegmentStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Segment number. Example: "Segment0", "result::r1/Segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXPvtSegmentStatusUpon return, contains the measurement status for an individual power versus time (PVT) measurement segment.

###### Return Value

Int32

##### Remarks

PvtResultsSegmentStatus

##### See Also

###### Reference

RFmxTdscdmaMXPvtResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/3d7a9944-0935-d301-d7a7-a5cb9470daf0.htm language=enus -->
## TOPIC 00043: rfmxtdscdmadotnet/html/3d7a9944-0935-d301-d7a7-a5cb9470daf0.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/3d7a9944-0935-d301-d7a7-a5cb9470daf0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/3d7a9944-0935-d301-d7a7-a5cb9470daf0.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.FetchCodeDomainErrorTrace Method

RFmxTdscdmaMXModAccResultsFetchCodeDomainErrorTrace Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCodeDomainErrorTrace(
	string selectorString,
	double timeout,
	ref float[] codeDomainError
)
```

```text
Public Function FetchCodeDomainErrorTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef codeDomainError As Single()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **codeDomainError**
  - Type: SystemSingle Upon return, contains an array of the code domain error traces for the individual code channels in the domain of the base spreading factor averaged over all active time slots and averaging iterations. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/3d7f18e0-2687-b768-ea5c-9d2d7da2ac20.htm language=enus -->
## TOPIC 00044: rfmxtdscdmadotnet/html/3d7f18e0-2687-b768-ea5c-9d2d7da2ac20.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/3d7f18e0-2687-b768-ea5c-9d2d7da2ac20.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/3d7f18e0-2687-b768-ea5c-9d2d7da2ac20.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemConfiguration.SetAllTracesEnabled Method

RFmxTdscdmaMXSemConfigurationSetAllTracesEnabled Method

Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemBooleanSpecifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

###### Return Value

Int32

##### Remarks

SemAllTracesEnabled

##### See Also

###### Reference

RFmxTdscdmaMXSemConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/3e636539-1992-af58-ab04-14dcbbe4c16e.htm language=enus -->
## TOPIC 00045: rfmxtdscdmadotnet/html/3e636539-1992-af58-ab04-14dcbbe4c16e.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/3e636539-1992-af58-ab04-14dcbbe4c16e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/3e636539-1992-af58-ab04-14dcbbe4c16e.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaResults.GetMaximumTotalActivePower Method

RFmxTdscdmaMXCdaResultsGetMaximumTotalActivePower Method

SetPowerUnit(String, RFmxTdscdmaMXCdaPowerUnit)

dB

dBm

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumTotalActivePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumTotalActivePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDouble Upon return, contains the maximum value, among all averaging iterations, of total power measured in the code domain of the base spreading factor normalized to the total code domain power. This value is expressed in dB, if you set the SetPowerUnit(String, RFmxTdscdmaMXCdaPowerUnit) method to dB, or in dBm, if you set the CDA Pwr Unit method to dBm.

###### Return Value

Int32

##### Remarks

CdaResultsMaximumTotalActivePower

##### See Also

###### Reference

RFmxTdscdmaMXCdaResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/419cc814-49ac-daba-7893-d618ac8bf013.htm language=enus -->
## TOPIC 00046: rfmxtdscdmadotnet/html/419cc814-49ac-daba-7893-d618ac8bf013.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/419cc814-49ac-daba-7893-d618ac8bf013.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/419cc814-49ac-daba-7893-d618ac8bf013.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetIQPowerEdgeTriggerSource Method

RFmxTdscdmaMXGetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxTdscdmaMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemString Upon return, contains the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/42ad60ac-9999-c019-a356-c6f2d05eff35.htm language=enus -->
## TOPIC 00047: rfmxtdscdmadotnet/html/42ad60ac-9999-c019-a356-c6f2d05eff35.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/42ad60ac-9999-c019-a356-c6f2d05eff35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/42ad60ac-9999-c019-a356-c6f2d05eff35.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemLowerOffsetMeasurementStatus Enumeration

RFmxTdscdmaMXSemLowerOffsetMeasurementStatus Enumeration

"offset(n)"

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXSemLowerOffsetMeasurementStatus
```

```text
Public Enumeration RFmxTdscdmaMXSemLowerOffsetMeasurementStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 | The lower offset segment measurement failed according to the measurement limits and criteria you set. |
|  | Pass | 1 | The lower offset segment measurement passed according to the measurement limits and criteria you set. |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/46dcef0d-58fb-9aea-47a1-d418cada57cd.htm language=enus -->
## TOPIC 00048: rfmxtdscdmadotnet/html/46dcef0d-58fb-9aea-47a1-d418cada57cd.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/46dcef0d-58fb-9aea-47a1-d418cada57cd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/46dcef0d-58fb-9aea-47a1-d418cada57cd.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXChpConfiguration.GetSweepTimeInterval Method

RFmxTdscdmaMXChpConfigurationGetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxTdscdmaMXChpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the sweep time when you set the SetSweepTimeAuto(String, RFmxTdscdmaMXChpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ChpSweepTimeInterval

##### See Also

###### Reference

RFmxTdscdmaMXChpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/4c5875bc-270a-727e-d5a1-9ec18890efa1.htm language=enus -->
## TOPIC 00049: rfmxtdscdmadotnet/html/4c5875bc-270a-727e-d5a1-9ec18890efa1.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/4c5875bc-270a-727e-d5a1-9ec18890efa1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/4c5875bc-270a-727e-d5a1-9ec18890efa1.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaResults.FetchSymbolEvm Method

RFmxTdscdmaMXCdaResultsFetchSymbolEvm Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSymbolEvm(
	string selectorString,
	double timeout,
	out double meanRmsSymbolEvm,
	out double maximumPeakSymbolEvm,
	out double frequencyError,
	out double chipRateError,
	out double meanRmsSymbolMagnitudeError,
	out double meanRmsSymbolPhaseError,
	out double meanSymbolPower
)
```

```text
Public Function FetchSymbolEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRmsSymbolEvm As Double,
	<OutAttribute> ByRef maximumPeakSymbolEvm As Double,
	<OutAttribute> ByRef frequencyError As Double,
	<OutAttribute> ByRef chipRateError As Double,
	<OutAttribute> ByRef meanRmsSymbolMagnitudeError As Double,
	<OutAttribute> ByRef meanRmsSymbolPhaseError As Double,
	<OutAttribute> ByRef meanSymbolPower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsSymbolEvm**
  - Type: SystemDouble Upon return, contains the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage.
- **maximumPeakSymbolEvm**
  - Type: SystemDouble Upon return, contains the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage.
- **frequencyError**
  - Type: SystemDouble Upon return, contains the frequency error averaged over all measured slots. This value is expressed in Hz.
- **chipRateError**
  - Type: SystemDouble Upon return, contains the chip rate error. This value is expressed in ppm.
- **meanRmsSymbolMagnitudeError**
  - Type: SystemDouble Upon return, contains the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage.
- **meanRmsSymbolPhaseError**
  - Type: SystemDouble Upon return, contains the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees.
- **meanSymbolPower**
  - Type: SystemDouble Upon return, contains the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the SetPowerUnit(String, RFmxTdscdmaMXCdaPowerUnit) method to dB, and in dBm if you set the CDA Pwr Unit method to dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXCdaResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/51917193-8ab6-0a6a-7a55-fa7a3e887cef.htm language=enus -->
## TOPIC 00050: rfmxtdscdmadotnet/html/51917193-8ab6-0a6a-7a55-fa7a3e887cef.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/51917193-8ab6-0a6a-7a55-fa7a3e887cef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/51917193-8ab6-0a6a-7a55-fa7a3e887cef.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.AbortMeasurements Method

RFmxTdscdmaMXAbortMeasurements Method

selectorString

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/5238b7f0-eff2-1ccd-d36e-a0667d329c54.htm language=enus -->
## TOPIC 00051: rfmxtdscdmadotnet/html/5238b7f0-eff2-1ccd-d36e-a0667d329c54.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/5238b7f0-eff2-1ccd-d36e-a0667d329c54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/5238b7f0-eff2-1ccd-d36e-a0667d329c54.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.GetAveragingCount Method

RFmxTdscdmaMXAcpConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxTdscdmaMXAcpAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxTdscdmaMXAcpAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

AcpAveragingCount

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/53b6bd31-6e26-7f73-2088-2fd5fe6cad44.htm language=enus -->
## TOPIC 00052: rfmxtdscdmadotnet/html/53b6bd31-6e26-7f73-2088-2fd5fe6cad44.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/53b6bd31-6e26-7f73-2088-2fd5fe6cad44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/53b6bd31-6e26-7f73-2088-2fd5fe6cad44.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.ConfigureSoftwareEdgeTrigger Method

RFmxTdscdmaMXConfigureSoftwareEdgeTrigger Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSoftwareEdgeTrigger(
	string selectorString,
	double triggerDelay,
	bool enableTrigger
)
```

```text
Public Function ConfigureSoftwareEdgeTrigger ( 
	selectorString As String,
	triggerDelay As Double,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **triggerDelay**
  - Type: SystemDoubleSpecifies the trigger delay time. This value is expressed in seconds.
- **enableTrigger**
  - Type: SystemBooleanSpecifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/54ee78f3-df09-6643-9fa5-7ab6f90c04d3.htm language=enus -->
## TOPIC 00053: rfmxtdscdmadotnet/html/54ee78f3-df09-6643-9fa5-7ab6f90c04d3.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/54ee78f3-df09-6643-9fa5-7ab6f90c04d3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/54ee78f3-df09-6643-9fa5-7ab6f90c04d3.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.Chp Property

RFmxTdscdmaMXChp Property

RFmxTdscdmaMXChp

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxTdscdmaMXChp Chp { get; }
```

```text
Public ReadOnly Property Chp As RFmxTdscdmaMXChp
	Get
```

###### Property Value

RFmxTdscdmaMXChp

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/55c0d7c7-1913-fe6c-15a4-fef234f3a34d.htm language=enus -->
## TOPIC 00054: rfmxtdscdmadotnet/html/55c0d7c7-1913-fe6c-15a4-fef234f3a34d.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/55c0d7c7-1913-fe6c-15a4-fef234f3a34d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/55c0d7c7-1913-fe6c-15a4-fef234f3a34d.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXObwConfiguration.SetSweepTimeInterval Method

RFmxTdscdmaMXObwConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxTdscdmaMXObwSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxTdscdmaMXObwSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ObwSweepTimeInterval

##### See Also

###### Reference

RFmxTdscdmaMXObwConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/579e1529-2ca8-4a03-7b0f-932b3746a9e1.htm language=enus -->
## TOPIC 00055: rfmxtdscdmadotnet/html/579e1529-2ca8-4a03-7b0f-932b3746a9e1.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/579e1529-2ca8-4a03-7b0f-932b3746a9e1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/579e1529-2ca8-4a03-7b0f-932b3746a9e1.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccConfiguration.SetIQGainImbalanceRemovalEnabled Method

RFmxTdscdmaMXModAccConfigurationSetIQGainImbalanceRemovalEnabled Method

Sets whether to remove the I/Q gain imbalance before the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQGainImbalanceRemovalEnabled(
	string selectorString,
	RFmxTdscdmaMXModAccIQGainImbalanceRemovalEnabled value
)
```

```text
Public Function SetIQGainImbalanceRemovalEnabled ( 
	selectorString As String,
	value As RFmxTdscdmaMXModAccIQGainImbalanceRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXModAccIQGainImbalanceRemovalEnabledSpecifies whether to remove the I/Q gain imbalance before the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccIQGainImbalanceRemovalEnabled

False

##### See Also

###### Reference

RFmxTdscdmaMXModAccConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/62130591-7486-7540-7bed-1d5d5f9f6218.htm language=enus -->
## TOPIC 00056: rfmxtdscdmadotnet/html/62130591-7486-7540-7bed-1d5d5f9f6218.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/62130591-7486-7540-7bed-1d5d5f9f6218.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/62130591-7486-7540-7bed-1d5d5f9f6218.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.GetFftOverlap Method

RFmxTdscdmaMXAcpConfigurationGetFftOverlap Method

Gets the number of samples to overlap between consecutive chunks while performing FFT. This value is expressed as a percentage of the Sequential FFT Size when you set the RFmxWcdmaMXAcpMeasurementMethod method to Sequential FFT.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftOverlap(
	string selectorString,
	out double value
)
```

```text
Public Function GetFftOverlap ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, gets the number of samples to overlap between consecutive chunks while performing FFT.

###### Return Value

Int32

##### Remarks

AcpFftOverlap

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/62388be1-f49b-1c6d-7f5e-2d57f257816b.htm language=enus -->
## TOPIC 00057: rfmxtdscdmadotnet/html/62388be1-f49b-1c6d-7f5e-2d57f257816b.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/62388be1-f49b-1c6d-7f5e-2d57f257816b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/62388be1-f49b-1c6d-7f5e-2d57f257816b.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccConfiguration.SetMeasurementLength Method

RFmxTdscdmaMXModAccConfigurationSetMeasurementLength Method

Sets the measurement length for the ModAcc measurement. This value is expressed in traffic slots.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementLength(
	string selectorString,
	int value
)
```

```text
Public Function SetMeasurementLength ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the measurement length for the ModAcc measurement. This value is expressed in traffic slots.

###### Return Value

Int32

##### Remarks

ModAccMeasurementLength

##### See Also

###### Reference

RFmxTdscdmaMXModAccConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/62fbe808-8a7b-dd0e-7807-5db5ace1ed8c.htm language=enus -->
## TOPIC 00058: rfmxtdscdmadotnet/html/62fbe808-8a7b-dd0e-7807-5db5ace1ed8c.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/62fbe808-8a7b-dd0e-7807-5db5ace1ed8c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/62fbe808-8a7b-dd0e-7807-5db5ace1ed8c.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpAveragingEnabled Enumeration

RFmxTdscdmaMXAcpAveragingEnabled Enumeration

Specifies whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXAcpAveragingEnabled
```

```text
Public Enumeration RFmxTdscdmaMXAcpAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The ACP measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the ACP measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/6316f6da-97f3-742a-5ec6-58d1f68c453a.htm language=enus -->
## TOPIC 00059: rfmxtdscdmadotnet/html/6316f6da-97f3-742a-5ec6-58d1f68c453a.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/6316f6da-97f3-742a-5ec6-58d1f68c453a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/6316f6da-97f3-742a-5ec6-58d1f68c453a.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXObwConfiguration.SetAllTracesEnabled Method

RFmxTdscdmaMXObwConfigurationSetAllTracesEnabled Method

Sets whether to enable storage and retrieval of the traces after performing the OBW measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemBooleanSpecifies whether to enable storage and retrieval of the traces after performing the OBW measurement.

###### Return Value

Int32

##### Remarks

ObwAllTracesEnabled

##### See Also

###### Reference

RFmxTdscdmaMXObwConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/632a366c-11aa-6d0a-2011-473e295826e3.htm language=enus -->
## TOPIC 00060: rfmxtdscdmadotnet/html/632a366c-11aa-6d0a-2011-473e295826e3.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/632a366c-11aa-6d0a-2011-473e295826e3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/632a366c-11aa-6d0a-2011-473e295826e3.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXObw.Results Property

RFmxTdscdmaMXObwResults Property

RFmxTdscdmaMXObwResults

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxTdscdmaMXObwResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxTdscdmaMXObwResults
	Get
```

###### Property Value

RFmxTdscdmaMXObwResults

##### See Also

###### Reference

RFmxTdscdmaMXObw Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/63d0db03-bd1f-fd8d-a8ae-4e2b0e8fa6d0.htm language=enus -->
## TOPIC 00061: rfmxtdscdmadotnet/html/63d0db03-bd1f-fd8d-a8ae-4e2b0e8fa6d0.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/63d0db03-bd1f-fd8d-a8ae-4e2b0e8fa6d0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/63d0db03-bd1f-fd8d-a8ae-4e2b0e8fa6d0.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.GetAveragingEnabled Method

RFmxTdscdmaMXAcpConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the ACP measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxTdscdmaMXAcpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXAcpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXAcpAveragingEnabledUpon return, contains whether to enable averaging for the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpAveragingEnabled

False

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/67806a5e-b52c-b273-ce21-96454ae51e3e.htm language=enus -->
## TOPIC 00062: rfmxtdscdmadotnet/html/67806a5e-b52c-b273-ce21-96454ae51e3e.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/67806a5e-b52c-b273-ce21-96454ae51e3e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/67806a5e-b52c-b273-ce21-96454ae51e3e.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.SetSweepTimeInterval Method

RFmxTdscdmaMXAcpConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxTdscdmaMXAcpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxTdscdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

AcpSweepTimeInterval

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/6cfa50fe-c1a6-2a88-33c4-23aef8c82ecb.htm language=enus -->
## TOPIC 00063: rfmxtdscdmadotnet/html/6cfa50fe-c1a6-2a88-33c4-23aef8c82ecb.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/6cfa50fe-c1a6-2a88-33c4-23aef8c82ecb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/6cfa50fe-c1a6-2a88-33c4-23aef8c82ecb.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccConfiguration.ConfigureSlotType Method

RFmxTdscdmaMXModAccConfigurationConfigureSlotType Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSlotType(
	string selectorString,
	RFmxTdscdmaMXModAccSlotType slotType
)
```

```text
Public Function ConfigureSlotType ( 
	selectorString As String,
	slotType As RFmxTdscdmaMXModAccSlotType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **slotType**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXModAccSlotTypeSpecifies the type of the Time Slot for ModAcc analysis.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXModAccConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/6d5283bd-ead7-9729-ce22-85948bbded7e.htm language=enus -->
## TOPIC 00064: rfmxtdscdmadotnet/html/6d5283bd-ead7-9729-ce22-85948bbded7e.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/6d5283bd-ead7-9729-ce22-85948bbded7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/6d5283bd-ead7-9729-ce22-85948bbded7e.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemUpperOffsetMeasurementStatus Enumeration

RFmxTdscdmaMXSemUpperOffsetMeasurementStatus Enumeration

"offset(n)"

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXSemUpperOffsetMeasurementStatus
```

```text
Public Enumeration RFmxTdscdmaMXSemUpperOffsetMeasurementStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Fail | 0 | The measured power exceeded the specified measurement limits and failure criteria. |
|  | Pass | 1 | The measured power did not exceed the specified measurement limits and failure criteria. |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/6e411769-ab57-7dae-6bea-fbc3f8d89552.htm language=enus -->
## TOPIC 00065: rfmxtdscdmadotnet/html/6e411769-ab57-7dae-6bea-fbc3f8d89552.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/6e411769-ab57-7dae-6bea-fbc3f8d89552.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/6e411769-ab57-7dae-6bea-fbc3f8d89552.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpResults.GetUpperOffsetAbsolutePower Method

RFmxTdscdmaMXAcpResultsGetUpperOffsetAbsolutePower Method

"offset(n)"

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemDouble Upon return, contains the absolute measured upper offset channel power. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

AcpResultsUpperOffsetAbsolutePower

##### See Also

###### Reference

RFmxTdscdmaMXAcpResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/6eee0b4b-46b1-6b16-0c48-995a72939d01.htm language=enus -->
## TOPIC 00066: rfmxtdscdmadotnet/html/6eee0b4b-46b1-6b16-0c48-995a72939d01.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/6eee0b4b-46b1-6b16-0c48-995a72939d01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/6eee0b4b-46b1-6b16-0c48-995a72939d01.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetErrorString Method

RFmxTdscdmaMXGetErrorString Method

Converts the status code returned by an RFmxTDSCDMA function into a string.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetErrorString(
	int errorCode,
	out string errorDescription
)
```

```text
Public Function GetErrorString ( 
	errorCode As Integer,
	<OutAttribute> ByRef errorDescription As String
) As Integer
```

###### Parameters

- **errorCode**
  - Type: SystemInt32Specifies an error or warning code.
- **errorDescription**
  - Type: SystemStringUpon return, contains the error description.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/6f9dd113-64f1-7dd3-474d-4f176a65363c.htm language=enus -->
## TOPIC 00067: rfmxtdscdmadotnet/html/6f9dd113-64f1-7dd3-474d-4f176a65363c.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/6f9dd113-64f1-7dd3-474d-4f176a65363c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/6f9dd113-64f1-7dd3-474d-4f176a65363c.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtResults.FetchSignalPowerTrace Method

RFmxTdscdmaMXPvtResultsFetchSignalPowerTrace Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSignalPowerTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> signalPower,
	ref AnalogWaveform<float> absoluteLimit
)
```

```text
Public Function FetchSignalPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef signalPower As AnalogWaveform(Of Single),
	ByRef absoluteLimit As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **signalPower**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the measured signal power over a specified period of time.
- **absoluteLimit**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the power limit as defined by the transmit ON/OFF time mask in the 3GPP TS 34.122 specification.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXPvtResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/70fcac07-8dbf-fc05-ed5f-22073d691c55.htm language=enus -->
## TOPIC 00068: rfmxtdscdmadotnet/html/70fcac07-8dbf-fc05-ed5f-22073d691c55.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/70fcac07-8dbf-fc05-ed5f-22073d691c55.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/70fcac07-8dbf-fc05-ed5f-22073d691c55.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.SetIFOutputPowerOffsetAuto Method

RFmxTdscdmaMXAcpConfigurationSetIFOutputPowerOffsetAuto Method

SetMeasurementMethod(String, RFmxTdscdmaMXAcpMeasurementMethod)

DynamicRange

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIFOutputPowerOffsetAuto(
	string selectorString,
	RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto value
)
```

```text
Public Function SetIFOutputPowerOffsetAuto ( 
	selectorString As String,
	value As RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXAcpIFOutputPowerOffsetAuto Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is used only if you set the SetMeasurementMethod(String, RFmxTdscdmaMXAcpMeasurementMethod) method to DynamicRange.

###### Return Value

Int32

##### Remarks

AcpIFOutputPowerOffsetAuto

True

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/71b3e0ce-191d-cc4d-b4f0-096736ac3d1a.htm language=enus -->
## TOPIC 00069: rfmxtdscdmadotnet/html/71b3e0ce-191d-cc4d-b4f0-096736ac3d1a.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/71b3e0ce-191d-cc4d-b4f0-096736ac3d1a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/71b3e0ce-191d-cc4d-b4f0-096736ac3d1a.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpResults.GetCarrierAbsolutePower Method

RFmxTdscdmaMXAcpResultsGetCarrierAbsolutePower Method

Gets the absolute measured carrier power. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the absolute measured carrier power. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AcpResultsCarrierAbsolutePower

##### See Also

###### Reference

RFmxTdscdmaMXAcpResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/71e3e74c-7dcd-d65d-f366-a32482f9bf43.htm language=enus -->
## TOPIC 00070: rfmxtdscdmadotnet/html/71e3e74c-7dcd-d65d-f366-a32482f9bf43.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/71e3e74c-7dcd-d65d-f366-a32482f9bf43.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/71e3e74c-7dcd-d65d-f366-a32482f9bf43.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaResults.FetchMeanSymbolEvmTrace Method

RFmxTdscdmaMXCdaResultsFetchMeanSymbolEvmTrace Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMeanSymbolEvmTrace(
	string selectorString,
	double timeout,
	ref float[] meanSymbolEvm
)
```

```text
Public Function FetchMeanSymbolEvmTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef meanSymbolEvm As Single()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanSymbolEvm**
  - Type: SystemSingle Upon return, contains an array of the averaged symbol EVM traces for the configured measurement channel. This value is expressed as a percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXCdaResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/79724a8c-6e5c-d709-9c72-a43eeda9dc82.htm language=enus -->
## TOPIC 00071: rfmxtdscdmadotnet/html/79724a8c-6e5c-d709-9c72-a43eeda9dc82.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/79724a8c-6e5c-d709-9c72-a43eeda9dc82.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/79724a8c-6e5c-d709-9c72-a43eeda9dc82.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.SetExternalAttenuation Method

RFmxTdscdmaMXSetExternalAttenuation Method

Sets the level of external attenuation that is considered by the selected measurement. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetExternalAttenuation(
	string selectorString,
	double value
)
```

```text
Public Function SetExternalAttenuation ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ExternalAttenuation

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/7bcf710a-b710-e2bf-b378-40111409cc18.htm language=enus -->
## TOPIC 00072: rfmxtdscdmadotnet/html/7bcf710a-b710-e2bf-b378-40111409cc18.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/7bcf710a-b710-e2bf-b378-40111409cc18.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/7bcf710a-b710-e2bf-b378-40111409cc18.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXChp Class

RFmxTdscdmaMXChp Class

Represents the CHP measurement.

##### Inheritance Hierarchy

RFmxTdscdmaMXSubObject

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxTdscdmaMXChp : RFmxTdscdmaMXSubObject
```

```text
Public NotInheritable Class RFmxTdscdmaMXChp
	Inherits RFmxTdscdmaMXSubObject
```

The RFmxTdscdmaMXChp type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxTdscdmaMXChpConfiguration instance that provides methods to configure the CHP measurement |
|  | Results | Gets the RFmxTdscdmaMXChpResults instance that provides methods to fetch and read the CHP measurement results. |

Top

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

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/7ccfc3ed-04dd-7ade-b768-6e6deaa00ea9.htm language=enus -->
## TOPIC 00073: rfmxtdscdmadotnet/html/7ccfc3ed-04dd-7ade-b768-6e6deaa00ea9.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/7ccfc3ed-04dd-7ade-b768-6e6deaa00ea9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/7ccfc3ed-04dd-7ade-b768-6e6deaa00ea9.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccConfiguration.GetSpectrumInverted Method

RFmxTdscdmaMXModAccConfigurationGetSpectrumInverted Method

Gets whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectrumInverted(
	string selectorString,
	out RFmxTdscdmaMXModAccSpectrumInverted value
)
```

```text
Public Function GetSpectrumInverted ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXModAccSpectrumInverted
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXModAccSpectrumInvertedUpon return, contains whether the spectrum of the signal is inverted.

###### Return Value

Int32

##### Remarks

ModAccSpectrumInverted

False

##### See Also

###### Reference

RFmxTdscdmaMXModAccConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/7f49b194-a41d-8eae-7993-3c31a760a5e0.htm language=enus -->
## TOPIC 00074: rfmxtdscdmadotnet/html/7f49b194-a41d-8eae-7993-3c31a760a5e0.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/7f49b194-a41d-8eae-7993-3c31a760a5e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/7f49b194-a41d-8eae-7993-3c31a760a5e0.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemConfiguration.SetMeasurementEnabled Method

RFmxTdscdmaMXSemConfigurationSetMeasurementEnabled Method

Sets whether to enable the SEM measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemBooleanSpecifies whether to enable the SEM measurement.

###### Return Value

Int32

##### Remarks

SemMeasurementEnabled

##### See Also

###### Reference

RFmxTdscdmaMXSemConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/833c5629-8b87-e3d5-fbeb-250d53c7cf46.htm language=enus -->
## TOPIC 00075: rfmxtdscdmadotnet/html/833c5629-8b87-e3d5-fbeb-250d53c7cf46.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/833c5629-8b87-e3d5-fbeb-250d53c7cf46.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/833c5629-8b87-e3d5-fbeb-250d53c7cf46.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCda Methods

RFmxTdscdmaMXCda Methods

The [RFmxTdscdmaMXCda](60593a58-00cb-363c-2fd8-27e19b3b01c3.htm) type exposes the following members.

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

RFmxTdscdmaMXCda Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/837617cb-8691-3d6c-b5d7-8dbfab5332f0.htm language=enus -->
## TOPIC 00076: rfmxtdscdmadotnet/html/837617cb-8691-3d6c-b5d7-8dbfab5332f0.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/837617cb-8691-3d6c-b5d7-8dbfab5332f0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/837617cb-8691-3d6c-b5d7-8dbfab5332f0.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXObwSweepTimeAuto Enumeration

RFmxTdscdmaMXObwSweepTimeAuto Enumeration

Specifies whether the measurement calculates the sweep time.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXObwSweepTimeAuto
```

```text
Public Enumeration RFmxTdscdmaMXObwSweepTimeAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(String, Double) method. |
|  | True | 1 | The measurement uses the default sweep time of .00066 seconds (s). |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/83bfab3c-4fa8-bb34-d81a-75c01c3c0fd1.htm language=enus -->
## TOPIC 00077: rfmxtdscdmadotnet/html/83bfab3c-4fa8-bb34-d81a-75c01c3c0fd1.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/83bfab3c-4fa8-bb34-d81a-75c01c3c0fd1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/83bfab3c-4fa8-bb34-d81a-75c01c3c0fd1.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX Class

RFmxTdscdmaMX Class

Defines a root class which is used to identify and control TDSCDMA signal configuration.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxTdscdmaMX : ISignalConfiguration, 
	IDisposable
```

```text
Public NotInheritable Class RFmxTdscdmaMX
	Implements ISignalConfiguration, IDisposable
```

The RFmxTdscdmaMX type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Acp | Gets the RFmxTdscdmaMXAcp instance that represents the ACP measurement. |
|  | Cda | Gets the RFmxTdscdmaMXCda instance that represents the CDA measurement. |
|  | Chp | Gets the RFmxTdscdmaMXChp instance that represents the CHP measurement. |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | ModAcc | Gets the RFmxTdscdmaMXModAcc instance that represents the ModAcc measurement. |
|  | Obw | Gets the RFmxTdscdmaMXObw instance that represents the OBW measurement. |
|  | Pvt | Gets the RFmxTdscdmaMXPvt instance that represents the PVT measurement. |
|  | Sem | Gets the RFmxTdscdmaMXSem instance that represents the SEM measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxTdscdmaMX. |
|  | SlotPower | Gets the RFmxTdscdmaMXSlotPower instance that represents the SlotPower measurement. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops the acquisition and measurements associated with the signal instance that you specify in the selectorString parameter. The acquisition and measurements were previously initiated by the Initiate(String, String) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionTypeMethod method value is either IQ or IQorSpectral. Query the Recommended Acquisition Type method from the RFmx driver after calling the RFmxTDSCDMA Commit method. |
|  | AnalyzeSpectrum1Waveform | Performs the enabled measurements on the Spectrum waveform that you specify in the spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionTypeMethod method value is either spectral or IQorSpectral. Query the Recommended Acquisition Type method from the RFmx driver after calling the RFmxTDSCDMA Commit method. |
|  | AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level method. Use this method to calculate an approximate setting for the reference level. The RFmxTDSCDMA Auto Level method completes the following tasks: Resets the mixer level, mixer level offset, and IF output power offset. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings. Iterates to adjust the reference level based on the input signal peak power. Uses immediate triggering and restores the trigger settings back to user setting after the execution. You can also specify the starting reference level using the SetAutoLevelInitialReferenceLevel(String, Double) method. When using PXIe-5663/5665/5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxTDSCDMA Auto Level method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method; thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildChannelString | Creates a selector string to use with channel-specific configuration or fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals. |
|  | BuildOffsetString | Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSegmentString | Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxTDSCDMA commits settings to the hardware when you call the Initiate(String, String) method. |
|  | ConfigureChannelConfigurationMode | Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureExternalAttenuation | Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. |
|  | ConfigureFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
|  | ConfigureFrequencyChannelNumber | Configures the carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
|  | ConfigureMidamble | Obsolete. This method is now deprecated, please use the RFmxTDSCDMA Configure Midamble Shift method in the place of this method. |
|  | ConfigureMidambleShift | Configures the midambleAutoDetectionMode, maximumNumberOfUsers, and MidambleShift parameters. |
|  | ConfigureNumberOfChannels | Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to userDefined. |
|  | ConfigurePilot | Configures the pilot code of the TD-SCDMA signal. |
|  | ConfigureReferenceLevel | Configures the reference level. The reference level represents the maximum expected power of an input RF signal. |
|  | ConfigureRF | Configures the RF methods of the signal specified by the selectorString parameter. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a software trigger to mark a reference point within the record. |
|  | ConfigureUplinkScramblingCode | Configures the scrambling code used for the uplink transmission. |
|  | ConfigureUserDefinedChannel | Configures an individual user-defined channel when the channel configuration mode is set to userDefined. Use "channel(n)" as the selector string to configure this method. A channel configuration is defined by the slot index it refers to, the channel type, and the modulation type. |
|  | ConfigureUserDefinedChannelArray | Configures all user-defined channels when the channel configuration mode is set to userDefined. Use equal-sized arrays for slotIndex, channelType, and modulationType. You can configure up to two channels for the same index for multi-code transmission. |
|  | DeleteSignalConfiguration | Deletes an instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllNamedResultNames | Returns all the named result names of the current signal instance. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | GetCenterFrequency | Gets the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. |
|  | GetChannelConfigurationMode | Gets whether to detect the channels automatically or to use a specified channel configuration. |
|  | GetChannelizationCode | Gets the channelization code of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | GetChannelType | Gets the channel type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | GetDigitalEdgeTriggerEdge | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
|  | GetDigitalEdgeTriggerSource | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
|  | GetErrorString | Converts the status code returned by an RFmxTDSCDMA function into a string. |
|  | GetExternalAttenuation | Gets the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIQPowerEdgeTriggerLevel | Gets the threshold above or below which the signal analyzer triggers, depending on the value of the SetIQPowerEdgeTriggerSlope(String, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(String, RFmxTdscdmaMXIQPowerEdgeTriggerLevelType) method is set to Relative or in dBm when the IQ Power Edge Level Type method is set to Absolute. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or when the signal power is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | GetMaximumNumberOfUsers | Configures the maximum number of users. |
|  | GetMidambleAutoDetectionMode | Gets the midamble auto detection mode. |
|  | GetMidambleCode | Obsolete. Gets the midamble code. |
|  | GetMidambleShift | Gets the midamble shift used when you set the SetMidambleAutoDetectionMode(String, RFmxTdscdmaMXMidambleAutoDetectionMode) method to Off. This value is expressed in chips. |
|  | GetModulationType | Gets the modulation type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | GetNumberOfChannels | Gets the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. |
|  | GetPilotCode | Gets the SYNC-UL code used by the uplink pilot time slot (UpPTS). This method is used when the SetSynchronizationMode(String, RFmxTdscdmaMXModAccSynchronizationMode) method is set to Subframe, or the SetSlotType(String, RFmxTdscdmaMXModAccSlotType) method is set to Pilot. |
|  | GetReferenceLevel | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | GetResultFetchTimeout | Gets the time to wait before results are available in the RFmx driver. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be used by the measurement. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | GetSlotFormat | Gets the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | GetSlotIndex | Gets the slot index of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | GetTriggerDelay | Gets the trigger delay time. This value is expressed in seconds. |
|  | GetTriggerMinimumQuietTimeDuration | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement calculates the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the trigger type. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUplinkScramblingCode | Gets the scrambling code and the basic midamble code for uplink transmission. |
|  | GetWarning | Gets the latest warning code and description. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the fetch methods or result methods. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or the CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. This method disables all the external attenuation tables in all calibration planes. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxTDSCDMA_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations:You configure an invalid trigger.You have not previously called the RFmxMXTdscdmaMX.Initiate method. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SetCenterFrequency | Sets the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. |
|  | SetChannelConfigurationMode | Sets whether to detect the channels automatically or to use a specified channel configuration. |
|  | SetChannelizationCode | Sets the channelization code of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | SetChannelType | Sets the channel type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | SetDigitalEdgeTriggerEdge | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
|  | SetExternalAttenuation | Sets the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. |
|  | SetIQPowerEdgeTriggerLevel | Sets the threshold above or below which the signal analyzer triggers, depending on the value of the SetIQPowerEdgeTriggerSlope(String, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(String, RFmxTdscdmaMXIQPowerEdgeTriggerLevelType) method is set to Relative or in dBm when the IQ Power Edge Level Type method is set to Absolute. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the trigger when the signal power is rising or when the signal power is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx in the locked signal configuration state. |
|  | SetMaximumNumberOfUsers | Configures the maximum number of users. |
|  | SetMidambleAutoDetectionMode | Sets the midamble auto detection mode. |
|  | SetMidambleCode | Obsolete. Sets the midamble code. |
|  | SetMidambleShift | Sets the midamble shift used when you set the SetMidambleAutoDetectionMode(String, RFmxTdscdmaMXMidambleAutoDetectionMode) method to Off. This value is expressed in chips. |
|  | SetModulationType | Sets the modulation type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | SetNumberOfChannels | Sets the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. |
|  | SetPilotCode | Sets the SYNC-UL code used by the uplink pilot time slot (UpPTS). This method is used when the SetSynchronizationMode(String, RFmxTdscdmaMXModAccSynchronizationMode) method is set to Subframe, or the SetSlotType(String, RFmxTdscdmaMXModAccSlotType) method is set to Pilot. |
|  | SetReferenceLevel | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | SetResultFetchTimeout | Sets the time to wait before results are available in the RFmx driver. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
|  | SetSelectedPorts | Sets the instrument port to be used by the measurement. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | SetSlotFormat | Sets the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | SetSlotIndex | Sets the slot index of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
|  | SetTriggerDelay | Sets the trigger delay time. This value is expressed in seconds. |
|  | SetTriggerMinimumQuietTimeDuration | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement calculates the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the trigger type. |
|  | SetUplinkScramblingCode | Sets the scrambling code and the basic midamble code for uplink transmission. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForMeasurementComplete | Waits for the specified number of seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/849d9fbe-97f3-763d-c69e-2c489c524c12.htm language=enus -->
## TOPIC 00078: rfmxtdscdmadotnet/html/849d9fbe-97f3-763d-c69e-2c489c524c12.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/849d9fbe-97f3-763d-c69e-2c489c524c12.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/849d9fbe-97f3-763d-c69e-2c489c524c12.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.GetBaseSpreadingFactor Method

RFmxTdscdmaMXCdaConfigurationGetBaseSpreadingFactor Method

Gets the base spreading factor for code domain analysis.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBaseSpreadingFactor(
	string selectorString,
	out int value
)
```

```text
Public Function GetBaseSpreadingFactor ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the base spreading factor for code domain analysis.

###### Return Value

Int32

##### Remarks

CdaBaseSpreadingFactor

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/8675d838-c7c4-d840-546c-b30d914a8a60.htm language=enus -->
## TOPIC 00079: rfmxtdscdmadotnet/html/8675d838-c7c4-d840-546c-b30d914a8a60.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/8675d838-c7c4-d840-546c-b30d914a8a60.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/8675d838-c7c4-d840-546c-b30d914a8a60.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccSpectrumInverted Enumeration

RFmxTdscdmaMXModAccSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXModAccSpectrumInverted
```

```text
Public Enumeration RFmxTdscdmaMXModAccSpectrumInverted
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measured spectrum is not inverted. |
|  | True | 1 | The measured spectrum is inverted. |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/87c375dc-5b2a-613b-81e2-ccc7b1e3700f.htm language=enus -->
## TOPIC 00080: rfmxtdscdmadotnet/html/87c375dc-5b2a-613b-81e2-ccc7b1e3700f.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/87c375dc-5b2a-613b-81e2-ccc7b1e3700f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/87c375dc-5b2a-613b-81e2-ccc7b1e3700f.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccConfiguration.ConfigureAveraging Method

RFmxTdscdmaMXModAccConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxTdscdmaMXModAccAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxTdscdmaMXModAccAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXModAccAveragingEnabledSpecifies whether to enable averaging for the ModAcc measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXModAccConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/87f38aaa-eeff-2191-0048-e4f64bb6178a.htm language=enus -->
## TOPIC 00081: rfmxtdscdmadotnet/html/87f38aaa-eeff-2191-0048-e4f64bb6178a.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/87f38aaa-eeff-2191-0048-e4f64bb6178a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/87f38aaa-eeff-2191-0048-e4f64bb6178a.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpResults Methods

RFmxTdscdmaMXAcpResults Methods

The [RFmxTdscdmaMXAcpResults](dee03f38-e1fc-6a58-2eeb-01f99577374e.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchAbsolutePowersTrace | Fetches the absolute powers trace for ACP measurement. |
|  | FetchCarrierAbsolutePower | Returns the absolute carrier power. |
|  | FetchOffsetMeasurement | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Use "offset(n)" as the selector string to read results from this method. |
|  | FetchOffsetMeasurementArray | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
|  | FetchRelativePowersTrace | Fetches the relative powers trace for ACP measurement. |
|  | FetchSpectrum | Fetches the spectrum used for the ACP measurement. |
|  | GetCarrierAbsolutePower | Gets the absolute measured carrier power. This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLowerOffsetAbsolutePower | Gets the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result. |
|  | GetLowerOffsetRelativePower | Gets the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this result. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUpperOffsetAbsolutePower | Gets the absolute measured upper offset channel power. This value is expressed in dBm. Use "offset(n)" as the selector string to read this result. |
|  | GetUpperOffsetRelativePower | Gets the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this result. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxTdscdmaMXAcpResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/885afe43-d0a8-c0a9-63c0-8dafa3171531.htm language=enus -->
## TOPIC 00082: rfmxtdscdmadotnet/html/885afe43-d0a8-c0a9-63c0-8dafa3171531.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/885afe43-d0a8-c0a9-63c0-8dafa3171531.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/885afe43-d0a8-c0a9-63c0-8dafa3171531.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.SetMeasurementChannelChannelizationCode Method

RFmxTdscdmaMXCdaConfigurationSetMeasurementChannelChannelizationCode Method

Sets the channelization code of the code domain analysis (CDA) measurement channel.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMeasurementChannelChannelizationCode(
	string selectorString,
	int value
)
```

```text
Public Function SetMeasurementChannelChannelizationCode ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Specifies the channelization code of the code domain analysis (CDA) measurement channel.

###### Return Value

Int32

##### Remarks

CdaMeasurementChannelChannelizationCode

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/894fe48e-1de2-e318-2d7d-72b9aea7429d.htm language=enus -->
## TOPIC 00083: rfmxtdscdmadotnet/html/894fe48e-1de2-e318-2d7d-72b9aea7429d.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/894fe48e-1de2-e318-2d7d-72b9aea7429d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/894fe48e-1de2-e318-2d7d-72b9aea7429d.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetMaximumPeakDataActiveCde Method

RFmxTdscdmaMXModAccResultsGetMaximumPeakDataActiveCde Method

Gets the maximum value of the peak data active code domain errors (CDEs) among all active physical channels and active time slots. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMaximumPeakDataActiveCde(
	string selectorString,
	out double value
)
```

```text
Public Function GetMaximumPeakDataActiveCde ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the maximum value of the peak data active code domain errors (CDEs) among all active physical channels and active time slots. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsMaximumPeakDataActiveCde

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/89a0041f-2fe9-65bb-2c1c-58e4ddd3435d.htm language=enus -->
## TOPIC 00084: rfmxtdscdmadotnet/html/89a0041f-2fe9-65bb-2c1c-58e4ddd3435d.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/89a0041f-2fe9-65bb-2c1c-58e4ddd3435d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/89a0041f-2fe9-65bb-2c1c-58e4ddd3435d.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccAveragingEnabled Enumeration

RFmxTdscdmaMXModAccAveragingEnabled Enumeration

Specifies whether to enable averaging for the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxTdscdmaMXModAccAveragingEnabled
```

```text
Public Enumeration RFmxTdscdmaMXModAccAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The ModAcc measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the ModAcc measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/8bdc798b-0aa8-091f-0431-70da1cfa91e3.htm language=enus -->
## TOPIC 00085: rfmxtdscdmadotnet/html/8bdc798b-0aa8-091f-0431-70da1cfa91e3.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/8bdc798b-0aa8-091f-0431-70da1cfa91e3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/8bdc798b-0aa8-091f-0431-70da1cfa91e3.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.GetSynchronizationMode Method

RFmxTdscdmaMXCdaConfigurationGetSynchronizationMode Method

Slot

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSynchronizationMode(
	string selectorString,
	out RFmxTdscdmaMXCdaSynchronizationMode value
)
```

```text
Public Function GetSynchronizationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxTdscdmaMXCdaSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXCdaSynchronizationMode Upon return, contains the synchronization mode for the code domain analysis (CDA) measurement. Currently, only the Slot mode is supported.

###### Return Value

Int32

##### Remarks

CdaSynchronizationMode

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/8c4f0ab9-c8e5-a591-47f4-6db617a56ac4.htm language=enus -->
## TOPIC 00086: rfmxtdscdmadotnet/html/8c4f0ab9-c8e5-a591-47f4-6db617a56ac4.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/8c4f0ab9-c8e5-a591-47f4-6db617a56ac4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/8c4f0ab9-c8e5-a591-47f4-6db617a56ac4.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.FetchMidambleEvm Method

RFmxTdscdmaMXModAccResultsFetchMidambleEvm Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMidambleEvm(
	string selectorString,
	double timeout,
	out double rmsMidambleEvm,
	out double peakMidambleEvm,
	out double midambleRho,
	out double rmsMidambleMagnitudeError,
	out double rmsMidamblePhaseError
)
```

```text
Public Function FetchMidambleEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef rmsMidambleEvm As Double,
	<OutAttribute> ByRef peakMidambleEvm As Double,
	<OutAttribute> ByRef midambleRho As Double,
	<OutAttribute> ByRef rmsMidambleMagnitudeError As Double,
	<OutAttribute> ByRef rmsMidamblePhaseError As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **rmsMidambleEvm**
  - Type: SystemDouble Upon return, contains the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage.
- **peakMidambleEvm**
  - Type: SystemDouble Upon return, contains the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage.
- **midambleRho**
  - Type: SystemDouble Upon return, contains the rho value of the midamble, averaged over all measured active time slots and averaging iterations.
- **rmsMidambleMagnitudeError**
  - Type: SystemDouble Upon return, contains the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage.
- **rmsMidamblePhaseError**
  - Type: SystemDouble Upon return, contains the RMS of the midamble phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/91fe101b-065f-bc42-43a5-46760b035d91.htm language=enus -->
## TOPIC 00087: rfmxtdscdmadotnet/html/91fe101b-065f-bc42-43a5-46760b035d91.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/91fe101b-065f-bc42-43a5-46760b035d91.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/91fe101b-065f-bc42-43a5-46760b035d91.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.ConfigureMidambleShift Method

RFmxTdscdmaMXConfigureMidambleShift Method

midambleAutoDetectionMode

maximumNumberOfUsers

MidambleShift

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMidambleShift(
	string selectorString,
	RFmxTdscdmaMXMidambleAutoDetectionMode midambleAutoDetectionMode,
	int maximumNumberOfUsers,
	int midambleShift
)
```

```text
Public Function ConfigureMidambleShift ( 
	selectorString As String,
	midambleAutoDetectionMode As RFmxTdscdmaMXMidambleAutoDetectionMode,
	maximumNumberOfUsers As Integer,
	midambleShift As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **midambleAutoDetectionMode**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXMidambleAutoDetectionModeEnables automatic midamble detection.
- **maximumNumberOfUsers**
  - Type: SystemInt32Configures the maximum number of users.
- **midambleShift**
  - Type: SystemInt32 Specifies the midamble shift used when the midambleAutoDetectionMode parameter is set to Off. This value is expressed in chips.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/a821cc0a-59b8-663b-95f4-337d737062ca.htm language=enus -->
## TOPIC 00088: rfmxtdscdmadotnet/html/a821cc0a-59b8-663b-95f4-337d737062ca.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/a821cc0a-59b8-663b-95f4-337d737062ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/a821cc0a-59b8-663b-95f4-337d737062ca.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXPvtResults Methods

RFmxTdscdmaMXPvtResults Methods

The [RFmxTdscdmaMXPvtResults](01152604-c689-b497-9707-751a2365cc79.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurementStatus | Fetches the overall status of the power versus time (PVT) measurement. |
|  | FetchPowers | Fetches the values of the meanAbsoluteONPower and meanAbsoluteOFFPower parameters. |
|  | FetchSegmentMeasurement | Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers. Use "segment(n)" as the selector string to read this method. |
|  | FetchSegmentMeasurementArray | Fetches the status and measured powers for all the power versus time (PVT) measurement segments. |
|  | FetchSignalPowerTrace | Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification. |
|  | GetBurstWidth | Gets the time interval between the time positions where the signal amplitude has reached 90 percent of the full amplitude. This value is expressed in seconds. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaximumAbsolutePower | Gets the maximum power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
|  | GetMeanAbsoluteOffPower | Gets the mean OFF power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
|  | GetMeanAbsoluteOnPower | Gets the mean ON power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
|  | GetMeasurementStatus | Gets the overall status of the power versus time (PVT) measurement. |
|  | GetMidambleCode | Gets the midamble code used for slot synchronization. |
|  | GetMidambleShift | Gets the midamble code shift used for slot synchronization. This value is expressed in chips. |
|  | GetMinimumAbsolutePower | Gets the minimum observed power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
|  | GetSegmentMargin | Gets the power margin for an individual power versus time (PVT) measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. |
|  | GetSegmentMarginTime | Gets the position in time corresponding to the GetSegmentMargin(String, Double) method. This value is expressed in seconds. |
|  | GetSegmentMaximumAbsolutePower | Gets the maximum measured power of an individual power versus time (PVT) measurement segment. This value is expressed in dBm. |
|  | GetSegmentMeanAbsolutePower | Gets the mean measured power corresponding to the GetSegmentMargin(String, Double) method. This value is expressed in dBm. |
|  | GetSegmentMinimumAbsolutePower | Gets the minimum measured power of an individual power versus time (PVT) measurement segment. This value is expressed in dBm. |
|  | GetSegmentStatus | Gets the measurement status for an individual power versus time (PVT) measurement segment. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxTdscdmaMXPvtResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/a880b4c0-79f9-6819-269f-0fec535c3f8c.htm language=enus -->
## TOPIC 00089: rfmxtdscdmadotnet/html/a880b4c0-79f9-6819-269f-0fec535c3f8c.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/a880b4c0-79f9-6819-269f-0fec535c3f8c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/a880b4c0-79f9-6819-269f-0fec535c3f8c.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetAttributeInt Method

RFmxTdscdmaMXGetAttributeInt Method

Gets the value of an RFmx 32-bit integer (int32) attribute.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeInt(
	string selectorString,
	int attributeIdentifier,
	out int value
)
```

```text
Public Function GetAttributeInt ( 
	selectorString As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx TDSCDMA Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt32Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/a9f474b4-cd07-97a7-a02f-1f285a5c82de.htm language=enus -->
## TOPIC 00090: rfmxtdscdmadotnet/html/a9f474b4-cd07-97a7-a02f-1f285a5c82de.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/a9f474b4-cd07-97a7-a02f-1f285a5c82de.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/a9f474b4-cd07-97a7-a02f-1f285a5c82de.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXCdaConfiguration.ConfigureSynchronizationModeAndOffset Method

RFmxTdscdmaMXCdaConfigurationConfigureSynchronizationModeAndOffset Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSynchronizationModeAndOffset(
	string selectorString,
	RFmxTdscdmaMXCdaSynchronizationMode synchronizationMode,
	int measurementOffset
)
```

```text
Public Function ConfigureSynchronizationModeAndOffset ( 
	selectorString As String,
	synchronizationMode As RFmxTdscdmaMXCdaSynchronizationMode,
	measurementOffset As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **synchronizationMode**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXCdaSynchronizationMode Specifies the synchronization mode for the CDA measurement. Currently, only the slot mode is supported.
- **measurementOffset**
  - Type: SystemInt32 Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the synchronizationMode parameter.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXCdaConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/aca2353b-97b8-2a4e-f109-5121af5dfd0d.htm language=enus -->
## TOPIC 00091: rfmxtdscdmadotnet/html/aca2353b-97b8-2a4e-f109-5121af5dfd0d.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/aca2353b-97b8-2a4e-f109-5121af5dfd0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/aca2353b-97b8-2a4e-f109-5121af5dfd0d.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.GetDataField2Power Method

RFmxTdscdmaMXModAccResultsGetDataField2Power Method

Gets the data field 2 power, averaged over all measured active time slots. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDataField2Power(
	string selectorString,
	out double value
)
```

```text
Public Function GetDataField2Power ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the data field 2 power, averaged over all measured active time slots. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

ModAccResultsDataField2Power

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/adb2bc86-09a8-0fb8-8f92-c462f1db5923.htm language=enus -->
## TOPIC 00092: rfmxtdscdmadotnet/html/adb2bc86-09a8-0fb8-8f92-c462f1db5923.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/adb2bc86-09a8-0fb8-8f92-c462f1db5923.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/adb2bc86-09a8-0fb8-8f92-c462f1db5923.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.SetMidambleAutoDetectionMode Method

RFmxTdscdmaMXSetMidambleAutoDetectionMode Method

Sets the midamble auto detection mode.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMidambleAutoDetectionMode(
	string selectorString,
	RFmxTdscdmaMXMidambleAutoDetectionMode value
)
```

```text
Public Function SetMidambleAutoDetectionMode ( 
	selectorString As String,
	value As RFmxTdscdmaMXMidambleAutoDetectionMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.TdscdmaMXRFmxTdscdmaMXMidambleAutoDetectionModeSpecifies the midamble auto detection mode.

###### Return Value

Int32

##### Remarks

MidambleAutoDetectionMode

MidambleShift

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b138a04b-2ae3-315c-36fc-eff0c806b6db.htm language=enus -->
## TOPIC 00093: rfmxtdscdmadotnet/html/b138a04b-2ae3-315c-36fc-eff0c806b6db.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b138a04b-2ae3-315c-36fc-eff0c806b6db.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b138a04b-2ae3-315c-36fc-eff0c806b6db.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.Cda Property

RFmxTdscdmaMXCda Property

RFmxTdscdmaMXCda

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxTdscdmaMXCda Cda { get; }
```

```text
Public ReadOnly Property Cda As RFmxTdscdmaMXCda
	Get
```

###### Property Value

RFmxTdscdmaMXCda

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b18f1dcf-eaa9-874b-1a88-0916a5f8719e.htm language=enus -->
## TOPIC 00094: rfmxtdscdmadotnet/html/b18f1dcf-eaa9-874b-1a88-0916a5f8719e.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b18f1dcf-eaa9-874b-1a88-0916a5f8719e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b18f1dcf-eaa9-874b-1a88-0916a5f8719e.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.GetSweepTimeInterval Method

RFmxTdscdmaMXAcpConfigurationGetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxTdscdmaMXAcpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the sweep time when you set the SetSweepTimeAuto(String, RFmxTdscdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

AcpSweepTimeInterval

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b1d52fc4-be3e-815a-3600-0882f616d3a4.htm language=enus -->
## TOPIC 00095: rfmxtdscdmadotnet/html/b1d52fc4-be3e-815a-3600-0882f616d3a4.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b1d52fc4-be3e-815a-3600-0882f616d3a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b1d52fc4-be3e-815a-3600-0882f616d3a4.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.ConfigureReferenceLevel Method

RFmxTdscdmaMXConfigureReferenceLevel Method

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemDouble Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b5e8e904-fbc1-4ce4-3925-0b928acba3ad.htm language=enus -->
## TOPIC 00096: rfmxtdscdmadotnet/html/b5e8e904-fbc1-4ce4-3925-0b928acba3ad.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b5e8e904-fbc1-4ce4-3925-0b928acba3ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b5e8e904-fbc1-4ce4-3925-0b928acba3ad.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetAllNamedResultNames Method

RFmxTdscdmaMXGetAllNamedResultNames Method

Returns all the named result names of the current signal instance.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **resultNames**
  - Type: SystemStringReturns an array of result names.
- **defaultResultExists**
  - Type: SystemBooleanIndicates whether the default result exists.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b86ac3d0-151c-6a0d-c478-5ded8f045a01.htm language=enus -->
## TOPIC 00097: rfmxtdscdmadotnet/html/b86ac3d0-151c-6a0d-c478-5ded8f045a01.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b86ac3d0-151c-6a0d-c478-5ded8f045a01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b86ac3d0-151c-6a0d-c478-5ded8f045a01.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXAcpConfiguration.SetRbwFilterBandwidth Method

RFmxTdscdmaMXAcpConfigurationSetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxTdscdmaMXAcpRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(String, RFmxTdscdmaMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpRbwFilterBandwidth

##### See Also

###### Reference

RFmxTdscdmaMXAcpConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b8b8aba8-8817-ccfe-9c6b-490504cfed7a.htm language=enus -->
## TOPIC 00098: rfmxtdscdmadotnet/html/b8b8aba8-8817-ccfe-9c6b-490504cfed7a.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b8b8aba8-8817-ccfe-9c6b-490504cfed7a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b8b8aba8-8817-ccfe-9c6b-490504cfed7a.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetAttributeString Method

RFmxTdscdmaMXGetAttributeString Method

Gets the value of a of an RFmx string.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemString Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx TDSCDMA Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemStringUpon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b8e2fbd9-a246-d0da-7d14-da15c24b96cf.htm language=enus -->
## TOPIC 00099: rfmxtdscdmadotnet/html/b8e2fbd9-a246-d0da-7d14-da15c24b96cf.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b8e2fbd9-a246-d0da-7d14-da15c24b96cf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b8e2fbd9-a246-d0da-7d14-da15c24b96cf.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXSemConfiguration.SetNumberOfAnalysisThreads Method

RFmxTdscdmaMXSemConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the SEM measurement.

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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
  - Type: SystemInt32Specifies the maximum number of threads used for parallelism for the SEM measurement.

###### Return Value

Int32

##### Remarks

SemNumberOfAnalysisThreads

##### See Also

###### Reference

RFmxTdscdmaMXSemConfiguration Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b8edc3cf-7311-7fa5-f4b4-591e50877df9.htm language=enus -->
## TOPIC 00100: rfmxtdscdmadotnet/html/b8edc3cf-7311-7fa5-f4b4-591e50877df9.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b8edc3cf-7311-7fa5-f4b4-591e50877df9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b8edc3cf-7311-7fa5-f4b4-591e50877df9.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMX.GetPilotCode Method

RFmxTdscdmaMXGetPilotCode Method

SetSynchronizationMode(String, RFmxTdscdmaMXModAccSynchronizationMode)

Subframe

SetSlotType(String, RFmxTdscdmaMXModAccSlotType)

Pilot

Namespace:

NationalInstruments.RFmx.TdscdmaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPilotCode(
	string selectorString,
	out int value
)
```

```text
Public Function GetPilotCode ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the SYNC-UL code used by the uplink pilot time slot (UpPTS). This method is used when the SetSynchronizationMode(String, RFmxTdscdmaMXModAccSynchronizationMode) method is set to Subframe, or the SetSlotType(String, RFmxTdscdmaMXModAccSlotType) method is set to Pilot.

###### Return Value

Int32

##### Remarks

PilotCode

##### See Also

###### Reference

RFmxTdscdmaMX Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-tdscdma-dotnet path=rfmxtdscdmadotnet/html/b96b9ecb-d19d-18bf-a258-062441fe1e14.htm language=enus -->
## TOPIC 00101: rfmxtdscdmadotnet/html/b96b9ecb-d19d-18bf-a258-062441fe1e14.htm

- bundle_id: `rfmx-tdscdma-dotnet`
- source_path: `rfmxtdscdmadotnet/html/b96b9ecb-d19d-18bf-a258-062441fe1e14.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-dotnet/raw/resource/enus/rfmxtdscdmadotnet/html/b96b9ecb-d19d-18bf-a258-062441fe1e14.htm
- document_id: `rfmx-tdscdma-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxTdscdmaMXModAccResults.FetchNumberOfDetectedChannels Method

RFmxTdscdmaMXModAccResultsFetchNumberOfDetectedChannels Method

SetChannelConfigurationMode(String, RFmxTdscdmaMXChannelConfigurationMode)

UserDefined

Namespace:

NationalInstruments.RFmx.TdscdmaMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **numberOfDetectedChannels**
  - Type: SystemInt32 Upon return, contains the total number of the detected channels.

###### Return Value

Int32

##### See Also

###### Reference

RFmxTdscdmaMXModAccResults Class

NationalInstruments.RFmx.TdscdmaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
