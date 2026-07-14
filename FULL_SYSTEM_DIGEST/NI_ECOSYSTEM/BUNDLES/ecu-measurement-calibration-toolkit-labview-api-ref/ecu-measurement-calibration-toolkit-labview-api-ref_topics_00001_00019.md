# NI DOCUMENT BUNDLE: ecu-measurement-calibration-toolkit-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ecu-measurement-calibration-toolkit-labview-api-ref start=1 end=19 -->
<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-get-property-vi.html language=enus -->
## TOPIC 00001: MC Get Property.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-get-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-get-property-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Gets a property for the object referenced by the reference in terminal. The poly VI selection determines the property to get. Format Input Name specifies an individual channel within the task defined by reference in. The default (unwired) value of name is empty, which means the property appl

### MC Get Property.vi

**Purpose**

Gets a property for the object referenced by the **reference in** terminal. The poly VI selection determines the property to get.

Format

[IMAGE alt='image' src='images/getproperty.gif']

Input

|  | Name specifies an individual channel within the task defined by reference in. The default (unwired) value of name is empty, which means the property applies to the entire task, not a specific channel. If a property relates to Measurement or Characteristic channels and does not apply to the entire task, but an individual channel or message within the task, you must wire the name of a Measurement or Characteristic channel from channel list into the name input. For other properties you must leave name unwired (empty). |
| --- | --- |
|  | Reference in is the reference to any opened A2L database, a selected ECU, or an ECU which is already connected (with MC Database Open.vi, MC ECU Select.vi, MC ECU Open.vi, or MC ECU Connect.vi). The type of this reference depends on the property you want to get. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | Reference out contains an ECU M&C task reference which can be wired through subsequent ECU M&C VIs. |
| --- | --- |
|  | Value is a poly output value that returns the property value. You select the property returned in value by selecting the poly VI type. The data type of value is also determined by the poly VI selection. For information about the different properties provided by MC Get Property.vi, refer to the Poly VI Types table in the Description section. To select the property, right-click the VI, go to Select Type, and select the property by name. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

#### Poly VI Types

| Type | Hierarchy | Sub-Hierarchy | Parameter | Description | Details |
| --- | --- | --- | --- | --- | --- |
|  | — | — | — | DB File Name | Returns the A2L Database file name with which the task has been opened. The value of this property cannot be changed using MC Set Property.vi. |

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-measurement-create-vi.html language=enus -->
## TOPIC 00002: MC Measurement Create.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-measurement-create-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-measurement-create-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates a Measurement object in memory. Format Input Conversion Name identifies the referred conversion object defined by MC Conversion Create.vi. Measurement Name sets the Measurement object name. ECU ref in is the task reference that links to the selected ECU. This reference is originally

### MC Measurement Create.vi

**Purpose**

Creates a Measurement object in memory.

**Format**

[IMAGE alt='image' src='images/MCMeasurementCreate.gif']

**Input**

|  | Conversion Name identifies the referred conversion object defined by MC Conversion Create.vi. |
| --- | --- |
|  | Measurement Name sets the Measurement object name. |
|  | ECU ref in is the task reference that links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Create.vi. |
|  | Address is a cluster that contains the following values: Address specifies the address part of the source address.Extension contains the extension part of the source address. |
|  | Address specifies the address part of the source address. |
|  | Extension contains the extension part of the source address. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | Data Type sets the measurement task data type. Data Type can contain the following values: Data TypeData Format0Unsigned byte1Signed byte2Unsigned word3Signed word4Unsigned long5Signed long6Float 32 |
| Data Type | Data Format |
| 0 | Unsigned byte |
| 1 | Signed byte |
| 2 | Unsigned word |
| 3 | Signed word |
| 4 | Unsigned long |
| 5 | Signed long |
| 6 | Float 32 |

**Output**

|  | ECU ref out is the task reference that links to the selected ECU. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

Use **MC Measurement Create.vi** to create a measurement object in memory instead of referring to a predefined measurement in the A2L database.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-measurement-read-vi.html language=enus -->
## TOPIC 00003: MC Measurement Read.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-measurement-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-measurement-read-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads a single Measurement value from the ECU. Format Input Measurement name is the name of a measurement channel stored in the A2L database file you want to read. ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or M

### MC Measurement Read.vi

**Purpose**

Reads a single Measurement value from the ECU.

**Format**

[IMAGE alt='image' src='images/measurementread.gif']

**Input**

|  | Measurement name is the name of a measurement channel stored in the A2L database file you want to read. |
| --- | --- |
|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Value returns a single sample for the Measurement channel initialized in Measurement name. The type of the poly output is determined by the poly VI selection. For information on the different poly VI types provided by MC Measurement Read.vi, refer to the Poly VI Types table in the Description section. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC Measurement Read.vi** performs a single point read of a measurement variable without opening a DAQ task.

