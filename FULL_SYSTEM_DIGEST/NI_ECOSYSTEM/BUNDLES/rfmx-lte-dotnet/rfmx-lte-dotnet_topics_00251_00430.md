# NI DOCUMENT BUNDLE: rfmx-lte-dotnet

<!--NI_BUNDLE_CHUNK bundle=rfmx-lte-dotnet start=251 end=430 -->
<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a4e10717-a302-3242-3511-476e955b1f7c.htm language=enus -->
## TOPIC 00251: rfmxltedotnet/html/a4e10717-a302-3242-3511-476e955b1f7c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a4e10717-a302-3242-3511-476e955b1f7c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a4e10717-a302-3242-3511-476e955b1f7c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxp.Results Property

RFmxLteMXTxpResults Property

RFmxLteMXTxpResults

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXTxpResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxLteMXTxpResults
	Get
```

###### Property Value

RFmxLteMXTxpResults

##### See Also

###### Reference

RFmxLteMXTxp Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a55d3fc2-114b-6ad7-0326-e52b54f44f8b.htm language=enus -->
## TOPIC 00252: rfmxltedotnet/html/a55d3fc2-114b-6ad7-0326-e52b54f44f8b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a55d3fc2-114b-6ad7-0326-e52b54f44f8b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a55d3fc2-114b-6ad7-0326-e52b54f44f8b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetRbwFilterBandwidth Method

RFmxLteMXChpConfigurationSetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxLteMXChpRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ChpRbwFilterBandwidth

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a66cef2c-cb13-bb7a-359d-a95e2bf2b277.htm language=enus -->
## TOPIC 00253: rfmxltedotnet/html/a66cef2c-cb13-bb7a-359d-a95e2bf2b277.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a66cef2c-cb13-bb7a-359d-a95e2bf2b277.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a66cef2c-cb13-bb7a-359d-a95e2bf2b277.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.GetSweepTimeInterval Method

RFmxLteMXChpConfigurationGetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxLteMXChpSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXChpSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

ChpSweepTimeInterval

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a6abcc69-07ef-c84e-bea9-14d4c71f6286.htm language=enus -->
## TOPIC 00254: rfmxltedotnet/html/a6abcc69-07ef-c84e-bea9-14d4c71f6286.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a6abcc69-07ef-c84e-bea9-14d4c71f6286.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a6abcc69-07ef-c84e-bea9-14d4c71f6286.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXDownlinkUserDefinedRatio Enumeration

RFmxLteMXDownlinkUserDefinedRatio Enumeration

3GPP TS 36.213

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXDownlinkUserDefinedRatio
```

```text
Public Enumeration RFmxLteMXDownlinkUserDefinedRatio
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PB0 | 0 | Specifies a ratio of 1 for one antenna port and 5/4 for two or four antenna ports. |
|  | PB1 | 1 | Specifies a ratio of 4/5 for one antenna port and 1 for two or four antenna ports. |
|  | PB2 | 2 | Specifies a ratio of 3/5 for one antenna port and 3/4 for two or four antenna ports. |
|  | PB3 | 3 | Specifies a ratio of 2/5 for one antenna port and 1/2 for two or four antenna ports. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a778b4f1-8d05-96cd-b254-15aa37f7941c.htm language=enus -->
## TOPIC 00255: rfmxltedotnet/html/a778b4f1-8d05-96cd-b254-15aa37f7941c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a778b4f1-8d05-96cd-b254-15aa37f7941c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a778b4f1-8d05-96cd-b254-15aa37f7941c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetLaaDownlinkNumberOfEndingSymbols Method

RFmxLteMXComponentCarrierGetLaaDownlinkNumberOfEndingSymbols Method

3GPP 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLaaDownlinkNumberOfEndingSymbols(
	string selectorString,
	out RFmxLteMXLaaDownlinkNumberOfEndingSymbols value
)
```

```text
Public Function GetLaaDownlinkNumberOfEndingSymbols ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXLaaDownlinkNumberOfEndingSymbols
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXLaaDownlinkNumberOfEndingSymbols Upon return, contains the number of ending symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the 3GPP 36.211 specification for more information regarding LAA downlink number of ending symbols.

###### Return Value

Int32

##### Remarks

LaaDownlinkNumberOfEndingSymbols

EndingSymbols14

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a77c6aed-cf92-7875-c523-22a3f4add417.htm language=enus -->
## TOPIC 00256: rfmxltedotnet/html/a77c6aed-cf92-7875-c523-22a3f4add417.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a77c6aed-cf92-7875-c523-22a3f4add417.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a77c6aed-cf92-7875-c523-22a3f4add417.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.ConfigureUplinkMaskType Method

RFmxLteMXSemConfigurationConfigureUplinkMaskType Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureUplinkMaskType(
	string selectorString,
	RFmxLteMXSemUplinkMaskType uplinkMaskType
)
```

```text
Public Function ConfigureUplinkMaskType ( 
	selectorString As String,
	uplinkMaskType As RFmxLteMXSemUplinkMaskType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **uplinkMaskType**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemUplinkMaskType Specifies the standard-defined spectrum emission mask used in the measurement for uplink. The following mask types are supported: general, NS_03orNS_11orNS_20orNS_21, NS_04, NS_06orNS_07, CA_NS_04, custom, generalCAClassB, CA_NC_NS_01, NS_27, and NS_35. Each mask type refers to a different Network Signalled (NS) value. CA_NS_04 and CA_NC_NS_01 refers to carrier aggregation case. You must set the mask type to CUSTOM to configure the custom offset masks. Refer to section 6.6.2.1 of the 3GPP 36.521 specification for more information about standard-defined mask types.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a87d63ee-024c-a978-16f1-39a5e01c44d9.htm language=enus -->
## TOPIC 00257: rfmxltedotnet/html/a87d63ee-024c-a978-16f1-39a5e01c44d9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a87d63ee-024c-a978-16f1-39a5e01c44d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a87d63ee-024c-a978-16f1-39a5e01c44d9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPsschResourceBlockOffset Method

RFmxLteMXComponentCarrierSetPsschResourceBlockOffset Method

Sets the starting resource block number of a physical sidelink shared channel (PSSCH) allocation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPsschResourceBlockOffset(
	string selectorString,
	int value
)
```

```text
Public Function SetPsschResourceBlockOffset ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the starting resource block number of a physical sidelink shared channel (PSSCH) allocation.

###### Return Value

Int32

##### Remarks

PsschResourceBlockOffset

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a8935e27-a569-2bd3-ffca-c7fd02e34508.htm language=enus -->
## TOPIC 00258: rfmxltedotnet/html/a8935e27-a569-2bd3-ffca-c7fd02e34508.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a8935e27-a569-2bd3-ffca-c7fd02e34508.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a8935e27-a569-2bd3-ffca-c7fd02e34508.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.ConfigureAutoResourceBlockDetectionEnabled Method

RFmxLteMXComponentCarrierConfigureAutoResourceBlockDetectionEnabled Method

SetPuschModulationType(String, RFmxLteMXPuschModulationType)

SetPuschNumberOfResourceBlockClusters(String, Int32)

SetPuschResourceBlockOffset(String, Int32)

SetPuschNumberOfResourceBlocks(String, Int32)

SetLinkDirection(String, RFmxLteMXLinkDirection)

Downlink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAutoResourceBlockDetectionEnabled(
	string selectorString,
	RFmxLteMXAutoResourceBlockDetectionEnabled autoResourceBlockDetectionEnabled
)
```

```text
Public Function ConfigureAutoResourceBlockDetectionEnabled ( 
	selectorString As String,
	autoResourceBlockDetectionEnabled As RFmxLteMXAutoResourceBlockDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **autoResourceBlockDetectionEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoResourceBlockDetectionEnabledSpecifies whether the values of the PUSCH Mod Type, PUSCH Num Clusters, PUSCH RB Offset, and PUSCH Num RBs methods are automatically detected by the measurement or if you specify the values of these methods.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/a8b33996-0883-6145-c643-59ef6319c441.htm language=enus -->
## TOPIC 00259: rfmxltedotnet/html/a8b33996-0883-6145-c643-59ef6319c441.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/a8b33996-0883-6145-c643-59ef6319c441.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/a8b33996-0883-6145-c643-59ef6319c441.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX Methods

RFmxLteMX Methods

The [RFmxLteMX](708db61e-6a1e-62ef-3f27-ce3f4b3ab233.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(String, String) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either IQ or IQorSpectral. When using the Analysis-Only mode in RFmxLTE, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx LTE Commit method. |
|  | AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum waveform that you specify in spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either spectral or IQorSpectral. When using the Analysis-Only mode in RFmxLTE, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx LTE Commit method. |
|  | AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(String, Double) method. Use this method to calculate an approximate setting for the reference level. The RFmxLTE Auto Level method completes the following tasks: Resets the mixer level, mixer level offset, and IF output power offset. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings. Iterates to adjust the reference level based on the input signal peak power. Uses immediate triggering and restores the trigger settings back to user setting after the execution. You can also specify the starting reference level using SetAutoLevelInitialReferenceLevel(String, Double) method. When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxLTE Auto Level method. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this method; thus reducing wear and tear, and maximizing the life time of the attenuator. |
|  | BuildCarrierString | Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch methods and methods. |
|  | BuildClusterString | Creates a cluster string to use as a selector string with the ModAcc cluster configuration or fetch methods and methods. |
|  | BuildListStepString | Creates the list step string. |
|  | BuildListString | Creates the list string. |
|  | BuildOffsetString | Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch methods and methods. |
|  | BuildPdschString | Creates a PDSCH string to use as a selector string with the configuration or fetch methods and methods. |
|  | BuildResultString | Creates selector string for use with configuration or fetch. |
|  | BuildSubblockString | Creates a subblock string to use as a selector string with the subblock configuration or fetch methods and methods. |
|  | BuildSubframeString | Creates a subframe string to use as a selector string with the configuration or fetch methods and methods. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current signal instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | CloneSignalConfiguration | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxLTE commits settings to the hardware when you call the Initiate(String, String) method. |
|  | ConfigureAutoDmrsDetectionEnabled | Configures whether the demodulation reference signal (DMRS) parameters are configured by a user or automatically detected by a measurement. |
|  | ConfigureBand | Configures the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
|  | ConfigureDuplexScheme | Configures the duplexing technique of the signal being measured. |
|  | ConfigureeNodeBCategory | Configures the eNodeB category of the signal being measured. |
|  | ConfigureExternalAttenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
|  | ConfigureFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureFrequencyEarfcn | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
|  | ConfigureLinkDirection | Configures the link direction of the signal being measured. |
|  | ConfigureNumberOfComponentCarriers | Configures the number of component carriers within a subblock. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureNumberOfDutAntennas | Configures the number of physical antennas used for transmission by the DUT in a MIMO setup. |
|  | ConfigureNumberOfSubblocks | Configures the number of subblocks. |
|  | ConfigureReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
|  | ConfigureRF | Configures the RF methods of the signal specified by the selector string. |
|  | ConfigureSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
|  | ConfigureTransmitAntennaToAnalyze | Configures the current physical antenna of the DUT in the MIMO setup being tested. |
|  | DeleteSignalConfiguration | Deletes an instance of a signal. |
|  | DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
|  | Dispose | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAcquisitionBandwidthOptimizationEnabled | Gets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |
|  | GetAllNamedResultNames | Gets the named result names of the signal that you specify in the selectorString parameter. |
|  | GetAttributeBool | Gets the value of a Bool attribute. |
|  | GetAttributeDouble | Gets the value of a Double attribute. |
|  | GetAttributeInt | Gets the value of an RFmx 32-bit integer (int32) attribute. |
|  | GetAttributeString | Gets the value of a of an RFmx string. |
|  | GetAutoDmrsDetectionEnabled | Gets whether you configure the values of the demodulation reference signal (DMRS) parameters, such as SetUplinkGroupHoppingEnabled(String, RFmxLteMXUplinkGroupHoppingEnabled), SetUplinkSequenceHoppingEnabled(String, RFmxLteMXUplinkSequenceHoppingEnabled), SetCellId(String, Int32), SetPuschNDmrs1(String, Int32), SetPuschNDmrs2(String, Int32), and SetPuschDeltaSequenceShift(String, Int32) properties, or if the values of these properties are auto-detected by the measurement. |
|  | GetAutoLevelInitialReferenceLevel | Gets the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | GetBand | Gets the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock, as defined in section 5.2 of the 3GPP TS 36.521 specification. |
|  | GetCenterFrequency | For a single carrier, this method specifies the center frequency of the acquired RF signal. |
|  | GetCenterFrequencyForLimits | Gets the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. |
|  | GetDigitalEdgeTriggerEdge | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | GetDigitalEdgeTriggerSource | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | GetDuplexScheme | Gets the duplexing technique of the signal being measured. |
|  | GeteNodeBCategory | Gets the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. |
|  | GetErrorString | Converts the status code returned by an RFmxLTE function into a string. |
|  | GetExternalAttenuation | Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetIQPowerEdgeTriggerLevel | Gets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxLteMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerLevelType | Gets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSlope | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetIQPowerEdgeTriggerSource | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | GetLimitedConfigurationChange | Gets the set of properties that are considered by RFmx driver in the locked signal configuration state. |
|  | GetLinkDirection | Gets the link direction of the received signal. |
|  | GetListStepTimerDuration | Gets the duration of a given list step in units specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). |
|  | GetListStepTimerOffset | Gets the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent |
|  | GetListStepTimerUnit | Gets the units in which SetListStepTimerDuration(String, Double) and SetListStepTimerOffset(String, Double) are specified. |
|  | GetMiConfiguration | Gets whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the SetDuplexScheme(String, RFmxLteMXDuplexScheme) method to Tdd. |
|  | GetNumberOfDutAntennas | Gets the number of physical antennas available at the DUT for transmission in a MIMO setup. |
|  | GetNumberOfSubblocks | Gets the number of subblocks that are configured in intra-band non-contiguous carrier aggregation. |
|  | GetPuschPower | Obsolete. Gets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | GetReferenceLevel | Gets the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. |
|  | GetReferenceLevelHeadroom | Gets the margin RFmx driver adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | GetResultFetchTimeout | Gets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. |
|  | GetSelectedPorts | Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | GetSpecialSubframeConfiguration | Gets the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. |
|  | GetSubblockFrequency | Gets the offset of the subblock from the center frequency. This value is expressed in Hz. |
|  | GetTransmitAntennaToAnalyze | Gets the physical antenna connected to the analyzer. |
|  | GetTransmitterArchitecture | Gets the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. |
|  | GetTriggerDelay | Gets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre trigger samples. If the delay is positive, the measurement acquires post trigger samples. |
|  | GetTriggerMinimumQuietTimeDuration | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | GetTriggerMinimumQuietTimeMode | Gets whether the measurement computes the minimum quiet time used for triggering. |
|  | GetTriggerType | Gets the trigger type. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUplinkDownlinkConfiguration | Gets the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. |
|  | GetWarning | Gets the latest warning code and description. |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetAttribute | Resets the attribute to its default value. |
|  | ResetToDefault | Resets a signal to the default values. |
|  | SelectMeasurements | Specifies the measurements that you want to enable. |
|  | SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxLTE_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configure an invalid trigger. You have not previously called the Initiate(String, String) method. |
|  | SetAcquisitionBandwidthOptimizationEnabled | Sets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |
|  | SetAttributeBool | Sets the value of a Bool attribute. |
|  | SetAttributeDouble | Sets the value of a Double attribute. |
|  | SetAttributeInt | Sets the value of a Int attribute. |
|  | SetAttributeString | Sets the value of a String attribute. |
|  | SetAutoDmrsDetectionEnabled | Sets whether you configure the values of the demodulation reference signal (DMRS) parameters, such as SetUplinkGroupHoppingEnabled(String, RFmxLteMXUplinkGroupHoppingEnabled), SetUplinkSequenceHoppingEnabled(String, RFmxLteMXUplinkSequenceHoppingEnabled), SetCellId(String, Int32), SetPuschNDmrs1(String, Int32), SetPuschNDmrs2(String, Int32), and SetPuschDeltaSequenceShift(String, Int32) properties, or if the values of these properties are auto-detected by the measurement. |
|  | SetAutoLevelInitialReferenceLevel | Sets the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
|  | SetBand | Sets the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock, as defined in section 5.2 of the 3GPP TS 36.521 specification. |
|  | SetCenterFrequency | For a single carrier, this method specifies the center frequency of the acquired RF signal. |
|  | SetCenterFrequencyForLimits | Sets the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this method, the measurement internally uses RFmxLteMX.SetCenterFrequency for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. |
|  | SetDigitalEdgeTriggerEdge | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | SetDigitalEdgeTriggerSource | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to DigitalEdge. |
|  | SetDuplexScheme | Sets the duplexing technique of the signal being measured. |
|  | SeteNodeBCategory | Sets the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. |
|  | SetExternalAttenuation | Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation. |
|  | SetIQPowerEdgeTriggerLevel | Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(String, RFmxLteMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerLevelType | Sets the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSlope | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetIQPowerEdgeTriggerSource | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge. |
|  | SetLimitedConfigurationChange | Sets the set of properties that are considered by RFmx driver in the locked signal configuration state. |
|  | SetLinkDirection | Sets the link direction of the received signal. |
|  | SetListStepTimerDuration | Sets the duration of a given list step in units specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). |
|  | SetListStepTimerOffset | Sets the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent. |
|  | SetListStepTimerUnit | Sets the units in which SetListStepTimerDuration(String, Double) and SetListStepTimerOffset(String, Double) are specified. |
|  | SetMiConfiguration | Sets whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the SetDuplexScheme(String, RFmxLteMXDuplexScheme) method to Tdd. |
|  | SetNumberOfDutAntennas | Sets the number of physical antennas available at the DUT for transmission in a MIMO setup. |
|  | SetNumberOfSubblocks | Sets the number of subblocks that are configured in intra-band non-contiguous carrier aggregation. |
|  | SetPuschPower | Obsolete. Sets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | SetReferenceLevel | Sets the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. |
|  | SetReferenceLevelHeadroom | Sets the margin RFmx driver adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860. |
|  | SetResultFetchTimeout | Sets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. |
|  | SetSelectedPorts | Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 |
|  | SetSpecialSubframeConfiguration | Sets the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. |
|  | SetSubblockFrequency | Sets the offset of the subblock from the center frequency. This value is expressed in Hz. |
|  | SetTransmitAntennaToAnalyze | Sets the physical antenna connected to the analyzer. |
|  | SetTransmitterArchitecture | Sets the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. |
|  | SetTriggerDelay | Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre trigger samples. If the delay is positive, the measurement acquires post trigger samples. |
|  | SetTriggerMinimumQuietTimeDuration | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
|  | SetTriggerMinimumQuietTimeMode | Sets whether the measurement computes the minimum quiet time used for triggering. |
|  | SetTriggerType | Sets the trigger type. |
|  | SetUplinkDownlinkConfiguration | Sets the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/aa28d6a9-fc71-ae5a-8089-46f6edd83560.htm language=enus -->
## TOPIC 00260: rfmxltedotnet/html/aa28d6a9-fc71-ae5a-8089-46f6edd83560.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/aa28d6a9-fc71-ae5a-8089-46f6edd83560.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/aa28d6a9-fc71-ae5a-8089-46f6edd83560.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetSrsnSrsCS Method

RFmxLteMXComponentCarrierSetSrsnSrsCS Method

nSRSCS

3GPP 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSrsnSrsCS(
	string selectorString,
	int value
)
```

```text
Public Function SetSrsnSrsCS ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the cyclic shift value nSRSCS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details.

###### Return Value

Int32

##### Remarks

SrsnSrsCS

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ac12bddb-e29b-7115-1d0c-b99be9393db4.htm language=enus -->
## TOPIC 00261: rfmxltedotnet/html/ac12bddb-e29b-7115-1d0c-b99be9393db4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ac12bddb-e29b-7115-1d0c-b99be9393db4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ac12bddb-e29b-7115-1d0c-b99be9393db4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetMeasurementEnabled Method

RFmxLteMXTxpConfigurationGetMeasurementEnabled Method

Gets whether to enable the Transmit Power (TXP) measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the Transmit Power (TXP) measurement.

###### Return Value

Int32

##### Remarks

TxpMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ad46bc43-513f-b800-97bd-36e9853703d2.htm language=enus -->
## TOPIC 00262: rfmxltedotnet/html/ad46bc43-513f-b800-97bd-36e9853703d2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ad46bc43-513f-b800-97bd-36e9853703d2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ad46bc43-513f-b800-97bd-36e9853703d2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetMeasurementInterval Method

RFmxLteMXTxpConfigurationGetMeasurementInterval Method

Gets the measurement interval. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeasurementInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the measurement interval. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TxpMeasurementInterval

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/adf2a5d9-e4d1-8cf0-cecb-feec68d43f6b.htm language=enus -->
## TOPIC 00263: rfmxltedotnet/html/adf2a5d9-e4d1-8cf0-cecb-feec68d43f6b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/adf2a5d9-e4d1-8cf0-cecb-feec68d43f6b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/adf2a5d9-e4d1-8cf0-cecb-feec68d43f6b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetPowerUnits Method

RFmxLteMXAcpConfigurationGetPowerUnits Method

Gets the units for the absolute power.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPowerUnits(
	string selectorString,
	out RFmxLteMXAcpPowerUnits value
)
```

```text
Public Function GetPowerUnits ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAcpPowerUnits
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpPowerUnitsUpon return, contains the units for the absolute power.

###### Return Value

Int32

##### Remarks

AcpPowerUnits

dBmByHz

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/adf4db5e-4551-31c8-df12-1cb72f1eb515.htm language=enus -->
## TOPIC 00264: rfmxltedotnet/html/adf4db5e-4551-31c8-df12-1cb72f1eb515.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/adf4db5e-4551-31c8-df12-1cb72f1eb515.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/adf4db5e-4551-31c8-df12-1cb72f1eb515.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.ConfigureSweepTime Method

RFmxLteMXSemConfigurationConfigureSweepTime Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSweepTime(
	string selectorString,
	RFmxLteMXSemSweepTimeAuto sweepTimeAuto,
	double sweepTimeInterval
)
```

```text
Public Function ConfigureSweepTime ( 
	selectorString As String,
	sweepTimeAuto As RFmxLteMXSemSweepTimeAuto,
	sweepTimeInterval As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **sweepTimeAuto**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemSweepTimeAutoSpecifies whether the measurement computes the sweep time.
- **sweepTimeInterval**
  - Type: SystemDouble Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ae15af79-799a-ef36-a57f-b020c299a166.htm language=enus -->
## TOPIC 00265: rfmxltedotnet/html/ae15af79-799a-ef36-a57f-b020c299a166.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ae15af79-799a-ef36-a57f-b020c299a166.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ae15af79-799a-ef36-a57f-b020c299a166.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetNoiseCalibrationAveragingAuto Method

RFmxLteMXChpConfigurationSetNoiseCalibrationAveragingAuto Method

Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCalibrationAveragingAuto(
	string selectorString,
	RFmxLteMXChpNoiseCalibrationAveragingAuto value
)
```

