# NI DOCUMENT BUNDLE: rfmx-vna-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-vna-dotnet start=1 end=94 -->
<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/00c6f059-5133-adfa-52fb-f637254783e9.htm language=enus -->
## TOPIC 00001: rfmxvnadotnet/html/00c6f059-5133-adfa-52fb-f637254783e9.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/00c6f059-5133-adfa-52fb-f637254783e9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/00c6f059-5133-adfa-52fb-f637254783e9.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSegmentDwellTime Method

RFmxVnaMXGetSegmentDwellTime Method

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentDwellTime(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentDwellTime ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SegmentDwellTime

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/0405b4c9-dd97-9b68-20d0-f57c4b2af4c4.htm language=enus -->
## TOPIC 00002: rfmxvnadotnet/html/0405b4c9-dd97-9b68-20d0-f57c4b2af4c4.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/0405b4c9-dd97-9b68-20d0-f57c4b2af4c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/0405b4c9-dd97-9b68-20d0-f57c4b2af4c4.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSegmentIFBandwidth Method

RFmxVnaMXSetSegmentIFBandwidth Method

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentIFBandwidth(
	string selectorString,
	double value
)
```

```text
Public Function SetSegmentIFBandwidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SegmentIFBandwidth

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/0aec5feb-b987-2347-d172-5bf1d48591a9.htm language=enus -->
## TOPIC 00003: rfmxvnadotnet/html/0aec5feb-b987-2347-d172-5bf1d48591a9.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/0aec5feb-b987-2347-d172-5bf1d48591a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/0aec5feb-b987-2347-d172-5bf1d48591a9.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetLimitedConfigurationChange Method

RFmxVnaMXSetLimitedConfigurationChange Method

Sets the set of properties that are considered by NI-RFmx in the locked signal configuration state.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLimitedConfigurationChange(
	string selectorString,
	RFmxVnaMXLimitedConfigurationChange value
)
```

```text
Public Function SetLimitedConfigurationChange ( 
	selectorString As String,
	value As RFmxVnaMXLimitedConfigurationChange
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXLimitedConfigurationChange**
  - Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state.

###### Return Value

Int32

##### Remarks

LimitedConfigurationChange

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/0f39a125-e21c-2cbd-c52e-5f011d5c9be7.htm language=enus -->
## TOPIC 00004: rfmxvnadotnet/html/0f39a125-e21c-2cbd-c52e-5f011d5c9be7.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/0f39a125-e21c-2cbd-c52e-5f011d5c9be7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/0f39a125-e21c-2cbd-c52e-5f011d5c9be7.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsConfiguration.SetReceiverPort Method

RFmxVnaMXSParamsConfigurationSetReceiverPort Method

Sets the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2".

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReceiverPort(
	string selectorString,
	string value
)
```

```text
Public Function SetReceiverPort ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2".

###### Return Value

Int32

##### Remarks

SParamsReceiverPort

##### See Also

###### Reference

RFmxVnaMXSParamsConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/143cd24e-49fd-b08b-cd5c-15debdfc1b6d.htm language=enus -->
## TOPIC 00005: rfmxvnadotnet/html/143cd24e-49fd-b08b-cd5c-15debdfc1b6d.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/143cd24e-49fd-b08b-cd5c-15debdfc1b6d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/143cd24e-49fd-b08b-cd5c-15debdfc1b6d.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsConfiguration.ConfigureSParameter Method

RFmxVnaMXSParamsConfigurationConfigureSParameter Method

Configures the S-Parameter to be measured in format S<receiver port number><source port number>

Use "sparam<n>" as the selector string to configure this method.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSParameter(
	string selectorString,
	string sParameter
)
```

```text
Public Function ConfigureSParameter ( 
	selectorString As String,
	sParameter As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sParameter String**
  - Specifies the S-Parameter to be measured. The default value is S11

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMXSParamsConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/17861ba6-bbe0-9259-f172-b436bad9e821.htm language=enus -->
## TOPIC 00006: rfmxvnadotnet/html/17861ba6-bbe0-9259-f172-b436bad9e821.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/17861ba6-bbe0-9259-f172-b436bad9e821.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/17861ba6-bbe0-9259-f172-b436bad9e821.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPowerLevel Method

RFmxVnaMXGetPowerLevel Method

Gets the source power level for the VNA port. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPowerLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetPowerLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number, signal number and port number. Example: "segment0" or "signal0" or "port0" or "signal0/segment0/port0". You can use the BuildPortString(String, String) method to build the selector string.
- **value Double**
  - Upon return, contains the source power level for the VNA port. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

PowerLevel

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/19562386-161a-ea2b-15a6-780a4132f575.htm language=enus -->
## TOPIC 00007: rfmxvnadotnet/html/19562386-161a-ea2b-15a6-780a4132f575.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/19562386-161a-ea2b-15a6-780a4132f575.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/19562386-161a-ea2b-15a6-780a4132f575.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalsetLoadFromFile Method

RFmxVnaMXCalsetLoadFromFile Method

CalsetSaveToFile(String, String, String)

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalsetLoadFromFile(
	string selectorString,
	string calsetName,
	string calsetFilePath
)
```

```text
Public Function CalsetLoadFromFile ( 
	selectorString As String,
	calsetName As String,
	calsetFilePath As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **calsetName String**
  - Specifies the name of the calset.
- **calsetFilePath String**
  - Specifies the complete path to the file with .ncst extension from which the calset is to be loaded.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/2094938f-918d-758b-a2a0-21e927c1e404.htm language=enus -->
## TOPIC 00008: rfmxvnadotnet/html/2094938f-918d-758b-a2a0-21e927c1e404.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/2094938f-918d-758b-a2a0-21e927c1e404.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/2094938f-918d-758b-a2a0-21e927c1e404.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPulseGeneratorWidth Method

RFmxVnaMXGetPulseGeneratorWidth Method

PulseGeneratorWidth

PulsePeriod

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseGeneratorWidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseGeneratorWidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the pulsegen number and signal number. Example: "signal0" or "signal0/pulsegen0". You can use the BuildPulseGeneratorString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseGeneratorWidth

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/231a7783-49c1-ede2-2a86-5448663e40a3.htm language=enus -->
## TOPIC 00009: rfmxvnadotnet/html/231a7783-49c1-ede2-2a86-5448663e40a3.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/231a7783-49c1-ede2-2a86-5448663e40a3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/231a7783-49c1-ede2-2a86-5448663e40a3.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetStopFrequency Method

RFmxVnaMXGetStopFrequency Method

Gets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStopFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetStopFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the highest frequency at which the measurement needs to be performed. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

StopFrequency

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/283d4206-651d-b0eb-767f-48225aaeb5e0.htm language=enus -->
## TOPIC 00010: rfmxvnadotnet/html/283d4206-651d-b0eb-767f-48225aaeb5e0.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/283d4206-651d-b0eb-767f-48225aaeb5e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/283d4206-651d-b0eb-767f-48225aaeb5e0.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSegmentIFBandwidthEnabled Enumeration

RFmxVnaMXSegmentIFBandwidthEnabled Enumeration

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXSegmentIFBandwidthEnabled
```

```text
Public Enumeration RFmxVnaMXSegmentIFBandwidthEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables individual IF Bandwidth value configured for each segment. |
| True | 1 | Enables individual IF Bandwidth value configured for each segment. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/28ffca2e-48a8-47e8-261d-fe9df8bac73b.htm language=enus -->
## TOPIC 00011: rfmxvnadotnet/html/28ffca2e-48a8-47e8-261d-fe9df8bac73b.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/28ffca2e-48a8-47e8-261d-fe9df8bac73b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/28ffca2e-48a8-47e8-261d-fe9df8bac73b.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsConfiguration.ExportToSnPFile Method

RFmxVnaMXSParamsConfigurationExportToSnPFile Method

Data Format

User Comment

Ports

Note

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int ExportToSnPFile(
	string selectorString,
	string snpFilePath
)
```

```text
Public Function ExportToSnPFile ( 
	selectorString As String,
	snpFilePath As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" You can use the BuildSParameterString(String, Int32) method to build the selector string.
- **snpFilePath String**
  - Specifies the .snp file to save the measured S-parameters.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMXSParamsConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/2ff3249a-f89f-601b-f77c-f7aa1886167c.htm language=enus -->
## TOPIC 00012: rfmxvnadotnet/html/2ff3249a-f89f-601b-f77c-f7aa1886167c.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/2ff3249a-f89f-601b-f77c-f7aa1886167c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/2ff3249a-f89f-601b-f77c-f7aa1886167c.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSegmentDwellTime Method

RFmxVnaMXSetSegmentDwellTime Method

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentDwellTime(
	string selectorString,
	double value
)
```

```text
Public Function SetSegmentDwellTime ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SegmentDwellTime

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/36bf088f-1c09-1b4e-d614-636369958dbf.htm language=enus -->
## TOPIC 00013: rfmxvnadotnet/html/36bf088f-1c09-1b4e-d614-636369958dbf.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/36bf088f-1c09-1b4e-d614-636369958dbf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/36bf088f-1c09-1b4e-d614-636369958dbf.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetStartFrequency Method

RFmxVnaMXSetStartFrequency Method

Sets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStartFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetStartFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

StartFrequency

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/37208155-cf1d-644c-0939-5bcc4006aeb9.htm language=enus -->
## TOPIC 00014: rfmxvnadotnet/html/37208155-cf1d-644c-0939-5bcc4006aeb9.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/37208155-cf1d-644c-0939-5bcc4006aeb9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/37208155-cf1d-644c-0939-5bcc4006aeb9.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsConfiguration.SetSnPUserComment Method

RFmxVnaMXSParamsConfigurationSetSnPUserComment Method

Sets user-specific additional information passed as SParams User Comment to write to SnP file.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSnPUserComment(
	string selectorString,
	string value
)
```

```text
Public Function SetSnPUserComment ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies user-specific additional information passed as SParams User Comment to write to SnP file.

###### Return Value

Int32

##### Remarks

SParamsSnPUserComment

##### See Also

###### Reference

RFmxVnaMXSParamsConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/437546ce-4cc0-7088-114a-b5e8462a9571.htm language=enus -->
## TOPIC 00015: rfmxvnadotnet/html/437546ce-4cc0-7088-114a-b5e8462a9571.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/437546ce-4cc0-7088-114a-b5e8462a9571.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/437546ce-4cc0-7088-114a-b5e8462a9571.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitRemoveCalibrationElement Method

RFmxVnaMXCalkitManagerCalkitRemoveCalibrationElement Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitRemoveCalibrationElement(
	string selectorString,
	string calibrationElementID
)
```

```text
Public Function CalkitManagerCalkitRemoveCalibrationElement ( 
	selectorString As String,
	calibrationElementID As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID" You can use the BuildCalkitString(String, String) method to build the selector string.
- **calibrationElementID String**
  - Specifies the ID of the Calibration Element within the Calkit.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/4ce3f1ad-a1b7-424f-23c7-1a3f670bb5a8.htm language=enus -->
## TOPIC 00016: rfmxvnadotnet/html/4ce3f1ad-a1b7-424f-23c7-1a3f670bb5a8.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/4ce3f1ad-a1b7-424f-23c7-1a3f670bb5a8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/4ce3f1ad-a1b7-424f-23c7-1a3f670bb5a8.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetNumberOfFrequencyPoints Method

RFmxVnaMXSetNumberOfFrequencyPoints Method

Sets the number of frequency points at which the measurement needs to be performed.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfFrequencyPoints(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfFrequencyPoints ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of frequency points at which the measurement needs to be performed.

###### Return Value

Int32

##### Remarks

NumberOfFrequencyPoints

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/4d89b0af-ccfa-2bfe-ed49-305fb370b2cb.htm language=enus -->
## TOPIC 00017: rfmxvnadotnet/html/4d89b0af-ccfa-2bfe-ed49-305fb370b2cb.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/4d89b0af-ccfa-2bfe-ed49-305fb370b2cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/4d89b0af-ccfa-2bfe-ed49-305fb370b2cb.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSegmentTestReceiverAttenuationEnabled Method

RFmxVnaMXGetSegmentTestReceiverAttenuationEnabled Method

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentTestReceiverAttenuationEnabled(
	string selectorString,
	out RFmxVnaMXSegmentTestReceiverAttenuationEnabled value
)
```

```text
Public Function GetSegmentTestReceiverAttenuationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXSegmentTestReceiverAttenuationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSegmentTestReceiverAttenuationEnabled**
  - Upon return, contains whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method.

###### Return Value

Int32

##### Remarks

SegmentTestReceiverAttenuationEnabled

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/5518fc83-8e90-ebca-defa-08ce567e2540.htm language=enus -->
## TOPIC 00018: rfmxvnadotnet/html/5518fc83-8e90-ebca-defa-08ce567e2540.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/5518fc83-8e90-ebca-defa-08ce567e2540.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/5518fc83-8e90-ebca-defa-08ce567e2540.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSegmentTestReceiverAttenuationEnabled Method

RFmxVnaMXSetSegmentTestReceiverAttenuationEnabled Method

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentTestReceiverAttenuationEnabled(
	string selectorString,
	RFmxVnaMXSegmentTestReceiverAttenuationEnabled value
)
```

```text
Public Function SetSegmentTestReceiverAttenuationEnabled ( 
	selectorString As String,
	value As RFmxVnaMXSegmentTestReceiverAttenuationEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSegmentTestReceiverAttenuationEnabled**
  - Specifies whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method.

###### Return Value

Int32

##### Remarks

SegmentTestReceiverAttenuationEnabled

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/5657e6bd-ca7b-29e9-d1d5-f93534f939d6.htm language=enus -->
## TOPIC 00019: rfmxvnadotnet/html/5657e6bd-ca7b-29e9-d1d5-f93534f939d6.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/5657e6bd-ca7b-29e9-d1d5-f93534f939d6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/5657e6bd-ca7b-29e9-d1d5-f93534f939d6.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSegmentIFBandwidthEnabled Method

RFmxVnaMXSetSegmentIFBandwidthEnabled Method

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentIFBandwidthEnabled(
	string selectorString,
	RFmxVnaMXSegmentIFBandwidthEnabled value
)
```

```text
Public Function SetSegmentIFBandwidthEnabled ( 
	selectorString As String,
	value As RFmxVnaMXSegmentIFBandwidthEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSegmentIFBandwidthEnabled**
  - Specifies whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method.

###### Return Value

Int32

##### Remarks

SegmentIFBandwidthEnabled

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/59ca7463-0d63-3289-866e-a925dcfa947b.htm language=enus -->
## TOPIC 00020: rfmxvnadotnet/html/59ca7463-0d63-3289-866e-a925dcfa947b.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/59ca7463-0d63-3289-866e-a925dcfa947b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/59ca7463-0d63-3289-866e-a925dcfa947b.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSegmentDwellTimeEnabled Enumeration

RFmxVnaMXSegmentDwellTimeEnabled Enumeration

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXSegmentDwellTimeEnabled
```

```text
Public Enumeration RFmxVnaMXSegmentDwellTimeEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables individual Dwell Time value configured for each segment. |
| True | 1 | Enables individual Dwell Time value configured for each segment. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/5ced075b-6346-ab8f-444f-b1bf7a7ac7ef.htm language=enus -->
## TOPIC 00021: rfmxvnadotnet/html/5ced075b-6346-ab8f-444f-b1bf7a7ac7ef.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/5ced075b-6346-ab8f-444f-b1bf7a7ac7ef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/5ced075b-6346-ab8f-444f-b1bf7a7ac7ef.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSegmentPowerLevelEnabled Method

RFmxVnaMXSetSegmentPowerLevelEnabled Method

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentPowerLevelEnabled(
	string selectorString,
	RFmxVnaMXSegmentPowerLevelEnabled value
)
```

```text
Public Function SetSegmentPowerLevelEnabled ( 
	selectorString As String,
	value As RFmxVnaMXSegmentPowerLevelEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSegmentPowerLevelEnabled**
  - Specifies whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method.

###### Return Value

Int32

##### Remarks

SegmentPowerLevelEnabled

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/5e09a186-f5ab-4fc2-d0df-ff6f842489d3.htm language=enus -->
## TOPIC 00022: rfmxvnadotnet/html/5e09a186-f5ab-4fc2-d0df-ff6f842489d3.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/5e09a186-f5ab-4fc2-d0df-ff6f842489d3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/5e09a186-f5ab-4fc2-d0df-ff6f842489d3.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetCorrectionCalibrationCalkitType Method

RFmxVnaMXSetCorrectionCalibrationCalkitType Method

Sets the type of calkit used for calibration.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCorrectionCalibrationCalkitType(
	string selectorString,
	RFmxVnaMXCorrectionCalibrationCalkitType value
)
```

```text
Public Function SetCorrectionCalibrationCalkitType ( 
	selectorString As String,
	value As RFmxVnaMXCorrectionCalibrationCalkitType
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the port number and signal number. Example: "signal0" or "signal0/port0". You can use the BuildPortString(String, String) method to build the selector string.
- **value RFmxVnaMXCorrectionCalibrationCalkitType**
  - Specifies the type of calkit used for calibration.

###### Return Value

Int32

##### Remarks

CorrectionCalibrationCalkitType

Electronic

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/5ed5be45-c351-332e-49c6-809fbc7dc061.htm language=enus -->
## TOPIC 00023: rfmxvnadotnet/html/5ed5be45-c351-332e-49c6-809fbc7dc061.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/5ed5be45-c351-332e-49c6-809fbc7dc061.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/5ed5be45-c351-332e-49c6-809fbc7dc061.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitAddConnector Method

RFmxVnaMXCalkitManagerCalkitAddConnector Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitAddConnector(
	string selectorString,
	string connectorID
)
```

```text
Public Function CalkitManagerCalkitAddConnector ( 
	selectorString As String,
	connectorID As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID" You can use the BuildCalkitString(String, String) method to build the selector string.
- **connectorID String**
  - Specifies the ID of the Connector within the Calkit.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/653bcb8c-46fc-4be5-9c6d-fa8395ea931d.htm language=enus -->
## TOPIC 00024: rfmxvnadotnet/html/653bcb8c-46fc-4be5-9c6d-fa8395ea931d.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/653bcb8c-46fc-4be5-9c6d-fa8395ea931d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/653bcb8c-46fc-4be5-9c6d-fa8395ea931d.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetCorrectionCalibrationCalkitMechanicalName Method

RFmxVnaMXGetCorrectionCalibrationCalkitMechanicalName Method

CorrectionCalibrationCalkitType

Mechanical

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCorrectionCalibrationCalkitMechanicalName(
	string selectorString,
	out string value
)
```

```text
Public Function GetCorrectionCalibrationCalkitMechanicalName ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the port number and signal number. Example: "signal0" or "signal0/port0". You can use the BuildPortString(String, String) method to build the selector string.
- **value String**
  - Upon return, contains the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical.

###### Return Value

Int32

##### Remarks

CorrectionCalibrationCalkitMechanicalName

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/6573d80e-d543-51c4-bf1b-9cef57539f2a.htm language=enus -->
## TOPIC 00025: rfmxvnadotnet/html/6573d80e-d543-51c4-bf1b-9cef57539f2a.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/6573d80e-d543-51c4-bf1b-9cef57539f2a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/6573d80e-d543-51c4-bf1b-9cef57539f2a.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType Enumeration

RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType Enumeration

specifies the model type of of the 1-port reflect standard.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType
```

```text
Public Enumeration RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| ReflectOpen | 0 | Models an Offset Open by specifying the offset parameters and the parameters of the Open (3rd order polynomial model of the capacitance). |
| ReflectShort | 1 | Models an Offset Short by specifying the offset parameters and the parameters of the short (3rd order polynomial model of the inductance). |
| Load | 2 | Models an Offset Load by specifying the offset parameters. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/6592fb60-dce9-d51a-134c-327c95ba9462.htm language=enus -->
## TOPIC 00026: rfmxvnadotnet/html/6592fb60-dce9-d51a-134c-327c95ba9462.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/6592fb60-dce9-d51a-134c-327c95ba9462.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/6592fb60-dce9-d51a-134c-327c95ba9462.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitCalibrationElementReflectModelGetC2 Method

RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelGetC2 Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitCalibrationElementReflectModelGetC2(
	string selectorString,
	out double c2
)
```

```text
Public Function CalkitManagerCalkitCalibrationElementReflectModelGetC2 ( 
	selectorString As String,
	<OutAttribute> ByRef c2 As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(String, String) method to build the selector string.
- **c2 Double**
  - Upon return, contains the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/6a3ac2c2-ad76-6047-619e-8c71697c196b.htm language=enus -->
## TOPIC 00027: rfmxvnadotnet/html/6a3ac2c2-ad76-6047-619e-8c71697c196b.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/6a3ac2c2-ad76-6047-619e-8c71697c196b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/6a3ac2c2-ad76-6047-619e-8c71697c196b.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSweepSequence Method

RFmxVnaMXSetSweepSequence Method

Sets the sequence of acquisitions for various frequency points and source ports.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSweepSequence(
	string selectorString,
	RFmxVnaMXSweepSequence value
)
```

```text
Public Function SetSweepSequence ( 
	selectorString As String,
	value As RFmxVnaMXSweepSequence
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSweepSequence**
  - Specifies the sequence of acquisitions for various frequency points and source ports.

###### Return Value

Int32

##### Remarks

SweepSequence

Standard

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/6b999fc8-ffc8-af50-e16c-21f4ce202204.htm language=enus -->
## TOPIC 00028: rfmxvnadotnet/html/6b999fc8-ffc8-af50-e16c-21f4ce202204.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/6b999fc8-ffc8-af50-e16c-21f4ce202204.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/6b999fc8-ffc8-af50-e16c-21f4ce202204.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitCalibrationElementDelayModelSetDelay Method

RFmxVnaMXCalkitManagerCalkitCalibrationElementDelayModelSetDelay Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitCalibrationElementDelayModelSetDelay(
	string selectorString,
	double delay
)
```

```text
Public Function CalkitManagerCalkitCalibrationElementDelayModelSetDelay ( 
	selectorString As String,
	delay As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(String, String) method to build the selector string.
- **delay Double**
  - Specifies the Delay of a Calibration Element defined by the Delay Model.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/6bf1cca9-4c60-a46d-0dd9-f5ef216d085e.htm language=enus -->
## TOPIC 00029: rfmxvnadotnet/html/6bf1cca9-4c60-a46d-0dd9-f5ef216d085e.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/6bf1cca9-4c60-a46d-0dd9-f5ef216d085e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/6bf1cca9-4c60-a46d-0dd9-f5ef216d085e.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetCorrectionPortExtensionLossDCLoss Method

RFmxVnaMXSetCorrectionPortExtensionLossDCLoss Method

True

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCorrectionPortExtensionLossDCLoss(
	string selectorString,
	double value
)
```

```text
Public Function SetCorrectionPortExtensionLossDCLoss ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the port number and signal number. Example: "signal0" or "signal0/port0". You can use the BuildPortString(String, String) method to build the selector string.
- **value Double**
  - Specifies the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

CorrectionPortExtensionLossDCLoss

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/6e10c9b5-7e15-eb2f-e82d-c53ad80e6dff.htm language=enus -->
## TOPIC 00030: rfmxvnadotnet/html/6e10c9b5-7e15-eb2f-e82d-c53ad80e6dff.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/6e10c9b5-7e15-eb2f-e82d-c53ad80e6dff.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/6e10c9b5-7e15-eb2f-e82d-c53ad80e6dff.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitCalibrationElementReflectModelGetC0 Method

RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelGetC0 Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitCalibrationElementReflectModelGetC0(
	string selectorString,
	out double c0
)
```

```text
Public Function CalkitManagerCalkitCalibrationElementReflectModelGetC0 ( 
	selectorString As String,
	<OutAttribute> ByRef c0 As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(String, String) method to build the selector string.
- **c0 Double**
  - Upon return, contains the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/72373451-d03d-aa1f-22bb-78ae87f4c163.htm language=enus -->
## TOPIC 00031: rfmxvnadotnet/html/72373451-d03d-aa1f-22bb-78ae87f4c163.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/72373451-d03d-aa1f-22bb-78ae87f4c163.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/72373451-d03d-aa1f-22bb-78ae87f4c163.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSegmentPowerLevel Method

RFmxVnaMXGetSegmentPowerLevel Method

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentPowerLevel(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentPowerLevel ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number, signal number and port number. Example: "segment0" or "signal0" or "port0" or "signal0/segment0/port0". You can use the BuildPortString(String, String) method to build the selector string.
- **value Double**
  - Upon return, contains the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SegmentPowerLevel

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/73457c80-6e7c-3a82-7c0e-4927d9756fd8.htm language=enus -->
## TOPIC 00032: rfmxvnadotnet/html/73457c80-6e7c-3a82-7c0e-4927d9756fd8.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/73457c80-6e7c-3a82-7c0e-4927d9756fd8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/73457c80-6e7c-3a82-7c0e-4927d9756fd8.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetPulsePeriod Method

RFmxVnaMXSetPulsePeriod Method

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPulsePeriod(
	string selectorString,
	double value
)
```

```text
Public Function SetPulsePeriod ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulsePeriod

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/73460228-5a31-11f7-418c-055d5e5952ef.htm language=enus -->
## TOPIC 00033: rfmxvnadotnet/html/73460228-5a31-11f7-418c-055d5e5952ef.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/73460228-5a31-11f7-418c-055d5e5952ef.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/73460228-5a31-11f7-418c-055d5e5952ef.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPulseAcquisitionWidth Method

RFmxVnaMXGetPulseAcquisitionWidth Method

PulseModeEnabled

True

PulseAcquisitionAuto

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseAcquisitionWidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseAcquisitionWidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the width of pulse acquisition when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseAcquisitionWidth

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/736fdbef-5142-015f-6b85-fe4bf6ed52e5.htm language=enus -->
## TOPIC 00034: rfmxvnadotnet/html/736fdbef-5142-015f-6b85-fe4bf6ed52e5.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/736fdbef-5142-015f-6b85-fe4bf6ed52e5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/736fdbef-5142-015f-6b85-fe4bf6ed52e5.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSweepType Method

RFmxVnaMXGetSweepType Method

Gets the sweep type for the measurement.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepType(
	string selectorString,
	out RFmxVnaMXSweepType value
)
```

```text
Public Function GetSweepType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXSweepType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSweepType**
  - Upon return, contains the sweep type for the measurement.

###### Return Value

Int32

##### Remarks

SweepType

List

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/745365c6-2cbb-e88b-c8e2-ac61f87bc4df.htm language=enus -->
## TOPIC 00035: rfmxvnadotnet/html/745365c6-2cbb-e88b-c8e2-ac61f87bc4df.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/745365c6-2cbb-e88b-c8e2-ac61f87bc4df.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/745365c6-2cbb-e88b-c8e2-ac61f87bc4df.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXAutoIFBandwidthScalingEnabled Enumeration

RFmxVnaMXAutoIFBandwidthScalingEnabled Enumeration

Specifies whether IF Bandwidth is scaled down at low frequencies.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXAutoIFBandwidthScalingEnabled
```

```text
Public Enumeration RFmxVnaMXAutoIFBandwidthScalingEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables IFBW scaling at low frequencies. The IF Bandwidth specified by you using IF Bandwidth method is used for all the frequencies. |
| True | 1 | Enables scaling of IF Bandwidth at low frequencies. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/74cfefca-beb7-82f3-aefc-d30d94307086.htm language=enus -->
## TOPIC 00036: rfmxvnadotnet/html/74cfefca-beb7-82f3-aefc-d30d94307086.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/74cfefca-beb7-82f3-aefc-d30d94307086.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/74cfefca-beb7-82f3-aefc-d30d94307086.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitConnectorSetImpedance Method

RFmxVnaMXCalkitManagerCalkitConnectorSetImpedance Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitConnectorSetImpedance(
	string selectorString,
	double impedance
)
```

```text
Public Function CalkitManagerCalkitConnectorSetImpedance ( 
	selectorString As String,
	impedance As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(String, String) method to build the selector string.
- **impedance Double**
  - Specifies the Impedance of a Connector of a specific Calkit.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/78ff67dd-29a6-18c7-9e72-610cd8fd1310.htm language=enus -->
## TOPIC 00037: rfmxvnadotnet/html/78ff67dd-29a6-18c7-9e72-610cd8fd1310.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/78ff67dd-29a6-18c7-9e72-610cd8fd1310.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/78ff67dd-29a6-18c7-9e72-610cd8fd1310.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition Enumeration

RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition Enumeration

specifies the S-Parameter definition of the Calibration Element.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition
```

```text
Public Enumeration RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| ReflectModel | 0 | S-Parameters defined by the Reflect model (1-port). |
| Sparameter | 1 | S-Parameters defined by a S-Parameter list (1-port and 2-port). |
| DelayModel | 2 | S-Parameters defined by a delay model (2-port). |
| Unknown | 3 | S-Parameters not further specified. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/7e0d759c-282c-22b2-f077-0e45a8905e06.htm language=enus -->
## TOPIC 00038: rfmxvnadotnet/html/7e0d759c-282c-22b2-f077-0e45a8905e06.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/7e0d759c-282c-22b2-f077-0e45a8905e06.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/7e0d759c-282c-22b2-f077-0e45a8905e06.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSegmentTestReceiverAttenuationEnabled Enumeration

RFmxVnaMXSegmentTestReceiverAttenuationEnabled Enumeration

False

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXSegmentTestReceiverAttenuationEnabled
```

```text
Public Enumeration RFmxVnaMXSegmentTestReceiverAttenuationEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables individual Test Receiver Attenuation value configured for each segment. |
| True | 1 | Enables individual Test Receiver Attenuation value configured for each segment. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/7f248b81-7559-f4c4-c8ca-a939274fa276.htm language=enus -->
## TOPIC 00039: rfmxvnadotnet/html/7f248b81-7559-f4c4-c8ca-a939274fa276.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/7f248b81-7559-f4c4-c8ca-a939274fa276.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/7f248b81-7559-f4c4-c8ca-a939274fa276.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SendSoftwareEdgeTrigger Method

RFmxVnaMXSendSoftwareEdgeTrigger Method

TriggerType

Namespace:

NationalInstruments.RFmx.VnaMX

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

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/81d71d6a-9a1e-136a-953c-542e3c7896d4.htm language=enus -->
## TOPIC 00040: rfmxvnadotnet/html/81d71d6a-9a1e-136a-953c-542e3c7896d4.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/81d71d6a-9a1e-136a-953c-542e3c7896d4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/81d71d6a-9a1e-136a-953c-542e3c7896d4.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPulseAcquisitionAuto Method

RFmxVnaMXGetPulseAcquisitionAuto Method

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseAcquisitionAuto(
	string selectorString,
	out RFmxVnaMXPulseAcquisitionAuto value
)
```

```text
Public Function GetPulseAcquisitionAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXPulseAcquisitionAuto
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXPulseAcquisitionAuto**
  - Upon return, contains whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True.

###### Return Value

Int32

##### Remarks

PulseAcquisitionAuto

True

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/81ffc536-c0bf-5c20-23d9-3487c67ddbbc.htm language=enus -->
## TOPIC 00041: rfmxvnadotnet/html/81ffc536-c0bf-5c20-23d9-3487c67ddbbc.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/81ffc536-c0bf-5c20-23d9-3487c67ddbbc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/81ffc536-c0bf-5c20-23d9-3487c67ddbbc.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerDeleteCalkit Method

RFmxVnaMXCalkitManagerDeleteCalkit Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerDeleteCalkit(
	string selectorString,
	string calkitID
)
```

```text
Public Function CalkitManagerDeleteCalkit ( 
	selectorString As String,
	calkitID As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **calkitID String**
  - Specifies the ID for the Calkit in Calkit Manager.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/824811c6-f66f-87b2-795c-55cb9f48b107.htm language=enus -->
## TOPIC 00042: rfmxvnadotnet/html/824811c6-f66f-87b2-795c-55cb9f48b107.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/824811c6-f66f-87b2-795c-55cb9f48b107.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/824811c6-f66f-87b2-795c-55cb9f48b107.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetDwellTime Method

RFmxVnaMXGetDwellTime Method

Gets the dwell time. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDwellTime(
	string selectorString,
	out double value
)
```

```text
Public Function GetDwellTime ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the time for which the analyzer waits before acquiring the signal for each measured frequency point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/86c4d46f-a6ac-d286-7608-ac827ffa6aa1.htm language=enus -->
## TOPIC 00043: rfmxvnadotnet/html/86c4d46f-a6ac-d286-7608-ac827ffa6aa1.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/86c4d46f-a6ac-d286-7608-ac827ffa6aa1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/86c4d46f-a6ac-d286-7608-ac827ffa6aa1.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetTriggerMode Method

RFmxVnaMXGetTriggerMode Method

Gets the trigger mode.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerMode(
	string selectorString,
	out RFmxVnaMXTriggerMode value
)
```

```text
Public Function GetTriggerMode ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXTriggerMode
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXTriggerMode**
  - Upon return, contains the trigger mode.

###### Return Value

Int32

##### Remarks

TriggerMode

Signal

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/8820777f-bb70-51ea-56c5-93134ba9ab8f.htm language=enus -->
## TOPIC 00044: rfmxvnadotnet/html/8820777f-bb70-51ea-56c5-93134ba9ab8f.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/8820777f-bb70-51ea-56c5-93134ba9ab8f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/8820777f-bb70-51ea-56c5-93134ba9ab8f.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitGetVersion Method

RFmxVnaMXCalkitManagerCalkitGetVersion Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitGetVersion(
	string selectorString,
	out string calkitVersion
)
```

```text
Public Function CalkitManagerCalkitGetVersion ( 
	selectorString As String,
	<OutAttribute> ByRef calkitVersion As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID" You can use the BuildCalkitString(String, String) method to build the selector string.
- **calkitVersion String**
  - Upon return, contains the version string of the Calkit.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/8b568eca-6c31-00f3-93a1-fa35f8108815.htm language=enus -->
## TOPIC 00045: rfmxvnadotnet/html/8b568eca-6c31-00f3-93a1-fa35f8108815.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/8b568eca-6c31-00f3-93a1-fa35f8108815.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/8b568eca-6c31-00f3-93a1-fa35f8108815.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitConnectorSetMinimumFrequency Method

RFmxVnaMXCalkitManagerCalkitConnectorSetMinimumFrequency Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitConnectorSetMinimumFrequency(
	string selectorString,
	double minimumFrequency
)
```

```text
Public Function CalkitManagerCalkitConnectorSetMinimumFrequency ( 
	selectorString As String,
	minimumFrequency As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(String, String) method to build the selector string.
- **minimumFrequency Double**
  - Specifies the Minimum Frequency of a Connector of a specific Calkit.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/9136ce72-e74a-5fbe-275c-99ab24c8f1f6.htm language=enus -->
## TOPIC 00046: rfmxvnadotnet/html/9136ce72-e74a-5fbe-275c-99ab24c8f1f6.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/9136ce72-e74a-5fbe-275c-99ab24c8f1f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/9136ce72-e74a-5fbe-275c-99ab24c8f1f6.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetPulseModulatorDelay Method

RFmxVnaMXSetPulseModulatorDelay Method

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPulseModulatorDelay(
	string selectorString,
	double value
)
```

```text
Public Function SetPulseModulatorDelay ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseModulatorDelay

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/914525bc-4f5c-8bbd-d0ef-bbdbf6bf337c.htm language=enus -->
## TOPIC 00047: rfmxvnadotnet/html/914525bc-4f5c-8bbd-d0ef-bbdbf6bf337c.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/914525bc-4f5c-8bbd-d0ef-bbdbf6bf337c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/914525bc-4f5c-8bbd-d0ef-bbdbf6bf337c.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability Method

RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(
	string selectorString,
	RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability sParameterAvailability
)
```

```text
Public Function CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability ( 
	selectorString As String,
	sParameterAvailability As RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(String, String) method to build the selector string.
- **sParameterAvailability RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability**
  - Specifies the S-Parameter availability.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/94d9c149-fe01-3603-efd5-9a0275dc5d2b.htm language=enus -->
## TOPIC 00048: rfmxvnadotnet/html/94d9c149-fe01-3603-efd5-9a0275dc5d2b.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/94d9c149-fe01-3603-efd5-9a0275dc5d2b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/94d9c149-fe01-3603-efd5-9a0275dc5d2b.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSegmentStopFrequency Method

RFmxVnaMXGetSegmentStopFrequency Method

Gets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentStopFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentStopFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SegmentStopFrequency

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/961f5b31-55c4-6641-9127-c198cb35ad42.htm language=enus -->
## TOPIC 00049: rfmxvnadotnet/html/961f5b31-55c4-6641-9127-c198cb35ad42.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/961f5b31-55c4-6641-9127-c198cb35ad42.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/961f5b31-55c4-6641-9127-c198cb35ad42.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability Method

RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(
	string selectorString,
	RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability sParameterAvailability
)
```

```text
Public Function CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability ( 
	selectorString As String,
	sParameterAvailability As RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(String, String) method to build the selector string.
- **sParameterAvailability RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability**
  - Specifies the S-Parameter availability.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/96628ec0-fcc5-78a1-1dec-c7f42af6c3b0.htm language=enus -->
## TOPIC 00050: rfmxvnadotnet/html/96628ec0-fcc5-78a1-1dec-c7f42af6c3b0.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/96628ec0-fcc5-78a1-1dec-c7f42af6c3b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/96628ec0-fcc5-78a1-1dec-c7f42af6c3b0.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetPulseModeEnabled Method

RFmxVnaMXSetPulseModeEnabled Method

Sets whether to enable pulse mode for VNA measurement.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPulseModeEnabled(
	string selectorString,
	RFmxVnaMXPulseModeEnabled value
)
```

```text
Public Function SetPulseModeEnabled ( 
	selectorString As String,
	value As RFmxVnaMXPulseModeEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXPulseModeEnabled**
  - Specifies whether to enable pulse mode for VNA measurement.

###### Return Value

Int32

##### Remarks

PulseModeEnabled

False

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/96fe127a-9ca1-a35a-171b-eeab56200b8a.htm language=enus -->
## TOPIC 00051: rfmxvnadotnet/html/96fe127a-9ca1-a35a-171b-eeab56200b8a.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/96fe127a-9ca1-a35a-171b-eeab56200b8a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/96fe127a-9ca1-a35a-171b-eeab56200b8a.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXWavesConfiguration.SetFormat Method

RFmxVnaMXWavesConfigurationSetFormat Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFormat(
	string selectorString,
	RFmxVnaMXWavesFormat value
)
```

```text
Public Function SetFormat ( 
	selectorString As String,
	value As RFmxVnaMXWavesFormat
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXWavesFormat**
  - Specifies the format for wave measurement.

###### Return Value

Int32

##### Remarks

WavesFormat

##### See Also

###### Reference

RFmxVnaMXWavesConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/97e1a0f8-3db2-5ffe-b47c-3e4f0b3c9e48.htm language=enus -->
## TOPIC 00052: rfmxvnadotnet/html/97e1a0f8-3db2-5ffe-b47c-3e4f0b3c9e48.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/97e1a0f8-3db2-5ffe-b47c-3e4f0b3c9e48.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/97e1a0f8-3db2-5ffe-b47c-3e4f0b3c9e48.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetAutoIFBandwidthScalingEnabled Method

RFmxVnaMXGetAutoIFBandwidthScalingEnabled Method

Gets whether IF Bandwidth is scaled down at low frequencies.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoIFBandwidthScalingEnabled(
	string selectorString,
	out RFmxVnaMXAutoIFBandwidthScalingEnabled value
)
```

```text
Public Function GetAutoIFBandwidthScalingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXAutoIFBandwidthScalingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value RFmxVnaMXAutoIFBandwidthScalingEnabled**
  - Upon return, contains whether IF Bandwidth is scaled down at low frequencies.

###### Return Value

Int32

##### Remarks

AutoIFBandwidthScalingEnabled

True

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/9870cbb8-d5ff-2fe2-a8a7-29c6bd0b60aa.htm language=enus -->
## TOPIC 00053: rfmxvnadotnet/html/9870cbb8-d5ff-2fe2-a8a7-29c6bd0b60aa.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/9870cbb8-d5ff-2fe2-a8a7-29c6bd0b60aa.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/9870cbb8-d5ff-2fe2-a8a7-29c6bd0b60aa.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPulseModulatorDelay Method

RFmxVnaMXGetPulseModulatorDelay Method

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseModulatorDelay(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulseModulatorDelay ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseModulatorDelay

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/99130f94-07fb-ed09-ed3d-ac5670138bc8.htm language=enus -->
## TOPIC 00054: rfmxvnadotnet/html/99130f94-07fb-ed09-ed3d-ac5670138bc8.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/99130f94-07fb-ed09-ed3d-ac5670138bc8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/99130f94-07fb-ed09-ed3d-ac5670138bc8.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXDigitalEdgeTriggerEdge Enumeration

RFmxVnaMXDigitalEdgeTriggerEdge Enumeration

TriggerType

DigitalEdge

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXDigitalEdgeTriggerEdge
```

```text
Public Enumeration RFmxVnaMXDigitalEdgeTriggerEdge
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/998cfda0-8a6c-2044-4c12-e12f63b51192.htm language=enus -->
## TOPIC 00055: rfmxvnadotnet/html/998cfda0-8a6c-2044-4c12-e12f63b51192.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/998cfda0-8a6c-2044-4c12-e12f63b51192.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/998cfda0-8a6c-2044-4c12-e12f63b51192.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetAttributeBool Method

RFmxVnaMXGetAttributeBool Method

Gets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.VnaMX

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

- **selectorString String**
  - Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Boolean**
  - Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/99b22dfa-a886-d30a-67da-bd672621e0c4.htm language=enus -->
## TOPIC 00056: rfmxvnadotnet/html/99b22dfa-a886-d30a-67da-bd672621e0c4.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/99b22dfa-a886-d30a-67da-bd672621e0c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/99b22dfa-a886-d30a-67da-bd672621e0c4.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetNumberOfFrequencyPoints Method

RFmxVnaMXGetNumberOfFrequencyPoints Method

Gets the number of frequency points at which the measurement needs to be performed.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfFrequencyPoints(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfFrequencyPoints ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of frequency points at which the measurement needs to be performed.

###### Return Value

Int32

##### Remarks

NumberOfFrequencyPoints

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/9a8739b1-9a4c-2983-5158-226077b0e925.htm language=enus -->
## TOPIC 00057: rfmxvnadotnet/html/9a8739b1-9a4c-2983-5158-226077b0e925.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/9a8739b1-9a4c-2983-5158-226077b0e925.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/9a8739b1-9a4c-2983-5158-226077b0e925.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXTriggerType Enumeration

RFmxVnaMXTriggerType Enumeration

Specifies the trigger type.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXTriggerType
```

```text
Public Enumeration RFmxVnaMXTriggerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 | No trigger is configured. |
| DigitalEdge | 1 | The trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the DigitalEdgeTriggerSource method. |
| Software | 2 | The trigger is not asserted until a software trigger occurs. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/9ca35d79-b295-0539-5f7b-980f67f93479.htm language=enus -->
## TOPIC 00058: rfmxvnadotnet/html/9ca35d79-b295-0539-5f7b-980f67f93479.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/9ca35d79-b295-0539-5f7b-980f67f93479.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/9ca35d79-b295-0539-5f7b-980f67f93479.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXPulseAcquisitionAuto Enumeration

RFmxVnaMXPulseAcquisitionAuto Enumeration

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXPulseAcquisitionAuto
```

```text
Public Enumeration RFmxVnaMXPulseAcquisitionAuto
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 |  |
| True | 1 | The measurement uses the PulseModulatorWidth method to compute pulse acquisition delay and pulse acquisition width. Approximately 20% of the pulse modulator width is set as the pulse acquisition delay and approximately 75% of Pulse Modulator Width is set as the pulse acquisition width. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/9d47f1ae-5679-6802-10fe-77b17af5b4a9.htm language=enus -->
## TOPIC 00059: rfmxvnadotnet/html/9d47f1ae-5679-6802-10fe-77b17af5b4a9.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/9d47f1ae-5679-6802-10fe-77b17af5b4a9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/9d47f1ae-5679-6802-10fe-77b17af5b4a9.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.ResetToDefault Method

RFmxVnaMXResetToDefault Method

Namespace:

NationalInstruments.RFmx.VnaMX

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

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/a119ec02-0550-4bed-70b9-c7d3b15a0e62.htm language=enus -->
## TOPIC 00060: rfmxvnadotnet/html/a119ec02-0550-4bed-70b9-c7d3b15a0e62.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/a119ec02-0550-4bed-70b9-c7d3b15a0e62.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/a119ec02-0550-4bed-70b9-c7d3b15a0e62.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetCorrectionCalibrationMethod Method

RFmxVnaMXGetCorrectionCalibrationMethod Method

Gets the calibration method.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCorrectionCalibrationMethod(
	string selectorString,
	out RFmxVnaMXCorrectionCalibrationMethod value
)
```

```text
Public Function GetCorrectionCalibrationMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXCorrectionCalibrationMethod
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXCorrectionCalibrationMethod**
  - Upon return, contains the calibration method.

###### Return Value

Int32

##### Remarks

CorrectionCalibrationMethod

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/a5caa0c2-cd20-0d96-0cff-368127888a7a.htm language=enus -->
## TOPIC 00061: rfmxvnadotnet/html/a5caa0c2-cd20-0d96-0cff-368127888a7a.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/a5caa0c2-cd20-0d96-0cff-368127888a7a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/a5caa0c2-cd20-0d96-0cff-368127888a7a.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSweepSequence Method

RFmxVnaMXGetSweepSequence Method

Gets the sequence of acquisitions for various frequency points and source ports.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepSequence(
	string selectorString,
	out RFmxVnaMXSweepSequence value
)
```

```text
Public Function GetSweepSequence ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXSweepSequence
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXSweepSequence**
  - Upon return, contains the sequence of acquisitions for various frequency points and source ports.

###### Return Value

Int32

##### Remarks

SweepSequence

Standard

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/a8cb2c56-a785-7a81-5c6d-aa79cfa84cbe.htm language=enus -->
## TOPIC 00062: rfmxvnadotnet/html/a8cb2c56-a785-7a81-5c6d-aa79cfa84cbe.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/a8cb2c56-a785-7a81-5c6d-aa79cfa84cbe.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/a8cb2c56-a785-7a81-5c6d-aa79cfa84cbe.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParams.Configuration Property

RFmxVnaMXSParamsConfiguration Property

RFmxVnaMXSParamsConfiguration

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxVnaMXSParamsConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxVnaMXSParamsConfiguration
	Get
```

###### Property Value

RFmxVnaMXSParamsConfiguration

##### See Also

###### Reference

RFmxVnaMXSParams Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/a91257c6-764b-49c8-8fcb-245e1678b670.htm language=enus -->
## TOPIC 00063: rfmxvnadotnet/html/a91257c6-764b-49c8-8fcb-245e1678b670.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/a91257c6-764b-49c8-8fcb-245e1678b670.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/a91257c6-764b-49c8-8fcb-245e1678b670.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXConstants.PxiTriggerLine6 Field

RFmxVnaMXConstantsPxiTriggerLine6 Field

The signal is exported to the PXI trigger line 6.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiTriggerLine6 = "PXI_Trig6"
```

```text
Public Const PxiTriggerLine6 As String = "PXI_Trig6"
```

###### Field Value

String

##### See Also

###### Reference

RFmxVnaMXConstants Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/aa497059-77ba-eb64-e688-3906c4f26e36.htm language=enus -->
## TOPIC 00064: rfmxvnadotnet/html/aa497059-77ba-eb64-e688-3906c4f26e36.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/aa497059-77ba-eb64-e688-3906c4f26e36.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/aa497059-77ba-eb64-e688-3906c4f26e36.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetSegmentIFBandwidth Method

RFmxVnaMXGetSegmentIFBandwidth Method

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSegmentIFBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetSegmentIFBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Upon return, contains the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SegmentIFBandwidth

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/aae42bd3-59ba-1e46-1730-7deb3dbd7f3b.htm language=enus -->
## TOPIC 00065: rfmxvnadotnet/html/aae42bd3-59ba-1e46-1730-7deb3dbd7f3b.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/aae42bd3-59ba-1e46-1730-7deb3dbd7f3b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/aae42bd3-59ba-1e46-1730-7deb3dbd7f3b.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetAveragingEnabled Method

RFmxVnaMXSetAveragingEnabled Method

Sets whether to enable averaging for the VNA measurement.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingEnabled(
	string selectorString,
	RFmxVnaMXAveragingEnabled value
)
```

```text
Public Function SetAveragingEnabled ( 
	selectorString As String,
	value As RFmxVnaMXAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXAveragingEnabled**
  - Specifies whether to enable averaging for the VNA measurement.

###### Return Value

Int32

##### Remarks

AveragingEnabled

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/aae9e28b-7f6d-ad03-b8c0-8f716be59118.htm language=enus -->
## TOPIC 00066: rfmxvnadotnet/html/aae9e28b-7f6d-ad03-b8c0-8f716be59118.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/aae9e28b-7f6d-ad03-b8c0-8f716be59118.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/aae9e28b-7f6d-ad03-b8c0-8f716be59118.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSweepType Enumeration

RFmxVnaMXSweepType Enumeration

Specifies the sweep type for the measurement.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXSweepType
```

```text
Public Enumeration RFmxVnaMXSweepType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| List | 0 | The frequency is swept in arbitrary frequency steps. |
| Linear | 1 | The frequency is swept in equidistant steps over the frequency range. |
| Segment | 2 | The frequency is swept in frequency sub-sweeps, called segments. For each segment, you can define independent values for settings like IF bandwidth, dwell time, power level per port and test receiver attenuation per port. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/acb8c5c6-7c04-d286-10c1-7acf7023056d.htm language=enus -->
## TOPIC 00067: rfmxvnadotnet/html/acb8c5c6-7c04-d286-10c1-7acf7023056d.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/acb8c5c6-7c04-d286-10c1-7acf7023056d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/acb8c5c6-7c04-d286-10c1-7acf7023056d.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.Commit Method

RFmxVnaMXCommit Method

Initiate(String, String)

Namespace:

NationalInstruments.RFmx.VnaMX

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

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/acd7103a-3889-793f-096a-21028100c7b7.htm language=enus -->
## TOPIC 00068: rfmxvnadotnet/html/acd7103a-3889-793f-096a-21028100c7b7.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/acd7103a-3889-793f-096a-21028100c7b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/acd7103a-3889-793f-096a-21028100c7b7.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsPhaseTraceType Enumeration

RFmxVnaMXSParamsPhaseTraceType Enumeration

Specifies the phase type for all S-Parameters for which (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_SPARAMS_FORMAT.html')")RFMXVNA_ATTR_SPARAMS_FORMAT(/a) method is set to (format type="bold")Phase(/format).

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXSParamsPhaseTraceType
```

```text
Public Enumeration RFmxVnaMXSParamsPhaseTraceType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Wrapped | 0 | The reported S-Parameter phase is wrapped between -180 degress to +180 degrees. |
| Unwrapped | 1 | The reported S-Parameter phase is unwrapped. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/acefedb9-f2b9-f3db-6e4f-7a5572083bcc.htm language=enus -->
## TOPIC 00069: rfmxvnadotnet/html/acefedb9-f2b9-f3db-6e4f-7a5572083bcc.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/acefedb9-f2b9-f3db-6e4f-7a5572083bcc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/acefedb9-f2b9-f3db-6e4f-7a5572083bcc.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSweepDelay Method

RFmxVnaMXSetSweepDelay Method

Sets the sweep delay. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSweepDelay(
	string selectorString,
	double value
)
```

```text
Public Function SetSweepDelay ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the sweep delay. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SweepDelay

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/ad1f441f-a42f-a833-9ffd-ce457e446eab.htm language=enus -->
## TOPIC 00070: rfmxvnadotnet/html/ad1f441f-a42f-a833-9ffd-ce457e446eab.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/ad1f441f-a42f-a833-9ffd-ce457e446eab.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/ad1f441f-a42f-a833-9ffd-ce457e446eab.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXWavesConfiguration.SetNumberOfWaves Method

RFmxVnaMXWavesConfigurationSetNumberOfWaves Method

Sets the number of waves to be measured.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNumberOfWaves(
	string selectorString,
	int value
)
```

```text
Public Function SetNumberOfWaves ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Specifies the number of waves to be measured.

###### Return Value

Int32

##### Remarks

WavesNumberOfWaves

##### See Also

###### Reference

RFmxVnaMXWavesConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/ad442b8c-b902-4c4a-3844-6ea0af3b6ebb.htm language=enus -->
## TOPIC 00071: rfmxvnadotnet/html/ad442b8c-b902-4c4a-3844-6ea0af3b6ebb.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/ad442b8c-b902-4c4a-3844-6ea0af3b6ebb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/ad442b8c-b902-4c4a-3844-6ea0af3b6ebb.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsConfiguration.GetSnPUserComment Method

RFmxVnaMXSParamsConfigurationGetSnPUserComment Method

Gets user-specific additional information passed as SParams User Comment to write to SnP file.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSnPUserComment(
	string selectorString,
	out string value
)
```

```text
Public Function GetSnPUserComment ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Upon return, contains user-specific additional information passed as SParams User Comment to write to SnP file.

###### Return Value

Int32

##### Remarks

SParamsSnPUserComment

##### See Also

###### Reference

RFmxVnaMXSParamsConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/ae78b34e-08a2-abea-a989-548d64bd9eec.htm language=enus -->
## TOPIC 00072: rfmxvnadotnet/html/ae78b34e-08a2-abea-a989-548d64bd9eec.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/ae78b34e-08a2-abea-a989-548d64bd9eec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/ae78b34e-08a2-abea-a989-548d64bd9eec.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetAttributeInt Method

RFmxVnaMXSetAttributeInt Method

Sets the value of a Int attribute.

Namespace:

NationalInstruments.RFmx.VnaMX

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

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Int32**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm language=enus -->
## TOPIC 00073: rfmxvnadotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/af4d93fd-35ff-7f81-1f64-2815c8673d38.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

NationalInstruments.RFmx.InstrMX Namespace

NationalInstruments.RFmx.InstrMX Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | RFmxVnaMXExtension | Provides extension methods to create Vna signal configuration. These methods are added to RFmxInstrMX class. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/b6062c8d-379c-8af8-c0a3-7323445e7dea.htm language=enus -->
## TOPIC 00074: rfmxvnadotnet/html/b6062c8d-379c-8af8-c0a3-7323445e7dea.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/b6062c8d-379c-8af8-c0a3-7323445e7dea.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/b6062c8d-379c-8af8-c0a3-7323445e7dea.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetPulseModulatorWidth Method

RFmxVnaMXSetPulseModulatorWidth Method

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPulseModulatorWidth(
	string selectorString,
	double value
)
```

```text
Public Function SetPulseModulatorWidth ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Specifies the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulseModulatorWidth

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/b68b3b36-8f4a-3dea-2788-0d87aaf8af9f.htm language=enus -->
## TOPIC 00075: rfmxvnadotnet/html/b68b3b36-8f4a-3dea-2788-0d87aaf8af9f.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/b68b3b36-8f4a-3dea-2788-0d87aaf8af9f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/b68b3b36-8f4a-3dea-2788-0d87aaf8af9f.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXPulseTriggerType Enumeration

RFmxVnaMXPulseTriggerType Enumeration

Specifies the pulse trigger type.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXPulseTriggerType
```

```text
Public Enumeration RFmxVnaMXPulseTriggerType
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| None | 0 |  |
| DigitalEdge | 1 |  |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/b9dfe317-c8cf-9f33-dcce-329dd1ea254d.htm language=enus -->
## TOPIC 00076: rfmxvnadotnet/html/b9dfe317-c8cf-9f33-dcce-329dd1ea254d.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/b9dfe317-c8cf-9f33-dcce-329dd1ea254d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/b9dfe317-c8cf-9f33-dcce-329dd1ea254d.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXWavesConfiguration.SetReceiverPort Method

RFmxVnaMXWavesConfigurationSetReceiverPort Method

Sets the receiver port name for wave measurement.Incident and scattered waves are denoted by "a_(receiver port name)_(receiver port name)" and "b_(receiver port name)_(receiver port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.For example, to measure 'b_port2_port1', set (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_WAVES_RECEIVER.html')")RFMXVNA_ATTR_WAVES_RECEIVER(/a) to (format type="bold")Test (0)(/format), set this method to "port2" and (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_WAVES_SOURCE_PORT.html')")RFMXVNA_ATTR_WAVES_SOURCE_PORT(/a) to "port1".

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetReceiverPort(
	string selectorString,
	string value
)
```

```text
Public Function SetReceiverPort ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the receiver port name for wave measurement.Incident and scattered waves are denoted by "a_(receiver port name)_(receiver port name)" and "b_(receiver port name)_(receiver port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.For example, to measure 'b_port2_port1', set (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_WAVES_RECEIVER.html')")RFMXVNA_ATTR_WAVES_RECEIVER(/a) to (format type="bold")Test (0)(/format), set this method to "port2" and (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_WAVES_SOURCE_PORT.html')")RFMXVNA_ATTR_WAVES_SOURCE_PORT(/a) to "port1".

###### Return Value

Int32

##### Remarks

WavesReceiverPort

##### See Also

###### Reference

RFmxVnaMXWavesConfiguration Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/b9ed14db-3d5c-a474-b373-e2f8f76bf260.htm language=enus -->
## TOPIC 00077: rfmxvnadotnet/html/b9ed14db-3d5c-a474-b373-e2f8f76bf260.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/b9ed14db-3d5c-a474-b373-e2f8f76bf260.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/b9ed14db-3d5c-a474-b373-e2f8f76bf260.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetCorrectionPortSubsetPorts Method

RFmxVnaMXSetCorrectionPortSubsetPorts Method

Sets the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to (format type="bold")True(/format).

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCorrectionPortSubsetPorts(
	string selectorString,
	string[] value
)
```

```text
Public Function SetCorrectionPortSubsetPorts ( 
	selectorString As String,
	value As String()
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Specifies the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to (format type="bold")True(/format).

###### Return Value

Int32

##### Remarks

CorrectionPortSubsetPorts

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/baa68585-39e6-dac1-596c-32cd7a39bb01.htm language=enus -->
## TOPIC 00078: rfmxvnadotnet/html/baa68585-39e6-dac1-596c-32cd7a39bb01.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/baa68585-39e6-dac1-596c-32cd7a39bb01.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/baa68585-39e6-dac1-596c-32cd7a39bb01.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetAttributeBool Method

RFmxVnaMXSetAttributeBool Method

Sets the value of a Bool attribute.

Namespace:

NationalInstruments.RFmx.VnaMX

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

- **selectorString String**
  - Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string.
- **attributeIdentifier Int32**
  - Specifies the ID of an attribute.
- **value Boolean**
  - Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/bb4e57e3-6110-1e24-a1a1-76cd378a1fe5.htm language=enus -->
## TOPIC 00079: rfmxvnadotnet/html/bb4e57e3-6110-1e24-a1a1-76cd378a1fe5.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/bb4e57e3-6110-1e24-a1a1-76cd378a1fe5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/bb4e57e3-6110-1e24-a1a1-76cd378a1fe5.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetTriggerType Method

RFmxVnaMXGetTriggerType Method

Gets the trigger type.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTriggerType(
	string selectorString,
	out RFmxVnaMXTriggerType value
)
```

```text
Public Function GetTriggerType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxVnaMXTriggerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXTriggerType**
  - Upon return, contains the trigger type.

###### Return Value

Int32

##### Remarks

TriggerType

None

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/bc65c585-d145-bee5-3934-411c898ec9ac.htm language=enus -->
## TOPIC 00080: rfmxvnadotnet/html/bc65c585-d145-bee5-3934-411c898ec9ac.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/bc65c585-d145-bee5-3934-411c898ec9ac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/bc65c585-d145-bee5-3934-411c898ec9ac.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetNumberOfSegments Method

RFmxVnaMXGetNumberOfSegments Method

Gets the number of segments.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfSegments(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfSegments ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Int32**
  - Upon return, contains the number of segments.

###### Return Value

Int32

##### Remarks

NumberOfSegments

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/be8b722a-45fd-4d68-ab10-132a8de9a44b.htm language=enus -->
## TOPIC 00081: rfmxvnadotnet/html/be8b722a-45fd-4d68-ab10-132a8de9a44b.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/be8b722a-45fd-4d68-ab10-132a8de9a44b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/be8b722a-45fd-4d68-ab10-132a8de9a44b.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetTriggerType Method

RFmxVnaMXSetTriggerType Method

Sets the trigger type.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerType(
	string selectorString,
	RFmxVnaMXTriggerType value
)
```

```text
Public Function SetTriggerType ( 
	selectorString As String,
	value As RFmxVnaMXTriggerType
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value RFmxVnaMXTriggerType**
  - Specifies the trigger type.

###### Return Value

Int32

##### Remarks

TriggerType

None

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/c11f426e-ea15-3efc-ed0f-e2b599ea278c.htm language=enus -->
## TOPIC 00082: rfmxvnadotnet/html/c11f426e-ea15-3efc-ed0f-e2b599ea278c.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/c11f426e-ea15-3efc-ed0f-e2b599ea278c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/c11f426e-ea15-3efc-ed0f-e2b599ea278c.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.DeselectActiveCalset Method

RFmxVnaMXDeselectActiveCalset Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int DeselectActiveCalset(
	string selectorString
)
```

```text
Public Function DeselectActiveCalset ( 
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

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/c1d278ef-54c7-b54d-913d-a36f35c5dff0.htm language=enus -->
## TOPIC 00083: rfmxvnadotnet/html/c1d278ef-54c7-b54d-913d-a36f35c5dff0.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/c1d278ef-54c7-b54d-913d-a36f35c5dff0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/c1d278ef-54c7-b54d-913d-a36f35c5dff0.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetCorrectionCalibrationCalkitElectronicResourceName Method

RFmxVnaMXGetCorrectionCalibrationCalkitElectronicResourceName Method

Gets the resource name of the electronic calibration module (vCal) used for calibration.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCorrectionCalibrationCalkitElectronicResourceName(
	string selectorString,
	out string value
)
```

```text
Public Function GetCorrectionCalibrationCalkitElectronicResourceName ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the port number and signal number. Example: "signal0" or "signal0/port0". You can use the BuildPortString(String, String) method to build the selector string.
- **value String**
  - Upon return, contains the resource name of the electronic calibration module (vCal) used for calibration.

###### Return Value

Int32

##### Remarks

CorrectionCalibrationCalkitElectronicResourceName

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/c2757677-8c17-ed66-b64e-74d53f5f88fb.htm language=enus -->
## TOPIC 00084: rfmxvnadotnet/html/c2757677-8c17-ed66-b64e-74d53f5f88fb.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/c2757677-8c17-ed66-b64e-74d53f5f88fb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/c2757677-8c17-ed66-b64e-74d53f5f88fb.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsResults.FetchComplexData Method

RFmxVnaMXSParamsResultsFetchComplexData Method

RFMXVNA_ATTR_SPARAMS_FORMAT

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchComplexData(
	string selectorString,
	double timeout,
	ref ComplexSingle[] complexData
)
```

```text
Public Function FetchComplexData ( 
	selectorString As String,
	timeout As Double,
	ByRef complexData As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name, and S-Parameter number. If you do not specify the result name, the default result instance is used. Example:"sparam0""result::r1/sparam0" You can use the BuildSParameterString(String, Int32) method to build the selector string.
- **timeout Double**
  - Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete.
- **complexData ComplexSingle**
  - Upon return, contains the measured S-Parameter complex array corresponding to the FrequencyList.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMXSParamsResults Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/c3ed1a2c-0d7d-9cc5-f796-26b5cf7c4df0.htm language=enus -->
## TOPIC 00085: rfmxvnadotnet/html/c3ed1a2c-0d7d-9cc5-f796-26b5cf7c4df0.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/c3ed1a2c-0d7d-9cc5-f796-26b5cf7c4df0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/c3ed1a2c-0d7d-9cc5-f796-26b5cf7c4df0.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParams Class

RFmxVnaMXSParams Class

Represents the SParams measurement.

##### Inheritance Hierarchy

RFmxVnaMXSubObject

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxVnaMXSParams : RFmxVnaMXSubObject
```

```text
Public NotInheritable Class RFmxVnaMXSParams
	Inherits RFmxVnaMXSubObject
```

The RFmxVnaMXSParams type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxVnaMXSParamsConfiguration instance that provides methods to configure the SParams measurement. |
|  | Results | Gets the RFmxVnaMXSParamsResults instance that provides methods to fetch and read the SParams measurement results. |

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

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/cde1f59c-8a4b-b9a5-6a8c-af81bcc460b8.htm language=enus -->
## TOPIC 00086: rfmxvnadotnet/html/cde1f59c-8a4b-b9a5-6a8c-af81bcc460b8.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/cde1f59c-8a4b-b9a5-6a8c-af81bcc460b8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/cde1f59c-8a4b-b9a5-6a8c-af81bcc460b8.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXWavesReceiver Enumeration

RFmxVnaMXWavesReceiver Enumeration

Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port.Incident and scattered waves are denoted by "a_(receiver port name)_(receiver port name)" and "b_(receiver port name)_(receiver port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure 'b_port2_port1', set this method to (format type="bold")Test (0)(/format), (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_WAVES_RECEIVER_PORT.html')")RFMXVNA_ATTR_WAVES_RECEIVER_PORT(/a) to "port2" and (a href="javascript:launchmergedhelp('rfmxvna.chm', 'rfmxvnacvi.chm', 'RFMXVNA_ATTR_WAVES_SOURCE_PORT.html')")RFMXVNA_ATTR_WAVES_SOURCE_PORT(/a) to "port1".

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXWavesReceiver
```

```text
Public Enumeration RFmxVnaMXWavesReceiver
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| Test | 0 | Measures the wave on the test receiver. |
| Reference | 1 | Measures the wave on the test receiver. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/cf492d69-7361-c85b-2501-ceebf27ec026.htm language=enus -->
## TOPIC 00087: rfmxvnadotnet/html/cf492d69-7361-c85b-2501-ceebf27ec026.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/cf492d69-7361-c85b-2501-ceebf27ec026.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/cf492d69-7361-c85b-2501-ceebf27ec026.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXSParamsResults Class

RFmxVnaMXSParamsResults Class

Provides methods to fetch and read the SParams measurement results.

##### Inheritance Hierarchy

RFmxVnaMXSubObject

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxVnaMXSParamsResults : RFmxVnaMXSubObject
```

```text
Public NotInheritable Class RFmxVnaMXSParamsResults
	Inherits RFmxVnaMXSubObject
```

The RFmxVnaMXSParamsResults type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object.(Inherited from Object) |
|  | FetchComplexData | Fetches the S-Parameter data for the S-Parameters whose RFMXVNA_ATTR_SPARAMS_FORMAT is RFMXVNA_VAL_Complex. Use "sparam(n)" as the selector string to read results from this method. |
|  | FetchRealData | Fetches the S-Parameter data for the S-Parameters whose RFMXVNA_ATTR_SPARAMS_FORMAT is RFMXVNA_VAL_Magnitude or RFMXVNA_VAL_Phase. Use "sparam(n)" as the selector string to read results from this method. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object) |
|  | GetType | Gets the Type of the current instance.(Inherited from Object) |
|  | ToString | Returns a string that represents the current object.(Inherited from Object) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/d2facdaa-8cac-5639-5f41-c0738b4c89a7.htm language=enus -->
## TOPIC 00088: rfmxvnadotnet/html/d2facdaa-8cac-5639-5f41-c0738b4c89a7.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/d2facdaa-8cac-5639-5f41-c0738b4c89a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/d2facdaa-8cac-5639-5f41-c0738b4c89a7.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.BuildCalstepString Method

RFmxVnaMXBuildCalstepString Method

CalibrationAcquire(String, Double)

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildCalstepString(
	string selectorString,
	int calstepNumber
)
```

```text
Public Shared Function BuildCalstepString ( 
	selectorString As String,
	calstepNumber As Integer
) As String
```

###### Parameters

- **selectorString String**
  - Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"result::myresult1" You can use the BuildResultString(String) method to build the selector string.
- **calstepNumber Int32**
  - Specifies the calibration step number for building the selector string.

###### Return Value

String

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/dc9d6289-2b91-e9e8-0513-93d921305585.htm language=enus -->
## TOPIC 00089: rfmxvnadotnet/html/dc9d6289-2b91-e9e8-0513-93d921305585.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/dc9d6289-2b91-e9e8-0513-93d921305585.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/dc9d6289-2b91-e9e8-0513-93d921305585.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPulseDigitalEdgeTriggerSource Method

RFmxVnaMXGetPulseDigitalEdgeTriggerSource Method

Gets the source of the digital edge pulse trigger.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulseDigitalEdgeTriggerSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetPulseDigitalEdgeTriggerSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value String**
  - Upon return, contains the source of the digital edge pulse trigger.

###### Return Value

Int32

##### Remarks

PulseDigitalEdgeTriggerSource

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/deaa0a83-4190-1308-dada-3520efa7238f.htm language=enus -->
## TOPIC 00090: rfmxvnadotnet/html/deaa0a83-4190-1308-dada-3520efa7238f.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/deaa0a83-4190-1308-dada-3520efa7238f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/deaa0a83-4190-1308-dada-3520efa7238f.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability Method

RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability Method

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(
	string selectorString,
	out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability sParameterAvailability
)
```

```text
Public Function CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability ( 
	selectorString As String,
	<OutAttribute> ByRef sParameterAvailability As RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(String, String) method to build the selector string.
- **sParameterAvailability RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability**
  - Upon return, contains the S-Parameter availability.

###### Return Value

Int32

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/e617e1a4-9976-4f07-51a8-a0eda6a25040.htm language=enus -->
## TOPIC 00091: rfmxvnadotnet/html/e617e1a4-9976-4f07-51a8-a0eda6a25040.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/e617e1a4-9976-4f07-51a8-a0eda6a25040.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/e617e1a4-9976-4f07-51a8-a0eda6a25040.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.SetSegmentStartFrequency Method

RFmxVnaMXSetSegmentStartFrequency Method

Sets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSegmentStartFrequency(
	string selectorString,
	double value
)
```

```text
Public Function SetSegmentStartFrequency ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Specifies the segment number and signal number. Example: "signal0" or "signal0/segment0". You can use the BuildSegmentString(String, Int32) method to build the selector string.
- **value Double**
  - Specifies the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SegmentStartFrequency

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/f048b180-455b-25c9-3b2c-9a20585e53d9.htm language=enus -->
## TOPIC 00092: rfmxvnadotnet/html/f048b180-455b-25c9-3b2c-9a20585e53d9.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/f048b180-455b-25c9-3b2c-9a20585e53d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/f048b180-455b-25c9-3b2c-9a20585e53d9.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXPulseModeEnabled Enumeration

RFmxVnaMXPulseModeEnabled Enumeration

Specifies whether to enable pulse mode for VNA measurement.

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxVnaMXPulseModeEnabled
```

```text
Public Enumeration RFmxVnaMXPulseModeEnabled
```

##### Members

| Member name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables pulse mode. |
| True | 1 | The measurement enables pulse mode. |

##### See Also

###### Reference

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/f3ea2b5b-7214-6669-27d0-a269d8132c61.htm language=enus -->
## TOPIC 00093: rfmxvnadotnet/html/f3ea2b5b-7214-6669-27d0-a269d8132c61.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/f3ea2b5b-7214-6669-27d0-a269d8132c61.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/f3ea2b5b-7214-6669-27d0-a269d8132c61.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMXExtension.GetVnaSignalConfiguration(RFmxInstrMX, String) Method

RFmxVnaMXExtensionGetVnaSignalConfiguration(RFmxInstrMX, String) Method

Creates a Vna signal configuration for specified signal name. Existing Vna signal configuration is
 returned if specified signal name exists.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxVnaMX GetVnaSignalConfiguration(
	this RFmxInstrMX instrSession,
	string signalName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetVnaSignalConfiguration ( 
	instrSession As RFmxInstrMX,
	signalName As String
) As RFmxVnaMX
```

###### Parameters

- **instrSession RFmxInstrMX**
  - Specifies an RFmxInstr session.
- **signalName String**
  - Specifies a signal name.

###### Return Value

RFmxVnaMX

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxVnaMXExtension Class

GetVnaSignalConfiguration Overload

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-vna-dotnet path=rfmxvnadotnet/html/fd73e3dd-df65-93ab-29f0-03c0014eee38.htm language=enus -->
## TOPIC 00094: rfmxvnadotnet/html/fd73e3dd-df65-93ab-29f0-03c0014eee38.htm

- bundle_id: `rfmx-vna-dotnet`
- source_path: `rfmxvnadotnet/html/fd73e3dd-df65-93ab-29f0-03c0014eee38.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-dotnet/raw/resource/enus/rfmxvnadotnet/html/fd73e3dd-df65-93ab-29f0-03c0014eee38.htm
- document_id: `rfmx-vna-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxVnaMX.GetPulsePeriod Method

RFmxVnaMXGetPulsePeriod Method

PulseModeEnabled

True

Namespace:

NationalInstruments.RFmx.VnaMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPulsePeriod(
	string selectorString,
	out double value
)
```

```text
Public Function GetPulsePeriod ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString String**
  - Pass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value Double**
  - Upon return, contains the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PulsePeriod

##### See Also

###### Reference

RFmxVnaMX Class

NationalInstruments.RFmx.VnaMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