#### Poly VI Types

| VI Type | Description |
| --- | --- |
| Parameter (Dbl) | Returns a single scaled double value for the selected Characteristic name. |
| Parameter (Raw) | Returns a single unscaled unsigned 64-bit integer value for the selected Characteristic name. |

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-measurement-write-vi.html language=enus -->
## TOPIC 00004: MC Measurement Write.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-measurement-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-measurement-write-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes a single Measurement value to the ECU. Format Input Measurement name is the name of a Measurement channel stored in the A2L database file to which to write a Measurement value. ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from

### MC Measurement Write.vi

**Purpose**

Writes a single Measurement value to the ECU.

**Format**

[IMAGE alt='image' src='images/measurementwrite.gif']

**Input**

|  | Measurement name is the name of a Measurement channel stored in the A2L database file to which to write a Measurement value. |
| --- | --- |
|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
|  | Value writes a single sample for the Measurement channel initialized in Measurement name. The type of the poly input is determined by the poly VI selection. For information on the different poly VI types provided by MC Measurement Write.vi, refer to the Poly VI Types table in the Description section. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC Measurement Write.vi** performs a single point write of a measurement variable without opening a DAQ task. **MC Measurement Write.vi** can only be performed if the Measurement is not set to **read only**. To query if an ECU Measurement channel can be accessed by **MC Measurement Write.vi**, first call [MC Get Property.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetpropertyvi) with the parameter **Measurement/Read Only?**.

#### Poly VI Types

| VI Type | Description |
| --- | --- |
| Parameter (Dbl) | Writes a single scaled double value to the selected Characteristic name. |
| Parameter (Raw) | Writes a single unscaled unsigned 64-bit integer value to the selected Characteristic name. |

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-program-reset-vi.html language=enus -->
## TOPIC 00005: MC Program Reset.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-program-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-program-reset-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Indicates the end of a programming sequence. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Error in is a cluster which describes error condit

### MC Program Reset.vi

**Purpose**

Indicates the end of a programming sequence.

**Format**