```text
Public Function SetNoiseCalibrationAveragingAuto ( 
	selectorString As String,
	value As RFmxLteMXChpNoiseCalibrationAveragingAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpNoiseCalibrationAveragingAutoSpecifies whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

###### Return Value

Int32

##### Remarks

ChpNoiseCalibrationAveragingAuto

True

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ae9a45bc-d0f7-cb7c-6f00-e5c4feed301a.htm language=enus -->
## TOPIC 00266: rfmxltedotnet/html/ae9a45bc-d0f7-cb7c-6f00-e5c4feed301a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ae9a45bc-d0f7-cb7c-6f00-e5c4feed301a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ae9a45bc-d0f7-cb7c-6f00-e5c4feed301a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetAveragingCount Method

RFmxLteMXAcpConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxLteMXAcpAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXAcpAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

AcpAveragingCount

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b0fa07ca-d58d-688c-ef92-590ff7f81b9d.htm language=enus -->
## TOPIC 00267: rfmxltedotnet/html/b0fa07ca-d58d-688c-ef92-590ff7f81b9d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b0fa07ca-d58d-688c-ef92-590ff7f81b9d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b0fa07ca-d58d-688c-ef92-590ff7f81b9d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier Class

RFmxLteMXComponentCarrier Class

Represents Component Carrier

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXComponentCarrier : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXComponentCarrier
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXComponentCarrier type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the componentCarrierBandwidth, componentCarrierFrequency, and cellID of the component carrier. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureArray | Configures an array of bandwidths, carrier offset frequencies, and cell IDs of component carriers. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureAutoNPuschChannelDetectionEnabled | Configures whether the values of the SetNPuschToneOffset(String, Int32), SetNPuschNumberOfTones(String, Int32), and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) methods for the NPUSCH channel are auto-detected by the measurement or specified by you. |
|  | ConfigureAutoResourceBlockDetectionEnabled | Configures whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) methods are automatically detected by the measurement or if you specify the values of these methods. The measurement ignores this method, when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Downlink. |
|  | ConfigureCellSpecificRatio | Configures the cellspecificratio parameter. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkAutoCellIDDetectionEnabled | Configures whether the cell ID is configured by the user or auto-detected by the measurement. |
|  | ConfigureDownlinkAutoChannelDetection | Configures whether the values of physical downlink shared channel (PDSCH) parameters, control channel signal powers, and physical control format indicator channel (PCFICH) CFI are configured by a user or auto-detected by the measurement. The measurement ignores this method, when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. |
|  | ConfigureDownlinkChannelConfigurationMode | Configures the downlink channel configuration mode. |
|  | ConfigureDownlinkNumberOfSubframes | Configures the number of unique subframes that are transmitted from the DUT. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkSynchronizationSignal | Configures the synchronization signal power relative to the cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkTestModel | Configures the E-UTRA Test Model type. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkTestModelArray | Configures an array of the E-UTRA Test Model type for each component carrier within the subblock. |
|  | ConfigureEmtcAnalysisEnabled | Configures whether the component carrier contains an enhanced machine type communications (Cat-M1 or Cat-M2) transmission. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNBIoTComponentCarrier | Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschDmrs | Configures the base sequence mode, base sequence index, cyclic shift, delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS and specifies whether group hopping is enabled. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschFormat | Configures the format of the narrowband physical uplink shared channel (NPUSCH). Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschStartingSlot | Configures the starting slot of the NPUSCH burst. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschTones | Configures the values of toneOffset, numberOfTones, and modulationType parameters for NPUSCH channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNumberOfPdschChannels | Configures the number of different physical downlink shared channel (PDSCH) allocations in a subframe. Use "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)" as the selector string to configure this method. |
|  | ConfigureNumberOfPuschResourceBlockClusters | Configures the number of clusters of resource allocations. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePbch | Configures the power of physical broadcast channel (PBCH) power relative to the cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePcfich | Configures the CFI and power parameters of the physical control format indicator channel (PCFICH). Use "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)" as the selector string to configure this method. |
|  | ConfigurePdcch | Configures the physical downlink control channel (PDCCH) power relative to the cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePdsch | Configures the codeword0 modulation type, resource block, and relative power of a physical downlink shared channel (PDSCH) allocation. Use "PDSCH(m)" or "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)/PDSCH(m)" as the selector string to configure this method. |
|  | ConfigurePhich | Configures the resource, duration, and power parameters of the physical hybrid-ARQ indicator channel (PHICH). Use "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)" as the selector string to configure this method. |
|  | ConfigurePsschModulationType | Configures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePsschResourceBlocks | Configures the start and number of resource blocks allocated for the physical sidelink shared channel (PSSCH) allocation. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePuschModulationType | Configures the modulation scheme used in the physical uplink shared channel (PUSCH) channel of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePuschResourceBlocks | Configures the start and number of resource blocks allocated for the physical uplink shared channel (PUSCH) cluster. Use "cluster(l)" or "carrier(k)" or "subblock(n)/carrier(k)/cluster(l)" as the selector string to configure this result. |
|  | ConfigureSpacing | Configures the componentCarrierSpacingType and componentCarrieratCenterFrequency parameters, which help to set the spacing between adjacent component carriers within a subblock. Use "subblock(n)" as the selector string to configure this method. Refer to the Channel Spacing and Carrier Frequency Offset Definition and Reference Frequency topics for more information about carrier spacing. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAutoControlChannelPowerDetectionEnabled | Gets whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported. |
|  | GetAutoNPuschChannelDetectionEnabled | Gets whether the values of the SetNPuschToneOffset(String, Int32), NPUSCH Number of Tones, and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) properties are auto-detected by the measurement or specified by you. |
|  | GetAutoPcfichCfiDetectionEnabled | Gets whether the value of SetPcfichCfi(String, Int32) method is auto-detected by the measurement or user-specified. |
|  | GetAutoPdschChannelDetectionEnabled | Gets whether the values of the SetPdschResourceBlockAllocation(String, String) method, the corresponding PDSCH CW0 Modulation Type method, and the PDSCH Power method are auto-detected by the measurement or user-specified. |
|  | GetAutoResourceBlockDetectionEnabled | Gets whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) properties are auto-detected by the measurement or if you specify the values of these properties. |
|  | GetBandwidth | Gets the channel bandwidth of the signal being measured. This value is expressed in Hz. |
|  | GetCellId | Gets a physical layer cell identity. |
|  | GetComponentCarrierAtCenterFrequency | Gets the index of the component carrier having its center at the user-configured center frequency. RFmxLTE uses this method along with ComponentCarrierSpacingType method to calculate the value of the SetFrequency(String, Double). |
|  | GetCyclicPrefixMode | Gets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
|  | GetDmrsOccEnabled | Gets whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases. |
|  | GetDownlinkAutoCellIDDetectionEnabled | Gets whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using GetDownlinkDetectedCellID(String, Int32) method. |
|  | GetDownlinkChannelConfigurationMode | Gets the channel configuration mode. |
|  | GetDownlinkNumberOfSubframes | Gets the number of unique subframes transmitted by the DUT. If you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel, this method will be set to 10 for FDD and 20 for TDD by default. |
|  | GetDownlinkTestModel | Gets the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. |
|  | GetDownlinkUserDefinedCellSpecificRatio | Gets the ratio Rhob/Rhoa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 specification. This method determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. |
|  | GetEmtcAnalysisEnabled | Gets whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. |
|  | GetFrequency | Gets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. This method is applicable only if you set the ComponentCarrierSpacingType method to User. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLaaDownlinkNumberOfEndingSymbols | Gets the number of ending symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the 3GPP 36.211 specification for more information regarding LAA downlink number of ending symbols. |
|  | GetLaaDownlinkStartingSymbol | Gets the starting symbol number in the first subframe of an LAA downlink burst. Refer to section 13A of the 3GPP 36.213 specification for more information regarding LAA downlink starting symbol. |
|  | GetLaaNumberOfSubframes | Gets the number of subframes in an LAA burst including the starting subframe. |
|  | GetLaaStartingSubframe | Gets the starting subframe of an LAA burst. |
|  | GetLaaUplinkEndingSymbol | Gets the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP 36.212 specification for more information regarding LAA uplink ending symbol. |
|  | GetLaaUplinkStartPosition | Gets the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the 3GPP 36.211 specification for more information regarding LAA uplink start position. |
|  | GetNBIoTUplinkSubcarrierSpacing | Gets the subcarrier bandwidth of an NB-IoT signal. This method specifies the spacing between adjacent subcarriers. |
|  | GetNCellId | Gets the narrowband physical layer cell identity. |
|  | GetNPuschDmrsBaseSequenceIndex | Gets the base sequence index of the Narrowband Physical Uplink Shared Channel (NPUSCH) DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |
|  | GetNPuschDmrsBaseSequenceMode | Gets whether the SetNPuschDmrsBaseSequenceIndex(String, Int32) method is computed by the measurement or specified by you. |
|  | GetNPuschDmrsCyclicShift | Gets the cyclic shift of the narrowband physical uplink shared channel (NPUSCH) DMRS as defined in Table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. |
|  | GetNPuschDmrsDeltaSequenceShift | Gets the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This method is valid when you set the SetNPuschDmrsGroupHoppingEnabled(String, RFmxLteMXNPuschDmrsGroupHoppingEnabled) method to True. |
|  | GetNPuschDmrsGroupHoppingEnabled | Gets whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the SetNPuschFormat(String, Int32) is 1. |
|  | GetNPuschFormat | Gets the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information. |
|  | GetNPuschModulationType | Gets the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). |
|  | GetNPuschNumberOfTones | Gets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | GetNPuschStartingSlot | Gets the starting slot number of the NPUSCH burst. |
|  | GetNPuschToneOffset | Gets the location of the starting subcarrier (tone) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | GetNumberOfComponentCarriers | Gets the number of component carriers configured within a subblock. |
|  | GetNumberOfPdschChannels | Gets the number of physical downlink shared channel (PDSCH) allocations in a subframe. |
|  | GetPbchPower | Gets the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPcfichCfi | Gets the control format indicator (CFI) carried by physical control format indicator channel (PCFICH). CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. |
|  | GetPcfichPower | Gets the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPdcchPower | Gets the power of physical downlink control channel (PDCCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPdschCW0ModulationType | Gets the modulation type of codeword0 PDSCH allocation. |
|  | GetPdschPower | Gets the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the SetDownlinkUserDefinedCellSpecificRatio(String, RFmxLteMXDownlinkUserDefinedRatio) method to calculate the Rb. Refer to section 3.3 of the 3GPP 36.521 specification for more information about Ra. |
|  | GetPdschResourceBlockAllocation | Gets the resource blocks of the physical downlink shared channel (PDSCH) allocation. |
|  | GetPhichDuration | Gets the physical hybrid-ARQ indicator channel (PHICH) duration. |
|  | GetPhichPower | Gets the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. |
|  | GetPhichResource | Gets the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This method is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. |
|  | GetPsschModulationType | Gets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. |
|  | GetPsschNumberOfResourceBlocks | Gets the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation. |
|  | GetPsschPower | Gets the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB. |
|  | GetPsschResourceBlockOffset | Gets the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. |
|  | GetPssPower | Gets the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPuschCyclicShiftField | Gets the cyclic shift field in uplink-related DCI format. When the SetDmrsOccEnabled(String, RFmxLteMXDmrsOccEnabled) method is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with SetTransmitAntennaToAnalyze(String, Int32). |
|  | GetPuschDeltaSequenceShift | Gets the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift. |
|  | GetPuschModulationType | Gets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | GetPuschNDmrs1 | Gets the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification. |
|  | GetPuschNDmrs2 | Gets the n_DMRS_2 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a slot. The valid values for this method are, as defined in table 5.5.2.1.1-1 of the 3GPP TS 36.211 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | GetPuschNumberOfResourceBlockClusters | Gets the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH).Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | GetPuschNumberOfResourceBlocks | Gets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. |
|  | GetPuschPower | Gets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | GetPuschResourceBlockOffset | Gets the starting resource block number of a physical uplink shared channel (PUSCH) cluster. |
|  | GetSpacingType | Gets the spacing between two adjacent component carriers within a subblock. |
|  | GetSrsbHop | Gets the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(String, Int32) method. |
|  | GetSrsBSrs | Gets the UE specific SRS bandwidth configuration BSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsCSrs | Gets the cell-specific SRS bandwidth configuration CSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsEnabled | Gets whether the LTE signal getting measured contains SRS transmission. |
|  | GetSrsISrs | Gets the SRS configuration index ISRS. It is used to determine the SRS periodicity and SRS subframe offset. It is a UE specific method which defines whether the SRS is transmitted in the subframe reserved for SRS by SRS subframe configuration. Refer to 3GPP 36.213 specification for more details. |
|  | GetSrskTC | Gets the transmission comb index. If you set this method to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this method to 1, SRS is transmitted on the odd subcarriers in the allocated region. |
|  | GetSrsMaximumUpPtsEnabled | Gets SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsnRrc | Gets the SRS frequency domain position nRRC. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsnSrsCS | Gets the cyclic shift value nSRSCS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsPower | Gets the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. |
|  | GetSrsSubframe1NRA | Gets the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD. |
|  | GetSrsSubframe6NRA | Gets the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. |
|  | GetSrsSubframeConfiguration | Gets the SRS subframe configuration specified in the Table 5.5.3.3-1 of 3GPP 36.211 specification. It is a cell-specific method. This method defines the subframes that are reserved for SRS transmission in a given cell. |
|  | GetSssPower | Gets the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUplinkGroupHoppingEnabled | Gets whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. |
|  | GetUplinkSequenceHoppingEnabled | Gets whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. This method is only applicable only when you set the SetPuschNumberOfResourceBlocks(String, Int32) method to a value greater than 5. |
|  | SetAutoControlChannelPowerDetectionEnabled | Sets whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported. |
|  | SetAutoNPuschChannelDetectionEnabled | Sets whether the values of the SetNPuschToneOffset(String, Int32), NPUSCH Number of Tones, and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) properties are auto-detected by the measurement or specified by you. |
|  | SetAutoPcfichCfiDetectionEnabled | Sets whether the value of SetPcfichCfi(String, Int32) method is auto-detected by the measurement or user-specified. |
|  | SetAutoPdschChannelDetectionEnabled | Sets whether the values of the SetPdschResourceBlockAllocation(String, String) method, the corresponding PDSCH CW0 Modulation Type method, and the PDSCH Power method are auto-detected by the measurement or user-specified. |
|  | SetAutoResourceBlockDetectionEnabled | Sets whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) properties are auto-detected by the measurement or if you specify the values of these properties. |
|  | SetBandwidth | Sets the channel bandwidth of the signal being measured. This value is expressed in Hz. |
|  | SetCellId | Sets a physical layer cell identity. |
|  | SetComponentCarrierAtCenterFrequency | Sets the index of the component carrier having its center at the user-configured center frequency. RFmxLTE uses this method along with ComponentCarrierSpacingType method to calculate the value of the SetFrequency(String, Double). |
|  | SetCyclicPrefixMode | Sets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
|  | SetDmrsOccEnabled | Sets whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases. |
|  | SetDownlinkAutoCellIDDetectionEnabled | Sets whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using GetDownlinkDetectedCellID(String, Int32) method. |
|  | SetDownlinkChannelConfigurationMode | Sets the channel configuration mode. |
|  | SetDownlinkNumberOfSubframes | Sets the number of unique subframes transmitted by the DUT. If you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel, this method will be set to 10 for FDD and 20 for TDD by default. |
|  | SetDownlinkTestModel | Sets the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. |
|  | SetDownlinkUserDefinedCellSpecificRatio | Sets the ratio Rhob/Rhoa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 specification. This method determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. |
|  | SetEmtcAnalysisEnabled | Sets whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. |
|  | SetFrequency | Sets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. This method is applicable only if you set the ComponentCarrierSpacingType method to User. |
|  | SetLaaDownlinkNumberOfEndingSymbols | Sets the number of ending symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the 3GPP 36.211 specification for more information regarding LAA downlink number of ending symbols. |
|  | SetLaaDownlinkStartingSymbol | Sets the starting symbol number in the first subframe of an LAA downlink burst. Refer to section 13A of the 3GPP 36.213 specification for more information regarding LAA downlink starting symbol. |
|  | SetLaaNumberOfSubframes | Sets the number of subframes in an LAA burst including the starting subframe. |
|  | SetLaaStartingSubframe | Sets the starting subframe of an LAA burst. |
|  | SetLaaUplinkEndingSymbol | Sets the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP 36.212 specification for more information regarding LAA uplink ending symbol. |
|  | SetLaaUplinkStartPosition | Sets the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the 3GPP 36.211 specification for more information regarding LAA uplink start position. |
|  | SetNBIoTUplinkSubcarrierSpacing | Sets the subcarrier bandwidth of an NB-IoT signal. This method specifies the spacing between adjacent subcarriers. |
|  | SetNCellId | Sets the narrowband physical layer cell identity. |
|  | SetNPuschDmrsBaseSequenceIndex | Sets the base sequence index of the Narrowband Physical Uplink Shared Channel (NPUSCH) DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |
|  | SetNPuschDmrsBaseSequenceMode | Sets whether the SetNPuschDmrsBaseSequenceIndex(String, Int32) method is computed by the measurement or specified by you. |
|  | SetNPuschDmrsCyclicShift | Sets the cyclic shift of the narrowband physical uplink shared channel (NPUSCH) DMRS as defined in Table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. |
|  | SetNPuschDmrsDeltaSequenceShift | Sets the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This method is valid when you set the SetNPuschDmrsGroupHoppingEnabled(String, RFmxLteMXNPuschDmrsGroupHoppingEnabled) method to True. |
|  | SetNPuschDmrsGroupHoppingEnabled | Sets whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the SetNPuschFormat(String, Int32) is 1. |
|  | SetNPuschFormat | Sets the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information. |
|  | SetNPuschModulationType | Sets the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). |
|  | SetNPuschNumberOfTones | Sets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | SetNPuschStartingSlot | Sets the starting slot number of the NPUSCH burst. |
|  | SetNPuschToneOffset | Sets the location of the starting subcarrier (tone) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | SetNumberOfComponentCarriers | Sets the number of component carriers configured within a subblock. |
|  | SetNumberOfPdschChannels | Sets the number of physical downlink shared channel (PDSCH) allocations in a subframe. |
|  | SetPbchPower | Sets the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPcfichCfi | Sets the control format indicator (CFI) carried by physical control format indicator channel (PCFICH). CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. |
|  | SetPcfichPower | Sets the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPdcchPower | Sets the power of physical downlink control channel (PDCCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPdschCW0ModulationType | Sets the modulation type of codeword0 PDSCH allocation. |
|  | SetPdschPower | Sets the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the SetDownlinkUserDefinedCellSpecificRatio(String, RFmxLteMXDownlinkUserDefinedRatio) method to calculate the Rb. Refer to section 3.3 of the 3GPP 36.521 specification for more information about Ra. |
|  | SetPdschResourceBlockAllocation | Sets the resource blocks of the physical downlink shared channel (PDSCH) allocation. |
|  | SetPhichDuration | Sets the physical hybrid-ARQ indicator channel (PHICH) duration. |
|  | SetPhichPower | Sets the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. |
|  | SetPhichResource | Sets the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This method is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. |
|  | SetPsschModulationType | Sets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. |
|  | SetPsschNumberOfResourceBlocks | Sets the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation. |
|  | SetPsschPower | Sets the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB. |
|  | SetPsschResourceBlockOffset | Sets the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. |
|  | SetPssPower | Sets the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPuschCyclicShiftField | Sets the cyclic shift field in uplink-related DCI format. When the SetDmrsOccEnabled(String, RFmxLteMXDmrsOccEnabled) method is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with SetTransmitAntennaToAnalyze(String, Int32). |
|  | SetPuschDeltaSequenceShift | Sets the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift. |
|  | SetPuschModulationType | Sets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | SetPuschNDmrs1 | Sets the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification. |
|  | SetPuschNDmrs2 | Sets the n_DMRS_2 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a slot. The valid values for this method are, as defined in table 5.5.2.1.1-1 of the 3GPP TS 36.211 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | SetPuschNumberOfResourceBlockClusters | Sets the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH).Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | SetPuschNumberOfResourceBlocks | Sets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. |
|  | SetPuschPower | Sets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | SetPuschResourceBlockOffset | Sets the starting resource block number of a physical uplink shared channel (PUSCH) cluster. |
|  | SetSpacingType | Sets the spacing between two adjacent component carriers within a subblock. |
|  | SetSrsbHop | Sets the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(String, Int32) method. |
|  | SetSrsBSrs | Sets the UE specific SRS bandwidth configuration BSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsCSrs | Sets the cell-specific SRS bandwidth configuration CSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsEnabled | Sets whether the LTE signal getting measured contains SRS transmission. |
|  | SetSrsISrs | Sets the SRS configuration index ISRS. It is used to determine the SRS periodicity and SRS subframe offset. It is a UE specific method which defines whether the SRS is transmitted in the subframe reserved for SRS by SRS subframe configuration. Refer to 3GPP 36.213 specification for more details. |
|  | SetSrskTC | Sets the transmission comb index. If you set this method to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this method to 1, SRS is transmitted on the odd subcarriers in the allocated region. |
|  | SetSrsMaximumUpPtsEnabled | Sets SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsnRrc | Sets the SRS frequency domain position nRRC. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsnSrsCS | Sets the cyclic shift value nSRSCS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsPower | Sets the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. |
|  | SetSrsSubframe1NRA | Sets the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD. |
|  | SetSrsSubframe6NRA | Sets the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. |
|  | SetSrsSubframeConfiguration | Sets the SRS subframe configuration specified in the Table 5.5.3.3-1 of 3GPP 36.211 specification. It is a cell-specific method. This method defines the subframes that are reserved for SRS transmission in a given cell. |
|  | SetSssPower | Sets the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetUplinkGroupHoppingEnabled | Sets whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. |
|  | SetUplinkSequenceHoppingEnabled | Sets whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. This method is only applicable only when you set the SetPuschNumberOfResourceBlocks(String, Int32) method to a value greater than 5. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b120f3fe-a8f1-bc2d-91fa-59eea0a97c0e.htm language=enus -->
## TOPIC 00268: rfmxltedotnet/html/b120f3fe-a8f1-bc2d-91fa-59eea0a97c0e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b120f3fe-a8f1-bc2d-91fa-59eea0a97c0e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b120f3fe-a8f1-bc2d-91fa-59eea0a97c0e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPuschCyclicShiftField Method

RFmxLteMXComponentCarrierGetPuschCyclicShiftField Method

SetDmrsOccEnabled(String, RFmxLteMXDmrsOccEnabled)

3GPP 36.211

SetTransmitAntennaToAnalyze(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschCyclicShiftField(
	string selectorString,
	out int value
)
```

```text
Public Function GetPuschCyclicShiftField ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the cyclic shift field in uplink-related DCI format. When the SetDmrsOccEnabled(String, RFmxLteMXDmrsOccEnabled) method is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with SetTransmitAntennaToAnalyze(String, Int32).

###### Return Value

Int32

##### Remarks

PuschCyclicShiftField

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b15837a3-60bd-c927-52e3-133266f01370.htm language=enus -->
## TOPIC 00269: rfmxltedotnet/html/b15837a3-60bd-c927-52e3-133266f01370.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b15837a3-60bd-c927-52e3-133266f01370.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b15837a3-60bd-c927-52e3-133266f01370.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetTriggerType Method

RFmxLteMXSetTriggerType Method

Sets the trigger type.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTriggerType(
	string selectorString,
	RFmxLteMXTriggerType value
)
```

```text
Public Function SetTriggerType ( 
	selectorString As String,
	value As RFmxLteMXTriggerType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTriggerTypeSpecifies the trigger type.

###### Return Value

Int32

##### Remarks

TriggerType

None

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b1617534-a19b-9dc9-c7f2-e4cf037b3ae5.htm language=enus -->
## TOPIC 00270: rfmxltedotnet/html/b1617534-a19b-9dc9-c7f2-e4cf037b3ae5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b1617534-a19b-9dc9-c7f2-e4cf037b3ae5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b1617534-a19b-9dc9-c7f2-e4cf037b3ae5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPhaseConfiguration.SetCommonClockSourceEnabled Method

RFmxLteMXSlotPhaseConfigurationSetCommonClockSourceEnabled Method

Sets whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCommonClockSourceEnabled(
	string selectorString,
	RFmxLteMXSlotPhaseCommonClockSourceEnabled value
)
```

```text
Public Function SetCommonClockSourceEnabled ( 
	selectorString As String,
	value As RFmxLteMXSlotPhaseCommonClockSourceEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSlotPhaseCommonClockSourceEnabledSpecifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

###### Return Value

Int32

##### Remarks

SlotPhaseCommonClockSourceEnabled

True

##### See Also

###### Reference

RFmxLteMXSlotPhaseConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b165a356-e562-5ed8-e432-667e9cda7153.htm language=enus -->
## TOPIC 00271: rfmxltedotnet/html/b165a356-e562-5ed8-e432-667e9cda7153.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b165a356-e562-5ed8-e432-667e9cda7153.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b165a356-e562-5ed8-e432-667e9cda7153.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwResults.GetAbsolutePower Method

RFmxLteMXObwResultsGetAbsolutePower Method

Gets the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ObwResultsAbsolutePower

##### See Also

###### Reference

RFmxLteMXObwResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b17874aa-af64-ef83-0d94-f38ee46f258d.htm language=enus -->
## TOPIC 00272: rfmxltedotnet/html/b17874aa-af64-ef83-0d94-f38ee46f258d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b17874aa-af64-ef83-0d94-f38ee46f258d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b17874aa-af64-ef83-0d94-f38ee46f258d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetMeanRmsPcfichEvm Method

RFmxLteMXModAccResultsGetMeanRmsPcfichEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanRmsPcfichEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanRmsPcfichEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the SetMeasurementLength(String, Int32) method.

###### Return Value

Int32

##### Remarks

ModAccResultsMeanRmsPcfichEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b18edba3-f230-e0a6-df42-fb125dfdc197.htm language=enus -->
## TOPIC 00273: rfmxltedotnet/html/b18edba3-f230-e0a6-df42-fb125dfdc197.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b18edba3-f230-e0a6-df42-fb125dfdc197.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b18edba3-f230-e0a6-df42-fb125dfdc197.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPsschMeanDmrsPower Method

RFmxLteMXModAccResultsGetPsschMeanDmrsPower Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPsschMeanDmrsPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetPsschMeanDmrsPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsPsschMeanDmrsPower

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b2f54a45-75e6-6eac-c743-909237f0ec7b.htm language=enus -->
## TOPIC 00274: rfmxltedotnet/html/b2f54a45-75e6-6eac-c743-909237f0ec7b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b2f54a45-75e6-6eac-c743-909237f0ec7b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b2f54a45-75e6-6eac-c743-909237f0ec7b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetAutoResourceBlockDetectionEnabled Method

RFmxLteMXComponentCarrierSetAutoResourceBlockDetectionEnabled Method

SetPuschModulationType(String, RFmxLteMXPuschModulationType)

SetPuschNumberOfResourceBlockClusters(String, Int32)

SetPuschResourceBlockOffset(String, Int32)

SetPuschNumberOfResourceBlocks(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoResourceBlockDetectionEnabled(
	string selectorString,
	RFmxLteMXAutoResourceBlockDetectionEnabled value
)
```

```text
Public Function SetAutoResourceBlockDetectionEnabled ( 
	selectorString As String,
	value As RFmxLteMXAutoResourceBlockDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoResourceBlockDetectionEnabled Specifies whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) properties are auto-detected by the measurement or if you specify the values of these properties.

###### Return Value

Int32

##### Remarks

AutoResourceBlockDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b385d5f6-0516-4145-9e9b-59f55fb15ba5.htm language=enus -->
## TOPIC 00275: rfmxltedotnet/html/b385d5f6-0516-4145-9e9b-59f55fb15ba5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b385d5f6-0516-4145-9e9b-59f55fb15ba5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b385d5f6-0516-4145-9e9b-59f55fb15ba5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetSrsbHop Method

RFmxLteMXComponentCarrierGetSrsbHop Method

SetSrsBSrs(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSrsbHop(
	string selectorString,
	out int value
)
```

```text
Public Function GetSrsbHop ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(String, Int32) method.

###### Return Value

Int32

##### Remarks

SrsbHop

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b58c8cef-5f4e-5918-6f6c-67b8b705bf5e.htm language=enus -->
## TOPIC 00276: rfmxltedotnet/html/b58c8cef-5f4e-5918-6f6c-67b8b705bf5e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b58c8cef-5f4e-5918-6f6c-67b8b705bf5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b58c8cef-5f4e-5918-6f6c-67b8b705bf5e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.ResetToDefault Method

RFmxLteMXListResetToDefault Method

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemStringPass an empty string. The list name that is passed when creating the list is used.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b5f6ac33-9f31-4867-af83-828e64951cec.htm language=enus -->
## TOPIC 00277: rfmxltedotnet/html/b5f6ac33-9f31-4867-af83-828e64951cec.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b5f6ac33-9f31-4867-af83-828e64951cec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b5f6ac33-9f31-4867-af83-828e64951cec.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration Methods

RFmxLteMXTxpConfiguration Methods

The [RFmxLteMXTxpConfiguration](d96b68a0-39eb-2fc6-dc51-4fabfbaf1722.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the TXP measurement. |
|  | ConfigureMeasurementOffsetAndInterval | Configures the measurement offset and measurement interval for the transmit power (TXP) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Enables the traces to be stored and retrieved after the TXP measurement is performed. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when Averaging Enabled is True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for TXP measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the Transmit Power (TXP) measurement. |
|  | GetMeasurementInterval | Gets the measurement interval. This value is expressed in seconds. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism inside TXP measurement. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Enables the traces to be stored and retrieved after the TXP measurement is performed. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when Averaging Enabled is True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for TXP measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the Transmit Power (TXP) measurement. |
|  | SetMeasurementInterval | Sets the measurement interval. This value is expressed in seconds. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism inside TXP measurement. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b868f2e0-c2b1-8b0b-3c6e-3f33a252ecb2.htm language=enus -->
## TOPIC 00278: rfmxltedotnet/html/b868f2e0-c2b1-8b0b-3c6e-3f33a252ecb2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b868f2e0-c2b1-8b0b-3c6e-3f33a252ecb2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b868f2e0-c2b1-8b0b-3c6e-3f33a252ecb2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpNoiseCompensationType Enumeration

RFmxLteMXAcpNoiseCompensationType Enumeration

Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAcpNoiseCompensationType
```

```text
Public Enumeration RFmxLteMXAcpNoiseCompensationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalyzerAndTermination | 0 | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
|  | AnalyzerOnly | 1 | Compensates for analyzer noise only. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b90fcabc-9a1c-f2ad-a4c5-19ad0d34bd27.htm language=enus -->
## TOPIC 00279: rfmxltedotnet/html/b90fcabc-9a1c-f2ad-a4c5-19ad0d34bd27.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b90fcabc-9a1c-f2ad-a4c5-19ad0d34bd27.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b90fcabc-9a1c-f2ad-a4c5-19ad0d34bd27.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetIQPowerEdgeTriggerLevelType Method

RFmxLteMXGetIQPowerEdgeTriggerLevelType Method

SetIQPowerEdgeTriggerLevel(String, Double)

SetTriggerType(String, RFmxLteMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIQPowerEdgeTriggerLevelType(
	string selectorString,
	out RFmxLteMXIQPowerEdgeTriggerLevelType value
)
```

