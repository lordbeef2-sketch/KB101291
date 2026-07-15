# NI DOCUMENT BUNDLE: rfmx-instr-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-instr-cvi start=1 end=77 -->
<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_buildcalibrationplanestring.html language=enus -->
## TOPIC 00001: RFmxInstr_BuildCalibrationPlaneString

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_buildcalibrationplanestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_buildcalibrationplanestring.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_BuildCalibrationPlaneString

int32 __stdcall RFmxInstr_BuildCalibrationPlaneString (char calibrationPlaneName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates the selector string to use with External Attenuation Table functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| calibrationPlaneName | char[] | Specifies the calibration plane name for building the selector string. This input accepts the calibration plane name with or without the "calplane::" prefix. example:"""calplane::plane0""plane0" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_buildinstrumentstring.html language=enus -->
## TOPIC 00002: RFmxInstr_BuildInstrumentString

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_buildinstrumentstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_buildinstrumentstring.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_BuildInstrumentString

int32 __stdcall RFmxInstr_BuildInstrumentString (char selectorString[],
 int32 LOIndex,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the instrument string to use as the Selector String for reading the recommended settings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies the selector string. example:"" |
| instrumentNumber | int32 | Specifies the instrument number for which you want the recommended settings to be read. |
| selectorStringOutLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_buildmodulestring.html language=enus -->
## TOPIC 00003: RFmxInstr_BuildModuleString

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_buildmodulestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_buildmodulestring.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_BuildModuleString

int32 __stdcall RFmxInstr_BuildModuleString (char selectorString[],
 char moduleName[],
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Configures the Module string to use as the [Selector String](/csh?topicname=rfmxspecan/) for reading temperature of specific modules of the device.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies the selector string. example:"" |
| moduleName | char[] | Specifies the module for which you want the temperature to be read. |
| selectorStringOutLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_cfgexternalattenuationtable.html language=enus -->
## TOPIC 00004: RFmxInstr_CfgExternalAttenuationTable

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_cfgexternalattenuationtable.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_cfgexternalattenuationtable.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgExternalAttenuationTable

int32 __stdcall RFmxInstr_CfgExternalAttenuationTable (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char tableName[],
 float64 frequency[],
 float64 externalAttenuation[],
 int32 arraySize);

#### Purpose

Stores the external attenuation table in the calibration plane specified by the **selectorString** parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. 

 
If there is only one table configured in any calibration plane, it is automatically selected as the active table. 

 
**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |  |
| tableName | char[] | Specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. example:"""table1" |
| frequency | float64[] | Specifies an array of frequencies in the external attenuation table. This value is expressed in Hz. |
| externalAttenuation | float64[] | Specifies an array of attenuations corresponding to the frequency specified by the frequency parameter. This value is expressed in dB. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_cfgfrequencyreference.html language=enus -->
## TOPIC 00005: RFmxInstr_CfgFrequencyReference

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_cfgfrequencyreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_cfgfrequencyreference.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgFrequencyReference

int32 __stdcall RFmxInstr_CfgFrequencyReference (niRFmxInstrHandle instrumentHandle, char channelName[], 
 char frequencyReferenceSource[],
 float64 frequencyReferenceFrequency);

#### Purpose

Configures the Reference Clock and the frequency reference source.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| channelName | char[] | Specifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter. |
| frequencyReferenceSource | char[] | Specifies the frequency reference source. RFMXINSTR_VAL_ONBOARD_CLOCK_STR (OnboardClock) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the PXIe-5860 onboard cloc RFMXINSTR_VAL_REF_IN_STR (RefIn) PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5840 with PXIe-5653: Lock onto the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use RFMXINSTR_VAL_REF_IN_STR for PXIe-5840 or RefIn2 for the PXIe-5840 with the PXIe-5653. PXIe-5831 with PXIe-5653: Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5840 with PXIe-5653: Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. RFMXINSTR_VAL_PXI_CLK_STR(PXI_Clk) PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842: Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the PXI backplane clock. RFMXINSTR_VAL_CLK_IN_STR (ClkIn) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN/OUT connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. RFMXINSTR_VAL_REF2_IN_STR (RefIn2) Configure open NI-RFSG sessions to the device to use RFMXINSTR_VAL_REF_IN_STR for the PXIe-5840 or RFMXINSTR_VAL_ONBOARD_CLOCK_STR for the PXIe-5840 with PXIe-5653.This configuration does not apply for PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. RFMXINSTR_VAL_PXI_CLKMASTER_IN_STR (PXI_ClkMaster) PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 with PXIe-3622 to use RFMXINSTR_VAL_PXI_CLK_STR as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 with PXIe-3623 to use RFMXINSTR_VAL_PXI_CLK_STR as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |
| RFMXINSTR_VAL_ONBOARD_CLOCK_STR (OnboardClock) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the PXIe-5860 onboard cloc |  |
| RFMXINSTR_VAL_REF_IN_STR (RefIn) | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5840 with PXIe-5653: Lock onto the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use RFMXINSTR_VAL_REF_IN_STR for PXIe-5840 or RefIn2 for the PXIe-5840 with the PXIe-5653. PXIe-5831 with PXIe-5653: Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5840 with PXIe-5653: Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. |  |
| RFMXINSTR_VAL_PXI_CLK_STR(PXI_Clk) | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842: Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the PXI backplane clock. |  |
| RFMXINSTR_VAL_CLK_IN_STR (ClkIn) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN/OUT connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. |  |
| RFMXINSTR_VAL_REF2_IN_STR (RefIn2) | Configure open NI-RFSG sessions to the device to use RFMXINSTR_VAL_REF_IN_STR for the PXIe-5840 or RFMXINSTR_VAL_ONBOARD_CLOCK_STR for the PXIe-5840 with PXIe-5653.This configuration does not apply for PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. |  |
| RFMXINSTR_VAL_PXI_CLKMASTER_IN_STR (PXI_ClkMaster) | PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 with PXIe-3622 to use RFMXINSTR_VAL_PXI_CLK_STR as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 with PXIe-3623 to use RFMXINSTR_VAL_PXI_CLK_STR as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |  |
| frequencyReferenceFrequency | float64 | Specifies the Reference Clock rate when you set the frequencyReferenceSource parameter to RFMXINSTR_VAL_CLK_IN_STR or RFMXINSTR_VAL_REF_IN_STR. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_cfgmechanicalattenuation.html language=enus -->
## TOPIC 00006: RFmxInstr_CfgMechanicalAttenuation

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_cfgmechanicalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_cfgmechanicalattenuation.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgMechanicalAttenuation

int32 __stdcall RFmxInstr_CfgMechanicalAttenuation (niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue);

#### Purpose

Configures the mechanical attenuation and RFmx attenuation hardware settings. 
 
Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| channelName | char[] | Specifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter. |
| mechanicalAttenuationAuto | int32 | Specifies whether RFmx chooses an attenuation setting based on the hardware settings. RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) Specifies that RFmx uses the value configured in the mechanicalAttenuationValue parameter. RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) Specifies that the measurement computes the mechanical attenuation. |
| RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that RFmx uses the value configured in the mechanicalAttenuationValue parameter. |  |
| RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |
| mechanicalAttenuationValue | float64 | Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_cfgrfattenuation.html language=enus -->
## TOPIC 00007: RFmxInstr_CfgRFAttenuation

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_cfgrfattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_cfgrfattenuation.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgRFAttenuation

int32 __stdcall RFmxInstr_CfgRFAttenuation (niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto,
 float64 rfAttenuationValue);

#### Purpose

Configures the nominal attenuation and RFmx attenuation hardware settings. 
 
Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| channelName | char[] | Specifies the channel to which the settings must be applied. Specify an empty string as the value of this parameter. |
| rfAttenuationAuto | int32 | Specifies whether RFmx computes the RF attenuation. If you set this parameter to True, RFmx automatically chooses an attenuation setting based on the reference level configured on the personality. RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE (0) Specifies that RFmx uses the value configured using the rfAttenuationValue parameter. RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE (1) Specifies that RFmx computes the RF attenuation. |
| RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that RFmx uses the value configured using the rfAttenuationValue parameter. |  |
| RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that RFmx computes the RF attenuation. |  |
| rfAttenuationValue | float64 | Specifies the nominal attenuation setting for all attenuators that are present before the first mixer in the RF signal chain. This value is expressed in dB. If you set the RF Attenuation Auto parameter to True, RFmx chooses an attenuation setting automatically. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_cfgsparameterexternalattenuationtable.html language=enus -->
## TOPIC 00008: RFmxInstr_CfgSParameterExternalAttenuationTable

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_cfgsparameterexternalattenuationtable.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_cfgsparameterexternalattenuationtable.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgSParameterExternalAttenuationTable

