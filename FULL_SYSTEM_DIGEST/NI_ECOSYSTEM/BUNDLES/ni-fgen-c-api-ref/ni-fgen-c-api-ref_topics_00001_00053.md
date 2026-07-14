# NI DOCUMENT BUNDLE: ni-fgen-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-fgen-c-api-ref start=1 end=53 -->
<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/arbitrary_waveform_output.html language=enus -->
## TOPIC 00001: Arbitrary Waveform Output Functions

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/arbitrary_waveform_output.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/arbitrary_waveform_output.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform Output Functions

| Configure Gain | niFgen_ConfigureGain |
| --- | --- |
| Configure Sample Rate | niFgen_ConfigureSampleRate |
| Query Arb Waveform Capabilities | niFgen_QueryArbWfmCapabilities |
| Create Waveform F64 | niFgen_CreateWaveformF64 |
| Create Waveform I16 | niFgen_CreateWaveformI16 |
| Create Waveform Complex F64 | niFgen_CreateWaveformComplexF64 |
| Create Waveform from File I16 | niFgen_CreateWaveformFromFileI16 |
| Create Waveform from File F64 | niFgen_CreateWaveformFromFileF64 |
| Create Waveform from File HWS | niFgen_CreateWaveformFromFileHWS |
| Configure Arbitrary Waveform | niFgen_ConfigureArbWaveform |
| Clear Arbitrary Waveform | niFgen_ClearArbWaveform |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/calibration_utility_functions.html language=enus -->
## TOPIC 00002: Calibration Utility Functions

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/calibration_utility_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/calibration_utility_functions.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Calibration Utility Functions

| Get Self Cal Supported | niFgen_GetSelfCalSupported |
| --- | --- |
| Get Self Cal Last Date And Time | niFgen_GetSelfCalLastDateAndTime |
| Get Ext Cal Last Date And Time | niFgen_GetExtCalLastDateAndTime |
| Get Self Cal Last Temp | niFgen_GetSelfCalLastTemp |
| Get Ext Cal Last Temp | niFgen_GetExtCalLastTemp |
| Get Ext Cal Recommended Interval | niFgen_GetExtCalRecommendedInterval |
| Change Ext Cal Password | niFgen_ChangeExtCalPassword |
| Set Cal User Defined Info | niFgen_SetCalUserDefinedInfo |
| Get Cal User Defined Info | niFgen_GetCalUserDefinedInfo |
| Get Cal User Defined Info Max Size | niFgen_GetCalUserDefinedInfoMaxSize |
| Read Current Temperature | niFgen_ReadCurrentTemperature |
| Restore Last Ext Cal Constants | niFgen_RestoreLastExtCalConstants |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/configure_clock.html language=enus -->
## TOPIC 00003: Configure Clock Functions

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/configure_clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/configure_clock.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Configure Clock Functions

| Configure Reference Clock | niFgen_ConfigureReferenceClock |
| --- | --- |
| Configure Sample Clock Source | niFgen_ConfigureSampleClockSource |
| Configure Clock Mode | niFgen_ConfigureClockMode |
| Adjust Sample Clock Relative Delay | niFgen_AdjustSampleClockRelativeDelay |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_abortgeneration.html language=enus -->
## TOPIC 00004: niFgen_AbortGeneration

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_abortgeneration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_abortgeneration.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_AbortGeneration

ViStatus niFgen_AbortGeneration (ViSession vi);

#### Purpose

Aborts any previously initiated signal generation. Call the 
[niFgen_InitiateGeneration](/csh?topicname=fgencref/cvinifgen_initiategeneration.html) function to cause the signal generator to produce a signal again.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_adjustsampleclockrelativedelay.html language=enus -->
## TOPIC 00005: niFgen_AdjustSampleClockRelativeDelay

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_adjustsampleclockrelativedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_adjustsampleclockrelativedelay.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_AdjustSampleClockRelativeDelay

ViStatus niFgen_AdjustSampleClockRelativeDelay (ViSession vi, ViReal64 adjustmentTime);

#### Purpose

Delays (or phase shifts) the Sample Clock, which delays the generated signal. Delaying the Sample Clock can be useful when synchronizing the output of multiple modules or when intentionally phase shifting the output relative to a fixed reference, such as the PLL Reference Clock.

Adjustment time can be positive or negative, but it must be less than or equal to the Sample Clock period. The delay takes effect immediately after this function is called. To delay an external Sample Clock, use the 
[NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY](/csh?topicname=fgencref/nifgen_attr_sample_clock_absolute_delay.html) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| adjustmentTime | ViReal64 | Specifies the amount of time to adjust the Sample Clock delay. Units: Seconds Default Value: 0 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_checkattributevireal64.html language=enus -->
## TOPIC 00006: niFgen_CheckAttributeViReal64

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_checkattributevireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_checkattributevireal64.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_CheckAttributeViReal64

ViStatus niFgen_CheckAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attributeID, ViReal64 attributeValue);

#### Purpose

