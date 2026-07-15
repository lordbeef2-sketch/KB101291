# NI DOCUMENT BUNDLE: rfmx-evdo-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-evdo-dotnet start=1 end=117 -->
<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/06bef319-8778-a3e0-35fd-191484151a6f.htm language=enus -->
## TOPIC 00001: rfmxevdodotnet/html/06bef319-8778-a3e0-35fd-191484151a6f.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/06bef319-8778-a3e0-35fd-191484151a6f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/06bef319-8778-a3e0-35fd-191484151a6f.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCda Methods

RFmxEvdoMXCda Methods

The [RFmxEvdoMXCda](df8d6296-5e1a-8050-e8b2-5872ab03cbc8.htm) type exposes the following members.

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

RFmxEvdoMXCda Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/08cdf40a-00c9-9a7d-a516-a33aae8a0b01.htm language=enus -->
## TOPIC 00002: rfmxevdodotnet/html/08cdf40a-00c9-9a7d-a516-a33aae8a0b01.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/08cdf40a-00c9-9a7d-a516-a33aae8a0b01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/08cdf40a-00c9-9a7d-a516-a33aae8a0b01.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SetUplinkSpreadingIMask Method

RFmxEvdoMXSetUplinkSpreadingIMask Method

Sets the long code mask of the in-phase (I) channel. The default value is 0x0.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUplinkSpreadingIMask(
	string selectorString,
	long value
)
```

```text
Public Function SetUplinkSpreadingIMask ( 
	selectorString As String,
	value As Long
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt64Specifies the long code mask of the in-phase (I) channel. The default value is 0x0.

###### Return Value

Int32

##### Remarks

UplinkSpreadingIMask

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/0b9d4b2d-ee04-f0ab-ad91-a9a1afeb769f.htm language=enus -->
## TOPIC 00003: rfmxevdodotnet/html/0b9d4b2d-ee04-f0ab-ad91-a9a1afeb769f.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/0b9d4b2d-ee04-f0ab-ad91-a9a1afeb769f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/0b9d4b2d-ee04-f0ab-ad91-a9a1afeb769f.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetUplinkPeakCdeBranch Method

RFmxEvdoMXModAccResultsGetUplinkPeakCdeBranch Method

Gets the branch of the channel corresponding to the Peak Active CDE (dB) method result.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkPeakCdeBranch(
	string selectorString,
	out RFmxEvdoMXModAccUplinkPeakCdeBranch value
)
```

```text
Public Function GetUplinkPeakCdeBranch ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXModAccUplinkPeakCdeBranch
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXModAccUplinkPeakCdeBranchUpon return, contains the branch of the channel corresponding to the Peak Active CDE (dB) method result.

###### Return Value

Int32

##### Remarks

ModAccResultsUplinkPeakCdeBranch

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/0cdbdd1b-393c-bfe7-f7a5-fc27ad1e97ad.htm language=enus -->
## TOPIC 00004: rfmxevdodotnet/html/0cdbdd1b-393c-bfe7-f7a5-fc27ad1e97ad.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/0cdbdd1b-393c-bfe7-f7a5-fc27ad1e97ad.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/0cdbdd1b-393c-bfe7-f7a5-fc27ad1e97ad.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetUplinkPeakCde Method

RFmxEvdoMXModAccResultsGetUplinkPeakCde Method

Gets the peak uplink code domain error (CDE), expressed in dB.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkPeakCde(
	string selectorString,
	out double value
)
```

```text
Public Function GetUplinkPeakCde ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak uplink code domain error (CDE), expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsUplinkPeakCde

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/0e04431f-c12f-958d-e0d6-7291b6c1c962.htm language=enus -->
## TOPIC 00005: rfmxevdodotnet/html/0e04431f-c12f-958d-e0d6-7291b6c1c962.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/0e04431f-c12f-958d-e0d6-7291b6c1c962.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/0e04431f-c12f-958d-e0d6-7291b6c1c962.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.FetchUplinkDetectedChannel Method

RFmxEvdoMXModAccResultsFetchUplinkDetectedChannel Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUplinkDetectedChannel(
	string selectorString,
	double timeout,
	out int uplinkDetectedWalshCodeLength,
	out int uplinkDetectedWalshCodeNumber,
	out RFmxEvdoMXModAccUplinkDetectedBranch uplinkDetectedBranch
)
```

```text
Public Function FetchUplinkDetectedChannel ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef uplinkDetectedWalshCodeLength As Integer,
	<OutAttribute> ByRef uplinkDetectedWalshCodeNumber As Integer,
	<OutAttribute> ByRef uplinkDetectedBranch As RFmxEvdoMXModAccUplinkDetectedBranch
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and channel number. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **uplinkDetectedWalshCodeLength**
  - Type: SystemInt32 Upon return, contains the detected Walsh code length.
- **uplinkDetectedWalshCodeNumber**
  - Type: SystemInt32 Upon return, contains the detected Walsh code number.
- **uplinkDetectedBranch**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXModAccUplinkDetectedBranch Upon return, contains the detected branch.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/11d8f4de-38cc-fb0e-5e72-fa6538304051.htm language=enus -->
## TOPIC 00006: rfmxevdodotnet/html/11d8f4de-38cc-fb0e-5e72-fa6538304051.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/11d8f4de-38cc-fb0e-5e72-fa6538304051.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/11d8f4de-38cc-fb0e-5e72-fa6538304051.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.SetIQGainImbalanceRemovalEnabled Method

RFmxEvdoMXModAccConfigurationSetIQGainImbalanceRemovalEnabled Method

Sets whether to remove the I/Q gain imbalance before the EVM measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQGainImbalanceRemovalEnabled(
	string selectorString,
	RFmxEvdoMXModAccIQGainImbalanceRemovalEnabled value
)
```

```text
Public Function SetIQGainImbalanceRemovalEnabled ( 
	selectorString As String,
	value As RFmxEvdoMXModAccIQGainImbalanceRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXModAccIQGainImbalanceRemovalEnabledSpecifies whether to remove the I/Q gain imbalance before the EVM measurement.

###### Return Value

Int32

##### Remarks

ModAccIQGainImbalanceRemovalEnabled

False

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/126fea5c-b5da-9c29-8686-5bb5f27c29e8.htm language=enus -->
## TOPIC 00007: rfmxevdodotnet/html/126fea5c-b5da-9c29-8686-5bb5f27c29e8.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/126fea5c-b5da-9c29-8686-5bb5f27c29e8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/126fea5c-b5da-9c29-8686-5bb5f27c29e8.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureCarrierFrequencyArray Method

RFmxEvdoMXConfigureCarrierFrequencyArray Method

ConfigureFrequency(String, Double)

ConfigureNumberOfCarriers(String, Int32)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureCarrierFrequencyArray(
	string selectorString,
	double[] carrierFrequency
)
```

```text
Public Function ConfigureCarrierFrequencyArray ( 
	selectorString As String,
	carrierFrequency As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **carrierFrequency**
  - Type: SystemDouble Specifies the carrier frequency. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1498cfd1-5e67-a555-59e4-0d5fe74e153e.htm language=enus -->
## TOPIC 00008: rfmxevdodotnet/html/1498cfd1-5e67-a555-59e4-0d5fe74e153e.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1498cfd1-5e67-a555-59e4-0d5fe74e153e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1498cfd1-5e67-a555-59e4-0d5fe74e153e.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPower.Results Property

RFmxEvdoMXSlotPowerResults Property

RFmxEvdoMXSlotPowerResults

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxEvdoMXSlotPowerResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxEvdoMXSlotPowerResults
	Get
```

###### Property Value

RFmxEvdoMXSlotPowerResults

##### See Also

###### Reference

RFmxEvdoMXSlotPower Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/16c8ddce-4374-1d8d-be42-0ada099e795d.htm language=enus -->
## TOPIC 00009: rfmxevdodotnet/html/16c8ddce-4374-1d8d-be42-0ada099e795d.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/16c8ddce-4374-1d8d-be42-0ada099e795d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/16c8ddce-4374-1d8d-be42-0ada099e795d.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemConfiguration.GetAveragingType Method

RFmxEvdoMXSemConfigurationGetAveragingType Method

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingType(
	string selectorString,
	out RFmxEvdoMXSemAveragingType value
)
```

```text
Public Function GetAveragingType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXSemAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXSemAveragingTypeUpon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement.

###### Return Value

Int32

##### Remarks

SemAveragingType

Rms

##### See Also

###### Reference

RFmxEvdoMXSemConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1715880d-6681-7b12-3f8c-8b7ce98ef93f.htm language=enus -->
## TOPIC 00010: rfmxevdodotnet/html/1715880d-6681-7b12-3f8c-8b7ce98ef93f.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1715880d-6681-7b12-3f8c-8b7ce98ef93f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1715880d-6681-7b12-3f8c-8b7ce98ef93f.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.Commit Method

RFmxEvdoMXCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/19cd3ffe-d322-69cc-2dce-ac115af11144.htm language=enus -->
## TOPIC 00011: rfmxevdodotnet/html/19cd3ffe-d322-69cc-2dce-ac115af11144.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/19cd3ffe-d322-69cc-2dce-ac115af11144.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/19cd3ffe-d322-69cc-2dce-ac115af11144.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetAveragingCount Method

RFmxEvdoMXAcpConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxEvdoMXAcpAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxEvdoMXAcpAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

AcpAveragingCount

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1a9c50d3-c74e-b74c-53a6-6b2a3b2848d2.htm language=enus -->
## TOPIC 00012: rfmxevdodotnet/html/1a9c50d3-c74e-b74c-53a6-6b2a3b2848d2.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1a9c50d3-c74e-b74c-53a6-6b2a3b2848d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1a9c50d3-c74e-b74c-53a6-6b2a3b2848d2.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureNumberOfCarriers Method

RFmxEvdoMXConfigureNumberOfCarriers Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfCarriers(
	string selectorString,
	int numberOfCarriers
)
```

```text
Public Function ConfigureNumberOfCarriers ( 
	selectorString As String,
	numberOfCarriers As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **numberOfCarriers**
  - Type: SystemInt32Specifies the number of carriers in the signal.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1b09f22b-d4d8-8c31-d844-1dd7d6fc44e3.htm language=enus -->
## TOPIC 00013: rfmxevdodotnet/html/1b09f22b-d4d8-8c31-d844-1dd7d6fc44e3.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1b09f22b-d4d8-8c31-d844-1dd7d6fc44e3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1b09f22b-d4d8-8c31-d844-1dd7d6fc44e3.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetNearIFOutputPowerOffset Method

RFmxEvdoMXAcpConfigurationSetNearIFOutputPowerOffset Method

SetMeasurementMethod(String, RFmxEvdoMXAcpMeasurementMethod)

DynamicRange

SetIFOutputPowerOffsetAuto(String, RFmxEvdoMXAcpIFOutputPowerOffsetAuto)

False

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNearIFOutputPowerOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetNearIFOutputPowerOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(String, RFmxEvdoMXAcpIFOutputPowerOffsetAuto) method to False.

###### Return Value

Int32

##### Remarks

AcpNearIFOutputPowerOffset

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1d0f297b-636a-8567-d7b8-7243cfb59c84.htm language=enus -->
## TOPIC 00014: rfmxevdodotnet/html/1d0f297b-636a-8567-d7b8-7243cfb59c84.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1d0f297b-636a-8567-d7b8-7243cfb59c84.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1d0f297b-636a-8567-d7b8-7243cfb59c84.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaConfiguration.SetSynchronizationMode Method

RFmxEvdoMXCdaConfigurationSetSynchronizationMode Method

Sets whether the measurement is performed from the frame, slot, or symbol boundary.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSynchronizationMode(
	string selectorString,
	RFmxEvdoMXCdaSynchronizationMode value
)
```

```text
Public Function SetSynchronizationMode ( 
	selectorString As String,
	value As RFmxEvdoMXCdaSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXCdaSynchronizationModeSpecifies whether the measurement is performed from the frame, slot, or symbol boundary.

###### Return Value

Int32

##### Remarks

CdaSynchronizationMode

Slot

##### See Also

###### Reference

RFmxEvdoMXCdaConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1d48f2fc-da72-c0f4-2d1c-390996f7a279.htm language=enus -->
## TOPIC 00015: rfmxevdodotnet/html/1d48f2fc-da72-c0f4-2d1c-390996f7a279.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1d48f2fc-da72-c0f4-2d1c-390996f7a279.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1d48f2fc-da72-c0f4-2d1c-390996f7a279.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SetAttributeBool Method

RFmxEvdoMXSetAttributeBool Method

Sets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx EVDO Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemBooleanSpecifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/1e692557-e268-dc0e-a750-ebf90d36ad57.htm language=enus -->
## TOPIC 00016: rfmxevdodotnet/html/1e692557-e268-dc0e-a750-ebf90d36ad57.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/1e692557-e268-dc0e-a750-ebf90d36ad57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/1e692557-e268-dc0e-a750-ebf90d36ad57.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetRbwFilterBandwidth Method

RFmxEvdoMXAcpConfigurationGetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxEvdoMXAcpRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetRbwFilterBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxEvdoMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpRbwFilterBandwidth

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/2810d8ed-5ee1-9fc2-7ec6-cc4c09d9e342.htm language=enus -->
## TOPIC 00017: rfmxevdodotnet/html/2810d8ed-5ee1-9fc2-7ec6-cc4c09d9e342.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/2810d8ed-5ee1-9fc2-7ec6-cc4c09d9e342.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/2810d8ed-5ee1-9fc2-7ec6-cc4c09d9e342.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetTriggerDelay Method

RFmxEvdoMXGetTriggerDelay Method

Gets the trigger delay time. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/2a6f5ac8-07af-b2e1-03d9-8850dab3346e.htm language=enus -->
## TOPIC 00018: rfmxevdodotnet/html/2a6f5ac8-07af-b2e1-03d9-8850dab3346e.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/2a6f5ac8-07af-b2e1-03d9-8850dab3346e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/2a6f5ac8-07af-b2e1-03d9-8850dab3346e.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetOffsetFrequency Method

RFmxEvdoMXAcpConfigurationGetOffsetFrequency Method

Gets the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpOffsetFrequency

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/2c8c75cd-bb50-7acc-a1b7-ff56de2829c5.htm language=enus -->
## TOPIC 00019: rfmxevdodotnet/html/2c8c75cd-bb50-7acc-a1b7-ff56de2829c5.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/2c8c75cd-bb50-7acc-a1b7-ff56de2829c5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/2c8c75cd-bb50-7acc-a1b7-ff56de2829c5.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXUplinkBranch Enumeration

RFmxEvdoMXUplinkBranch Enumeration

SetChannelConfigurationMode(String, RFmxEvdoMXChannelConfigurationMode)

UserDefined

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXUplinkBranch
```

```text
Public Enumeration RFmxEvdoMXUplinkBranch
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | I | 0 | Specifies the in-phase component. |
|  | Q | 1 | Specifies the quadrature component. |
|  | IAndQ | 2 | Specifies both the in-phase component and the quadrature component. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/2c8d3c8a-5723-3c5c-6b0a-938d46d6df95.htm language=enus -->
## TOPIC 00020: rfmxevdodotnet/html/2c8d3c8a-5723-3c5c-6b0a-938d46d6df95.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/2c8d3c8a-5723-3c5c-6b0a-938d46d6df95.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/2c8d3c8a-5723-3c5c-6b0a-938d46d6df95.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SendSoftwareEdgeTrigger Method

RFmxEvdoMXSendSoftwareEdgeTrigger Method

1. You configure an invalid trigger.
2. You have not previously called the RFmxEvdoMX.Initiate method.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SendSoftwareEdgeTrigger()
```

```text
Public Function SendSoftwareEdgeTrigger As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/2d8e0b87-0da3-a636-6649-2cb2208545fe.htm language=enus -->
## TOPIC 00021: rfmxevdodotnet/html/2d8e0b87-0da3-a636-6649-2cb2208545fe.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/2d8e0b87-0da3-a636-6649-2cb2208545fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/2d8e0b87-0da3-a636-6649-2cb2208545fe.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaResults.GetUplinkIMeanActivePower Method

RFmxEvdoMXCdaResultsGetUplinkIMeanActivePower Method

Gets the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkIMeanActivePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUplinkIMeanActivePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit method to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

###### Return Value

Int32

##### Remarks

CdaResultsUplinkIMeanActivePower

##### See Also

###### Reference

RFmxEvdoMXCdaResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3015a78e-ecaa-2fa5-cd58-e8877b641c06.htm language=enus -->
## TOPIC 00022: rfmxevdodotnet/html/3015a78e-ecaa-2fa5-cd58-e8877b641c06.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3015a78e-ecaa-2fa5-cd58-e8877b641c06.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3015a78e-ecaa-2fa5-cd58-e8877b641c06.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.GetMeasurementOffset Method

RFmxEvdoMXModAccConfigurationGetMeasurementOffset Method

SetSynchronizationMode(String, RFmxEvdoMXModAccSynchronizationMode)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementOffset(
	string selectorString,
	out int value
)
```

```text
Public Function GetMeasurementOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32 Upon return, contains the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxEvdoMXModAccSynchronizationMode) method.

###### Return Value

Int32

##### Remarks

ModAccMeasurementOffset

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3583fa9f-22c8-af33-902d-0fb06f67b696.htm language=enus -->
## TOPIC 00023: rfmxevdodotnet/html/3583fa9f-22c8-af33-902d-0fb06f67b696.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3583fa9f-22c8-af33-902d-0fb06f67b696.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3583fa9f-22c8-af33-902d-0fb06f67b696.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpResults Methods

RFmxEvdoMXAcpResults Methods

The [RFmxEvdoMXAcpResults](7a8b4cac-5727-32e1-63aa-baa4b8915be2.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchAbsolutePowersTrace | Fetches the absolute powers trace for the adjacent channel power (ACP) measurement. |
|  | FetchCarrierMeasurement | Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier(n)" as the selector string to read results from this method. |
|  | FetchCarrierMeasurementArray | Returns the absolute and relative powers measured in the carrier channels. The relative powers are measured relative to the integrated power of the power reference carrier. |
|  | FetchOffsetMeasurement | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. Use "offset(n)" as the selector string to read results from this method. |
|  | FetchOffsetMeasurementArray | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. |
|  | FetchRelativePowersTrace | Fetches the relative powers trace for the adjacent channel power (ACP) measurement. |
|  | FetchSpectrum | Fetches the spectrum used for the adjacent channel power (ACP) measurement. |
|  | FetchTotalCarrierPower | Fetches the total carrier power measured by the adjacent channel power (ACP) measurement. |
|  | GetCarrierAbsolutePower | Gets the absolute measured carrier power. This value is expressed in dBm. Use "carrier(n)" as the selector string to read this method. |
|  | GetCarrierRelativePower | Gets the relative measured carrier power. This value is expressed in dB. Use "carrier(n)" as the selector string to read this method. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLowerOffsetAbsolutePower | Gets the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset(n)" as the selector string to read this method. |
|  | GetLowerOffsetRelativePower | Gets the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this method. |
|  | GetTotalCarrierPower | Gets the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUpperOffsetAbsolutePower | Gets the absolute measured upper offset channel power. This value is expressed in dBm. Use "offset(n)" as the selector string to read this method. |
|  | GetUpperOffsetRelativePower | Gets the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset(n)" as the selector string to read this method. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxEvdoMXAcpResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/394f2b46-7d36-6b78-1495-4ea9473206c7.htm language=enus -->
## TOPIC 00024: rfmxevdodotnet/html/394f2b46-7d36-6b78-1495-4ea9473206c7.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/394f2b46-7d36-6b78-1495-4ea9473206c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/394f2b46-7d36-6b78-1495-4ea9473206c7.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPhaseConfiguration.GetAllTracesEnabled Method

RFmxEvdoMXSlotPhaseConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces after performing the SlotPhase measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the traces after performing the SlotPhase measurement.

###### Return Value

Int32

##### Remarks

SlotPhaseAllTracesEnabled

##### See Also

###### Reference

RFmxEvdoMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3ad15cc8-7541-d65f-a9f4-8546b0be41e6.htm language=enus -->
## TOPIC 00025: rfmxevdodotnet/html/3ad15cc8-7541-d65f-a9f4-8546b0be41e6.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3ad15cc8-7541-d65f-a9f4-8546b0be41e6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3ad15cc8-7541-d65f-a9f4-8546b0be41e6.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCda.Results Property

RFmxEvdoMXCdaResults Property

RFmxEvdoMXCdaResults

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxEvdoMXCdaResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxEvdoMXCdaResults
	Get
```

###### Property Value

RFmxEvdoMXCdaResults

##### See Also

###### Reference

RFmxEvdoMXCda Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3b56752d-77d8-acc2-a448-87fb6aa7f43b.htm language=enus -->
## TOPIC 00026: rfmxevdodotnet/html/3b56752d-77d8-acc2-a448-87fb6aa7f43b.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3b56752d-77d8-acc2-a448-87fb6aa7f43b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3b56752d-77d8-acc2-a448-87fb6aa7f43b.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetOffsetPowerReferenceCarrier Method

RFmxEvdoMXAcpConfigurationSetOffsetPowerReferenceCarrier Method

Sets the carrier number that is used as the power reference to measure the offset channel relative power.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetPowerReferenceCarrier(
	string selectorString,
	RFmxEvdoMXAcpOffsetPowerReferenceCarrier value
)
```

```text
Public Function SetOffsetPowerReferenceCarrier ( 
	selectorString As String,
	value As RFmxEvdoMXAcpOffsetPowerReferenceCarrier
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpOffsetPowerReferenceCarrierSpecifies the carrier number that is used as the power reference to measure the offset channel relative power.

###### Return Value

Int32

##### Remarks

AcpOffsetPowerReferenceCarrier

Composite

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3b61c871-11bc-fd54-7e20-1fae9d1db3fc.htm language=enus -->
## TOPIC 00027: rfmxevdodotnet/html/3b61c871-11bc-fd54-7e20-1fae9d1db3fc.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3b61c871-11bc-fd54-7e20-1fae9d1db3fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3b61c871-11bc-fd54-7e20-1fae9d1db3fc.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXConstants.PxiStarLine Field

RFmxEvdoMXConstantsPxiStarLine Field

The signal is exported to the PXI star trigger line.

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMXConstants Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3b713b0c-c22d-30c8-3355-8dab14994b7e.htm language=enus -->
## TOPIC 00028: rfmxevdodotnet/html/3b713b0c-c22d-30c8-3355-8dab14994b7e.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3b713b0c-c22d-30c8-3355-8dab14994b7e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3b713b0c-c22d-30c8-3355-8dab14994b7e.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetUplinkBranch Method

RFmxEvdoMXGetUplinkBranch Method

SetChannelConfigurationMode(String, RFmxEvdoMXChannelConfigurationMode)

UserDefined

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkBranch(
	string selectorString,
	out RFmxEvdoMXUplinkBranch value
)
```

```text
Public Function GetUplinkBranch ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXUplinkBranch
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the channel number. Example: "channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXUplinkBranch Upon return, contains the quadrature branch on which a specific user defined-channel is mapped. This method is used only when you set the SetChannelConfigurationMode(String, RFmxEvdoMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the Selector Strings to configure or read this method.

###### Return Value

Int32

##### Remarks

UplinkBranch

I

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3bfea774-1be7-a25e-e624-69429d27d471.htm language=enus -->
## TOPIC 00029: rfmxevdodotnet/html/3bfea774-1be7-a25e-e624-69429d27d471.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3bfea774-1be7-a25e-e624-69429d27d471.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3bfea774-1be7-a25e-e624-69429d27d471.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetCarrierIntegrationBandwidth Method

RFmxEvdoMXAcpConfigurationGetCarrierIntegrationBandwidth Method

Gets the ACP carrier integration bandwidth. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemString Specifies the carrier number. Example: "carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the ACP carrier integration bandwidth. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpCarrierIntegrationBandwidth

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3c7728e9-6a2c-22a4-b4cc-5866555f497a.htm language=enus -->
## TOPIC 00030: rfmxevdodotnet/html/3c7728e9-6a2c-22a4-b4cc-5866555f497a.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3c7728e9-6a2c-22a4-b4cc-5866555f497a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3c7728e9-6a2c-22a4-b4cc-5866555f497a.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetReferenceLevel Method

RFmxEvdoMXGetReferenceLevel Method

pk-pk

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemDouble Upon return, contains the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### Remarks

ReferenceLevel

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3d6da061-b740-9655-bb01-c660ae9752fa.htm language=enus -->
## TOPIC 00031: rfmxevdodotnet/html/3d6da061-b740-9655-bb01-c660ae9752fa.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3d6da061-b740-9655-bb01-c660ae9752fa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3d6da061-b740-9655-bb01-c660ae9752fa.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetUplinkPeakEvm Method

RFmxEvdoMXModAccResultsGetUplinkPeakEvm Method

Gets the peak value of the uplink error vector magnitude (EVM), averaged over all measured slots. This value isexpressed as a percentage.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkPeakEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetUplinkPeakEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the peak value of the uplink error vector magnitude (EVM), averaged over all measured slots. This value isexpressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsUplinkPeakEvm

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/3d810871-0722-280e-908f-6ff0a3ae047f.htm language=enus -->
## TOPIC 00032: rfmxevdodotnet/html/3d810871-0722-280e-908f-6ff0a3ae047f.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/3d810871-0722-280e-908f-6ff0a3ae047f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/3d810871-0722-280e-908f-6ff0a3ae047f.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetBandClass Method

RFmxEvdoMXGetBandClass Method

Gets the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBandClass(
	string selectorString,
	out int value
)
```

```text
Public Function GetBandClass ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0.

###### Return Value

Int32

##### Remarks

BandClass

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/411ee396-5d79-1ecf-374d-b9b8bb3f8256.htm language=enus -->
## TOPIC 00033: rfmxevdodotnet/html/411ee396-5d79-1ecf-374d-b9b8bb3f8256.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/411ee396-5d79-1ecf-374d-b9b8bb3f8256.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/411ee396-5d79-1ecf-374d-b9b8bb3f8256.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetLimitedConfigurationChange Method

RFmxEvdoMXGetLimitedConfigurationChange Method

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLimitedConfigurationChange(
	string selectorString,
	out RFmxEvdoMXLimitedConfigurationChange value
)
```

```text
Public Function GetLimitedConfigurationChange ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXLimitedConfigurationChangeUpon return, contains the set of properties that are considered by RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

LimitedConfigurationChange

Disabled

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/417a6f43-0f07-3719-d970-d1fdca24f85f.htm language=enus -->
## TOPIC 00034: rfmxevdodotnet/html/417a6f43-0f07-3719-d970-d1fdca24f85f.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/417a6f43-0f07-3719-d970-d1fdca24f85f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/417a6f43-0f07-3719-d970-d1fdca24f85f.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemResults.FetchCarrierMeasurement Method

RFmxEvdoMXSemResultsFetchCarrierMeasurement Method

"carrier(n)"

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurement(
	string selectorString,
	double timeout,
	out double absoluteIntegratedPower,
	out double relativeIntegratedPower
)
```

```text
Public Function FetchCarrierMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef absoluteIntegratedPower As Double,
	<OutAttribute> ByRef relativeIntegratedPower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and carrier number. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absoluteIntegratedPower**
  - Type: SystemDouble Upon return, contains absolute power of the selected carrier. This value is expressed in dBm.
- **relativeIntegratedPower**
  - Type: SystemDouble Upon return, contains the relative power of the selected carrier. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXSemResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/41d818ca-492a-2e6b-d07e-e83c6676aa28.htm language=enus -->
## TOPIC 00035: rfmxevdodotnet/html/41d818ca-492a-2e6b-d07e-e83c6676aa28.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/41d818ca-492a-2e6b-d07e-e83c6676aa28.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/41d818ca-492a-2e6b-d07e-e83c6676aa28.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SetAttributeInt Method

RFmxEvdoMXSetAttributeInt Method

Sets the value of a Int attribute.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeInt(
	string selectorString,
	int attributeIdentifier,
	int value
)
```

```text
Public Function SetAttributeInt ( 
	selectorString As String,
	attributeIdentifier As Integer,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx EVDO Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt32Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/42221b83-f5aa-06e2-2afa-57de9c1dca8b.htm language=enus -->
## TOPIC 00036: rfmxevdodotnet/html/42221b83-f5aa-06e2-2afa-57de9c1dca8b.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/42221b83-f5aa-06e2-2afa-57de9c1dca8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/42221b83-f5aa-06e2-2afa-57de9c1dca8b.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaResults.FetchUplinkSymbolEvmTrace Method

RFmxEvdoMXCdaResultsFetchUplinkSymbolEvmTrace Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUplinkSymbolEvmTrace(
	string selectorString,
	double timeout,
	ref float[] symbolEvm
)
```

```text
Public Function FetchUplinkSymbolEvmTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef symbolEvm As Single()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **symbolEvm**
  - Type: SystemSingle Upon return, contains the trace of symbol EVM. This value is expressed as a percentage.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXCdaResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/44116ccf-2b79-3bae-ae6d-506992b52499.htm language=enus -->
## TOPIC 00037: rfmxevdodotnet/html/44116ccf-2b79-3bae-ae6d-506992b52499.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/44116ccf-2b79-3bae-ae6d-506992b52499.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/44116ccf-2b79-3bae-ae6d-506992b52499.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXObwResults.FetchMeasurement Method

RFmxEvdoMXObwResultsFetchMeasurement Method

Namespace:

NationalInstruments.RFmx.EvdoMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **occupiedBandwidth**
  - Type: SystemDouble Upon return, contains the occupied bandwidth. This value is expressed in Hz.
- **absolutePower**
  - Type: SystemDouble Upon return, contains the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm.
- **startFrequency**
  - Type: SystemDouble Upon return, contains the start frequency of the OBW. This value is expressed in Hz.
- **stopFrequency**
  - Type: SystemDouble Upon return, contains the stop frequency of the OBW. This value is expressed in Hz.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXObwResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/448ab9f3-0a7c-f8a1-2f4e-09cbc6cccb02.htm language=enus -->
## TOPIC 00038: rfmxevdodotnet/html/448ab9f3-0a7c-f8a1-2f4e-09cbc6cccb02.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/448ab9f3-0a7c-f8a1-2f4e-09cbc6cccb02.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/448ab9f3-0a7c-f8a1-2f4e-09cbc6cccb02.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureDigitalEdgeTrigger Method

RFmxEvdoMXConfigureDigitalEdgeTrigger Method

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureDigitalEdgeTrigger(
	string selectorString,
	string digitalEdgeTriggerSource,
	RFmxEvdoMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge,
	double triggerDelay,
	bool enableTrigger
)
```

```text
Public Function ConfigureDigitalEdgeTrigger ( 
	selectorString As String,
	digitalEdgeTriggerSource As String,
	digitalEdgeTriggerEdge As RFmxEvdoMXDigitalEdgeTriggerEdge,
	triggerDelay As Double,
	enableTrigger As Boolean
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **digitalEdgeTriggerSource**
  - Type: SystemString Specifies the source terminal for the digital-edge trigger. Use the string constants from RFmxEvdoMXConstants class or any other valid string to configure this parameter.
- **digitalEdgeTriggerEdge**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXDigitalEdgeTriggerEdgeSpecifies the trigger edge to detect.
- **triggerDelay**
  - Type: SystemDouble Specifies the trigger delay time. This value is expressed in seconds.
- **enableTrigger**
  - Type: SystemBoolean Specifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/4667e6fa-6339-6e3f-3610-398ce33be231.htm language=enus -->
## TOPIC 00039: rfmxevdodotnet/html/4667e6fa-6339-6e3f-3610-398ce33be231.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/4667e6fa-6339-6e3f-3610-398ce33be231.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/4667e6fa-6339-6e3f-3610-398ce33be231.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPowerResults Methods

RFmxEvdoMXSlotPowerResults Methods

The [RFmxEvdoMXSlotPowerResults](447762db-92c5-e0e0-6338-3c8768aea31b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchPowers | Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxEvdoMXSlotPowerResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/4669df6d-4616-99cc-74df-e936a067f348.htm language=enus -->
## TOPIC 00040: rfmxevdodotnet/html/4669df6d-4616-99cc-74df-e936a067f348.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/4669df6d-4616-99cc-74df-e936a067f348.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/4669df6d-4616-99cc-74df-e936a067f348.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemResults.GetCompositeMeasurementStatus Method

RFmxEvdoMXSemResultsGetCompositeMeasurementStatus Method

Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCompositeMeasurementStatus(
	string selectorString,
	out RFmxEvdoMXSemCompositeMeasurementStatus value
)
```

```text
Public Function GetCompositeMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXSemCompositeMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXSemCompositeMeasurementStatusIndicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment.

###### Return Value

Int32

##### Remarks

SemResultsCompositeMeasurementStatus

##### See Also

###### Reference

RFmxEvdoMXSemResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/46bee95c-0148-bd1a-bc2f-be8c8b6cc7aa.htm language=enus -->
## TOPIC 00041: rfmxevdodotnet/html/46bee95c-0148-bd1a-bc2f-be8c8b6cc7aa.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/46bee95c-0148-bd1a-bc2f-be8c8b6cc7aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/46bee95c-0148-bd1a-bc2f-be8c8b6cc7aa.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SetTriggerMinimumQuietTimeMode Method

RFmxEvdoMXSetTriggerMinimumQuietTimeMode Method

Sets whether the measurement computes the minimum quiet time used for triggering.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerMinimumQuietTimeMode(
	string selectorString,
	RFmxEvdoMXTriggerMinimumQuietTimeMode value
)
```

```text
Public Function SetTriggerMinimumQuietTimeMode ( 
	selectorString As String,
	value As RFmxEvdoMXTriggerMinimumQuietTimeMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXTriggerMinimumQuietTimeModeSpecifies whether the measurement computes the minimum quiet time used for triggering.

###### Return Value

Int32

##### Remarks

TriggerMinimumQuietTimeMode

Auto

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/46e806ed-7414-39a6-7b4d-5a5cf76d8c36.htm language=enus -->
## TOPIC 00042: rfmxevdodotnet/html/46e806ed-7414-39a6-7b4d-5a5cf76d8c36.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/46e806ed-7414-39a6-7b4d-5a5cf76d8c36.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/46e806ed-7414-39a6-7b4d-5a5cf76d8c36.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcp Class

RFmxEvdoMXAcp Class

Represents the ACP measurement.

##### Inheritance Hierarchy

RFmxEvdoMXSubObject

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxEvdoMXAcp : RFmxEvdoMXSubObject
```

```text
Public NotInheritable Class RFmxEvdoMXAcp
	Inherits RFmxEvdoMXSubObject
```

The RFmxEvdoMXAcp type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxEvdoMXAcpConfiguration instance that provides methods to configure the ACP measurement |
|  | Results | Gets the RFmxEvdoMXAcpResults instance that provides methods to fetch and read the ACP measurement results. |

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

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/47727d32-2c8e-0711-654b-8b025e194edc.htm language=enus -->
## TOPIC 00043: rfmxevdodotnet/html/47727d32-2c8e-0711-654b-8b025e194edc.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/47727d32-2c8e-0711-654b-8b025e194edc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/47727d32-2c8e-0711-654b-8b025e194edc.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCda.Configuration Property

RFmxEvdoMXCdaConfiguration Property

RFmxEvdoMXCdaConfiguration

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxEvdoMXCdaConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxEvdoMXCdaConfiguration
	Get
```

###### Property Value

RFmxEvdoMXCdaConfiguration

##### See Also

###### Reference

RFmxEvdoMXCda Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/4e209b3b-ab7d-1067-8ac3-5863c52617b1.htm language=enus -->
## TOPIC 00044: rfmxevdodotnet/html/4e209b3b-ab7d-1067-8ac3-5863c52617b1.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/4e209b3b-ab7d-1067-8ac3-5863c52617b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/4e209b3b-ab7d-1067-8ac3-5863c52617b1.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.ConfigureMeasurementMethod Method

RFmxEvdoMXAcpConfigurationConfigureMeasurementMethod Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementMethod(
	string selectorString,
	RFmxEvdoMXAcpMeasurementMethod measurementMethod
)
```

```text
Public Function ConfigureMeasurementMethod ( 
	selectorString As String,
	measurementMethod As RFmxEvdoMXAcpMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementMethod**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpMeasurementMethodSpecifies the method for performing the ACP measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/4f4e0b1d-e46e-945a-7925-a6beae1bcc32.htm language=enus -->
## TOPIC 00045: rfmxevdodotnet/html/4f4e0b1d-e46e-945a-7925-a6beae1bcc32.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/4f4e0b1d-e46e-945a-7925-a6beae1bcc32.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/4f4e0b1d-e46e-945a-7925-a6beae1bcc32.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureSoftwareEdgeTrigger Method

RFmxEvdoMXConfigureSoftwareEdgeTrigger Method

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/4ffdee24-ee3e-994f-8561-5248125f2404.htm language=enus -->
## TOPIC 00046: rfmxevdodotnet/html/4ffdee24-ee3e-994f-8561-5248125f2404.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/4ffdee24-ee3e-994f-8561-5248125f2404.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/4ffdee24-ee3e-994f-8561-5248125f2404.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaConfiguration.GetUplinkWalshCodeNumber Method

RFmxEvdoMXCdaConfigurationGetUplinkWalshCodeNumber Method

Gets the Walsh code number of the channel, subject to channel-specific analysis.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkWalshCodeNumber(
	string selectorString,
	out int value
)
```

```text
Public Function GetUplinkWalshCodeNumber ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the Walsh code number of the channel, subject to channel-specific analysis.

###### Return Value

Int32

##### Remarks

CdaUplinkWalshCodeNumber

##### See Also

###### Reference

RFmxEvdoMXCdaConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/51141ed2-076f-e821-3512-b1ca3e918850.htm language=enus -->
## TOPIC 00047: rfmxevdodotnet/html/51141ed2-076f-e821-3512-b1ca3e918850.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/51141ed2-076f-e821-3512-b1ca3e918850.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/51141ed2-076f-e821-3512-b1ca3e918850.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccUplinkPeakCdeBranch Enumeration

RFmxEvdoMXModAccUplinkPeakCdeBranch Enumeration

Returns the branch of the channel corresponding to the Peak Active CDE (dB) method result.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXModAccUplinkPeakCdeBranch
```

```text
Public Enumeration RFmxEvdoMXModAccUplinkPeakCdeBranch
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | I | 0 | Returns the in-phase branch of the peak CDE. |
|  | Q | 1 | Returns the quadrature branch of the peak CDE. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5458c0fa-54d2-1aed-d552-350f346ff848.htm language=enus -->
## TOPIC 00048: rfmxevdodotnet/html/5458c0fa-54d2-1aed-d552-350f346ff848.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5458c0fa-54d2-1aed-d552-350f346ff848.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5458c0fa-54d2-1aed-d552-350f346ff848.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXObw Properties

RFmxEvdoMXObw Properties

The [RFmxEvdoMXObw](daa4cb90-5b64-e6a9-9380-ccc18952227b.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxEvdoMXObwConfiguration instance that provides methods to configure the OBW measurement |
|  | Results | Gets the RFmxEvdoMXObwResults instance that provides methods to fetch and read the OBW measurement results. |

Top

##### See Also

###### Reference

RFmxEvdoMXObw Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/549a91b6-0cd7-d904-cf2f-6e96f1a6b09a.htm language=enus -->
## TOPIC 00049: rfmxevdodotnet/html/549a91b6-0cd7-d904-cf2f-6e96f1a6b09a.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/549a91b6-0cd7-d904-cf2f-6e96f1a6b09a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/549a91b6-0cd7-d904-cf2f-6e96f1a6b09a.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemResults.GetLowerOffsetAbsoluteIntegratedPower Method

RFmxEvdoMXSemResultsGetLowerOffsetAbsoluteIntegratedPower Method

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetAbsoluteIntegratedPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetAbsoluteIntegratedPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset(n)" as the selector string to read this method.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetAbsoluteIntegratedPower

##### See Also

###### Reference

RFmxEvdoMXSemResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/549b3feb-f336-b906-329e-f31c2c185711.htm language=enus -->
## TOPIC 00050: rfmxevdodotnet/html/549b3feb-f336-b906-329e-f31c2c185711.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/549b3feb-f336-b906-329e-f31c2c185711.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/549b3feb-f336-b906-329e-f31c2c185711.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetRbwFilterAutoBandwidth Method

RFmxEvdoMXAcpConfigurationSetRbwFilterAutoBandwidth Method

Sets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAutoBandwidth(
	string selectorString,
	RFmxEvdoMXAcpRbwAutoBandwidth value
)
```

```text
Public Function SetRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxEvdoMXAcpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpRbwAutoBandwidthSpecifies whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

AcpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/58b57c31-b655-887a-9829-9d56dd0cb0fb.htm language=enus -->
## TOPIC 00051: rfmxevdodotnet/html/58b57c31-b655-887a-9829-9d56dd0cb0fb.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/58b57c31-b655-887a-9829-9d56dd0cb0fb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/58b57c31-b655-887a-9829-9d56dd0cb0fb.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemResults.GetLowerOffsetMargin Method

RFmxEvdoMXSemResultsGetLowerOffsetMargin Method

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemDouble Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset(n)" as the selector string to read this method.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetMargin

##### See Also

###### Reference

RFmxEvdoMXSemResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/58e9cd6e-78a5-668a-c0b1-4518bbf55f2f.htm language=enus -->
## TOPIC 00052: rfmxevdodotnet/html/58e9cd6e-78a5-668a-c0b1-4518bbf55f2f.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/58e9cd6e-78a5-668a-c0b1-4518bbf55f2f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/58e9cd6e-78a5-668a-c0b1-4518bbf55f2f.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemConfiguration.GetOffsetBandwidthIntegral Method

RFmxEvdoMXSemConfigurationGetOffsetBandwidthIntegral Method

Gets the bandwidth integral for a specific offset segment.

Namespace:

NationalInstruments.RFmx.EvdoMX

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

- **selectorString**
  - Type: SystemString Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the bandwidth integral for a specific offset segment.

###### Return Value

Int32

##### Remarks

SemOffsetBandwidthIntegral

##### See Also

###### Reference

RFmxEvdoMXSemConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/59844c9b-384d-ef9b-af58-385cbe149a49.htm language=enus -->
## TOPIC 00053: rfmxevdodotnet/html/59844c9b-384d-ef9b-af58-385cbe149a49.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/59844c9b-384d-ef9b-af58-385cbe149a49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/59844c9b-384d-ef9b-af58-385cbe149a49.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpResults.GetCarrierAbsolutePower Method

RFmxEvdoMXAcpResultsGetCarrierAbsolutePower Method

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemString Specifies the result name and Carrier number. Example: "Carrier0", "result::r1/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the absolute measured carrier power. This value is expressed in dBm. Use "carrier(n)" as the selector string to read this method.

###### Return Value

Int32

##### Remarks

AcpResultsCarrierAbsolutePower

##### See Also

###### Reference

RFmxEvdoMXAcpResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/59b994da-1ec6-cc1f-6bda-dd61610c87fe.htm language=enus -->
## TOPIC 00054: rfmxevdodotnet/html/59b994da-1ec6-cc1f-6bda-dd61610c87fe.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/59b994da-1ec6-cc1f-6bda-dd61610c87fe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/59b994da-1ec6-cc1f-6bda-dd61610c87fe.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaIQQuadratureErrorRemovalEnabled Enumeration

RFmxEvdoMXCdaIQQuadratureErrorRemovalEnabled Enumeration

Specifies whether to remove the I/Q quadrature error before the CDA measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXCdaIQQuadratureErrorRemovalEnabled
```

```text
Public Enumeration RFmxEvdoMXCdaIQQuadratureErrorRemovalEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The I/Q quadrature error is not removed before the CDA measurement. |
|  | True | 1 | The I/Q quadrature error is removed before the CDA measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/59d5c54e-7d3d-2218-46ad-d4ce01b7cb1b.htm language=enus -->
## TOPIC 00055: rfmxevdodotnet/html/59d5c54e-7d3d-2218-46ad-d4ce01b7cb1b.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/59d5c54e-7d3d-2218-46ad-d4ce01b7cb1b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/59d5c54e-7d3d-2218-46ad-d4ce01b7cb1b.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXChpResults.FetchSpectrum Method

RFmxEvdoMXChpResultsFetchSpectrum Method

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: NationalInstrumentsSpectrumSingle Upon return, contains the trace of power levels in the spectral domain.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXChpResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5a03b081-e05f-5780-708f-5cf5fccc7623.htm language=enus -->
## TOPIC 00056: rfmxevdodotnet/html/5a03b081-e05f-5780-708f-5cf5fccc7623.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5a03b081-e05f-5780-708f-5cf5fccc7623.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5a03b081-e05f-5780-708f-5cf5fccc7623.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPhase Methods

RFmxEvdoMXSlotPhase Methods

The [RFmxEvdoMXSlotPhase](ba03d12e-255e-ba21-fa1a-d8f6901a4d22.htm) type exposes the following members.

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

RFmxEvdoMXSlotPhase Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5a7b36e3-fe18-ba70-54c4-36dd63bfd124.htm language=enus -->
## TOPIC 00057: rfmxevdodotnet/html/5a7b36e3-fe18-ba70-54c4-36dd63bfd124.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5a7b36e3-fe18-ba70-54c4-36dd63bfd124.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5a7b36e3-fe18-ba70-54c4-36dd63bfd124.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetNearIFOutputPowerOffset Method

RFmxEvdoMXAcpConfigurationGetNearIFOutputPowerOffset Method

SetMeasurementMethod(String, RFmxEvdoMXAcpMeasurementMethod)

DynamicRange

SetIFOutputPowerOffsetAuto(String, RFmxEvdoMXAcpIFOutputPowerOffsetAuto)

False

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNearIFOutputPowerOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetNearIFOutputPowerOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(String, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(String, RFmxEvdoMXAcpIFOutputPowerOffsetAuto) method to False.

###### Return Value

Int32

##### Remarks

AcpNearIFOutputPowerOffset

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5b037cc1-f13e-52a2-ba6a-813de019f617.htm language=enus -->
## TOPIC 00058: rfmxevdodotnet/html/5b037cc1-f13e-52a2-ba6a-813de019f617.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5b037cc1-f13e-52a2-ba6a-813de019f617.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5b037cc1-f13e-52a2-ba6a-813de019f617.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPhaseConfiguration.GetSynchronizationMode Method

RFmxEvdoMXSlotPhaseConfigurationGetSynchronizationMode Method

Gets whether the measurement is performed from the frame or the slot boundary.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSynchronizationMode(
	string selectorString,
	out RFmxEvdoMXSlotPhaseSynchronizationMode value
)
```

```text
Public Function GetSynchronizationMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXSlotPhaseSynchronizationMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXSlotPhaseSynchronizationModeUpon return, contains whether the measurement is performed from the frame or the slot boundary.

###### Return Value

Int32

##### Remarks

SlotPhaseSynchronizationMode

Frame

##### See Also

###### Reference

RFmxEvdoMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5b90ced0-22ff-dedd-a20e-def4ce98956b.htm language=enus -->
## TOPIC 00059: rfmxevdodotnet/html/5b90ced0-22ff-dedd-a20e-def4ce98956b.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5b90ced0-22ff-dedd-a20e-def4ce98956b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5b90ced0-22ff-dedd-a20e-def4ce98956b.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.AutoLevel Method

RFmxEvdoMXAutoLevel Method

SetReferenceLevel(String, Double)

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

SetAutoLevelInitialReferenceLevel(String, Double)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int AutoLevel(
	string selectorString,
	double measurementInterval,
	out double referenceLevel
)
```

```text
Public Function AutoLevel ( 
	selectorString As String,
	measurementInterval As Double,
	<OutAttribute> ByRef referenceLevel As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementInterval**
  - Type: SystemDouble Specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the RF signal analyzer. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal.
- **referenceLevel**
  - Type: SystemDouble Upon return, contains the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5c22975c-e6e3-205b-1c0a-ae2662ac7b9c.htm language=enus -->
## TOPIC 00060: rfmxevdodotnet/html/5c22975c-e6e3-205b-1c0a-ae2662ac7b9c.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5c22975c-e6e3-205b-1c0a-ae2662ac7b9c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5c22975c-e6e3-205b-1c0a-ae2662ac7b9c.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SetUplinkDataModulationType Method

RFmxEvdoMXSetUplinkDataModulationType Method

SetChannelConfigurationMode(String, RFmxEvdoMXChannelConfigurationMode)

UserDefined

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetUplinkDataModulationType(
	string selectorString,
	RFmxEvdoMXUplinkDataModulationType value
)
```

```text
Public Function SetUplinkDataModulationType ( 
	selectorString As String,
	value As RFmxEvdoMXUplinkDataModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXUplinkDataModulationType Defines the modulation of the data channel. This method is used only when you set the SetChannelConfigurationMode(String, RFmxEvdoMXChannelConfigurationMode) method to UserDefined.

###### Return Value

Int32

##### Remarks

UplinkDataModulationType

Auto

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5d35ec91-8ac7-492c-1d94-3cb2e589e33c.htm language=enus -->
## TOPIC 00061: rfmxevdodotnet/html/5d35ec91-8ac7-492c-1d94-3cb2e589e33c.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5d35ec91-8ac7-492c-1d94-3cb2e589e33c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5d35ec91-8ac7-492c-1d94-3cb2e589e33c.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPhaseConfiguration.SetTransientDuration Method

RFmxEvdoMXSlotPhaseConfigurationSetTransientDuration Method

Sets the transient duration for the SlotPhase measurement. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTransientDuration(
	string selectorString,
	double value
)
```

```text
Public Function SetTransientDuration ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the transient duration for the SlotPhase measurement. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SlotPhaseTransientDuration

##### See Also

###### Reference

RFmxEvdoMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5da16890-b2ea-ad6d-9b94-ccbd8fbe258d.htm language=enus -->
## TOPIC 00062: rfmxevdodotnet/html/5da16890-b2ea-ad6d-9b94-ccbd8fbe258d.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5da16890-b2ea-ad6d-9b94-ccbd8fbe258d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5da16890-b2ea-ad6d-9b94-ccbd8fbe258d.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaSynchronizationMode Enumeration

RFmxEvdoMXCdaSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXCdaSynchronizationMode
```

```text
Public Enumeration RFmxEvdoMXCdaSynchronizationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SetMeasurementLength(String, Int32) method starting at SetMeasurementOffset(String, Int32) slots from the frame boundary. |
|  | Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. |
|  | Arbitrary | 2 | The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length method, starting at CDA Meas Offset slots from the symbol boundary. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5e6c9407-f21c-2c50-7c82-2cd69e5cb9ee.htm language=enus -->
## TOPIC 00063: rfmxevdodotnet/html/5e6c9407-f21c-2c50-7c82-2cd69e5cb9ee.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5e6c9407-f21c-2c50-7c82-2cd69e5cb9ee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5e6c9407-f21c-2c50-7c82-2cd69e5cb9ee.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetUplinkRmsEvm Method

RFmxEvdoMXModAccResultsGetUplinkRmsEvm Method

Gets the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. Thisvalue is expressed as a percentage.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkRmsEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetUplinkRmsEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. Thisvalue is expressed as a percentage.

###### Return Value

Int32

##### Remarks

ModAccResultsUplinkRmsEvm

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5e972737-a857-3443-d0b7-ac75a9deaa42.htm language=enus -->
## TOPIC 00064: rfmxevdodotnet/html/5e972737-a857-3443-d0b7-ac75a9deaa42.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5e972737-a857-3443-d0b7-ac75a9deaa42.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5e972737-a857-3443-d0b7-ac75a9deaa42.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcp Properties

RFmxEvdoMXAcp Properties

The [RFmxEvdoMXAcp](46e806ed-7414-39a6-7b4d-5a5cf76d8c36.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxEvdoMXAcpConfiguration instance that provides methods to configure the ACP measurement |
|  | Results | Gets the RFmxEvdoMXAcpResults instance that provides methods to fetch and read the ACP measurement results. |

Top

##### See Also

###### Reference

RFmxEvdoMXAcp Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/5f792013-9fbd-4864-8dc3-c7ca90cad1d9.htm language=enus -->
## TOPIC 00065: rfmxevdodotnet/html/5f792013-9fbd-4864-8dc3-c7ca90cad1d9.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/5f792013-9fbd-4864-8dc3-c7ca90cad1d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/5f792013-9fbd-4864-8dc3-c7ca90cad1d9.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.DeleteSignalConfiguration Method

RFmxEvdoMXDeleteSignalConfiguration Method

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/608c50b9-608d-04fb-71ff-2558e62cee78.htm language=enus -->
## TOPIC 00066: rfmxevdodotnet/html/608c50b9-608d-04fb-71ff-2558e62cee78.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/608c50b9-608d-04fb-71ff-2558e62cee78.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/608c50b9-608d-04fb-71ff-2558e62cee78.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXPhysicalLayerSubtype Enumeration

RFmxEvdoMXPhysicalLayerSubtype Enumeration

Selects the EV-DO physical layer subtype.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXPhysicalLayerSubtype
```

```text
Public Enumeration RFmxEvdoMXPhysicalLayerSubtype
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Subtype0_1 | 0 | Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. |
|  | Subtype2 | 1 | Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. |
|  | Subtype3 | 2 | Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/60b4629d-b1d0-fd9f-ae18-183dcb04dc42.htm language=enus -->
## TOPIC 00067: rfmxevdodotnet/html/60b4629d-b1d0-fd9f-ae18-183dcb04dc42.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/60b4629d-b1d0-fd9f-ae18-183dcb04dc42.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/60b4629d-b1d0-fd9f-ae18-183dcb04dc42.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.FetchConstellationTrace Method

RFmxEvdoMXModAccResultsFetchConstellationTrace Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchConstellationTrace(
	string selectorString,
	double timeout,
	ref ComplexSingle[] constellation
)
```

```text
Public Function FetchConstellationTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef constellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **constellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/61aebc9a-a21e-5821-68a4-912d81c303ca.htm language=enus -->
## TOPIC 00068: rfmxevdodotnet/html/61aebc9a-a21e-5821-68a4-912d81c303ca.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/61aebc9a-a21e-5821-68a4-912d81c303ca.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/61aebc9a-a21e-5821-68a4-912d81c303ca.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetIQPowerEdgeTriggerLevel Method

RFmxEvdoMXGetIQPowerEdgeTriggerLevel Method

SetIQPowerEdgeTriggerLevelType(String, RFmxEvdoMXIQPowerEdgeTriggerLevelType)

Relative

Absolute

SetTriggerType(String, RFmxEvdoMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.EvdoMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the power level at which the device triggers. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(String, RFmxEvdoMXIQPowerEdgeTriggerLevelType) method is set to Relative and in dBm when the IQ Power Edge Level Type method is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxEvdoMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevel

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/674747a4-776b-7eae-b84d-53bc7d38eb37.htm language=enus -->
## TOPIC 00069: rfmxevdodotnet/html/674747a4-776b-7eae-b84d-53bc7d38eb37.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/674747a4-776b-7eae-b84d-53bc7d38eb37.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/674747a4-776b-7eae-b84d-53bc7d38eb37.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetSweepTimeAuto Method

RFmxEvdoMXAcpConfigurationGetSweepTimeAuto Method

Gets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxEvdoMXAcpSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXAcpSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpSweepTimeAutoUpon return, contains whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

AcpSweepTimeAuto

True

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/67cbe9c4-c51d-5da3-d4c0-d1586bded181.htm language=enus -->
## TOPIC 00070: rfmxevdodotnet/html/67cbe9c4-c51d-5da3-d4c0-d1586bded181.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/67cbe9c4-c51d-5da3-d4c0-d1586bded181.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/67cbe9c4-c51d-5da3-d4c0-d1586bded181.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXObwResults Methods

RFmxEvdoMXObwResults Methods

The [RFmxEvdoMXObwResults](67d41335-172d-9925-e065-e96eda47cf44.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchMeasurement | Returns the occupied bandwidth (OBW) measurement. |
|  | FetchSpectrum | Fetches the spectrum trace used for the OBW measurement. |
|  | GetAbsolutePower | Gets the absolute power measured in the occupied bandwidth (OBW). This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetOccupiedBandwidth | Gets the bandwidth that occupies 99 percent of the total power of the signal. This value is expressed in Hz. |
|  | GetStartFrequency | Gets the start frequency of the occupied bandwidth (OBW). This value is expressed in Hz. |
|  | GetStopFrequency | Gets the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxEvdoMXObwResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/68b27b48-8514-594f-ad16-f652b5e1e0c9.htm language=enus -->
## TOPIC 00071: rfmxevdodotnet/html/68b27b48-8514-594f-ad16-f652b5e1e0c9.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/68b27b48-8514-594f-ad16-f652b5e1e0c9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/68b27b48-8514-594f-ad16-f652b5e1e0c9.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.SetIQOffsetRemovalEnabled Method

RFmxEvdoMXModAccConfigurationSetIQOffsetRemovalEnabled Method

Sets whether to remove the I/Q offset before the EVM measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQOffsetRemovalEnabled(
	string selectorString,
	RFmxEvdoMXModAccIQOffsetRemovalEnabled value
)
```

```text
Public Function SetIQOffsetRemovalEnabled ( 
	selectorString As String,
	value As RFmxEvdoMXModAccIQOffsetRemovalEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXModAccIQOffsetRemovalEnabledSpecifies whether to remove the I/Q offset before the EVM measurement.

###### Return Value

Int32

##### Remarks

ModAccIQOffsetRemovalEnabled

False

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/6fb1d77f-6db0-cd94-269d-4af9cd0c384e.htm language=enus -->
## TOPIC 00072: rfmxevdodotnet/html/6fb1d77f-6db0-cd94-269d-4af9cd0c384e.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/6fb1d77f-6db0-cd94-269d-4af9cd0c384e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/6fb1d77f-6db0-cd94-269d-4af9cd0c384e.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.FetchUplinkNumberOfDetectedChannels Method

RFmxEvdoMXModAccResultsFetchUplinkNumberOfDetectedChannels Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUplinkNumberOfDetectedChannels(
	string selectorString,
	double timeout,
	out int uplinkNumberOfDetectedChannels
)
```

```text
Public Function FetchUplinkNumberOfDetectedChannels ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef uplinkNumberOfDetectedChannels As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **uplinkNumberOfDetectedChannels**
  - Type: SystemInt32 Upon return, contains the number of channels detected by the ModAcc.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/724ecad5-cddb-7de6-4fb5-0e8ebc59faa2.htm language=enus -->
## TOPIC 00073: rfmxevdodotnet/html/724ecad5-cddb-7de6-4fb5-0e8ebc59faa2.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/724ecad5-cddb-7de6-4fb5-0e8ebc59faa2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/724ecad5-cddb-7de6-4fb5-0e8ebc59faa2.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXConstants.PxiTriggerLine0 Field

RFmxEvdoMXConstantsPxiTriggerLine0 Field

The signal is exported to the PXI trigger line 0.

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMXConstants Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/73bf830b-5b97-027e-d19d-477592cf839e.htm language=enus -->
## TOPIC 00074: rfmxevdodotnet/html/73bf830b-5b97-027e-d19d-477592cf839e.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/73bf830b-5b97-027e-d19d-477592cf839e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/73bf830b-5b97-027e-d19d-477592cf839e.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAcc Methods

RFmxEvdoMXModAcc Methods

The [RFmxEvdoMXModAcc](9e18599c-91ec-7661-179c-1ee31fdbd14b.htm) type exposes the following members.

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

RFmxEvdoMXModAcc Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/7542c461-49aa-13e9-9a2d-afc2b7debcb5.htm language=enus -->
## TOPIC 00075: rfmxevdodotnet/html/7542c461-49aa-13e9-9a2d-afc2b7debcb5.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/7542c461-49aa-13e9-9a2d-afc2b7debcb5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/7542c461-49aa-13e9-9a2d-afc2b7debcb5.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXMeasurementTypes Enumeration

RFmxEvdoMXMeasurementTypes Enumeration

Specifies the type of measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum RFmxEvdoMXMeasurementTypes
```

```text
<FlagsAttribute>
Public Enumeration RFmxEvdoMXMeasurementTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ModAcc | 1 | Selects ModAcc measurement. |
|  | Acp | 2 | Selects ACP measurement. |
|  | Chp | 4 | Selects CHP measurement. |
|  | Obw | 8 | Selects OBW measurement. |
|  | Sem | 16 | Selects SEM measurement. |
|  | Cda | 32 | Selects CDA measurement. |
|  | SlotPhase | 64 | Selects SlotPhase measurement. |
|  | SlotPower | 128 | Selects SlotPower measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/7950cd03-df96-c66f-c953-70c177160c02.htm language=enus -->
## TOPIC 00076: rfmxevdodotnet/html/7950cd03-df96-c66f-c953-70c177160c02.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/7950cd03-df96-c66f-c953-70c177160c02.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/7950cd03-df96-c66f-c953-70c177160c02.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXChpConfiguration.GetRbwFilterAutoBandwidth Method

RFmxEvdoMXChpConfigurationGetRbwFilterAutoBandwidth Method

Gets whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterAutoBandwidth(
	string selectorString,
	out RFmxEvdoMXChpRbwAutoBandwidth value
)
```

```text
Public Function GetRbwFilterAutoBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXChpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXChpRbwAutoBandwidthUpon return, contains whether the measurement computes the RBW.

###### Return Value

Int32

##### Remarks

ChpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxEvdoMXChpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/7b0542b8-e924-513f-413f-ffb63728a1d7.htm language=enus -->
## TOPIC 00077: rfmxevdodotnet/html/7b0542b8-e924-513f-413f-ffb63728a1d7.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/7b0542b8-e924-513f-413f-ffb63728a1d7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/7b0542b8-e924-513f-413f-ffb63728a1d7.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemResults.GetUpperOffsetMarginAbsolutePower Method

RFmxEvdoMXSemResultsGetUpperOffsetMarginAbsolutePower Method

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetMarginAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetMarginAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use "offset(n)" as the selector string to read this method.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetMarginAbsolutePower

##### See Also

###### Reference

RFmxEvdoMXSemResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/7cf353c2-32c6-98b6-a0f7-77aff9f64c34.htm language=enus -->
## TOPIC 00078: rfmxevdodotnet/html/7cf353c2-32c6-98b6-a0f7-77aff9f64c34.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/7cf353c2-32c6-98b6-a0f7-77aff9f64c34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/7cf353c2-32c6-98b6-a0f7-77aff9f64c34.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXObwSweepTimeAuto Enumeration

RFmxEvdoMXObwSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXObwSweepTimeAuto
```

```text
Public Enumeration RFmxEvdoMXObwSweepTimeAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(String, Double) method. |
|  | True | 1 | The measurement uses the default sweep time of 1.67 ms. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/805be008-a965-59c1-ade2-40a7ee38ef54.htm language=enus -->
## TOPIC 00079: rfmxevdodotnet/html/805be008-a965-59c1-ade2-40a7ee38ef54.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/805be008-a965-59c1-ade2-40a7ee38ef54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/805be008-a965-59c1-ade2-40a7ee38ef54.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAcc Properties

RFmxEvdoMXModAcc Properties

The [RFmxEvdoMXModAcc](9e18599c-91ec-7661-179c-1ee31fdbd14b.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxEvdoMXModAccConfiguration instance that provides methods to configure the ModAcc measurement |
|  | Results | Gets the RFmxEvdoMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Top

##### See Also

###### Reference

RFmxEvdoMXModAcc Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/8435b259-8ff1-8183-6b63-8c2218f89e81.htm language=enus -->
## TOPIC 00080: rfmxevdodotnet/html/8435b259-8ff1-8183-6b63-8c2218f89e81.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/8435b259-8ff1-8183-6b63-8c2218f89e81.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/8435b259-8ff1-8183-6b63-8c2218f89e81.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.GetMeasurementEnabled Method

RFmxEvdoMXModAccConfigurationGetMeasurementEnabled Method

Gets whether to enable the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccMeasurementEnabled

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/8439437a-5e49-a57c-32fb-668588e14653.htm language=enus -->
## TOPIC 00081: rfmxevdodotnet/html/8439437a-5e49-a57c-32fb-668588e14653.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/8439437a-5e49-a57c-32fb-668588e14653.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/8439437a-5e49-a57c-32fb-668588e14653.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetTriggerMinimumQuietTimeDuration Method

RFmxEvdoMXGetTriggerMinimumQuietTimeDuration Method

SetIQPowerEdgeTriggerSlope(String, RFmxEvdoMXIQPowerEdgeTriggerSlope)

Rising

Falling

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerMinimumQuietTimeDuration(
	string selectorString,
	out double value
)
```

```text
Public Function GetTriggerMinimumQuietTimeDuration ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(String, RFmxEvdoMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level.

###### Return Value

Int32

##### Remarks

TriggerMinimumQuietTimeDuration

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/853e832c-51bc-e8ee-d1e1-69f7ba33c8a9.htm language=enus -->
## TOPIC 00082: rfmxevdodotnet/html/853e832c-51bc-e8ee-d1e1-69f7ba33c8a9.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/853e832c-51bc-e8ee-d1e1-69f7ba33c8a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/853e832c-51bc-e8ee-d1e1-69f7ba33c8a9.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetIFOutputPowerOffsetAuto Method

RFmxEvdoMXAcpConfigurationSetIFOutputPowerOffsetAuto Method

SetMeasurementMethod(String, RFmxEvdoMXAcpMeasurementMethod)

DynamicRange

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIFOutputPowerOffsetAuto(
	string selectorString,
	RFmxEvdoMXAcpIFOutputPowerOffsetAuto value
)
```

```text
Public Function SetIFOutputPowerOffsetAuto ( 
	selectorString As String,
	value As RFmxEvdoMXAcpIFOutputPowerOffsetAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpIFOutputPowerOffsetAuto Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. This method is used only if you set the SetMeasurementMethod(String, RFmxEvdoMXAcpMeasurementMethod) method to DynamicRange.

###### Return Value

Int32

##### Remarks

AcpIFOutputPowerOffsetAuto

True

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/882835d4-a328-e78c-8dcc-1a96b01664c6.htm language=enus -->
## TOPIC 00083: rfmxevdodotnet/html/882835d4-a328-e78c-8dcc-1a96b01664c6.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/882835d4-a328-e78c-8dcc-1a96b01664c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/882835d4-a328-e78c-8dcc-1a96b01664c6.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.GetMultiCarrierFilterEnabled Method

RFmxEvdoMXModAccConfigurationGetMultiCarrierFilterEnabled Method

Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMultiCarrierFilterEnabled(
	string selectorString,
	out RFmxEvdoMXModAccMultiCarrierFilterEnabled value
)
```

```text
Public Function GetMultiCarrierFilterEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXModAccMultiCarrierFilterEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXModAccMultiCarrierFilterEnabledEnables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers.

###### Return Value

Int32

##### Remarks

ModAccMultiCarrierFilterEnabled

False

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/8846f58d-77cd-9f6f-81fe-5252cddb2569.htm language=enus -->
## TOPIC 00084: rfmxevdodotnet/html/8846f58d-77cd-9f6f-81fe-5252cddb2569.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/8846f58d-77cd-9f6f-81fe-5252cddb2569.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/8846f58d-77cd-9f6f-81fe-5252cddb2569.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ModAcc Property

RFmxEvdoMXModAcc Property

RFmxEvdoMXModAcc

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxEvdoMXModAcc ModAcc { get; }
```

```text
Public ReadOnly Property ModAcc As RFmxEvdoMXModAcc
	Get
```

###### Property Value

RFmxEvdoMXModAcc

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/8853fb27-f84f-2711-1014-32cd75bda62d.htm language=enus -->
## TOPIC 00085: rfmxevdodotnet/html/8853fb27-f84f-2711-1014-32cd75bda62d.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/8853fb27-f84f-2711-1014-32cd75bda62d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/8853fb27-f84f-2711-1014-32cd75bda62d.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.SetTriggerType Method

RFmxEvdoMXSetTriggerType Method

Sets the trigger type.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerType(
	string selectorString,
	RFmxEvdoMXTriggerType value
)
```

```text
Public Function SetTriggerType ( 
	selectorString As String,
	value As RFmxEvdoMXTriggerType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXTriggerTypeSpecifies the trigger type.

###### Return Value

Int32

##### Remarks

TriggerType

None

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/886cda72-b0ae-acdb-fc0d-e797ef84c3dc.htm language=enus -->
## TOPIC 00086: rfmxevdodotnet/html/886cda72-b0ae-acdb-fc0d-e797ef84c3dc.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/886cda72-b0ae-acdb-fc0d-e797ef84c3dc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/886cda72-b0ae-acdb-fc0d-e797ef84c3dc.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXLinkDirection Enumeration

RFmxEvdoMXLinkDirection Enumeration

Specifies the direction for which the frequency is calculated. Only Uplink is supported.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXLinkDirection
```

```text
Public Enumeration RFmxEvdoMXLinkDirection
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Uplink | 1 | The frequency is calculated in the reverse link direction, also know as the uplink direction. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/8ac46f0a-8ee8-61cc-9214-d1756d2b1749.htm language=enus -->
## TOPIC 00087: rfmxevdodotnet/html/8ac46f0a-8ee8-61cc-9214-d1756d2b1749.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/8ac46f0a-8ee8-61cc-9214-d1756d2b1749.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/8ac46f0a-8ee8-61cc-9214-d1756d2b1749.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccUplinkDetectedDataModulationType Enumeration

RFmxEvdoMXModAccUplinkDetectedDataModulationType Enumeration

Returns the modulation type of the uplink data channel.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXModAccUplinkDetectedDataModulationType
```

```text
Public Enumeration RFmxEvdoMXModAccUplinkDetectedDataModulationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DataChannelAbsent | 1 | The specified uplink data channel is absent. |
|  | B4 | 2 | The specified uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |
|  | Q4 | 3 | The specified uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
|  | Q2 | 4 | The specified uplink data channel uses QPSK with the Walsh function W(2,1). |
|  | Q4Q2 | 5 | The specified uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |
|  | E4E2 | 6 | The specified uplink data channel 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/90b30f0d-4635-be05-da73-4bce00c3d20e.htm language=enus -->
## TOPIC 00088: rfmxevdodotnet/html/90b30f0d-4635-be05-da73-4bce00c3d20e.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/90b30f0d-4635-be05-da73-4bce00c3d20e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/90b30f0d-4635-be05-da73-4bce00c3d20e.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.GetAllTracesEnabled Method

RFmxEvdoMXModAccConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccAllTracesEnabled

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/90e2d977-01c9-5361-d9a4-62fc2a98b9cf.htm language=enus -->
## TOPIC 00089: rfmxevdodotnet/html/90e2d977-01c9-5361-d9a4-62fc2a98b9cf.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/90e2d977-01c9-5361-d9a4-62fc2a98b9cf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/90e2d977-01c9-5361-d9a4-62fc2a98b9cf.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetRbwFilterBandwidth Method

RFmxEvdoMXAcpConfigurationSetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxEvdoMXAcpRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemDouble Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxEvdoMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

AcpRbwFilterBandwidth

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/9117f378-5544-7e9d-374b-abf55ce2a11b.htm language=enus -->
## TOPIC 00090: rfmxevdodotnet/html/9117f378-5544-7e9d-374b-abf55ce2a11b.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/9117f378-5544-7e9d-374b-abf55ce2a11b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/9117f378-5544-7e9d-374b-abf55ce2a11b.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemResults.FetchCarrierMeasurementArray Method

RFmxEvdoMXSemResultsFetchCarrierMeasurementArray Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurementArray(
	string selectorString,
	double timeout,
	ref double[] absoluteIntegratedPower,
	ref double[] relativeIntegratedPower
)
```

```text
Public Function FetchCarrierMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef absoluteIntegratedPower As Double(),
	ByRef relativeIntegratedPower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **absoluteIntegratedPower**
  - Type: SystemDouble Upon return, contains the array of absolute carrier powers. This value is expressed in dBm.
- **relativeIntegratedPower**
  - Type: SystemDouble Upon return, contains the array of relative carrier powers. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXSemResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/9821081c-e5a1-bb05-25c9-4272ade2cf4c.htm language=enus -->
## TOPIC 00091: rfmxevdodotnet/html/9821081c-e5a1-bb05-25c9-4272ade2cf4c.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/9821081c-e5a1-bb05-25c9-4272ade2cf4c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/9821081c-e5a1-bb05-25c9-4272ade2cf4c.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetIQGainImbalance Method

RFmxEvdoMXModAccResultsGetIQGainImbalance Method

Gets the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.EvdoMX

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

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: SystemDoubleUpon return, contains the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

ModAccResultsIQGainImbalance

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/9a047edc-3ba4-5c44-677a-b4c8df835569.htm language=enus -->
## TOPIC 00092: rfmxevdodotnet/html/9a047edc-3ba4-5c44-677a-b4c8df835569.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/9a047edc-3ba4-5c44-677a-b4c8df835569.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/9a047edc-3ba4-5c44-677a-b4c8df835569.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetSweepTimeAuto Method

RFmxEvdoMXAcpConfigurationSetSweepTimeAuto Method

Sets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSweepTimeAuto(
	string selectorString,
	RFmxEvdoMXAcpSweepTimeAuto value
)
```

```text
Public Function SetSweepTimeAuto ( 
	selectorString As String,
	value As RFmxEvdoMXAcpSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpSweepTimeAutoSpecifies whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

AcpSweepTimeAuto

True

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/9ce67bc9-3e90-510f-dc3b-efe774421d11.htm language=enus -->
## TOPIC 00093: rfmxevdodotnet/html/9ce67bc9-3e90-510f-dc3b-efe774421d11.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/9ce67bc9-3e90-510f-dc3b-efe774421d11.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/9ce67bc9-3e90-510f-dc3b-efe774421d11.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccConfiguration.SetMeasurementOffset Method

RFmxEvdoMXModAccConfigurationSetMeasurementOffset Method

SetSynchronizationMode(String, RFmxEvdoMXModAccSynchronizationMode)

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemInt32 Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxEvdoMXModAccSynchronizationMode) method.

###### Return Value

Int32

##### Remarks

ModAccMeasurementOffset

##### See Also

###### Reference

RFmxEvdoMXModAccConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a04ea828-13ac-b174-f0ff-6c48dda8fdc5.htm language=enus -->
## TOPIC 00094: rfmxevdodotnet/html/a04ea828-13ac-b174-f0ff-6c48dda8fdc5.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a04ea828-13ac-b174-f0ff-6c48dda8fdc5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a04ea828-13ac-b174-f0ff-6c48dda8fdc5.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaConfiguration Methods

RFmxEvdoMXCdaConfiguration Methods

The [RFmxEvdoMXCdaConfiguration](04061942-52db-cc0b-1db8-e6604348bea2.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigurePowerUnit | Configures the power unit for the code domain power results, except total power. |
|  | ConfigureSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length. |
|  | ConfigureUplinkMeasurementChannel | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces after performing the CDA measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIQGainImbalanceRemovalEnabled | Gets whether to remove the I/Q gain imbalance before the CDA measurement. |
|  | GetIQOffsetRemovalEnabled | Gets whether to remove the I/Q offset before the CDA measurement. |
|  | GetIQQuadratureErrorRemovalEnabled | Gets whether to remove the I/Q quadrature error before the CDA measurement. |
|  | GetMeasurementEnabled | Gets whether to enable the CDA measurement. |
|  | GetMeasurementLength | Gets the duration of the CDA measurement. This value is expressed in slots. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxEvdoMXCdaSynchronizationMode) method. |
|  | GetPowerUnit | Gets the measurement unit of the code domain power results. |
|  | GetReceiveFilterEnabled | Gets whether to enable receive filtering. |
|  | GetSpectrumInverted | Gets whether the signal spectrum is inverted. |
|  | GetSynchronizationMode | Gets whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUplinkBranch | Gets the Walsh branch of the channel, subject to channel-specific analysis. |
|  | GetUplinkWalshCodeLength | Gets the Walsh code length of the channel, subject to channel-specific analysis. |
|  | GetUplinkWalshCodeNumber | Gets the Walsh code number of the channel, subject to channel-specific analysis. |
|  | SetAllTracesEnabled | Sets whether to enable the traces after performing the CDA measurement. |
|  | SetIQGainImbalanceRemovalEnabled | Sets whether to remove the I/Q gain imbalance before the CDA measurement. |
|  | SetIQOffsetRemovalEnabled | Sets whether to remove the I/Q offset before the CDA measurement. |
|  | SetIQQuadratureErrorRemovalEnabled | Sets whether to remove the I/Q quadrature error before the CDA measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the CDA measurement. |
|  | SetMeasurementLength | Sets the duration of the CDA measurement. This value is expressed in slots. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxEvdoMXCdaSynchronizationMode) method. |
|  | SetPowerUnit | Sets the measurement unit of the code domain power results. |
|  | SetReceiveFilterEnabled | Sets whether to enable receive filtering. |
|  | SetSpectrumInverted | Sets whether the signal spectrum is inverted. |
|  | SetSynchronizationMode | Sets whether the measurement is performed from the frame, slot, or symbol boundary. |
|  | SetUplinkBranch | Sets the Walsh branch of the channel, subject to channel-specific analysis. |
|  | SetUplinkWalshCodeLength | Sets the Walsh code length of the channel, subject to channel-specific analysis. |
|  | SetUplinkWalshCodeNumber | Sets the Walsh code number of the channel, subject to channel-specific analysis. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxEvdoMXCdaConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a07b3e64-e755-dca2-ef27-036a5bc11841.htm language=enus -->
## TOPIC 00095: rfmxevdodotnet/html/a07b3e64-e755-dca2-ef27-036a5bc11841.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a07b3e64-e755-dca2-ef27-036a5bc11841.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a07b3e64-e755-dca2-ef27-036a5bc11841.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.SetFftOverlapMode Method

RFmxEvdoMXAcpConfigurationSetFftOverlapMode Method

Sets how the FFT overlap is applied to the acquired samples.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFftOverlapMode(
	string selectorString,
	RFmxEvdoMXAcpFftOverlapMode value
)
```

```text
Public Function SetFftOverlapMode ( 
	selectorString As String,
	value As RFmxEvdoMXAcpFftOverlapMode
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpFftOverlapModemissing content

###### Return Value

Int32

##### Remarks

AcpFftOverlapMode

Disabled

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a0cc7c12-1749-92e4-e77f-1acea3f48636.htm language=enus -->
## TOPIC 00096: rfmxevdodotnet/html/a0cc7c12-1749-92e4-e77f-1acea3f48636.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a0cc7c12-1749-92e4-e77f-1acea3f48636.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a0cc7c12-1749-92e4-e77f-1acea3f48636.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.FetchPhaseErrorTrace Method

RFmxEvdoMXModAccResultsFetchPhaseErrorTrace Method

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: NationalInstrumentsAnalogWaveformSingle Specifies the data for a real waveform including the start, delta, and actual values.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a1da520b-7a9e-b3d1-e4d4-a8084791bcbc.htm language=enus -->
## TOPIC 00097: rfmxevdodotnet/html/a1da520b-7a9e-b3d1-e4d4-a8084791bcbc.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a1da520b-7a9e-b3d1-e4d4-a8084791bcbc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a1da520b-7a9e-b3d1-e4d4-a8084791bcbc.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSlotPhaseResults.FetchChipPhaseErrorLinearFitTrace Method

RFmxEvdoMXSlotPhaseResultsFetchChipPhaseErrorLinearFitTrace Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchChipPhaseErrorLinearFitTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> chipPhaseErrorLinearFit
)
```

```text
Public Function FetchChipPhaseErrorLinearFitTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef chipPhaseErrorLinearFit As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **chipPhaseErrorLinearFit**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the data for a real waveform including the start, delta, and actual values.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXSlotPhaseResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a1dfa7c9-a157-7026-6334-9bdbcb1cb054.htm language=enus -->
## TOPIC 00098: rfmxevdodotnet/html/a1dfa7c9-a157-7026-6334-9bdbcb1cb054.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a1dfa7c9-a157-7026-6334-9bdbcb1cb054.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a1dfa7c9-a157-7026-6334-9bdbcb1cb054.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemConfiguration.GetNumberOfOffsets Method

RFmxEvdoMXSemConfigurationGetNumberOfOffsets Method

Gets the number of SEM offset segments.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfOffsets(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfOffsets ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemInt32Upon return, contains the number of SEM offset segments.

###### Return Value

Int32

##### Remarks

SemNumberOfOffsets

##### See Also

###### Reference

RFmxEvdoMXSemConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a1f8c161-88d2-5a3c-5538-e4cd7485de9a.htm language=enus -->
## TOPIC 00099: rfmxevdodotnet/html/a1f8c161-88d2-5a3c-5538-e4cd7485de9a.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a1f8c161-88d2-5a3c-5538-e4cd7485de9a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a1f8c161-88d2-5a3c-5538-e4cd7485de9a.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX Properties

RFmxEvdoMX Properties

The [RFmxEvdoMX](763b6cdd-6004-23c1-c462-21a9c6498a94.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Acp | Gets the RFmxEvdoMXAcp instance that represents the ACP measurement. |
|  | Cda | Gets the RFmxEvdoMXCda instance that represents the CDA measurement. |
|  | Chp | Gets the RFmxEvdoMXChp instance that represents the CHP measurement. |
|  | IsDisposed | Gets a value that indicates whether the signal has been disposed. |
|  | ModAcc | Gets the RFmxEvdoMXModAcc instance that represents the ModAcc measurement. |
|  | Obw | Gets the RFmxEvdoMXObw instance that represents the OBW measurement. |
|  | Sem | Gets the RFmxEvdoMXSem instance that represents the SEM measurement. |
|  | SignalConfigurationName | Gets the signal configuration name. |
|  | SignalConfigurationType | Gets the Type object for RFmxEvdoMX. |
|  | SlotPhase | Gets the RFmxEvdoMXSlotPhase instance that represents the SlotPhase measurement. |
|  | SlotPower | Gets the RFmxEvdoMXSlotPower instance that represents the SlotPower measurement. |

Top

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a4af4961-07e2-7cab-4ee6-2e70736f84f7.htm language=enus -->
## TOPIC 00100: rfmxevdodotnet/html/a4af4961-07e2-7cab-4ee6-2e70736f84f7.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a4af4961-07e2-7cab-4ee6-2e70736f84f7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a4af4961-07e2-7cab-4ee6-2e70736f84f7.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.ConfigureOffsetPowerReference Method

RFmxEvdoMXAcpConfigurationConfigureOffsetPowerReference Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureOffsetPowerReference(
	string selectorString,
	RFmxEvdoMXAcpOffsetPowerReferenceCarrier offsetPowerReferenceCarrier,
	int offsetPowerReferenceSpecific
)
```

```text
Public Function ConfigureOffsetPowerReference ( 
	selectorString As String,
	offsetPowerReferenceCarrier As RFmxEvdoMXAcpOffsetPowerReferenceCarrier,
	offsetPowerReferenceSpecific As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **offsetPowerReferenceCarrier**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpOffsetPowerReferenceCarrier Specifies how the reference power is selected.
- **offsetPowerReferenceSpecific**
  - Type: SystemInt32 Specifies the carrier number that is used as power reference. This parameter only applies if you set the offsetPowerReferenceCarrier parameter to Specific.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a4d6da17-63ae-63b1-3070-afc013ad5ecf.htm language=enus -->
## TOPIC 00101: rfmxevdodotnet/html/a4d6da17-63ae-63b1-3070-afc013ad5ecf.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a4d6da17-63ae-63b1-3070-afc013ad5ecf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a4d6da17-63ae-63b1-3070-afc013ad5ecf.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetIQOriginOffset Method

RFmxEvdoMXModAccResultsGetIQOriginOffset Method

Gets the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.EvdoMX

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

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a543270b-38ac-d3a6-724e-0d287d25b585.htm language=enus -->
## TOPIC 00102: rfmxevdodotnet/html/a543270b-38ac-d3a6-724e-0d287d25b585.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a543270b-38ac-d3a6-724e-0d287d25b585.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a543270b-38ac-d3a6-724e-0d287d25b585.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetSelectedPorts Method

RFmxEvdoMXGetSelectedPorts Method

Valid values

Default values

Supported devices: PXIe-5820/5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSelectedPorts(
	string selectorString,
	out string value
)
```

```text
Public Function GetSelectedPorts ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringSpecifies the instrument port to be used by the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a59064f4-3686-98f0-8212-06360cddbffe.htm language=enus -->
## TOPIC 00103: rfmxevdodotnet/html/a59064f4-3686-98f0-8212-06360cddbffe.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a59064f4-3686-98f0-8212-06360cddbffe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a59064f4-3686-98f0-8212-06360cddbffe.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXChpConfiguration.SetMeasurementEnabled Method

RFmxEvdoMXChpConfigurationSetMeasurementEnabled Method

Sets whether to enable the channel power (CHP) measurement.

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemBooleanSpecifies whether to enable the channel power (CHP) measurement.

###### Return Value

Int32

##### Remarks

ChpMeasurementEnabled

##### See Also

###### Reference

RFmxEvdoMXChpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a734817e-f5f2-9c1a-8cb7-4113579bdf02.htm language=enus -->
## TOPIC 00104: rfmxevdodotnet/html/a734817e-f5f2-9c1a-8cb7-4113579bdf02.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a734817e-f5f2-9c1a-8cb7-4113579bdf02.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a734817e-f5f2-9c1a-8cb7-4113579bdf02.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXCdaResults.FetchUplinkCodeDomainIandQPowerTrace Method

RFmxEvdoMXCdaResultsFetchUplinkCodeDomainIandQPowerTrace Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchUplinkCodeDomainIandQPowerTrace(
	string selectorString,
	double timeout,
	ref float[] iCodeDomainPowers,
	ref float[] qCodeDomainPowers
)
```

```text
Public Function FetchUplinkCodeDomainIandQPowerTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef iCodeDomainPowers As Single(),
	ByRef qCodeDomainPowers As Single()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **iCodeDomainPowers**
  - Type: SystemSingle Upon return, contains the I code domain power traces. This value is expressed in dB or dBm.
- **qCodeDomainPowers**
  - Type: SystemSingle Upon return, contains the Q code domain power traces. This value is expressed in dB or dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXCdaResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a73e5deb-34df-7ef0-c6e2-0eacc77ec783.htm language=enus -->
## TOPIC 00105: rfmxevdodotnet/html/a73e5deb-34df-7ef0-c6e2-0eacc77ec783.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a73e5deb-34df-7ef0-c6e2-0eacc77ec783.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a73e5deb-34df-7ef0-c6e2-0eacc77ec783.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpConfiguration.GetOffsetPowerReferenceCarrier Method

RFmxEvdoMXAcpConfigurationGetOffsetPowerReferenceCarrier Method

Gets the carrier number that is used as the power reference to measure the offset channel relative power.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetPowerReferenceCarrier(
	string selectorString,
	out RFmxEvdoMXAcpOffsetPowerReferenceCarrier value
)
```

```text
Public Function GetOffsetPowerReferenceCarrier ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXAcpOffsetPowerReferenceCarrier
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXAcpOffsetPowerReferenceCarrierUpon return, contains the carrier number that is used as the power reference to measure the offset channel relative power.

###### Return Value

Int32

##### Remarks

AcpOffsetPowerReferenceCarrier

Composite

##### See Also

###### Reference

RFmxEvdoMXAcpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a94b44b7-8f04-6292-12ab-83ea26b9ac40.htm language=enus -->
## TOPIC 00106: rfmxevdodotnet/html/a94b44b7-8f04-6292-12ab-83ea26b9ac40.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a94b44b7-8f04-6292-12ab-83ea26b9ac40.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a94b44b7-8f04-6292-12ab-83ea26b9ac40.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureUplinkNumberOfChannels Method

RFmxEvdoMXConfigureUplinkNumberOfChannels Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUplinkNumberOfChannels(
	string selectorString,
	int uplinkNumberOfChannels
)
```

```text
Public Function ConfigureUplinkNumberOfChannels ( 
	selectorString As String,
	uplinkNumberOfChannels As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **uplinkNumberOfChannels**
  - Type: SystemInt32Specifies the number of user-defined channels.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a980c625-e476-e6dd-75f5-ac5fe19883e8.htm language=enus -->
## TOPIC 00107: rfmxevdodotnet/html/a980c625-e476-e6dd-75f5-ac5fe19883e8.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a980c625-e476-e6dd-75f5-ac5fe19883e8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a980c625-e476-e6dd-75f5-ac5fe19883e8.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXChpConfiguration.SetSweepTimeInterval Method

RFmxEvdoMXChpConfigurationSetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxEvdoMXChpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.EvdoMX

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
  - Type: SystemDouble Specifies the sweep time when you set the SetSweepTimeAuto(String, RFmxEvdoMXChpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ChpSweepTimeInterval

##### See Also

###### Reference

RFmxEvdoMXChpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/a9f90d32-b7f0-0a2f-1fd1-1fa4aa8cc066.htm language=enus -->
## TOPIC 00108: rfmxevdodotnet/html/a9f90d32-b7f0-0a2f-1fd1-1fa4aa8cc066.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/a9f90d32-b7f0-0a2f-1fd1-1fa4aa8cc066.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/a9f90d32-b7f0-0a2f-1fd1-1fa4aa8cc066.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXChpConfiguration.GetRbwFilterType Method

RFmxEvdoMXChpConfigurationGetRbwFilterType Method

Gets the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterType(
	string selectorString,
	out RFmxEvdoMXChpRbwFilterType value
)
```

```text
Public Function GetRbwFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxEvdoMXChpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXChpRbwFilterTypeUpon return, contains the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

ChpRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxEvdoMXChpConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/adfbe396-4476-9484-5fdd-90ad4bef37f6.htm language=enus -->
## TOPIC 00109: rfmxevdodotnet/html/adfbe396-4476-9484-5fdd-90ad4bef37f6.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/adfbe396-4476-9484-5fdd-90ad4bef37f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/adfbe396-4476-9484-5fdd-90ad4bef37f6.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ResetToDefault Method

RFmxEvdoMXResetToDefault Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ResetToDefault(
	string selectorString
)
```

```text
Public Function ResetToDefault ( 
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

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/ae39ff9c-d127-dcb4-01b4-e51b86f70a26.htm language=enus -->
## TOPIC 00110: rfmxevdodotnet/html/ae39ff9c-d127-dcb4-01b4-e51b86f70a26.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/ae39ff9c-d127-dcb4-01b4-e51b86f70a26.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/ae39ff9c-d127-dcb4-01b4-e51b86f70a26.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureUplinkUserDefinedChannelArray Method

RFmxEvdoMXConfigureUplinkUserDefinedChannelArray Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUplinkUserDefinedChannelArray(
	string selectorString,
	int[] uplinkWalshCodeLength,
	int[] uplinkWalshCodeNumber,
	RFmxEvdoMXUplinkBranch[] uplinkBranch
)
```

```text
Public Function ConfigureUplinkUserDefinedChannelArray ( 
	selectorString As String,
	uplinkWalshCodeLength As Integer(),
	uplinkWalshCodeNumber As Integer(),
	uplinkBranch As RFmxEvdoMXUplinkBranch()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **uplinkWalshCodeLength**
  - Type: SystemInt32Specifies the Walsh code length of a specific user-defined channel.
- **uplinkWalshCodeNumber**
  - Type: SystemInt32Specifies the Walsh code number of a specific user-defined channel.
- **uplinkBranch**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXUplinkBranchSpecifies the quadrature branch on which a specific user-defined channel is mapped.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/aeed2b4d-d714-ce82-c1b2-ca10cae8b390.htm language=enus -->
## TOPIC 00111: rfmxevdodotnet/html/aeed2b4d-d714-ce82-c1b2-ca10cae8b390.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/aeed2b4d-d714-ce82-c1b2-ca10cae8b390.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/aeed2b4d-d714-ce82-c1b2-ca10cae8b390.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXSemConfiguration.GetOffsetStartFrequency Method

RFmxEvdoMXSemConfigurationGetOffsetStartFrequency Method

Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetStartFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetStartFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemOffsetStartFrequency

##### See Also

###### Reference

RFmxEvdoMXSemConfiguration Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm language=enus -->
## TOPIC 00112: rfmxevdodotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.InstrMX Namespace

NationalInstruments.RFmx.InstrMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxEvdoMXExtension | Provides extension methods to create EV-DO signal configuration. These methods are added to RFmxInstrMX class. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/b140d675-05e1-7e10-0003-96e8411e2c78.htm language=enus -->
## TOPIC 00113: rfmxevdodotnet/html/b140d675-05e1-7e10-0003-96e8411e2c78.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/b140d675-05e1-7e10-0003-96e8411e2c78.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/b140d675-05e1-7e10-0003-96e8411e2c78.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXModAccResults.GetUplinkDetectedWalshCodeNumber Method

RFmxEvdoMXModAccResultsGetUplinkDetectedWalshCodeNumber Method

(n)

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkDetectedWalshCodeNumber(
	string selectorString,
	out int value
)
```

```text
Public Function GetUplinkDetectedWalshCodeNumber ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Channel number. Example: "Channel0", "result::r1/Channel0". You can use the BuildChannelString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the Walsh Code number of a detected channel. Use "channel(n)" as the selector string to read this method.

###### Return Value

Int32

##### Remarks

ModAccResultsUplinkDetectedWalshCodeNumber

##### See Also

###### Reference

RFmxEvdoMXModAccResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/b210e78f-e5e3-ac26-dd94-5508d63992aa.htm language=enus -->
## TOPIC 00114: rfmxevdodotnet/html/b210e78f-e5e3-ac26-dd94-5508d63992aa.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/b210e78f-e5e3-ac26-dd94-5508d63992aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/b210e78f-e5e3-ac26-dd94-5508d63992aa.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXChpResults.FetchCarrierMeasurementArray Method

RFmxEvdoMXChpResultsFetchCarrierMeasurementArray Method

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCarrierMeasurementArray(
	string selectorString,
	double timeout,
	ref double[] carrierAbsolutePower,
	ref double[] carrierRelativePower
)
```

```text
Public Function FetchCarrierMeasurementArray ( 
	selectorString As String,
	timeout As Double,
	ByRef carrierAbsolutePower As Double(),
	ByRef carrierRelativePower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **carrierAbsolutePower**
  - Type: SystemDouble Upon return, contains the array of absolute carrier powers. This value is expressed in dBm.
- **carrierRelativePower**
  - Type: SystemDouble Upon return, contains the array of relative carrier powers. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMXChpResults Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/b8474392-add9-6d32-9bb3-962b009cdad3.htm language=enus -->
## TOPIC 00115: rfmxevdodotnet/html/b8474392-add9-6d32-9bb3-962b009cdad3.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/b8474392-add9-6d32-9bb3-962b009cdad3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/b8474392-add9-6d32-9bb3-962b009cdad3.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMXAcpRbwAutoBandwidth Enumeration

RFmxEvdoMXAcpRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxEvdoMXAcpRbwAutoBandwidth
```

```text
Public Enumeration RFmxEvdoMXAcpRbwAutoBandwidth
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement uses the RBW that you specify in the ACP RBW method. |
|  | True | 1 | The measurement computes the RBW. |

##### See Also

###### Reference

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/b8890744-3c4f-0cdc-4a1d-fb74d7ed6c4a.htm language=enus -->
## TOPIC 00116: rfmxevdodotnet/html/b8890744-3c4f-0cdc-4a1d-fb74d7ed6c4a.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/b8890744-3c4f-0cdc-4a1d-fb74d7ed6c4a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/b8890744-3c4f-0cdc-4a1d-fb74d7ed6c4a.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.GetDigitalEdgeTriggerSource Method

RFmxEvdoMXGetDigitalEdgeTriggerSource Method

SetTriggerType(String, RFmxEvdoMXTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDigitalEdgeTriggerSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetDigitalEdgeTriggerSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemString Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxEvdoMXTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

DigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-evdo-dotnet path=rfmxevdodotnet/html/c1414fe2-1ce0-6260-364f-211abeefe1c0.htm language=enus -->
## TOPIC 00117: rfmxevdodotnet/html/c1414fe2-1ce0-6260-364f-211abeefe1c0.htm

- bundle_id: `rfmx-evdo-dotnet`
- source_path: `rfmxevdodotnet/html/c1414fe2-1ce0-6260-364f-211abeefe1c0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-dotnet/raw/resource/enus/rfmxevdodotnet/html/c1414fe2-1ce0-6260-364f-211abeefe1c0.htm
- document_id: `rfmx-evdo-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxEvdoMX.ConfigureUplinkUserDefinedChannel Method

RFmxEvdoMXConfigureUplinkUserDefinedChannel Method

"channel(n)"

Namespace:

NationalInstruments.RFmx.EvdoMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUplinkUserDefinedChannel(
	string selectorString,
	int uplinkWalshCodeLength,
	int uplinkWalshCodeNumber,
	RFmxEvdoMXUplinkBranch uplinkBranch
)
```

```text
Public Function ConfigureUplinkUserDefinedChannel ( 
	selectorString As String,
	uplinkWalshCodeLength As Integer,
	uplinkWalshCodeNumber As Integer,
	uplinkBranch As RFmxEvdoMXUplinkBranch
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of channel number.
- **uplinkWalshCodeLength**
  - Type: SystemInt32Specifies the Walsh code length of a specific user-defined channel.
- **uplinkWalshCodeNumber**
  - Type: SystemInt32Specifies the Walsh code number of a specific user-defined channel.
- **uplinkBranch**
  - Type: NationalInstruments.RFmx.EvdoMXRFmxEvdoMXUplinkBranchSpecifies the quadrature branch on which a specific user-defined channel is mapped.

###### Return Value

Int32

##### See Also

###### Reference

RFmxEvdoMX Class

NationalInstruments.RFmx.EvdoMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