int32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationTable(
 niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char tableName[],
 float64 frequency[],
 int32 frequencyArraySize,
 NIComplexDouble sParameters[],
 int32 sParameterTableSize,
 int32 numberOfPorts,
 int32 sParameterOrientation
 );

#### Purpose

Stores the S-parameter table in the calibration plane specified by the **Selector String** parameter. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane.

Supported devices

|  | Note If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |  |
| tableName | char[] | Specifies the name to be associated with the S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table. Example: "" "table1" |
| frequency | float64[] | Specifies an array of frequencies in the S-parameter table. This value is expressed in Hz. |
| frequencyArraySize | int32 | Specifies the size of the frequency array. |
| sParameters | NIComplexDouble[] | Specifies the S-parameters for each frequency. The first index indicates the corresponding frequency entry, the second index corresponds to the target port for the S-parameter, and the third index corresponds to the the source port. For example, to index the s21 parameter for the fourth frequency in the table, you would use {3, 1, 0} as the indexes since they are zero-based. |
| sParameterTableSize | int32 | Specifies the size of the S-parameter table. |
| numberOfPorts | int32 | Specifies the number of ports. |
| sParameterOrientation | int32 | Specifies the orientation of the data in the S-parameter table relative to the port you specify. |

| RFMXINSTR_VAL_PORT1_TOWARDS_DUT (0) | Port 1 of the S2P is oriented towards the DUT. |
| --- | --- |
| RFMXINSTR_VAL_PORT2_TOWARDS_DUT (1) | Port 2 of the S2P is oriented towards the DUT. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_cfgsparameterexternalattenuationtype.html language=enus -->
## TOPIC 00009: RFmxInstr_CfgSParameterExternalAttenuationType

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_cfgsparameterexternalattenuationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_cfgsparameterexternalattenuationtype.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgSParameterExternalAttenuationType

int32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationType (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sParameterType);

#### Purpose

Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the selector String input to specify the name of the Calplane and port to configure for S-parameter. 
**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which either S-parameter or external attenuation is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |  |
| sParameterType | int32 | Specifies the type of S-parameter which applies to measurements on the specified port for a Calplane. If you set this parameter to RFMXINSTR_VAL_SPARAMETER_TYPE_SCALAR or RFMXINSTR_VAL_SPARAMETER_TYPE_VECTOR, RFmx adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT. PXIe-5831/5832: Valid values for this parameter are RFMXINSTR_VAL_SPARAMETER_TYPE_SCALAR and RFMXINSTR_VAL_SPARAMETER_TYPE_VECTOR. RFMXINSTR_VAL_SPARAMETER_TYPE_VECTOR is only supported for TRX ports in a semiconductor test system (STS). PXIe-5840/5841/5842/5860: The only valid value for this parameter is RFMXINSTR_VAL_SPARAMETER_TYPE_SCALAR. RFMXINSTR_VAL_SPARAMETER_TYPE_SCALAR (1) De-embeds the measurement using the gain term. RFMXINSTR_VAL_SPARAMETER_TYPE_VECTOR (2) De-embeds the measurement using the gain term and the reflection term. |
| RFMXINSTR_VAL_SPARAMETER_TYPE_SCALAR (1) | De-embeds the measurement using the gain term. |  |
| RFMXINSTR_VAL_SPARAMETER_TYPE_VECTOR (2) | De-embeds the measurement using the gain term and the reflection term. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_checkacquisitionstatus.html language=enus -->
## TOPIC 00010: RFmxInstr_CheckAcquisitionStatus

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_checkacquisitionstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_checkacquisitionstatus.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CheckAcquisitionStatus

int32 __stdcall RFmxInstr_CheckAcquisitionStatus (niRFmxInstrHandle instrumentHandle,
 int32* acquisitionDone);

#### Purpose

Checks the status of the acquisition. Use this function to check for any errors that may occur during acquisition, or to check whether RFmx has completed the acquisition operation.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| Output |  |  |
| Name | Type | Description |
| acquisitionDone | int32* | Indicates whether the acquisition is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_checkiflistexists.html language=enus -->
## TOPIC 00011: RFmxInstr_CheckIfListExists

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_checkiflistexists.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_checkiflistexists.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CheckIfListExists

int32 __stdcall RFmxInstr_CheckIfListExists (niRFmxInstrHandle instrumentHandle,
 char listName[],
 int32* listExists,
 int32* personality);

#### Purpose

Returns whether the list you specify in the **listName** parameter exists, and also returns the corresponding personality of the list, if the list exists. This function does not support an empty ("") list name.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| listName | char[] | Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. example:"list::samplelist1""samplelist1" |
| Output |  |  |
| Name | Type | Description |
| listExists | int32* | Indicates whether the list exists or not. FALSE Indicates that the list does not exist. TRUE Indicates that the list exists. |
| FALSE | Indicates that the list does not exist. |  |
| TRUE | Indicates that the list exists. |  |
| personality | int32* | Indicates the personality of the list if the list exists. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_disablecalibrationplane.html language=enus -->
## TOPIC 00012: RFmxInstr_DisableCalibrationPlane

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_disablecalibrationplane.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_disablecalibrationplane.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_DisableCalibrationPlane