[IMAGE alt='image' src='images/ProgramReset.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

If you are using the XCP protocol, **MC Program Reset .vi** implements the XCP command PROGRAM_RESET. This optional command indicates the end of a non-volatile memory programming sequence and may or may not have a response from the ECU. In either case, the slave device will go into a disconnected state.

**MC Program Reset .vi** may be used to reset a slave device for other purposes. For further information on how to use program ECU memory and to use the **MC Program Reset .vi** command refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-program-start-vi.html language=enus -->
## TOPIC 00006: MC Program Start.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-program-start-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-program-start-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Indicates the start of a programming sequence. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Error in is a cluster which describes error cond

### MC Program Start.vi

**Purpose**

Indicates the start of a programming sequence.

**Format**

[IMAGE alt='image' src='images/XCPProgramStart.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

If you are using the XCP protocol, **MC Program Start.vi** implements the XCP command PROGRAM_START. This optional command indicates the beginning of a programming sequence into a non-volatile memory area. If the slave device is not in a state which permits programming, an error is returned. The memory programming commands The end of a non-volatile memory programming sequence is indicated by using the **MC Program Start.vi** function.

For further information on how to use program ECU memory and to use the **MC Program Start.vi** command refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-program-vi.html language=enus -->
## TOPIC 00007: MC Program.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-program-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-program-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Programs a memory block on the ECU. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Address is a cluster which contains the following values. A

### MC Program.vi

**Purpose**

Programs a memory block on the ECU.

**Format**

[IMAGE alt='image' src='images/Program.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Address is a cluster which contains the following values. Address specifies the address part of the destination address.Extension contains the extension part of the destination address. |
|  | Address specifies the address part of the destination address. |
|  | Extension contains the extension part of the destination address. |
|  | Data contains the byte array to be transmitted to the ECU. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

If you are using the CCP protocol, **MC Program.vi** implements the CCP command PROGRAM. The command is used to program the specified data into nonvolatile ECU memory (Flash, EEPROM, etc.). Programming starts at the selected MTA0 address and extension defined in the **Address** cluster.

If you are using the XCP protocol, **MC Program.vi** implements the XCP command PROGRAM. The command is used to program a non-volatile memory segment in the ECU slave. The end of the programming sequence is indicated by using the [MC Program Reset .vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramresetvi) command which executes the XCP command PROGRAM_RESET. The slave device will move into a disconnected state. Usually a hardware reset of the slave device is executed. This command may support block transfer similar to the commands DOWNLOAD and DOWNLOAD_NEXT.

For further information on how to use the **MC Program.vi** and details on block mode transfers, refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-set-property-vi.html language=enus -->
## TOPIC 00008: MC Set Property.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-set-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-set-property-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets a property for the specified A2L database file, Measurement Task or Characteristic referenced by the reference in terminal. The poly VI selection determines the property to set. Format Input Name is not used, and can be left unwired. This parameter may be used for further extensions. Re

### MC Set Property.vi

**Purpose**

Sets a property for the specified A2L database file, Measurement Task or Characteristic referenced by the **reference in** terminal. The poly VI selection determines the property to set.
Format

[IMAGE alt='image' src='images/setproperty.gif']

**Input**

|  | Name is not used, and can be left unwired. This parameter may be used for further extensions. |
| --- | --- |
|  | Reference in specifies a valid task handle depending on the information which has to be set. If a generic property has to be set, a db ref handle is needed. If a Measurement property has to be set, a valid DAQ ref handle has to be wired into reference in. If an ECU property has to be set, a valid ECU ref handle has to be wired into reference in. |
|  | Value is a poly output value that specifies the property value. You select the property to set as value by selecting the poly VI type. The data type of value is also determined by the poly VI selection. For information about the different properties provided by MC Set Property.vi, refer to the Poly VI Types section. To select the property, right-click the VI, go to Select Type, and select the property by name. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | Reference out is a copy of the reference in terminal which can be wired through subsequent ECU M&C VIs. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

There are four types of properties which can be modified in the poly input value: ECU-specific properties, DAQ-specific properties, Characteristic-specific properties, and Measurement-specific properties.

#### ECU-Specific Properties

ECU-specific properties relate to the setting of the ECU. If you need to change a property of the ECU you need a valid ECU reference, but the ECU should not be connected. First, call [MC ECU Open.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuopenvi), followed by **MC Set Property.vi** and then [MC ECU Connect.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnectvi). If you have already connected to the ECU, you can change an ECU property by calling [MC ECU Disconnect.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecudisconnectvi), followed by **MC Set Property.vi**, and then [MC ECU Connect.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnectvi) again. Refer to the ECU-Specific Properties table below for a list of ECU-specific properties that can be used to define the poly input **value**.

#### DAQ-Specific Properties

You cannot set a property while the task is running. If you need to change a property prior to starting the task, call [MC DAQ Initialize.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializevi), followed by **MC Set Property.vi** and then [MC DAQ Start Stop.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstopvi). After you start the task, you also can change a property by calling [MC DAQ Start Stop.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstopvi), followed by **MC Set Property.vi**, and then restart the task with [MC DAQ Start Stop.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstopvi). Refer to the DAQ-specific Properties table for a list of DAQ-specific properties that can be used to define the poly input **value**.

#### Poly VI Types

#### ECU-Specific Properties

| Type | Hierarchy | Sub-Hierarchy | Parameter | Description | Notes |
| --- | --- | --- | --- | --- | --- |
|  | ECU | CCP | — | CRO Id | Sets the CRO ID, which is used to send commands and data from the host to the slave device. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
|  | ECU | CCP | — | Baud Rate | Sets the Baud Rate used by the CAN interface with CCP protocol. This property applies to all tasks initialized with the Interface. You can specify the following basic baud rates as the numeric rate: 33333, 83333, 100000, 125000, 200000, 250000, 400000, 500000, 800000, and 1000000. You also can specify advanced (custom) baud rates depending on the interface type. Refer to the NI-XNET or NI-CAN Help for more information. |
|  | ECU | CCP | — | Termination | For all XNET devices, the termination is software selectable. XNET provides the option of 120 Ω between Bus Plus and Bus Minus or no termination. The Termination property configures the onboard termination of the NI-XNET interface CAN connector (port). The Boolean property supports two values: TRUE = Termination ON and FALSE = Termination Off. However, different CAN or LIN hardware has different termination requirements, and the termination values have different meanings. Refer to the Termination attribute in the XNET API for more details. (This property is supported for NI-XNET devices only.) |
|  | ECU | CCP | — | Station Address | Sets the Station Address of the slave device. CCP is based on the idea that several ECUs can share the same CAN Arbitration IDs for CCP communication. To avoid communication conflicts, CCP defines a Station Address that has to be unique for all ECUs sharing the same CAN Arbitration IDs. Unless an ECU has been addressed by its Station Address, the ECU must not react to CCP commands sent by the CCP master. |
|  | ECU | CCP | — | SeedKey Cal Name | Sets the filename of the SeedKey DLL used for Calibration purposes. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
|  | ECU | CCP | — | SeedKey DAQ Name | Sets the filename of the SeedKey DLL used for DAQ purposes. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
|  | ECU | CCP | — | SeedKey Prog Name | Sets the filename of the SeedKey DLL used for programming purposes. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
|  | ECU | CCP | — | DTO Id | Sets the DTO ID, which is the CAN identifier for the Data Transmission Object (DTO). The DTO is used by the CCP slave devices to return data and status information to the application. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
|  | ECU | CCP | — | Master Id | Sets the identifier of the CCP master that is used by the CCP command EXCHANGE_ID as a parameter. This ID information is optional and specific to the ECU implementation. For more information about the CCP master ID, refer to the documentation for the ECU. |
|  | ECU | CCP | — | Single Byte DAQ List? | Sets the ECU to support single-byte or multi-byte DAQ list entries. |

#### Measurement-Specific Properties

| Type | Hierarchy | Sub-Hierarchy | Parameter | Description | Notes |
| --- | --- | --- | --- | --- | --- |
|  | Measurement | — | — | Byte Order | Sets the specified byte order of the selected Measurement: 0—Intel format Bytes are in little-endian order, with least-significant bit first. 1—Motorola format Bytes are in big-endian order, with most-significant bit first. |

#### Characteristic-Specific Properties

| Type | Hierarchy | Sub-Hierarchy | Parameter | Description | Notes |
| --- | --- | --- | --- | --- | --- |
|  | Characteristic | — | — | Byte Order | Sets the specified byte order of the entire Characteristic: 0—Intel format Bytes are in little-endian order, with least-significant bit first. 1—Motorola format Bytes are in big-endian order, with most-significant bit first. |
|  | Characteristic | — | — | X Axis | Sets the X-axis values on which the Characteristic is defined. The Characteristic dimension must be at least 1. |
|  | Characteristic | — | — | Y Axis | Sets the Y-axis values on which the Characteristic is defined. The Characteristic dimension must be 2. |

#### DAQ-Specific Properties

| Type | Hierarchy | Sub-Hierarchy | Parameter | Description | Notes |
| --- | --- | --- | --- | --- | --- |
|  | DAQ | — | — | Mode | Sets the selected I/O mode for the M&C Measurement task. 0—DAQ List The data is transmitted from the ECU in equidistant time intervals as defined in the A2L database. The data can be read back with the MC DAQ Read.vi as Single point data using sample rate = 0, or as a waveform using a sample rate > 0. Input channel data is received from the DAQ messages. Use MC DAQ Read.vi to obtain input samples as single-point, array, or waveform. 1—Polling In this mode the data from the Measurement task is uploaded from the ECU whenever MC DAQ Read.vi is called. |
|  | DAQ | — | — | SampleRate | SampleRate specifies the timing to use for the samples of the (NI-CAN) task. The sample rate is specified in Hertz (samples per second). A sample rate of zero means to sample immediately. For a DAQMode of mcDAQModeDAQList, SampleRate of zero means that MC DAQ Read.vi returns a single sample from the most recent messages received, and greater than zero means that MC DAQ Read.vi returns samples timed at the specified rate. For DAQMode of mcDAQModePolling, SampleRate is ignored. |
|  | DAQ | — | — | Event Channel Name | Sets the event channel name to which the Measurement task is assigned. If there is no event channel name defined in the A2L file, you can set the Event Channel Number manually by passing a decimal number as a string. |
|  | DAQ | — | — | Prescaler | Sets the prescaling factor, which reduces the desired transmission frequency of the associated DAQ list. |
|  | DAQ | CCP | — | DTO Id | Sets the DTO ID, which is used by the ECU to send DAQ list data to the CCP master. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
|  | DAQ | XCP | — | Timing Source | Sets the DAQ Timing Source property value. The default is Automatic. Note The Timing Source property is only supported with XCP protocol. Values are: 0AutomaticThe default method (1, 2, or 3, below) is selected.1Host TimingTimestamps are generated from the host system time whenever a frame arrives.This mode is always available.This is the default for XCP on TCP/UDP if the ECU does not support timestamps.2CAN TimingTimestamps are generated from the network interface hardware (e.g. NI-XNET hardware).This mode is available only if the network hardware generates timestamps.This is the default for XCP on CAN if the ECU does not support timestamps.3ECU TimingTimestamps are taken from the ECU data. The Start Time is taken from the host, and increments are taken from the ECU.This mode is only available if the ECU generates timestamps; in this case, it is default. |
| 0 | AutomaticThe default method (1, 2, or 3, below) is selected. |  |  |  |  |
| 1 | Host TimingTimestamps are generated from the host system time whenever a frame arrives.This mode is always available.This is the default for XCP on TCP/UDP if the ECU does not support timestamps. |  |  |  |  |
| 2 | CAN TimingTimestamps are generated from the network interface hardware (e.g. NI-XNET hardware).This mode is available only if the network hardware generates timestamps.This is the default for XCP on CAN if the ECU does not support timestamps. |  |  |  |  |
| 3 | ECU TimingTimestamps are taken from the ECU data. The Start Time is taken from the host, and increments are taken from the ECU.This mode is only available if the ECU generates timestamps; in this case, it is default. |  |  |  |  |

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-text-to-double-vi.html language=enus -->
## TOPIC 00009: MC Text To Double.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-text-to-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-text-to-double-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts a text value into the numeric representation using an enumeration or range text type scaling. Format Input object name indicates the object (measurement or characteristic) for which the enumeration or range text scaling is performed. ECU ref in is the task reference that links to th

### MC Text To Double.vi

**Purpose**

Converts a text value into the numeric representation using an enumeration or range text type scaling.

**Format**

[IMAGE alt='image' src='images/TextToDouble.gif']

**Input**

|  | object name indicates the object (measurement or characteristic) for which the enumeration or range text scaling is performed. |
| --- | --- |
|  | ECU ref in is the task reference that links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
|  | object type is a U32 ring that indicates the type of the object named in object name. Valid values are: 1Measurement Name2Characteristic Name |
| 1 | Measurement Name |
| 2 | Characteristic Name |
|  | TextValue is the text value you want to convert. Use MC Get Property.vi (Scaling—Text Values) to request the available values. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | value returns the numeric value to be transferred to the ECU in subsequent Write requests. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC Text To Double.vi** performs the conversion from the text input value into a double value.

You can use this especially if the measurement or characteristic has an associated enumeration or range text type scaling before writing the double values to the ECU, using the regular Write VIs ([MC DAQ Write.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqwritevi), [MC Measurement Write.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementwritevi), [MC Characteristic Write.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mccharacteristicwritevi)).

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-upload-vi.html language=enus -->
## TOPIC 00010: MC Upload.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-upload-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-upload-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Uploads data from an ECU. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Address is a cluster which contains the following values. Address spe

### MC Upload.vi

**Purpose**

Uploads data from an ECU.

**Format**

[IMAGE alt='image' src='images/CCPupload.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Address is a cluster which contains the following values. Address specifies the address part of the source address in the ECU from which the memory block is copied.Extension contains the extension part of the source address. |
|  | Address specifies the address part of the source address in the ECU from which the memory block is copied. |
|  | Extension contains the extension part of the source address. |
|  | Block size is the size of the data block, in bytes, to be uploaded. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Data is a byte array which receives the uploaded data from the ECU. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC Upload.vi** implements the UPLOAD command. A data block of the specified length, starting at the specified address, is uploaded from the ECU. **MC Upload.vi** will set the Memory Transfer Address pointer MTA0 to the appropriate value as defined in the **Address** cluster.

If you are using the CCP protocol, **MC Upload.vi** implements the UPLOAD command. A data block of the specified length, starting at the specified address, is uploaded from the ECU. **MC Upload.vi** will set the Memory Transfer Address pointer MTA0 to the appropriate value as defined in the **Address** cluster.

If you are using the XCP protocol, **MC Upload.vi** implements the XCP command UPLOAD. A data block of the specified length starting at the specified address is uploaded from the ECU. The Memory Transfer Address pointer MTA0 is post-incremented by the given number of data elements. If the slave device does not support block transfer mode, all uploaded data is transferred in a single response packet. If block transfer mode is supported, the uploaded data is transferred in multiple responses on the same request packet. For the master there are no limitations allowed concerning the maximum block size.

For further information on how to upload data and to use the **MC Upload.vi** command refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-copy-cal-page-vi.html language=enus -->
## TOPIC 00011: MC XCP Copy Cal Page.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-copy-cal-page-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-copy-cal-page-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Forces a copy transaction of one calibration page to another. Format Input Source page specifies the logical page number of the source data page. Source segment specifies the logical segment number of the source data page. ECU ref in is the task reference which links to the selected ECU. Thi

### MC XCP Copy Cal Page.vi

**Purpose**

Forces a copy transaction of one calibration page to another.

**Format**

[IMAGE alt='image' src='images/XCPCopyCalPage.gif']

**Input**

|  | Source page specifies the logical page number of the source data page. |
| --- | --- |
|  | Source segment specifies the logical segment number of the source data page. |
|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
|  | Destination page specifies the logical segment number of the destination data page. |
|  | Destination segment specifies logical page number of the destination data page. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Copy Cal Page.vi** implements the XCP command COPY_CAL_PAGE and forces the slave to copy one calibration page to another. This command is only available if more than one calibration page is defined. In principal, any page of any segment can be copied to any page of any other segment but there may be restrictions.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-get-cal-page-vi.html language=enus -->
## TOPIC 00012: MC XCP Get Cal Page.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-get-cal-page-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-get-cal-page-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Queries a calibration page setting. Format Input Mode specifies the access mode: Mode = 1 The given page is used by the slave device application. Mode = 2 The slave device XCP driver will access the given page. ECU ref in is the task reference which links to the selected ECU. This reference

### MC XCP Get Cal Page.vi

**Purpose**

Queries a calibration page setting.

**Format**

[IMAGE alt='image' src='images/XCPGetCalPage.gif']

**Input**

|  | Mode specifies the access mode: Mode = 1 The given page is used by the slave device application. Mode = 2 The slave device XCP driver will access the given page. |
| --- | --- |
|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
|  | Segment specifies the selected logical data segment number. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Page returns the logical data page number. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Get Cal Page.vi** implements the XCP command GET_CAL_PAGE and queries the logical number for the calibration data page that is currently activated for the specified access mode and data segment.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-get-id-vi.html language=enus -->
## TOPIC 00013: MC XCP Get ID.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-get-id-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-get-id-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Queries session configuration or slave device identification. Format Input Reference in is the reference to any opened A2L database, a selected ECU, or an ECU which is already connected (with , , , or ). The type of this reference depends on the property you want to get. Type specifies the t

### MC XCP Get ID.vi

**Purpose**

Queries session configuration or slave device identification.

**Format**

[IMAGE alt='image' src='images/XCPGetId.gif']

**Input**

|  | Reference in is the reference to any opened A2L database, a selected ECU, or an ECU which is already connected (with , , , or ). The type of this reference depends on the property you want to get. |
| --- | --- |
|  | Type specifies the type of the requested identification: TypeDescription0ASCII text1ASAM-MC2 filename without path and extension2ASAM-MC2 filename with path and extension3URL where the ASAM-MC2 file can be found4ASAM-MC2 file to upload 128..255User defined |
| Type | Description |
| 0 | ASCII text |
| 1 | ASAM-MC2 filename without path and extension |
| 2 | ASAM-MC2 filename with path and extension |
| 3 | URL where the ASAM-MC2 file can be found |
| 4 | ASAM-MC2 file to upload |
| 128..255 | User defined |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | Reference out is a copy of the reference in terminal which can be wired through subsequent ECU M&C VIs. |
| --- | --- |
|  | Id contains the queried identification string. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Get ID.vi** implements the XCP command GET_ID and returns session configuration or slave device identification information of the selected ECU slave device. The supported types are implementation specific of the ECU slave device. The identification string is ASCII text format.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-get-status-vi.html language=enus -->
## TOPIC 00014: MC XCP Get Status.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-get-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-get-status-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Queries the current session status from an ECU slave device. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Error in is a cluster which descri

### MC XCP Get Status.vi

**Purpose**

Queries the current session status from an ECU slave device.

**Format**

[IMAGE alt='image' src='images/XCPGetStatus.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | Session Id returns the defined session configuration ID. |
| --- | --- |
|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
|  | Session status returns the current status of the selected ECU. |
|  | Resource mask is the current resource protection status of the selected ECU. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Get Status.vi** implements the XCP command GET_STATUS and returns all current status information of the selected ECU slave device, including the status of the resource protection, pending store requests and the general status of data acquisition and stimulation.

#### Current Session Status

Session status contains a bit mask which is described below:

| Bit Number | Flag | Description |
| --- | --- | --- |
| 0 | STORE_CAL_REQ | REQuest to STORE CALibration data: 0—STORE_CAL_REQ mode is reset. 1—STORE_CAL_REQ mode is set. |
| 1 | Unused | — |
| 2 | STORE_DAQ_REQ | REQuest to STORE DAQ list: 0—STORE_DAQ_REQ mode is reset. 1—STORE_DAQ_REQ mode is set. |
| 3 | CLEAR_DAQ_REQ | REQuest to CLEAR DAQ configuration: 0—CLEAR_DAQ_REQ is reset. 1—CLEAR_DAQ_REQ is set. |
| 4 | Unused | — |
| 5 | Unused | — |
| 6 | DAQ_RUNNING | Data Transfer: 0—The data transfer is not running. 1—The data transfer is running. |
| 7 | RESUME | RESUME Mode: 0—The slave device is not in RESUME mode. 1—The slave device is in RESUME mode. |

The STORE_CAL_REQ flag indicates a pending request to save the calibration data into non-volatile memory. As soon as the request has been fulfilled, the slave will reset the appropriate bit. The slave device may indicate this by transmitting an EV_STORE_CAL event packet.

The STORE_DAQ_REQ flag indicates a pending request to save the DAQ list setup in non-volatile memory. As soon as the request has been fulfilled, the slave will reset the appropriate bit. The slave device may indicate this by transmitting an EV_STORE_DAQ event packet.

The CLEAR_DAQ_REQ flag indicates a pending request to clear all DAQ lists in non-volatile memory. All ODT entries are reset to address = 0, extension = 0, size = 0 and bit_offset = FF. Session configuration ID is reset to 0. As soon as the request has been fulfilled, the slave will reset the appropriate bit. The slave device may indicate this by transmitting an EV_CLEAR_DAQ event packet. If the slave device does not support the requested mode, an ERR_OUT_OF_RANGE is returned.

The DAQ_RUNNING flag indicates that at least one DAQ list has been started and is in RUNNING mode.

The RESUME flag indicates that the slave is in RESUME mode.

**Resource mask** contains the current resource protection status as a bit mask described below:

| Bit Number | Flag | Description |
| --- | --- | --- |
| 0 | CAL/PAG | REQuest to STORE CALibration data: 0—STORE_CAL_REQ mode is reset. 1—STORE_CAL_REQ mode is set. |
| 1 | Unused | — |
| 2 | DAQ | DAQ list commands (DIRECTION = DAQ): 0—DAQ list commands are not protected with SEED & Key mechanism. 1—DAQ list commands are protected with SEED & Key mechanism. |
| 3 | STIM | DAQ list commands (DIRECTION = STIM): 0—DAQ list commands are not protected with SEED & Key mechanism. 1—DAQ list commands are protected with SEED & Key mechanism. |
| 4 | PGM | ProGraMming commands: 0—ProGraMming commands are not protected with SEED & Key mechanism. 1—ProGraMming commands are protected with SEED & Key mechanism |
| 5 | Unused | — |
| 6 | Unused | — |
| 7 | Unused | — |

The CAL/PAG flags indicates that all commands of the CALibration/PAGing group are protected and will return an ERR_ACCESS_LOCKED upon an attempt to execute the command without a previous successful GET_SEED/UNLOCK sequence.

The PGM flags indicates that all the commands of the ProGraMming group are protected and will return a ERR_ACCESS_LOCKED upon an attempt to execute the command without a previous successful GET_SEED/UNLOCK sequence.

The parameter **Session Id** contains the Session configuration ID. The session configuration ID must be set by a prior [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetrequestvi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetrequestvi) call with STORE_DAQ_REQ set. This allows the master device to verify that automatically started DAQ lists contain the expected data transfer configuration.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-program-prepare-vi.html language=enus -->
## TOPIC 00015: MC XCP Program Prepare.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-program-prepare-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-program-prepare-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Prepares the programming of non volatile memory. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Address is a cluster which contains the follow

### MC XCP Program Prepare.vi

**Purpose**

Prepares the programming of non volatile memory.

**Format**

[IMAGE alt='image' src='images/XCPProgramPrepare.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Address is a cluster which contains the following values. Address specifies the address part of the source address.Extension contains the extension part of the source address. |
|  | Address specifies the address part of the source address. |
|  | Extension contains the extension part of the source address. |
|  | code size determines the size of data code to be downloaded by the subsequent memory programming. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Program Prepare.vi** may be used to indicate a data download as a pre-condition for non-volatile memory reprogramming. The Memory Transfer address (MTA) pointer is set to the volatile memory location specified by the parameters **Address** and **Extension**. The download itself is done by using subsequent standard commands like [MC Download.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdownloadvi). The slave device must ensure that the target memory area is available and it is in an operational state which permits the download of code. If not, an error will be returned.

**MC XCP Program Prepare.vi** implements the optional XCP PROGRAM_PREPARE command defined by the XCP specification. For further information on how to program non-volatile ECU memory refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-program-verify-vi.html language=enus -->
## TOPIC 00016: MC XCP Program Verify.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-program-verify-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-program-verify-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Performs a non-volatile memory certification task on the ECU device. Format Input Verification mode may be defined as: Type Description 0 Request to start an internal routine. 1 Transmit a Verification Value. ECU ref in is the task reference which links to the selected ECU. This reference is

### MC XCP Program Verify.vi

**Purpose**

Performs a non-volatile memory certification task on the ECU device.

**Format**

[IMAGE alt='image' src='images/XCPProgramVerify.gif']

**Input**

|  | Verification mode may be defined as: |
| --- | --- |

| Type | Description |
| --- | --- |
| 0 | Request to start an internal routine. |
| 1 | Transmit a Verification Value. |

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Verification type specifies the Verification Type of the requested program verification. The Verification Type is a bit mask described below: |

| Verification Type | Description |
| --- | --- |
| 0x0001 | Calibration area(s) of the flash. |
| 0x0002 | Code area(s) of the flash. |
| 0x0004 | Complete flash content. |
| 0x0008...0x0080 | Reserved. |
| 0x0100...0xFF00 | User defined. |

|  | Verification value is project-specific. |
| --- | --- |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Program Verify.vi** may be used to verify the success of non-volatile memory reprogramming.

With **Verification mode** set to 00 the master may request the slave to begin internal test routines to check whether the new flash contents fits to the rest of the flash. Only the result is of interest. With **Verification mode** set to 01, the master may tell the slave that it will be sending a **Verification value** to the slave. The definition of the **Verification mode** is project-specific. The master receives the **Verification mode** from the project-specific programming flow control and passes it to the slave.

**MC XCP Program Verify.vi** implements the optional XCP PROGRAM_VERIFY command defined by the XCP specification. For further information on how to program non-volatile ECU memory refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-set-cal-page-vi.html language=enus -->
## TOPIC 00017: MC XCP Set Cal Page.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-set-cal-page-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-set-cal-page-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets a calibration page. Format Input Mode is a bit mask described below: Bit Description 0 The given page is used by the slave device application. 1 The slave device XCP driver will access the given page. 2 Unused. 3 Unused. 4 Unused. 5 Unused. 6 Unused. 7 The logical segment number is igno

### MC XCP Set Cal Page.vi

**Purpose**

Sets a calibration page.

**Format**

[IMAGE alt='image' src='images/XCPSetCalPage.gif']

**Input**

|  | Mode is a bit mask described below: |
| --- | --- |

| Bit | Description |
| --- | --- |
| 0 | The given page is used by the slave device application. |
| 1 | The slave device XCP driver will access the given page. |
| 2 | Unused. |
| 3 | Unused. |
| 4 | Unused. |
| 5 | Unused. |
| 6 | Unused. |
| 7 | The logical segment number is ignored. The command applies to all segments. |

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Segment specifies the selected logical data segment number. |
|  | Page specifies the logical data page number. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Address is a cluster which contains the following values. Address specifies the address part of the active calibration page address.Extension contains the extension part of the active calibration page address. |
|  | Address specifies the address part of the active calibration page address. |
|  | Extension contains the extension part of the active calibration page address. |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Set Cal Page.vi** implements the XCP command SET_CAL_PAGE and sets the access mode for a calibration data segment, if the slave device supports calibration data page switching. A calibration data segment and its pages are specified by logical numbers.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-set-request-vi.html language=enus -->
## TOPIC 00018: MC XCP Set Request.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-set-request-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-set-request-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Performs a request to save session and device information to non-volatile memory. Format Input Mode is a bit mask described below: Bit Description 0 Request to store calibration data in non-volatile memory. 1 Unused. 2 Request to save all DAQ lists, which have been selected with START_STOP_D

### MC XCP Set Request.vi

**Purpose**

Performs a request to save session and device information to non-volatile memory.

**Format**

[IMAGE alt='image' src='images/XCPSetRequest.gif']

**Input**

|  | Mode is a bit mask described below: |
| --- | --- |

| Bit | Description |
| --- | --- |
| 0 | Request to store calibration data in non-volatile memory. |
| 1 | Unused. |
| 2 | Request to save all DAQ lists, which have been selected with START_STOP_DAQ_LIST(Select) into non-volatile memory. The slave also must store the session configuration ID in non-volatile memory. Upon saving, the slave first must clear any DAQ list configuration that might already be stored in non-volatile memory. |
| 3 | Request to clear all DAQ lists in non-volatile memory. All ODT entries reset to address = 0, extension = 0, size = 0 and bit_offset = FF. Session configuration ID reset to 0. |
| 4 | Unused. |
| 5 | Unused. |
| 6 | Unused. |
| 7 | Unused. |

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Session ID is a session configuration ID that is stored in non-volatile memory together with the information requested by the Mode parameter. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Set Request.vi** implements the XCP command SET_REQUEST and is used to save session configuration information into non-volatile memory in the ECU.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for LabVIEW

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-labview-api-ref path=mc-xcp-set-segment-mode-vi.html language=enus -->
## TOPIC 00019: MC XCP Set Segment Mode.vi

- bundle_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- source_path: `mc-xcp-set-segment-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-labview-api-ref/raw/resource/enus/mc-xcp-set-segment-mode-vi.html
- document_id: `ecu-measurement-calibration-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets the mode of a specified segment. Format Input ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. Segment specifies the logical data segment number. Mode s

### MC XCP Set Segment Mode.vi

**Purpose**

Sets the mode of a specified segment.

**Format**

[IMAGE alt='image' src='images/XCPSetSegmentMode.gif']

**Input**

|  | ECU ref in is the task reference which links to the selected ECU. This reference is originally returned from MC ECU Open.vi or MC ECU Select.vi, and then wired through subsequent VIs. |
| --- | --- |
|  | Segment specifies the logical data segment number. |
|  | Mode specifies the mode for the segment. |
|  | Error in is a cluster which describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Output**

|  | ECU ref out is the same as ECU ref in. Wire the task reference to subsequent VIs for this task. |
| --- | --- |
|  | Error out describes error conditions. If the Error in cluster indicated an error, the Error out cluster contains the same information. Otherwise, Error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: VI did not execute the intended operation. A positive value means warning: VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

**Description**

**MC XCP Set Segment Mode.vi** implements the XCP command SET_SEGMENT_MODE and sets the selected segment into the specified mode. If **Mode**=0 the segment disables the FREEZE mode, if **Mode**=1 the segment is set to FREEZE mode through an XCP STORE_CAL_REQ operation.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for LabVIEW