Checks the validity of a value you specify for a ViReal64 attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| channelName | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel-based. If the attribute is not channel-based, then pass VI_NULL or an empty string (""). Default Value: "" (empty string) |
| attributeID | ViAttr | Specifies the ID of an attribute. |
| attributeValue | ViReal64 | Specifies the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current settings of the instrument session. Default Value: None |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_cleararbsequence.html language=enus -->
## TOPIC 00007: niFgen_ClearArbSequence

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_cleararbsequence.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_cleararbsequence.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ClearArbSequence

ViStatus niFgen_ClearArbSequence (ViSession vi, ViInt32 sequenceHandle);

#### Purpose

Removes a previously created arbitrary sequence from the signal generator memory and invalidates the sequence handle.

|  | Note The signal generator must not be in the Generating state when you call this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| sequenceHandle | ViInt32 | Specifies the handle of the arbitrary sequence that you want the signal generator to remove. You can create an arbitrary sequence using the niFgen_CreateArbSequence or niFgen_CreateAdvancedArbSequence function. These functions return a handle that you use to identify the sequence. Defined Value:NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal generator Default Value: None |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_cleararbwaveform.html language=enus -->
## TOPIC 00008: niFgen_ClearArbWaveform

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_cleararbwaveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_cleararbwaveform.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ClearArbWaveform

ViStatus niFgen_ClearArbWaveform (ViSession vi, ViInt32 waveformHandle);

#### Purpose

Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle.

|  | Note The signal generator must not be in the Generating state when you call this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| waveformHandle | ViInt32 | Specifies the handle of the arbitrary waveform that you want the signal generator to remove. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform functions: niFgen_CreateWaveformF64 niFgen_CreateWaveformI16 niFgen_CreateWaveformFromFileI16 niFgen_CreateWaveformFromFileF64 niFgen_CreateWaveformFromFileHWS Defined Value: NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal generator. Default Value: None |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_clearerror.html language=enus -->
## TOPIC 00009: niFgen_ClearError

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_clearerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_clearerror.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ClearError

ViStatus niFgen_ClearError (ViSession vi);

#### Purpose

Clears the error information for the current execution thread and the IVI session you specify. If you pass VI_NULL for the **vi** parameter, this function clears the error information only for the current execution thread.

This function sets the error code to VI_SUCCESS (0), and sets the error description string to "" (empty string).

The IVI Engine also maintains this error information separately for each thread. This feature is useful if you do not have a session handle to pass to the [niFgen_ClearError](/csh?topicname=fgencref/cvinifgen_clearerror.html) or the [niFgen_GetError](/csh?topicname=fgencref/cvinifgen_geterror.html) function. This situation occurs when a call to the [niFgen_init](/csh?topicname=fgencref/cvinifgen_init.html) or [niFgen_InitWithOptions](/csh?topicname=fgencref/cvinifgen_initwithoptions.html) function fails.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_initializecaladccalibration.html language=enus -->
## TOPIC 00010: niFgen_InitializeCalADCCalibration

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_initializecaladccalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_initializecaladccalibration.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_InitializeCalADCCalibration

ViStatus niFgen_InitializeCalADCCalibration (ViSession vi);

#### Purpose

Initializes an external calibration session for ADC calibration. For the NI 5421/5422/5441, ADC calibration involves characterizing the gain and offset of the onboard ADC.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_InitExtCal function and identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_initializewithchannels.html language=enus -->
## TOPIC 00011: niFgen_InitializeWithChannels

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_initializewithchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_initializewithchannels.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_InitializeWithChannels

ViStatus niFgen_InitializeWithChannels (ViRsrc resourceName, ViConstString channelName, ViBoolean resetDevice, ViConstString optionString, ViSession *vi);

#### Purpose

Creates and returns a new NI-FGEN session to the specified channel of a waveform generator that is used in all subsequent NI-FGEN function calls.

#### Parameters