int32 __stdcall RFmxInstr_DisableCalibrationPlane (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Disables the calibration plane specified by the **selectorString** parameter for amplitude correction. 
**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. If you specify "calplane::all", all the calibration planes are disabled.example:"""calplane::plane0""calplane::all" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_enablecalibrationplane.html language=enus -->
## TOPIC 00013: RFmxInstr_EnableCalibrationPlane

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_enablecalibrationplane.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_enablecalibrationplane.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_EnableCalibrationPlane

int32 __stdcall RFmxInstr_EnableCalibrationPlane (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Enables the calibration plane specified by the **selectorString** parameter for amplitude correction. 
**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which the external attenuation table or S-parameter is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. If "calplane::all" is specified, all the calibration planes are enabled.example:"""calplane::plane0""calplane::all" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_getattributef64.html language=enus -->
## TOPIC 00014: RFmxInstr_GetAttributeF64

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_getattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_getattributef64.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeF64

int32 __stdcall RFmxInstr_GetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_getattributei16.html language=enus -->
## TOPIC 00015: RFmxInstr_GetAttributeI16

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_getattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_getattributei16.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeI16

int32 __stdcall RFmxInstr_GetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_getattributei32.html language=enus -->
## TOPIC 00016: RFmxInstr_GetAttributeI32

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_getattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_getattributei32.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeI32

int32 __stdcall RFmxInstr_GetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_getattributei32array.html language=enus -->
## TOPIC 00017: RFmxInstr_GetAttributeI32Array

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_getattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_getattributei32array.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeI32Array

int32 __stdcall RFmxInstr_GetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int32 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00018: RFmxInstr_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_getattributenicomplexdoublearray.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxInstr_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexDouble attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | NIComplexDouble[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=cvirfmxinstr_getattributenicomplexsinglearray.html language=enus -->
## TOPIC 00019: RFmxInstr_GetAttributeNIComplexSingleArray

- bundle_id: `rfmx-instr-cvi`
- source_path: `cvirfmxinstr_getattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/cvirfmxinstr_getattributenicomplexsinglearray.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeNIComplexSingleArray

int32 __stdcall RFmxInstr_GetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexSingle attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | NIComplexSingle[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_device_temperature.html language=enus -->
## TOPIC 00020: RFMXINSTR_ATTR_DEVICE_TEMPERATURE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_device_temperature.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_device_temperature.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DEVICE_TEMPERATURE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the current temperature of the module. This value is expressed in degrees Celsius. To use this attribute for PXIe-5830/5831/5832, you must first use the Selector string attribute to specify the name of the channel you are configuring. When you are reading the device temperature, you must specify the context in the Selector String input as 'module::(ModuleName)'. You can also use the RFmxInstr_BuildModuleString function to build the module string. For all other devices, the only valid value for the selector string is '' (empty string). On a MIMO session, use 'port::(deviceName)/(channelNumber)' as the selector string to read this attribute. You can use the RFmxInstr_BuildPortString2 function to build the selector string. For PXIe-5830/5831/5832, you must specify the context in the selector string input as port::(deviceName)/(channelNumber)/module::(moduleName). Refer to the following table to determine which strings are valid for your configuration. Hardware ModuleTRX Port TypeSelector StringPXIe-3621/3622/3623-if or '' (empty string)PXIe-5820-fpgaFirst connected mmRH-5582DIRECT TRX PORTS Onlyrf0SWITCHED TRX PORTS [0-7]rf0switch0SWITCHED TRX PORTS [8-15]rf0switch1Second connected mmRH-5582DIRECT TRX PORTS Onlyrf1SWITCHED TRX PORTS [0-7]rf1switch0SWITCHED TRX PORTS [8-15]rf1switch1 Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetDeviceTemperature |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_digital_gain.html language=enus -->
## TOPIC 00021: RFMXINSTR_ATTR_DIGITAL_GAIN

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_digital_gain.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_digital_gain.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DIGITAL_GAIN

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. RFmx does not compensate for the specified digital gain. You can use this property to account for external gain changes without changing the analog signal path. The PXIe-5644/5645/5646 applies this gain when the data is scaled. The raw data does not include this scaling on these devices. The default value is 0 dB. Supported devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5860 Get Function: RFmxInstr_GetDigitalGain Set Function: RFmxInstr_SetDigitalGain |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_digitizer_dither_enabled.html language=enus -->
## TOPIC 00022: RFMXINSTR_ATTR_DIGITIZER_DITHER_ENABLED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_digitizer_dither_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_digitizer_dither_enabled.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DIGITIZER_DITHER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether dithering is enabled on the digitizer. Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the ADC and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies of up to approximately 12 MHz. PXIe-5663/5663E/5665: When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled. For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When performing spectral measurements, this leakage can also appear as a wide, low-amplitude signal near the 12.5 MHz and 62.5 MHz frequencies. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT. PXIe-5668: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power level with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax.For PXIe-5820/5830/5831/5832/5840/5841/5842, only Enabled is supported. Note For the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy. The default value is RFMXINSTR_VAL_DIGITIZER_DITHER_ENABLED. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetDigitizerDitherEnabled Set Function: RFmxInstr_SetDigitizerDitherEnabled |
| Values: | RFMXINSTR_VAL_DIGITIZER_DITHER_DISABLED (0)Disables the attribute. RFMXINSTR_VAL_DIGITIZER_DITHER_ENABLED (1)Enables the attribute. |
| RFMXINSTR_VAL_DIGITIZER_DITHER_DISABLED (0) | Disables the attribute. |
| RFMXINSTR_VAL_DIGITIZER_DITHER_ENABLED (1) | Enables the attribute. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_digitizer_temperature.html language=enus -->
## TOPIC 00023: RFMXINSTR_ATTR_DIGITIZER_TEMPERATURE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_digitizer_temperature.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_digitizer_temperature.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DIGITIZER_TEMPERATURE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the current temperature of the digitizer module. This value is expressed in degrees Celsius. On a MIMO session, use 'port::(deviceName)/(channelNumber)' as the Selector string to read this attribute. You can use the RFmxInstr_BuildPortString2 function to build the selector string.This attribute is not supported if you are using an external digitizer. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842/5860 Get Function: RFmxInstr_GetDigitizerTemperature |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_done_event_output_terminal.html language=enus -->
## TOPIC 00024: RFMXINSTR_ATTR_DONE_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_done_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_done_event_output_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DONE_EVENT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the Done event. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetDoneEventOutputTerminal Set Function: RFmxInstr_SetDoneEventOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_done_event_terminal_name.html language=enus -->
## TOPIC 00025: RFMXINSTR_ATTR_DONE_EVENT_TERMINAL_NAME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_done_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_done_event_terminal_name.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DONE_EVENT_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/DoneEvent, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/DoneEvent, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/DoneEvent, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. PXIe-5860: /ModuleName/ai/ChannelNumber/DoneEvent, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetDoneEventTerminalName |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_downconverter_center_frequency.html language=enus -->
## TOPIC 00026: RFMXINSTR_ATTR_DOWNCONVERTER_CENTER_FREQUENCY

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_downconverter_center_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_downconverter_center_frequency.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DOWNCONVERTER_CENTER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. After you set this attribute, the RF downconverter is locked to that frequency until the value is changed or the attribute is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured without the overhead of retuning the LO and waiting for the LO to settle. This method is called in-band retuning and it has the highest benefit on analyzers that have larger LO settling times. After setting the downconverter center frequency, you can set the center frequency to the frequencies at which you want to take the measurements. If you want to avoid the LO leakage or DC offset of analyzers that use a direct conversion architecture, it is more convenient to use the RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET or RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attributes.If you set this attribute, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset this attribute or call the RFmxInstr_ResettoDefault function.This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is the carrier frequency or spectrum center frequency. Valid Values: Any supported tuning frequency of the device. PXIe-5820: The only valid value for this attribute is 0 Hz. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetDownconverterCenterFrequency Set Function: RFmxInstr_SetDownconverterCenterFrequency |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_downconverter_frequency_offset.html language=enus -->
## TOPIC 00027: RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_downconverter_frequency_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_downconverter_frequency_offset.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies an offset from the center frequency value for the downconverter. Use this attribute to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this attribute to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. NI recommends using the RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attribute instead of the Downconverter Frequency Offset attribute. The RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attribute automatically configures the Downconverter Frequency Offset attribute to an appropriate offset based on the bandwidth or span of the measurement.This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Default values: For spectrum acquisition types, RFmx automatically calculates the default value to avoid residual LO power. For I/Q acquisition types, the default value is 0 Hz. If the center frequency is set to a non-multiple of LO Frequency Step Size attribute, this attribute is set to compensate for the difference.The following valid values correspond to their respective devices: PXIe-5646-100 MHz to +100 MHz PXIe-5830/5831/5832/5840/5841-500 MHz to +500 MHz PXIe-5842-1 GHz to +1 GHz Other devices-42 MHz to +42 MHz Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetDownconverterFrequencyOffset Set Function: RFmxInstr_SetDownconverterFrequencyOffset |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_downconverter_gain.html language=enus -->
## TOPIC 00028: RFMXINSTR_ATTR_DOWNCONVERTER_GAIN

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_downconverter_gain.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_downconverter_gain.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DOWNCONVERTER_GAIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this attribute. For a vector signal analyzer (VSA), the system is defined as the RF downconverter for all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel. This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is N/A. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetDownconverterGain |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_downconverter_preselector_enabled.html language=enus -->
## TOPIC 00029: RFMXINSTR_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_downconverter_preselector_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_downconverter_preselector_enabled.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether the tunable preselector is enabled on the downconverter. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_DISABLED. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetDownconverterPreselectorEnabled Set Function: RFmxInstr_SetDownconverterPreselectorEnabled |
| Values: | RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_DISABLED (0)Disables the preselector. RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_ENABLED (1)The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the RFMXINSTR_ATTR_PRESELECTOR_PRESENT attribute to determine if the downconverter has a preselector. |
| RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_DISABLED (0) | Disables the preselector. |
| RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_ENABLED (1) | The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the RFMXINSTR_ATTR_PRESELECTOR_PRESENT attribute to determine if the downconverter has a preselector. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_end_of_record_event_output_terminal.html language=enus -->
## TOPIC 00030: RFMXINSTR_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_end_of_record_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_end_of_record_event_output_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the End of Record event. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetEndOfRecordEventOutputTerminal Set Function: RFmxInstr_SetEndOfRecordEventOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_end_of_record_event_terminal_name.html language=enus -->
## TOPIC 00031: RFMXINSTR_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_end_of_record_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_end_of_record_event_terminal_name.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/EndOfRecordEvent, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/EndOfRecordEvent, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/EndOfRecordEvent, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. PXIe-5860: /ModuleName/ai/ChannelNumber/EndOfRecordEvent, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetEndOfRecordEventTerminalName |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_fft_width.html language=enus -->
## TOPIC 00032: RFMXINSTR_ATTR_FFT_WIDTH

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_fft_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_fft_width.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FFT_WIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. The lower limit for all devices that support setting the RFMXINSTR_ATTR_FFT_WIDTH attribute is 7.325 kHz. PXIe-5663/5663E: The FFT width upper limit for the PXIe-5663/5663E depends on the RF frequency and on the module revision of the PXIe-5601. For more information about determining which revision of the PXIe-5601 RF downconverter you have installed, refer to the Identifying Module Revision topic in the NI RF Vector Signal Analyzers Help. The maximum FFT width for your device is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. You can use the RFMXINSTR_ATTR_FFT_WIDTH attribute with in-band retuning. For more information about in-band retuning, refer to the Downconverter Center Frequency attribute. RFmx treats the device instantaneous bandwidth as the effective real-time bandwidth of the signal path. The span specifies the frequency range of the computed spectrum. A signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth. If the span you choose is greater than the device instantaneous bandwidth, RFmx obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Supported devices: PXIe-5663/5663E/5665, PXIe-5668 Get Function: RFmxInstr_GetFFTWidth Set Function: RFmxInstr_SetFFTWidth |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_frequency_reference_exported_terminal.html language=enus -->
## TOPIC 00033: RFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_frequency_reference_exported_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_frequency_reference_exported_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies a comma-separated list of the terminals at which to export the frequency reference. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_NONE_STR. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetFrequencyReferenceExportedTerminal Set Function: RFmxInstr_SetFrequencyReferenceExportedTerminal |
| Values: | RFMXINSTR_VAL_NONE_STR ()The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. RFMXINSTR_VAL_REF_OUT_STR (RefOut)Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2)Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut)Export the Reference Clock on the CLK OUT terminal on the Digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_NONE_STR () | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Export the Reference Clock on the CLK OUT terminal on the Digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_frequency_reference_frequency.html language=enus -->
## TOPIC 00034: RFMXINSTR_ATTR_FREQUENCY_REFERENCE_FREQUENCY

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_frequency_reference_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_frequency_reference_frequency.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FREQUENCY_REFERENCE_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the Reference Clock rate, when the Frequency Reference Source attribute is set to ClkIn or RefIn. This value is expressed in Hz. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 10 MHz. Valid values PXIe-5644/5645/5646, PXIe-5663/5663E, PXIe-5820/5830/5831/5832/5840/5841/5842 10 MHz PXIe-5665/5668 5 MHz to 100 MHz (inclusive), in increments of 1 MHz PXIe-5860 10 MHz , 100 MHz Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetFrequencyReferenceFrequency Set Function: RFmxInstr_SetFrequencyReferenceFrequency |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_frequency_reference_source.html language=enus -->
## TOPIC 00035: RFMXINSTR_ATTR_FREQUENCY_REFERENCE_SOURCE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_frequency_reference_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_frequency_reference_source.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FREQUENCY_REFERENCE_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the frequency reference source. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. All other devices default value is OnboardClock. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetFrequencyReferenceSource Set Function: RFmxInstr_SetFrequencyReferenceSource |
| Values: | RFMXINSTR_VAL_ONBOARD_CLOCK_STR (OnboardClock) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860: Lock to the PXIe-5860 onboard clock. RFMXINSTR_VAL_REF_IN_STR (RefIn)PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency attribute according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency attribute according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860: Lock to the signal at the REF IN connector on the PXIe-5860. RFMXINSTR_VAL_PXI_CLK_STR (PXI_Clk)PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5860: The RFmx driver locks the device to the PXI backplane clock. PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842/5860: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. RFMXINSTR_VAL_CLK_IN_STR (ClkIn)PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency attribute to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency attribute to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840/5860 with PXIe-5653: This configuration does not apply. RFMXINSTR_VAL_PXI_CLK_MASTER_STR (PXI_ClkMaster)PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5840 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clk. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |
| RFMXINSTR_VAL_ONBOARD_CLOCK_STR (OnboardClock) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860: Lock to the PXIe-5860 onboard clock. |
| RFMXINSTR_VAL_REF_IN_STR (RefIn) | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency attribute according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency attribute according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860: Lock to the signal at the REF IN connector on the PXIe-5860. |
| RFMXINSTR_VAL_PXI_CLK_STR (PXI_Clk) | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5860: The RFmx driver locks the device to the PXI backplane clock. PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842/5860: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| RFMXINSTR_VAL_CLK_IN_STR (ClkIn) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency attribute to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency attribute to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840/5860 with PXIe-5653: This configuration does not apply. |
| RFMXINSTR_VAL_PXI_CLK_MASTER_STR (PXI_ClkMaster) | PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5840 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clk. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_frequency_settling.html language=enus -->
## TOPIC 00036: RFMXINSTR_ATTR_FREQUENCY_SETTLING

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_frequency_settling.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_frequency_settling.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FREQUENCY_SETTLING

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the Frequency Settling Units attribute. Valid valuesYou do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax.Frequency Settling Units Attribute Value PXIe-5663/5663E PXIe-5665/5668 PXIe-5644/5645/5646 PXIe-5830/5831/5832/5840/5841/5842/5860, PXIe-5831 with PXIe-5653 (using PXIe-3622 LO), PXIe-5832 with PXIe-5653 (using PXIe-3623 LO) PXIe-5831 with PXIe-5653 (using PXIe-5653 LO) and PXIe-5832 with PXIe-5653 (using PXIe-5653 LO) Seconds After Lock 2 Âµs to 80 ms, resolution of approximately 2 Âµs 4 Âµs to 80 ms, resolution of approximately 4 Âµs 1 Âµs to 65 ms, resolution of 1 Âµs 1 Âµs to 10s, resolution of 1 Âµs 4 Âµs to 80 ms, resolution of approximately 4 Âµs Seconds After I/O 0 Âµs to 80 ms, resolution of 1 Âµs 0 Âµs to 80 ms, resolution of 1 Âµs 1 Âµs to 65 ms, resolution of 1 Âµs 0 Âµs to 10s, resolution of 1 Âµs 0 Âµs to 80 ms, resolution of 1 Âµs PPM 1.0, 0.1, 0.01 1.0, 0.1, 0.01, 0.001 1.0, 0.1, 0.01 1.0 to 0.01 1.0 to 0.01 Note This attribute is not supported if you are using an external LO. The default value is 0.1. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetFrequencySettling Set Function: RFmxInstr_SetFrequencySettling |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_frequency_settling_units.html language=enus -->
## TOPIC 00037: RFMXINSTR_ATTR_FREQUENCY_SETTLING_UNITS

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_frequency_settling_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_frequency_settling_units.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FREQUENCY_SETTLING_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies the delay duration units and interpretation for LO settling. Specify the actual settling value using the Frequency Settling attribute. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Note The Frequency Settling Units attribute is not supported if you are using an external LO. The default value is RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_PPM. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetFrequencySettlingUnits Set Function: RFmxInstr_SetFrequencySettlingUnits |
| Values: | RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_PPM (0)Specifies the frequency settling in parts per million (ppm). RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_SECONDS_AFTER_LOCK (1)Specifies the frequency settling in time after lock (seconds). RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_SECONDS_AFTER_IO (2)Specifies the frequency settling in time after I/O (seconds). |
| RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_PPM (0) | Specifies the frequency settling in parts per million (ppm). |
| RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_SECONDS_AFTER_LOCK (1) | Specifies the frequency settling in time after lock (seconds). |
| RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_SECONDS_AFTER_IO (2) | Specifies the frequency settling in time after I/O (seconds). |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_if_filter_bandwidth.html language=enus -->
## TOPIC 00038: RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_if_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_if_filter_bandwidth.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the IF filter path bandwidth for your device configuration. RFmx chooses an appropriate IF filter as default IF Filter based on measurement configuration, center frequency, cleaner spectrum and downconverter preselector.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Note For composite devices, such as the PXIe-5665/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device. Supported devices: PXIe-5665/5668 Get Function: RFmxInstr_GetIFFilterBandwidth Set Function: RFmxInstr_SetIFFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_if_output_power_level_offset.html language=enus -->
## TOPIC 00039: RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_if_output_power_level_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_if_output_power_level_offset.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the power offset by which to adjust the default IF output power level. This value is expressed in dB. This attribute does not depend on absolute IF output power levels; therefore, you can use this attribute to adjust the IF output power level on all RFmx-supported devices without knowing the exact default value. Use this attribute to increase or decrease the nominal output level to achieve better measurement results.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 0. Supported devices: PXIe-5663/5663E/5665, PXIe-5668 Get Function: RFmxInstr_GetIFOutputPowerLevelOffset Set Function: RFmxInstr_SetIFOutputPowerLevelOffset |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_input_isolation_enabled.html language=enus -->
## TOPIC 00040: RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_input_isolation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_input_isolation_enabled.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether input isolation is enabled. Enabling this attribute isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this attribute reintegrates the input signal into the RF downconverter signal path. If you enable input isolation for your device, the device impedance is changed from the characteristic 50-ohm impedance. A change in the device impedance may increase the VSWR value higher than the device specifications. For PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_INPUT_ISOLATION_DISABLED. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetInputIsolationEnabled Set Function: RFmxInstr_SetInputIsolationEnabled |
| Values: | RFMXINSTR_VAL_INPUT_ISOLATION_DISABLED (0)Indicates that the attribute is disabled. RFMXINSTR_VAL_INPUT_ISOLATION_ENABLED (1)Indicates that the attribute is enabled. |
| RFMXINSTR_VAL_INPUT_ISOLATION_DISABLED (0) | Indicates that the attribute is disabled. |
| RFMXINSTR_VAL_INPUT_ISOLATION_ENABLED (1) | Indicates that the attribute is enabled. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_instrument_firmware_revision.html language=enus -->
## TOPIC 00041: RFMXINSTR_ATTR_INSTRUMENT_FIRMWARE_REVISION

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_instrument_firmware_revision.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_instrument_firmware_revision.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_INSTRUMENT_FIRMWARE_REVISION

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. On a MIMO session, use 'port::(deviceName)/(channelNumber)' as the Selector string to read this attribute. You can use the RFmxInstr_BuildPortString2 function to build the selector string. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetInstrumentFirmwareRevision |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_instrument_model.html language=enus -->
## TOPIC 00042: RFMXINSTR_ATTR_INSTRUMENT_MODEL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_instrument_model.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_instrument_model.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_INSTRUMENT_MODEL

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns a string that contains the model number or name of the RF device that you are currently using. On a MIMO session, use 'port::(deviceName)/(channelNumber)' as the Selector string to read this attribute. You can use the RFmxInstr_BuildPortString2 function to build the selector string. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetInstrumentModel |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo2_export_enabled.html language=enus -->
## TOPIC 00043: RFMXINSTR_ATTR_LO2_EXPORT_ENABLED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo2_export_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo2_export_enabled.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO2_EXPORT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether to enable the LO2 OUT terminals in the installed devices. Set this attribute to Enabled to export the 4 GHz LO signal from the LO2 IN terminal to the LO2 OUT terminal. You can also export the LO2 signal by setting the RFMXINSTR_ATTR_LO_EXPORT_ENABLED attribute to TRUE. This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_LO2_EXPORT_DISABLED. Supported Devices: PXIe-5665/5668 Get Function: RFmxInstr_GetLO2ExportEnabled Set Function: RFmxInstr_SetLO2ExportEnabled |
| Values: | RFMXINSTR_VAL_LO2_EXPORT_DISABLED (0)Disables the LO2 OUT terminals. RFMXINSTR_VAL_LO2_EXPORT_ENABLED (1)Enables the LO2 OUT terminals. |
| RFMXINSTR_VAL_LO2_EXPORT_DISABLED (0) | Disables the LO2 OUT terminals. |
| RFMXINSTR_VAL_LO2_EXPORT_ENABLED (1) | Enables the LO2 OUT terminals. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_export_enabled.html language=enus -->
## TOPIC 00044: RFMXINSTR_ATTR_LO_EXPORT_ENABLED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_export_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_export_enabled.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_EXPORT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether to enable the LO OUT terminals on the installed devices. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.This attribute is not supported on a MIMO session.You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector string topic for information about the string syntax.TRUE Enables the LO OUT terminals. FALSE Disables the LO OUT terminals Default value:PXIe-5663/5663E: TRUE PXIe-5644/5645/5646, PXIe-5665/5668, PXIe-5830/5831/5832/5840/5841/5842: FALSE Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOExportEnabled Set Function: RFmxInstr_SetLOExportEnabled |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_frequency.html language=enus -->
## TOPIC 00045: RFMXINSTR_ATTR_LO_FREQUENCY

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_frequency.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz. If you are using the vector signal analyzer with an external LO, use this attribute to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this attribute after configuring the rest of the parameters returns the LO frequency needed by the device. You can set this attribute to the actual LO frequency because RFmx corrects for any difference between expected and actual LO frequencies. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.This attribute is not supported on a MIMO session. You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 0. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOFrequency Set Function: RFmxInstr_SetLOFrequency |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_frequency_step_size.html language=enus -->
## TOPIC 00046: RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_frequency_step_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_frequency_step_size.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the step size for tuning the LO phase-locked loop (PLL). You can only tune the LO frequency in multiples of the LO Frequency Step Size attribute. Therefore, the LO frequency can be offset from the requested center frequency by as much as half of the LO Frequency Step Size attribute. This offset is corrected by digitally frequency shifting the LO frequency to the value requested in Downconverter Center Frequency attribute. For PXIe-5831 with PXIe-5653, PXIe-5832 with PXIe-5653, this attribute is ignored if PXIe-5653 is used as the LO source. The valid values for this attribute depend on the RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute. PXIe-5644/5645/5646: If you set the RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute to RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED, the specified value is coerced to the nearest valid value. PXIe-5840: If you set the RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute to RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size. This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED Attribute Setting LO Frequency Step Size Attribute Valid Values on PXIe-5644/5645 LO Frequency Step Size Attribute Valid Values on PXIe-5646 LO Frequency Step Size Attribute Valid Values on PXIe-5840/5841 LO Frequency Step Size Attribute Valid Values on PXIe-5830/5831/5832 LO Frequency Step Size Property Valid Values on PXIe-5841 with PXIe-5655, PXIe-5842* LO1 LO2 Enabled 50 kHz to 24 MHz 50 kHz to 25 MHz 50 kHz to 100 MHz 8 Hz to 400 MHz 4 kHz to 400 MHz 1 nHz to 50 MHz Disabled 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz 2 MHz, 5 MHz, 10 MHz, 25 MHz 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz -- -- Default valuesPXIe-5644/5645/5646200 kHzPXIe-58302 MHz PXIe-5831/5832 (RF port)8 MHz PXIe-5831/5832 (IF port)2 MHz, 4 MHzPXIe-5840/5841500 kHzPXIe-58421 HzThe default value for PXIe-5831/5832 depends on the frequency range of the selected port for your instrument configuration. Use RFmxInstr Get Available Ports function to get the valid port names. Supported devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOFrequencyStepSize Set Function: RFmxInstr_SetLOFrequencyStepSize |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_leakage_avoidance_enabled.html language=enus -->
## TOPIC 00047: RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_leakage_avoidance_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_leakage_avoidance_enabled.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. This attribute is ignored if: the bandwidth required by the measurement is more than the available instrument bandwidth after offsetting the LO. You set the Downconverter Center Frequency or Downconverter Frequency Offset attributes. When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set this attribute to False when the LO Source attribute is set to Automatic_SG_SA_Shared. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value for PXIe-5830/5831/5832/5840/5841/5842 is True, else the default value is False. Supported devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOLeakageAvoidanceEnabled Set Function: RFmxInstr_SetLOLeakageAvoidanceEnabled |
| Values: | RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_FALSE (0)RFmx does not modify the Downconverter Frequency Offset attribute. RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_TRUE (1)RFmx calculates the required LO offset based on the measurement configuration and appropriately sets the Downconverter Frequency Offset attribute. |
| RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_FALSE (0) | RFmx does not modify the Downconverter Frequency Offset attribute. |
| RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_TRUE (1) | RFmx calculates the required LO offset based on the measurement configuration and appropriately sets the Downconverter Frequency Offset attribute. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_pll_fractional_mode.html language=enus -->
## TOPIC 00048: RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_pll_fractional_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_pll_fractional_mode.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether to use fractional mode for the LO phase-locked loop (PLL). Fractional mode provides a finer frequency step resolution, but may result in non harmonic spurs. Refer to the specifications document of your device for more information about fractional mode and non harmonic spurs. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.This attribute is not supported on a MIMO session. You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector string topic for information about the string syntax. The RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute is applicable only when using the internal LO. For PXIe-5831 with PXIe-5653, PXIe-5832 with PXIe-5653, this attribute is ignored if the PXIe-5653 is used as the LO source. The default value is RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_ENABLED. Supported devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOPLLFractionalMode Set Function: RFmxInstr_SetLOPLLFractionalMode |
| Values: | RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED (0)Indicates that the attribute is disabled. RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_ENABLED (1)Indicates that the attribute is enabled. |
| RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED (0) | Indicates that the attribute is disabled. |
| RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_ENABLED (1) | Indicates that the attribute is enabled. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_sharing_mode.html language=enus -->
## TOPIC 00049: RFMXINSTR_ATTR_LO_SHARING_MODE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_sharing_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_sharing_mode.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_SHARING_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies the RFmx session with the respective LO sharing mode. The following figures illustrate different connection configuration topologies for different LO Sharing modes. You must set the RFMXINSTR_ATTR_NUMBER_OF_LO_SHARING_GROUPS attribute to 1 for the following LO connection configurations. You must set the RFMXINSTR_ATTR_NUMBER_OF_LO_SHARING_GROUPS attribute to 2 for the following LO connection configurations. The default value is RFMXINSTR_VAL_LO_SHARING_MODE_DISABLED. Get Function: RFmxInstr_GetLOSharingMode Set Function: RFmxInstr_SetLOSharingMode |
| Values: | RFMXINSTR_VAL_LO_SHARING_MODE_DISABLED (0)LO Sharing is disabled. RFMXINSTR_VAL_LO_SHARING_MODE_ONBOARD_STAR (1)The LO connection configuration is configured as Onboard Star. RFMXINSTR_VAL_LO_SHARING_MODE_ONBOARD_DAISY_CHAIN (2)The LO connection configuration is configured as Onboard Daisy Chain. RFMXINSTR_VAL_LO_SHARING_MODE_EXTERNAL_STAR (3)The LO connection configuration is configured as External Star. RFMXINSTR_VAL_LO_SHARING_MODE_EXTERNAL_DAISY_CHAIN (4)The LO connection configuration is configured as External Daisy Chain. |
| RFMXINSTR_VAL_LO_SHARING_MODE_DISABLED (0) | LO Sharing is disabled. |
| RFMXINSTR_VAL_LO_SHARING_MODE_ONBOARD_STAR (1) | The LO connection configuration is configured as Onboard Star. |
| RFMXINSTR_VAL_LO_SHARING_MODE_ONBOARD_DAISY_CHAIN (2) | The LO connection configuration is configured as Onboard Daisy Chain. |
| RFMXINSTR_VAL_LO_SHARING_MODE_EXTERNAL_STAR (3) | The LO connection configuration is configured as External Star. |
| RFMXINSTR_VAL_LO_SHARING_MODE_EXTERNAL_DAISY_CHAIN (4) | The LO connection configuration is configured as External Daisy Chain. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_source.html language=enus -->
## TOPIC 00050: RFMXINSTR_ATTR_LO_SOURCE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_source.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the local oscillator (LO) signal source used to downconvert the RF input signal. If this attribute is set to '' (empty string), RFmx uses the internal LO source. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.If no signal downconversion is required, this attribute is ignored.This attribute is not supported on a MIMO session.You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector string topic for information about the string syntax. The default value is RFMXINSTR_VAL_LO_SOURCE_ONBOARD. Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOSource Set Function: RFmxInstr_SetLOSource |
| Values: | RFMXINSTR_VAL_LO_SOURCE_NONE (None)Specifies that no LO source is required to downconvert the RF input signal. RFMXINSTR_VAL_LO_SOURCE_ONBOARD (Onboard)Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. RFMXINSTR_VAL_LO_SOURCE_LO_IN (LO_In)Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. RFMXINSTR_VAL_LO_SOURCE_SECONDARY (Secondary)Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), or PXIe-5832 with PXIe-5653 (LO1 stage only). RFMXINSTR_VAL_LO_SOURCE_SG_SA_SHARED (SG_SA_Shared)Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on PXIe-5830/5831/5832/5841/5842. RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED (Automatic_SG_SA_Shared)Specifies whether RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings.configures instrument specific attributes on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: 1. Set LO Source attribute to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library) 2. Set RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED in RFmx 3. Configure any additional settings on RFSG and RFmx, including selecting waveforms 4. Initiate RFSG 5. Initiate RFmx. Note: When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attribute to RFMXINSTR_VAL_FALSE and RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED. Refer to following functions for examples in RFmx WLAN and RFmx NR that show the behavior of Automatic SG SA Shared LO. (LabVIEW directory)\\examples\\RFmx\\WLAN\\RFmxWLAN FEM Test with Automatic SG SA Shared LO.vi(LabVIEW directory)\\examples\\RFmx\\NR\\RFmxNR FEM Test with Automatic SG SA Shared LO.vi This value is valid only on PXIe-5830/5831/5832/5840/5841/5842. |
| RFMXINSTR_VAL_LO_SOURCE_NONE (None) | Specifies that no LO source is required to downconvert the RF input signal. |
| RFMXINSTR_VAL_LO_SOURCE_ONBOARD (Onboard) | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. |
| RFMXINSTR_VAL_LO_SOURCE_LO_IN (LO_In) | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
| RFMXINSTR_VAL_LO_SOURCE_SECONDARY (Secondary) | Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), or PXIe-5832 with PXIe-5653 (LO1 stage only). |
| RFMXINSTR_VAL_LO_SOURCE_SG_SA_SHARED (SG_SA_Shared) | Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on PXIe-5830/5831/5832/5841/5842. |
| RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED (Automatic_SG_SA_Shared) | Specifies whether RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings.configures instrument specific attributes on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: 1. Set LO Source attribute to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library) 2. Set RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED in RFmx 3. Configure any additional settings on RFSG and RFmx, including selecting waveforms 4. Initiate RFSG 5. Initiate RFmx. Note: When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attribute to RFMXINSTR_VAL_FALSE and RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED. Refer to following functions for examples in RFmx WLAN and RFmx NR that show the behavior of Automatic SG SA Shared LO. (LabVIEW directory)\\examples\\RFmx\\WLAN\\RFmxWLAN FEM Test with Automatic SG SA Shared LO.vi(LabVIEW directory)\\examples\\RFmx\\NR\\RFmxNR FEM Test with Automatic SG SA Shared LO.vi This value is valid only on PXIe-5830/5831/5832/5840/5841/5842. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_temperature.html language=enus -->
## TOPIC 00051: RFMXINSTR_ATTR_LO_TEMPERATURE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_temperature.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_temperature.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_TEMPERATURE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. On a MIMO session, use 'port::(deviceName)/(channelNumber)' as the Selector string to read this attribute. You can use the RFmxInstr_BuildPortString2 function to build the selector string.This attribute is not supported if you are using an external LO. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5840/5841/5842 Get Function: RFmxInstr_GetLOTemperature |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_lo_vco_frequency_step_size.html language=enus -->
## TOPIC 00052: RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_lo_vco_frequency_step_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_lo_vco_frequency_step_size.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. Do not set this attribute with the LO Frequency Step Size attribute. This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 1 MHz. Supported devices: PXIe-5830/5831/5832 Get Function: RFmxInstr_GetLOVCOFrequencyStepSize Set Function: RFmxInstr_SetLOVCOFrequencyStepSize |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_load_options.html language=enus -->
## TOPIC 00053: RFMXINSTR_ATTR_LOAD_OPTIONS

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_load_options.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_load_options.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LOAD_OPTIONS

| Data Type: | int32 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the configurations to skip while loading from a file using the RFmxInstr_LoadConfigurations. The default value is an empty array. Get Function: RFmxInstr_GetLoadOptions Set Function: RFmxInstr_SetLoadOptions |
| Values: | RFMXINSTR_VAL_LOAD_OPTIONS_SKIP_NONE (0)RFmx loads all the configurations to the session. RFMXINSTR_VAL__LOAD_OPTIONS_SKIP_RFINSTR (1)RFmx skips loading the RFmxInstr configurations to the session. |
| RFMXINSTR_VAL_LOAD_OPTIONS_SKIP_NONE (0) | RFmx loads all the configurations to the session. |
| RFMXINSTR_VAL__LOAD_OPTIONS_SKIP_RFINSTR (1) | RFmx skips loading the RFmxInstr configurations to the session. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_ready_for_reference_event_output_terminal.html language=enus -->
## TOPIC 00054: RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_ready_for_reference_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_ready_for_reference_event_output_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the Ready for Reference event. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetReadyForReferenceEventOutputTerminal Set Function: RFmxInstr_SetReadyForReferenceEventOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_ready_for_reference_event_terminal_name.html language=enus -->
## TOPIC 00055: RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_ready_for_reference_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_ready_for_reference_event_terminal_name.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForReferenceEvent, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForReferenceEvent, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/ReadyForReferenceEvent, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. PXIe-5860: /ModuleName/ai/ChannelNumber/ReadyForReferenceEvent, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetReadyForReferenceEventTerminalName |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_ready_for_start_event_output_terminal.html language=enus -->
## TOPIC 00056: RFMXINSTR_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_ready_for_start_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_ready_for_start_event_output_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the Ready for Start event. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetReadyForStartEventOutputTerminal Set Function: RFmxInstr_SetReadyForStartEventOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_ready_for_start_event_terminal_name.html language=enus -->
## TOPIC 00057: RFMXINSTR_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_ready_for_start_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_ready_for_start_event_terminal_name.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForStartEvent, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForStartEvent, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/ReadyForStartEvent, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. PXIe-5860: /ModuleName/ai/ChannelNumber/ReadyForStartEvent, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetReadyForStartEventTerminalName |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_acquisition_type.html language=enus -->
## TOPIC 00058: RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_acquisition_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_acquisition_type.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeI32 |
| Description: | Returns the recommended acquisition type for the last committed measurement configuration. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedAcquisitionType |
| Values: | RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ (0)Indicates that the recommended acquisition type is I/Q. Use the Analyze (IQ) function to perform the measurement. RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_SPECTRAL (1)Indicates that the recommended acquisition type is Spectral. Use Analyze (Spectrum) function to perform the measurement. RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ_OR_SPECTRAL (2)Indicates that the recommended acquisition type is I/Q or Spectral. Use either Analyze (IQ) or Analyze (Spectrum) function to perform the measurement. |
| RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ (0) | Indicates that the recommended acquisition type is I/Q. Use the Analyze (IQ) function to perform the measurement. |
| RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_SPECTRAL (1) | Indicates that the recommended acquisition type is Spectral. Use Analyze (Spectrum) function to perform the measurement. |
| RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ_OR_SPECTRAL (2) | Indicates that the recommended acquisition type is I/Q or Spectral. Use either Analyze (IQ) or Analyze (Spectrum) function to perform the measurement. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_iq_pre_trigger_time.html language=enus -->
## TOPIC 00059: RFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_iq_pre_trigger_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_iq_pre_trigger_time.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended pretrigger time for I/Q acquisition. This value is expressed in seconds. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedIQPreTriggerTime |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_number_of_records.html language=enus -->
## TOPIC 00060: RFMXINSTR_ATTR_RECOMMENDED_NUMBER_OF_RECORDS

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_number_of_records.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_number_of_records.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_NUMBER_OF_RECORDS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeI32 |
| Description: | Returns the recommended number of records to acquire to complete measurement averaging. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedNumberOfRecords |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_spectral_acquisition_span.html language=enus -->
## TOPIC 00061: RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_ACQUISITION_SPAN

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_spectral_acquisition_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_spectral_acquisition_span.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_ACQUISITION_SPAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended acquisition span for spectral acquisition. This value is expressed in Hz. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedSpectralAcquisitionSpan |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_spectral_fft_window.html language=enus -->
## TOPIC 00062: RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOW

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_spectral_fft_window.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_spectral_fft_window.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOW

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeI32 |
| Description: | Returns the recommended FFT window type for spectral acquisition. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedSpectralFFTWindow |
| Values: | RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_NONE (0)Indicates that the measurement does not use FFT windowing to reduce spectral leakage. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_FLAT_TOP (1)Indicates a Flat Top FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HANNING (2)Indicates a Hanning FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HAMMING (3)Indicates a Hamming FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_GAUSSIAN (4)Indicates a Gaussian FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN (5)Indicates a Blackman FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN_HARRIS (6)Indicates a Blackman-Harris FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_KAISER_BESSEL (7)Indicates a Kaiser-Bessel FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_NONE (0) | Indicates that the measurement does not use FFT windowing to reduce spectral leakage. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_FLAT_TOP (1) | Indicates a Flat Top FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HANNING (2) | Indicates a Hanning FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HAMMING (3) | Indicates a Hamming FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_GAUSSIAN (4) | Indicates a Gaussian FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN (5) | Indicates a Blackman FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN_HARRIS (6) | Indicates a Blackman-Harris FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_KAISER_BESSEL (7) | Indicates a Kaiser-Bessel FFT window type. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_spectral_resolution_bandwidth.html language=enus -->
## TOPIC 00063: RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_spectral_resolution_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_spectral_resolution_bandwidth.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedSpectralResolutionBandwidth |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_recommended_trigger_minimum_quiet_time.html language=enus -->
## TOPIC 00064: RFMXINSTR_ATTR_RECOMMENDED_TRIGGER_MINIMUM_QUIET_TIME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_recommended_trigger_minimum_quiet_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_recommended_trigger_minimum_quiet_time.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_TRIGGER_MINIMUM_QUIET_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedTriggerMinimumQuietTime |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_rf_attenuation_auto.html language=enus -->
## TOPIC 00065: RFMXINSTR_ATTR_RF_ATTENUATION_AUTO

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_rf_attenuation_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_rf_attenuation_auto.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RF_ATTENUATION_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether RFmx computes the RF attenuation. If you set this attribute to True, RFmx chooses an attenuation setting based on the reference level configured on the personality. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE. Supported devices: PXIe-5663/5663E, PXIe-5665/5668 Get Function: RFmxInstr_GetRFAttenuationAuto Set Function: RFmxInstr_SetRFAttenuationAuto |
| Values: | RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that RFmx uses the value configured using RF Attenuation Value attribute. RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that RFmx computes the RF attenuation. |
| RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that RFmx uses the value configured using RF Attenuation Value attribute. |
| RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that RFmx computes the RF attenuation. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_rf_attenuation_step_size.html language=enus -->
## TOPIC 00066: RFMXINSTR_ATTR_RF_ATTENUATION_STEP_SIZE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_rf_attenuation_step_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_rf_attenuation_step_size.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RF_ATTENUATION_STEP_SIZE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Default values: PXIe-5601/5663/5663E0.0PXIe-5603/5665 (3.6 GHz)1.0PXIe-5605/5665 (14 GHz), PXIe-5606/56685.0 Valid values: PXIe-5601/5663/5663E0.0 to 93.0, continuousPXIe-5603/5665 (3.6 GHz)1.0 to 74.0, in 1 dB stepsPXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band)1.0 to 106.0, in 1 dB stepsPXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (high band)5.0 to 75.0, in 5 dB steps Supported devices: PXIe-5663, PXIe-5665, PXIe-5668 Get Function: RFmxInstr_GetRFAttenuationStepSize Set Function: RFmxInstr_SetRFAttenuationStepSize |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_rf_attenuation_value.html language=enus -->
## TOPIC 00067: RFMXINSTR_ATTR_RF_ATTENUATION_VALUE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_rf_attenuation_value.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_rf_attenuation_value.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RF_ATTENUATION_VALUE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. RFmx uses the value of this attribute as the attenuation setting when you set the RFMXINSTR_ATTR_RF_ATTENUATION_AUTO attribute to RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax.PXIe-5663/5663E You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level but decreases distortion; lower attenuation levels decrease the noise level but increases distortion. PXIe-5603/5605/5665/5668 Refer to the PXIe-5665 or the PXIe-5668 RF Attenuation and Signal Levels topic in the NI RF Vector Signal Analyzers Help for more information about configuring attenuation. The valid values for this attribute depend on the device configuration. Supported devices: PXIe-5663/5663E/5603/5605/5665/5668 Get Function: RFmxInstr_GetRFAttenuationValue Set Function: RFmxInstr_SetRFAttenuationValue |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_rf_highpass_filter_frequency.html language=enus -->
## TOPIC 00068: RFMXINSTR_ATTR_RF_HIGHPASS_FILTER_FREQUENCY

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_rf_highpass_filter_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_rf_highpass_filter_frequency.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RF_HIGHPASS_FILTER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly. For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this attribute returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 0.The valid values range from 0 to 26.5. Supported devices: PXIe-5668 Get Function: RFmxInstr_GetRFHighpassFilterFrequency Set Function: RFmxInstr_SetRFHighpassFilterFrequency |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_start_trigger_digital_edge.html language=enus -->
## TOPIC 00069: RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_start_trigger_digital_edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_start_trigger_digital_edge.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies the active edge for the start trigger. This attribute is used only when you set the RFMXINSTR_ATTR_START_TRIGGER_TYPE attribute to RFMXINSTR_VAL_START_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_RISING_EDGE. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetStartTriggerDigitalEdge Set Function: RFmxInstr_SetStartTriggerDigitalEdge |
| Values: | RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_RISING_EDGE (0) The trigger asserts on the rising edge of the signal. RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_FALLING_EDGE (1) The trigger asserts on the falling edge of the signal. |
| RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the signal. |
| RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the signal. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_start_trigger_digital_edge_source.html language=enus -->
## TOPIC 00070: RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_start_trigger_digital_edge_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_start_trigger_digital_edge_source.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the source terminal for the start trigger. This attribute is used only when you set the RFMXINSTR_ATTR_START_TRIGGER_TYPE attribute to RFMXINSTR_VAL_START_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value of this attribute is '' (empty string). Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetStartTriggerDigitalEdgeSource Set Function: RFmxInstr_SetStartTriggerDigitalEdgeSource |
| Values: | RFMXINSTR_VAL_PFI0_STR (PFI0) The trigger is received on PFI 0. RFMXINSTR_VAL_PFI1_STR (PFI1) The trigger is received on PFI 1. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) The trigger is received on PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) The trigger is received on PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) The trigger is received on PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) The trigger is received on PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) The trigger is received on PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) The trigger is received on PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) The trigger is received on PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) The trigger is received on PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARB_STR (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_TIMER_EVENT (TimerEvent) The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | The trigger is received on PFI 0. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | The trigger is received on PFI 1. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARB_STR (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_TIMER_EVENT (TimerEvent) | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_start_trigger_export_output_terminal.html language=enus -->
## TOPIC 00071: RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_start_trigger_export_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_start_trigger_export_output_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the exported start trigger. You can also choose not to export any signal. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetStartTriggerExportOutputTerminal Set Function: RFmxInstr_SetStartTriggerExportOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_start_trigger_terminal_name.html language=enus -->
## TOPIC 00072: RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_start_trigger_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_start_trigger_terminal_name.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/StartTrigger, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/StartTrigger, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/StartTrigger, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. PXIe-5860: /ModuleName/ai/ChannelNumber/StartTrigge, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetStartTriggerTerminalName |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_start_trigger_type.html language=enus -->
## TOPIC 00073: RFMXINSTR_ATTR_START_TRIGGER_TYPE

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_start_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_start_trigger_type.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether the start trigger is a digital edge or a software trigger. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_START_TRIGGER_TYPE_NONE. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetStartTriggerType Set Function: RFmxInstr_SetStartTriggerType |
| Values: | RFMXINSTR_VAL_START_TRIGGER_TYPE_NONE (0) No start trigger is configured. RFMXINSTR_VAL_START_TRIGGER_TYPE_DIGITAL_EDGE (1) The start trigger is not asserted until a digital edge is detected. The source of the digital edge is specified by the RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCE attribute. RFMXINSTR_VAL_START_TRIGGER_TYPE_SOFTWARE (3) The start trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr_SendSoftwareEdgeTrigger function. |
| RFMXINSTR_VAL_START_TRIGGER_TYPE_NONE (0) | No start trigger is configured. |
| RFMXINSTR_VAL_START_TRIGGER_TYPE_DIGITAL_EDGE (1) | The start trigger is not asserted until a digital edge is detected. The source of the digital edge is specified by the RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCE attribute. |
| RFMXINSTR_VAL_START_TRIGGER_TYPE_SOFTWARE (3) | The start trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr_SendSoftwareEdgeTrigger function. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_thermal_correction_temperature_resolution.html language=enus -->
## TOPIC 00074: RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_thermal_correction_temperature_resolution.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_thermal_correction_temperature_resolution.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Default valuePXIe-5830/5831/5832/5842/5860 0.2 PXIe-5840/5841 1.0 Supported devices: PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetThermalCorrectionTemperatureResolution Set Function: RFmxInstr_SetThermalCorrectionTemperatureResolution |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_trigger_export_output_terminal.html language=enus -->
## TOPIC 00075: RFMXINSTR_ATTR_TRIGGER_EXPORT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_trigger_export_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_trigger_export_output_terminal.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_TRIGGER_EXPORT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646 and PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxInstr_GetTriggerExportOutputTerminal Set Function: RFmxInstr_SetTriggerExportOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR ()Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists on only PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0)Exports the signal to the PFI 0 connector on PXIe-5142 and PXIe-5624. RFMXINSTR_VAL_PFI1_STR (PFI1)Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0)Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1)Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2)Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3)Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4)Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5)Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6)Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7)Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR)Exports the signal to the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid on only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists on only PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector on PXIe-5142 and PXIe-5624. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid on only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_trigger_terminal_name.html language=enus -->
## TOPIC 00076: RFMXINSTR_ATTR_TRIGGER_TERMINAL_NAME

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_trigger_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_trigger_terminal_name.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_TRIGGER_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. This attribute is not supported on a MIMO session. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/RefTrigger, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/RefTrigger, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/RefTrigger, where DigitizerName is the name of your associated digitizer module in MAX.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. PXIe-5860:/ModuleName/ai/ChannelNumber/RefTrigger, where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1). Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetTriggerTerminalName |

<!--NI_TOPIC bundle=rfmx-instr-cvi path=rfmxinstr_attr_tuning_speed.html language=enus -->
## TOPIC 00077: RFMXINSTR_ATTR_TUNING_SPEED

- bundle_id: `rfmx-instr-cvi`
- source_path: `rfmxinstr_attr_tuning_speed.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-cvi/raw/resource/enus/rfmxinstr_attr_tuning_speed.html
- document_id: `rfmx-instr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_TUNING_SPEED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Makes tradeoffs between tuning speed and phase noise. This attribute is not supported if you are using an external LO. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed. This attribute is not supported on a MIMO session.You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector string topic for information about the string syntax.The PXIe-5830/5831/5832/5840/5841/5842 supports only Medium for this attribute. Default value: Normal for PXIe-5663/5663E/5665/5668, Medium for PXIe-5644/5645/5646 and PXIe-5830/5831/5832/5840/5841/5842 Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetTuningSpeed Set Function: RFmxInstr_SetTuningSpeed |
| Values: | RFMXINSTR_VAL_TUNING_SPEED_NORMAL (0)PXIe-5665/5668: Adjusts the YIG main coil on the LO for an underdamped response. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a narrow loop bandwidth. RFMXINSTR_VAL_TUNING_SPEED_MEDIUM (1)Specifies that the RF downconverter module uses a medium loop bandwidth. This value is not supported on PXIe-5663/5663E/5665/5668 devices. RFMXINSTR_VAL_TUNING_SPEED_FAST (2)PXIe-5665/5668: Adjusts the YIG main coil on the LO for an overdamped response. Setting this attribute to Fast allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a wide loop bandwidth. |
| RFMXINSTR_VAL_TUNING_SPEED_NORMAL (0) | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an underdamped response. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a narrow loop bandwidth. |
| RFMXINSTR_VAL_TUNING_SPEED_MEDIUM (1) | Specifies that the RF downconverter module uses a medium loop bandwidth. This value is not supported on PXIe-5663/5663E/5665/5668 devices. |
| RFMXINSTR_VAL_TUNING_SPEED_FAST (2) | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an overdamped response. Setting this attribute to Fast allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a wide loop bandwidth. |