```text
Public Function GetIQPowerEdgeTriggerLevelType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXIQPowerEdgeTriggerLevelType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXIQPowerEdgeTriggerLevelType Upon return, contains the reference for the SetIQPowerEdgeTriggerLevel(String, Double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerLevelType

Relative

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b9135f55-e7eb-4173-82ad-f5f95d1de73e.htm language=enus -->
## TOPIC 00280: rfmxltedotnet/html/b9135f55-e7eb-4173-82ad-f5f95d1de73e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b9135f55-e7eb-4173-82ad-f5f95d1de73e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b9135f55-e7eb-4173-82ad-f5f95d1de73e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetAveragingCount Method

RFmxLteMXSemConfigurationGetAveragingCount Method

SetAveragingEnabled(String, RFmxLteMXSemAveragingEnabled)

True

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemInt32 Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXSemAveragingEnabled) method to True.

###### Return Value

Int32

##### Remarks

SemAveragingCount

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/b9b43af0-6d0d-b5e8-df1f-0c9213921736.htm language=enus -->
## TOPIC 00281: rfmxltedotnet/html/b9b43af0-6d0d-b5e8-df1f-0c9213921736.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/b9b43af0-6d0d-b5e8-df1f-0c9213921736.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/b9b43af0-6d0d-b5e8-df1f-0c9213921736.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults Methods

RFmxLteMXModAccResults Methods

The [RFmxLteMXModAccResults](82230182-7536-5c9d-a759-ee039e09d904.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchCompositeEvm | Fetches the composite EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchCompositeEvmArray | Returns an array of the composite EVM for ModAcc measurements. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchCompositeMagnitudeAndPhaseError | Returns the mean RMS composite magnitude error, phase error, the maximum peak composite magnitude error, and the phase error. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchCompositeMagnitudeAndPhaseErrorArray | Returns the arrays of the mean RMS composite magnitude error and phase error, and the max peak composite magnitude error and phase error. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchCsrsConstellation | Fetches the constellation trace for a cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchCsrsEvm | Fetches the cell-specific reference signal EVM. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read results from this method. |
|  | FetchCsrsEvmArray | Fetches the array of CSRS EVMs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchDownlinkDetectedCellID | Fetches the detected cell ID. This method is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS). Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkDetectedCellIDArray | Fetches the array of detected cell IDs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchDownlinkPbchConstellation | Fetches the PBCH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkPcfichConstellation | Fetches the PCFICH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkPdcchConstellation | Fetches the PDCCH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkPhichConstellation | Fetches the PHICH constellation trace for the control channels. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkTransmitPower | Fetches the reference signal power and the OFDM symbol transmit power. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchDownlinkTransmitPowerArray | Fetches the array of reference signal powers and the OFDM symbol transmit powers for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchEvmHighPerSymbolTrace | Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmLowPerSymbolTrace | Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C-W/2. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmPerSlotTrace | Returns the EVM of each slot averaged across all the symbols within the slots and all the allocated subcarriers. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmPerSubcarrierTrace | Returns the EVM of each allocated subcarrier averaged across all the symbols within the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchEvmPerSymbolTrace | Returns the EVM on each symbol within the SetMeasurementLength(String, Int32) method averaged across all the allocated subcarriers. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method. |
|  | FetchInBandEmissionMargin | Returns the in-band emission margin on non allocated resource blocks (RBs) in the uplink signal. This value is expressed in dB. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchInBandEmissionMarginArray | Returns an array of margins on non allocated resource blocks (RBs) in the uplink signal for all component carriers within the subblock. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchInBandEmissionTrace | Returns the in-band emission (IBE) and limit traces. In-band emission is the interference falling into non allocated resource blocks. The IBE for various spectral regions (general, carrier leakage, and I/Q image) are evaluated according to section 6.5.2.3.5 of the 3GPP 36.521 specification and concatenated to form a composite trace. The limit trace is derived from the limits in the section 6.5.2.3.5 of the 3GPP 36.521 specification. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchIQImpairments | Returns the mean I/Q origin offset, mean I/Q gain imbalance, and mean I/Q quadrature error. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchIQImpairmentsArray | Returns an array of the mean I/Q origin offset, mean I/Q gain imbalance, and mean I/Q quadrature error. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchMaximumEvmPerSlotTrace | Returns the peak value of an EVM for each slot computed across all the symbols and all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumEvmPerSubcarrierTrace | Returns the peak value of an EVM for each allocated subcarrier computed across all the symbols within the value of the SetMeasurementLength(String, Int32). The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumEvmPerSymbolTrace | Returns the peak value of an EVM for each symbol computed across all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumFrequencyErrorPerSlotTrace | Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumMagnitudeErrorPerSymbolTrace | Returns the peak value of the magnitude error for each symbol computed across all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchMaximumPhaseErrorPerSymbolTrace | Returns the peak value of the phase error for each symbol computed across all the allocated subcarriers. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchNPuschConstellationTrace | Returns the recovered narrowband physical uplink shared channel (NPUSCH) constellation points. The constellation points of different slots in the measurement length are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchNPuschDataEvm | Fetches the narrowband physical uplink shared channel (NPUSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | FetchNPuschDmrsEvm | Fetches the EVM values calculated on NPUSCH DMRS over the length of the measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | FetchNPuschSymbolPower | Fetches the narrowband physical uplink shared channel (NPUSCH) symbol powers. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch1024QamConstellation | Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch1024QamEvm | Fetches the physical downlink shared channel (PDSCH) 1024QAM EVMs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch1024QamEvmArray | Fetches an array of physical downlink shared channel (PDSCH) 1024QAM EVMs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPdsch16QamConstellation | Fetches the physical downlink shared channel (PDSCH) 16 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch256QamConstellation | Fetches the physical downlink shared channel (PDSCH) 256 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdsch64QamConstellation | Fetches the physical downlink shared channel (PDSCH) 64 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdschEvm | Fetches the physical downlink shared channel (PDSCH) EVMs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPdschEvmArray | Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPdschQpskConstellation | Fetches the physical downlink shared channel (PDSCH) QPSK trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPsschConstellationTrace | Returns the recovered physical sidelink shared channel (PSSCH) constellation points. The constellation points of different slots in the measurement length are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPsschDataEvm | Fetches the physical sidelink shared channel (PSSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschDataEvmArray | Fetches the array of the physical sidelink shared channel (PSSCH) data EVM for ModAcc measurements. Use "subblock(n)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschDmrsEvm | Fetches the EVM values calculated on PSSCH DMRS over the length of the measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschDmrsEvmArray | Fetches the array of the EVM values calculated on PSSCH DMRS over the length of the measurement. Use "subblock(n)" as the selector string to read results from this method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the method returns the results as a percentage. When you set the ModAcc EVM Unit method to dB, the method returns the results in dB. |
|  | FetchPsschSymbolPower | Fetches the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPsschSymbolPowerArray | Fetches the array of the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPuschConstellationTrace | Returns the recovered physical uplink shared channel (PUSCH) constellation points. The constellation points of different slots in the SetMeasurementLength(String, Int32) are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDataEvm | Fetches the physical uplink shared channel (PUSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDataEvmArray | Returns an array of the Mean RMS PUSCH data EVM and the maximum peak PUSCH data EVM. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPuschDemodulatedBits | Fetches the recovered bits during EVM calculation. The bits of different slots in the SetMeasurementLength(String, Int32) method are concatenated. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDmrsEvm | Fetches the EVM values calculated on PUSCH DMRS calculated over the length of the measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschDmrsEvmArray | Returns an array of the PUSCH mean RMS DMRS EVM and the PUSCH maximum peak DMRS EVM of all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchPuschSymbolPower | Fetches the physical uplink shared channel (PUSCH) symbol power measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchPuschSymbolPowerArray | Returns an array of powers of the physical uplink shared channel (PUSCH) data symbols and DMRS of all the component carriers in the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchRmsMagnitudeErrorPerSymbolTrace | Returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchRmsPhaseErrorPerSymbolTrace | Returns the RMS mean value of the phase error for each symbol computed over all the allocated subcarriers and within the measurement length. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSpectralFlatness | Returns the spectral flatness measurements of the component carrier. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSpectralFlatnessArray | Returns the arrays of spectral flatness measurements of all component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSpectralFlatnessTrace | Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of the 3GPP TS 36.521 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSrsConstellation | Fetches the constellation trace for the SRS channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSrsEvm | Fetches the mean RMS EVM and the mean power for the SRS channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSrsEvmArray | Fetches the array of SRS EVMs for all the component carriers within the subblock. This value is expressed in percentage or dB. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSubblockInBandEmissionMargin | Returns the margin on non-allocated resource blocks (RBs) within the subblock aggregated bandwidth. This value is expressed in dB. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Refer to section 6.5.2A.3 of the 3GPP TS 36.521 specification for more information about in-band emission margin. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSubblockInBandEmissionTrace | Returns the in-band emission trace and the limit trace within the subblock aggregated bandwidth. The in-band emissions are a measure of the interference in the non-allocated resources blocks. The in-band emissions for various regions, such as general, carrier leakage, and I/Q image, are evaluated according to the method defined in the 3GPP 36.521 specification, and concatenated to form a composite trace. Limit trace is derived from the limits defined in section 6.5.2A.3 of the 3GPP TS 36.521 specification. The method result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSubblockIQImpairments | Returns the mean I/Q origin offset, the mean I/Q gain imbalance, and the mean I/Q quadrature error of a subblock. This method is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Otherwise, the method returns NaN, as measurements of this result are currently not supported. Use "subblock(n)" as the selector string to read results from this method. |
|  | FetchSynchronizationSignalConstellation | Fetches the constellations traces for PSS and SSS. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSynchronizationSignalEvm | Fetches the primary synchronization signal (PSS) EVM and secondary synchronization signal (SSS) EVM. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
|  | FetchSynchronizationSignalEvmArray | Fetches the array of primary synchronization signal (PSS) EVMs and secondary synchronization signal (SSS) EVMS for all the component carriers within a subblock. Use "subblock(n)" as the selector string to read results from this method. |
|  | GetDownlinkDetectedCellID | Gets the detected cell ID value. |
|  | GetDownlinkOfdmSymbolTransmitPower | Gets the mean value of power calculated in one OFDM symbol over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetDownlinkRSTransmitPower | Gets the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetInBandEmissionMargin | Gets the in-band emission margin. This value is expressed in dB. |
|  | GetMaximumPeakCompositeEvm | Gets the maximum value of the peak EVMs calculated on all the configured channels over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMaximumPeakCompositeMagnitudeError | Gets the peak value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels. |
|  | GetMaximumPeakCompositePhaseError | Gets the peak value of phase error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all thee configured channels. This value is expressed in degrees. |
|  | GetMaximumPeakFrequencyError | Gets the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in Hz. |
|  | GetMaximumPeakIQOriginOffset | Gets the estimated maximum IQ origin offset over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBc. |
|  | GetMeanFrequencyError | Gets the estimated carrier frequency offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetMeanIQGainImbalance | Gets the estimated I/Q gain imbalance averaged over the measurement length. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. NoteWhen you set the CC Bandwidth Method to 200.0 k and the NPUSCH Num Tones Method to 12, this result is available. For other values of NPUSCH Num Tones, this result will be reported as NaN. |
| Note |  |  |
| When you set the CC Bandwidth Method to 200.0 k and the NPUSCH Num Tones Method to 12, this result is available. For other values of NPUSCH Num Tones, this result will be reported as NaN. |  |  |
|  | GetMeanIQOriginOffset | Gets the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBc. |
|  | GetMeanIQTimingSkew | Returns the estimated IQ timing skew averaged over measured length. IQ timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds |
|  | GetMeanQuadratureError | Gets the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in degrees. |
|  | GetMeanRmsCompositeEvm | Gets the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsCompositeMagnitudeError | Gets the RMS mean value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels. |
|  | GetMeanRmsCompositePhaseError | Gets the RMS mean value of the composite phase error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels. This value is expressed in degrees. |
|  | GetMeanRmsCsrsEvm | Gets the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPbchEvm | Gets the mean value of RMS EVMs calculated on PBCH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPcfichEvm | Gets the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPdcchEvm | Gets the mean value of RMS EVMs calculated on PDCCH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPhichEvm | Gets the mean value of RMS EVMs calculated on PHICH channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsPssEvm | Gets the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsSrsEvm | Gets the mean value of RMS EVMs calculated on the SRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanRmsSssEvm | Gets the mean value of RMS EVMs calculated on secondary synchronization signal (SSS) channel over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetMeanSrsPower | Gets the mean value of power calculated on SRS over the slots specified by the SetMeasurementLength(String, Int32) method. This values is expressed in dBm. |
|  | GetMeanSymbolClockError | Gets the estimated symbol clock error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in ppm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetMeanTimeOffset | Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of ModAccSynchronizationMode method. This value is expressed in seconds. |
|  | GetNPuschMaximumPeakDataEvm | Gets the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetNPuschMaximumPeakDmrsEvm | Gets the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetNPuschMeanDataPower | Gets the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetNPuschMeanDmrsPower | Gets the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetNPuschMeanRmsDataEvm | Gets the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetNPuschMeanRmsDmrsEvm | Gets the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms1024QamEvm | Gets the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms16QamEvm | Gets the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms256QamEvm | Gets the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRms64QamEvm | Gets the mean value of RMS EVMs calculated on all 64 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRmsEvm | Gets the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPdschMeanRmsQpskEvm | Gets the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method. |
|  | GetPeakCompositeEvmSlotIndex | Gets the slot index where the ModAcc maximum peak composite EVM occurs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPeakCompositeEvmSubcarrierIndex | Gets the subcarrier index where the maximum peak composite EVM for ModAcc occurs. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPeakCompositeEvmSymbolIndex | Gets the symbol index of the GetMaximumPeakCompositeEvm(String, Double) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMaximumPeakDataEvm | Gets the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMaximumPeakDmrsEvm | Gets the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanDataPower | Gets the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanDmrsPower | Gets the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanRmsDataEvm | Gets the mean value of the RMS EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPsschMeanRmsDmrsEvm | Gets the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMaximumPeakDataEvm | Gets the maximum value of the peak EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMaximumPeakDmrsEvm | Gets the maximum value of the peak EVMs calculated on PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMeanDataPower | Gets the mean value of the power calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMeanDmrsPower | Gets the mean value of the power calculated on the PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. |
|  | GetPuschMeanRmsDataEvm | Gets the mean value of the RMS EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetPuschMeanRmsDmrsEvm | Gets the mean value of the RMS EVMs calculated on the PUSCH DMRS over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetSpectralFlatnessRange1MaximumToRange1Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. This value is expressed in dB. |
|  | GetSpectralFlatnessRange1MaximumToRange2Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |
|  | GetSpectralFlatnessRange2MaximumToRange1Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients from frequency Measurement Offset parameter to frequency Range1. This value is expressed in dB. |
|  | GetSpectralFlatnessRange2MaximumToRange2Minimum | Gets the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Measurement Offset parameter. This value is expressed in dB. |
|  | GetSubblockInBandEmissionMargin | Gets the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB. |
|  | GetSubblockMeanIQGainImbalance | Gets the estimated I/Q gain imbalance averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock. This result is valid only when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(String, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. Otherwise, this parameter returns NaN, as measurement of this result is currently not supported. |
|  | GetSubblockMeanIQOriginOffset | Gets the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(String, Int32) method in the subblock. This value is expressed in dBc. |
|  | GetSubblockMeanQuadratureError | Gets the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/bacbce91-4274-61ce-da57-e96a69177a29.htm language=enus -->
## TOPIC 00282: rfmxltedotnet/html/bacbce91-4274-61ce-da57-e96a69177a29.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/bacbce91-4274-61ce-da57-e96a69177a29.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/bacbce91-4274-61ce-da57-e96a69177a29.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList Methods

RFmxLteMXList Methods

The [RFmxLteMXList](1bca98d4-455d-65fb-0491-80b8af5e5e67.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AbortMeasurements | Stops acquisition and measurements associated with list instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(String, String) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
|  | CheckMeasurementStatus | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
|  | ClearAllNamedResults | Clears all results for the current list instance. |
|  | ClearNamedResult | Clears a result instance specified by the result name in the selectorString parameter. |
|  | Commit | Commits settings to the hardware. Calling this method is optional. RFmxLTE commits settings to the hardware when you call the Initiate(String, String) method. |
|  | CreateListStep | Creates a new list step instance in a list. |
|  | DeleteList | Deletes an instance of a list. |
|  | Dispose | Deletes the list and clears any trace of the current list, if any. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetListStep | Returns a list step instance in a list. |
|  | GetListStepAll | Returns all list step instances in a list. |
|  | GetListStepRange | Returns a range of list step instances in a list. |
|  | GetNumberOfSteps | Returns number of list step instances in a list. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Initiate | Initiates all enabled measurements. Call this method after configuring the list and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the WaitForMeasurementComplete(String, Double) method or CheckMeasurementStatus(String, Boolean) method. |
|  | ResetToDefault | Resets a list to the default values. |
|  | SetNumberOfSteps | Sets number of list step instances in a list. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

Top

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/bb39f6ca-5127-b2bf-216f-d4dd67350aed.htm language=enus -->
## TOPIC 00283: rfmxltedotnet/html/bb39f6ca-5127-b2bf-216f-d4dd67350aed.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/bb39f6ca-5127-b2bf-216f-d4dd67350aed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/bb39f6ca-5127-b2bf-216f-d4dd67350aed.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.GetRbwFilterType Method

RFmxLteMXObwConfigurationGetRbwFilterType Method

Gets the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRbwFilterType(
	string selectorString,
	out RFmxLteMXObwRbwFilterType value
)
```

```text
Public Function GetRbwFilterType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXObwRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXObwRbwFilterTypeUpon return, contains the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

ObwRbwFilterType

Gaussian

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/bcb62a99-fedc-b875-ce75-ae74e873ea70.htm language=enus -->
## TOPIC 00284: rfmxltedotnet/html/bcb62a99-fedc-b875-ce75-ae74e873ea70.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/bcb62a99-fedc-b875-ce75-ae74e873ea70.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/bcb62a99-fedc-b875-ce75-ae74e873ea70.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchMaximumEvmPerSubcarrierTrace Method

RFmxLteMXModAccResultsFetchMaximumEvmPerSubcarrierTrace Method

SetMeasurementLength(String, Int32)

SetLinkDirection(String, RFmxLteMXLinkDirection)

Uplink

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchMaximumEvmPerSubcarrierTrace(
	string selectorString,
	double timeout,
	ref AnalogWaveform<float> maximumEvmPerSubcarrier
)
```

```text
Public Function FetchMaximumEvmPerSubcarrierTrace ( 
	selectorString As String,
	timeout As Double,
	ByRef maximumEvmPerSubcarrier As AnalogWaveform(Of Single)
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **maximumEvmPerSubcarrier**
  - Type: NationalInstrumentsAnalogWaveformSingle Upon return, contains the peak value of an EVM for each allocated subcarrier computed across all the symbols within the value of the ModAcc Meas Length method. This value is expressed as a percentage or in dB

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/bd399784-acc4-98af-3cb7-f5b47c630192.htm language=enus -->
## TOPIC 00285: rfmxltedotnet/html/bd399784-acc4-98af-3cb7-f5b47c630192.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/bd399784-acc4-98af-3cb7-f5b47c630192.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/bd399784-acc4-98af-3cb7-f5b47c630192.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.ClearAllNamedResults Method

RFmxLteMXClearAllNamedResults Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ClearAllNamedResults(
	string selectorString
)
```

```text
Public Function ClearAllNamedResults ( 
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

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/bdc5a225-c361-f8ea-877a-cbd5f0053a7d.htm language=enus -->
## TOPIC 00286: rfmxltedotnet/html/bdc5a225-c361-f8ea-877a-cbd5f0053a7d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/bdc5a225-c361-f8ea-877a-cbd5f0053a7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/bdc5a225-c361-f8ea-877a-cbd5f0053a7d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetNPuschDmrsGroupHoppingEnabled Method

RFmxLteMXComponentCarrierSetNPuschDmrsGroupHoppingEnabled Method

SetNPuschFormat(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNPuschDmrsGroupHoppingEnabled(
	string selectorString,
	RFmxLteMXNPuschDmrsGroupHoppingEnabled value
)
```

```text
Public Function SetNPuschDmrsGroupHoppingEnabled ( 
	selectorString As String,
	value As RFmxLteMXNPuschDmrsGroupHoppingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXNPuschDmrsGroupHoppingEnabled Specifies whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the SetNPuschFormat(String, Int32) is 1.

###### Return Value

Int32

##### Remarks

NPuschDmrsGroupHoppingEnabled

False

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c1d1171a-06f4-8e33-a949-1d3734602ddf.htm language=enus -->
## TOPIC 00287: rfmxltedotnet/html/c1d1171a-06f4-8e33-a949-1d3734602ddf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c1d1171a-06f4-8e33-a949-1d3734602ddf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c1d1171a-06f4-8e33-a949-1d3734602ddf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.GetNumberOfSteps Method

RFmxLteMXListGetNumberOfSteps Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfSteps(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfSteps ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Pass an empty string. The list name that is passed when creating the list is used.
- **value**
  - Type: SystemInt32Upon return, contains the number of list step instances in a list.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c2f9c2e3-3c63-46d6-4e01-d3a2d963ee99.htm language=enus -->
## TOPIC 00288: rfmxltedotnet/html/c2f9c2e3-3c63-46d6-4e01-d3a2d963ee99.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c2f9c2e3-3c63-46d6-4e01-d3a2d963ee99.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c2f9c2e3-3c63-46d6-4e01-d3a2d963ee99.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.CreateListStep Method

RFmxLteMXListCreateListStep Method

Creates a new list step instance in a list.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMX CreateListStep()
```

```text
Public Function CreateListStep As RFmxLteMX
```

###### Return Value

RFmxLteMX

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c45e407a-90a4-7e52-3142-50b4317a6285.htm language=enus -->
## TOPIC 00289: rfmxltedotnet/html/c45e407a-90a4-7e52-3142-50b4317a6285.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c45e407a-90a4-7e52-3142-50b4317a6285.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c45e407a-90a4-7e52-3142-50b4317a6285.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetRbwFilterType Method

RFmxLteMXChpConfigurationSetRbwFilterType Method