| Input |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Description |  |
| resourceName | ViRsrc | Specifies the resource name of the device to initialize. Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. If you use the DAQ::n syntax and an NI-DAQmx device name already exists with that same name, the NI-DAQmx device is matched first. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Caution Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. |  |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |
|  | Caution Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. |  |  |
| channelName | ViConstString | Specifies the channel that this VI uses. Default Value: "0" |  |
| resetDevice | ViBoolean | Specifies whether you want to reset the device during the initialization procedure. VI_TRUE specifies that the device is reset and performs the same function as the niFgen_reset function. Defined Values VI_TRUEReset device VI_FALSEDo not reset device Default Value: VI_FALSE |  |
| VI_TRUE | Reset device |  |  |
| VI_FALSE | Do not reset device |  |  |
| optionString | ViConstString | Sets the initial value of certain session attributes. The syntax for optionString is <attributeName> = <value> where attributeName is the name of the attribute and value is the value to which the attribute is set To set multiple attributes, separate them with a comma. If you pass NULL or an empty string for this parameter, the session uses the default values for these attributes. You can override the default values by assigning a value explicitly in a string that you pass for this parameter. You do not have to specify all of the attributes and may leave any of them out. However, if you do not specify one of the attributes, its default value is used. If simulation is enabled (Simulate=1), you may specify the device that you want to simulate. To specify a device, enter the following syntax in optionString. DriverSetup=Model:<driver model number>;Channels:<channel names>;BoardType:<module type>;MemorySize:<size of onboard memory in bytes> Syntax Examples Device optionString Syntax NI PXI-5404 DriverSetup=Model:5404;BoardType:PXI NI PCI-5411 DriverSetup=Model:5411;BoardType:PCI;MemorySize:8000000 NI PXIe-5450 DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:8000000 Attributes and Defined Values Attribute Name Attribute Values RangeCheck NIFGEN_ATTR_RANGE_CHECK VI_TRUE, VI_FALSE QueryInstrStatus NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS VI_TRUE, VI_FALSE Cache NIFGEN_ATTR_CACHE VI_TRUE, VI_FALSE Simulate NIFGEN_ATTR_SIMULATE VI_TRUE, VI_FALSE Default Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1" |  |
| Device | optionString Syntax |  |  |
| NI PXI-5404 | DriverSetup=Model:5404;BoardType:PXI |  |  |
| NI PCI-5411 | DriverSetup=Model:5411;BoardType:PCI;MemorySize:8000000 |  |  |
| NI PXIe-5450 | DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:8000000 |  |  |
| Attribute Name | Attribute | Values |  |
| RangeCheck | NIFGEN_ATTR_RANGE_CHECK | VI_TRUE, VI_FALSE |  |
| QueryInstrStatus | NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE, VI_FALSE |  |
| Cache | NIFGEN_ATTR_CACHE | VI_TRUE, VI_FALSE |  |
| Simulate | NIFGEN_ATTR_SIMULATE | VI_TRUE, VI_FALSE |  |
| Output |  |  |  |
| Name | Type | Description |  |
| vi | ViSession | Returns a session handle that you can use to identify the device in all subsequent NI-FGEN function calls. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_locksession.html language=enus -->
## TOPIC 00012: niFgen_LockSession

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_locksession.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_locksession.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_LockSession

ViStatus niFgen_LockSession (ViSession vi, ViBoolean* callerHasLock);

#### Purpose

Obtains a multithread lock on the instrument session. Before it does so, this function waits until all other execution threads have released their locks on the instrument session.

Other threads might have obtained a lock on this session in the following ways:

- Your application called the niFgen_LockSession function.
- A call to the NI-FGEN locked the session.
- A call to the IVI Engine locked the session.

After your call to the niFgen_LockSession function returns successfully, no other threads can access the instrument session until you call the [niFgen_UnlockSession](/csh?topicname=fgencref/cvinifgen_unlocksession.html) function.

Use the niFgen_LockSession function and the niFgen_UnlockSession function around a sequence of calls to NI-FGEN functions if you require that the instrument retain its settings through the end of the sequence.

You can safely make nested calls to the niFgen_LockSession function within the same thread. To completely unlock the session, you must balance each call to the niFgen_LockSession function with a call to the niFgen_UnlockSession function. If, however, you use the **callerHasLock** parameter in all calls to the niFgen_LockSession function and the niFgen_UnlockSession function within a function, the IVI Engine locks the session only once within the function regardless of the number of calls you make to the niFgen_LockSession function. This configuration allows you to call the niFgen_UnlockSession function just once at the end of the function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| callerHasLock | ViBoolean* | Keeps track of whether you obtained a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the niFgen_LockSession function or the niFgen_UnlockSession function in the same function. This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. This parameter is an input/output parameter. The niFgen_LockSession function and the niFgen_UnlockSession function each inspect the current value and take the following actions: If the value is VI_TRUE, the niFgen_LockSession function does not lock the session again. If the value is VI_FALSE, the niFgen_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE. If the value is VI_FALSE, the niFgen_UnlockSession function does not attempt to unlock the session. If the value is VI_TRUE, the niFgen_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE. Thus, you can call the niFgen_UnlockSession function at the end of your function without worrying about whether you actually have the lock. Example: ViStatus TestFunc (ViSession vi, ViInt32 flags) { ViStatus error = VI_SUCCESS; ViBoolean haveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr( niFgen_LockSession(vi, &haveLock)); viCheckErr( TakeAction1(vi)); if (flags & BIT_2) { viCheckErr( niFgen_UnlockSession(vi, &haveLock)); viCheckErr( TakeAction2(vi)); viCheckErr( niFgen_LockSession(vi, &haveLock); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); } Error: /* At this point, you cannot really be sure that you have the lock. Fortunately, the haveLock variable takes care of that for you. */ niFgen_UnlockSession(vi, &haveLock); return error; } |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_manualenablep2pstream.html language=enus -->
## TOPIC 00013: niFgen_ManualEnableP2PStream

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_manualenablep2pstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_manualenablep2pstream.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ManualEnableP2PStream

ViStatus niFgen_ManualEnableP2PStream (ViSession vi, ViConstString endpointName[]

#### Purpose

Enables a peer-to-peer data stream using manual flow control.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| endpointName | ViConstString [] | Specifies the stream endpoint FIFO to configure. Refer to the Peer-to-Peer Data Streaming documentation in the NI Signal Generators Help for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_queryarbseqcapabilities.html language=enus -->
## TOPIC 00014: niFgen_QueryArbSeqCapabilities

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_queryarbseqcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_queryarbseqcapabilities.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_QueryArbSeqCapabilities

ViStatus niFgen_QueryArbSeqCapabilities (ViSession vi, ViInt32* maximumNumberofSequences, ViInt32* minimumSequenceLength, ViInt32* maximumSequenceLength, ViInt32* maximumLoopCount);

#### Purpose

Returns the attributes of the signal generator that are related to creating arbitrary sequences (the [NIFGEN_ATTR_MAX_NUM_SEQUENCES](/csh?topicname=fgencref/nifgen_attr_max_num_sequences.html), [NIFGEN_ATTR_MIN_SEQUENCE_LENGTH](/csh?topicname=fgencref/nifgen_attr_min_sequence_length.html), [NIFGEN_ATTR_MAX_SEQUENCE_LENGTH](/csh?topicname=fgencref/nifgen_attr_max_sequence_length.html), and [NIFGEN_ATTR_MAX_LOOP_COUNT](/csh?topicname=fgencref/nifgen_attr_max_loop_count.html) attributes).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| maximumNumberofSequences | ViInt32* | Returns the maximum number of arbitrary waveform sequences that the signal generator allows. NI-FGEN obtains this value from the NIFGEN_ATTR_MAX_NUM_SEQUENCES attribute. |
| minimumSequenceLength | ViInt32* | Returns the minimum number of arbitrary waveforms the signal generator allows in a sequence. NI-FGEN obtains this value from the NIFGEN_ATTR_MIN_SEQUENCE_LENGTH attribute. |
| maximumSequenceLength | ViInt32* | Returns the maximum number of arbitrary waveforms the signal generator allows in a sequence. NI-FGEN obtains this value from the NIFGEN_ATTR_MAX_SEQUENCE_LENGTH attribute. |
| maximumLoopCount | ViInt32* | Returns the maximum number of times the signal generator can repeat an arbitrary waveform in a sequence. NI-FGEN obtains this value from the NIFGEN_ATTR_MAX_LOOP_COUNT attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_readcurrenttemperature.html language=enus -->
## TOPIC 00015: niFgen_ReadCurrentTemperature

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_readcurrenttemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_readcurrenttemperature.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ReadCurrentTemperature

ViStatus niFgen_ReadCurrentTemperature (ViSession vi, ViReal64* temperature);

#### Purpose

Reads the current onboard temperature of the device. The temperature is returned in degrees Celsius.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init or the niFgen_InitExtCal function and identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| Temperature | ViReal64* | Returns the current temperature read from onboard temperature sensors, in degrees Celsius. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_reset.html language=enus -->
## TOPIC 00016: niFgen_reset

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_reset.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_reset

ViStatus niFgen_reset (ViSession vi);

#### Purpose

Resets the instrument to a known state. This function aborts the generation, clears all 
routes, and resets session attributes to the default values. This function does not, 
however, commit the session properties or configure the device hardware to its default 
state.

|  | Note For the NI 5401/5404/5411/5431, this function exhibits the same behavior as the niFgen_ResetDevice function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_resetattribute.html language=enus -->
## TOPIC 00017: niFgen_ResetAttribute

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_resetattribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_resetattribute.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ResetAttribute

ViStatus niFgen_ResetAttribute (ViSession vi, ViConstString channelName, ViAttr attributeID);

#### Purpose

Resets the attribute to its default value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |
| channelName | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel-based. If the attribute is not channel-based, then pass VI_NULL or an empty string (""). Default Value: "" (empty string) |
| attributeID | ViAttr | Specifies the ID of an attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/cvinifgen_resetdevice.html language=enus -->
## TOPIC 00018: niFgen_ResetDevice

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/cvinifgen_resetdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/cvinifgen_resetdevice.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niFgen_ResetDevice

ViStatus niFgen_ResetDevice (ViSession vi);

#### Purpose

Performs a hard reset on the device. Generation is stopped, all routes are released, external bidirectional terminals are tristated, FPGAs are reset, hardware is configured to its default state, and all session attributes are reset to their default states.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi is obtained from the niFgen_init, niFgen_InitWithOptions, or niFgen_InitializeWithChannels functions and identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You can examine the status code from each call to an NI-FGEN function to determine if an error occurred. To obtain a text description of the status code, call the niFgen_error_message function. To obtain additional information about the error condition, call the niFgen_GetError function. To clear the error information from NI-FGEN, call the niFgen_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_marker_event_pulse_width.html language=enus -->
## TOPIC 00019: NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_marker_event_pulse_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_marker_event_pulse_width.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150340 | ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the pulse width value of the Marker event.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_marker_event_pulse_width_units.html language=enus -->
## TOPIC 00020: NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_marker_event_pulse_width_units.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_marker_event_pulse_width_units.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150341 | ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the pulse width units of the Marker event.

**Defined Values**

| NIFGEN_VAL_SAMPLE_CLOCK_PERIODS | Specifies the pulse width in Sample clock periods. |
| --- | --- |
| NIFGEN_VAL_SECONDS | Specifies the pulse width in seconds. |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_markerevents_count.html language=enus -->
## TOPIC 00021: NIFGEN_ATTR_MARKER_EVENTS_COUNT

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_markerevents_count.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_markerevents_count.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MARKER_EVENTS_COUNT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150271 | ViInt32 | RO | N/A | None | None |

#### Description

Returns the number of markers supported by the device. Use this attribute when the [NIFGEN_ATTR_OUTPUT_MODE](nifgen_attr_output_mode.html) attribute is set to NIFGEN_VAL_OUTPUT_SCRIPT.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_max_freq_list_duration.html language=enus -->
## TOPIC 00022: NIFGEN_ATTR_MAX_FREQ_LIST_DURATION

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_max_freq_list_duration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_max_freq_list_duration.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MAX_FREQ_LIST_DURATION

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150213 | ViReal64 | RO | N/A | None | None |

#### Description

Specifies the maximum duration of any one step in the frequency list.

|  | Note You cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete. |
| --- | --- |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_max_num_freq_lists.html language=enus -->
## TOPIC 00023: NIFGEN_ATTR_MAX_NUM_FREQ_LISTS

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_max_num_freq_lists.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_max_num_freq_lists.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MAX_NUM_FREQ_LISTS

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150209 | ViInt32 | RO | N/A | None | None |

#### Description

Returns the maximum number of frequency lists the signal generator allows.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_max_num_sequences.html language=enus -->
## TOPIC 00024: NIFGEN_ATTR_MAX_NUM_SEQUENCES

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_max_num_sequences.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_max_num_sequences.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MAX_NUM_SEQUENCES

#### IviFgenArbSeq Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250212 | ViInt32 | RO | N/A | None | niFgen_QueryArbSeqCapabilities |

#### Description

Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_max_num_waveforms.html language=enus -->
## TOPIC 00025: NIFGEN_ATTR_MAX_NUM_WAVEFORMS

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_max_num_waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_max_num_waveforms.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MAX_NUM_WAVEFORMS

#### IviFgenArbWfm Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250205 | ViInt32 | RO | N/A | None | niFgen_QueryArbWfmCapabilities |

#### Description

Returns the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_max_sequence_length.html language=enus -->
## TOPIC 00026: NIFGEN_ATTR_MAX_SEQUENCE_LENGTH

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_max_sequence_length.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_max_sequence_length.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MAX_SEQUENCE_LENGTH

#### IviFgenArbSeq Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250214 | ViInt32 | RO | N/A | None | niFgen_QueryArbSeqCapabilities |

#### Description

Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_memory_size.html language=enus -->
## TOPIC 00027: NIFGEN_ATTR_MEMORY_SIZE

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_memory_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_memory_size.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MEMORY_SIZE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150242 | ViInt32 | RO | N/A | None | None |

#### Description

Returns the total amount of memory, in bytes, on the signal generator.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_min_freq_list_duration.html language=enus -->
## TOPIC 00028: NIFGEN_ATTR_MIN_FREQ_LIST_DURATION

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_min_freq_list_duration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_min_freq_list_duration.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_MIN_FREQ_LIST_DURATION

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150212 | ViReal64 | RO | N/A | None | None |

#### Description

Returns the minimum duration in seconds of any one step in a frequency list.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_range_check.html language=enus -->
## TOPIC 00029: NIFGEN_ATTR_RANGE_CHECK

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_range_check.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_range_check.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_RANGE_CHECK

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050002 | ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether to validate attribute values and function parameters. If enabled, NI-FGEN validates the parameter values that you pass to NI-FGEN functions. Range-checking parameters is useful for debugging. After you validate your program, you can set this attribute to VI_FALSE to disable range checking and maximize performance.

Use the [niFgen_InitWithOptions](cvinifgen_initwithoptions.html) function to override the default value.

**Defined Values**

| VI_TRUE | Enables range checking. |
| --- | --- |
| VI_FALSE | Disables range checking. |

**Default Value**: VI_TRUE

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_ref_clock_source.html language=enus -->
## TOPIC 00030: NIFGEN_ATTR_REF_CLOCK_SOURCE

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_ref_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_ref_clock_source.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_REF_CLOCK_SOURCE

#### IviFgenBase Attribute

| Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niFgen_ConfigureRefClockSource |

#### Description

Specifies the source for the Reference Clock. For example, when you set this attribute to "ClkIn," the signal generator uses the signal it receives at its CLK IN front panel connector as the Reference Clock.

The Reference Clock at the specified source phase-locks with the signal generator Sample Clock timebase to allow the frequency stability and accuracy of the Sample Clock timebase to match that of the Reference Clock.

|  | Notes The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call the niFgen Abort Generation function or wait for the generation to complete. |
| --- | --- |
|  | The following defined values are examples of possible Reference Clock sources. For a complete list of the Reference Clock sources available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. |

**Defined Values**

| "None" | Specifies that a Reference Clock is not used. |
| --- | --- |
| "PXI_Clk10" | Specifies that the 10 MHz Reference Clock signal provided by the PXI bus is used as the Reference Clock source. |
| "ClkIn" | Specifies that the CLK IN input signal from the front panel connector is used as the Reference Clock source. |
| "OnboardReferenceClock" | Specifies that the onboard reference clock is used as the Reference Clock source. |
| "RTSI7" | Specifies that the RTSI line 7 is used as the Reference Clock source. |
| "RefIn" | Specifies that the external signal on the REF IN front panel connector is used as the Reference Clock source. |

**Default Value**: "None"

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_sample_clock_absolute_delay.html language=enus -->
## TOPIC 00031: NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_sample_clock_absolute_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_sample_clock_absolute_delay.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150231 | ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the delay in seconds to apply to an external Sample clock. This property is useful when trying to align the output of two devices.

|  | Note For the NI 5421, absolute delay can only be applied when an external Sample clock is used. |
| --- | --- |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_sample_clock_source.html language=enus -->
## TOPIC 00032: NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_sample_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_sample_clock_source.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150112 | ViString | R/W | N/A | None | None |

#### Description

Specifies the Sample clock source.

|  | Notes The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete. |
| --- | --- |
|  | The following defined values are examples of possible Sample clock sources. For a complete list of the Sample clock sources available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. |

**Defined Values**

| OnboardClock | Specifies that the onboard clock is used as the Sample clock source. |
| --- | --- |
| ClkIn | Specifies that the signal at the CLK IN front panel connector is used as the Sample clock source. |
| PXI_Star | Specifies that the PXI star trigger line is used as the Sample clock source. |
| PXI_Trig0 | Specifies that the PXI or RTSI line 0 is used as the Sample clock source. |
| PXI_Trig1 | Specifies that the PXI or RTSI line 1 is used as the Sample clock source. |
| PXI_Trig2 | Specifies that the PXI or RTSI line 2 is used as the Sample clock source. |
| PXI_Trig3 | Specifies that the PXI or RTSI line 3 is used as the Sample clock source. |
| PXI_Trig4 | Specifies that the PXI or RTSI line 4 is used as the Sample clock source. |
| PXI_Trig5 | Specifies that the PXI or RTSI line 5 is used as the Sample clock source. |
| PXI_Trig6 | Specifies that the PXI or RTSI line 6 is used as the Sample clock source. |
| PXI_Trig7 | Specifies that the PXI or RTSI line 7 is used as the Sample clock source. |
| DDC_ClkIn | Specifies that the Sample clock from DDC connector is used as the Sample clock source. |

**Default Value**: OnboardClock

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_sample_clock_timebase_rate.html language=enus -->
## TOPIC 00033: NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_sample_clock_timebase_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_sample_clock_timebase_rate.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150368 | ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the Sample clock timebase rate. This attribute applies only to external Sample clock timebases.

|  | Note The signal generator must not be in the Generating state when you set this attribute. To change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete. |
| --- | --- |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_sample_clock_timebase_source.html language=enus -->
## TOPIC 00034: NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_sample_clock_timebase_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_sample_clock_timebase_source.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150367 | ViString | R/W | N/A | None | None |

#### Description

Specifies the Sample clock timebase source.

|  | Notes The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete. |
| --- | --- |
|  | The following defined values are examples of possible Sample clock timebase sources. For a complete list of the Sample clock timebase sources available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. |

**Defined Values**

| OnboardClk (Default) | Specifies that the onboard Sample clock timebase is used as the source. |
| --- | --- |
| ClkIn | Specifies that the external signal on the CLK IN front panel connector is used as the source. |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_script_trigger_type.html language=enus -->
## TOPIC 00035: NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_script_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_script_trigger_type.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150290 | ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the Script trigger type. Depending upon the value of this attribute, additional attributes may be needed to fully configure the trigger.

**Defined Values**:

| NIFGEN_VAL_TRIG_NONE | No trigger is configured. Signal generation starts immediately. |
| --- | --- |
| NIFGEN_VAL_DIGITAL_EDGE | Trigger is asserted when a digital edge is detected. |
| NIFGEN_VAL_DIGITAL_LEVEL | Trigger is asserted when a digital level is detected. |
| NIFGEN_VAL_SOFTWARE_EDGE | Trigger is asserted when a software edge is detected. |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_scripttriggers_count.html language=enus -->
## TOPIC 00036: NIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_scripttriggers_count.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_scripttriggers_count.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NNIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150272 | ViInt32 | RO | N/A | None | None |

#### Description

Specifies the number of Script triggers supported by the device. Use this attribute when the [NIFGEN_ATTR_OUTPUT_MODE](nifgen_attr_output_mode.html) attribute is set to NIFGEN_VAL_OUTPUT_SCRIPT.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_secondary_error.html language=enus -->
## TOPIC 00037: NIFGEN_ATTR_SECONDARY_ERROR

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_secondary_error.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_secondary_error.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SECONDARY_ERROR

#### Specific Attribute

| Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies an optional code that provides additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. A value of 0 indicates no additional information.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_specific_driver_description.html language=enus -->
## TOPIC 00038: NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_specific_driver_description.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_specific_driver_description.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050514 | ViString | RO | N/A | None | None |

#### Description

Returns a brief description of the specific driver.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_specific_driver_prefix.html language=enus -->
## TOPIC 00039: NIFGEN_ATTR_SPECIFIC_DRIVER_PREFIX

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_specific_driver_prefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_specific_driver_prefix.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SPECIFIC_DRIVER_PREFIX

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050302 | ViString | RO | N/A | None | None |

#### Description

Returns a string that contains the prefix for NI-FGEN. The name of each user-callable function in NI-FGEN starts with this prefix.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_specific_driver_revision.html language=enus -->
## TOPIC 00040: NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_specific_driver_revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_specific_driver_revision.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050551 | ViString | RO | N/A | None | None |

#### Description

Returns a string that contains additional version information about NI-FGEN.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_specific_driver_vendor.html language=enus -->
## TOPIC 00041: NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_specific_driver_vendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_specific_driver_vendor.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050513 | ViString | RO | N/A | None | None |

#### Description

Returns a string that contains the name of the vendor that supplies NI-FGEN.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_started_event_delay.html language=enus -->
## TOPIC 00042: NIFGEN_ATTR_STARTED_EVENT_DELAY

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_started_event_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_started_event_delay.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STARTED_EVENT_DELAY

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150356 | ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the amount of delay applied to a Started event with respect to the analog output of the signal generator. A positive delay value specifies that the Started event occurs after the analog data, and a negative delay value specifies that the Started event occurs before the analog data. The default value is zero, which aligns the Started event with the analog output.

You can specify the units of the delay value by setting the [NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS](nifgen_attr_started_event_delay_units.html) attribute.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_started_event_delay_units.html language=enus -->
## TOPIC 00043: NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_started_event_delay_units.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_started_event_delay_units.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150357 | ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the units used for the [NIFGEN_ATTR_STARTED_EVENT_DELAY](nifgen_attr_started_event_delay.html) attribute.

##### Defined Values

| NIFGEN_VAL_SECONDS | Delay is specified in seconds and then coerced up by NI-FGEN to the nearest Sample clock period. |
| --- | --- |
| NIFGEN_VAL_SAMPLE_CLOCK_PERIODS | Delay is specified in Sample clock periods and then coerced up by NI-FGEN to the nearest Sample clock period. |

**Default Value**: NIFGEN_VAL_SECONDS

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_started_event_latched_status.html language=enus -->
## TOPIC 00044: NIFGEN_ATTR_STARTED_EVENT_LATCHED_STATUS

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_started_event_latched_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_started_event_latched_status.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STARTED_EVENT_LATCHED_STATUS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150352 | ViBoolean | RO | N/A | None | None |

#### Description

Returns the latched status of the Started event.

**Defined Values**

| VI_TRUE | The specified Started event has been active. |
| --- | --- |
| VI_FALSE | The specified Started event has not been active. |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_started_event_level_active_level.html language=enus -->
## TOPIC 00045: NIFGEN_ATTR_STARTED_EVENT_LEVEL_ACTIVE_LEVEL

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_started_event_level_active_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_started_event_level_active_level.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STARTED_EVENT_LEVEL_ACTIVE_LEVEL

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150316 | ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the output polarity of the Started event.

**Defined Values**:

| NIFGEN_VAL_ACTIVE_HIGH | When the operation has started, the Started event level is high. |
| --- | --- |
| NIFGEN_VAL_ACTIVE_LOW | When the operation has started, the Started event level is low. |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_started_event_output_behavior.html language=enus -->
## TOPIC 00046: NIFGEN_ATTR_STARTED_EVENT_OUTPUT_BEHAVIOR

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_started_event_output_behavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_started_event_output_behavior.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STARTED_EVENT_OUTPUT_BEHAVIOR

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150331 | ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the output behavior for the Started event.

**Defined Values**

| NIFGEN_VAL_PULSE | Triggers a pulse for a specified period of time. |
| --- | --- |
| NIFGEN_VAL_LEVEL | Shifts high or low while the event is active, depending on the active state you specify. |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_started_event_output_terminal.html language=enus -->
## TOPIC 00047: NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_started_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_started_event_output_terminal.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150314 | ViString | R/W | N/A | None | niFgen_ExportSignal |

#### Description

Specifies the destination terminal for the Started event. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_streaming_waveform_name.html language=enus -->
## TOPIC 00048: NIFGEN_ATTR_STREAMING_WAVEFORM_NAME

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_streaming_waveform_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_streaming_waveform_name.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STREAMING_WAVEFORM_NAME

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150326 | ViString | R/W | N/A | None | None |

#### Description

Specifies the name of the waveform used to continuously stream data during generation. This attribute defaults to "" (empty string)
 when no streaming waveform is specified.

Use this attribute in conjunction with the [NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM](nifgen_attr_streaming_space_available_in_waveform.html) attribute.

|  | Note You cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete. |
| --- | --- |

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_streaming_write_timeout.html language=enus -->
## TOPIC 00049: NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_streaming_write_timeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_streaming_write_timeout.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150409 | ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the maximum amount of time allowed to complete a streaming write operation.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_supported_instrument_models.html language=enus -->
## TOPIC 00050: NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_supported_instrument_models.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_supported_instrument_models.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050327 | ViString | RO | N/A | None | None |

#### Description

Returns a model code of the device. For NI-FGEN versions that support more than one device, this attribute contains a comma-separated list of supported device models.

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_sync_duty_cycle_high.html language=enus -->
## TOPIC 00051: NIFGEN_ATTR_SYNC_DUTY_CYCLE_HIGH

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_sync_duty_cycle_high.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_sync_duty_cycle_high.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SYNC_DUTY_CYCLE_HIGH

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150105 | ViReal64 | R/W | N/A | None | None |

#### Description

Controls the duty cycle of the square wave the signal generator produces on the SYNC OUT connector. Specify this attribute as a percentage of the time the square wave is high in each cycle.

**Units:** Percentage of the time the waveform is high

**Default Value**: 50%

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_attr_synchronization.html language=enus -->
## TOPIC 00052: NIFGEN_ATTR_SYNCHRONIZATION

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_attr_synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_attr_synchronization.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIFGEN_ATTR_SYNCHRONIZATION

#### Specific Attribute

| Numeric Value | Data Type | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150111 | ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the source of the synchronization signal to use.

|  | Note You cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete. |
| --- | --- |

**Defined Values**

| NIFGEN_VAL_NONE | Specifies that the generator use no synchronization source. |
| --- | --- |
| NIFGEN_VAL_RTSI_0 | Specifies that the generator use RTSI 0 as the synchronization source. |
| NIFGEN_VAL_RTSI_1 | Specifies that the generator use RTSI 1 as the synchronization source. |
| NIFGEN_VAL_RTSI_2 | Specifies that the generator use RTSI 2 as the synchronization source. |
| NIFGEN_VAL_RTSI_3 | Specifies that the generator use RTSI 3 as the synchronization source. |
| NIFGEN_VAL_RTSI_4 | Specifies that the generator use RTSI 4 as the synchronization source. |
| NIFGEN_VAL_RTSI_5 | Specifies that the generator use RTSI 5 as the synchronization source. |
| NIFGEN_VAL_RTSI_6 | Specifies that the generator use RTSI 6 as the synchronization source. |
| NIFGEN_VAL_TTL0 | Specifies that the generator use PXI TRIG0 or VXI TTL0 as the synchronization source. |
| NIFGEN_VAL_TTL1 | Specifies that the generator use PXI TRIG1 or VXI TTL1 as the synchronization source. |
| NIFGEN_VAL_TTL2 | Specifies that the generator use PXI TRIG2 or VXI TTL2 as the synchronization source. |
| NIFGEN_VAL_TTL3 | Specifies that the generator use PXI TRIG3 or VXI TTL3 as the synchronization source. |
| NIFGEN_VAL_TTL4 | Specifies that the generator use PXI TRIG4 or VXI TTL4 as the synchronization source. |
| NIFGEN_VAL_TTL5 | Specifies that the generator use PXI TRIG5 or VXI TTL5 as the synchronization source. |
| NIFGEN_VAL_TTL6 | Specifies that the generator use PXI TRIG6 or VXI TTL6 as the synchronization source. |

**Default Value**: NIFGEN_VAL_NONE

<!--NI_TOPIC bundle=ni-fgen-c-api-ref path=fgencref/nifgen_c_cplusplus_examples.html language=enus -->
## TOPIC 00053: NI-FGEN Examples for Microsoft Visual C/C++ (C examples)

- bundle_id: `ni-fgen-c-api-ref`
- source_path: `fgencref/nifgen_c_cplusplus_examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-c-api-ref/raw/resource/enus/fgencref/nifgen_c_cplusplus_examples.html
- document_id: `ni-fgen-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-FGEN 
Examples for Microsoft Visual C/C++ (C examples)

NI-FGEN ships with several examples for use with Microsoft Visual C/C++ (MSVC). These examples can help you develop software, and they illustrate how to perform the most common operations with the NI signal generators.

The MSVC examples were built and tested using Microsoft Visual C.

|  | Note Use the NMAKE utility in MSVC to build the examples. From an MS-DOS session, navigate to the location of the example files specified in the NI-FGEN Instrument Driver Readme. |
| --- | --- |

Use the msvc vcvars32.bat to set up the variables necessary for building examples. To build an example, run nmake /f examplename.mak. The executable is built to the debug subdirectory.

The source code for these examples as well as all of the input and output
values, is documented, making it easy to change the code to perform different types of generation.