Sets the shape of the digital RBW filter.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterType(
	string selectorString,
	RFmxLteMXChpRbwFilterType value
)
```

```text
Public Function SetRbwFilterType ( 
	selectorString As String,
	value As RFmxLteMXChpRbwFilterType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpRbwFilterTypeSpecifies the shape of the digital RBW filter.

###### Return Value

Int32

##### Remarks

ChpRbwFilterType

FftBased

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c474e4ea-579d-ba7e-a561-9e598a800885.htm language=enus -->
## TOPIC 00290: rfmxltedotnet/html/c474e4ea-579d-ba7e-a561-9e598a800885.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c474e4ea-579d-ba7e-a561-9e598a800885.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c474e4ea-579d-ba7e-a561-9e598a800885.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXConstants.PxiTriggerLine7 Field

RFmxLteMXConstantsPxiTriggerLine7 Field

The signal is exported to the PXI trigger line 7.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXConstants Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c4d91fbc-57fd-bcd9-118e-8e71a8a4d151.htm language=enus -->
## TOPIC 00291: rfmxltedotnet/html/c4d91fbc-57fd-bcd9-118e-8e71a8a4d151.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c4d91fbc-57fd-bcd9-118e-8e71a8a4d151.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c4d91fbc-57fd-bcd9-118e-8e71a8a4d151.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPowerConfiguration.GetAllTracesEnabled Method

RFmxLteMXSlotPowerConfigurationGetAllTracesEnabled Method

Gets whether to enable the traces to be stored and retrieved after performing the SlotPower measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanUpon return, contains whether to enable the traces to be stored and retrieved after performing the SlotPower measurement.

###### Return Value

Int32

##### Remarks

SlotPowerAllTracesEnabled

##### See Also

###### Reference

RFmxLteMXSlotPowerConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c4eeb5f7-2f55-a69b-5c07-0fabd65e70e0.htm language=enus -->
## TOPIC 00292: rfmxltedotnet/html/c4eeb5f7-2f55-a69b-5c07-0fabd65e70e0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c4eeb5f7-2f55-a69b-5c07-0fabd65e70e0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c4eeb5f7-2f55-a69b-5c07-0fabd65e70e0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetNCellId Method

RFmxLteMXComponentCarrierSetNCellId Method

Sets the narrowband physical layer cell identity.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNCellId(
	string selectorString,
	int value
)
```

```text
Public Function SetNCellId ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies the narrowband physical layer cell identity.

###### Return Value

Int32

##### Remarks

NCellId

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c543c6ba-d58a-51fb-a408-d2ce4b9260b7.htm language=enus -->
## TOPIC 00293: rfmxltedotnet/html/c543c6ba-d58a-51fb-a408-d2ce4b9260b7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c543c6ba-d58a-51fb-a408-d2ce4b9260b7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c543c6ba-d58a-51fb-a408-d2ce4b9260b7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetDuplexScheme Method

RFmxLteMXGetDuplexScheme Method

Gets the duplexing technique of the signal being measured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDuplexScheme(
	string selectorString,
	out RFmxLteMXDuplexScheme value
)
```

```text
Public Function GetDuplexScheme ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXDuplexScheme
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXDuplexSchemeUpon return, contains the duplexing technique of the signal being measured.

###### Return Value

Int32

##### Remarks

DuplexScheme

Fdd

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c576beec-a936-01bf-73b2-9207c237f3a0.htm language=enus -->
## TOPIC 00294: rfmxltedotnet/html/c576beec-a936-01bf-73b2-9207c237f3a0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c576beec-a936-01bf-73b2-9207c237f3a0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c576beec-a936-01bf-73b2-9207c237f3a0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAutoResourceBlockDetectionEnabled Enumeration

RFmxLteMXAutoResourceBlockDetectionEnabled Enumeration

SetPuschModulationType(String, RFmxLteMXPuschModulationType)

SetPuschNumberOfResourceBlockClusters(String, Int32)

SetPuschResourceBlockOffset(String, Int32)

SetPuschNumberOfResourceBlocks(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAutoResourceBlockDetectionEnabled
```

```text
Public Enumeration RFmxLteMXAutoResourceBlockDetectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The values of the PUSCH Mod Type, PUSCH Num Clusters, PUSCH RB Offset, and PUSCH Num RBs properties that you specify are used for the measurement. |
|  | True | 1 | The values of the PUSCH Mod Type, PUSCH Num Clusters, PUSCH RB Offset, and PUSCH Num RBs properties are detected automatically and used for the measurement. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c718ad86-d75c-2013-921f-fcd76b65a951.htm language=enus -->
## TOPIC 00295: rfmxltedotnet/html/c718ad86-d75c-2013-921f-fcd76b65a951.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c718ad86-d75c-2013-921f-fcd76b65a951.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c718ad86-d75c-2013-921f-fcd76b65a951.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetMeasurementEnabled Method

RFmxLteMXAcpConfigurationSetMeasurementEnabled Method

Sets whether to enable the ACP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanSpecifies whether to enable the ACP measurement.

###### Return Value

Int32

##### Remarks

AcpMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c79859c6-2922-84b5-c6fb-f0516aff92b2.htm language=enus -->
## TOPIC 00296: rfmxltedotnet/html/c79859c6-2922-84b5-c6fb-f0516aff92b2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c79859c6-2922-84b5-c6fb-f0516aff92b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c79859c6-2922-84b5-c6fb-f0516aff92b2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetListStepTimerDuration Method

RFmxLteMXSetListStepTimerDuration Method

SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetListStepTimerDuration(
	string selectorString,
	double value
)
```

```text
Public Function SetListStepTimerDuration ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the duration of a given list step in units specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit).

###### Return Value

Int32

##### Remarks

ListStepTimerDuration

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c894a1a5-ca12-ed97-bacf-631b14c1b6e7.htm language=enus -->
## TOPIC 00297: rfmxltedotnet/html/c894a1a5-ca12-ed97-bacf-631b14c1b6e7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c894a1a5-ca12-ed97-bacf-631b14c1b6e7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c894a1a5-ca12-ed97-bacf-631b14c1b6e7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpResults.FetchSubblockMeasurement Method

RFmxLteMXChpResultsFetchSubblockMeasurement Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSubblockMeasurement(
	string selectorString,
	double timeout,
	out double subblockPower,
	out double integrationBandwidth,
	out double frequency
)
```

```text
Public Function FetchSubblockMeasurement ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef subblockPower As Double,
	<OutAttribute> ByRef integrationBandwidth As Double,
	<OutAttribute> ByRef frequency As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **subblockPower**
  - Type: SystemDouble Upon return, contains the sum of powers of all the frequency bins over the integration bandwidth of the subblock.
- **integrationBandwidth**
  - Type: SystemDouble Upon return, contains the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock.
- **frequency**
  - Type: SystemDouble Upon return, contains the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXChpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c8d5addf-b250-69d1-3f96-98dd3642adfc.htm language=enus -->
## TOPIC 00298: rfmxltedotnet/html/c8d5addf-b250-69d1-3f96-98dd3642adfc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c8d5addf-b250-69d1-3f96-98dd3642adfc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c8d5addf-b250-69d1-3f96-98dd3642adfc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetDownlinkAutoCellIDDetectionEnabled Method

RFmxLteMXComponentCarrierGetDownlinkAutoCellIDDetectionEnabled Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetDownlinkAutoCellIDDetectionEnabled(
	string selectorString,
	out RFmxLteMXDownlinkAutoCellIDDetectionEnabled value
)
```

```text
Public Function GetDownlinkAutoCellIDDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXDownlinkAutoCellIDDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXDownlinkAutoCellIDDetectionEnabled Upon return, contains whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using GetDownlinkDetectedCellID(String, Int32) method.

###### Return Value

Int32

##### Remarks

DownlinkAutoCellIDDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c98001fb-202f-757a-7c4e-6066742f87e2.htm language=enus -->
## TOPIC 00299: rfmxltedotnet/html/c98001fb-202f-757a-7c4e-6066742f87e2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c98001fb-202f-757a-7c4e-6066742f87e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c98001fb-202f-757a-7c4e-6066742f87e2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPsschModulationType Method

RFmxLteMXComponentCarrierSetPsschModulationType Method

Sets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPsschModulationType(
	string selectorString,
	RFmxLteMXPsschModulationType value
)
```

```text
Public Function SetPsschModulationType ( 
	selectorString As String,
	value As RFmxLteMXPsschModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPsschModulationTypeSpecifies the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured.

###### Return Value

Int32

##### Remarks

PsschModulationType

Qpsk

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/c9fea603-a861-93dc-59e8-99d86feae869.htm language=enus -->
## TOPIC 00300: rfmxltedotnet/html/c9fea603-a861-93dc-59e8-99d86feae869.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/c9fea603-a861-93dc-59e8-99d86feae869.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/c9fea603-a861-93dc-59e8-99d86feae869.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.GetAveragingEnabled Method

RFmxLteMXTxpConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for TXP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxLteMXTxpAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXTxpAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTxpAveragingEnabledUpon return, contains whether to enable averaging for TXP measurement.

###### Return Value

Int32

##### Remarks

TxpAveragingEnabled

False

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ccac0dcf-af4f-a5e5-7dcf-26df0d6320c6.htm language=enus -->
## TOPIC 00301: rfmxltedotnet/html/ccac0dcf-af4f-a5e5-7dcf-26df0d6320c6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ccac0dcf-af4f-a5e5-7dcf-26df0d6320c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ccac0dcf-af4f-a5e5-7dcf-26df0d6320c6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetListStepTimerUnit Method

RFmxLteMXSetListStepTimerUnit Method

SetListStepTimerDuration(String, Double)

SetListStepTimerOffset(String, Double)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetListStepTimerUnit(
	string selectorString,
	RFmxLteMXListStepTimerUnit value
)
```

```text
Public Function SetListStepTimerUnit ( 
	selectorString As String,
	value As RFmxLteMXListStepTimerUnit
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXListStepTimerUnit Specifies the units in which SetListStepTimerDuration(String, Double) and SetListStepTimerOffset(String, Double) are specified.

###### Return Value

Int32

##### Remarks

ListStepTimerUnit

Slot

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/cd8a5ad5-a7a1-050d-e5dd-95228f318d0f.htm language=enus -->
## TOPIC 00302: rfmxltedotnet/html/cd8a5ad5-a7a1-050d-e5dd-95228f318d0f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/cd8a5ad5-a7a1-050d-e5dd-95228f318d0f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/cd8a5ad5-a7a1-050d-e5dd-95228f318d0f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.Txp Property

RFmxLteMXTxp Property

RFmxLteMXTxp

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXTxp Txp { get; }
```

```text
Public ReadOnly Property Txp As RFmxLteMXTxp
	Get
```

###### Property Value

RFmxLteMXTxp

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ce6303d9-5902-4df1-d2f0-5471ade94fdd.htm language=enus -->
## TOPIC 00303: rfmxltedotnet/html/ce6303d9-5902-4df1-d2f0-5471ade94fdd.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ce6303d9-5902-4df1-d2f0-5471ade94fdd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ce6303d9-5902-4df1-d2f0-5471ade94fdd.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.GetListStep Method

RFmxLteMXListGetListStep Method

Returns a list step instance in a list.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMX GetListStep(
	int stepIndex
)
```

```text
Public Function GetListStep ( 
	stepIndex As Integer
) As RFmxLteMX
```

###### Parameters

- **stepIndex**
  - Type: SystemInt32 Pass the list step number.

###### Return Value

RFmxLteMX

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/cebef773-a9c8-9c87-2227-e182fb52237f.htm language=enus -->
## TOPIC 00304: rfmxltedotnet/html/cebef773-a9c8-9c87-2227-e182fb52237f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/cebef773-a9c8-9c87-2227-e182fb52237f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/cebef773-a9c8-9c87-2227-e182fb52237f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration.ConfigureAveraging Method

RFmxLteMXTxpConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxLteMXTxpAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxLteMXTxpAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXTxpAveragingEnabledSpecifies whether to enable averaging for the measurement.
- **averagingCount**
  - Type: SystemInt32Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXTxpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/cec1054e-111e-1192-05d1-53fd0b60c740.htm language=enus -->
## TOPIC 00305: rfmxltedotnet/html/cec1054e-111e-1192-05d1-53fd0b60c740.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/cec1054e-111e-1192-05d1-53fd0b60c740.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/cec1054e-111e-1192-05d1-53fd0b60c740.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchDownlinkTransmitPowerArray Method

RFmxLteMXModAccResultsFetchDownlinkTransmitPowerArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDownlinkTransmitPowerArray(
	string selectorString,
	double timeout,
	ref double[] RSTransmitPower,
	ref double[] ofdmSymbolTransmitPower,
	ref double[] reserved1,
	ref double[] reserved2
)
```

```text
Public Function FetchDownlinkTransmitPowerArray ( 
	selectorString As String,
	timeout As Double,
	ByRef RSTransmitPower As Double(),
	ByRef ofdmSymbolTransmitPower As Double(),
	ByRef reserved1 As Double(),
	ByRef reserved2 As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **RSTransmitPower**
  - Type: SystemDouble Upon return, contains the array of mean values of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm.
- **ofdmSymbolTransmitPower**
  - Type: SystemDouble Upon return, contains the array the mean value of power calculated in one OFDM symbol over the slots specified by the ModAcc Meas Length method. This value is expressed in dBm.
- **reserved1**
  - Type: SystemDouble This result is not supported in this release and it is reserved for future enhancements.
- **reserved2**
  - Type: SystemDouble This result is not supported in this release and it is reserved for future enhancements.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/cfdece03-15de-e49d-7791-55159ab27c5b.htm language=enus -->
## TOPIC 00306: rfmxltedotnet/html/cfdece03-15de-e49d-7791-55159ab27c5b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/cfdece03-15de-e49d-7791-55159ab27c5b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/cfdece03-15de-e49d-7791-55159ab27c5b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetOffsetAbsoluteLimitStop Method

RFmxLteMXSemConfigurationGetOffsetAbsoluteLimitStop Method

Gets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetAbsoluteLimitStop(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetAbsoluteLimitStop ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

SemOffsetAbsoluteLimitStop

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d02d5ed4-c0a9-d285-ef13-2c71bfbc7014.htm language=enus -->
## TOPIC 00307: rfmxltedotnet/html/d02d5ed4-c0a9-d285-ef13-2c71bfbc7014.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d02d5ed4-c0a9-d285-ef13-2c71bfbc7014.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d02d5ed4-c0a9-d285-ef13-2c71bfbc7014.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccInBandEmissionMaskType Enumeration

RFmxLteMXModAccInBandEmissionMaskType Enumeration

Specifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccInBandEmissionMaskType
```

```text
Public Enumeration RFmxLteMXModAccInBandEmissionMaskType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Release8_10 | 0 | Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. |
|  | Release11Onwards | 1 | Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d0c84083-0c69-e4e8-d930-9849aaba6a57.htm language=enus -->
## TOPIC 00308: rfmxltedotnet/html/d0c84083-0c69-e4e8-d930-9849aaba6a57.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d0c84083-0c69-e4e8-d930-9849aaba6a57.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d0c84083-0c69-e4e8-d930-9849aaba6a57.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetAutoPdschChannelDetectionEnabled Method

RFmxLteMXComponentCarrierSetAutoPdschChannelDetectionEnabled Method

SetPdschResourceBlockAllocation(String, String)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoPdschChannelDetectionEnabled(
	string selectorString,
	RFmxLteMXAutoPdschChannelDetectionEnabled value
)
```

```text
Public Function SetAutoPdschChannelDetectionEnabled ( 
	selectorString As String,
	value As RFmxLteMXAutoPdschChannelDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoPdschChannelDetectionEnabled Specifies whether the values of the SetPdschResourceBlockAllocation(String, String) method, the corresponding PDSCH CW0 Modulation Type method, and the PDSCH Power method are auto-detected by the measurement or user-specified.

###### Return Value

Int32

##### Remarks

AutoPdschChannelDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d2ef62ee-db86-df9a-1eb2-099aec17b332.htm language=enus -->
## TOPIC 00309: rfmxltedotnet/html/d2ef62ee-db86-df9a-1eb2-099aec17b332.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d2ef62ee-db86-df9a-1eb2-099aec17b332.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d2ef62ee-db86-df9a-1eb2-099aec17b332.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.ListName Property

RFmxLteMXListListName Property

Gets the list name.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public string ListName { get; }
```

```text
Public ReadOnly Property ListName As String
	Get
```

###### Property Value

String

###### Implements

IList.ListName

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d2f639b2-faf1-61ec-b2be-931809f809f5.htm language=enus -->
## TOPIC 00310: rfmxltedotnet/html/d2f639b2-faf1-61ec-b2be-931809f809f5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d2f639b2-faf1-61ec-b2be-931809f809f5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d2f639b2-faf1-61ec-b2be-931809f809f5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetNoiseCalibrationAveragingAuto Method

RFmxLteMXAcpConfigurationSetNoiseCalibrationAveragingAuto Method

Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetNoiseCalibrationAveragingAuto(
	string selectorString,
	RFmxLteMXAcpNoiseCalibrationAveragingAuto value
)
```

```text
Public Function SetNoiseCalibrationAveragingAuto ( 
	selectorString As String,
	value As RFmxLteMXAcpNoiseCalibrationAveragingAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpNoiseCalibrationAveragingAutoSpecifies whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

###### Return Value

Int32

##### Remarks

AcpNoiseCalibrationAveragingAuto

True

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d2f8e7d5-0d94-855a-1cc3-1049c0f9d0c8.htm language=enus -->
## TOPIC 00311: rfmxltedotnet/html/d2f8e7d5-0d94-855a-1cc3-1049c0f9d0c8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d2f8e7d5-0d94-855a-1cc3-1049c0f9d0c8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d2f8e7d5-0d94-855a-1cc3-1049c0f9d0c8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetIQQuadratureErrorCorrectionEnabled Method

RFmxLteMXModAccConfigurationSetIQQuadratureErrorCorrectionEnabled Method

Sets whether to enable IQ quadrature error correction.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIQQuadratureErrorCorrectionEnabled(
	string selectorString,
	RFmxLteMXModAccIQQuadratureErrorCorrectionEnabled value
)
```

```text
Public Function SetIQQuadratureErrorCorrectionEnabled ( 
	selectorString As String,
	value As RFmxLteMXModAccIQQuadratureErrorCorrectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccIQQuadratureErrorCorrectionEnabledSpecifies whether to enable IQ quadrature error correction.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d369122b-7fc0-adfe-4e52-98195194e379.htm language=enus -->
## TOPIC 00312: rfmxltedotnet/html/d369122b-7fc0-adfe-4e52-98195194e379.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d369122b-7fc0-adfe-4e52-98195194e379.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d369122b-7fc0-adfe-4e52-98195194e379.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetListStepTimerDuration Method

RFmxLteMXGetListStepTimerDuration Method

SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetListStepTimerDuration(
	string selectorString,
	out double value
)
```

```text
Public Function GetListStepTimerDuration ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the duration of a given list step in units specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit).

###### Return Value

Int32

##### Remarks

ListStepTimerDuration

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d64e4756-4687-c91b-4c9c-70703c5536fc.htm language=enus -->
## TOPIC 00313: rfmxltedotnet/html/d64e4756-4687-c91b-4c9c-70703c5536fc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d64e4756-4687-c91b-4c9c-70703c5536fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d64e4756-4687-c91b-4c9c-70703c5536fc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.IsDisposed Property

RFmxLteMXListIsDisposed Property

Gets a value that indicates whether the list has been disposed.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d66c3ad6-47ca-a2eb-2063-bd353fa50ee4.htm language=enus -->
## TOPIC 00314: rfmxltedotnet/html/d66c3ad6-47ca-a2eb-2063-bd353fa50ee4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d66c3ad6-47ca-a2eb-2063-bd353fa50ee4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d66c3ad6-47ca-a2eb-2063-bd353fa50ee4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.SetOffsetRelativeLimitStop Method

RFmxLteMXSemConfigurationSetOffsetRelativeLimitStop Method

Sets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOffsetRelativeLimitStop(
	string selectorString,
	double value
)
```

```text
Public Function SetOffsetRelativeLimitStop ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

SemOffsetRelativeLimitStop

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d66e76ce-5d3d-07e6-281e-51ebbdb82a4c.htm language=enus -->
## TOPIC 00315: rfmxltedotnet/html/d66e76ce-5d3d-07e6-281e-51ebbdb82a4c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d66e76ce-5d3d-07e6-281e-51ebbdb82a4c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d66e76ce-5d3d-07e6-281e-51ebbdb82a4c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetSrsbHop Method

RFmxLteMXComponentCarrierSetSrsbHop Method

SetSrsBSrs(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSrsbHop(
	string selectorString,
	int value
)
```

```text
Public Function SetSrsbHop ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(String, Int32) method.

###### Return Value

Int32

##### Remarks

SrsbHop

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d69e55f8-fefa-89b2-fa48-710b243a23d8.htm language=enus -->
## TOPIC 00316: rfmxltedotnet/html/d69e55f8-fefa-89b2-fa48-710b243a23d8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d69e55f8-fefa-89b2-fa48-710b243a23d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d69e55f8-fefa-89b2-fa48-710b243a23d8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxp.Configuration Property

RFmxLteMXTxpConfiguration Property

RFmxLteMXTxpConfiguration

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXTxpConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxLteMXTxpConfiguration
	Get
```

###### Property Value

RFmxLteMXTxpConfiguration

##### See Also

###### Reference

RFmxLteMXTxp Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d6a0fb9d-e6dc-14a7-dce2-20fd0b1c58a1.htm language=enus -->
## TOPIC 00317: rfmxltedotnet/html/d6a0fb9d-e6dc-14a7-dce2-20fd0b1c58a1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d6a0fb9d-e6dc-14a7-dce2-20fd0b1c58a1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d6a0fb9d-e6dc-14a7-dce2-20fd0b1c58a1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChp Class

RFmxLteMXChp Class

Represents the CHP measurement.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXChp : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXChp
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXChp type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXChpConfiguration instance that provides methods to configure the CHP measurement. |
|  | Results | Gets the RFmxLteMXChpResults instance that provides methods to fetch and read the CHP measurement results. |

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

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/d96b68a0-39eb-2fc6-dc51-4fabfbaf1722.htm language=enus -->
## TOPIC 00318: rfmxltedotnet/html/d96b68a0-39eb-2fc6-dc51-4fabfbaf1722.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/d96b68a0-39eb-2fc6-dc51-4fabfbaf1722.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/d96b68a0-39eb-2fc6-dc51-4fabfbaf1722.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpConfiguration Class

RFmxLteMXTxpConfiguration Class

Provides methods to configure the TXP measurement.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXTxpConfiguration : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXTxpConfiguration
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXTxpConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the TXP measurement. |
|  | ConfigureMeasurementOffsetAndInterval | Configures the measurement offset and measurement interval for the transmit power (TXP) measurement. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Enables the traces to be stored and retrieved after the TXP measurement is performed. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when Averaging Enabled is True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for TXP measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMeasurementEnabled | Gets whether to enable the Transmit Power (TXP) measurement. |
|  | GetMeasurementInterval | Gets the measurement interval. This value is expressed in seconds. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism inside TXP measurement. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Enables the traces to be stored and retrieved after the TXP measurement is performed. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when Averaging Enabled is True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for TXP measurement. |
|  | SetMeasurementEnabled | Sets whether to enable the Transmit Power (TXP) measurement. |
|  | SetMeasurementInterval | Sets the measurement interval. This value is expressed in seconds. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism inside TXP measurement. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/dd033737-a22d-f1c0-764b-7bc6d1270433.htm language=enus -->
## TOPIC 00319: rfmxltedotnet/html/dd033737-a22d-f1c0-764b-7bc6d1270433.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/dd033737-a22d-f1c0-764b-7bc6d1270433.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/dd033737-a22d-f1c0-764b-7bc6d1270433.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetAutoControlChannelPowerDetectionEnabled Method

RFmxLteMXComponentCarrierGetAutoControlChannelPowerDetectionEnabled Method

Gets whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoControlChannelPowerDetectionEnabled(
	string selectorString,
	out RFmxLteMXAutoControlChannelPowerDetectionEnabled value
)
```

```text
Public Function GetAutoControlChannelPowerDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAutoControlChannelPowerDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoControlChannelPowerDetectionEnabledUpon return, contains whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported.

###### Return Value

Int32

##### Remarks

AutoControlChannelPowerDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/dd0ee166-cf9f-20e4-b4bc-7fca4db115ae.htm language=enus -->
## TOPIC 00320: rfmxltedotnet/html/dd0ee166-cf9f-20e4-b4bc-7fca4db115ae.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/dd0ee166-cf9f-20e4-b4bc-7fca4db115ae.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/dd0ee166-cf9f-20e4-b4bc-7fca4db115ae.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetIFOutputPowerOffsetAuto Method

RFmxLteMXAcpConfigurationSetIFOutputPowerOffsetAuto Method

SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod)

DynamicRange

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIFOutputPowerOffsetAuto(
	string selectorString,
	RFmxLteMXAcpIFOutputPowerOffsetAuto value
)
```

```text
Public Function SetIFOutputPowerOffsetAuto ( 
	selectorString As String,
	value As RFmxLteMXAcpIFOutputPowerOffsetAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpIFOutputPowerOffsetAuto Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange.

###### Return Value

Int32

##### Remarks

AcpIFOutputPowerOffsetAuto

True

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/dd1a1c3c-a5f3-a15c-aed8-21b81069e9b0.htm language=enus -->
## TOPIC 00321: rfmxltedotnet/html/dd1a1c3c-a5f3-a15c-aed8-21b81069e9b0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/dd1a1c3c-a5f3-a15c-aed8-21b81069e9b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/dd1a1c3c-a5f3-a15c-aed8-21b81069e9b0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpResults.GetSubblockFrequency Method

RFmxLteMXChpResultsGetSubblockFrequency Method

Gets the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSubblockFrequency(
	string selectorString,
	out double value
)
```

```text
Public Function GetSubblockFrequency ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ChpResultsSubblockFrequency

##### See Also

###### Reference

RFmxLteMXChpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/dd43c56c-0662-e37d-2bbd-1a3e2748639f.htm language=enus -->
## TOPIC 00322: rfmxltedotnet/html/dd43c56c-0662-e37d-2bbd-1a3e2748639f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/dd43c56c-0662-e37d-2bbd-1a3e2748639f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/dd43c56c-0662-e37d-2bbd-1a3e2748639f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetListStepTimerOffset Method

RFmxLteMXGetListStepTimerOffset Method

SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit)

SetDigitalEdgeTriggerSource(String, String)

TimerEvent

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetListStepTimerOffset(
	string selectorString,
	out double value
)
```

```text
Public Function GetListStepTimerOffset ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent

###### Return Value

Int32

##### Remarks

ListStepTimerOffset

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/deb950a9-c167-1df7-fb0c-5bc2cf695ae7.htm language=enus -->
## TOPIC 00323: rfmxltedotnet/html/deb950a9-c167-1df7-fb0c-5bc2cf695ae7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/deb950a9-c167-1df7-fb0c-5bc2cf695ae7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/deb950a9-c167-1df7-fb0c-5bc2cf695ae7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPsschPower Method

RFmxLteMXComponentCarrierSetPsschPower Method

Sets the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPsschPower(
	string selectorString,
	double value
)
```

```text
Public Function SetPsschPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PsschPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/dfcb29f7-7f2c-ecfd-839f-3d21a6e169f2.htm language=enus -->
## TOPIC 00324: rfmxltedotnet/html/dfcb29f7-7f2c-ecfd-839f-3d21a6e169f2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/dfcb29f7-7f2c-ecfd-839f-3d21a6e169f2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/dfcb29f7-7f2c-ecfd-839f-3d21a6e169f2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.GetSweepTimeAuto Method

RFmxLteMXChpConfigurationGetSweepTimeAuto Method

Gets whether the measurement computes the sweep time.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSweepTimeAuto(
	string selectorString,
	out RFmxLteMXChpSweepTimeAuto value
)
```

```text
Public Function GetSweepTimeAuto ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXChpSweepTimeAuto
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpSweepTimeAutoUpon return, contains whether the measurement computes the sweep time.

###### Return Value

Int32

##### Remarks

ChpSweepTimeAuto

True

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e07aabfd-4d1e-6e16-4941-eb3835d90730.htm language=enus -->
## TOPIC 00325: rfmxltedotnet/html/e07aabfd-4d1e-6e16-4941-eb3835d90730.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e07aabfd-4d1e-6e16-4941-eb3835d90730.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e07aabfd-4d1e-6e16-4941-eb3835d90730.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxpResults.GetAveragePowerMean Method

RFmxLteMXTxpResultsGetAveragePowerMean Method

Gets the average power of the acquired signal.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragePowerMean(
	string selectorString,
	out double value
)
```

```text
Public Function GetAveragePowerMean ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(String) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the average power of the acquired signal.

###### Return Value

Int32

##### Remarks

TxpResultsAveragePowerMean

##### See Also

###### Reference

RFmxLteMXTxpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e0843871-5a95-2487-999f-da5a8e16930e.htm language=enus -->
## TOPIC 00326: rfmxltedotnet/html/e0843871-5a95-2487-999f-da5a8e16930e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e0843871-5a95-2487-999f-da5a8e16930e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e0843871-5a95-2487-999f-da5a8e16930e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.ConfigureNumberOfGsmOffsets Method

RFmxLteMXAcpConfigurationConfigureNumberOfGsmOffsets Method

true

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNumberOfGsmOffsets(
	string selectorString,
	int numberOfGsmOffsets
)
```

```text
Public Function ConfigureNumberOfGsmOffsets ( 
	selectorString As String,
	numberOfGsmOffsets As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **numberOfGsmOffsets**
  - Type: SystemInt32 Specifies the number of GSM adjacent channel offsets to be configured when you set the SetBandwidth(String, Double) to 200.0k and when you set the ACP Configurable Number of Offset Enabled method to true. The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e0be02a6-3748-da0c-8143-a74ba14de5bf.htm language=enus -->
## TOPIC 00327: rfmxltedotnet/html/e0be02a6-3748-da0c-8143-a74ba14de5bf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e0be02a6-3748-da0c-8143-a74ba14de5bf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e0be02a6-3748-da0c-8143-a74ba14de5bf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetNumberOfAnalysisThreads Method

RFmxLteMXModAccConfigurationSetNumberOfAnalysisThreads Method

Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e0f8a7e4-5cb8-5d51-e5f2-ba2b10ca22a1.htm language=enus -->
## TOPIC 00328: rfmxltedotnet/html/e0f8a7e4-5cb8-5d51-e5f2-ba2b10ca22a1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e0f8a7e4-5cb8-5d51-e5f2-ba2b10ca22a1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e0f8a7e4-5cb8-5d51-e5f2-ba2b10ca22a1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetAutoLevelInitialReferenceLevel Method

RFmxLteMXGetAutoLevelInitialReferenceLevel Method

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the initial reference level that the AutoLevel(String, Double, Double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

AutoLevelInitialReferenceLevel

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e17164c6-c6b9-9ab7-b796-04fdca0aea3e.htm language=enus -->
## TOPIC 00329: rfmxltedotnet/html/e17164c6-c6b9-9ab7-b796-04fdca0aea3e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e17164c6-c6b9-9ab7-b796-04fdca0aea3e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e17164c6-c6b9-9ab7-b796-04fdca0aea3e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpAmplitudeCorrectionType Enumeration

RFmxLteMXAcpAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAcpAmplitudeCorrectionType
```

```text
Public Enumeration RFmxLteMXAcpAmplitudeCorrectionType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
|  | SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e1c28f38-f439-97e1-fd6a-59d4983848cc.htm language=enus -->
## TOPIC 00330: rfmxltedotnet/html/e1c28f38-f439-97e1-fd6a-59d4983848cc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e1c28f38-f439-97e1-fd6a-59d4983848cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e1c28f38-f439-97e1-fd6a-59d4983848cc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChp.Configuration Property

RFmxLteMXChpConfiguration Property

RFmxLteMXChpConfiguration

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXChpConfiguration Configuration { get; }
```

```text
Public ReadOnly Property Configuration As RFmxLteMXChpConfiguration
	Get
```

###### Property Value

RFmxLteMXChpConfiguration

##### See Also

###### Reference

RFmxLteMXChp Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e7fab768-4728-cb6a-4dd2-e16fcfa94af6.htm language=enus -->
## TOPIC 00331: rfmxltedotnet/html/e7fab768-4728-cb6a-4dd2-e16fcfa94af6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e7fab768-4728-cb6a-4dd2-e16fcfa94af6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e7fab768-4728-cb6a-4dd2-e16fcfa94af6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwResults.FetchMeasurement Method

RFmxLteMXObwResultsFetchMeasurement Method

LTE Occupied Bandwidth

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **occupiedBandwidth**
  - Type: SystemDouble Upon return, contains the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock.
- **absolutePower**
  - Type: SystemDouble Upon return, contains the power measured over the integration bandwidth of the carrier/subblock.
- **startFrequency**
  - Type: SystemDouble Upon return, contains the start frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth.
- **stopFrequency**
  - Type: SystemDouble Upon return, contains the stop frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXObwResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/e81d8210-db39-351e-ecb7-44a145f8480b.htm language=enus -->
## TOPIC 00332: rfmxltedotnet/html/e81d8210-db39-351e-ecb7-44a145f8480b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/e81d8210-db39-351e-ecb7-44a145f8480b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/e81d8210-db39-351e-ecb7-44a145f8480b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetSpectrumInverted Method

RFmxLteMXModAccConfigurationGetSpectrumInverted Method

Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSpectrumInverted(
	string selectorString,
	out RFmxLteMXModAccSpectrumInverted value
)
```

```text
Public Function GetSpectrumInverted ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccSpectrumInverted
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccSpectrumInvertedUpon return, contains whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

###### Return Value

Int32

##### Remarks

ModAccSpectrumInverted

False

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/eaafe810-83bb-bb48-d8b8-482641be4e0d.htm language=enus -->
## TOPIC 00333: rfmxltedotnet/html/eaafe810-83bb-bb48-d8b8-482641be4e0d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/eaafe810-83bb-bb48-d8b8-482641be4e0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/eaafe810-83bb-bb48-d8b8-482641be4e0d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObw.Results Property

RFmxLteMXObwResults Property

RFmxLteMXObwResults

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXObwResults Results { get; }
```

```text
Public ReadOnly Property Results As RFmxLteMXObwResults
	Get
```

###### Property Value

RFmxLteMXObwResults

##### See Also

###### Reference

RFmxLteMXObw Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/eb14cc76-fb08-5edd-a709-a3091512db6c.htm language=enus -->
## TOPIC 00334: rfmxltedotnet/html/eb14cc76-fb08-5edd-a709-a3091512db6c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/eb14cc76-fb08-5edd-a709-a3091512db6c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/eb14cc76-fb08-5edd-a709-a3091512db6c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetAcquisitionBandwidthOptimizationEnabled Method

RFmxLteMXSetAcquisitionBandwidthOptimizationEnabled Method

Sets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAcquisitionBandwidthOptimizationEnabled(
	string selectorString,
	RFmxLteMXAcquisitionBandwidthOptimizationEnabled value
)
```

```text
Public Function SetAcquisitionBandwidthOptimizationEnabled ( 
	selectorString As String,
	value As RFmxLteMXAcquisitionBandwidthOptimizationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcquisitionBandwidthOptimizationEnabledSpecifies whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

###### Return Value

Int32

##### Remarks

AcquisitionBandwidthOptimizationEnabled

True

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/eb83abf2-5486-1521-0a04-d56c4eed3c94.htm language=enus -->
## TOPIC 00335: rfmxltedotnet/html/eb83abf2-5486-1521-0a04-d56c4eed3c94.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/eb83abf2-5486-1521-0a04-d56c4eed3c94.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/eb83abf2-5486-1521-0a04-d56c4eed3c94.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtResults.GetBurstWidth Method

RFmxLteMXPvtResultsGetBurstWidth Method

Gets the width of the captured burst. This value is expressed in seconds. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBurstWidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetBurstWidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the width of the captured burst. This value is expressed in seconds. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

PvtResultsBurstWidth

##### See Also

###### Reference

RFmxLteMXPvtResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ebf48229-421d-05b7-fb13-0e137b7ab529.htm language=enus -->
## TOPIC 00336: rfmxltedotnet/html/ebf48229-421d-05b7-fb13-0e137b7ab529.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ebf48229-421d-05b7-fb13-0e137b7ab529.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ebf48229-421d-05b7-fb13-0e137b7ab529.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetComponentCarrierAtCenterFrequency Method

RFmxLteMXComponentCarrierSetComponentCarrierAtCenterFrequency Method

ComponentCarrierSpacingType

SetFrequency(String, Double)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetComponentCarrierAtCenterFrequency(
	string selectorString,
	int value
)
```

```text
Public Function SetComponentCarrierAtCenterFrequency ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the index of the component carrier having its center at the user-configured center frequency. RFmxLTE uses this method along with ComponentCarrierSpacingType method to calculate the value of the SetFrequency(String, Double).

###### Return Value

Int32

##### Remarks

ComponentCarrierAtCenterFrequency

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ec2c91fd-b70d-9ee4-dcf2-c9879a1c248b.htm language=enus -->
## TOPIC 00337: rfmxltedotnet/html/ec2c91fd-b70d-9ee4-dcf2-c9879a1c248b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ec2c91fd-b70d-9ee4-dcf2-c9879a1c248b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ec2c91fd-b70d-9ee4-dcf2-c9879a1c248b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration Class

RFmxLteMXModAccConfiguration Class

Provides methods to configure the ModAcc measurement.

##### Inheritance Hierarchy

RFmxLteMXSubObject

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public sealed class RFmxLteMXModAccConfiguration : RFmxLteMXSubObject
```

```text
Public NotInheritable Class RFmxLteMXModAccConfiguration
	Inherits RFmxLteMXSubObject
```

The RFmxLteMXModAccConfiguration type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAveraging | Configures averaging for the ModAcc measurement. |
|  | ConfigureCommonClockSourceEnabled | Configures the Reference Clock and specifies whether same Reference Clock is used for local oscillator and D/A converter. The ModAcc measurement ignores this method, when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Downlink. |
|  | ConfigureEvmUnit | Configures the units of the EVM results. |
|  | ConfigureFftWindowOffset | Configures the position of the FFT window that is used to calculate the EVM. |
|  | ConfigureFftWindowPosition | Configures the FFT window position used for an EVM calculation. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information about FFT window position. |
|  | ConfigureInBandEmissionMaskType | Configures the inBandEmissionMaskType parameter to be used. |
|  | ConfigureSynchronizationModeAndInterval | Configures the synchronizationhronizationMode, the measurementOffset, and the measurementLength parameters of the ModAcc measurement. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information about ModAcc measurements. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAllTracesEnabled | Gets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
|  | GetAveragingCount | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXModAccAveragingEnabled) method to True. |
|  | GetAveragingEnabled | Gets whether to enable averaging for the ModAcc measurement. |
|  | GetChannelEstimationType | Gets the method used for the channel estimation for the ModAcc measurement. |
|  | GetCommonClockSourceEnabled | Gets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
|  | GetEvmUnit | Gets the units of the EVM results. |
|  | GetEvmWithExclusionPeriodEnabled | Gets whether to exclude some portion of the slots when calculating the EVM. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP TS 36.521-1 specification for more information about exclusion. |
|  | GetFftWindowLength | Gets the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(String, RFmxLteMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of 3GPP 36.521 specification for more information. |
|  | GetFftWindowOffset | Gets the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this method to 0, the EVM window starts at the end of cyclic prefix. If you set this method to 100, the EVM window starts at the beginning of cyclic prefix. The default value is 50. Valid values are 0 to 100, inclusive. |
|  | GetFftWindowType | Gets the FFT window type used for the EVM calculation for the ModAcc measurement. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetInBandEmissionMaskType | Gets the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results. |
|  | GetIQGainImbalanceCorrectionEnabled | Gets whether to enable IQ gain imbalance correction. |
|  | GetIQMismatchEstimationEnabled | Gets whether to estimate IQ mismatch such as IQ gain imbalance, quadrature skew, and timing skew. NoteTiming skew value is estimated only when you set the Link direction property to Uplink. |
| Note |  |  |
| Timing skew value is estimated only when you set the Link direction property to Uplink. |  |  |
|  | GetIQOriginOffsetEstimationEnabled | Gets whether to estimate IQ origin offset. NoteIQ origin offset estimation is supported only when you set the Link direction property to Uplink or Sidelink. |
| Note |  |  |
| IQ origin offset estimation is supported only when you set the Link direction property to Uplink or Sidelink. |  |  |
|  | GetIQQuadratureErrorCorrectionEnabled | Gets whether to enable IQ quadrature error correction. |
|  | GetIQTimingSkewCorrectionEnabled | Gets whether to enable IQ timing skew correction. |
|  | GetMeasurementEnabled | Gets whether to enable the ModAcc measurement. |
|  | GetMeasurementLength | Gets the number of slots to be measured. This value is expressed in slots. |
|  | GetMeasurementOffset | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxLteMXModAccSynchronizationMode) method. This value is expressed in slots. |
|  | GetMulticarrierFilterEnabled | Gets whether to use a filter to suppress the interference from out of band emissions into the carriers being measured. |
|  | GetMultiCarrierFilterEnabled | Obsolete. Gets whether to use a filter to suppress the interference from out of band emissions into the carriers being measured. |
|  | GetMulticarrierTimeSynchronizationMode | Gets the time synchronization mode used in uplink in the case of carrier aggregation. |
|  | GetNumberOfAnalysisThreads | Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | GetPhaseTrackingEnabled | Gets whether phase tracking is enabled. |
|  | GetPreFftErrorEstimationInterval | Gets the interval used for Pre-FFT Error Estimation. |
|  | GetSpectralFlatnessCondition | Gets the frequency ranges at which to measure spectral flatness. |
|  | GetSpectrumInverted | Gets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
|  | GetSymbolClockErrorEstimationEnabled | Gets whether to estimate symbol clock error. |
|  | GetSynchronizationMode | Gets whether the measurement is performed from the frame or the slot boundary. |
|  | GetTimingTrackingEnabled | Gets whether timing tracking is enabled. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetAllTracesEnabled | Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
|  | SetAveragingCount | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(String, RFmxLteMXModAccAveragingEnabled) method to True. |
|  | SetAveragingEnabled | Sets whether to enable averaging for the ModAcc measurement. |
|  | SetChannelEstimationType | Sets the method used for the channel estimation for the ModAcc measurement. |
|  | SetCommonClockSourceEnabled | Sets whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. |
|  | SetEvmUnit | Sets the units of the EVM results. |
|  | SetEvmWithExclusionPeriodEnabled | Sets whether to exclude some portion of the slots when calculating the EVM. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP TS 36.521-1 specification for more information about exclusion. |
|  | SetFftWindowLength | Sets the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(String, RFmxLteMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of 3GPP 36.521 specification for more information. |
|  | SetFftWindowOffset | Sets the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this method to 0, the EVM window starts at the end of cyclic prefix. If you set this method to 100, the EVM window starts at the beginning of cyclic prefix. The default value is 50. Valid values are 0 to 100, inclusive. |
|  | SetFftWindowType | Sets the FFT window type used for the EVM calculation for the ModAcc measurement. |
|  | SetInBandEmissionMaskType | Sets the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results. |
|  | SetIQGainImbalanceCorrectionEnabled | Sets whether to enable IQ gain imbalance correction. |
|  | SetIQMismatchEstimationEnabled | Sets whether to estimate IQ mismatch such as IQ gain imbalance, quadrature skew, and timing skew. NoteTiming skew value is estimated only when you set the Link direction property to Uplink. |
| Note |  |  |
| Timing skew value is estimated only when you set the Link direction property to Uplink. |  |  |
|  | SetIQOriginOffsetEstimationEnabled | Sets whether to estimate IQ origin offset. NoteIQ origin offset estimation is supported only when you set the Link direction property to Uplink or Sidelink. |
| Note |  |  |
| IQ origin offset estimation is supported only when you set the Link direction property to Uplink or Sidelink. |  |  |
|  | SetIQQuadratureErrorCorrectionEnabled | Sets whether to enable IQ quadrature error correction. |
|  | SetIQTimingSkewCorrectionEnabled | Sets whether to enable IQ timing skew correction. |
|  | SetMeasurementEnabled | Sets whether to enable the ModAcc measurement. |
|  | SetMeasurementLength | Sets the number of slots to be measured. This value is expressed in slots. |
|  | SetMeasurementOffset | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(String, RFmxLteMXModAccSynchronizationMode) method. This value is expressed in slots. |
|  | SetMulticarrierFilterEnabled | Sets whether to use a filter to suppress the interference from out of band emissions into the carriers being measured. |
|  | SetMultiCarrierFilterEnabled | Obsolete. Sets whether to use a filter to suppress the interference from out of band emissions into the carriers being measured. |
|  | SetMulticarrierTimeSynchronizationMode | Sets the time synchronization mode used in uplink in the case of carrier aggregation. |
|  | SetNumberOfAnalysisThreads | Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
|  | SetPhaseTrackingEnabled | Sets whether phase tracking is enabled. |
|  | SetPreFftErrorEstimationInterval | Sets the interval used for Pre-FFT Error Estimation. |
|  | SetSpectralFlatnessCondition | Sets the frequency ranges at which to measure spectral flatness. |
|  | SetSpectrumInverted | Sets whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. |
|  | SetSymbolClockErrorEstimationEnabled | Sets whether to estimate symbol clock error. |
|  | SetSynchronizationMode | Sets whether the measurement is performed from the frame or the slot boundary. |
|  | SetTimingTrackingEnabled | Sets whether timing tracking is enabled. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ec78340f-39e1-7cf5-dea1-cab4e4768b44.htm language=enus -->
## TOPIC 00338: rfmxltedotnet/html/ec78340f-39e1-7cf5-dea1-cab4e4768b44.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ec78340f-39e1-7cf5-dea1-cab4e4768b44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ec78340f-39e1-7cf5-dea1-cab4e4768b44.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetTimingTrackingEnabled Method

RFmxLteMXModAccConfigurationGetTimingTrackingEnabled Method

Gets whether timing tracking is enabled.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTimingTrackingEnabled(
	string selectorString,
	out RFmxLteMXModAccTimingTrackingEnabled value
)
```

```text
Public Function GetTimingTrackingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccTimingTrackingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccTimingTrackingEnabledUpon return, contains whether timing tracking is enabled.

###### Return Value

Int32

##### Remarks

ModAccTimingTrackingEnabled

False

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ecb58f2c-27d1-7d51-1db5-63bc196f0955.htm language=enus -->
## TOPIC 00339: rfmxltedotnet/html/ecb58f2c-27d1-7d51-1db5-63bc196f0955.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ecb58f2c-27d1-7d51-1db5-63bc196f0955.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ecb58f2c-27d1-7d51-1db5-63bc196f0955.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXExtension.GetLteList Method

RFmxLteMXExtensionGetLteList Method

Creates a new Lte list if it doesn't exist; otherwise, it returns the
 existing Lte list.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static RFmxLteMXList GetLteList(
	this RFmxInstrMX instrSession,
	string listName
)
```

```text
<ExtensionAttribute>
Public Shared Function GetLteList ( 
	instrSession As RFmxInstrMX,
	listName As String
) As RFmxLteMXList
```

###### Parameters

- **instrSession**
  - Type: RFmxInstrMXSpecifies an instr session.
- **listName**
  - Type: SystemString Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::list1" "list1"

###### Return Value

RFmxLteMXList

###### Usage Note

RFmxInstrMX

Extension Methods (Visual Basic)

Extension Methods (C# Programming Guide)

##### See Also

###### Reference

RFmxLteMXExtension Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ed2cb8e2-0714-84a8-fc7a-f4f9fcc16c35.htm language=enus -->
## TOPIC 00340: rfmxltedotnet/html/ed2cb8e2-0714-84a8-fc7a-f4f9fcc16c35.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ed2cb8e2-0714-84a8-fc7a-f4f9fcc16c35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ed2cb8e2-0714-84a8-fc7a-f4f9fcc16c35.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetAutoDmrsDetectionEnabled Method

RFmxLteMXGetAutoDmrsDetectionEnabled Method

SetUplinkGroupHoppingEnabled(String, RFmxLteMXUplinkGroupHoppingEnabled)

SetUplinkSequenceHoppingEnabled(String, RFmxLteMXUplinkSequenceHoppingEnabled)

SetCellId(String, Int32)

SetPuschNDmrs1(String, Int32)

SetPuschNDmrs2(String, Int32)

SetPuschDeltaSequenceShift(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAutoDmrsDetectionEnabled(
	string selectorString,
	out RFmxLteMXAutoDmrsDetectionEnabled value
)
```

```text
Public Function GetAutoDmrsDetectionEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAutoDmrsDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoDmrsDetectionEnabled Upon return, contains whether you configure the values of the demodulation reference signal (DMRS) parameters, such as SetUplinkGroupHoppingEnabled(String, RFmxLteMXUplinkGroupHoppingEnabled), SetUplinkSequenceHoppingEnabled(String, RFmxLteMXUplinkSequenceHoppingEnabled), SetCellId(String, Int32), SetPuschNDmrs1(String, Int32), SetPuschNDmrs2(String, Int32), and SetPuschDeltaSequenceShift(String, Int32) properties, or if the values of these properties are auto-detected by the measurement.

###### Return Value

Int32

##### Remarks

AutoDmrsDetectionEnabled

False

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ed44e703-8668-b2c6-0b71-329b03aae195.htm language=enus -->
## TOPIC 00341: rfmxltedotnet/html/ed44e703-8668-b2c6-0b71-329b03aae195.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ed44e703-8668-b2c6-0b71-329b03aae195.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ed44e703-8668-b2c6-0b71-329b03aae195.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetNumberOfEutraOffsets Method

RFmxLteMXAcpConfigurationGetNumberOfEutraOffsets Method

Gets the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNumberOfEutraOffsets(
	string selectorString,
	out int value
)
```

```text
Public Function GetNumberOfEutraOffsets ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True.

###### Return Value

Int32

##### Remarks

AcpNumberOfEutraOffsets

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/edb1acd9-ab15-2bb7-6cfb-ff8807f076bf.htm language=enus -->
## TOPIC 00342: rfmxltedotnet/html/edb1acd9-ab15-2bb7-6cfb-ff8807f076bf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/edb1acd9-ab15-2bb7-6cfb-ff8807f076bf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/edb1acd9-ab15-2bb7-6cfb-ff8807f076bf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetBand Method

RFmxLteMXGetBand Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetBand(
	string selectorString,
	out int value
)
```

```text
Public Function GetBand ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Upon return, contains the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock, as defined in section 5.2 of the 3GPP TS 36.521 specification.

###### Return Value

Int32

##### Remarks

Band

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/edeb69c9-3ae8-955b-8d3a-4920cc76f7be.htm language=enus -->
## TOPIC 00343: rfmxltedotnet/html/edeb69c9-3ae8-955b-8d3a-4920cc76f7be.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/edeb69c9-3ae8-955b-8d3a-4920cc76f7be.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/edeb69c9-3ae8-955b-8d3a-4920cc76f7be.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpAveragingEnabled Enumeration

RFmxLteMXChpAveragingEnabled Enumeration

Specifies whether to enable averaging for the CHP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXChpAveragingEnabled
```

```text
Public Enumeration RFmxLteMXChpAveragingEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The measurement is performed on a single acquisition. |
|  | True | 1 | The CHP measurement uses the value of the SetAveragingCount(String, Int32) method as the number of acquisitions over which the CHP measurement is averaged. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ee53a735-a304-111a-6637-a9a3c80e7f07.htm language=enus -->
## TOPIC 00344: rfmxltedotnet/html/ee53a735-a304-111a-6637-a9a3c80e7f07.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ee53a735-a304-111a-6637-a9a3c80e7f07.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ee53a735-a304-111a-6637-a9a3c80e7f07.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXList.Dispose Method

RFmxLteMXListDispose Method

Deletes the list and clears any trace of the current list, if any.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Remarks

You can call this method safely more than once, even if the list is already deleted.

##### See Also

###### Reference

RFmxLteMXList Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ee5f63e9-ac76-9792-959e-e20eed8ff94b.htm language=enus -->
## TOPIC 00345: rfmxltedotnet/html/ee5f63e9-ac76-9792-959e-e20eed8ff94b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ee5f63e9-ac76-9792-959e-e20eed8ff94b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ee5f63e9-ac76-9792-959e-e20eed8ff94b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetLowerOffsetAbsolutePeakPower Method

RFmxLteMXSemResultsGetLowerOffsetAbsolutePeakPower Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetLowerOffsetAbsolutePeakPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetLowerOffsetAbsolutePeakPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetAbsolutePeakPower

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ee8f1401-4fe1-c158-e0d2-bf0c26069c44.htm language=enus -->
## TOPIC 00346: rfmxltedotnet/html/ee8f1401-4fe1-c158-e0d2-bf0c26069c44.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ee8f1401-4fe1-c158-e0d2-bf0c26069c44.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ee8f1401-4fe1-c158-e0d2-bf0c26069c44.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpMeasurementMethod Enumeration

RFmxLteMXAcpMeasurementMethod Enumeration

Specifies the method for performing the ACP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAcpMeasurementMethod
```

```text
Public Enumeration RFmxLteMXAcpMeasurementMethod
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
|  | DynamicRange | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668 |
|  | SequentialFft | 2 | The ACP measurement acquires I/Q samples for a duration specified by the SetSweepTimeInterval(String, Double) method. These samples are divided into smaller chunks. The size of each chunk is defined by the SetSequentialFftSize(String, Int32) method. FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Sequential FFT method should be used for the following scenarios.While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced.When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used.For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. NoteFor multi-Span FFT, the averaging count should be 1. |
| Note |  |  |  |
| For multi-Span FFT, the averaging count should be 1. |  |  |  |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/eee3f201-f234-2a71-68f2-3e8010e83a68.htm language=enus -->
## TOPIC 00347: rfmxltedotnet/html/eee3f201-f234-2a71-68f2-3e8010e83a68.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/eee3f201-f234-2a71-68f2-3e8010e83a68.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/eee3f201-f234-2a71-68f2-3e8010e83a68.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetRbwFilterAutoBandwidth Method

RFmxLteMXChpConfigurationSetRbwFilterAutoBandwidth Method

Sets whether the CHP measurement computes the RBW.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetRbwFilterAutoBandwidth(
	string selectorString,
	RFmxLteMXChpRbwAutoBandwidth value
)
```

```text
Public Function SetRbwFilterAutoBandwidth ( 
	selectorString As String,
	value As RFmxLteMXChpRbwAutoBandwidth
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpRbwAutoBandwidthSpecifies whether the CHP measurement computes the RBW.

###### Return Value

Int32

##### Remarks

ChpRbwFilterAutoBandwidth

True

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/eef1346e-7254-1212-c53c-9770e4e71656.htm language=enus -->
## TOPIC 00348: rfmxltedotnet/html/eef1346e-7254-1212-c53c-9770e4e71656.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/eef1346e-7254-1212-c53c-9770e4e71656.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/eef1346e-7254-1212-c53c-9770e4e71656.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPuschSymbolPowerArray Method

RFmxLteMXModAccResultsFetchPuschSymbolPowerArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPuschSymbolPowerArray(
	string selectorString,
	double timeout,
	ref double[] puschMeanDataPower,
	ref double[] puschMeanDmrsPower
)
```

```text
Public Function FetchPuschSymbolPowerArray ( 
	selectorString As String,
	timeout As Double,
	ByRef puschMeanDataPower As Double(),
	ByRef puschMeanDmrsPower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **puschMeanDataPower**
  - Type: SystemDouble Upon return, contains the array of the mean value of the power calculated on PUSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method.
- **puschMeanDmrsPower**
  - Type: SystemDouble Upon return, contains the array of the mean value of the power calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ef6a4f3d-e80c-b65c-50bd-96c6ed767bf3.htm language=enus -->
## TOPIC 00349: rfmxltedotnet/html/ef6a4f3d-e80c-b65c-50bd-96c6ed767bf3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ef6a4f3d-e80c-b65c-50bd-96c6ed767bf3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ef6a4f3d-e80c-b65c-50bd-96c6ed767bf3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetNPuschMaximumPeakDataEvm Method

RFmxLteMXModAccResultsGetNPuschMaximumPeakDataEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNPuschMaximumPeakDataEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetNPuschMaximumPeakDataEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method.

###### Return Value

Int32

##### Remarks

ModAccResultsNPuschMaximumPeakDataEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ef6ebafe-4604-f0dd-ae37-f25debec51ba.htm language=enus -->
## TOPIC 00350: rfmxltedotnet/html/ef6ebafe-4604-f0dd-ae37-f25debec51ba.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ef6ebafe-4604-f0dd-ae37-f25debec51ba.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ef6ebafe-4604-f0dd-ae37-f25debec51ba.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetMeanRmsCompositeMagnitudeError Method

RFmxLteMXModAccResultsGetMeanRmsCompositeMagnitudeError Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanRmsCompositeMagnitudeError(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanRmsCompositeMagnitudeError ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the RMS mean value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(String, Int32) method on all the configured channels.

###### Return Value

Int32

##### Remarks

ModAccResultsMeanRmsCompositeMagnitudeError

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ef9643db-059e-ab7b-07fd-31ce242cdd08.htm language=enus -->
## TOPIC 00351: rfmxltedotnet/html/ef9643db-059e-ab7b-07fd-31ce242cdd08.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ef9643db-059e-ab7b-07fd-31ce242cdd08.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ef9643db-059e-ab7b-07fd-31ce242cdd08.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetUpperOffsetRelativePeakPower Method

RFmxLteMXSemResultsGetUpperOffsetRelativePeakPower Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

SemResultsUpperOffsetRelativePeakPower

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/efeedc61-b8ae-d623-bf61-52263160cc08.htm language=enus -->
## TOPIC 00352: rfmxltedotnet/html/efeedc61-b8ae-d623-bf61-52263160cc08.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/efeedc61-b8ae-d623-bf61-52263160cc08.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/efeedc61-b8ae-d623-bf61-52263160cc08.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPssPower Method

RFmxLteMXComponentCarrierGetPssPower Method

Gets the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPssPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetPssPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PssPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/eff10012-c161-014d-870a-b19f501cff52.htm language=enus -->
## TOPIC 00353: rfmxltedotnet/html/eff10012-c161-014d-870a-b19f501cff52.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/eff10012-c161-014d-870a-b19f501cff52.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/eff10012-c161-014d-870a-b19f501cff52.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.ConfigureNPuschDmrs Method

RFmxLteMXComponentCarrierConfigureNPuschDmrs Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureNPuschDmrs(
	string selectorString,
	RFmxLteMXNPuschDmrsBaseSequenceMode nPuschDmrsBaseSequenceMode,
	int nPuschDmrsBaseSequenceIndex,
	int nPuschDmrsCyclicShift,
	RFmxLteMXNPuschDmrsGroupHoppingEnabled nPuschDmrsGroupHoppingEnabled,
	int nPuschDmrsDeltaSS
)
```

```text
Public Function ConfigureNPuschDmrs ( 
	selectorString As String,
	nPuschDmrsBaseSequenceMode As RFmxLteMXNPuschDmrsBaseSequenceMode,
	nPuschDmrsBaseSequenceIndex As Integer,
	nPuschDmrsCyclicShift As Integer,
	nPuschDmrsGroupHoppingEnabled As RFmxLteMXNPuschDmrsGroupHoppingEnabled,
	nPuschDmrsDeltaSS As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **nPuschDmrsBaseSequenceMode**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXNPuschDmrsBaseSequenceMode Specifies whether the NPUSCHDMRSBaseSequenceindex is computed by the measurement or user-specified. This parameter is valid when you set the NPUSCHDMRSGroupHoppingEnabled parameter to False, the value of SetNPuschFormat(String, Int32) method to 1, and the value of NPUSCH Number of Tones method to 3, 6, or 12.
- **nPuschDmrsBaseSequenceIndex**
  - Type: SystemInt32 Specifies the base sequence index of the NPUSCH DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. This parameter is valid when you set the NPUSCHDMRSGroupHoppingEnabled parameter to False, the NPUSCHDMRSBaseSequenceMode parameter to Manual, and the value of NPUSCH Number of Tones method to 3, 6, or 12.
- **nPuschDmrsCyclicShift**
  - Type: SystemInt32 Specifies the cyclic shift of the NPUSCH DMRS as defined in table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification.
- **nPuschDmrsGroupHoppingEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXNPuschDmrsGroupHoppingEnabled Specifies whether group hopping is enabled for the NPUSCH DMRS. This parameter is valid when the value of SetNPuschFormat(String, Int32) is equal to 1.
- **nPuschDmrsDeltaSS**
  - Type: SystemInt32 Specifies the delta sequence shift of the NPUSCH DMRS that is used to calculate the sequence shift pattern, which in turn is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This parameter is valid when you set the NPUSCHDMRSGroupHoppingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f01c5cd2-17c9-e952-4e8a-486196b6687c.htm language=enus -->
## TOPIC 00354: rfmxltedotnet/html/f01c5cd2-17c9-e952-4e8a-486196b6687c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f01c5cd2-17c9-e952-4e8a-486196b6687c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f01c5cd2-17c9-e952-4e8a-486196b6687c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPdschCW0ModulationType Method

RFmxLteMXComponentCarrierGetPdschCW0ModulationType Method

Gets the modulation type of codeword0 PDSCH allocation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschCW0ModulationType(
	string selectorString,
	out RFmxLteMXUserDefinedPdschCW0ModulationType value
)
```

```text
Public Function GetPdschCW0ModulationType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXUserDefinedPdschCW0ModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the subblock number, carrier number, subframe number and pdsch number. Example: "pdsch0" or "subframe0" or "carrier0" or "subblock0" or "subblock0/carrier0/subframe0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXUserDefinedPdschCW0ModulationTypeUpon return, contains the modulation type of codeword0 PDSCH allocation.

###### Return Value

Int32

##### Remarks

PdschCW0ModulationType

Qpsk

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f04531b7-8269-222e-a072-a743db169ed3.htm language=enus -->
## TOPIC 00355: rfmxltedotnet/html/f04531b7-8269-222e-a072-a743db169ed3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f04531b7-8269-222e-a072-a743db169ed3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f04531b7-8269-222e-a072-a743db169ed3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetMiConfiguration Method

RFmxLteMXSetMiConfiguration Method

3GPP TS 36.141

3GPP TS 36.211

SetDuplexScheme(String, RFmxLteMXDuplexScheme)

Tdd

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMiConfiguration(
	string selectorString,
	RFmxLteMXMiConfiguration value
)
```

```text
Public Function SetMiConfiguration ( 
	selectorString As String,
	value As RFmxLteMXMiConfiguration
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXMiConfiguration Specifies whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the SetDuplexScheme(String, RFmxLteMXDuplexScheme) method to Tdd.

###### Return Value

Int32

##### Remarks

MiConfiguration

Standard

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f0519038-5326-40ff-7e4c-6a0810697761.htm language=enus -->
## TOPIC 00356: rfmxltedotnet/html/f0519038-5326-40ff-7e4c-6a0810697761.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f0519038-5326-40ff-7e4c-6a0810697761.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f0519038-5326-40ff-7e4c-6a0810697761.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPuschMeanRmsDataEvm Method

RFmxLteMXModAccResultsGetPuschMeanRmsDataEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschMeanRmsDataEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetPuschMeanRmsDataEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of the RMS EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsPuschMeanRmsDataEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f051b74a-c47a-fd21-95cc-759771d697c1.htm language=enus -->
## TOPIC 00357: rfmxltedotnet/html/f051b74a-c47a-fd21-95cc-759771d697c1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f051b74a-c47a-fd21-95cc-759771d697c1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f051b74a-c47a-fd21-95cc-759771d697c1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.FetchLowerOffsetMargin Method

RFmxLteMXSemResultsFetchLowerOffsetMargin Method

LTE Uplink Spectral Emission Mask

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchLowerOffsetMargin(
	string selectorString,
	double timeout,
	out RFmxLteMXSemLowerOffsetMeasurementStatus measurementStatus,
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
	<OutAttribute> ByRef measurementStatus As RFmxLteMXSemLowerOffsetMeasurementStatus,
	<OutAttribute> ByRef margin As Double,
	<OutAttribute> ByRef marginFrequency As Double,
	<OutAttribute> ByRef marginAbsolutePower As Double,
	<OutAttribute> ByRef marginRelativePower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **measurementStatus**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemLowerOffsetMeasurementStatus Upon return, contains the measurement status indicating whether the power before and after the burst is within the standard defined limit.
- **margin**
  - Type: SystemDouble Upon return, contains the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginFrequency**
  - Type: SystemDouble Upon return, contains the frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginAbsolutePower**
  - Type: SystemDouble Upon return, contains the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.
- **marginRelativePower**
  - Type: SystemDouble Upon return, contains the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the GetTotalAggregatedPower(String, Double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f058c1cd-e14a-05cb-8184-5c212795d7f6.htm language=enus -->
## TOPIC 00358: rfmxltedotnet/html/f058c1cd-e14a-05cb-8184-5c212795d7f6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f058c1cd-e14a-05cb-8184-5c212795d7f6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f058c1cd-e14a-05cb-8184-5c212795d7f6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPdschMeanRms256QamEvm Method

RFmxLteMXModAccResultsGetPdschMeanRms256QamEvm Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschMeanRms256QamEvm(
	string selectorString,
	out double value
)
```

```text
Public Function GetPdschMeanRms256QamEvm ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(String, Int32) method.

###### Return Value

Int32

##### Remarks

ModAccResultsPdschMeanRms256QamEvm

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f1138b7c-4b56-1f37-afb7-fbd1af5cc4b0.htm language=enus -->
## TOPIC 00359: rfmxltedotnet/html/f1138b7c-4b56-1f37-afb7-fbd1af5cc4b0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f1138b7c-4b56-1f37-afb7-fbd1af5cc4b0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f1138b7c-4b56-1f37-afb7-fbd1af5cc4b0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetSelectedPorts Method

RFmxLteMXSetSelectedPorts Method

Valid values

Default values

Supported devices: PXIe-5820/5830/5831/5832/5840

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringSpecifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names.

###### Return Value

Int32

##### Remarks

SelectedPorts

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f156bf44-321f-1ab9-f163-2af8262a6418.htm language=enus -->
## TOPIC 00360: rfmxltedotnet/html/f156bf44-321f-1ab9-f163-2af8262a6418.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f156bf44-321f-1ab9-f163-2af8262a6418.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f156bf44-321f-1ab9-f163-2af8262a6418.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetNumberOfOffsets Method

RFmxLteMXSemConfigurationGetNumberOfOffsets Method

Gets the number of SEM offset segments.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemString Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the number of SEM offset segments.

###### Return Value

Int32

##### Remarks

SemNumberOfOffsets

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f16657df-ab6e-79c3-1e4c-28b9864f2f5f.htm language=enus -->
## TOPIC 00361: rfmxltedotnet/html/f16657df-ab6e-79c3-1e4c-28b9864f2f5f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f16657df-ab6e-79c3-1e4c-28b9864f2f5f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f16657df-ab6e-79c3-1e4c-28b9864f2f5f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.GetRbwFilterBandwidth Method

RFmxLteMXObwConfigurationGetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxLteMXObwRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ObwRbwFilterBandwidth

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f190c627-f031-fec3-fffe-588afd35f3c6.htm language=enus -->
## TOPIC 00362: rfmxltedotnet/html/f190c627-f031-fec3-fffe-588afd35f3c6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f190c627-f031-fec3-fffe-588afd35f3c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f190c627-f031-fec3-fffe-588afd35f3c6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPdschPower Method

RFmxLteMXComponentCarrierSetPdschPower Method

SetDownlinkUserDefinedCellSpecificRatio(String, RFmxLteMXDownlinkUserDefinedRatio)

3GPP 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPdschPower(
	string selectorString,
	double value
)
```

```text
Public Function SetPdschPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the subblock number, carrier number, subframe number and pdsch number. Example: "pdsch0" or "subframe0" or "carrier0" or "subblock0" or "subblock0/carrier0/subframe0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the SetDownlinkUserDefinedCellSpecificRatio(String, RFmxLteMXDownlinkUserDefinedRatio) method to calculate the Rb. Refer to section 3.3 of the 3GPP 36.521 specification for more information about Ra.

###### Return Value

Int32

##### Remarks

PdschPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f1917570-56a1-4889-72cc-c2585235da0e.htm language=enus -->
## TOPIC 00363: rfmxltedotnet/html/f1917570-56a1-4889-72cc-c2585235da0e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f1917570-56a1-4889-72cc-c2585235da0e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f1917570-56a1-4889-72cc-c2585235da0e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetSrsMaximumUpPtsEnabled Method

RFmxLteMXComponentCarrierSetSrsMaximumUpPtsEnabled Method

3GPP 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSrsMaximumUpPtsEnabled(
	string selectorString,
	RFmxLteMXSrsMaximumUpPtsEnabled value
)
```

```text
Public Function SetSrsMaximumUpPtsEnabled ( 
	selectorString As String,
	value As RFmxLteMXSrsMaximumUpPtsEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSrsMaximumUpPtsEnabled Specifies SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details.

###### Return Value

Int32

##### Remarks

SrsMaximumUpPtsEnabled

False

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f222a091-0e55-dde2-3f1e-8ffc891c0849.htm language=enus -->
## TOPIC 00364: rfmxltedotnet/html/f222a091-0e55-dde2-3f1e-8ffc891c0849.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f222a091-0e55-dde2-3f1e-8ffc891c0849.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f222a091-0e55-dde2-3f1e-8ffc891c0849.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPdschResourceBlockAllocation Method

RFmxLteMXComponentCarrierGetPdschResourceBlockAllocation Method

Gets the resource blocks of the physical downlink shared channel (PDSCH) allocation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPdschResourceBlockAllocation(
	string selectorString,
	out string value
)
```

```text
Public Function GetPdschResourceBlockAllocation ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the subblock number, carrier number, subframe number and pdsch number. Example: "pdsch0" or "subframe0" or "carrier0" or "subblock0" or "subblock0/carrier0/subframe0/pdsch0". You can use the BuildPdschString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemStringUpon return, contains the resource blocks of the physical downlink shared channel (PDSCH) allocation.

###### Return Value

Int32

##### Remarks

PdschResourceBlockAllocation

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f2425913-da5e-7d6c-5fdb-c87bfc3578a7.htm language=enus -->
## TOPIC 00365: rfmxltedotnet/html/f2425913-da5e-7d6c-5fdb-c87bfc3578a7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f2425913-da5e-7d6c-5fdb-c87bfc3578a7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f2425913-da5e-7d6c-5fdb-c87bfc3578a7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.GetMeasurementMethod Method

RFmxLteMXPvtConfigurationGetMeasurementMethod Method

Gets the method for performing the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementMethod(
	string selectorString,
	out RFmxLteMXPvtMeasurementMethod value
)
```

```text
Public Function GetMeasurementMethod ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXPvtMeasurementMethod
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPvtMeasurementMethodUpon return, contains the method for performing the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtMeasurementMethod

Normal

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f25e0061-2af1-128f-dda8-f90550d930b3.htm language=enus -->
## TOPIC 00366: rfmxltedotnet/html/f25e0061-2af1-128f-dda8-f90550d930b3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f25e0061-2af1-128f-dda8-f90550d930b3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f25e0061-2af1-128f-dda8-f90550d930b3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetSweepTimeInterval Method

RFmxLteMXSemConfigurationGetSweepTimeInterval Method

SetSweepTimeAuto(String, RFmxLteMXSemSweepTimeAuto)

False

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the sweep time when you set the SetSweepTimeAuto(String, RFmxLteMXSemSweepTimeAuto) method to False. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SemSweepTimeInterval

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f27a22eb-a8f9-dba9-3455-2255ce3b097b.htm language=enus -->
## TOPIC 00367: rfmxltedotnet/html/f27a22eb-a8f9-dba9-3455-2255ce3b097b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f27a22eb-a8f9-dba9-3455-2255ce3b097b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f27a22eb-a8f9-dba9-3455-2255ce3b097b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchDownlinkDetectedCellID Method

RFmxLteMXModAccResultsFetchDownlinkDetectedCellID Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchDownlinkDetectedCellID(
	string selectorString,
	double timeout,
	out int detectedCellID
)
```

```text
Public Function FetchDownlinkDetectedCellID ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef detectedCellID As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **detectedCellID**
  - Type: SystemInt32 Upon return, contains the detected cell ID value.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f287d3ca-a755-8efe-4f86-532868693e60.htm language=enus -->
## TOPIC 00368: rfmxltedotnet/html/f287d3ca-a755-8efe-4f86-532868693e60.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f287d3ca-a755-8efe-4f86-532868693e60.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f287d3ca-a755-8efe-4f86-532868693e60.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchNPuschDataEvm Method

RFmxLteMXModAccResultsFetchNPuschDataEvm Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchNPuschDataEvm(
	string selectorString,
	double timeout,
	out double nPuschMeanRmsDataEvm,
	out double nPuschMaximumPeakDataEvm
)
```

```text
Public Function FetchNPuschDataEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef nPuschMeanRmsDataEvm As Double,
	<OutAttribute> ByRef nPuschMaximumPeakDataEvm As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **nPuschMeanRmsDataEvm**
  - Type: SystemDouble Upon return, contains the mean value of the RMS EVMs calculated on the NPUSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the result is returned as a percentage, and when you set the ModAcc EVM Unit method to dB, the result is returned in dB.
- **nPuschMaximumPeakDataEvm**
  - Type: SystemDouble Upon return, contains the maximum value of the peak EVMs calculated on the NPUSCH data symbols over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the result is returned as a percentage. When you set the ModAcc EVM Unit method to dB, the result is returned in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f28e3923-1ef4-cbb1-cdd1-8a29f9b4b2b2.htm language=enus -->
## TOPIC 00369: rfmxltedotnet/html/f28e3923-1ef4-cbb1-cdd1-8a29f9b4b2b2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f28e3923-1ef4-cbb1-cdd1-8a29f9b4b2b2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f28e3923-1ef4-cbb1-cdd1-8a29f9b4b2b2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetAutoNPuschChannelDetectionEnabled Method

RFmxLteMXComponentCarrierSetAutoNPuschChannelDetectionEnabled Method

SetNPuschToneOffset(String, Int32)

SetNPuschModulationType(String, RFmxLteMXNPuschModulationType)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoNPuschChannelDetectionEnabled(
	string selectorString,
	RFmxLteMXAutoNPuschChannelDetectionEnabled value
)
```

```text
Public Function SetAutoNPuschChannelDetectionEnabled ( 
	selectorString As String,
	value As RFmxLteMXAutoNPuschChannelDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoNPuschChannelDetectionEnabled Specifies whether the values of the SetNPuschToneOffset(String, Int32), NPUSCH Number of Tones, and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) properties are auto-detected by the measurement or specified by you.

###### Return Value

Int32

##### Remarks

AutoNPuschChannelDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f29fd0a2-1a20-09d8-a926-938acca845b1.htm language=enus -->
## TOPIC 00370: rfmxltedotnet/html/f29fd0a2-1a20-09d8-a926-938acca845b1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f29fd0a2-1a20-09d8-a926-938acca845b1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f29fd0a2-1a20-09d8-a926-938acca845b1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpComponentCarrierResults.GetAbsolutePower Method

RFmxLteMXChpComponentCarrierResultsGetAbsolutePower Method

Gets the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAbsolutePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetAbsolutePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

RFmxLteMXChpComponentCarrierResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f2f982ff-0472-0df6-2ce7-721bf070783e.htm language=enus -->
## TOPIC 00371: rfmxltedotnet/html/f2f982ff-0472-0df6-2ce7-721bf070783e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f2f982ff-0472-0df6-2ce7-721bf070783e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f2f982ff-0472-0df6-2ce7-721bf070783e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetOffsetLimitFailMask Method

RFmxLteMXSemConfigurationGetOffsetLimitFailMask Method

Gets the criteria to determine the measurement fail status.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetLimitFailMask(
	string selectorString,
	out RFmxLteMXSemOffsetLimitFailMask value
)
```

```text
Public Function GetOffsetLimitFailMask ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSemOffsetLimitFailMask
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemOffsetLimitFailMaskUpon return, contains the criteria to determine the measurement fail status.

###### Return Value

Int32

##### Remarks

SemOffsetLimitFailMask

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f314f5c2-5458-abe1-97c4-cc2919c27d1f.htm language=enus -->
## TOPIC 00372: rfmxltedotnet/html/f314f5c2-5458-abe1-97c4-cc2919c27d1f.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f314f5c2-5458-abe1-97c4-cc2919c27d1f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f314f5c2-5458-abe1-97c4-cc2919c27d1f.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPsschModulationType Enumeration

RFmxLteMXPsschModulationType Enumeration

Specifies the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXPsschModulationType
```

```text
Public Enumeration RFmxLteMXPsschModulationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Qpsk | 0 | Specifies a QPSK modulation scheme. |
|  | Qam16 | 1 | Specifies a 16-QAM modulation scheme. |
|  | Qam64 | 2 | Specifies a 64-QAM modulation scheme. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f31f2e82-039c-dc40-b507-45efa2658922.htm language=enus -->
## TOPIC 00373: rfmxltedotnet/html/f31f2e82-039c-dc40-b507-45efa2658922.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f31f2e82-039c-dc40-b507-45efa2658922.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f31f2e82-039c-dc40-b507-45efa2658922.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetNearIFOutputPowerOffset Method

RFmxLteMXAcpConfigurationGetNearIFOutputPowerOffset Method

SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto)

False

SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod)

DynamicRange

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Upon return, contains the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange.

###### Return Value

Int32

##### Remarks

AcpNearIFOutputPowerOffset

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f35b95f2-055b-c5f8-8e5e-ec8c4b091361.htm language=enus -->
## TOPIC 00374: rfmxltedotnet/html/f35b95f2-055b-c5f8-8e5e-ec8c4b091361.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f35b95f2-055b-c5f8-8e5e-ec8c4b091361.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f35b95f2-055b-c5f8-8e5e-ec8c4b091361.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpResults.GetUpperOffsetRelativePower Method

RFmxLteMXAcpResultsGetUpperOffsetRelativePower Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUpperOffsetRelativePower(
	string selectorString,
	out double value
)
```

```text
Public Function GetUpperOffsetRelativePower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. For the intra-band non-contiguous type of carrier aggregation, if this offset is not applicable, a NaN is returned. Refer to the 3GPP TS 36.521 specification for more information about the applicability of the offset channel. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

AcpResultsUpperOffsetRelativePower

##### See Also

###### Reference

RFmxLteMXAcpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f37b0383-6f30-9faf-f7cd-bf41286ebd2d.htm language=enus -->
## TOPIC 00375: rfmxltedotnet/html/f37b0383-6f30-9faf-f7cd-bf41286ebd2d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f37b0383-6f30-9faf-f7cd-bf41286ebd2d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f37b0383-6f30-9faf-f7cd-bf41286ebd2d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetCellId Method

RFmxLteMXComponentCarrierSetCellId Method

Sets a physical layer cell identity.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetCellId(
	string selectorString,
	int value
)
```

```text
Public Function SetCellId ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Specifies a physical layer cell identity.

###### Return Value

Int32

##### Remarks

CellId

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f3bcb5c0-26ff-fbaa-f260-05b321628625.htm language=enus -->
## TOPIC 00376: rfmxltedotnet/html/f3bcb5c0-26ff-fbaa-f260-05b321628625.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f3bcb5c0-26ff-fbaa-f260-05b321628625.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f3bcb5c0-26ff-fbaa-f260-05b321628625.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetAveragingType Method

RFmxLteMXChpConfigurationSetAveragingType Method

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAveragingType(
	string selectorString,
	RFmxLteMXChpAveragingType value
)
```

```text
Public Function SetAveragingType ( 
	selectorString As String,
	value As RFmxLteMXChpAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpAveragingTypeSpecifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

###### Return Value

Int32

##### Remarks

ChpAveragingType

Rms

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f3d404e3-eda0-74e3-27c1-8771aa2a9295.htm language=enus -->
## TOPIC 00377: rfmxltedotnet/html/f3d404e3-eda0-74e3-27c1-8771aa2a9295.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f3d404e3-eda0-74e3-27c1-8771aa2a9295.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f3d404e3-eda0-74e3-27c1-8771aa2a9295.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetSymbolClockErrorEstimationEnabled Method

RFmxLteMXModAccConfigurationSetSymbolClockErrorEstimationEnabled Method

Sets whether to estimate symbol clock error.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetSymbolClockErrorEstimationEnabled(
	string selectorString,
	RFmxLteMXModAccSymbolClockErrorEstimationEnabled value
)
```

```text
Public Function SetSymbolClockErrorEstimationEnabled ( 
	selectorString As String,
	value As RFmxLteMXModAccSymbolClockErrorEstimationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccSymbolClockErrorEstimationEnabledSpecifies whether to estimate symbol clock error.

###### Return Value

Int32

##### Remarks

ModAccSymbolClockErrorEstimationEnabled

True

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f3d61356-505b-33e5-e42e-c101f62d3cc3.htm language=enus -->
## TOPIC 00378: rfmxltedotnet/html/f3d61356-505b-33e5-e42e-c101f62d3cc3.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f3d61356-505b-33e5-e42e-c101f62d3cc3.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f3d61356-505b-33e5-e42e-c101f62d3cc3.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.SetFarIFOutputPowerOffset Method

RFmxLteMXAcpConfigurationSetFarIFOutputPowerOffset Method

SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto)

False

SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod)

DynamicRange

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetFarIFOutputPowerOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetFarIFOutputPowerOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(String, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(String, RFmxLteMXAcpMeasurementMethod) method to DynamicRange.

###### Return Value

Int32

##### Remarks

AcpFarIFOutputPowerOffset

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f3e00de4-e7f4-cab7-d19f-dad87de8a39c.htm language=enus -->
## TOPIC 00379: rfmxltedotnet/html/f3e00de4-e7f4-cab7-d19f-dad87de8a39c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f3e00de4-e7f4-cab7-d19f-dad87de8a39c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f3e00de4-e7f4-cab7-d19f-dad87de8a39c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPhase Properties

RFmxLteMXSlotPhase Properties

The [RFmxLteMXSlotPhase](445655b6-8183-6448-072d-2d9b240cf77d.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Configuration | Gets the RFmxLteMXSlotPhaseConfiguration instance that provides methods to configure the SlotPhase measurement. |
|  | Results | Gets the RFmxLteMXSlotPhaseResults instance that provides methods to fetch and read the SlotPhase measurement results. |

Top

##### See Also

###### Reference

RFmxLteMXSlotPhase Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f4151a70-0c6a-9c55-e206-897d2545a648.htm language=enus -->
## TOPIC 00380: rfmxltedotnet/html/f4151a70-0c6a-9c55-e206-897d2545a648.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f4151a70-0c6a-9c55-e206-897d2545a648.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f4151a70-0c6a-9c55-e206-897d2545a648.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.ConfigureAveraging Method

RFmxLteMXModAccConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxLteMXModAccAveragingEnabled averagingEnabled,
	int averagingCount
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxLteMXModAccAveragingEnabled,
	averagingCount As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccAveragingEnabledSpecifies whether to enable averaging for the measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f41a3840-d74b-4323-2d25-c1c9c30b5b6d.htm language=enus -->
## TOPIC 00381: rfmxltedotnet/html/f41a3840-d74b-4323-2d25-c1c9c30b5b6d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f41a3840-d74b-4323-2d25-c1c9c30b5b6d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f41a3840-d74b-4323-2d25-c1c9c30b5b6d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXExtension Class

RFmxLteMXExtension Class

Provides extension methods to create LTE signal configuration. These methods are added to RFmxInstrMX class.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static class RFmxLteMXExtension
```

```text
<ExtensionAttribute>
Public NotInheritable Class RFmxLteMXExtension
```

The RFmxLteMXExtension type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetLteList | Creates a new Lte list if it doesn't exist; otherwise, it returns the existing Lte list. |
|  | GetLteSignalConfiguration(RFmxInstrMX) | Creates a new default LTE signal configuration if it doesn't exist; otherwise, it returns the existing default LTE signal configuration. |
|  | GetLteSignalConfiguration(RFmxInstrMX, String) | Creates a LTE signal configuration for specified signal name. Existing LTE signal configuration is returned if specified signal name exists. |
|  | LteClearNoiseCalibrationDatabase | Clears the noise calibration database used for noise compensation. |

Top

##### Remarks

For more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f45b36b7-6183-adf6-d52a-cfbd35180516.htm language=enus -->
## TOPIC 00382: rfmxltedotnet/html/f45b36b7-6183-adf6-d52a-cfbd35180516.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f45b36b7-6183-adf6-d52a-cfbd35180516.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f45b36b7-6183-adf6-d52a-cfbd35180516.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetNBIoTUplinkSubcarrierSpacing Method

RFmxLteMXComponentCarrierGetNBIoTUplinkSubcarrierSpacing Method

Gets the subcarrier bandwidth of an NB-IoT signal. This method specifies the spacing between adjacent subcarriers.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNBIoTUplinkSubcarrierSpacing(
	string selectorString,
	out RFmxLteMXNBIoTUplinkSubcarrierSpacing value
)
```

```text
Public Function GetNBIoTUplinkSubcarrierSpacing ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXNBIoTUplinkSubcarrierSpacing
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXNBIoTUplinkSubcarrierSpacingUpon return, contains the subcarrier bandwidth of an NB-IoT signal. This method specifies the spacing between adjacent subcarriers.

###### Return Value

Int32

##### Remarks

NBIoTUplinkSubcarrierSpacing

SubcarrierSpacing15kHz

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f45da116-d852-221b-7c68-f328bbe30cfc.htm language=enus -->
## TOPIC 00383: rfmxltedotnet/html/f45da116-d852-221b-7c68-f328bbe30cfc.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f45da116-d852-221b-7c68-f328bbe30cfc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f45da116-d852-221b-7c68-f328bbe30cfc.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetOffsetRbwFilterBandwidth Method

RFmxLteMXSemConfigurationGetOffsetRbwFilterBandwidth Method

Gets the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffsetRbwFilterBandwidth(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffsetRbwFilterBandwidth ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

SemOffsetRbwFilterBandwidth

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f46175f1-17a9-9b0b-d7a1-59ef4f688ff1.htm language=enus -->
## TOPIC 00384: rfmxltedotnet/html/f46175f1-17a9-9b0b-d7a1-59ef4f688ff1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f46175f1-17a9-9b0b-d7a1-59ef4f688ff1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f46175f1-17a9-9b0b-d7a1-59ef4f688ff1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetAveragingEnabled Method

RFmxLteMXModAccConfigurationGetAveragingEnabled Method

Gets whether to enable averaging for the ModAcc measurement.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAveragingEnabled(
	string selectorString,
	out RFmxLteMXModAccAveragingEnabled value
)
```

```text
Public Function GetAveragingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccAveragingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccAveragingEnabledUpon return, contains whether to enable averaging for the ModAcc measurement.

###### Return Value

Int32

##### Remarks

ModAccAveragingEnabled

False

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f4722a96-ac8e-6df3-a1df-7463e08a6d8d.htm language=enus -->
## TOPIC 00385: rfmxltedotnet/html/f4722a96-ac8e-6df3-a1df-7463e08a6d8d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f4722a96-ac8e-6df3-a1df-7463e08a6d8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f4722a96-ac8e-6df3-a1df-7463e08a6d8d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXTxp Methods

RFmxLteMXTxp Methods

The [RFmxLteMXTxp](3793912c-7b60-55bb-130f-60b983c112f9.htm) type exposes the following members.

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

RFmxLteMXTxp Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f47d95a7-6067-a669-c3c4-cbe671a8b9ed.htm language=enus -->
## TOPIC 00386: rfmxltedotnet/html/f47d95a7-6067-a669-c3c4-cbe671a8b9ed.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f47d95a7-6067-a669-c3c4-cbe671a8b9ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f47d95a7-6067-a669-c3c4-cbe671a8b9ed.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetUplinkGroupHoppingEnabled Method

RFmxLteMXComponentCarrierGetUplinkGroupHoppingEnabled Method

3GPP TS 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetUplinkGroupHoppingEnabled(
	string selectorString,
	out RFmxLteMXUplinkGroupHoppingEnabled value
)
```

```text
Public Function GetUplinkGroupHoppingEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXUplinkGroupHoppingEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXUplinkGroupHoppingEnabled Upon return, contains whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification.

###### Return Value

Int32

##### Remarks

UplinkGroupHoppingEnabled

False

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f4828b2f-98de-8703-70bd-7cefba8f9a09.htm language=enus -->
## TOPIC 00387: rfmxltedotnet/html/f4828b2f-98de-8703-70bd-7cefba8f9a09.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f4828b2f-98de-8703-70bd-7cefba8f9a09.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f4828b2f-98de-8703-70bd-7cefba8f9a09.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccIQTimingSkewCorrectionEnabled Enumeration

RFmxLteMXModAccIQTimingSkewCorrectionEnabled Enumeration

Specifies whether to enable IQ timing skew correction. The default value is False.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccIQTimingSkewCorrectionEnabled
```

```text
Public Enumeration RFmxLteMXModAccIQTimingSkewCorrectionEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | IQ timing skew correction is disabled. |
|  | True | 1 | IQ timing skew correction is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f4e75c28-6c4d-b9bc-2fcd-9132aa9598c6.htm language=enus -->
## TOPIC 00388: rfmxltedotnet/html/f4e75c28-6c4d-b9bc-2fcd-9132aa9598c6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f4e75c28-6c4d-b9bc-2fcd-9132aa9598c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f4e75c28-6c4d-b9bc-2fcd-9132aa9598c6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXObwConfiguration.SetRbwFilterBandwidth Method

RFmxLteMXObwConfigurationSetRbwFilterBandwidth Method

SetRbwFilterAutoBandwidth(String, RFmxLteMXObwRbwAutoBandwidth)

False

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDouble Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(String, RFmxLteMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

ObwRbwFilterBandwidth

##### See Also

###### Reference

RFmxLteMXObwConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f528de5c-ec25-2b64-21f4-4b4027abb5b4.htm language=enus -->
## TOPIC 00389: rfmxltedotnet/html/f528de5c-ec25-2b64-21f4-4b4027abb5b4.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f528de5c-ec25-2b64-21f4-4b4027abb5b4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f528de5c-ec25-2b64-21f4-4b4027abb5b4.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetLowerOffsetMargin Method

RFmxLteMXSemResultsGetLowerOffsetMargin Method

3GPP TS 36.521

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemString Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

SemResultsLowerOffsetMargin

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f545ad0c-0a8a-0e42-ee2e-142158f5703d.htm language=enus -->
## TOPIC 00390: rfmxltedotnet/html/f545ad0c-0a8a-0e42-ee2e-142158f5703d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f545ad0c-0a8a-0e42-ee2e-142158f5703d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f545ad0c-0a8a-0e42-ee2e-142158f5703d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPhichResource Method

RFmxLteMXComponentCarrierSetPhichResource Method

3GPP 36.211

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPhichResource(
	string selectorString,
	RFmxLteMXDownlinkUserDefinedPhichResource value
)
```

```text
Public Function SetPhichResource ( 
	selectorString As String,
	value As RFmxLteMXDownlinkUserDefinedPhichResource
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the carrier number, subblock number and subframe number. Example: "carrier0" or "subblock0" or "subframe0" or "subblock0/carrier0/subframe0". You can use the BuildSubframeString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXDownlinkUserDefinedPhichResourceSpecifies the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This method is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH.

###### Return Value

Int32

##### Remarks

PhichResource

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f546465b-2a1a-2abe-2789-6ee31d072517.htm language=enus -->
## TOPIC 00391: rfmxltedotnet/html/f546465b-2a1a-2abe-2789-6ee31d072517.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f546465b-2a1a-2abe-2789-6ee31d072517.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f546465b-2a1a-2abe-2789-6ee31d072517.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.ConfigureAveraging Method

RFmxLteMXAcpConfigurationConfigureAveraging Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureAveraging(
	string selectorString,
	RFmxLteMXAcpAveragingEnabled averagingEnabled,
	int averagingCount,
	RFmxLteMXAcpAveragingType averagingType
)
```

```text
Public Function ConfigureAveraging ( 
	selectorString As String,
	averagingEnabled As RFmxLteMXAcpAveragingEnabled,
	averagingCount As Integer,
	averagingType As RFmxLteMXAcpAveragingType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **averagingEnabled**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpAveragingEnabledSpecifies whether to enable averaging for the measurement.
- **averagingCount**
  - Type: SystemInt32 Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True.
- **averagingType**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcpAveragingTypeSpecifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f5666b18-b2c9-7b65-c701-477d57aa149a.htm language=enus -->
## TOPIC 00392: rfmxltedotnet/html/f5666b18-b2c9-7b65-c701-477d57aa149a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f5666b18-b2c9-7b65-c701-477d57aa149a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f5666b18-b2c9-7b65-c701-477d57aa149a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPdsch16QamConstellation Method

RFmxLteMXModAccResultsFetchPdsch16QamConstellation Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPdsch16QamConstellation(
	string selectorString,
	double timeout,
	ref ComplexSingle[] qam16Constellation
)
```

```text
Public Function FetchPdsch16QamConstellation ( 
	selectorString As String,
	timeout As Double,
	ByRef qam16Constellation As ComplexSingle()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **qam16Constellation**
  - Type: NationalInstrumentsComplexSingle Upon return, contains the 16 QAM constellation trace.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f58d9789-2244-0710-52d0-0d7783f144ee.htm language=enus -->
## TOPIC 00393: rfmxltedotnet/html/f58d9789-2244-0710-52d0-0d7783f144ee.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f58d9789-2244-0710-52d0-0d7783f144ee.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f58d9789-2244-0710-52d0-0d7783f144ee.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchSynchronizationSignalEvmArray Method

RFmxLteMXModAccResultsFetchSynchronizationSignalEvmArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSynchronizationSignalEvmArray(
	string selectorString,
	double timeout,
	ref double[] meanRmsPssEvm,
	ref double[] meanRmsSssEvm
)
```

```text
Public Function FetchSynchronizationSignalEvmArray ( 
	selectorString As String,
	timeout As Double,
	ByRef meanRmsPssEvm As Double(),
	ByRef meanRmsSssEvm As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsPssEvm**
  - Type: SystemDouble Upon return, contains the array of mean values of RMS EVMs calculated on PSS channel over the slots specified by the SetMeasurementLength(String, Int32) method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.
- **meanRmsSssEvm**
  - Type: SystemDouble Upon return, contains the array of mean values of RMS EVMs calculated on SSS channel over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f5b7b9d9-f50e-a032-8485-43d6b1d46a79.htm language=enus -->
## TOPIC 00394: rfmxltedotnet/html/f5b7b9d9-f50e-a032-8485-43d6b1d46a79.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f5b7b9d9-f50e-a032-8485-43d6b1d46a79.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f5b7b9d9-f50e-a032-8485-43d6b1d46a79.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetAutoControlChannelPowerDetectionEnabled Method

RFmxLteMXComponentCarrierSetAutoControlChannelPowerDetectionEnabled Method

Sets whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAutoControlChannelPowerDetectionEnabled(
	string selectorString,
	RFmxLteMXAutoControlChannelPowerDetectionEnabled value
)
```

```text
Public Function SetAutoControlChannelPowerDetectionEnabled ( 
	selectorString As String,
	value As RFmxLteMXAutoControlChannelPowerDetectionEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAutoControlChannelPowerDetectionEnabledSpecifies whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported.

###### Return Value

Int32

##### Remarks

AutoControlChannelPowerDetectionEnabled

True

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f5c7d592-4796-d48a-5535-811beae55228.htm language=enus -->
## TOPIC 00395: rfmxltedotnet/html/f5c7d592-4796-d48a-5535-811beae55228.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f5c7d592-4796-d48a-5535-811beae55228.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f5c7d592-4796-d48a-5535-811beae55228.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpNoiseCalibrationAveragingAuto Enumeration

RFmxLteMXAcpNoiseCalibrationAveragingAuto Enumeration

Specifies whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXAcpNoiseCalibrationAveragingAuto
```

```text
Public Enumeration RFmxLteMXAcpNoiseCalibrationAveragingAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | The RFmx driver uses the averages that you set for SetNoiseCalibrationAveragingCount(String, Int32) method. |
|  | True | 1 | The RFmx driver uses the following averaging counts: |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f648f2e3-8e84-c437-e83d-80bd89f9909a.htm language=enus -->
## TOPIC 00396: rfmxltedotnet/html/f648f2e3-8e84-c437-e83d-80bd89f9909a.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f648f2e3-8e84-c437-e83d-80bd89f9909a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f648f2e3-8e84-c437-e83d-80bd89f9909a.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPhichDuration Method

RFmxLteMXComponentCarrierGetPhichDuration Method

Gets the physical hybrid-ARQ indicator channel (PHICH) duration.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPhichDuration(
	string selectorString,
	out RFmxLteMXDownlinkUserDefinedPhichDuration value
)
```

```text
Public Function GetPhichDuration ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXDownlinkUserDefinedPhichDuration
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the carrier number, subblock number and subframe number. Example: "carrier0" or "subblock0" or "subframe0" or "subblock0/carrier0/subframe0". You can use the BuildSubframeString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXDownlinkUserDefinedPhichDurationUpon return, contains the physical hybrid-ARQ indicator channel (PHICH) duration.

###### Return Value

Int32

##### Remarks

PhichDuration

Normal

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f68b2fb8-98b6-1837-470d-d8ec629cbbaf.htm language=enus -->
## TOPIC 00397: rfmxltedotnet/html/f68b2fb8-98b6-1837-470d-d8ec629cbbaf.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f68b2fb8-98b6-1837-470d-d8ec629cbbaf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f68b2fb8-98b6-1837-470d-d8ec629cbbaf.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPuschNumberOfResourceBlockClusters Method

RFmxLteMXComponentCarrierSetPuschNumberOfResourceBlockClusters Method

3GPP TS 36.213

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschNumberOfResourceBlockClusters(
	string selectorString,
	int value
)
```

```text
Public Function SetPuschNumberOfResourceBlockClusters ( 
	selectorString As String,
	value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32 Specifies the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH).Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

PuschNumberOfResourceBlockClusters

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f6e23e25-4b1b-f2b6-1170-09d3879bf4f1.htm language=enus -->
## TOPIC 00398: rfmxltedotnet/html/f6e23e25-4b1b-f2b6-1170-09d3879bf4f1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f6e23e25-4b1b-f2b6-1170-09d3879bf4f1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f6e23e25-4b1b-f2b6-1170-09d3879bf4f1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetWarning Method

RFmxLteMXGetWarning Method

Gets the latest warning code and description.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetWarning(
	out int warningCode,
	out string warningDescription
)
```

```text
Public Function GetWarning ( 
	<OutAttribute> ByRef warningCode As Integer,
	<OutAttribute> ByRef warningDescription As String
) As Integer
```

###### Parameters

- **warningCode**
  - Type: SystemInt32Upon return, contains the latest warning code.
- **warningDescription**
  - Type: SystemStringUpon return, contains the latest warning description.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f760532a-aaac-4cb3-4e01-02655b3c60a2.htm language=enus -->
## TOPIC 00399: rfmxltedotnet/html/f760532a-aaac-4cb3-4e01-02655b3c60a2.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f760532a-aaac-4cb3-4e01-02655b3c60a2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f760532a-aaac-4cb3-4e01-02655b3c60a2.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.SetEvmWithExclusionPeriodEnabled Method

RFmxLteMXModAccConfigurationSetEvmWithExclusionPeriodEnabled Method

3GPP TS 36.521-1

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetEvmWithExclusionPeriodEnabled(
	string selectorString,
	RFmxLteMXModAccEvmWithExclusionPeriodEnabled value
)
```

```text
Public Function SetEvmWithExclusionPeriodEnabled ( 
	selectorString As String,
	value As RFmxLteMXModAccEvmWithExclusionPeriodEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccEvmWithExclusionPeriodEnabled Specifies whether to exclude some portion of the slots when calculating the EVM. This method is applicable only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP TS 36.521-1 specification for more information about exclusion.

###### Return Value

Int32

##### Remarks

ModAccEvmWithExclusionPeriodEnabled

False

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f7baaf0c-e4d4-82d0-93b2-1845b643ccb0.htm language=enus -->
## TOPIC 00400: rfmxltedotnet/html/f7baaf0c-e4d4-82d0-93b2-1845b643ccb0.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f7baaf0c-e4d4-82d0-93b2-1845b643ccb0.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f7baaf0c-e4d4-82d0-93b2-1845b643ccb0.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemComponentCarrierConfiguration.ConfigureMaximumOutputPower Method

RFmxLteMXSemComponentCarrierConfigurationConfigureMaximumOutputPower Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMaximumOutputPower(
	string selectorString,
	double componentCarrierMaximumOutputPower
)
```

```text
Public Function ConfigureMaximumOutputPower ( 
	selectorString As String,
	componentCarrierMaximumOutputPower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **componentCarrierMaximumOutputPower**
  - Type: SystemDouble Specifies the maximum output power per carrier, which is used only to choose the limit table for Medium Range Base Station. This value is expressed in dBm. Refer to the section 6.6.3 of the 3GPP 36.141 specification for more details.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemComponentCarrierConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f83936ac-57c3-a328-ca7e-2e285fab19d8.htm language=enus -->
## TOPIC 00401: rfmxltedotnet/html/f83936ac-57c3-a328-ca7e-2e285fab19d8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f83936ac-57c3-a328-ca7e-2e285fab19d8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f83936ac-57c3-a328-ca7e-2e285fab19d8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPuschModulationType Method

RFmxLteMXComponentCarrierSetPuschModulationType Method

Sets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschModulationType(
	string selectorString,
	RFmxLteMXPuschModulationType value
)
```

```text
Public Function SetPuschModulationType ( 
	selectorString As String,
	value As RFmxLteMXPuschModulationType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXPuschModulationTypeSpecifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

###### Return Value

Int32

##### Remarks

PuschModulationType

ModulationTypeQpsk

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f8b4a5b4-3a07-c119-fc5e-a44d48537fa6.htm language=enus -->
## TOPIC 00402: rfmxltedotnet/html/f8b4a5b4-3a07-c119-fc5e-a44d48537fa6.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f8b4a5b4-3a07-c119-fc5e-a44d48537fa6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f8b4a5b4-3a07-c119-fc5e-a44d48537fa6.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.ConfigureNumberOfOffsets Method

RFmxLteMXSemConfigurationConfigureNumberOfOffsets Method

Namespace:

NationalInstruments.RFmx.LteMX

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

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **numberOfOffsets**
  - Type: SystemInt32Specifies the number of SEM offset segments.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f8b882c7-232f-4d06-c354-fc82cf3b8962.htm language=enus -->
## TOPIC 00403: rfmxltedotnet/html/f8b882c7-232f-4d06-c354-fc82cf3b8962.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f8b882c7-232f-4d06-c354-fc82cf3b8962.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f8b882c7-232f-4d06-c354-fc82cf3b8962.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXAcpConfiguration.GetMeasurementEnabled Method

RFmxLteMXAcpConfigurationGetMeasurementEnabled Method

Gets whether to enable the ACP measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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

RFmxLteMXAcpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/f9f7c072-f152-81c1-8069-d8de6a64fb30.htm language=enus -->
## TOPIC 00404: rfmxltedotnet/html/f9f7c072-f152-81c1-8069-d8de6a64fb30.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/f9f7c072-f152-81c1-8069-d8de6a64fb30.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/f9f7c072-f152-81c1-8069-d8de6a64fb30.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.ConfigureSoftwareEdgeTrigger Method

RFmxLteMXConfigureSoftwareEdgeTrigger Method

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemDoubleSpecifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre trigger samples. If the delay is positive, the measurement acquires post-trigger samples.
- **enableTrigger**
  - Type: SystemBooleanSpecifies whether to enable the trigger.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fa484b62-e6f5-e065-ac0d-09809b2f7bf1.htm language=enus -->
## TOPIC 00405: rfmxltedotnet/html/fa484b62-e6f5-e065-ac0d-09809b2f7bf1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fa484b62-e6f5-e065-ac0d-09809b2f7bf1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fa484b62-e6f5-e065-ac0d-09809b2f7bf1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.BuildResultString Method

RFmxLteMXBuildResultString Method

Creates selector string for use with configuration or fetch.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildResultString(
	string resultName
)
```

```text
Public Shared Function BuildResultString ( 
	resultName As String
) As String
```

###### Parameters

- **resultName**
  - Type: SystemStringSpecifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1".

###### Return Value

String

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fa7b8784-df24-ad91-1217-9d221e5f0247.htm language=enus -->
## TOPIC 00406: rfmxltedotnet/html/fa7b8784-df24-ad91-1217-9d221e5f0247.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fa7b8784-df24-ad91-1217-9d221e5f0247.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fa7b8784-df24-ad91-1217-9d221e5f0247.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetIQPowerEdgeTriggerSource Method

RFmxLteMXGetIQPowerEdgeTriggerSource Method

SetTriggerType(String, RFmxLteMXTriggerType)

IQPowerEdge

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemString Upon return, contains the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(String, RFmxLteMXTriggerType) method to IQPowerEdge.

###### Return Value

Int32

##### Remarks

IQPowerEdgeTriggerSource

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fa990eb3-a928-ca7b-6c16-f0d60c483365.htm language=enus -->
## TOPIC 00407: rfmxltedotnet/html/fa990eb3-a928-ca7b-6c16-f0d60c483365.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fa990eb3-a928-ca7b-6c16-f0d60c483365.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fa990eb3-a928-ca7b-6c16-f0d60c483365.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetAcquisitionBandwidthOptimizationEnabled Method

RFmxLteMXGetAcquisitionBandwidthOptimizationEnabled Method

Gets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAcquisitionBandwidthOptimizationEnabled(
	string selectorString,
	out RFmxLteMXAcquisitionBandwidthOptimizationEnabled value
)
```

```text
Public Function GetAcquisitionBandwidthOptimizationEnabled ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXAcquisitionBandwidthOptimizationEnabled
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXAcquisitionBandwidthOptimizationEnabledUpon return, contains whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

###### Return Value

Int32

##### Remarks

AcquisitionBandwidthOptimizationEnabled

True

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fab0a403-82a4-f9de-149e-63d06cd2da69.htm language=enus -->
## TOPIC 00408: rfmxltedotnet/html/fab0a403-82a4-f9de-149e-63d06cd2da69.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fab0a403-82a4-f9de-149e-63d06cd2da69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fab0a403-82a4-f9de-149e-63d06cd2da69.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetMeanIQTimingSkew Method

RFmxLteMXModAccResultsGetMeanIQTimingSkew Method

Returns the estimated IQ timing skew averaged over measured length. IQ timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeanIQTimingSkew(
	string selectorString,
	out double value
)
```

```text
Public Function GetMeanIQTimingSkew ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the estimated IQ timing skew averaged over measured length.

###### Return Value

Int32

##### Remarks

ModAccResultsMeanIQTimingSkew

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fac29c71-4120-8e33-bb31-af6ba0cb2123.htm language=enus -->
## TOPIC 00409: rfmxltedotnet/html/fac29c71-4120-8e33-bb31-af6ba0cb2123.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fac29c71-4120-8e33-bb31-af6ba0cb2123.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fac29c71-4120-8e33-bb31-af6ba0cb2123.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSlotPowerConfiguration.ConfigureMeasurementInterval Method

RFmxLteMXSlotPowerConfigurationConfigureMeasurementInterval Method

measurementOffset

measurementLength

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureMeasurementInterval(
	string selectorString,
	int measurementOffset,
	int measurementLength
)
```

```text
Public Function ConfigureMeasurementInterval ( 
	selectorString As String,
	measurementOffset As Integer,
	measurementLength As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **measurementOffset**
  - Type: SystemInt32Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframes.
- **measurementLength**
  - Type: SystemInt32Specifies the number of subframes to be measured. This value is expressed in subframes.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXSlotPowerConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fae3b511-c95a-d574-c5a5-4053960e4de1.htm language=enus -->
## TOPIC 00410: rfmxltedotnet/html/fae3b511-c95a-d574-c5a5-4053960e4de1.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fae3b511-c95a-d574-c5a5-4053960e4de1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fae3b511-c95a-d574-c5a5-4053960e4de1.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.GetReferenceLevelHeadroom Method

RFmxLteMXGetReferenceLevelHeadroom Method

SetReferenceLevel(String, Double)

Default values

Supported devices: PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetReferenceLevelHeadroom(
	string selectorString,
	out double value
)
```

```text
Public Function GetReferenceLevelHeadroom ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Upon return, contains the margin RFmx driver adds to the SetReferenceLevel(String, Double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

###### Return Value

Int32

##### Remarks

ReferenceLevelHeadroom

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fb2807c1-9d9d-7e7d-ad96-9f23073460d5.htm language=enus -->
## TOPIC 00411: rfmxltedotnet/html/fb2807c1-9d9d-7e7d-ad96-9f23073460d5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fb2807c1-9d9d-7e7d-ad96-9f23073460d5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fb2807c1-9d9d-7e7d-ad96-9f23073460d5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetNPuschStartingSlot Method

RFmxLteMXComponentCarrierGetNPuschStartingSlot Method

Gets the starting slot number of the NPUSCH burst.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetNPuschStartingSlot(
	string selectorString,
	out int value
)
```

```text
Public Function GetNPuschStartingSlot ( 
	selectorString As String,
	<OutAttribute> ByRef value As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemInt32Upon return, contains the starting slot number of the NPUSCH burst.

###### Return Value

Int32

##### Remarks

NPuschStartingSlot

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fb4b75db-f1a0-6927-a044-12b7e6052fac.htm language=enus -->
## TOPIC 00412: rfmxltedotnet/html/fb4b75db-f1a0-6927-a044-12b7e6052fac.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fb4b75db-f1a0-6927-a044-12b7e6052fac.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fb4b75db-f1a0-6927-a044-12b7e6052fac.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemResults.GetMeasurementStatus Method

RFmxLteMXSemResultsGetMeasurementStatus Method

Gets the overall measurement status based on the standard mask type that you configure in the SEM Standard Mask Type method.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMeasurementStatus(
	string selectorString,
	out RFmxLteMXSemMeasurementStatus value
)
```

```text
Public Function GetMeasurementStatus ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSemMeasurementStatus
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name.Example: """result::r1" You can use the BuildResultString(String) method to build the selectorString.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemMeasurementStatusUpon return, contains the overall measurement status based on the standard mask type that you configure in the SEM Standard Mask Type method.

###### Return Value

Int32

##### Remarks

SemResultsMeasurementStatus

##### See Also

###### Reference

RFmxLteMXSemResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fb8612a2-7c23-2507-6de4-2af6b30de80b.htm language=enus -->
## TOPIC 00413: rfmxltedotnet/html/fb8612a2-7c23-2507-6de4-2af6b30de80b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fb8612a2-7c23-2507-6de4-2af6b30de80b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fb8612a2-7c23-2507-6de4-2af6b30de80b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccConfiguration.GetPreFftErrorEstimationInterval Method

RFmxLteMXModAccConfigurationGetPreFftErrorEstimationInterval Method

Gets the interval used for Pre-FFT Error Estimation.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPreFftErrorEstimationInterval(
	string selectorString,
	out RFmxLteMXModAccPreFftErrorEstimationInterval value
)
```

```text
Public Function GetPreFftErrorEstimationInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXModAccPreFftErrorEstimationInterval
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXModAccPreFftErrorEstimationIntervalUpon return, contains the interval used for Pre-FFT Error Estimation.

###### Return Value

Int32

##### Remarks

ModAccPreFftErrorEstimationInterval

MeasurementLength

##### See Also

###### Reference

RFmxLteMXModAccConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fbce3ddf-2818-1dd6-b642-02407e38a6c7.htm language=enus -->
## TOPIC 00414: rfmxltedotnet/html/fbce3ddf-2818-1dd6-b642-02407e38a6c7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fbce3ddf-2818-1dd6-b642-02407e38a6c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fbce3ddf-2818-1dd6-b642-02407e38a6c7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchSrsEvmArray Method

RFmxLteMXModAccResultsFetchSrsEvmArray Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchSrsEvmArray(
	string selectorString,
	double timeout,
	ref double[] meanRmsSrsEvm,
	ref double[] meanSrsPower
)
```

```text
Public Function FetchSrsEvmArray ( 
	selectorString As String,
	timeout As Double,
	ByRef meanRmsSrsEvm As Double(),
	ByRef meanSrsPower As Double()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsSrsEvm**
  - Type: SystemDouble Upon return, contains the array of mean values of RMS EVMs calculated on the SRS symbols over the slots specified by the SetMeasurementLength(String, Int32) method. When you set the SetEvmUnit(String, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB.
- **meanSrsPower**
  - Type: SystemDouble Upon return, contains the array of mean values of power calculated on SRS over the slots specified by the ModAcc Meas Length method. This value is expressed in dB.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fc3c8010-54bf-1bc4-68bb-ad8ff9cc454b.htm language=enus -->
## TOPIC 00415: rfmxltedotnet/html/fc3c8010-54bf-1bc4-68bb-ad8ff9cc454b.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fc3c8010-54bf-1bc4-68bb-ad8ff9cc454b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fc3c8010-54bf-1bc4-68bb-ad8ff9cc454b.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.SetPuschPower Method

RFmxLteMXComponentCarrierSetPuschPower Method

Sets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPuschPower(
	string selectorString,
	double value
)
```

```text
Public Function SetPuschPower ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PuschPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fc7bb02c-4c0f-c4c8-2d45-2b7727148be8.htm language=enus -->
## TOPIC 00416: rfmxltedotnet/html/fc7bb02c-4c0f-c4c8-2d45-2b7727148be8.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fc7bb02c-4c0f-c4c8-2d45-2b7727148be8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fc7bb02c-4c0f-c4c8-2d45-2b7727148be8.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.SetListStepTimerOffset Method

RFmxLteMXSetListStepTimerOffset Method

SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit)

SetDigitalEdgeTriggerSource(String, String)

TimerEvent

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetListStepTimerOffset(
	string selectorString,
	double value
)
```

```text
Public Function SetListStepTimerOffset ( 
	selectorString As String,
	value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDouble Specifies the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(String, RFmxLteMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(String, String) method to TimerEvent.

###### Return Value

Int32

##### Remarks

ListStepTimerOffset

##### See Also

###### Reference

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fc7ea8e6-362f-2588-47f0-1e5c9f1d6595.htm language=enus -->
## TOPIC 00417: rfmxltedotnet/html/fc7ea8e6-362f-2588-47f0-1e5c9f1d6595.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fc7ea8e6-362f-2588-47f0-1e5c9f1d6595.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fc7ea8e6-362f-2588-47f0-1e5c9f1d6595.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchCompositeEvm Method

RFmxLteMXModAccResultsFetchCompositeEvm Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchCompositeEvm(
	string selectorString,
	double timeout,
	out double meanRmsCompositeEvm,
	out double maximumPeakCompositeEvm,
	out double meanFrequencyError,
	out int peakCompositeEvmSymbolIndex,
	out int peakCompositeEvmSubcarrierIndex,
	out int peakCompositeEvmSlotIndex
)
```

```text
Public Function FetchCompositeEvm ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef meanRmsCompositeEvm As Double,
	<OutAttribute> ByRef maximumPeakCompositeEvm As Double,
	<OutAttribute> ByRef meanFrequencyError As Double,
	<OutAttribute> ByRef peakCompositeEvmSymbolIndex As Integer,
	<OutAttribute> ByRef peakCompositeEvmSubcarrierIndex As Integer,
	<OutAttribute> ByRef peakCompositeEvmSlotIndex As Integer
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **meanRmsCompositeEvm**
  - Type: SystemDouble Upon return, contains the mean value of the RMS EVMs calculated on all configured channels over the slots specified by the SetMeasurementLength(String, Int32) method.
- **maximumPeakCompositeEvm**
  - Type: SystemDouble Upon return, contains the symbol index where the ModAcc maximum peak composite EVM occurs.
- **meanFrequencyError**
  - Type: SystemDouble Upon return, contains the estimated carrier frequency offset averaged over the slots specified by the ModAcc Meas Length method.
- **peakCompositeEvmSymbolIndex**
  - Type: SystemInt32 Upon return, contains the symbol index where the ModAcc maximum peak composite EVM occurs.
- **peakCompositeEvmSubcarrierIndex**
  - Type: SystemInt32 Upon return, contains the subcarrier index where the ModAcc maximum peak composite EVM occurs.
- **peakCompositeEvmSlotIndex**
  - Type: SystemInt32 Upon return, contains the slot index where the ModAcc maximum peak composite EVM occurs.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fca113d5-ebfa-1e57-6f75-fe01e57e0840.htm language=enus -->
## TOPIC 00418: rfmxltedotnet/html/fca113d5-ebfa-1e57-6f75-fe01e57e0840.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fca113d5-ebfa-1e57-6f75-fe01e57e0840.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fca113d5-ebfa-1e57-6f75-fe01e57e0840.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.SetMeasurementEnabled Method

RFmxLteMXPvtConfigurationSetMeasurementEnabled Method

Sets whether to enable the power versus time (PVT) measurement.

Namespace:

NationalInstruments.RFmx.LteMX

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
  - Type: SystemBooleanSpecifies whether to enable the power versus time (PVT) measurement.

###### Return Value

Int32

##### Remarks

PvtMeasurementEnabled

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fcce5637-0728-4455-08e5-077f721ac1e9.htm language=enus -->
## TOPIC 00419: rfmxltedotnet/html/fcce5637-0728-4455-08e5-077f721ac1e9.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fcce5637-0728-4455-08e5-077f721ac1e9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fcce5637-0728-4455-08e5-077f721ac1e9.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.GetPsschMeanDataPower Method

RFmxLteMXModAccResultsGetPsschMeanDataPower Method

SetMeasurementLength(String, Int32)

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPsschMeanDataPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetPsschMeanDataPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Upon return, contains the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(String, Int32) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

###### Return Value

Int32

##### Remarks

ModAccResultsPsschMeanDataPower

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fcf986bf-2a0a-23cf-d15d-734abedc198c.htm language=enus -->
## TOPIC 00420: rfmxltedotnet/html/fcf986bf-2a0a-23cf-d15d-734abedc198c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fcf986bf-2a0a-23cf-d15d-734abedc198c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fcf986bf-2a0a-23cf-d15d-734abedc198c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMX.DisableTrigger Method

RFmxLteMXDisableTrigger Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int DisableTrigger(
	string selectorString
)
```

```text
Public Function DisableTrigger ( 
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

RFmxLteMX Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fd9e610b-89c7-4bd9-6717-02f3ccee1332.htm language=enus -->
## TOPIC 00421: rfmxltedotnet/html/fd9e610b-89c7-4bd9-6717-02f3ccee1332.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fd9e610b-89c7-4bd9-6717-02f3ccee1332.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fd9e610b-89c7-4bd9-6717-02f3ccee1332.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXMiConfiguration Enumeration

RFmxLteMXMiConfiguration Enumeration

3GPP TS 36.141

3GPP TS 36.211

SetDuplexScheme(String, RFmxLteMXDuplexScheme)

Tdd

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXMiConfiguration
```

```text
Public Enumeration RFmxLteMXMiConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TestModel | 0 | Mi parameter is set to 1 as specified in section 6.1.2.6 of 3GPP TS 36.141 specification. |
|  | Standard | 1 | Mi parameter is specified by the Table 6.9-1 of 3GPP TS 36.211 specification. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fdc106e6-031a-1141-3894-735b4c92f03e.htm language=enus -->
## TOPIC 00422: rfmxltedotnet/html/fdc106e6-031a-1141-3894-735b4c92f03e.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fdc106e6-031a-1141-3894-735b4c92f03e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fdc106e6-031a-1141-3894-735b4c92f03e.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPuschPower Method

RFmxLteMXComponentCarrierGetPuschPower Method

Gets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPuschPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetPuschPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PuschPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fe16ceb8-8e76-b521-27a1-2c952e33690c.htm language=enus -->
## TOPIC 00423: rfmxltedotnet/html/fe16ceb8-8e76-b521-27a1-2c952e33690c.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fe16ceb8-8e76-b521-27a1-2c952e33690c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fe16ceb8-8e76-b521-27a1-2c952e33690c.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccSymbolClockErrorEstimationEnabled Enumeration

RFmxLteMXModAccSymbolClockErrorEstimationEnabled Enumeration

Specifies whether to estimate symbol clock error.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxLteMXModAccSymbolClockErrorEstimationEnabled
```

```text
Public Enumeration RFmxLteMXModAccSymbolClockErrorEstimationEnabled
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Symbol Clock Error estimation and correction is disabled. |
|  | True | 1 | Symbol Clock Error estimation and correction is enabled. |

##### See Also

###### Reference

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/fe4a9dd1-369f-5ea5-1b82-2c7a6cf519a5.htm language=enus -->
## TOPIC 00424: rfmxltedotnet/html/fe4a9dd1-369f-5ea5-1b82-2c7a6cf519a5.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/fe4a9dd1-369f-5ea5-1b82-2c7a6cf519a5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/fe4a9dd1-369f-5ea5-1b82-2c7a6cf519a5.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXPvtConfiguration.GetOffPowerExclusionBefore Method

RFmxLteMXPvtConfigurationGetOffPowerExclusionBefore Method

Gets the time excluded from the Off region before the burst. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetOffPowerExclusionBefore(
	string selectorString,
	out double value
)
```

```text
Public Function GetOffPowerExclusionBefore ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the time excluded from the Off region before the burst. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

PvtOffPowerExclusionBefore

##### See Also

###### Reference

RFmxLteMXPvtConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/feb0fbb4-1f56-c618-e6c5-625046d9ddec.htm language=enus -->
## TOPIC 00425: rfmxltedotnet/html/feb0fbb4-1f56-c618-e6c5-625046d9ddec.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/feb0fbb4-1f56-c618-e6c5-625046d9ddec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/feb0fbb4-1f56-c618-e6c5-625046d9ddec.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier.GetPbchPower Method

RFmxLteMXComponentCarrierGetPbchPower Method

Gets the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPbchPower(
	string selectorString,
	out double value
)
```

```text
Public Function GetPbchPower ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

PbchPower

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/feec5f61-d670-7698-e616-361a0ff8e3cb.htm language=enus -->
## TOPIC 00426: rfmxltedotnet/html/feec5f61-d670-7698-e616-361a0ff8e3cb.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/feec5f61-d670-7698-e616-361a0ff8e3cb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/feec5f61-d670-7698-e616-361a0ff8e3cb.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpConfiguration.SetIntegrationBandwidthType Method

RFmxLteMXChpConfigurationSetIntegrationBandwidthType Method

Sets the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval.

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int SetIntegrationBandwidthType(
	string selectorString,
	RFmxLteMXChpIntegrationBandwidthType value
)
```

```text
Public Function SetIntegrationBandwidthType ( 
	selectorString As String,
	value As RFmxLteMXChpIntegrationBandwidthType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXChpIntegrationBandwidthTypeSpecifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval.

###### Return Value

Int32

##### Remarks

ChpIntegrationBandwidthType

SignalBandwidth

##### See Also

###### Reference

RFmxLteMXChpConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ff0cb549-28ff-02a4-d28c-99f679819a0d.htm language=enus -->
## TOPIC 00427: rfmxltedotnet/html/ff0cb549-28ff-02a4-d28c-99f679819a0d.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ff0cb549-28ff-02a4-d28c-99f679819a0d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ff0cb549-28ff-02a4-d28c-99f679819a0d.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXChpResults.ComponentCarrier Property

RFmxLteMXChpResultsComponentCarrier Property

RFmxLteMXChpComponentCarrierResults

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public RFmxLteMXChpComponentCarrierResults ComponentCarrier { get; }
```

```text
Public ReadOnly Property ComponentCarrier As RFmxLteMXChpComponentCarrierResults
	Get
```

###### Property Value

RFmxLteMXChpComponentCarrierResults

##### See Also

###### Reference

RFmxLteMXChpResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ff2b3af4-9c69-1789-1783-3257c89c8b61.htm language=enus -->
## TOPIC 00428: rfmxltedotnet/html/ff2b3af4-9c69-1789-1783-3257c89c8b61.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ff2b3af4-9c69-1789-1783-3257c89c8b61.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ff2b3af4-9c69-1789-1783-3257c89c8b61.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXComponentCarrier Methods

RFmxLteMXComponentCarrier Methods

The [RFmxLteMXComponentCarrier](b0fa07ca-d58d-688c-ef92-590ff7f81b9d.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures the componentCarrierBandwidth, componentCarrierFrequency, and cellID of the component carrier. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureArray | Configures an array of bandwidths, carrier offset frequencies, and cell IDs of component carriers. Use "subblock(n)" as the selector string to configure this method. |
|  | ConfigureAutoNPuschChannelDetectionEnabled | Configures whether the values of the SetNPuschToneOffset(String, Int32), SetNPuschNumberOfTones(String, Int32), and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) methods for the NPUSCH channel are auto-detected by the measurement or specified by you. |
|  | ConfigureAutoResourceBlockDetectionEnabled | Configures whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) methods are automatically detected by the measurement or if you specify the values of these methods. The measurement ignores this method, when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Downlink. |
|  | ConfigureCellSpecificRatio | Configures the cellspecificratio parameter. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkAutoCellIDDetectionEnabled | Configures whether the cell ID is configured by the user or auto-detected by the measurement. |
|  | ConfigureDownlinkAutoChannelDetection | Configures whether the values of physical downlink shared channel (PDSCH) parameters, control channel signal powers, and physical control format indicator channel (PCFICH) CFI are configured by a user or auto-detected by the measurement. The measurement ignores this method, when you set the SetLinkDirection(String, RFmxLteMXLinkDirection) method to Uplink. |
|  | ConfigureDownlinkChannelConfigurationMode | Configures the downlink channel configuration mode. |
|  | ConfigureDownlinkNumberOfSubframes | Configures the number of unique subframes that are transmitted from the DUT. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkSynchronizationSignal | Configures the synchronization signal power relative to the cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkTestModel | Configures the E-UTRA Test Model type. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureDownlinkTestModelArray | Configures an array of the E-UTRA Test Model type for each component carrier within the subblock. |
|  | ConfigureEmtcAnalysisEnabled | Configures whether the component carrier contains an enhanced machine type communications (Cat-M1 or Cat-M2) transmission. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNBIoTComponentCarrier | Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschDmrs | Configures the base sequence mode, base sequence index, cyclic shift, delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS and specifies whether group hopping is enabled. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschFormat | Configures the format of the narrowband physical uplink shared channel (NPUSCH). Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschStartingSlot | Configures the starting slot of the NPUSCH burst. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNPuschTones | Configures the values of toneOffset, numberOfTones, and modulationType parameters for NPUSCH channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigureNumberOfPdschChannels | Configures the number of different physical downlink shared channel (PDSCH) allocations in a subframe. Use "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)" as the selector string to configure this method. |
|  | ConfigureNumberOfPuschResourceBlockClusters | Configures the number of clusters of resource allocations. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePbch | Configures the power of physical broadcast channel (PBCH) power relative to the cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePcfich | Configures the CFI and power parameters of the physical control format indicator channel (PCFICH). Use "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)" as the selector string to configure this method. |
|  | ConfigurePdcch | Configures the physical downlink control channel (PDCCH) power relative to the cell-specific reference signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePdsch | Configures the codeword0 modulation type, resource block, and relative power of a physical downlink shared channel (PDSCH) allocation. Use "PDSCH(m)" or "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)/PDSCH(m)" as the selector string to configure this method. |
|  | ConfigurePhich | Configures the resource, duration, and power parameters of the physical hybrid-ARQ indicator channel (PHICH). Use "subframe(l)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/subframe(l)" as the selector string to configure this method. |
|  | ConfigurePsschModulationType | Configures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePsschResourceBlocks | Configures the start and number of resource blocks allocated for the physical sidelink shared channel (PSSCH) allocation. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePuschModulationType | Configures the modulation scheme used in the physical uplink shared channel (PUSCH) channel of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. |
|  | ConfigurePuschResourceBlocks | Configures the start and number of resource blocks allocated for the physical uplink shared channel (PUSCH) cluster. Use "cluster(l)" or "carrier(k)" or "subblock(n)/carrier(k)/cluster(l)" as the selector string to configure this result. |
|  | ConfigureSpacing | Configures the componentCarrierSpacingType and componentCarrieratCenterFrequency parameters, which help to set the spacing between adjacent component carriers within a subblock. Use "subblock(n)" as the selector string to configure this method. Refer to the Channel Spacing and Carrier Frequency Offset Definition and Reference Frequency topics for more information about carrier spacing. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetAutoControlChannelPowerDetectionEnabled | Gets whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported. |
|  | GetAutoNPuschChannelDetectionEnabled | Gets whether the values of the SetNPuschToneOffset(String, Int32), NPUSCH Number of Tones, and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) properties are auto-detected by the measurement or specified by you. |
|  | GetAutoPcfichCfiDetectionEnabled | Gets whether the value of SetPcfichCfi(String, Int32) method is auto-detected by the measurement or user-specified. |
|  | GetAutoPdschChannelDetectionEnabled | Gets whether the values of the SetPdschResourceBlockAllocation(String, String) method, the corresponding PDSCH CW0 Modulation Type method, and the PDSCH Power method are auto-detected by the measurement or user-specified. |
|  | GetAutoResourceBlockDetectionEnabled | Gets whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) properties are auto-detected by the measurement or if you specify the values of these properties. |
|  | GetBandwidth | Gets the channel bandwidth of the signal being measured. This value is expressed in Hz. |
|  | GetCellId | Gets a physical layer cell identity. |
|  | GetComponentCarrierAtCenterFrequency | Gets the index of the component carrier having its center at the user-configured center frequency. RFmxLTE uses this method along with ComponentCarrierSpacingType method to calculate the value of the SetFrequency(String, Double). |
|  | GetCyclicPrefixMode | Gets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
|  | GetDmrsOccEnabled | Gets whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases. |
|  | GetDownlinkAutoCellIDDetectionEnabled | Gets whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using GetDownlinkDetectedCellID(String, Int32) method. |
|  | GetDownlinkChannelConfigurationMode | Gets the channel configuration mode. |
|  | GetDownlinkNumberOfSubframes | Gets the number of unique subframes transmitted by the DUT. If you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel, this method will be set to 10 for FDD and 20 for TDD by default. |
|  | GetDownlinkTestModel | Gets the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. |
|  | GetDownlinkUserDefinedCellSpecificRatio | Gets the ratio Rhob/Rhoa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 specification. This method determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. |
|  | GetEmtcAnalysisEnabled | Gets whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. |
|  | GetFrequency | Gets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. This method is applicable only if you set the ComponentCarrierSpacingType method to User. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLaaDownlinkNumberOfEndingSymbols | Gets the number of ending symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the 3GPP 36.211 specification for more information regarding LAA downlink number of ending symbols. |
|  | GetLaaDownlinkStartingSymbol | Gets the starting symbol number in the first subframe of an LAA downlink burst. Refer to section 13A of the 3GPP 36.213 specification for more information regarding LAA downlink starting symbol. |
|  | GetLaaNumberOfSubframes | Gets the number of subframes in an LAA burst including the starting subframe. |
|  | GetLaaStartingSubframe | Gets the starting subframe of an LAA burst. |
|  | GetLaaUplinkEndingSymbol | Gets the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP 36.212 specification for more information regarding LAA uplink ending symbol. |
|  | GetLaaUplinkStartPosition | Gets the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the 3GPP 36.211 specification for more information regarding LAA uplink start position. |
|  | GetNBIoTUplinkSubcarrierSpacing | Gets the subcarrier bandwidth of an NB-IoT signal. This method specifies the spacing between adjacent subcarriers. |
|  | GetNCellId | Gets the narrowband physical layer cell identity. |
|  | GetNPuschDmrsBaseSequenceIndex | Gets the base sequence index of the Narrowband Physical Uplink Shared Channel (NPUSCH) DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |
|  | GetNPuschDmrsBaseSequenceMode | Gets whether the SetNPuschDmrsBaseSequenceIndex(String, Int32) method is computed by the measurement or specified by you. |
|  | GetNPuschDmrsCyclicShift | Gets the cyclic shift of the narrowband physical uplink shared channel (NPUSCH) DMRS as defined in Table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. |
|  | GetNPuschDmrsDeltaSequenceShift | Gets the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This method is valid when you set the SetNPuschDmrsGroupHoppingEnabled(String, RFmxLteMXNPuschDmrsGroupHoppingEnabled) method to True. |
|  | GetNPuschDmrsGroupHoppingEnabled | Gets whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the SetNPuschFormat(String, Int32) is 1. |
|  | GetNPuschFormat | Gets the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information. |
|  | GetNPuschModulationType | Gets the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). |
|  | GetNPuschNumberOfTones | Gets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | GetNPuschStartingSlot | Gets the starting slot number of the NPUSCH burst. |
|  | GetNPuschToneOffset | Gets the location of the starting subcarrier (tone) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | GetNumberOfComponentCarriers | Gets the number of component carriers configured within a subblock. |
|  | GetNumberOfPdschChannels | Gets the number of physical downlink shared channel (PDSCH) allocations in a subframe. |
|  | GetPbchPower | Gets the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPcfichCfi | Gets the control format indicator (CFI) carried by physical control format indicator channel (PCFICH). CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. |
|  | GetPcfichPower | Gets the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPdcchPower | Gets the power of physical downlink control channel (PDCCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPdschCW0ModulationType | Gets the modulation type of codeword0 PDSCH allocation. |
|  | GetPdschPower | Gets the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the SetDownlinkUserDefinedCellSpecificRatio(String, RFmxLteMXDownlinkUserDefinedRatio) method to calculate the Rb. Refer to section 3.3 of the 3GPP 36.521 specification for more information about Ra. |
|  | GetPdschResourceBlockAllocation | Gets the resource blocks of the physical downlink shared channel (PDSCH) allocation. |
|  | GetPhichDuration | Gets the physical hybrid-ARQ indicator channel (PHICH) duration. |
|  | GetPhichPower | Gets the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. |
|  | GetPhichResource | Gets the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This method is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. |
|  | GetPsschModulationType | Gets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. |
|  | GetPsschNumberOfResourceBlocks | Gets the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation. |
|  | GetPsschPower | Gets the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB. |
|  | GetPsschResourceBlockOffset | Gets the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. |
|  | GetPssPower | Gets the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetPuschCyclicShiftField | Gets the cyclic shift field in uplink-related DCI format. When the SetDmrsOccEnabled(String, RFmxLteMXDmrsOccEnabled) method is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with SetTransmitAntennaToAnalyze(String, Int32). |
|  | GetPuschDeltaSequenceShift | Gets the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift. |
|  | GetPuschModulationType | Gets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | GetPuschNDmrs1 | Gets the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification. |
|  | GetPuschNDmrs2 | Gets the n_DMRS_2 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a slot. The valid values for this method are, as defined in table 5.5.2.1.1-1 of the 3GPP TS 36.211 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | GetPuschNumberOfResourceBlockClusters | Gets the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH).Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | GetPuschNumberOfResourceBlocks | Gets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. |
|  | GetPuschPower | Gets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | GetPuschResourceBlockOffset | Gets the starting resource block number of a physical uplink shared channel (PUSCH) cluster. |
|  | GetSpacingType | Gets the spacing between two adjacent component carriers within a subblock. |
|  | GetSrsbHop | Gets the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(String, Int32) method. |
|  | GetSrsBSrs | Gets the UE specific SRS bandwidth configuration BSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsCSrs | Gets the cell-specific SRS bandwidth configuration CSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsEnabled | Gets whether the LTE signal getting measured contains SRS transmission. |
|  | GetSrsISrs | Gets the SRS configuration index ISRS. It is used to determine the SRS periodicity and SRS subframe offset. It is a UE specific method which defines whether the SRS is transmitted in the subframe reserved for SRS by SRS subframe configuration. Refer to 3GPP 36.213 specification for more details. |
|  | GetSrskTC | Gets the transmission comb index. If you set this method to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this method to 1, SRS is transmitted on the odd subcarriers in the allocated region. |
|  | GetSrsMaximumUpPtsEnabled | Gets SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsnRrc | Gets the SRS frequency domain position nRRC. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsnSrsCS | Gets the cyclic shift value nSRSCS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | GetSrsPower | Gets the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. |
|  | GetSrsSubframe1NRA | Gets the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD. |
|  | GetSrsSubframe6NRA | Gets the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. |
|  | GetSrsSubframeConfiguration | Gets the SRS subframe configuration specified in the Table 5.5.3.3-1 of 3GPP 36.211 specification. It is a cell-specific method. This method defines the subframes that are reserved for SRS transmission in a given cell. |
|  | GetSssPower | Gets the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetUplinkGroupHoppingEnabled | Gets whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. |
|  | GetUplinkSequenceHoppingEnabled | Gets whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. This method is only applicable only when you set the SetPuschNumberOfResourceBlocks(String, Int32) method to a value greater than 5. |
|  | SetAutoControlChannelPowerDetectionEnabled | Sets whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power method is not supported. |
|  | SetAutoNPuschChannelDetectionEnabled | Sets whether the values of the SetNPuschToneOffset(String, Int32), NPUSCH Number of Tones, and SetNPuschModulationType(String, RFmxLteMXNPuschModulationType) properties are auto-detected by the measurement or specified by you. |
|  | SetAutoPcfichCfiDetectionEnabled | Sets whether the value of SetPcfichCfi(String, Int32) method is auto-detected by the measurement or user-specified. |
|  | SetAutoPdschChannelDetectionEnabled | Sets whether the values of the SetPdschResourceBlockAllocation(String, String) method, the corresponding PDSCH CW0 Modulation Type method, and the PDSCH Power method are auto-detected by the measurement or user-specified. |
|  | SetAutoResourceBlockDetectionEnabled | Sets whether the values of the SetPuschModulationType(String, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(String, Int32), SetPuschResourceBlockOffset(String, Int32), and SetPuschNumberOfResourceBlocks(String, Int32) properties are auto-detected by the measurement or if you specify the values of these properties. |
|  | SetBandwidth | Sets the channel bandwidth of the signal being measured. This value is expressed in Hz. |
|  | SetCellId | Sets a physical layer cell identity. |
|  | SetComponentCarrierAtCenterFrequency | Sets the index of the component carrier having its center at the user-configured center frequency. RFmxLTE uses this method along with ComponentCarrierSpacingType method to calculate the value of the SetFrequency(String, Double). |
|  | SetCyclicPrefixMode | Sets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
|  | SetDmrsOccEnabled | Sets whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases. |
|  | SetDownlinkAutoCellIDDetectionEnabled | Sets whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using GetDownlinkDetectedCellID(String, Int32) method. |
|  | SetDownlinkChannelConfigurationMode | Sets the channel configuration mode. |
|  | SetDownlinkNumberOfSubframes | Sets the number of unique subframes transmitted by the DUT. If you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel, this method will be set to 10 for FDD and 20 for TDD by default. |
|  | SetDownlinkTestModel | Sets the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(String, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. |
|  | SetDownlinkUserDefinedCellSpecificRatio | Sets the ratio Rhob/Rhoa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 specification. This method determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. |
|  | SetEmtcAnalysisEnabled | Sets whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. |
|  | SetFrequency | Sets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. This method is applicable only if you set the ComponentCarrierSpacingType method to User. |
|  | SetLaaDownlinkNumberOfEndingSymbols | Sets the number of ending symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the 3GPP 36.211 specification for more information regarding LAA downlink number of ending symbols. |
|  | SetLaaDownlinkStartingSymbol | Sets the starting symbol number in the first subframe of an LAA downlink burst. Refer to section 13A of the 3GPP 36.213 specification for more information regarding LAA downlink starting symbol. |
|  | SetLaaNumberOfSubframes | Sets the number of subframes in an LAA burst including the starting subframe. |
|  | SetLaaStartingSubframe | Sets the starting subframe of an LAA burst. |
|  | SetLaaUplinkEndingSymbol | Sets the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP 36.212 specification for more information regarding LAA uplink ending symbol. |
|  | SetLaaUplinkStartPosition | Sets the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the 3GPP 36.211 specification for more information regarding LAA uplink start position. |
|  | SetNBIoTUplinkSubcarrierSpacing | Sets the subcarrier bandwidth of an NB-IoT signal. This method specifies the spacing between adjacent subcarriers. |
|  | SetNCellId | Sets the narrowband physical layer cell identity. |
|  | SetNPuschDmrsBaseSequenceIndex | Sets the base sequence index of the Narrowband Physical Uplink Shared Channel (NPUSCH) DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |
|  | SetNPuschDmrsBaseSequenceMode | Sets whether the SetNPuschDmrsBaseSequenceIndex(String, Int32) method is computed by the measurement or specified by you. |
|  | SetNPuschDmrsCyclicShift | Sets the cyclic shift of the narrowband physical uplink shared channel (NPUSCH) DMRS as defined in Table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. |
|  | SetNPuschDmrsDeltaSequenceShift | Sets the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This method is valid when you set the SetNPuschDmrsGroupHoppingEnabled(String, RFmxLteMXNPuschDmrsGroupHoppingEnabled) method to True. |
|  | SetNPuschDmrsGroupHoppingEnabled | Sets whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the SetNPuschFormat(String, Int32) is 1. |
|  | SetNPuschFormat | Sets the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information. |
|  | SetNPuschModulationType | Sets the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). |
|  | SetNPuschNumberOfTones | Sets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | SetNPuschStartingSlot | Sets the starting slot number of the NPUSCH burst. |
|  | SetNPuschToneOffset | Sets the location of the starting subcarrier (tone) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |
|  | SetNumberOfComponentCarriers | Sets the number of component carriers configured within a subblock. |
|  | SetNumberOfPdschChannels | Sets the number of physical downlink shared channel (PDSCH) allocations in a subframe. |
|  | SetPbchPower | Sets the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPcfichCfi | Sets the control format indicator (CFI) carried by physical control format indicator channel (PCFICH). CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. |
|  | SetPcfichPower | Sets the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPdcchPower | Sets the power of physical downlink control channel (PDCCH) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPdschCW0ModulationType | Sets the modulation type of codeword0 PDSCH allocation. |
|  | SetPdschPower | Sets the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the SetDownlinkUserDefinedCellSpecificRatio(String, RFmxLteMXDownlinkUserDefinedRatio) method to calculate the Rb. Refer to section 3.3 of the 3GPP 36.521 specification for more information about Ra. |
|  | SetPdschResourceBlockAllocation | Sets the resource blocks of the physical downlink shared channel (PDSCH) allocation. |
|  | SetPhichDuration | Sets the physical hybrid-ARQ indicator channel (PHICH) duration. |
|  | SetPhichPower | Sets the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. |
|  | SetPhichResource | Sets the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This method is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. |
|  | SetPsschModulationType | Sets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. |
|  | SetPsschNumberOfResourceBlocks | Sets the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation. |
|  | SetPsschPower | Sets the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB. |
|  | SetPsschResourceBlockOffset | Sets the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. |
|  | SetPssPower | Sets the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetPuschCyclicShiftField | Sets the cyclic shift field in uplink-related DCI format. When the SetDmrsOccEnabled(String, RFmxLteMXDmrsOccEnabled) method is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with SetTransmitAntennaToAnalyze(String, Int32). |
|  | SetPuschDeltaSequenceShift | Sets the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift. |
|  | SetPuschModulationType | Sets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | SetPuschNDmrs1 | Sets the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification. |
|  | SetPuschNDmrs2 | Sets the n_DMRS_2 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a slot. The valid values for this method are, as defined in table 5.5.2.1.1-1 of the 3GPP TS 36.211 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | SetPuschNumberOfResourceBlockClusters | Sets the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH).Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. |
|  | SetPuschNumberOfResourceBlocks | Sets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. |
|  | SetPuschPower | Sets the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
|  | SetPuschResourceBlockOffset | Sets the starting resource block number of a physical uplink shared channel (PUSCH) cluster. |
|  | SetSpacingType | Sets the spacing between two adjacent component carriers within a subblock. |
|  | SetSrsbHop | Sets the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(String, Int32) method. |
|  | SetSrsBSrs | Sets the UE specific SRS bandwidth configuration BSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsCSrs | Sets the cell-specific SRS bandwidth configuration CSRS. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsEnabled | Sets whether the LTE signal getting measured contains SRS transmission. |
|  | SetSrsISrs | Sets the SRS configuration index ISRS. It is used to determine the SRS periodicity and SRS subframe offset. It is a UE specific method which defines whether the SRS is transmitted in the subframe reserved for SRS by SRS subframe configuration. Refer to 3GPP 36.213 specification for more details. |
|  | SetSrskTC | Sets the transmission comb index. If you set this method to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this method to 1, SRS is transmitted on the odd subcarriers in the allocated region. |
|  | SetSrsMaximumUpPtsEnabled | Sets SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsnRrc | Sets the SRS frequency domain position nRRC. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsnSrsCS | Sets the cyclic shift value nSRSCS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. |
|  | SetSrsPower | Sets the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. |
|  | SetSrsSubframe1NRA | Sets the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD. |
|  | SetSrsSubframe6NRA | Sets the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. |
|  | SetSrsSubframeConfiguration | Sets the SRS subframe configuration specified in the Table 5.5.3.3-1 of 3GPP 36.211 specification. It is a cell-specific method. This method defines the subframes that are reserved for SRS transmission in a given cell. |
|  | SetSssPower | Sets the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB. |
|  | SetUplinkGroupHoppingEnabled | Sets whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. |
|  | SetUplinkSequenceHoppingEnabled | Sets whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. This method is only applicable only when you set the SetPuschNumberOfResourceBlocks(String, Int32) method to a value greater than 5. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RFmxLteMXComponentCarrier Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ff71575f-7ff2-6453-6019-25f9a0c96131.htm language=enus -->
## TOPIC 00429: rfmxltedotnet/html/ff71575f-7ff2-6453-6019-25f9a0c96131.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ff71575f-7ff2-6453-6019-25f9a0c96131.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ff71575f-7ff2-6453-6019-25f9a0c96131.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXSemConfiguration.GetSidelinkMaskType Method

RFmxLteMXSemConfigurationGetSidelinkMaskType Method

Custom

3GPP 36.521

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSidelinkMaskType(
	string selectorString,
	out RFmxLteMXSemSidelinkMaskType value
)
```

```text
Public Function GetSidelinkMaskType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxLteMXSemSidelinkMaskType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.LteMXRFmxLteMXSemSidelinkMaskType Upon return, contains the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about standard-defined mask types.

###### Return Value

Int32

##### Remarks

SemSidelinkMaskType

##### See Also

###### Reference

RFmxLteMXSemConfiguration Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-lte-dotnet path=rfmxltedotnet/html/ff8490ff-f8df-9a30-f42d-e41fd2d7d7c7.htm language=enus -->
## TOPIC 00430: rfmxltedotnet/html/ff8490ff-f8df-9a30-f42d-e41fd2d7d7c7.htm

- bundle_id: `rfmx-lte-dotnet`
- source_path: `rfmxltedotnet/html/ff8490ff-f8df-9a30-f42d-e41fd2d7d7c7.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-dotnet/raw/resource/enus/rfmxltedotnet/html/ff8490ff-f8df-9a30-f42d-e41fd2d7d7c7.htm
- document_id: `rfmx-lte-dotnet`
- page_type: `leaf`
- content_type: ``

RFmxLteMXModAccResults.FetchPuschSymbolPower Method

RFmxLteMXModAccResultsFetchPuschSymbolPower Method

Namespace:

NationalInstruments.RFmx.LteMX

Assembly:

##### Syntax

C#

VB

```text
public int FetchPuschSymbolPower(
	string selectorString,
	double timeout,
	out double puschMeanDataPower,
	out double puschMeanDmrsPower
)
```

```text
Public Function FetchPuschSymbolPower ( 
	selectorString As String,
	timeout As Double,
	<OutAttribute> ByRef puschMeanDataPower As Double,
	<OutAttribute> ByRef puschMeanDmrsPower As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(String, Int32) method to build the selector string.
- **timeout**
  - Type: SystemDoubleSpecifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete.
- **puschMeanDataPower**
  - Type: SystemDouble Upon return, contains the mean value of the power calculated on PUSCH data symbols over the slots specified by the SetMeasurementLength(String, Int32) method.
- **puschMeanDmrsPower**
  - Type: SystemDouble Upon return, contains the mean value of the power calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length method.

###### Return Value

Int32

##### See Also

###### Reference

RFmxLteMXModAccResults Class

NationalInstruments.RFmx.LteMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
