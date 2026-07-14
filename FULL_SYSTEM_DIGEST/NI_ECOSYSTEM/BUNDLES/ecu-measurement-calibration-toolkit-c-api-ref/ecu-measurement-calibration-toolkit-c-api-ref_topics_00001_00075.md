# NI DOCUMENT BUNDLE: ecu-measurement-calibration-toolkit-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ecu-measurement-calibration-toolkit-c-api-ref start=1 end=75 -->
<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=ecu-m-c-api-for-c.html language=enus -->
## TOPIC 00001: ECU M&C API for C

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `ecu-m-c-api-for-c.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/ecu-m-c-api-for-c.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic lists the ECU M&C Toolkit functions and describes the format, purpose and parameters. Unless otherwise stated, each ECU M&C function suspends execution of the calling thread until it completes. The functions in this topic are listed alphabetically. Section Headings The following are secti

### ECU M&C API for C

This topic lists the ECU M&C Toolkit functions and describes the format, purpose and parameters.

Unless otherwise stated, each ECU M&C function suspends execution of the calling thread until it completes. The functions in this
topic are listed alphabetically.
Section Headings

The following are section headings found in the ECU M&C API for C functions.

#### Purpose

Each function description includes a brief statement of the purpose of the function.

#### Format

The format section describes the format of each function for the C programming language.

#### Input and Output

The input and output parameters for each function are listed.

#### Description

The description section gives details about the purpose and effect of each function.

#### Data Types

The following data types are used with functions of the ECU M&C API for C.

#### Data Types for the ECU M&C API for C

| ECU M&C API functions for C |  |
| --- | --- |
| Data Type | Purpose |
| i8 | 8-bit signed integer |
| i16 | 16-bit signed integer |
| i32 | 32-bit signed integer |
| i64 | 64-bit signed integer |
| u8 | 8-bit unsigned integer |
| u16 | 16-bit unsigned integer |
| u32 | 32-bit unsigned integer |
| u64 | 64-bit unsigned integer |
| f32 | 32-bit floating point number |
| f64 | 64-bit floating point number |
| str | ASCII string represented as an array of characters terminated by null character ('\\0'). This type is used with output strings. str is typically used in the ECU M&C API as a pointer to a string, as char*. |
| cstr | ASCII string represented as an array of characters terminated by null character ('\\0'). This type is used with input strings. cstr is typically used in the ECU M&C API as a pointer to a string, as const char*. |
| nctTypeTaskRef | Reference to an initialized database task, ECU task, or Measurement task. |
| mcAddress | C struct which represents the target address for a specific CCP operation in the ECU. |

The following table contains an alphabetical list of the ECU M&C Toolkit API functions.

#### Functions for the ECU M&C API for C

| Function | Purpose |
| --- | --- |
| mcBuildChecksum | Calculates a checksum over a defined memory range within the ECU. |
| mcCalculateChecksum | Calculates the checksum of a data block in memory. |
| mcCCPActionService | Calls an implementation-specific action service on the ECU. |
| mcCCPDiagService | Calls an implementation-specific diagnostic service on the ECU. |
| mcCCPGetActiveCalPage | Retrieves the ECU Memory Transfer Address pointer to the calibration data page. |
| mcCCPGetResult | Uploads data from the ECU when the Memory Transfer Address pointer 0 (MTA0) has been set. |
| mcCCPGetSessionStatus | Retrieves the current status of the Calibration Session. |
| mcCCPGetVersion | Retrieves CCP version implemented in the ECU. |
| mcCCPMoveMemory | Moves a memory block on the ECU. |
| mcCCPSelectCalPage | Sets the specified address to be the start address of the calibration data page. |
| mcCCPSetSessionStatus | Updates the ECU with the current state of the calibration session. |
| mcCharacteristicRead | Reads all data as scaled from a named Characteristic on the ECU which is identified by the ECU Reference handle. |
| mcCharacteristicReadRaw | Reads all data as raw (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle. |
| mcCharacteristicReadByteArray | Reads all data as raw byte array (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle. |
| mcCharacteristicReadSingleValue | Reads a single scaled value from a named Characteristic on the ECU which is identified by the ECU Reference handle. |
| mcCharacteristicReadRawSingleValue | Reads a single raw value (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle. |
| mcCharacteristicWrite | Downloads scaled data to a Characteristic for a selected ECU. |
| mcCharacteristicWriteRaw | Downloads raw data (no scaling) to a Characteristic for a selected ECU. |
| mcCharacteristicWriteByteArray | Downloads raw data as byte array (no scaling) to a Characteristic for a selected ECU. |
| mcCharacteristicWriteSingleValue | Writes a single scaled value to a named Characteristic on the ECU. |
| mcCharacteristicWriteRawSingleValue | Writes a single raw value (no scaling) to a named Characteristic on the ECU. |
| mcClearMemory | Clears the contents of the specified ECU memory. |
| mcConversionCreate | Creates a signal conversion object in memory. |
| mcDAQClear | Stops communication for the Measurement task and clears the task. |
| mcDAQInitialize | Initializes a Measurement task for the specified scaled Measurement channel list. |
| mcDAQInitializeEx | Initializes a Measurement task for the specified scaled and raw (unscaled) Measurement channel lists. |
| mcDAQListInitialize | Defines a DAQ list on a specific DAQ list number and initializes the Measurement task for the specified scaled Measurement channel list. |
| mcDAQListInitializeEx | Defines a DAQ list on a specific DAQ list number and initializes the Measurement task for the specified scaled and raw (unscaled) Measurement channel lists. |
| mcDAQRead | Reads scaled samples from a Measurement task. Samples are obtained from received CAN messages. |
| mcDAQReadEx | Reads samples from a Measurement task. Samples are obtained from received CAN messages. Scaled and raw (unscaled) Measurements are acquired. |
| mcDAQReadTimestamped | Reads timestamped scaled samples from a DAQ task initialized with the selected mode of mcDAQModeDAQListTimeStamped. |
| mcDAQReadTimestampedEx | Reads timestamped scaled and timestamped raw (unscaled) samples from a DAQ task initialized with the selected mode of mcDAQModeDAQListTimeStamped. |
| mcDAQStartStop | Starts or stops the transmission of the DAQ lists for the specified Measurement task on the ECU. |
| mcDAQWrite | Writes scaled samples to an ECU DAQ list. |
| mcDAQWriteEx | Writes scaled and raw (unscaled) samples to an ECU DAQ list. |
| mcDatabaseClose | Closes a specified A2L Database reference. |
| mcDatabaseOpen | Opens a specified A2L Database. |
| mcDatabaseOpenEx | Creates an A2L database in memory. |
| mcDoubleToText | Converts a numerical value to a text string using an enumeration or range text type scaling. |
| mcDownload | Downloads data to an ECU. |
| mcECUConnect | Establishes communication to the selected ECU through XCP or CCP. |
| mcECUConnect2 | Establishes communication to the selected ECU through XCP or CCP. Allows you to specify the mode for the XCP CONNECT command. |
| mcECUCreate | Creates an ECU object in memory. |
| mcECUDeselect | Deselects an ECU and invalidates the ECU reference handle. |
| mcECUDisconnect | Disconnects XCP or CCP communication to the selected ECU. |
| mcECUSelectEx | Selects an ECU from the names stored in an A2L database. |
| mcECUSetCalibrationPage | Sets the appropriate RAM or ROM calibration page on the ECU. |
| mcEventCreate | Creates an Event object in memory. |
| mcGeneric | Sends a generic XCP or CCP command. |
| mcGetNames | Retrieves a comma-separated list of ECU names, Transport Layer Instance names, Measurement names, Characteristic names, Event names, Characteristic pages, or Group names from a specified A2L database. |
| mcGetNamesLength | Retrieves the amount of memory required to store the names returned by mcGetNames. |
| mcGetProperty | Retrieves a property of the driver, the database, the ECU, a characteristic, a Measurement, or a Measurement task. |
| mcMeasurementCreate | Creates a Measurement object in memory. |
| mcMeasurementRead | Reads a single scaled Measurement value from the ECU. |
| mcMeasurementReadRaw | Reads a single raw (unscaled) Measurement value from the ECU. |
| mcMeasurementWrite | Writes a single scaled Measurement value to the ECU. |
| mcMeasurementWriteRaw | Writes a single raw (unscaled) Measurement value to the ECU. |
| mcProgram | Programs a memory block on the ECU. |
| mcProgramReset | Indicates the end of a programming sequence. |
| mcProgramStart | Indicates the start of a programming sequence. |
| mcSetProperty | Sets a property of the driver, the database, the ECU, a characteristic, a Measurement, or a Measurement task. |
| mcStatusToString | Converts a status code into a descriptive string. |
| mcTextToDouble | Converts a text string to a numerical value using an enumeration or range text scaling. |
| mcUpload | Uploads data from an ECU. |
| mcXCPCopyCalPage | Forces a copy transaction of one calibration page to another. |
| mcXCPGetCalPage | Queries a calibration page setting. |
| mcXCPGetId | Queries session configuration or slave device identification. |
| mcXCPGetStatus | Queries the current session status from an ECU slave device. |
| mcXCPProgramPrepare | Prepares the programming of non volatile memory. |
| mcXCPProgramVerify | Performs a non-volatile memory certification task on the ECU device. |
| mcXCPSetCalPage | Sets a calibration page. |
| mcXCPSetRequest | Performs a request to save session and device information to non-volatile memory. |
| mcXCPSetSegmentMode | Sets the mode of a specified segment. |

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=ecumc_c_intro.html language=enus -->
## TOPIC 00002: ECU Measurement Calibration Toolkit C Programming Reference Manual

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `ecumc_c_intro.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/ecumc_c_intro.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ECU Measurement Calibration Toolkit Programming Reference Manual provides information about the ECUMC C APIs and error codes.

### ECU Measurement Calibration Toolkit C Programming Reference Manual

The ECU Measurement Calibration Toolkit Programming Reference Manual provides information about the ECUMC C APIs and error codes.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcbuildchecksum.html language=enus -->
## TOPIC 00003: mcBuildChecksum

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcbuildchecksum.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcbuildchecksum.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Calculates a checksum over a defined memory range within the ECU. Format mcTypeStatus mcBuildChecksum( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *ChecksumType, u8 *SizeOfChecksum, u32 *Checksum); Input ECURefNum ECURefNum is the task reference which links to the selected

### mcBuildChecksum

Purpose

Calculates a checksum over a defined memory range within the ECU.
Format

| mcTypeStatus | mcBuildChecksum( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *ChecksumType, u8 *SizeOfChecksum, u32 *Checksum); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address, |
| u32 | BlockSize, |
| u8 | *ChecksumType, |
| u8 | *SizeOfChecksum, |
| u32 | *Checksum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Configures the target address for the checksum operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the target address.

**Extension**

Extension contains the extension part of the target address.

BlockSize

BlockSize determines the size of the block on which the checksum has to be calculated.
Output

ChecksumType

ChecksumType returns the type of the calculated checksum. For CCP, ChecksumType is 0xFF. For XCP, refer to the Description section.

SizeofChecksum

SizeofChecksum returns the size in bytes of the calculated checksum.

Checksum

Checksum is the calculated checksum.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcBuildChecksum is used to calculate the checksum of a specified memory block inside the ECU starting at the selected **Address**.

If you are using the CCP protocol, mcBuildChecksum implements the CCP BUILD_CHKSUM command. The checksum algorithm is not specified by CCP and the checksum algorithm may be different on different devices.

If you are using the XCP protocol, mcBuildChecksum implements the BUILD_CHECKSUM command of the XCP specification. The result of the checksum calculation is returned in Checksum regardless of the checksum type. The following values for ChecksumType are defined in the XCP specification:

| Type | Name | Description |
| --- | --- | --- |
| 0x01 | XCP_ADD_11 | Add BYTE into a BYTE checksum, ignore overflows |
| 0x02 | XCP_ADD_12 | Add BYTE into a WORD checksum, ignore overflows |
| 0x03 | XCP_ADD_14 | Add BYTE into a DWORD checksum, ignore overflows |
| 0x04 | XCP_ADD_22 | Add WORD into a WORD checksum, ignore overflows, blocksize must be modulo 2 |
| 0x05 | XCP_ADD_24 | Add WORD into a DWORD checksum, ignore overflows, blocksize must be modulo 2 |
| 0x06 | XCP_ADD_44 | Add DWORD into DWORD, ignore overflows, blocksize must be modulo 4 |
| 0x07 | XCP_CRC_16 | Refer to CRC error detection algorithms |
| 0x08 | XCP_CRC_16_CITT | Refer to CRC error detection algorithms |
| 0x09 | XCP_CRC_32 | Refer to CRC error detection algorithms |
| 0xFF | XCP_USER_DEFINED | User defined algorithm, in externally calculated function |

With ChecksumType XCP_USER_DEFINED, the Slave may indicate that the Master which calculates the checksum must use a user-defined algorithm implemented in an externally calculated function (for instance, Win32 DLL, UNIX shared object file, etc.). The master retrieves the name of the external function file to be used for this slave from the ASAM MCD 2MC description file.

The CRC algorithms are specified by the following parameters:

| Name | Width | Poly | Init | Refin | Refout | XORout |
| --- | --- | --- | --- | --- | --- | --- |
| XCP_CRC_16 | 16 | 0x8005 | 0x0000 | TRUE | TRUE | 0x0000 |
| XCP_CRC16_CITT | 16 | 0x1021 | 0xFFFF | FALSE | FALSE | 0x0000 |
| XCP_CRC_32 32 | 32 | 0x04C11DB7 | 0xFFFFFFFF | TRUE | TRUE | 0xFFFFFFFF |

#### Name

The name of the algorithm. A string value starting with "XCP_".

#### Width

The width of the algorithm expressed in bits. This is one less than the width of the Poly.

#### Poly

The polynomial. This is a binary value specified as a hexadecimal number. The top bit of the Poly should be omitted. For example, if the Poly is 0x10110, you should specify 0x06. An important aspect of this parameter is that it represents the unreflected polynomial. The bottom of this parameter is always the least significant bit (LSB) of the divisor during the division, regardless of whether the algorithm is reflected.

#### Init

This parameter specifies the initial value of the register when the algorithm starts. This is the value to be assigned to the register in the direct table algorithm. In the table algorithm, we may think of the register always commencing with the value zero, and this value being XORed into the register after the nth bit iteration. This parameter should be specified as a hexadecimal number.

#### Refin

A Boolean parameter. If it is FALSE, input bytes are processed with bit 7 being treated as the most significant bit (MSB) and bit 0 being treated as the least significant bit. If this parameter is TRUE, each byte is reflected before being processed.

#### Refout

A Boolean parameter. If it is set to FALSE, the final value in the register is fed into the XORout stage directly. If this parameter is TRUE, the final register value is reflected first.

#### XORout

This is a width-bit value that should be specified as hexadecimal number. It is XORed to the final register value (after the Refout stage) before the value is returned as the official checksum.

For more detailed information about CRC algorithms, refer to:

http://www.repairfaq.org/filipg/LINK/F_crc_v34.html

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccalculatechecksum.html language=enus -->
## TOPIC 00004: mcCalculateChecksum

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccalculatechecksum.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccalculatechecksum.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Calculates the checksum of a data block in memory. Format mcTypeStatus mcCalculateChecksum( mcTypeTaskRef ECURefNum, u32 BlockSize, u8 *Data, u8 TypeOfChecksum, u8 *SizeOfChecksum, u32 *Checksum); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference

### mcCalculateChecksum

Purpose

Calculates the checksum of a data block in memory.
Format

| mcTypeStatus | mcCalculateChecksum( mcTypeTaskRef ECURefNum, u32 BlockSize, u8 *Data, u8 TypeOfChecksum, u8 *SizeOfChecksum, u32 *Checksum); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u32 | BlockSize, |
| u8 | *Data, |
| u8 | TypeOfChecksum, |
| u8 | *SizeOfChecksum, |
| u32 | *Checksum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

BlockSize

BlockSize determines the size of the block on which the checksum has to be calculated.
Output

TypeOfChecksum

TypeOfChecksum specifies the type of the calculated checksum.

Data

Data is a byte array over which the checksum calculation is performed.

SizeofChecksum

SizeofChecksum returns the size in bytes of the calculated checksum.

Checksum

Checksum is the calculated checksum.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCalculateChecksum implements a checksum calculation over a given data block. The checksum algorithm is performed over a dedicated checksum function provided by a specific DLL. The name of the Checksum DLL is defined in the A2L data base and can be changed by the application by the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) function using the mcPropECU_Checksum property.

If you are using the CCP protocol, TypeOfChecksum must be set to 0xFFh, since CCP only supports an external checksum DLL. If you are using XCP, the following values for TypeOfChecksum are defined in the XCP specification:

| Type | Name | Description |
| --- | --- | --- |
| 0x01 | XCP_ADD_11 | Add BYTE into a BYTE checksum, ignore overflows |
| 0x02 | XCP_ADD_12 | Add BYTE into a WORD checksum, ignore overflows |
| 0x03 | XCP_ADD_14 | Add BYTE into a DWORD checksum, ignore overflows |
| 0x04 | XCP_ADD_22 | Add WORD into a WORD checksum, ignore overflows, blocksize must be modulo 2 |
| 0x05 | XCP_ADD_24 | Add WORD into a DWORD checksum, ignore overflows, blocksize must be modulo 2 |
| 0x06 | XCP_ADD_44 | Add DWORD into DWORD, ignore overflows, blocksize must be modulo 4 |
| 0x07 | XCP_CRC_16 | Refer to CRC error detection algorithms |
| 0x08 | XCP_CRC_16_CITT | Refer to CRC error detection algorithms |
| 0x09 | XCP_CRC_32 | Refer to CRC error detection algorithms |
| 0xFF | XCP_USER_DEFINED | User defined algorithm, in externally calculated function |

For a detailed description of the checksum algorithm refer to the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcbuildchecksum](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcbuildchecksum) command or the XCP Part 2 Protocol Layer Specification.

For more detailed information about CRC algorithms, please refer to:

http://www.repairfaq.org/filipg/LINK/F_crc_v34.html

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpactionservice.html language=enus -->
## TOPIC 00005: mcCCPActionService

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpactionservice.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpactionservice.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Calls an implementation-specific action service on the ECU (CCP only). Format mcTypeStatus mcCCPActionService( mcTypeTaskRef ECURefNum, u16 ServiceNo, u8 Params[4], u8 *ResultLength, u8 *DataType); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This referenc

### mcCCPActionService

Purpose

Calls an implementation-specific action service on the ECU (CCP only).
Format

| mcTypeStatus | mcCCPActionService( mcTypeTaskRef ECURefNum, u16 ServiceNo, u8 Params[4], u8 *ResultLength, u8 *DataType); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u16 | ServiceNo, |
| u8 | Params[4], |
| u8 | *ResultLength, |
| u8 | *DataType); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

ServiceNo

ServiceNo determines the service that is executed inside the ECU. For more information about the services that are implemented in the ECU refer to the documentation for the ECU.

Params

Params passes the parameters of the service function as an array of bytes to the ECU. Since the parameters and their data types are specific to the ECU implementation, you are responsible of providing the required parameters in the correct byte ordering.
Output

ResultLength

ResultLength indicates the amount of data that can be uploaded from the ECU as a result of the execution of the service. The result of this service can be accessed by calling the function [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult) right after mcCCPActionService.

DataType

DataType is a data type qualifier that determines the data format of the result.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPActionService implements the CCP command ACTION_SERVICE. The ECU carries out the requested service and automatically sets the Memory Transfer Address MTA0 to the location from which the CCP master may upload the requested action service return information (if applicable).

The result of this service can be accessed by calling the function [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult) right after mcCCPActionService.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpdiagservice.html language=enus -->
## TOPIC 00006: mcCCPDiagService

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpdiagservice.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpdiagservice.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Calls an implementation-specific diagnostic service on the ECU (CCP only). Format mcTypeStatus mcCCPDiagService( mcTypeTaskRef ECURefNum, u16 ServiceNo, u8 Params[4], u8 *ResultLength, u8 *DataType); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This refere

### mcCCPDiagService

Purpose

Calls an implementation-specific diagnostic service on the ECU (CCP only).
Format

| mcTypeStatus | mcCCPDiagService( mcTypeTaskRef ECURefNum, u16 ServiceNo, u8 Params[4], u8 *ResultLength, u8 *DataType); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u16 | ServiceNo, |
| u8 | Params[4], |
| u8 | *ResultLength, |
| u8 | *DataType); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

ServiceNo

ServiceNo determines the diagnostic service that is executed inside the ECU. For more information about the services that are implemented in the ECU refer to the documentation for the ECU.

Params

Params passes an array of bytes to the ECU that might be needed by the ECU to run the diagnostic service. Since the definition of the parameters is specific to the implementation of the ECU, the parameters can only be passed as an array of bytes. It is your responsibility to pass the correct number of parameters in the correct byte ordering to this function.
Output

ResultLength

ResultLength returns the number of bytes that can be uploaded from the ECU as a result of the execution of the service. The result of this service can be accessed by calling the function [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult) right after mcCCPDiagService.

DataType

DataType is a data type qualifier which provides information about the data type of the result of the diagnostic service.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPDiagService implements the CCP command DIAG_SERVICE which calls a diagnostic service on the ECU and waits until it is finished. The selected ServiceNo specifies the diagnostic service that has to be executed inside the ECU. For more information about the available services that are implemented in the ECU refer to the documentation for the ECU.

The result of this service can be accessed by calling the function [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpgetresult) right after mcCCPDiagService.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpgetactivecalpage.html language=enus -->
## TOPIC 00007: mcCCPGetActiveCalPage

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpgetactivecalpage.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpgetactivecalpage.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Retrieves the ECU Memory Transfer Address pointer to the calibration data page (CCP only). Format mcTypeStatus mcCCPGetActiveCalPage( mcTypeTaskRef ECURefNum, mcAddress *Address); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally re

### mcCCPGetActiveCalPage

Purpose

Retrieves the ECU Memory Transfer Address pointer to the calibration data page (CCP only).
Format

| mcTypeStatus | mcCCPGetActiveCalPage( mcTypeTaskRef ECURefNum, mcAddress *Address); |
| --- | --- |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

Address

Returns the address for the active calibration page in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the address.

**Extension**

Extension contains the extension part of the address.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPGetActiveCalPage retrieves the start address of the active calibration data page in the ECU memory.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpgetresult.html language=enus -->
## TOPIC 00008: mcCCPGetResult

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpgetresult.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpgetresult.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Uploads data from the ECU when the Memory Transfer Address pointer 0 (MTA0) has been set (CCP only). Format mcTypeStatus mcCCPGetResult( mcTypeTaskRef ECURefNum, u32 BlockSize, u8 *Data); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is origi

### mcCCPGetResult

Purpose

Uploads data from the ECU when the Memory Transfer Address pointer 0 (MTA0) has been set (CCP only).
Format

| mcTypeStatus | mcCCPGetResult( mcTypeTaskRef ECURefNum, u32 BlockSize, u8 *Data); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u32 | BlockSize, |
| u8 | *Data); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

BlockSize

BlockSize determines the size of the data block to be uploaded from the ECU.
Output

Data

Data contains the data uploaded from the ECU memory.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

This function uploads data from the ECU. It is assumed that the Memory Transfer Address 0 (MTA0) has already been set to the start address of the data to be uploaded. Functions like [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpactionservice](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpactionservice) or [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpdiagservice](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpdiagservice) implicitly set the Memory Transfer Address 0 (MTA0) to the beginning of their result. To upload data from a specified address, use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcupload](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcupload) instead.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpgetsessionstatus.html language=enus -->
## TOPIC 00009: mcCCPGetSessionStatus

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpgetsessionstatus.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpgetsessionstatus.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Uploads data from the ECU when the Memory Transfer Address pointer 0 (MTA0) has been set (CCP only). Format mcTypeStatus mcCCPGetSessionStatus( mcTypeTaskRef ECURefNum, u8 *SessionStatus, u8 *StatusQualifier, u8 *AdditionalStatus); Input ECURefNum ECURefNum is the task reference which links

### mcCCPGetSessionStatus

Purpose

Uploads data from the ECU when the Memory Transfer Address pointer 0 (MTA0) has been set (CCP only).
Format

| mcTypeStatus | mcCCPGetSessionStatus( mcTypeTaskRef ECURefNum, u8 *SessionStatus, u8 *StatusQualifier, u8 *AdditionalStatus); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | *SessionStatus, |
| u8 | *StatusQualifier, |
| u8 | *AdditionalStatus); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

SessionStatus

The current SessionStatus which is returned from the ECU.

StatusQualifier

The additional StatusQualifier is manufacturer and/or project specific and is not part of the CCP protocol specification.

AdditionalStatus

If the StatusQualifier does not contain additional status information, AdditionalStatus must be set to FALSE. If AdditionalStatus is not FALSE, it may be used to determine the type of the additional status information.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPGetSessionStatus retrieves the current calibration session status of the ECU. The return value SessionStatus is a bit mask that represents several session states inside the ECU. StatusQualifier and AdditionalStatus contain additional status information. The content of these parameters is ECU specific and not defined by CCP. For more information about the parameter SessionStatus, refer to the description of mcCCPSetSessionStatus.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpgetversion.html language=enus -->
## TOPIC 00010: mcCCPGetVersion

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpgetversion.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpgetversion.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Retrieves CCP version implemented in the ECU (CCP only). Format mcTypeStatus mcCCPGetVersion( mcTypeTaskRef ECURefNum, u8 *MajorVersion, u8 *MinorVersion); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Output Maj

### mcCCPGetVersion

Purpose

Retrieves CCP version implemented in the ECU (CCP only).
Format

| mcTypeStatus | mcCCPGetVersion( mcTypeTaskRef ECURefNum, u8 *MajorVersion, u8 *MinorVersion); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | *MajorVersion, |
| u8 | *MinorVersion); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

MajorVersion

MajorVersion returns the major version number of the CCP implementation.

MinorVersion

MinorVersion returns the minor version number of the CCP implementation.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPGetVersion can be used to query the CCP version implemented in the ECU. This command performs a mutual identification of the protocol version in the slave device to agree on a common protocol version.

mcCCPGetVersion implements the CCP command GET_CCP_VERSION defined by the CCP specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpmovememory.html language=enus -->
## TOPIC 00011: mcCCPMoveMemory

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpmovememory.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpmovememory.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Moves a memory block on the ECU (CCP only). Format mcTypeStatus mcCCPMoveMemory( mcTypeTaskRef ECURefNum, mcAddress Source, mcAddress Destination, u32 BlockSize); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Sou

### mcCCPMoveMemory

Purpose

Moves a memory block on the ECU (CCP only).
Format

| mcTypeStatus | mcCCPMoveMemory( mcTypeTaskRef ECURefNum, mcAddress Source, mcAddress Destination, u32 BlockSize); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Source, |
| mcAddress | Destination, |
| u32 | BlockSize); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Source

Configures the source address for the memory move operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the source address.

**Extension**

Extension contains the extension part of the source address.

Destination

Configures the destination address for the memory move operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the destination address.

**Extension**

Extension contains the extension part of the destination address.

BlockSize

BlockSize determines the size of memory block in bytes which should be moved from the source address to the destination address.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPMoveMemory is used to move the memory contents of an ECU from one memory location to another. Before calling the CCP MOVE command this function sets the Memory Transfer Address pointers MTA0 as defined in the source struct and MTA1 as defined in the destination struct to appropriate values.

mcCCPMoveMemory implements the CCP command MOVE defined by the CCP specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpselectcalpage.html language=enus -->
## TOPIC 00012: mcCCPSelectCalPage

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpselectcalpage.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpselectcalpage.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets the specified address to be the start address of the calibration data page (CCP only). Format mcTypeStatus mcCCPSelectCalPage( mcTypeTaskRef ECURefNum, mcAddress Address); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally retur

### mcCCPSelectCalPage

Purpose

Sets the specified address to be the start address of the calibration data page (CCP only).
Format

| mcTypeStatus | mcCCPSelectCalPage( |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Configures the target address for the programming operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the target address.

**Extension**

Extension contains the extension part of the address.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPSelectCalPage implements the CCP command SELECT_CAL_PAGE. This command sets the beginning of the calibration data page to the specified address within the ECU.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcccpsetsessionstatus.html language=enus -->
## TOPIC 00013: mcCCPSetSessionStatus

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcccpsetsessionstatus.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcccpsetsessionstatus.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Updates the ECU with the current state of the calibration session (CCP only). Format mcTypeStatus mcCCPSetSessionStatus( mcTypeTaskRef ECURefNum, u8 SessionStatus); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . S

### mcCCPSetSessionStatus

Purpose

Updates the ECU with the current state of the calibration session (CCP only).
Format

| mcTypeStatus | mcCCPSetSessionStatus( |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | SessionStatus); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

SessionStatus

SessionStatus contains the new status to be set in the ECU.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCCPSetSessionStatus implements the CCP command SET_S_STATUS and is used to keep the ECU informed about the current state of the calibration session. The session status bits of an ECU can be read and written. Possible conditions are: reset on power-up, session log-off, and in applicable error conditions. The calibration session status is organized as a bit mask with the following assignment:

| Bit | Name | Description |
| --- | --- | --- |
| 0 | CAL | Calibration data initialized. |
| 1 | DAQ | DAQ list(s) initialized. |
| 2 | RESUME | Request to save DAQ set-up during shutdown in CCP slave. CCP slave automatically restarts DAQ after start-up. |
| 3 | Reserved | — |
| 4 | Reserved | — |
| 5 | Reserved | — |
| 6 | STORE | Request to save calibration data during shut-down in CCP slave. |
| 7 | RUN | Session in progress. |

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicread.html language=enus -->
## TOPIC 00014: mcCharacteristicRead

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicread.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicread.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads all data as scaled from a named Characteristic on the ECU which is identified by the ECU Reference handle. Format mcTypeStatus mcCharacteristicRead( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 *Values, u32 NumberOfValues); Input ECURefNum ECURefNum is the task reference whic

### mcCharacteristicRead

Purpose

Reads all data as scaled from a named Characteristic on the ECU which is identified by the ECU Reference handle.
Format

| mcTypeStatus | mcCharacteristicRead( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 *Values, u32 NumberOfValues); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *CharacteristicName, |
| f64 | *Values, |
| u32 | NumberOfValues); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

NumberOfValues

Specifies the number of values to read. To determine the dimension of the Characteristic, use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) function with the parameter mcPropChar_Dimension. To determine the size of each dimension use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) function with the parameter mcPropChar_Sizes.
Output

Values

Returns a single value, a 1-dimensional array, or a 2-dimensional array of values for the selected Characteristic.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicRead reads values from a named Characteristic on the ECU which is identified by the ECU Reference handle. The function returns a scaled double, 1D, or 2D array.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicreadbytearray.html language=enus -->
## TOPIC 00015: mcCharacteristicReadByteArray

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicreadbytearray.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicreadbytearray.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads all data as raw byte array (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle. Format mcTypeStatus mcCharacteristicReadByteArray( mcTypeTaskRef ECURefNum char *CharacteristicName, u8 *Values, u32 NumberOfValues; Input ECURefNum ECURefNum

### mcCharacteristicReadByteArray

Purpose

Reads all data as raw byte array (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle.
Format

| mcTypeStatus | mcCharacteristicReadByteArray( mcTypeTaskRef ECURefNum char *CharacteristicName, u8 *Values, u32 NumberOfValues; |
| --- | --- |
| mcTypeTaskRef | ECURefNum |
| char | *CharacteristicName, |
| u8 | *Values, |
| u32 | NumberOfValues; |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

NumberOfValues

Specifies the number of values to read. To determine the dimension of the Characteristic, use the [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) function with the parameter **mcPropChar_Dimension**. To determine the size of each dimension, use the [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) function with the parameter **mcPropChar_Sizes**.
Output

Values

Returns a 1-dimensional byte array of values for the selected Characteristic. The byte array corresponds to the memory area in the ECU representing this Characteristic.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicReadByteArray reads values from a named Characteristic on the ECU which is identified by the ECU Reference handle. The function returns a raw (unscaled) 1D byte array.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicreadraw.html language=enus -->
## TOPIC 00016: mcCharacteristicReadRaw

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicreadraw.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicreadraw.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads all data as raw (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle. Format mcTypeStatus mcCharacteristicReadRaw( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 *Values, u32 NumberOfValues); Input ECURefNum ECURefNum is the task re

### mcCharacteristicReadRaw

Purpose

Reads all data as raw (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle.
Format

| mcTypeStatus | mcCharacteristicReadRaw( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 *Values, u32 NumberOfValues); |
| --- | --- |
| mcTypeTaskRef | ECURefNum |
| char | *CharacteristicName, |
| u64 | *Values, |
| u32 | NumberOfValues); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

NumberOfValues

Specifies the number of values to read. To determine the dimension of the Characteristic, use the [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) function with the parameter **mcPropChar_Dimension**. To determine the size of each dimension, use the [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) function with the parameter **mcPropChar_Sizes**.
Output

Values

Returns a single value, a 1-dimensional array, or a 2-dimensional array of values for the selected Characteristic.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicReadRaw reads values from a named Characteristic on the ECU which is identified by the ECU Reference handle. The function returns a raw (unscaled) unsigned 64-bit integer, 1D, or 2D array.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicreadrawsinglevalue.html language=enus -->
## TOPIC 00017: mcCharacteristicReadRawSingleValue

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicreadrawsinglevalue.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicreadrawsinglevalue.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads a single raw value (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle. Format mcTypeStatus mcCharacteristicReadRawSingleValue( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 *Value, u32 X, u32 Y); Input ECURefNum ECURefNum is the

### mcCharacteristicReadRawSingleValue

Purpose

Reads a single raw value (no scaling) from a named Characteristic on the ECU which is identified by the ECU Reference handle.
Format

| mcTypeStatus | mcCharacteristicReadRawSingleValue( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 *Value, u32 X, u32 Y); |
| --- | --- |
| mcTypeTaskRef | ECURefNum |
| char | *CharacteristicName, |
| u64 | *Value, |
| u32 | X, |
| u32 | Y); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

X

X is the horizontal index if the Characteristic consists of 1 or 2 dimensions.

Y

Y is the vertical index if the Characteristic consists of 2 dimensions.
Output

Value

Value returns a single raw value from the selected Characteristic.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicReadRawSingleValue reads a raw (unscaled) value from a named Characteristic on the ECU which is identified by the ECU Reference handle. The value to be read is identified by the X and Y indices.

If the Characteristic array is 0-dimensional, X and Y can be set to 0.

If the Characteristic array is 1-dimensional, Y can be set to 0.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicreadsinglevalue.html language=enus -->
## TOPIC 00018: mcCharacteristicReadSingleValue

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicreadsinglevalue.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicreadsinglevalue.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads a single scaled value from a named Characteristic on the ECU which is identified by the ECU Reference handle. Format mcTypeStatus mcCharacteristicReadSingleValue( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 *Value, u32 X, u32 Y); Input ECURefNum ECURefNum is the task referen

### mcCharacteristicReadSingleValue

Purpose

Reads a single scaled value from a named Characteristic on the ECU which is identified by the ECU Reference handle.
Format

| mcTypeStatus | mcCharacteristicReadSingleValue( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 *Value, u32 X, u32 Y); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *CharacteristicName, |
| f64 | *Value, |
| u32 | X, |
| u32 | Y); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

X

X is the horizontal index if the Characteristic consists of 1 or 2 dimensions.

Y

Y is the vertical index if the Characteristic consists of 2 dimensions.
Output

Value

Returns a single value from the selected Characteristic.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicReadSingleValue reads a scaled value from a named Characteristic on the ECU which is identified by the ECU Reference handle. The value to be read is identified by the X and Y indices.

If the Characteristic array is 0-dimensional, X and Y can be set to 0.

If the Characteristic array is 1-dimensional, Y can be set to 0.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicwrite.html language=enus -->
## TOPIC 00019: mcCharacteristicWrite

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicwrite.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicwrite.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Downloads scaled data to a Characteristic for a selected ECU. Format mcTypeStatus mcCharacteristicWrite( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 *Values, u32 NumberOfValues); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is ori

### mcCharacteristicWrite

Purpose

Downloads scaled data to a Characteristic for a selected ECU.
Format

| mcTypeStatus | mcCharacteristicWrite( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 *Values, u32 NumberOfValues); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *CharacteristicName, |
| f64 | *Values, |
| u32 | NumberOfValues); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

Values

Values contains a pointer to a double, a double 1D, or 2D array which is sent to the ECU.

NumberOfValues

Specifies the number of values to write for the task.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicWrite writes the scaled value(s) of a named Characteristic to an ECU identified by the ECU reference handle ECURefNum.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicwritebytearray.html language=enus -->
## TOPIC 00020: mcCharacteristicWriteByteArray

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicwritebytearray.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicwritebytearray.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Downloads raw data as byte array (no scaling) to a Characteristic for a selected ECU. Format mcTypeStatus mcCharacteristicWriteByteArray( mcTypeTaskRef ECURefNum, char *CharacteristicName, u8 *Values, u32 NumberOfValues); Input ECURefNum ECURefNum is the task reference which links to the sel

### mcCharacteristicWriteByteArray

Purpose

Downloads raw data as byte array (no scaling) to a Characteristic for a selected ECU.
Format

| mcTypeStatus | mcCharacteristicWriteByteArray( mcTypeTaskRef ECURefNum, char *CharacteristicName, u8 *Values, u32 NumberOfValues); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *CharacteristicName, |
| u8 | *Values, |
| u32 | NumberOfValues); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

Values

Values contains a pointer to an unsigned 1D byte array which is sent to the ECU. The byte array corresponds to the memory area in the ECU representing this characteristic.

NumberOfValues

Specifies the number of values to write for the task.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicWriteByteArray writes the raw value(s) as byte array of a named Characteristic to an ECU identified by the ECU reference handle ECURefNum.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicwriteraw.html language=enus -->
## TOPIC 00021: mcCharacteristicWriteRaw

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicwriteraw.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicwriteraw.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Downloads raw data (no scaling) to a Characteristic for a selected ECU. Format mcTypeStatus mcCharacteristicWriteRaw( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 *Values, u32 NumberOfValues); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This refe

### mcCharacteristicWriteRaw

Purpose

Downloads raw data (no scaling) to a Characteristic for a selected ECU.
Format

| mcTypeStatus | mcCharacteristicWriteRaw( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 *Values, u32 NumberOfValues); |
| --- | --- |
| mcTypeTaskRef | ECURefNum |
| char | *CharacteristicName, |
| u64 | *Values, |
| u32 | NumberOfValues); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file.

Values

Values contains a pointer to an unsigned 64-bit integer, an unsigned 64-bit integer 1D, or 2D array which is sent to the ECU.

NumberOfValues

Specifies the number of values to write for the task.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicWriteRaw writes the raw value(s) of a named Characteristic to an ECU identified by the ECU reference handle ECURefNum.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicwriterawsinglevalue.html language=enus -->
## TOPIC 00022: mcCharacteristicWriteRawSingleValue

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicwriterawsinglevalue.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicwriterawsinglevalue.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes a single raw value (no scaling) to a named Characteristic on the ECU. Format mcTypeStatus mcCharacteristicWriteRawSingleValue( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 Value, u32 X, u32 Y); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. T

### mcCharacteristicWriteRawSingleValue

Purpose

Writes a single raw value (no scaling) to a named Characteristic on the ECU.
Format

| mcTypeStatus | mcCharacteristicWriteRawSingleValue( mcTypeTaskRef ECURefNum char *CharacteristicName, u64 Value, u32 X, u32 Y); |
| --- | --- |
| mcTypeTaskRef | ECURefNum |
| char | *CharacteristicName, |
| u64 | Value, |
| u32 | X, |
| u32 | Y); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file to which the values are written.

Value

Value contains the value which is sent to the ECU.

X

X refers to the array offset of the Characteristic defined in the A2L database file as 1- or 2-dimensional. If the Characteristic is defined as 0-dimensional, you can set X to 0.

Y

Y refers to the array offset of the Characteristic defined in the A2L database file as 2-dimensional. If the Characteristic is defined as 0- or 1-dimensional, you can set Y to 0.
Output

Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicWriteRawSingleValue writes a raw value to a named Characteristic on the ECU which is identified by the ECU Reference handle ECURefNum. The location to which the value is written is identified by the X and Y indices. If the Characteristic array is 0- or 1-dimensional, X and/or Y can be set to 0.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mccharacteristicwritesinglevalue.html language=enus -->
## TOPIC 00023: mcCharacteristicWriteSingleValue

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mccharacteristicwritesinglevalue.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mccharacteristicwritesinglevalue.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes a single scaled value to a named Characteristic on the ECU. Format mcTypeStatus mcCharacteristicWriteSingleValue( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 Value, u32 X, u32 Y); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This referenc

### mcCharacteristicWriteSingleValue

Purpose

Writes a single scaled value to a named Characteristic on the ECU.
Format

| mcTypeStatus | mcCharacteristicWriteSingleValue( mcTypeTaskRef ECURefNum, char *CharacteristicName, f64 Value, u32 X, u32 Y); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *CharacteristicName, |
| f64 | Value, |
| u32 | X, |
| u32 | Y); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

CharacteristicName

CharacteristicName is the name of the Characteristic defined in the A2L database file, to which the values are written.

Value

Value contains the value which is sent to the ECU.

X

X refers to the array offset of the Characteristic defined in the A2L database file as 1- or 2-dimensional. If the Characteristic is defined as 0-dimensional you can set X to 0.

Y

Y refers to the array offset of the Characteristic defined in the A2L database file as 2-dimensional. If the Characteristic is defined as 0- or 1-dimensional you can set Y to 0.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcCharacteristicWriteSingleValue writes a scaled value to a named Characteristic on the ECU which is identified by the ECU Reference handle ECURefNum. The location to which the value is written is identified by the X and Y indices. If the Characteristic array is 0- or 1-dimensional, Y and/or X can be set to 0.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcclearmemory.html language=enus -->
## TOPIC 00024: mcClearMemory

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcclearmemory.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcclearmemory.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Clears the contents of the specified ECU memory. Format mcTypeStatus mcClearMemory( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Address Configures the

### mcClearMemory

Purpose

Clears the contents of the specified ECU memory.
Format

| mcTypeStatus | mcClearMemory( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address, |
| u32 | BlockSize); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Configures the target address for the checksum operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the target address.

**Extension**

Extension contains the extension part of the target address.

BlockSize

BlockSize determines the size of the block on which the checksum must be calculated.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcClearMemory can be used to clear the contents of the non-volatile memory prior to reprogramming it. The Memory Transfer Address 0 (MTA 0) is set to the start of the memory block automatically by this function. The size parameter is the size of the block to be erased.

If you are using the XCP protocol, mcClearMemory implements the PROGRAM_CLEAR command. Refer to the ASAM XCP specification for further information on how to clear parts of non-volatile memory in the ECU.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcconversioncreate.html language=enus -->
## TOPIC 00025: mcConversionCreate

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcconversioncreate.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcconversioncreate.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates a signal conversion object in memory. Format mcTypeStatus mcConversionCreate( mcTypeTaskRef ECURefNum, char *ConversionName, f64 Factor, f64 Offset, char *Unit); Input ECURefNum ECURefNum is the task reference that links to the selected ECU. This reference is originally returned from

### mcConversionCreate

Purpose

Creates a signal conversion object in memory.
Format

| mcTypeStatus | mcConversionCreate( mcTypeTaskRef ECURefNum, char *ConversionName, f64 Factor, f64 Offset, char *Unit); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *ConversionName, |
| f64 | Factor, |
| f64 | Offset, |
| char | *Unit); |

Input

ECURefNum

ECURefNum is the task reference that links to the selected ECU. This reference is originally returned from [mcECUCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecucreate).

ConversionName

ConversionName identifies the conversion object that handles measurement scaling. Use this name as a reference in [mcMeasurementCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementcreate).

Factor

Factor configures the scaling factor used to convert raw measurement data in the message to/from scaled floating-point units. The factor is the A in the linear scaling formula AX+B, where X is the raw data, and B is the scaling offset.

Offset

Offset configures the scaling offset used to convert raw data in the measurement message to/from scaled floating-point units. The scaling offset is the B in the linear scaling formula AX+B, where X is the raw data, and A is the scaling factor.

Unit

Configures the measurement channel unit string. You can use this value to display units (such as volts or RPM) along with the channel samples.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

Use mcConversionCreate to create a conversion object in memory instead of referring to measurement properties defined in the A2L database.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqclear.html language=enus -->
## TOPIC 00026: mcDAQClear

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqclear.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqclear.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Stops communication for the Measurement task and clears the task. Format mcTypeStatus mcDAQClear( mcTypeTaskRef *DAQRefNum); Input DAQRefNum DAQRefNum is the task reference which links to the selected Measurement task. This reference is originally returned from . Output Return ValueThe retur

### mcDAQClear

Purpose

Stops communication for the Measurement task and clears the task.
Format

| mcTypeStatus | mcDAQClear( mcTypeTaskRef *DAQRefNum); |
| --- | --- |
| mcTypeTaskRef | *DAQRefNum); |

Input

DAQRefNum

DAQRefNum is the task reference which links to the selected Measurement task. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcDAQClear must always be the final function called for a Measurement task. If you do not use mcDAQClear, the remaining Measurement task configuration can cause problems in the execution of subsequent applications. Because this function clears the Measurement task, the Measurement task reference is not given as an output but is transferred into an ECU reference task handle. To change properties of a running Measurement task, use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to stop the task, [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) to change the desired DAQ property, then [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to restart the Measurement task.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqinitialize.html language=enus -->
## TOPIC 00027: mcDAQInitialize

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqinitialize.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqinitialize.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Initializes a Measurement task for the specified scaled Measurement channel list. Format mcTypeStatus mcDAQInitialize( cstr MeasurementNames, mcTypeTaskRef ECURefNum, i32 DAQMode, u32 DTO ID, f64 SampleRate, mcTypeTaskRef *DAQRefNum); Input MeasurementNames Comma-separated list of Measuremen

### mcDAQInitialize

Purpose

Initializes a Measurement task for the specified scaled Measurement channel list.
Format

| mcTypeStatus | mcDAQInitialize( cstr MeasurementNames, mcTypeTaskRef ECURefNum, i32 DAQMode, u32 DTO ID, f64 SampleRate, mcTypeTaskRef *DAQRefNum); |
| --- | --- |
| cstr | MeasurementNames, |
| mcTypeTaskRef | ECURefNum, |
| i32 | DAQMode, |
| u32 | DTO ID, |
| f64 | SampleRate, |
| mcTypeTaskRef | *DAQRefNum); |

Input

MeasurementNames

Comma-separated list of Measurement names to initialize as a task. You can type in the channel list as a string constant or you can obtain the list from an A2L database file by using the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function. Data for those Measurements will be scaled.

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

DAQMode

DAQMode specifies the I/O mode for the task. For an overview of the I/O modes, including figures, refer to the [Basic Programming Model](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_basic_programming_model) topic.

**mcDAQModeDAQList**

Data is transmitted automatically by the ECU using DAQ lists. The data can be read back with the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) as Single point data using sample rate = 0 or as waveform using a sample rate > 0. Input channel data is received from the DAQ messages.

**mcDAQModePolling**

In this mode the data from the Measurement task are uploaded from the ECU whenever the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) function is called.

**mcDAQModeSTIMList**

For XCP, this defines a DAQ list for data stimulation (STIM). Within a DAQ task initialized with this parameter, you can call [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqwrite](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqwrite) to write stimulation data to the ECU. Calling [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) is not allowed. For CCP, an error is returned.

**mcDAQModeDAQListTimeStamped**

The data is transmitted from the ECU in equidistant time intervals as defined in the A2L database. The data can be read back with [mcDAQReadTimestamped](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadtimestamped) as timestamped data array. Input channel data are received from the DAQ messages. Use [mcDAQReadTimestamped](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadtimestamped) to obtain input samples as an array of sample/timestamp pairs. Use this input mode to read samples with timestamps that indicate when each channel is received from the network.

DTO ID

DTO ID is the CAN identifier for the Data Transmission Object (DTO) used to transmit the data from the DAQ lists to the host. If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit). The default value is -1, which means that the DTO ID used to transmit the DAQ list data is the same that is used for the rest of the CCP communication. This is currently supported with CCP protocol and is being ignored with XCP.

SampleRate

SampleRate specifies the timing to use for samples of the Measurement task. The sample rate is specified in Hertz (samples per second). A sample rate of zero means to sample immediately.

For a DAQMode of **mcDAQModeDAQList**, SampleRate of zero means that [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) returns a single sample from the most recent messages received, and greater than zero means that [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) returns samples timed at the specified rate. For DAQMode of **mcDAQModePolling**, SampleRate is ignored.
Output

DAQRefNum

DAQRefNum is the reference handle for the Measurement task. Use this Measurement task reference in subsequent M&C DAQ functions for this task.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcDAQInitialize does not start the transmission of the DAQ lists on the ECU. This enables you to use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) to change the properties of a Measurement task. After you change properties, use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to start the transmission of the Measurement task.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqinitializeex.html language=enus -->
## TOPIC 00028: mcDAQInitializeEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqinitializeex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqinitializeex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Initializes a Measurement task for the specified scaled and raw (unscaled) Measurement channel lists. Format mcTypeStatus mcDAQInitializeEx( cstr MeasurementNames, cstr RawMeasurementNames, mcTypeTaskRef ECURefNum, i32 DAQMode, u32 DTO_ID, f64 SampleRate, mcTypeTaskRef *DAQRefNum); Input Mea

### mcDAQInitializeEx

Purpose

Initializes a Measurement task for the specified scaled and raw (unscaled) Measurement channel lists.
Format

| mcTypeStatus | mcDAQInitializeEx( cstr MeasurementNames, cstr RawMeasurementNames, mcTypeTaskRef ECURefNum, i32 DAQMode, u32 DTO_ID, f64 SampleRate, mcTypeTaskRef *DAQRefNum); |
| --- | --- |
| cstr | MeasurementNames, |
| cstr | RawMeasurementNames, |
| mcTypeTaskRef | ECURefNum, |
| i32 | DAQMode, |
| u32 | DTO_ID, |
| f64 | SampleRate, |
| mcTypeTaskRef | *DAQRefNum); |

Input

MeasurementNames

Comma-separated list of Measurement names added to the task. You can type in the channel list as a string constant or you can obtain the list from an A2L database file by using the [mcGetNames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function. Data for those Measurements will be scaled. At least one of the lists must be non-empty.

RawMeasurementNames

Comma-separated list of Measurement added to the task. You can type in the channel list as a string constant or you can obtain the list from an A2L database file by using the [mcGetNames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function. Data for those Measurements will be raw (no scaling). At least one of the lists must be non-empty.

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

DAQMode

DAQMode specifies the I/O mode for the task. For an overview of the I/O modes, refer to the [ECU M&C API Basic Programming Model](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_basic_programming_model) topic.

**mcDAQModeDAQList**

Data is transmitted automatically by the ECU using DAQ lists. The data can be read back with [mcDAQReadEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) as single point data using sample rate = 0, or as waveform using a sample rate > 0. Input channel data is received from the DAQ messages.

**mcDAQModePolling**

In this mode, the data from the Measurement task are uploaded from the ECU whenever [mcDAQReadEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) is called.

**mcDAQModeSTIMList**

For XCP, this defines a DAQ list for data stimulation (STIM). Within a DAQ task initialized with this parameter, you can call [mcDAQWriteEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqwriteex) to write stimulation data to the ECU. Calling [mcDAQReadEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) is not allowed. For CCP, an error is returned.

**mcDAQModeDAQListTimeStamped**

The data is transmitted from the ECU in equidistant time intervals as defined in the A2L database. The data can be read back with [mcDAQReadTimestampedEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadtimestampedex) as a timestamped data array. Input channel data are received from the DAQ messages. Use [mcDAQReadTimestampedEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadtimestampedex) to obtain input samples as an array of sample/timestamp pairs. Use this input mode to read samples with timestamps that indicate when each channel is received from the network.

DTO_ID

DTO_ID is the CAN identifier for the Data Transmission Object (DTO) used to transmit the data from the DAQ lists to the host. If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit). The default value is -1, which means that the DTO ID used to transmit the DAQ list data is the same that is used for the rest of the CCP communication. This is currently supported with CCP protocol and is being ignored with XCP.

SampleRate

SampleRate specifies the timing to use for samples of the Measurement task. The sample rate is specified in Hertz (samples per second). A sample rate of zero means to sample immediately.

For a DAQMode of **mcDAQModeDAQList**, a SampleRate of zero means that [mcDAQReadEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) returns a single sample from the most recent messages received, and greater than zero means that mcDAQReadEx returns samples timed at the specified rate. For a DAQMode of **mcDAQModePolling**, SampleRate is ignored.
Output

DAQRefNum

DAQRefNum is the reference handle for the Measurement task. Use this Measurement task reference in subsequent M&C DAQ functions for this task.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcDAQInitializeEx does not start the transmission of the DAQ lists on the ECU. This enables you to use [mcSetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) to change the properties of a Measurement task. After you change properties, use [mcDAQStartStop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to start the transmission of the Measurement task.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqlistinitialize.html language=enus -->
## TOPIC 00029: mcDAQListInitialize

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqlistinitialize.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqlistinitialize.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Defines a DAQ list on a specific DAQ list number and initializes the Measurement task for the specified scaled Measurement channel list. Format mcTypeStatus mcDAQListInitialize( cstr MeasurementNames, mcTypeTaskRef ECURefNum, i16 DAQListNo, i32 DAQMode, u32 DTO_ID, f64 SampleRate, mcTypeTask

### mcDAQListInitialize

Purpose

Defines a DAQ list on a specific DAQ list number and initializes the Measurement task for the specified scaled Measurement channel list.
Format

| mcTypeStatus | mcDAQListInitialize( cstr MeasurementNames, mcTypeTaskRef ECURefNum, i16 DAQListNo, i32 DAQMode, u32 DTO_ID, f64 SampleRate, mcTypeTaskRef *DAQRefNum); |
| --- | --- |
| cstr | MeasurementNames, |
| mcTypeTaskRef | ECURefNum, |
| i16 | DAQListNo, |
| i32 | DAQMode, |
| u32 | DTO_ID, |
| f64 | SampleRate, |
| mcTypeTaskRef | *DAQRefNum); |

Input

MeasurementNames

Comma-separated list of Measurement names to initialize as a task. You can type in the channel list as a string constant or you can obtain the list from an A2L database file by using the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function. Data for those Measurements will be scaled.

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

DAQListNoDAQListNo specifies which DAQ list entry number should be used for the defined Measurement channel list for the selected ECU. To query the available amount of DAQ List numbers on the ECU use mcPropECU_NumberOfDefinedDAQLists with the function [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty). To query the defined DAQ list numbers use mcPropECU_DAQListNumbers with [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty).

DAQMode

DAQMode specifies the I/O mode for the task. For an overview of the I/O modes, refer to the [ECU M&C API Basic Programming Model](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_basic_programming_model) topic.

**mcDAQModeDAQList**

Data is transmitted automatically by the ECU using DAQ lists. The data can be read back with the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) as Single point data using sample rate = 0 or as waveform using a sample rate > 0. Input channel data is received from the DAQ messages.

**mcDAQModePolling**

In this mode the data from the Measurement task are uploaded from the ECU whenever the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) function is called.

DTO_ID

DTO_ID is the CAN identifier for the Data Transmission Object (DTO) used to transmit the data from the DAQ lists to the host. If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit). The default value is -1, which means that the DTO ID used to transmit the DAQ list data is the same that is used for the rest of the CCP communication. This is currently supported with CCP protocol and is being ignored with XCP.

SampleRate

SampleRate specifies the timing to use for samples of the Measurement task. The sample rate is specified in Hertz (samples per second). A sample rate of zero means to sample immediately.

For a DAQMode of **mcDAQModeDAQList**, SampleRate of zero means that [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) returns a single sample from the most recent messages received, and greater than zero means that [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) returns samples timed at the specified rate. For DAQMode of **mcDAQModePolling**, SampleRate is ignored.
Output

DAQRefNum

DAQRefNum is the reference handle for the Measurement task. Use this Measurement task reference in subsequent M&C DAQ functions for this task.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If an ECU offers a reduced and specific range of DAQ list entry numbers use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqlistinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqlistinitialize) function to set up your Measurement list. mcDAQListInitialize does not start the transmission of the DAQ lists from the ECU to the application or vice versa through XCP or CCP. This enables you to use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) to change the properties of a Measurement task. After you change properties use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to start the communication for the Measurement task. To query the available DAQ list entry numbers use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) with the property mcPropECU_DAQListNumbers.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqlistinitializeex.html language=enus -->
## TOPIC 00030: mcDAQListInitializeEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqlistinitializeex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqlistinitializeex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Defines a DAQ list on a specific DAQ list number and initializes the Measurement task for the specified scaled and raw (unscaled) Measurement channel lists. Format mcTypeStatus mcDAQListInitializeEx( cstr MeasurementNames, cstr RawMeasurementNames, mcTypeTaskRef ECURefNum, i16 DAQListNo, i32

### mcDAQListInitializeEx

Purpose

Defines a DAQ list on a specific DAQ list number and initializes the Measurement task for the specified scaled and raw (unscaled) Measurement channel lists.
Format

| mcTypeStatus | mcDAQListInitializeEx( cstr MeasurementNames, cstr RawMeasurementNames, mcTypeTaskRef ECURefNum, i16 DAQListNo, i32 DAQMode, u32 DTO_ID, f64 SampleRate, mcTypeTaskRef *DAQRefNum); |
| --- | --- |
| cstr | MeasurementNames, |
| cstr | RawMeasurementNames, |
| mcTypeTaskRef | ECURefNum, |
| i16 | DAQListNo, |
| i32 | DAQMode, |
| u32 | DTO_ID, |
| f64 | SampleRate, |
| mcTypeTaskRef | *DAQRefNum); |

Input

MeasurementNames

Comma-separated list of Measurement names added to the task. You can type in the channel list as a string constant or you can obtain the list from an A2L database file by using the [mcGetNames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function. Data for those Measurements will be scaled. At least one of the lists must be non-empty.

RawMeasurementNames

Comma-separated list of Measurement added to the task. You can type in the channel list as a string constant or you can obtain the list from an A2L database file by using the [mcGetNames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function. Data for those Measurements will be raw (no scaling). At least one of the lists must be non-empty.

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

DAQListNo

DAQListNo specifies which DAQ list entry number should be used for the defined Measurement channel list for the selected ECU. To query the available amount of DAQ List numbers on the ECU, use **mcPropECU_NumberOfDefinedDAQLists** with the function [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty). To query the defined DAQ list numbers use **mcPropECU_DAQListNumbers** with [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty).

DAQMode

DAQMode specifies the I/O mode for the task. For an overview of the I/O modes, refer to the [ECU M&C API Basic Programming Model](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_basic_programming_model) topic.

**mcDAQModeDAQList**

Data is transmitted automatically by the ECU using DAQ lists. The data can be read back with [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) as single point data using sample rate = 0 or as waveform using a sample rate > 0. Input channel data is received from the DAQ messages.

**mcDAQModePolling**

In this mode the data from the Measurement task are uploaded from the ECU whenever [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) is called.

DTO_ID

DTO_ID is the CAN identifier for the Data Transmission Object (DTO) used to transmit the data from the DAQ lists to the host. If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit). The default value is -1, which means that the DTO ID used to transmit the DAQ list data is the same that is used for the rest of the CCP communication.

SampleRate

SampleRate specifies the timing to use for samples of the Measurement task. The sample rate is specified in Hertz (samples per second). A sample rate of zero means to sample immediately.

For a DAQMode of **mcDAQModeDAQList**, a SampleRate of zero means that [mcDAQReadEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqreadex) returns a single sample from the most recent messages received, and greater than zero means that mcDAQReadEx returns samples timed at the specified rate. For a DAQMode of **mcDAQModePolling**, SampleRate is ignored.
Output

DAQRefNum

DAQRefNum is the reference handle for the Measurement task. Use this Measurement task reference in subsequent M&C DAQ functions for this task.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If an ECU offers a reduced and specific range of DAQ list entry numbers, use the mcDAQListInitializeEx function to set up your Measurement list. mcDAQListInitializeEx does not start the transmission of the DAQ lists from the ECU to the application or vice versa through CCP or XCP. This enables you to use [mcSetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) to change the properties of a Measurement task. After you change properties use [mcDAQStartStop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to start the communication for the Measurement task. To query the available DAQ list entry numbers, use [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) with the property **mcPropECU_DAQListNumbers**.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqread.html language=enus -->
## TOPIC 00031: mcDAQRead

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqread.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqread.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads samples from a Measurement task. Samples are obtained from received CAN messages. Only scaled Measurements are acquired. Format mcTypeStatus mcDAQRead( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead, mcTypeTimestamp *StartTime, mcTypeTimestamp *DeltaTime, f64 *SampleArray, u32 *Num

### mcDAQRead

Purpose

Reads samples from a Measurement task. Samples are obtained from received CAN messages. Only scaled Measurements are acquired.
Format

| mcTypeStatus | mcDAQRead( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead, mcTypeTimestamp *StartTime, mcTypeTimestamp *DeltaTime, f64 *SampleArray, u32 *NumberOfSamplesReturned); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | NumberOfSamplesToRead, |
| mcTypeTimestamp | *StartTime, |
| mcTypeTimestamp | *DeltaTime, |
| f64 | *SampleArray, |
| u32 | *NumberOfSamplesReturned); |

Input

DAQRefNum

DAQRefNum is the task reference from the previous Measurement task function. The task reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize), and then reused by subsequent Measurement task functions.

NumberOfSamplesToRead

Specifies the number of samples to read for the task. For single-sample input, pass 1 to this parameter.
If the initialized sample rate is zero, you must pass NumberOfSamplesToRead no greater than 1. SampleRate of zero means mcDAQRead immediately returns a single sample from the most recent message(s) received.
Output

StartTime

Returns the time of the first CAN sample in SampleArray. This parameter is optional. If you pass NULL for the StartTime parameter, the mcDAQRead function proceeds normally. If the initialized sample rate is greater than zero, the StartTime is determined by the sample timing. If the initialized SampleRate is zero, the StartTime is zero, because the most recent sample is returned regardless of timing.

StartTime uses the mcTypeTimestamp data type. The mcTypeTimestamp data type is a 64-bit unsigned integer compatible with the Microsoft Win32 FILETIME type. This absolute time is kept in a Coordinated Universal Time (UTC) format. UTC time is loosely defined as the current date and time of day in Greenwich, England. Microsoft defines its UTC time (FILETIME) as a 64-bit counter of 100 ns intervals that have elapsed since 12:00 a.m., January 1, 1601. Because mcTypeTimestamp is compatible with Win32 FILETIME, you can pass it into the Win32 FileTimeToLocalFileTime function to convert it to the local time zone, and then pass the resulting local time to the Win32 FileTimeToSystemTime function to convert to the Win32 SYSTEMTIME type. SYSTEMTIME is a struct with fields for year, month, day, and so on. For more information on Win32 time types and functions, refer to the Microsoft Win32 documentation.

DeltaTime

Returns the time between each sample in SampleArray. This parameter is optional. If you pass NULL for the DeltaTime parameter, the mcDAQRead function proceeds normally. If the initialized sample rate is greater than zero, the DeltaTime is determined by the sample timing. If the initialized sample rate is zero, the DeltaTime is zero, because the most recent sample is returned regardless of timing. DeltaTime uses the mcTypeTimestamp data type. The delta time is a relative 64-bit counter of 100 ns intervals, not an absolute UTC time. Nevertheless, you can use functions like the Win32 FileTimeToSystemTime function to convert to the Win32 SYSTEMTIME type. In addition, you can use the 32-bit LowPart of DeltaTime to obtain a simple 100 ns count, because values for SampleRate as slow as 0.4 Hz are still limited to a 32-bit 100 ns count.

SampleArray

Returns a 2D array, one array for each scaled channel initialized in the task. The array of each channel must have NumberOfSamplesToRead entries allocated. The order of channel entries in SampleArray is the same as the order in the original channel list. If you need to determine the number of channels in the task after initialization, get the mcPropDAQ_NumChannels property for the task reference. If no message has been received since you started the task, 0 is returned as default value for of the channel in all entries of SampleArray.

NumberOfSamplesReturned

NumberOfSamplesReturned indicates the number of samples returned for each channel in SampleArray. The remaining entries are left unchanged (zero).

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If the initialized SampleRate is greater than zero, this function returns an array of samples, each of which indicates the value of the CAN channel at a specific point in time. The [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) function waits for these samples to arrive in time before returning. In other words, the SampleRate specifies a virtual clock that copies the most recent value from CAN messages for each sample time. The changes in sample values from message to message enable you to view the channel over time, such as for comparison with other CAN or DAQ input channels. To avoid internal waiting, you can use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) to obtain nctPropSamplesPending property, and pass that as the NumberOfSamplesToRead parameter to [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread).

If the initialized SampleRate is zero, [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) immediately returns a single sample from the most recent message(s) received. For this single-point read, you must pass the NumberOfSamplesToRead parameter as 1. You can use the return value of [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) to determine whether a new message has been received since the previous call to [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) (or [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop)). If no message has been received, the warning code mcWarningOldData is returned. If a new message has been received, the success code 0 is returned. If no message has been received since you started the task, the default value of the channel (nctPropChanDefaultValue) is returned in all entries of SampleArray.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqreadex.html language=enus -->
## TOPIC 00032: mcDAQReadEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqreadex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqreadex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads samples from a Measurement task. Samples are obtained from received CAN messages. Scaled and raw (unscaled) Measurements are acquired. Format mcTypeStatus mcDAQReadEx( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead mcTypeTimestamp *StartTime, mcTypeTimestamp *DeltaTime, f64 *Sample

### mcDAQReadEx

Purpose

Reads samples from a Measurement task. Samples are obtained from received CAN messages. Scaled and raw (unscaled) Measurements are acquired.
Format

| mcTypeStatus | mcDAQReadEx( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead mcTypeTimestamp *StartTime, mcTypeTimestamp *DeltaTime, f64 *SampleArray, u64 *RawSampleArray, u32 *NumberOfSamplesReturned); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | NumberOfSamplesToRead |
| mcTypeTimestamp | *StartTime, |
| mcTypeTimestamp | *DeltaTime, |
| f64 | *SampleArray, |
| u64 | *RawSampleArray, |
| u32 | *NumberOfSamplesReturned); |

Input

DAQRefNum

DAQRefNum is the task reference from the previous Measurement task function. The task reference is originally returned from [mcDAQInitializeEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializeex), and then reused by subsequent Measurement task functions.

NumberOfSamplesToRead

Specifies the number of samples to read for the task. For single-sample input, pass 1 to this parameter.

If the initialized sample rate is zero, you must pass **NumberOfSamplesToRead** no greater than 1. A SampleRate of zero means mcDAQReadEx immediately returns a single sample from the most recent message(s) received.
Output

StartTime

Returns the time of the first CAN sample in SampleArray (or in RawSampleArray if no scaled Measurements are defined). This parameter is optional. If you pass NULL for the StartTime parameter, the mcDAQReadEx function proceeds normally. If the initialized sample rate is greater than zero, the StartTime is determined by the sample timing. If the initialized SampleRate is zero, the StartTime is zero, because the most recent sample is returned regardless of timing.

StartTime uses the mcTypeTimestamp data type. The mcTypeTimestamp data type is a 64-bit unsigned integer compatible with the Microsoft Win32 FILETIME type. This absolute time is kept in a Coordinated Universal Time (UTC) format. UTC time is loosely defined as the current date and time of day in Greenwich, England. Microsoft defines its UTC time (FILETIME) as a 64-bit counter of 100 ns intervals that have elapsed since 12:00 a.m., January 1, 1601. Because mcTypeTimestamp is compatible with Win32 FILETIME, you can pass it into the Win32 FileTimeToLocalFileTime function to convert it to the local time zone, and then pass the resulting local time to the Win32 FileTimeToSystemTime function to convert to the Win32 SYSTEMTIME type. SYSTEMTIME is a struct with fields for year, month, day, and so on. For more information on Win32 time types and functions, refer to the Microsoft Win32 documentation.

DeltaTime

Returns the time between each sample in (Raw)SampleArray. This parameter is optional. If you pass NULL for the DeltaTime parameter, the mcDAQReadEx function proceeds normally. If the initialized sample rate is greater than zero, the DeltaTime is determined by the sample timing. If the initialized sample rate is zero, the DeltaTime is zero, because the most recent sample is returned regardless of timing. DeltaTime uses the mcTypeTimestamp data type. The delta time is a relative 64-bit counter of 100 ns intervals, not an absolute UTC time. Nevertheless, you can use functions like the Win32 FileTimeToSystemTime function to convert to the Win32 SYSTEMTIME type. In addition, you can use the 32-bit LowPart of DeltaTime to obtain a simple 100 ns count, because values for SampleRate as slow as 0.4 Hz are still limited to a 32-bit 100 ns count.

SampleArray

Returns a 2D array, one array for each scaled channel initialized in the task. The array of each channel must have NumberOfSamplesToRead entries allocated. The order of channel entries in SampleArray is the same as the order in the original channel list. If you need to determine the number of channels in the task after initialization, get the mcPropDAQ_NumChannels property for the task reference. If no message has been received since you started the task, 0 is returned as default value for of the channel in all entries of SampleArray.

RawSampleArray

Returns a 2D array, one array for each raw channel initialized in the task. The array of each channel must have NumberOfSamplesToRead entries allocated. The order of channel entries in RawSampleArray is the same as the order in the original channel list. If you need to determine the number of channels in the task after initialization, get the mcPropDAQ_NumRawChannels property for the task reference. If no message has been received since you started the task, 0 is returned as default value for of the channel in all entries of RawSampleArray.

NumberOfSamplesReturned

NumberOfSamplesReturned indicates the number of samples returned for each channel in SampleArray and RawSampleArray. The remaining entries are left unchanged (zero).

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If the initialized SampleRate is greater than zero, this function returns an array of samples, each of which indicates the value of the CAN channel at a specific point in time. The mcDAQReadEx function waits for these samples to arrive in time before returning. In other words, the SampleRate specifies a virtual clock that copies the most recent value from CAN messages for each sample time. The changes in sample values from message to message enable you to view the channel over time, such as for comparison with other CAN or DAQ input channels. To avoid internal waiting, you can use [mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) to obtain nctPropSamplesPending property, and pass that as the NumberOfSamplesToRead parameter to mcDAQReadEx.

If the initialized SampleRate is zero, mcDAQReadEx immediately returns a single sample from the most recent message(s) received. For this single-point read, you must pass the NumberOfSamplesToRead parameter as 1. You can use the return value of mcDAQReadEx to determine whether a new message has been received since the previous call to mcDAQReadEx (or mcDAQStartStop). If no message has been received, the warning code mcWarningOldData is returned. If a new message has been received, the success code 0 is returned. If no message has been received since you started the task, the default value of the channel (nctPropChanDefaultValue) is returned in all entries of (Raw)SampleArray.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqreadtimestamped.html language=enus -->
## TOPIC 00033: mcDAQReadTimestamped

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqreadtimestamped.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqreadtimestamped.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads timestamped scaled samples from a DAQ task initialized with the selected mode of mcDAQModeDAQListTimeStamped. Format mcTypeStatus mcDAQReadTimestamped( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead, i64 *TimestampArray, double *SampleArray, u32 *NumberOfSamplesReturned); Input DAQ

### mcDAQReadTimestamped

Purpose

Reads timestamped scaled samples from a DAQ task initialized with the selected mode of mcDAQModeDAQListTimeStamped.
Format

| mcTypeStatus | mcDAQReadTimestamped( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead, i64 *TimestampArray, double *SampleArray, u32 *NumberOfSamplesReturned); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | NumberOfSamplesToRead, |
| i64 | *TimestampArray, |
| double | *SampleArray, |
| u32 | *NumberOfSamplesReturned); |

Input

DAQRefNum

DAQRefNum is the task reference that links to the selected measurement task. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize) or [mcDAQListInitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqlistinitialize).

NumberOfSamplesToRead

Specifies the number of samples to read for the task.
Output

TimestampArray

Returns the time at which each corresponding sample in SampleArray was received in a CAN message. The timestamps are returned as an array of arrays (2D array), one array for each channel initialized in the task. The array of each channel must have NumberOfSamplesToRead entries allocated. For example, if you call [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize) with MeasurementNames of myDAQ1,myDAQ2, and then call mcDAQReadTimestamped with NumberOfSamplesToRead of 20, both TimestampArray and SampleArray must be allocated as:

i64 mcTypeTimestamp TimestampArray[2][20];
 double SampleArray[2][20];

The order of channel entries in TimestampArray is the same as the order in the original DAQ channel list. To determine the number of channels in the DAQ task after initialization, get the mcPropDAQ_NumChannels property for the DAQ task reference. Each timestamp in TimestampArray uses the i64 data type compatible with the Microsoft Win32 FILETIME type. This absolute time is kept in a Coordinated Universal Time (UTC) format. UTC time is loosely defined as the current date and time of day in Greenwich, England. Microsoft defines its UTC time (FILETIME) as a 64-bit counter of 100 ns intervals that have elapsed since 12:00 a.m., January 1, 1601. Because the timestamp is compatible with Win32 FILETIME, you can pass it into the Win32 FileTimeToLocalFileTime function to convert it to the local timezone, and then pass the resulting local time to the Win32 FileTimeToSystemTime function to convert to the Win32 SYSTEMTIME type. SYSTEMTIME is a struct with fields for year, month, day, and so on. For more information about Win32 time types and functions, refer to the Microsoft Win32 documentation.

SampleArray

SampleArray returns the scaled sample value(s) for each received CAN message. The samples are returned as an array of arrays (a 2D array), one array for each scaled channel initialized in the DAQ task. The array of each channel must have NumberOfSamplesToRead entries allocated. You must allocate SampleArray exactly as TimestampArray, and the order of channel entries is the same for both.

NumberOfSamplesReturned

Indicates the number of samples returned for each channel in SampleArray, and the number of timestamps returned for each channel in TimestampArray. The remaining entries are left unchanged (zero).

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

Each returned sample corresponds to a received CAN message for the measurement channels initialized in the DAQ channel list. For each sample, mcDAQReadTimestamped returns the sample value and a timestamp that indicates when the message was received. Because the timing of samples returned by mcDAQReadTimestamped is determined by when the message is received, the initialized sample rate is not used.

The function waits until NumberOfSamplesToRead messages have been received. The number of samples returned is indicated in the NumberOfSamplesReturned output, up to a maximum of NumberOfSamplesToRead messages. If no new message has been received, NumberOfSamplesReturned is 0, and the return value indicates success. To avoid blocking a mcDAQReadTimestamped function, read the mcPropDAQ_SamplesPending property to check the number of collected sample points before calling mcDAQReadTimestamped.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqreadtimestampedex.html language=enus -->
## TOPIC 00034: mcDAQReadTimestampedEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqreadtimestampedex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqreadtimestampedex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads timestamped scaled and timestamped raw (unscaled) samples from a DAQ task initialized with the selected mode of mcDAQModeDAQListTimeStamped. Format mcTypeStatus mcDAQReadTimestampedEx( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead, i64 *TimestampArray, double *SampleArray, u64 *Ra

### mcDAQReadTimestampedEx

Purpose

Reads timestamped scaled and timestamped raw (unscaled) samples from a DAQ task initialized with the selected mode of mcDAQModeDAQListTimeStamped.
Format

| mcTypeStatus | mcDAQReadTimestampedEx( mcTypeTaskRef DAQRefNum, u32 NumberOfSamplesToRead, i64 *TimestampArray, double *SampleArray, u64 *RawSampleArray, u32 *NumberOfSamplesReturned); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | NumberOfSamplesToRead, |
| i64 | *TimestampArray, |
| double | *SampleArray, |
| u64 | *RawSampleArray, |
| u32 | *NumberOfSamplesReturned); |

Input

DAQRefNum

DAQRefNum is the task reference that links to the selected measurement task. This reference is originally returned from [mcDAQInitializeEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializeex) or [mcDAQListInitializeEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqlistinitializeex).

NumberOfSamplesToRead

Specifies the number of samples to read for the task.
Output

TimestampArray

Returns the time at which each corresponding sample in SampleArray and RawSampleArray was received in a CAN message. The timestamps are returned as an array of arrays (2D array), one array for each channel initialized in the task. The array of each channel must have NumberOfSamplesToRead entries allocated. For example, if you call [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializeex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializeex) with MeasurementNames of myDAQ1,myDAQ2, and then call mcDAQReadTimestampedEx with NumberOfSamplesToRead of 20, TimestampArray, SampleArray, and RawSampleArray must be allocated as:

```text
    i64 mcTypeTimestamp TimestampArray[3][20];
    double SampleArray[2][20];
    u64 RawSampleArray[1][20];
```

The order of channel entries in TimestampArray is the same as the order in the original DAQ channel lists, i.e. first all scaled Measurements and then all raw Measurements. To determine the number of channels in the DAQ task after initialization, get the mcPropDAQ_NumChannels and mcPropDAQ_NumRawChannels properties for the DAQ task reference. Each timestamp in TimestampArray uses the i64 data type compatible with the Microsoft Win32 FILETIME type. This absolute time is kept in a Coordinated Universal Time (UTC) format. UTC time is loosely defined as the current date and time of day in Greenwich, England. Microsoft defines its UTC time (FILETIME) as a 64-bit counter of 100 ns intervals that have elapsed since 12:00 a.m., January 1, 1601. Because the timestamp is compatible with Win32 FILETIME, you can pass it into the Win32 FileTimeToLocalFileTime function to convert it to the local timezone, and then pass the resulting local time to the Win32 FileTimeToSystemTime function to convert to the Win32 SYSTEMTIME type. SYSTEMTIME is a struct with fields for year, month, day, and so on. For more information about Win32 time types and functions, refer to the Microsoft Win32 documentation.

SampleArray

SampleArray returns the scaled sample value(s) for each received CAN message. The samples are returned as an array of arrays (a 2D array), one array for each scaled channel initialized in the DAQ task. The array of each channel must have NumberOfSamplesToRead entries allocated. You must allocate SampleArray similar to TimestampArray. TimestampArray has entries for both SampleArray and RawSampleArray. If you have N-many scaled channels, M-many raw channels, and K is NumberOfSamplesToRead, then you need the following arrays:

```text
    i64 mcTypeTimestamp TimestampArray[N+M][K];
    double SampleArray[N][K];
    u64 RawSampleArray[M][K];
```

The order of channel entries is the same as the two original channel lists used for initialization, i.e. first the scaled Measurements, and then the raw Measurements.

RawSampleArray

RawSampleArray returns the raw sample value(s) for each received CAN message. The samples are returned as an array of arrays (a 2D array), one array for each raw channel initialized in the DAQ task. The array of each channel must have NumberOfSamplesToRead entries allocated. You must allocate RawSampleArray similar to TimestampArray. TimestampArray has entries for both SampleArray and RawSampleArray. If you have N-many scaled channels, M-many raw channels, and K is NumberOfSamplesToRead, then you need the following arrays:

```text
    i64 mcTypeTimestamp TimestampArray[N+M][K];
    double SampleArray[N][K];
    u64 RawSampleArray[M][K];
```

The order of channel entries is the same as the two original channel lists used for initialization, i.e. first the scaled Measurements, and then the raw Measurements. All arrays return the same number of samples.

NumberOfSamplesReturned

Indicates the number of samples returned for each channel in SampleArray and RawSampleArray, and the number of timestamps returned for each channel in TimestampArray. All arrays return the same number of samples but TimestampArray has as many channels as the sum of channels in SampleArray and RawSampleArray. The remaining entries are left unchanged (zero).

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

Each returned sample corresponds to a received CAN message for the measurement channels initialized in the DAQ channel lists. For each sample, mcDAQReadTimestamped returns the sample value and a timestamp that indicates when the message was received. Because the timing of samples returned by mcDAQReadTimestamped is determined by when the message is received, the initialized sample rate is not used.

The function waits until NumberOfSamplesToRead messages have been received. The number of samples returned is indicated in the NumberOfSamplesReturned output, up to a maximum of NumberOfSamplesToRead messages. If no new message has been received, NumberOfSamplesReturned is 0, and the return value indicates success. To avoid a blocking mcDAQReadTimestamped function, read the property mcPropDAQ_SamplesPending to check the number of collected sample points before calling mcDAQReadTimestamped.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqstartstop.html language=enus -->
## TOPIC 00035: mcDAQStartStop

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqstartstop.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqstartstop.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Starts or stops the transmission of the DAQ lists assigned to the Measurement task on the ECU. Format mcTypeStatus mcDAQStartStop( mcTypeTaskRef DAQRefNum, u32 StartStopMode); Input DAQRefNum DAQRefNum is the task reference from the previous Measurement task function. The task reference is o

### mcDAQStartStop

Purpose

Starts or stops the transmission of the DAQ lists assigned to the Measurement task on the ECU.
Format

| mcTypeStatus | mcDAQStartStop( mcTypeTaskRef DAQRefNum, u32 StartStopMode); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | StartStopMode); |

Input

DAQRefNum

DAQRefNum is the task reference from the previous Measurement task function. The task reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize), and then reused by subsequent Measurement task functions.

StartStopMode

StartStopMode indicates the type of function to be performed.

0—mcStartStopModeStop

Configures the ECU to stop transmitting a DAQ task. If stopped, properties of the DAQ task can be changed using [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty). This function is performed automatically before [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqclear](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqclear).

1—mcStartStopModeStart

Configures the ECU to start sending data for a Measurement task. Ensure that the DAQ list has not yet been transferred to the ECU first. Once started, properties of the DAQ list can no longer be changed using [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty). This function is performed automatically before the first read of the DAQ list with [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread).

2—mcStartStopModeTransmitDAQ

Transfers the DAQ list to the ECU, but does not start it. For example, use this mode if you want to change the session status before starting the DAQ list. For some ECUs this is necessary.

3—mcStartStopModePrepareStartAll

Prepares a DAQ or STIM list to be started by a single command. This is useful when multiple DAQ or STIM lists are used with the same ECU. After preparing the DAQ or STIM lists with this command, use mcDAQStartStop with mode mcStartStopModeStartAll to start all lists at the same time.

4—mcStartStopModeStartAll

Starts all previously prepared DAQ or STIM lists at the same time with a single command.

5—mcStartStopModeStopAll

Stops all running DAQ or STIM lists on the same ECU with a single command.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) is an optional command to start or stop communication for an M&C Measurement task. If you do not perform [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) (with the parameter mcStartStopModeStart) before using [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread) the Measurement task is started by the first call of [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqread). After you start the transmission of the DAQ lists, you can no longer change the configuration of the Measurement task with [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty). You must call [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) (with the parameter mcStartStopModeStop) first.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqwrite.html language=enus -->
## TOPIC 00036: mcDAQWrite

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqwrite.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqwrite.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes scaled samples to an ECU DAQ list. Format mcTypeStatus mcDAQWrite( mcTypeTaskRef DAQRefNum, u32 NumberofSamplesToWrite, f64 *SampleArray); Input DAQRefNum DAQRefNum is the task reference from the previous Measurement task function. The task reference is originally returned from , and

### mcDAQWrite

Purpose

Writes scaled samples to an ECU DAQ list.
Format

| mcTypeStatus | mcDAQWrite( mcTypeTaskRef DAQRefNum, u32 NumberofSamplesToWrite, f64 *SampleArray); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | NumberofSamplesToWrite, |
| f64 | *SampleArray); |

Input

DAQRefNum

DAQRefNum is the task reference from the previous Measurement task function. The task reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize), and then reused by subsequent Measurement task functions.

NumberofSamplesToWrite

NumberofSamplesToWrite specifies the number of samples to write for the ECU MC DAQ task to the ECU DAQ list. For single-sample output, pass 1 to this parameter. The initialized DAQ sample rate is ignored. mcDAQWrite immediately writes a single sample to the ECU when calling the mcDAQWrite function.

SampleArray

SampleArray specifies a 2D array, one array for each scaled channel initialized in the task. The array of each channel must have NumberOfSamplesToWrite entries allocated. The order of channel entries in SampleArray is the same as the order in the original MeasurementNames. If you must determine the number of channels in the task after initialization, get the mcPropDAQ_NumChannels property for the task reference.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

For XCP STIM lists (refer to [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize)), [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqwrite](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqwrite) transfers an array of samples to the ECU. These samples are called data stimulation packets (STIM). On the ECU side the STIM processor buffers incoming data stimulation packets. When an event occurs, which triggers a DAQ list in data stimulation mode, the buffered data is transferred to the memory on the slave device.

XCP Part 2 Protocol Layer Specification

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdaqwriteex.html language=enus -->
## TOPIC 00037: mcDAQWriteEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdaqwriteex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdaqwriteex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes scaled and raw samples to an ECU DAQ list. Format mcTypeStatus mcDAQWriteEx( mcTypeTaskRef DAQRefNum, u32 NumberofSamplesToWrite, f64 *SampleArray u64 *RawSampleArray); Input DAQRefNum DAQRefNum is the task reference from the previous Measurement task function. The task reference is o

### mcDAQWriteEx

Purpose

Writes scaled and raw samples to an ECU DAQ list.
Format

| mcTypeStatus | mcDAQWriteEx( mcTypeTaskRef DAQRefNum, u32 NumberofSamplesToWrite, f64 *SampleArray u64 *RawSampleArray); |
| --- | --- |
| mcTypeTaskRef | DAQRefNum, |
| u32 | NumberofSamplesToWrite, |
| f64 | *SampleArray |
| u64 | *RawSampleArray); |

Input

DAQRefNum

DAQRefNum is the task reference from the previous Measurement task function. The task reference is originally returned from [mcDAQInitializeEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializeex), and then reused by subsequent Measurement task functions.

NumberofSamplesToWrite

NumberofSamplesToWrite specifies the number of samples to write for the ECU MC DAQ task to the ECU DAQ list. For single-sample output, pass 1 to this parameter. The initialized DAQ sample rate is ignored. mcDAQWriteEx immediately writes a single sample to the ECU when calling the mcDAQWriteEx function.

SampleArray

SampleArray specifies a 2D array, one array for each scaled channel initialized in the task. The array of each channel must have NumberOfSamplesToWrite entries allocated. The order of channel entries in SampleArray is the same as the order in the original MeasurementNames. If you must determine the number of channels in the task after initialization, get the mcPropDAQ_NumChannels property for the task reference.

RawSampleArray

RawSampleArray specifies a 2D array, one array for each raw channel initialized in the task. The array of each channel must have NumberOfSamplesToWrite entries allocated. The order of channel entries in RawSampleArray is the same as the order in the original RawMeasurementNames. If you must determine the number of channels in the task after initialization, get the mcPropDAQ_NumRawChannels property for the task reference.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

For XCP STIM lists (refer to [mcDAQInitializeEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitializeex)), mcDAQWriteEx transfers an array of samples to the ECU. These samples are called data stimulation packets (STIM). On the ECU side the STIM processor buffers incoming data stimulation packets. When an event occurs, which triggers a DAQ list in data stimulation mode, the buffered data is transferred to the memory on the slave device.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to configure data stimulation.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdatabaseclose.html language=enus -->
## TOPIC 00038: mcDatabaseClose

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdatabaseclose.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdatabaseclose.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Closes a specified A2L Database. Format mcTypeStatus mcDatabaseClose( mcTypeTaskRef *DBRefNum); Input DBRefNum DBRefNum is the task reference from the initial database task function. The database task reference is originally returned from . Output Return ValueThe return value indicates the s

### mcDatabaseClose

Purpose

Closes a specified A2L Database.
Format

| mcTypeStatus | mcDatabaseClose( |
| --- | --- |
| mcTypeTaskRef | *DBRefNum); |

Input

DBRefNum

DBRefNum is the task reference from the initial database task function. The database task reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseopen](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseopen).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcDatabaseClose must always be the final ECU M&C function called for each database task. If you do not use the mcDatabaseClose function, the remaining task configurations can cause problems in the execution of subsequent Measurement and Calibration applications.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdatabaseopen.html language=enus -->
## TOPIC 00039: mcDatabaseOpen

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdatabaseopen.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdatabaseopen.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Opens a specified A2L Database. Format mcTypeStatus mcDatabaseOpen( cstr Database, mcTypeTaskRef *DBRefNum); Input Database Database is a path to an A2L database file containing the information to access Measurements and Characteristics inside the ECU. The file must use an .A2L extension. Yo

### mcDatabaseOpen

Purpose

Opens a specified A2L Database.
Format

| mcTypeStatus | mcDatabaseOpen( cstr Database, mcTypeTaskRef *DBRefNum); |
| --- | --- |
| cstr | Database, |
| mcTypeTaskRef | *DBRefNum); |

Input

Database

Database is a path to an A2L database file containing the information to access Measurements and Characteristics inside the ECU. The file must use an .A2L extension. You can generate A2L database files with several third-party tools.

You can also create an empty database in memory, then add objects to this database programmatically. For in-memory database use the syntax :<myname>:. You can use multiple databases in memory at the same time (e.g., :MyDatabase1: and :MyDatabase2:).

DBRefNum

DBRefNum is the database reference returned from this function. At the end of the application, the reference must be closed with [mcDatabaseClose](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseclose).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

The mcDatabaseOpen and mcDatabaseOpenEx functions open the database but do not start communication. If you are using a path to an existing A2L database with this function, you can query all defined ECU names in the A2L database using the [mcGetNames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function and select the ECU with [mcECUSelect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

If you are using in-memory database (see **Database** parameter), you can create an ECU object using [mcECUCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecucreate), a scaling object using [mcConversionCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcconversioncreate), a measurement object using [mcMeasurementCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementcreate), and an event using [mcEventCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mceventcreate). Characteristics are currently not supported with in-memory databases.

To use the ECU M&C Toolkit on a LabVIEW RT system with an ASAM MCD 2MC database (*.A2L), you must download your A2L file to the RT target.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdatabaseopenex.html language=enus -->
## TOPIC 00040: mcDatabaseOpenEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdatabaseopenex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdatabaseopenex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Opens a specified A2L Database. Format mcTypeStatus mcDatabaseOpenEx( cstr Database, mcTypeTaskRef *DBRefNum, cstr Reserved); Input Database Database is a path to an A2L database file containing the information to access Measurements and Characteristics inside the ECU. The file must use an .

### mcDatabaseOpenEx

Purpose

Opens a specified A2L Database.
Format

| mcTypeStatus | mcDatabaseOpenEx( cstr Database, mcTypeTaskRef *DBRefNum, cstr Reserved); |
| --- | --- |
| cstr | Database, |
| mcTypeTaskRef | *DBRefNum, |
| cstr | Reserved); |

Input

Database

Database is a path to an A2L database file containing the information to access Measurements and Characteristics inside the ECU. The file must use an .A2L extension. You can generate A2L database files with several third-party tools.

You can also create an empty database in memory, then add objects to this database programmatically. For in-memory database use the syntax :<myname>:. You can use multiple databases in memory at the same time (e.g., :MyDatabase1: and :MyDatabase2:).

DBRefNum

DBRefNum is the database reference returned from this function. At the end of the application, the reference must be closed with [mcDatabaseClose](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseclose).

Reserved

Reserved for future use. Set this parameter to empty string "".
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

The mcDatabaseOpen and mcDatabaseOpenEx functions open the database but do not start communication. If you are using a path to an existing A2L database with this function, you can query all defined ECU names in the A2L database using the [mcGetNames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) function and select the ECU with [mcECUSelect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

If you are using in-memory database (see **Database** parameter), you can create an ECU object using [mcECUCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecucreate), a scaling object using [mcConversionCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcconversioncreate), a measurement object using [mcMeasurementCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementcreate), and an event using [mcEventCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mceventcreate). Characteristics are currently not supported with in-memory databases.

To use the ECU M&C Toolkit on a LabVIEW RT system with an ASAM MCD 2MC database (*.A2L), you must download your A2L file to the RT target.

Note

Reserved

mcDatabaseOpen

mcDatabaseOpenEx

mcDatabaseOpen

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdoubletotext.html language=enus -->
## TOPIC 00041: mcDoubleToText

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdoubletotext.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdoubletotext.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts a numerical value to a text string using an enumeration or range text type scaling. Format mcTypeStatus mcDoubleToText( mcTypeTaskRef ECURefNum, u32 ObjectType, cstr ObjectName, double Value, u32 SizeOfTextValue, str TextValue); Input ECURefNum ECURefNum is the task reference which

### mcDoubleToText

Purpose

Converts a numerical value to a text string using an enumeration or range text type scaling.
Format

| mcTypeStatus | mcDoubleToText( mcTypeTaskRef ECURefNum, u32 ObjectType, cstr ObjectName, double Value, u32 SizeOfTextValue, str TextValue); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u32 | ObjectType, |
| cstr | ObjectName, |
| double | Value, |
| u32 | SizeOfTextValue, |
| str | TextValue); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

ObjectType

Indicates the type of the object named in ObjectName. Valid values are:

| 1 | Measurement Name |
| --- | --- |
| 2 | Characteristic Name |

ObjectName

Indicates the object (measurement or characteristic) for which the COMPU_VTAB scaling is performed. If no COMPU_VTAB scaling is available for the object, TextValue is just a string representation of the value specified in Value.

Value

The numerical value to be converted. For example, this could have been returned from [mcCharacteristicRead](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mccharacteristicread) or [mcMeasurementRead](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementread).

SizeOfTextValue

Must contain the number of bytes in the buffer passed to TextValue. Note that there is no way of requesting the necessary size of this buffer. If you do not know up front how long your text could become, specify a buffer of 256 bytes. This is the maximum the ASAM standard allows.
Output

TextValue

The buffer for the resulting converted text string. If the Value specified is listed in a COMPU_VTAB scaling for the characteristic or measurement specified in ObjectName, the respective text is returned. If no such value is available, a string representation of the double value is returned.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcDoubleToText performs text conversion for measurement or characteristic values. Especially if the measurement or characteristic has an associated COMPU_VTAB type scaling, the textual representation of the value is returned. If no such value is present, either because the object does not have a text scaling or the value does not have a textual representation in the table, a string representation of the double value is returned.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcdownload.html language=enus -->
## TOPIC 00042: mcDownload

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcdownload.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcdownload.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Downloads data to an ECU. Format mcTypeStatus mcDownload( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *Data); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Address Configures the target address

### mcDownload

Purpose

Downloads data to an ECU.
Format

| mcTypeStatus | mcDownload( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *Data); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address, |
| u32 | BlockSize, |
| u8 | *Data); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Configures the target address for the download operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the target address.

**Extension**

Extension contains the extension part of the target address.

BlockSize

BlockSize determines the size of the data block to be downloaded.
Output

Data

Data pointer to the information to be downloaded.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcDownload downloads data to an ECU. The data is stored starting at the selected **Address** and **Extension** in the ECU memory. The function can download more than 5 data bytes to the ECU.

If you are using the CCP protocol and the selected BlockSize is higher than 5 bytes, mcDownload performs several CCP DNLOAD commands until all data bytes are downloaded to the ECU. mcDownload implements the CCP DNLOAD command defined by the CCP specification.

If you are using the XCP protocol, the Data block of the specified BlockSize is copied into the ECU memory, starting at the MTA. The MTA is post-incremented by the number of downloaded data bytes. If the slave device does not support Block Transfer Mode, all downloaded data is transferred in a single command packet. If Block Transfer Mode is supported, the downloaded data is transferred in multiple command packets. For the slave however, there might be limitations concerning the maximum number of consecutive command packets, so the number of data elements may be within a limited range. The master device has two additional consecutive DOWNLOAD_NEXT command packets. The slave device will acknowledge only the last DOWNLOAD_NEXT command packet. The separation time between the command packets and the maximum number of packets are specified in the response for the CONNECT command.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecuconnect.html language=enus -->
## TOPIC 00043: mcECUConnect

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecuconnect.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecuconnect.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Establishes communication to the selected ECU through XCP or CCP. After a successful ECU Connect you can create a Measurement task or read/write a Characteristic. Format mcTypeStatus mcECUConnect( mcTypeTaskRef ECURefNum); Input ECURefNum ECURefNum is the task reference which links to the se

### mcECUConnect

Purpose

Establishes communication to the selected ECU through XCP or CCP. After a successful ECU Connect you can create a Measurement task or read/write a Characteristic.
Format

| mcTypeStatus | mcECUConnect( |
| --- | --- |
| mcTypeTaskRef | ECURefNum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcECUConnect implements the XCP or CCP CONNECT command. It establishes a logical connection to an ECU, using the provided ECU Reference handle ECURefNum. Unless a slave device (ECU) is unconnected, it must not execute or respond to any command sent by the application. The only exception to this rule is the Test command, to which the XCP or CCP slave with the specific address may return an acknowledgement. Only a single XCP or CCP slave can be connected to the application at a time.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecuconnect2.html language=enus -->
## TOPIC 00044: mcECUConnect2

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecuconnect2.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecuconnect2.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Establishes communication to the selected ECU through XCP or CCP. After a successful ECU Connect you can create a Measurement task or read/write a Characteristic. Format mcTypeStatus mcECUConnect2( mcTypeTaskRef ECURefNum, u8 ECUMode); Input ECURefNum ECURefNum is the task reference which li

### mcECUConnect2

Purpose

Establishes communication to the selected ECU through XCP or CCP. After a successful ECU Connect you can create a Measurement task or read/write a Characteristic.
Format

| mcTypeStatus | mcECUConnect2( mcTypeTaskRef ECURefNum, u8 ECUMode); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, u8 ECUMode); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

ECUMode

ECUMode is the mode parameter for the CONNECT command, used only with XCP, user-defined. The default is 0 (normal mode).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcECUConnect2 implements the XCP or CCP CONNECT command. It establishes a logical connection to an ECU, using the provided ECU Reference handle ECURefNum. Unless a slave device (ECU) is unconnected, it must not execute or respond to any command sent by the application. The only exception to this rule is the Test command, to which the XCP or CCP slave with the specific address may return an acknowledgement. With mcECUConnect2 you can specify the mode for the XCP CONNECT command, while [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect) always assumes mode 0 (normal mode).

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecucreate.html language=enus -->
## TOPIC 00045: mcECUCreate

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecucreate.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecucreate.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates an ECU object in memory. Format mcTypeStatus mcECUCreate( mcTypeTaskRef DBRefNum, cstr ECUName, char *Interface, i32 ByteOrder, u32 CRO_ID, u32 DTO_ID, u16 StationAddress, u32 BaudRate, mcTypeTaskRef *ECURefNum); Input DBRefNum DBRefNum is the task reference from the initial database

### mcECUCreate

Purpose

Creates an ECU object in memory.
Format

| mcTypeStatus | mcECUCreate( mcTypeTaskRef DBRefNum, cstr ECUName, char *Interface, i32 ByteOrder, u32 CRO_ID, u32 DTO_ID, u16 StationAddress, u32 BaudRate, mcTypeTaskRef *ECURefNum); |
| --- | --- |
| mcTypeTaskRef | DBRefNum, |
| cstr | ECUName, |
| char | *Interface, |
| i32 | ByteOrder, |
| u32 | CRO_ID, |
| u32 | DTO_ID, |
| u16 | StationAddress, |
| u32 | BaudRate, |
| mcTypeTaskRef | *ECURefNum); |

Input

DBRefNum

DBRefNum is the task reference from the initial database task function. The database task reference is originally returned from [mcDatabaseOpen](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseopen).

ECUname

Identifies the ECU object. Use this name as reference in [mcMeasurementCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementcreate) to create a DAQ list on the ECU.

Interface

Specifies the protocol and optional interface to use for this task.

ByteOrder

Sets the byte order of the CCP slave device:

**0—MSB_LAST**

The CCP Slave device uses the MSB_LAST (Intel) byte ordering.

**1—MSB_FIRST**

The CCP Slave device uses the MSB_FIRST (Motorola) byte ordering.

CRO_ID

Sets the Command Receive Object (CRO) CAN identifier for CCP or XCP on CAN. The CRO is used to send commands and data from the host to the slave device. If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit). If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit).

DTO_ID

Sets the Data Transfer Object (DTO) CAN identifier for CCP or XCP on CAN. The DTO is used to send commands and data from the slave device to the host. If **bit 31** (hex 0x80000000) of the value is set, the value is considered an **extended CAN identifier** (29-bit).

StationAddress

Sets the slave device station address. CCP is based on the idea that several ECUs can share the same CAN Arbitration IDs for CCP communication. To avoid communication conflicts, CCP defines a station address that must be unique for all ECUs sharing the same CAN Arbitration IDs. Unless an ECU has been addressed by its station address, the ECU must not react to CCP commands sent by the CCP master.

BaudRate

Sets the CAN baud rate in use by the selected interface. This property applies to all tasks initialized with the NI-CAN or NI-XNET interface. You can specify the following basic baud rates as the numeric rate: 33333, 83333, 100000, 125000, 200000, 250000, 400000, 500000, 800000, and 1000000. You can specify advanced baud rates as 8000XXYY hex, where YY is the value of Bit Timing Register 0 (BTR0), and XX is the value of Bit Timing Register 1 (BTR1). For more information, refer to the Interface Properties dialog in MAX.
Output

ECURefNum

ECURefNum is the task reference that links to the selected ECU.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

The function mcECUCreate is used to create an ECU object in memory instead of referring to a predefined ECU of an A2L database.

Interface selects the communication protocol and the desired interface to use for this task. The protocol and interface input are required, as these parameters are not defined in the A2L database. The default baud rate for CCP or XCP on CAN, or the IP address for XCP on UDP/TCP, may be defined in the A2L database, but you can change it by setting the Interface Baud Rate or IP Address property with [MC Set Property.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetpropertyvi).

This parameter is expected to be a string with the format Protocol:CommInterface.

Protocol supports:

- CCP to use the CAN Calibration Protocol
- XCP to use the XCP Universal Measurement and Calibration Protocol

CommInterface selects the transport layer and hardware interface to employ:

**Ethernet**

Use UDP or TCP as CommInterface. Supported with XCP protocol only.

**NI-CAN**

Use CANx as CommInterface to select the corresponding NI-CAN interface. The special CAN interface values 256 and 257 refer to virtual interfaces. For more information about using virtual interfaces, refer to the Frame to Channel Conversion section of Chapter 6, Using The Channel API, in the NI-CAN Hardware and Software User Manual.

**NI-XNET**

Use CANx@nixnet as CommInterface to select the corresponding NI-XNET interface as configured under **Devices and Interfaces** in MAX.

For using NI-XNET hardware on CompactRIO or R Series hardware, you may need to create an FPGA bit file to enable access to the modules. Refer to NI-XNET documentation for information about creating and loading a bit file; use the regular NI-XNET string format.

Note

@nixnet

Protocol and Interface

@ni_genie_nixnet

Protocol and Interface

**NI 985x CAN modules**

Use CANx@BridgeBitFile.lvbitx as CommInterface. A bridge FPGA VI (found in the LabVIEW examples of ECU MC) must be compiled for the RIO target; BridgeBitFile.lvbitx represents the absolute file path of the resulting bit file. It will be downloaded to the FPGA automatically when opening the CAN interface. For Real-Time targets, the bit file must be transferred to the internal disk, and this local file path must be used.

CANx refers to the name of the front panel controls used in the bridge FPGA VI (not to the module name in the LabVIEW project). Only a single 985x CAN interface is supported per FPGA target.

Use CANx@RIOx,BridgeBitFile.lvbitx as CommInterface to also specify the RIO target. RIOx equals the RIO target name as defined in your LabVIEW Project definition.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecudeselect.html language=enus -->
## TOPIC 00046: mcECUDeselect

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecudeselect.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecudeselect.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Deselects an ECU and invalidates the ECU reference handle. Format mcTypeStatus mcECUDeselect( mcTypeTaskRef *ECURefNum); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Output DBRefNum DBRefNum is the database hand

### mcECUDeselect

Purpose

Deselects an ECU and invalidates the ECU reference handle.
Format

| mcTypeStatus | mcECUDeselect( |
| --- | --- |
| mcTypeTaskRef | *ECURefNum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

DBRefNum

DBRefNum is the database handle created from the ECURefNum value by the function.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcECUDeselect deselects the an ECU and clears all internal driver data stored for this ECU. After calling this function it is no longer possible to communicate with the specified ECU. The task reference ECURefNum is transferred into a database handle DBRefNum.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecudisconnect.html language=enus -->
## TOPIC 00047: mcECUDisconnect

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecudisconnect.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecudisconnect.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Disconnects XCP or CCP communication to the selected ECU. Format mcTypeStatus mcECUDisconnect( mcTypeTaskRef ECURefNum); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Output Return ValueThe return value indicates

### mcECUDisconnect

Purpose

Disconnects XCP or CCP communication to the selected ECU.
Format

| mcTypeStatus | mcECUDisconnect( |
| --- | --- |
| mcTypeTaskRef | ECURefNum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcECUDisconnect implements the XCP or CCP command DISCONNECT. mcECUDisconnect disconnects the specified XCP or CCP slave from the actual communication and ends the calibration session. When the calibration session is terminated, all XCP or CCP DAQ lists of the device are stopped and cleared, and the protection masks of the device are set to their default values.
mcECUDisconnect is an optional command as disconnecting from the ECU is performed by the function [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecudeselect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecudeselect).

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecuselectex.html language=enus -->
## TOPIC 00048: mcECUSelectEx

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecuselectex.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecuselectex.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Selects an ECU from the names stored in an A2L database. Format mcTypeStatus mcECUSelectEx( mcTypeTaskRef DBRefNum, cstr ECUName, cstr Interface, mcTypeTaskRef *ECURefNum); Input DBRefNum DBRefNum is the task reference from the initial database task function. The database task reference is o

### mcECUSelectEx

Purpose

Selects an ECU from the names stored in an A2L database.
Format

| mcTypeStatus | mcECUSelectEx( mcTypeTaskRef DBRefNum, cstr ECUName, cstr Interface, mcTypeTaskRef *ECURefNum); |
| --- | --- |
| mcTypeTaskRef | DBRefNum, |
| cstr | ECUName, |
| cstr | Interface, |
| mcTypeTaskRef | *ECURefNum); |

Input

DBRefNum

DBRefNum is the task reference from the initial database task function. The database task reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseopen](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdatabaseopen).

ECUName

ECUName is the selected ECU name out of an A2L Database file with which to initialize all subsequent tasks.

Interface

Specifies the protocol and optional interface to use for this task.

The interface input uses an enumeration in which value 0 selects CAN0, value 1 selects CAN1, and so on. As the ECU M&C API is based on the NI-CAN Channel API, the NI-CAN Frame API cannot be used on the same CAN network interface simultaneously. If the CAN network interface is already initialized in the Frame API, this function returns an error.
Output

ECURefNum

ECURefNum is the task reference which links to the selected ECU.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcECUSelectEx creates an ECU reference handle to the selected ECU name. The mcECUSelectEx function does not start communication. This enables you to use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) to change the properties of an ECU task. After you change properties, use [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect) to start communication for the task and logically connect to the selected ECU.

Interface selects the communication protocol and the desired interface to use for this task. The protocol and interface input are required, as these parameters are not defined in the A2L database. The default baud rate for CCP or XCP on CAN, or the IP address for XCP on UDP/TCP, may be defined in the A2L database, but you can change it by setting the Interface Baud Rate or IP Address property with [MC Set Property.vi](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetpropertyvi).

This parameter is expected to be a string with the format Protocol:CommInterface.

Protocol supports:

- CCP to use the CAN Calibration Protocol
- XCP to use the XCP Universal Measurement and Calibration Protocol

CommInterface selects the transport layer and hardware interface to employ:

**Ethernet**

Use UDP or TCP as CommInterface. Supported with XCP protocol only.

**NI-CAN**

Use CANx as CommInterface to select the corresponding NI-CAN interface. The special CAN interface values 256 and 257 refer to virtual interfaces. For more information about using virtual interfaces, refer to the Frame to Channel Conversion section of Chapter 6, Using The Channel API, in the NI-CAN Hardware and Software User Manual.

**NI-XNET**

Use CANx@nixnet as CommInterface to select the corresponding NI-XNET interface as configured under **Devices and Interfaces** in MAX.

For using NI-XNET hardware on CompactRIO or R Series hardware, you may need to create an FPGA bit file to enable access to the modules. Refer to NI-XNET documentation for information about creating and loading a bit file; use the regular NI-XNET string format.

Note

@nixnet

Protocol and Interface

@ni_genie_nixnet

Protocol and Interface

**NI 985x CAN modules**

Use CANx@BridgeBitFile.lvbitx as CommInterface. A bridge FPGA VI (found in the LabVIEW examples of ECU MC) must be compiled for the RIO target; BridgeBitFile.lvbitx represents the absolute file path of the resulting bit file. It will be downloaded to the FPGA automatically when opening the CAN interface. For Real-Time targets, the bit file must be transferred to the internal disk, and this local file path must be used.

CANx refers to the name of the front panel controls used in the bridge FPGA VI (not to the module name in the LabVIEW project). Only a single 985x CAN interface is supported per FPGA target.

Use CANx@RIOx,BridgeBitFile.lvbitx as CommInterface to also specify the RIO target. RIOx equals the RIO target name as defined in your LabVIEW Project definition.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcecusetcalibrationpage.html language=enus -->
## TOPIC 00049: mcECUSetCalibrationPage

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcecusetcalibrationpage.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcecusetcalibrationpage.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets the appropriate RAM or ROM calibration page on the ECU. Format mcTypeStatus mcECUSetCalibrationPage ( mcTypeTaskRef ECURefNum, u8 UseRAM, u8 mapAddresses); Input ECURefNum ECURefNum is the task reference that links to the selected ECU. This reference is originally returned from mcECUSel

### mcECUSetCalibrationPage

Purpose

Sets the appropriate RAM or ROM calibration page on the ECU.
Format

| mcTypeStatus | mcECUSetCalibrationPage ( mcTypeTaskRef ECURefNum, u8 UseRAM, u8 mapAddresses); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | UseRAM, |
| u8 | mapAddresses); |

Input

ECURefNum

ECURefNum is the task reference that links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

UseRAM

0: Select ROM calibration page.
1: Select RAM calibration page.

mapAddresses

0: Do not map addresses.
1: Map addresses from ROM to the page specified in UseRAM.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcECUSetCalibrationPage tries to identify a single RAM or ROM page on the ECU and select it according to the UseRAM input.

To identify an appropriate page, the function searches for the calibration page information from the A2L file or online information from the ECU. If the function identifies a unique calibration page, it is activated in the ECU, and the function returns success.

If the function does not identify a unique page, an error indicating this is returned, and no further action is taken. This does not state a fault, but just the algorithm's inability to uniquely identify the desired page. In this case, you can use the calibration page-related ECU properties ([mcGetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty), **ECU»CCP»Cal Pages»...** or **ECU»XCP»Cal Pages»...**) to gain the information about available calibration pages, and manually select the correct page using [mcCCPSelectCalPage](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcccpselectcalpage) or [mcXCPSetCalPage](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetcalpage).

The mapAddresses parameter activates the address mapping from the ROM page, assumed to be the reference page to the target page specified in UseRAM. Address mapping is supported for only the CCP protocol and requires a unique ROM and unique RAM page in the A2L file. Addresses of measurements and characteristics in the A2L file must point to the ROM page as a reference page.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mceventcreate.html language=enus -->
## TOPIC 00050: mcEventCreate

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mceventcreate.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mceventcreate.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates an Event object in memory. Format mcTypeStatus mcEventCreate( mcTypeTaskRef ECURefNum, cstr EventChannelName, u8 EventChannelNumber); Input ECURefNum ECURefNum is the task reference that links to the selected ECU. This reference is originally returned from mcECUCreate. EventChannelNa

### mcEventCreate

Purpose

Creates an Event object in memory.
Format

| mcTypeStatus | mcEventCreate( mcTypeTaskRef ECURefNum, cstr EventChannelName, u8 EventChannelNumber); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| cstr | EventChannelName, |
| u8 | EventChannelNumber); |

Input

ECURefNum

ECURefNum is the task reference that links to the selected ECU. This reference is originally returned from [mcECUCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecucreate).

EventChannelName

EventChannelName identifies the Event Channel object.

EventChannelNumber

EventChannelNumber identifies the number of the Event Channel. The event channel number specifies the generic signal source that effectively determines the data transmission timing. To allow a reduction of the desired transmission rate, a prescaler may be applied to the Event Channel. The prescaler value factor must be greater than or equal to 1 to use [mcSetProperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcsetproperty) using mcPropDAQ_Prescaler.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

Use the function mcEventCreate to create an Event object in memory instead of referring to a predefined Event Channel in the A2L database. Assign the event channel object by name to a DAQ List in [mcMeasurementCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcmeasurementcreate).

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcgeneric.html language=enus -->
## TOPIC 00051: mcGeneric

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcgeneric.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcgeneric.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sends a generic XCP or CCP command. Format mcTypeStatus mcGeneric( mcTypeTaskRef ECURefNum, u8 Command, u8 *Data, u32 DataSize, u32 Timeout, u8 *ErrorCode, u8 *ReturnValue, u32 *ReturnValueSize); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference

### mcGeneric

Purpose

Sends a generic XCP or CCP command.
Format

| mcTypeStatus | mcGeneric( mcTypeTaskRef ECURefNum, u8 Command, u8 *Data, u32 DataSize, u32 Timeout, u8 *ErrorCode, u8 *ReturnValue, u32 *ReturnValueSize); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Command, |
| u8 | *Data, |
| u32 | DataSize, |
| u32 | Timeout, |
| u8 | *ErrorCode, |
| u8 | *ReturnValue, |
| u32 | *ReturnValueSize); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Command

Command is the command code to send to the ECU.

Data

Data contains the parameters of the command as an array of bytes. For more information about the parameters of the (user defined) commands implemented in the ECU, refer to the documentation for the ECU.

DataSize

DataSize defines the number of bytes (the array size) passed in the input parameter Data.

Timeout

Timeout specifies the maximum number of milliseconds to wait for a response from the ECU. If the Timeout expires before an ECU response occurs, the error mcErrorTimeout is returned.
Output

ErrorCode

ErrorCode describes the error returned from the ECU during the communication.

ReturnValue

ReturnValue may contain an array of bytes returned from the ECU as a response to the command sent to the ECU.

ReturnValueSize

ReturnValueSize contains the number of bytes returned from the ECU passed to ReturnValue.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcGeneric can be used to send commands to the ECU that are not defined by the XCP or CCP specification. The command code in Command and the parameters of this command defined in Data are sent to the ECU, and the data returned by the ECU is passed to the parameter ReturnValue. Since the ECU M&C driver has no knowledge of the parameters of the command and their data types, all parameters and return values are passed as an array of bytes. Therefore you are responsible for the correct type casting of all parameters and return values of this command. Make sure that all parameters are passed in the correct byte ordering for this function. For more information about the (user defined) commands and their parameters refer to the documentation for the ECU.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcgetnames.html language=enus -->
## TOPIC 00052: mcGetNames

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcgetnames.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcgetnames.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Retrieves a comma-separated list of ECU names, Measurement names, Characteristic names, Event names, Characteristic pages, or Group names from a specified A2L database. Format mcTypeStatus mcGetNames( mcTypeTaskRef RefNum, u32 Type, cstr ECUName, u32 SizeOfNamesList, str NameList); Input Ref

### mcGetNames

Purpose

Retrieves a comma-separated list of ECU names, Measurement names, Characteristic names, Event names, Characteristic pages, or Group names from a specified A2L database.
Format

| mcTypeStatus | mcGetNames( mcTypeTaskRef RefNum, u32 Type, cstr ECUName, u32 SizeOfNamesList, str NameList); |
| --- | --- |
| mcTypeTaskRef | RefNum, |
| u32 | Type, |
| cstr | ECUName, |
| u32 | SizeOfNamesList, |
| str | NameList); |

Input

RefNum

RefNum is any ECU M&C task reference which consists of a valid link to the opened A2L database (DBRefNum), a selected ECU (ECURefNum) or a Measurement task (DAQRefNum). RefNum has to be valid for the related Type.

Type

Specifies the Type of names to return.

0—**mcTypeECUNames**

Returns a list of ECU names. You can pass one of the returned names to [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

1—**mcTypeMeasurementNames**

Returns a list of Measurement names. You can pass the returned NamesList to [mcDAQInitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize).

2—**mcTypeCharacteristicNames**

Returns a list of Characteristic names. You can pass a single name out of the NamesList to [mcCharacteristicWrite](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mccharacteristicwrite) or [mcCharacteristicRead](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mccharacteristicread).

3—**mcTypeEventChannelNames**

Returns a list of Event Channel names.

4—**mcTypeDefinedPagesNames**

Returns a list of Calibration page names.

5—**mcTypeGroupNames**

Returns a list of Group names.

6—**mcTypeGroup_SubGroupNames**

Returns a list of Subgroup names of the specified Group name.

7—**mcTypeGroup_MeasurementNames**

Returns a list of Measurement names within the specified Group.

8—**mcTypeGroup_CharacteristicNames**

Returns a list of Characteristic names within the specified Group.

9—**mcTypeFuncNames**

Returns a list of Function names within the specified ECU.

10—**mcTypeFunc_DefCharacNames**

Returns a list of Characteristic names referred by the DEF_CHARACTERISTIC keyword within the related Function.

11—**mcTypeFunc_RefCharacNames**

Returns a list of Characteristic names referred by the REF_CHARACTERISTIC keyword within the related Function.

12—**mcTypeFunc_InMeasNames**

Returns a list of Measurement names referred by the IN_MEASUREMENT keyword within the related Function.

13—**mcTypeFunc_OutMeasNames**

Returns a list of Measurement names referred by the OUT_MEASUREMENT keyword within the related Function.

14—**mcTypeFunc_LocMeasNames**

Returns a list of Measurement names referred by the LOC_MEASUREMENT keyword within the related Function.

15—**mcTypeFunc_SubFuncNames**

Returns a list of Function names referred by the SUB_FUNCTION keyword within the related Function.

16—**mcTypeGroup_FunctionListNames**

Returns a list of Function names referred by the FUNCTION_LIST keyword within the related Group.

17—**mcTypeTLI_XcpOnCanNames**

Returns a list of Transport Layer Instance names of the XCP_ON_CAN blocks within the IF_DATA XCPplus block. No entries are returned for XCP_ON_CAN blocks without the TRANSPORT_LAYER_INSTANCE keyword or an XCP_ON_CAN block within an IF_DATA XCP block.

18—**cTypeTLI_XcpOnTcpNames**

Returns a list of Transport Layer Instance names of the XCP_ON_TCP_IP blocks within the IF_DATA XCPplus block. No entries are returned for XCP_ON_TCP_IP blocks without the TRANSPORT_LAYER_INSTANCE keyword or an XCP_ON_TCP_IP block within an IF_DATA XCP block.

19—**mcTypeTLI_XcpOnUdpNames**

Returns a list of Transport Layer Instance names of the XCP_ON_UDP_IP blocks within the IF_DATA XCPplus block. No entries are returned for XCP_ON_UDP_IP blocks without the TRANSPORT_LAYER_INSTANCE keyword or an XCP_ON_UDP_IP block within an IF_DATA XCP block.

ECUName

If the Type = **mcTypeMeasurementNames** or Type = **mcTypeCharacteristicNames** and RefNum contains a DBRefNum, the corresponding ECU name has to be referenced in order to access ECU specific properties. If RefNum contains an ECURefNum or DAQRefNum the parameter ECUName is ignored and can be set to NULL.

SizeOfNamesList

Size of the buffer provided to take the names list. After calling [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnameslength](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnameslength), you can allocate an array of size SizeofNamesList, and then pass that array to mcGetNames using the same input parameters. This ensures that mcGetNames will return all names without error.
Output

NameList

Returns the comma-separated list of names specified by Type.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

Get a comma-separated list of ECU, Measurement, Characteristic, or Event Channel names from a specified A2L database file.

If using mcGetNames to query the list of supported event channels on an ECU, the event channels might be stored inside the ECU instead of the A2L file. To query these event channel names from the ECU directly, connect to the ECU using [mcECUConnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect) before calling mcGetNames.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcgetnameslength.html language=enus -->
## TOPIC 00053: mcGetNamesLength

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcgetnameslength.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcgetnameslength.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Retrieves the amount of memory required to store the names returned by . Format mcTypeStatus mcGetNamesLength( mcTypeTaskRef RefNum, u32 Type, cstr ECUName, u32 *SizeOfNamesList); Input RefNum RefNum is any ECU M&C task reference which consists of a valid link to the opened A2L database (DBR

### mcGetNamesLength

Purpose

Retrieves the amount of memory required to store the names returned by [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames).
Format

| mcTypeStatus | mcGetNamesLength( mcTypeTaskRef RefNum, u32 Type, cstr ECUName, u32 *SizeOfNamesList); |
| --- | --- |
| mcTypeTaskRef | RefNum, |
| u32 | Type, |
| cstr | ECUName, |
| u32 | *SizeOfNamesList); |

Input

RefNum

RefNum is any ECU M&C task reference which consists of a valid link to the opened A2L database (DBRefNum), a selected ECU (ECURefNum) or a Measurement task (DAQRefNum). RefNum has to be valid for the related Type.

Type

Specifies the Type of names to return.

0—**mcTypeECUNames**

Returns a list of ECU names.

1—**mcTypeMeasurementNames**

Returns a list of Measurement names.

2—**mcTypeCharacteristicNames**

Returns a list of Characteristic names.

3—**mcTypeEventChannelNames**

Returns a list of Event Channel names.

4—**mcTypeDefinedPagesNames**

Returns a list of Calibration page names.

5—**mcTypeGroupNames**

Returns a list of Group names.

6—**mcTypeGroup_SubGroupNames**

Returns a list of Subgroup names of the specified Group name.

7—**mcTypeGroup_MeasurementNames**

Returns a list of Measurement names within the specified Group.

8—**mcTypeGroup_CharacteristicNames**

Returns a list of Characteristic names within the specified Group.

9—**mcTypeFuncNames**

Returns a list of Function names within the specified ECU.

10—**mcTypeFunc_DefCharacNames**

Returns a list of Characteristic names referred by the DEF_CHARACTERISTIC keyword within the related Function.

11—**mcTypeFunc_RefCharacNames**

Returns a list of Characteristic names referred by the REF_CHARACTERISTIC keyword within the related Function.

12—**mcTypeFunc_InMeasNames**

Returns a list of Measurement names referred by the IN_MEASUREMENT keyword within the related Function.

13—**mcTypeFunc_OutMeasNames**

Returns a list of Measurement names referred by the OUT_MEASUREMENT keyword within the related Function.

14—**mcTypeFunc_LocMeasNames**

Returns a list of Measurement names referred by the LOC_MEASUREMENT keyword within the related Function.

15—**mcTypeFunc_SubFuncNames**

Returns a list of Function names referred by the SUB_FUNCTION keyword within the related Function.

16—**mcTypeGroup_FunctionListNames**

Returns a list of Function names referred by the FUNCTION_LIST keyword within the related Group.

17—**mcTypeTLI_XcpOnCanNames**

Returns a list of Transport Layer Instance names of the XCP_ON_CAN blocks within the IF_DATA XCPplus block. No entries are returned for XCP_ON_CAN blocks without the TRANSPORT_LAYER_INSTANCE keyword or an XCP_ON_CAN block within an IF_DATA XCP block.

18—**cTypeTLI_XcpOnTcpNames**

Returns a list of Transport Layer Instance names of the XCP_ON_TCP_IP blocks within the IF_DATA XCPplus block. No entries are returned for XCP_ON_TCP_IP blocks without the TRANSPORT_LAYER_INSTANCE keyword or an XCP_ON_TCP_IP block within an IF_DATA XCP block.

19—**mcTypeTLI_XcpOnUdpNames**

Returns a list of Transport Layer Instance names of the XCP_ON_UDP_IP blocks within the IF_DATA XCPplus block. No entries are returned for XCP_ON_UDP_IP blocks without the TRANSPORT_LAYER_INSTANCE keyword or an XCP_ON_UDP_IP block within an IF_DATA XCP block.

ECUName

If the Type = **mcTypeMeasurementNames** or Type = **mcTypeCharacteristicNames** and RefNum contains a DBRefNum, the corresponding ECU name has to be referenced in order to access ECU specific properties. If RefNum contains an ECURefNum or DAQRefNum the parameter ECUName is ignored and can be set to NULL.
Output

SizeOfNamesList

Number of bytes required for [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) to return all names for the specified ECUName and Type. After calling mcGetNamesLength, you can allocate an array of size SizeofNamesList, then pass that array to [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) using the same input parameters. This ensures that mcGetNames will return all names without error.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

After calling mcGetNamesLength, you can allocate an array of size SizeofNamesList, then pass that array to [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) using the same input parameters. This ensures that [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetnames) will return all names without error.

If using mcGetNamesLength to query the length of the list of supported event channels on an ECU, the event channels might be stored inside the ECU instead of the A2L file. To query these event channel names from the ECU directly, connect to the ECU using [mcECUConnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect) before calling mcGetNamesLength.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcgetproperty.html language=enus -->
## TOPIC 00054: mcGetProperty

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcgetproperty.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcgetproperty.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Retrieves a property of the driver, the database, the ECU, a Characteristic, a Measurement, or a Measurement task. Format 1 Format Return Type Function Signature mcTypeStatus mcGetProperty( Parameter Type Parameter Name mcTypeTaskRef RefNum, cstr Name, u32 PropertyID, u32 SizeOfValue, void *

### mcGetProperty

Purpose

Retrieves a property of the driver, the database, the ECU, a Characteristic, a Measurement, or a Measurement task.
Format

| Return Type | Function Signature |
| --- | --- |
| mcTypeStatus | mcGetProperty( Parameter Type Parameter Name mcTypeTaskRef RefNum, cstr Name, u32 PropertyID, u32 SizeOfValue, void *Value); |
| Parameter Type | Parameter Name |
| mcTypeTaskRef | RefNum, |
| cstr | Name, |
| u32 | PropertyID, |
| u32 | SizeOfValue, |
| void | *Value); |

Input

RefNum

RefNum is any ECU M&C task reference which consists of a valid link to the opened A2L database (DBRefNum), a selected ECU (ECURefNum) or a Measurement task (DAQRefNum). RefNum has to be valid for the related PropertyID type.

Name

Specifies an individual name (ECU name, Measurement channel name, or Characteristic name) within the task.

PropertyID

Selects the property to get. The PropertyID is represented by a property name as defined in the niemc.h header file. Refer to the Properties section for PropertyID data type, name, and description.

SizeOfValue

Number of bytes allocated for the Value output. This size normally depends on the data type listed in the description of the property.
Output

Value

Returns the property value. PropertyId determines the data type of the returned value.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

#### Values for PropertyID

| Data Type | Name | Description |
| --- | --- | --- |
| u32 | mcPropCANBaudrate | Returns the CAN Baud rate for XCP or CCP on CAN which is used to send commands and data from the host to the slave device. |
| u32 | mcPropCANTermination | For all XNET devices, the termination is software selectable. XNET provides the option of 120 Ω between Bus Plus and Bus Minus or no termination. The Termination property configures the onboard termination of the NI-XNET interface CAN connector (port). The Boolean property supports two values: TRUE = Termination ON and FALSE = Termination Off. However, different CAN hardware has different termination requirements, and the termination values have different meanings. Refer to the Termination attribute in the XNET API for more details. (This property is supported for NI-XNET devices only.) 0—FALSE (termination off) 1—TRUE (termination on) |
| u64 | mcPropCANBaudrate64 | Indicates the baud rate used by the CAN Interface with XCP protocol. Basic baud rates such as 125000 and 500000 are specified as numeric values. Advanced (or custom) baud rates are specific to the CAN interface in use and the description can be found in the NI-XNET or NI-CAN documentation. The default value for the property is the baud rate set in the A2L database used for the application. If NI-XNET is used and the A2L file specifies a sampling point for the baud rate which differs from the sampling point used internally in NI-XNET, ECUMC replaces the standard baud rate value by a custom 64-bit baud rate which uses the sampling point as close as possible to the sampling point in A2L database. You can find the documentation of the NI-XNET custom baud rate in NI-XNET Hardware and Software Help under Interface:64bit Baud Rate. |
| u64 | mcPropCANFDBaudrate64 | Indicates the CAN FD baud rate value (used for the data part of transmission). If CAN FD is used, 64bit Baud Rate specifies the baud rate for the arbitration part of the CAN message, while this property specifies the baud rate for the data part of the CAN message. CAN FD is only supported by NI-XNET interfaces for XCP protocol. Basic baud rates such as 500000 and 2000000 are specified as numeric values. Information about the advanced (or custom) baud rates can be found in the NI-XNET Hardware and Software Help under Interface:CAN:64bit FD Baud Rate. The default value for the property is the baud rate set in the CAN_FD section of the A2L database used for the application. You can set the property to use any other baud rate or custom baud rate according to NI-XNET specification. If the A2L file specifies a sampling point for the CAN FD baud rate which differs from the sampling point used internally in NI-XNET, ECUMC replaces the standard baud rate value by a custom 64-bit baud rate which uses the sampling point as close as possible to the sampling point in A2L database. Refer to information about the custom baud rates in the NI-XNET Hardware and Software Help under Interface:64bit FD Baud Rate. Transceiver Delay Compensation defined by the A2L database is not used while calculating the custom baud rate value, as the value is hardware implementation specific and the value found in the database may not match the NI-XNET specification. If you need very specific values for the CAN FD baud rate, you need to follow the NI-XNET documentation and set a custom baud rate using mcSetProperty(). |
| u32 | mcPropCANIOmode | Indicates the CAN I/O Mode of the specified interface. The CAN I/O mode is only supported with XNET interfaces. It determines if the interface is running in CAN 2.0 mode (supports frames with payload up to 8 bytes), CAN FD mode (supports frames up to 64 bytes), or CAN FD+BRS mode (CAN FD with baud rate switching). The default value is determined by the A2L database used by the application. In ECU Determined mode, the master can communicate with ECUs using either traditional CAN or CAN FD frames. The master starts the communication with a traditional CAN 2.0 frame; if the ECU responds in any mode, this mode is selected for further communication. If the ECU does not respond to the CAN 2.0 frame, the master repeats (after timeout) the first command using a CAN FD frame. In ECU Determined mode, the NI-XNET interface runs in CAN FD BRS mode, so the CAN FD baud rate must be set before using this mode. In CAN FD+BRS mode, the NI-XNET interface can receive and transmit CAN 2.0, CAN FD, and CAN FD+BRS frames. 0—mcCANioMode_CAN 1—mcCANioMode_CAN_FD 2—mcCANioMode_CAN_FD_BRS 3—mcCANioMode_ECU_Determined Note CAN FD is only supported with NI-XNET version 17.0.1 or later. |
| i32 | mcPropActCANIOmode | This read-only property allows querying the CAN I/O mode that is actually used when the CAN I/O mode is set to ECU Determined. As long as the mode has not been determined, the value is ECU Determined (refer to the mcPropCANIOmode property description for possible values). When the communication with the ECU has been established, the value changes to CAN 2.0, CAN FD, or CAN FD+BRS mode. |
| u32 | mcPropCANUseMaxDLC | This Boolean property determines if the master in CAN 2.0 mode transmits frames with the actual used payload length or always transmits the maximum number of bytes (8 bytes). The default value of this property is being retrieved from the A2L database based on the MAX_DLC_REQUIRED keyword within the XCP_ON_CAN section. 0—FALSE 1—TRUE |
| u32 | mcPropCANFDMaxDLC | This property determines the payload length which should be used if the mcPropCANFDUseMaxDLC setting is TRUE. The default value of this property is being retrieved from the A2L database based on the MAX_DLC keyword within the CAN_FD section. |
| u32 | mcPropCANFDUseMaxDLC | This Boolean property determines if the master in CAN FD mode transmits frames with the actual used payload length or always transmits the maximum number of bytes, defined by the mcPropCANFDMaxDLC DLC setting (8…64 bytes). The default value of this property is being retrieved from the A2L database based on the MAX_DLC_REQUIRED keyword within the CAN_FD section. 0—FALSE 1—TRUE |
| u32 | mcPropChar_Address | Returns the address of the selected Characteristic in the memory of the ECU. |
| u32 | mcPropChar_ByteOrder | Returns the specified byte order: 0—Intel format Bytes are in little-endian order, with least-significant bit first. 1—Motorola format Bytes are in big-endian order, with most-significant bit first. |
| u8 | mcPropChar_Datatype | Returns the data type of the Characteristic. |
| u32 | mcPropChar_Dimension | Returns the dimension of the Characteristic: 0—0-dimensional: The Characteristic can be accessed (read/write) through a double value. 1—1-dimensional: The Characteristic can be accessed (read/write) through a one-dimensional array of double value. 2—2-dimensional: The Characteristic can be accessed (read/write) through a two-dimensional array of double value. |
| u8 | mcPropChar_Extension | Returns additional address information. For instance it can be used to distinguish different address spaces of an ECU (multi-microcontroller devices). |
| f64 | mcPropChar_Maximum | Returns the Maximum value of the Characteristic. |
| f64 | mcPropChar_Minimum | Returns the Minimum value of the Characteristic. |
| u32 | mcPropChar_ReadOnly | Returns if a Characteristic is set to read only. In this case it is not allowed to call mcCharacteristicWrite for this Characteristic. |
| u32 | mcPropChar_Sizes | Returns the Array Sizes for the X and Y directions of the Characteristic. |
| str | mcPropChar_Unit | Returns the unit string defined for this Characteristic in the A2L database. |
| u32 | mcPropChar_Unit_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropChar_Unit. |
| str | mcPropChar_Comment | Returns the comment of this Characteristic defined in the A2L database. |
| u32 | mcPropChar_Comment_Size | Returns the required buffer size for the characteristic comment when using mcPropChar_Comment property. |
| f64 | mcPropChar_X_Axis | Returns X-axis values on which the Characteristic is defined. Valid if the selected Characteristic is 1- or 2-dimensional. |
| f64 | mcPropChar_Y_Axis | Returns Y-axis values on which the Characteristic is defined, Valid if the selected Characteristic is 2-dimensional. |
| f64 | mcPropChar_Scale_Factor | Returns the scaling factor defined for this Characteristic in the A2L database. |
| f64 | mcPropChar_Scale_Offset | Returns the scaling offset defined for this Characteristic in the A2L database. |
| u32 | mcPropChar_Scale_Type | Returns the scaling type defined for this Characteristic in the A2L database. 0: Unknown The type of the scaling could not be derived from the A2L file content. 1: Rational Function The related scaling is based on a rational function of second order. This covers also the linear scaling, given by factor and offset. 2: Enumeration Text The related scaling is based on the COMPU_VTAB keyword within the A2L file. Read functions return nonscaled, numeric values.Write functions accept nonscaled, numeric values.It is possible to use mcDoubleToText and mcTextToDouble to convert between enumeration text values and double values. 3: Range Text The related scaling is based on the COMPU_VTAB_RANGE keyword within the A2L file. Read functions return nonscaled, numeric values.Write functions accept nonscaled, numeric values.It is possible to use mcDoubleToText and mcTextToDouble to convert between range text values and double values. 4: Formula The related scaling is based on the FORMULA keyword within the A2L file, using a free formula to calculate the values. 5: Table (Using Interpolation) The related scaling is based on the TAB_INTP keyword within the A2L file, using interpolation between x-y pairs. 6: Table (Without Interpolation) The related scaling is based on the TAB_NOINTP keyword within the A2L file, using x-y pairs without interpolation. |
| u32 | mcPropChar_Scale_TextValues_Size | If the scaling type is 2 = Enumeration Text or 3 = Range Text, you can use this property to request the length needed to store the comma-separated list of text values that can be converted into raw values (refer to the mcPropChar_Scale_TextValues property). |
| str | mcPropChar_Scale_TextValues | If the scaling type is 2 = Enumeration Text or 3 = Range Text, you can use this property to request the comma-separated list of text values that can be converted into raw values. |
| u32 | mcPropCmd_EXCHANGE_ID | Returns whether or not the EXCHANGE_ID command should be suppressed during connection to the ECU. |
| u32 | mcPropCROID | Returns the CRO CAN Identifier for XCP or CCP on CAN. The CRO is used to send commands and data from the host to the slave device. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| u32 | mcPropDAQ_DTO_ID | Returns the DTO ID, which is used by the ECU to transmit the DAQ list data to the CCP master. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| nctType Taskref | mcPropDAQ_DTO_Task | NI-CAN task reference to the CAN Task assigned to the DTO ID of the Measurement task. |
| str | mcPropDAQ_EventChannelName | Returns the selected event channel name to which the Measurement task is assigned. |
| u32 | mcPropDAQ_EventChannelName_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropDAQ_EventChannelName. |
| u32 | mcPropDAQ_Mode | Returns the selected mode of an M&C Measurement task. 0—DAQ List The data is transmitted from the ECU in equidistant time intervals as defined in the A2L database. The data can be read back with mcDAQRead as Single point data using sample rate = 0, or as waveform using a sample rate > 0. Input channel data is received from the DAQ messages. Use mcDAQRead to obtain input samples as single-point, array, or waveform. 1—Polling In this mode the data from the Measurement task is uploaded from the ECU whenever mcDAQRead is called. |
| u32 | mcPropDAQ_NumChannels | Returns the number of scaled channels initialized in a DAQ channel list of an M&C Measurement task. This is the number of array entries required when using mcDAQRead. mcPropDAQ_NumChannels and mcPropDAQ_NumRawChannels provide the number of array entries required when using mcDAQReadEx. |
| u32 | mcPropDAQ_NumRawChannels | Returns the number of raw channels initialized in a DAQ channel list of an M&C Measurement task. mcPropDAQ_NumRawChannels and mcPropDAQ_NumChannels provide the number of array entries required when using mcDAQReadEx. |
| u16 | mcPropDAQ_Prescaler | Prescaler for the Measurement task on the ECU. |
| f64 | mcPropDAQ_SampleRate | Returns the Sample Rate in Hz for the M&C Measurement task. The sample rate is defined in mcDAQInitialize, mcDAQInitializeEx, mcDAQListInitialize, and mcDAQListInitializeEx functions or by mcSetProperty. |
| u32 | mcPropDAQ_SamplesPending | Returns the number of samples available for read in DAQ tasks defined with sample rate > 0. If this property is queried before the DAQ list is started, it always returns 0. Start the DAQ list first with mcDAQStartStop before you query this property. |
| f64 | mcPropDAQ_TimeSinceLastFrame | Indicates how much time has passed (in seconds) since the measurement session received the last DAQ frame. You can reuse this property to restart the measurement when the value increases a threshold (for example, 0.5 seconds), assuming the ECU stopped sending DAQ messages and must be restarted. This property is read only. |
| u32 | mcPropDAQ_NumDAQPIDs | Indicates the number of PIDs (frames) used in the DAQ session. The number of PIDs is only valid after the DAQ list has been transmitted to the ECU otherwise the returned value is 0. For example, you can call mcDAQStartStop with the mode mcStartStopModeTransmitDAQ after mcDAQInitialize before reading this property. This property is read only. |
| u32 | mcPropDAQ_TimingSource | Returns the timing source used for DAQ measurements. The default is Automatic. Values are: ValueDescription0AutomaticThe default method (1, 2, or 3, below) is selected.1Host TimingTimestamps are generated from the host system time whenever a frame arrives.This mode is always available.This is the default for XCP on TCP/UDP if the ECU does not support timestamps.2CAN TimingTimestamps are generated from the network interface hardware (e.g. NI-XNET hardware).This mode is available only if the network hardware generates timestamps.This is the default for XCP on CAN if the ECU does not support timestamps.3ECU TimingTimestamps are taken from the ECU data. The Start Time is taken from the host, and increments are taken from the ECU.This mode is only available if the ECU generates timestamps; in this case, it is default. |
| Value | Description |  |
| 0 | AutomaticThe default method (1, 2, or 3, below) is selected. |  |
| 1 | Host TimingTimestamps are generated from the host system time whenever a frame arrives.This mode is always available.This is the default for XCP on TCP/UDP if the ECU does not support timestamps. |  |
| 2 | CAN TimingTimestamps are generated from the network interface hardware (e.g. NI-XNET hardware).This mode is available only if the network hardware generates timestamps.This is the default for XCP on CAN if the ECU does not support timestamps. |  |
| 3 | ECU TimingTimestamps are taken from the ECU data. The Start Time is taken from the host, and increments are taken from the ECU.This mode is only available if the ECU generates timestamps; in this case, it is default. |  |
| str | mcPropDB_Filename | Returns the A2L Database file name with which the task has been opened. The value of this property cannot be changed using mcSetProperty. |
| u32 | mcPropDB_Filename_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropDB_Filename. |
| u32 | mcPropDTOID | Returns the Data Transfer Object (DTO) CAN Identifier for XCP or CCP on CAN. The DTO is used to send commands and data from the slave device to the host. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| u32 | mcPropECU_BaudRate | Returns the baud rate in use. |
| u32 | mcPropECU_ByteOrder | Returns the byte order of the slave device. 0—MSB_LAST The Slave device uses the MSB_LAST (Intel) byte ordering. 1—MSB_FIRST The Slave device uses the MSB_FIRST (Motorola) byte ordering. |
| u32 | mcPropECU_CCP_NumPages | Returns the number of DEFINED_PAGES structures for this ECU in the A2L file. |
| u32 | mcPropECU_CCP_PageNo | Returns the page number of the page selected with the Name input. |
| u32 | mcPropECU_CCP_PageFlags | Returns the page flags of the page selected with the Name input. The value returned is a bitmask ored from the following values: ValueDescription1RAM page2ROM page4FLASH page8EEPROM page16RAM_INIT_BY_ECU - RAM page initialized at ECU startup.32RAM_INIT_BY_TOOL - RAM page that the calibration tool initializes.64AUTO_FLASH_BACK - RAM page automatically flashed back.128FLASH_BACK - RAM page that the calibration tool can flash back.256DEFAULT - Page is standard (fallback). |
| Value | Description |  |
| 1 | RAM page |  |
| 2 | ROM page |  |
| 4 | FLASH page |  |
| 8 | EEPROM page |  |
| 16 | RAM_INIT_BY_ECU - RAM page initialized at ECU startup. |  |
| 32 | RAM_INIT_BY_TOOL - RAM page that the calibration tool initializes. |  |
| 64 | AUTO_FLASH_BACK - RAM page automatically flashed back. |  |
| 128 | FLASH_BACK - RAM page that the calibration tool can flash back. |  |
| 256 | DEFAULT - Page is standard (fallback). |  |
| u32 | mcPropECU_CCP_PageAddress | Returns the memory address of the page selected with the Name input. |
| u8 | mcPropECU_CCP_PageAddressExtension | Returns the memory address extension of the page selected with the Name input. |
| str | mcPropECU_Checksum | Returns the file name of the Checksum DLL used for verifying the checksum. |
| u32 | mcPropECU_Checksum_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_Checksum. |
| u32 | mcPropECU_CmdByteOrder | Returns the byte order for multi-byte command parameters. 0—MSB_LAST The CCP Slave device uses the MSB_LAST (Intel) byte ordering. 1—MSB_FIRST The CCP Slave device uses the MSB_FIRST (Motorola) byte ordering. |
| u32 | mcPropECU_CRO_ID | Returns the CRO ID, which is used to send commands and data from the host to the slave device. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| nctType Taskref | mcPropECU_CRO_Task | NI-CAN Task reference to the CAN Task assigned to the CRO ID. |
| u32 | mcPropECU_DTO_ID | Returns the DTO ID, which is used by the ECU to respond to CCP commands and to send data and status information to the CCP master. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| nctType Taskref | mcPropECU_DTO_Task | NI-CAN Task reference to the CAN Task assigned to the DTO ID. |
| i32 | mcPropECU_EventChannel | Translates the event channel name to the event channel number. Pass the event channel name in the Name parameter of GetProperty. |
| [u8] | mcPropECU_ID | Returns the slave device identifier. This ID information is optional and specific to the ECU implementation. For more information about the CCP slave ID information refer to the documentation for the ECU. |
| u8 | mcPropECU_ID_DataType | Returns a data type qualifier of the slave device ID information. This ID information is optional and specific to the ECU implementation. For more information about the CCP slave ID information refer to the documentation for the ECU. |
| u8 | mcPropECU_ID_Length | Returns the length of the slave device identifier in bytes. |
| u32 | mcPropECU_Interface | Returns the interface initialized for the task, such as with mcDAQInitialize. |
| [u8] | mcPropECU_MasterID | Returns CCP master ID information. This ID information is optional and specific to the ECU implementation. For more information about the CCP master ID information refer to the documentation for the ECU. |
| str | mcPropECU_Name | Returns the name of the selected ECU opened by mcECUSelectEx. |
| str | mcPropECU_TransportLayerInstance | Returns the Transport Layer Instance name of the selected transport protocol instance. Empty string (default) indicates that no named instance is selected. The fallbacks, in order, are a single unnamed instance of the transport protocol in the IF_DATA XCPplus block or the IF_DATA XCP block. Otherwise, no transport protocol related properties can be read from the database. |
| u32 | mcPropECU_TransportLayerInstance_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_TransportLayerInstance. |
| str | mcPropECU_Comment | Returns the comment of the selected ECU opened by mcECUSelectEx. |
| u32 | mcPropECU_Comment_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_Comment. |
| u8 | mcPropECU_XCP_NumSegments | Returns the number of XCP memory segments found for this ECU. |
| u8 | mcPropECU_XCP_NumPages | Returns the number of memory pages defined for the memory segment specified in the Name input. Specify the segment by the string SEGMENT[<n>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property). |
| u8 | mcPropECU_XCP_AddressExtension | Returns the memory address extension for the memory segment specified in the Name input. Specify the segment by the string SEGMENT[<n>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property). |
| u8 | mcPropECU_XCP_CompressionMethod | Returns the compression method for the memory segment specified in the Name input. A value of 0 means no compression. Other values are user defined. Specify the segment by the string SEGMENT[<n>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property). |
| u8 | mcPropECU_XCP_EncryptionMethod | Returns the encryption method for the memory segment specified in the Name input. A value of 0 means no encryption. Other values are user defined. Specify the segment by the string SEGMENT[<n>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property). |
| u8 | mcPropECU_XCP_PageNo | Returns the logical page number for the memory segment page specified in the Name input. Specify the page by the string SEGMENT[<n>]PAGE[<m>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property) and m is the decimal representation of the page number within the segment (0..M-1, where M is the number returned from the mcPropECU_XCP_NumPages property for this segment). |
| u8 | mcPropECU_XCP_PageECUAccess | Returns a flag indicating ECU access rights for the memory segment page specified in the Name input. Defined values are: 0ECU access not allowed1ECU access allowed without XCP access only2ECU access allowed with XCP access only3ECU access allowed always Specify the page by the string SEGMENT[<n>]PAGE[<m>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property) and m is the decimal representation of the page number within the segment (0..M-1, where M is the number returned from the mcPropECU_XCP_NumPages property for this segment). |
| 0 | ECU access not allowed |  |
| 1 | ECU access allowed without XCP access only |  |
| 2 | ECU access allowed with XCP access only |  |
| 3 | ECU access allowed always |  |
| u8 | mcPropECU_XCP_PageXCPReadAccess | Returns a flag indicating XCP Read access rights for the memory segment page specified in the Name input. Defined values are: 0XCP Read access not allowed1XCP Read access allowed without ECU access only2XCP Read access allowed with ECU access only3XCP Read access allowed always Specify the page by the string SEGMENT[<n>]PAGE[<m>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property) and m is the decimal representation of the page number within the segment (0..M-1, where M is the number returned from the mcPropECU_XCP_NumPages property for this segment). |
| 0 | XCP Read access not allowed |  |
| 1 | XCP Read access allowed without ECU access only |  |
| 2 | XCP Read access allowed with ECU access only |  |
| 3 | XCP Read access allowed always |  |
| u8 | mcPropECU_XCP_PageXCPWriteAccess | Returns a flag indicating XCP Write access rights for the memory segment page specified in the Name input. Defined values are: 0XCP Write access not allowed1XCP Write access allowed without ECU access only2XCP Write access allowed with ECU access only3XCP Write access allowed always Specify the page by the string SEGMENT[<n>]PAGE[<m>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property) and m is the decimal representation of the page number within the segment (0..M-1, where M is the number returned from the mcPropECU_XCP_NumPages property for this segment). |
| 0 | XCP Write access not allowed |  |
| 1 | XCP Write access allowed without ECU access only |  |
| 2 | XCP Write access allowed with ECU access only |  |
| 3 | XCP Write access allowed always |  |
| u8 | mcPropECU_XCP_PageInitSegment | Returns the number of the segment that initializes the memory segment page specified in the Name input. Specify the page by the string SEGMENT[<n>]PAGE[<m>], where <n> is the decimal representation of the segment number (0..N-1, where N is the number returned from the mcPropECU_XCP_NumSegments property) and m is the decimal representation of the page number within the segment (0..M-1, where M is the number returned from the mcPropECU_XCP_NumPages property for this segment). |
| [u16] | mcPropECU_DAQListNumbers | Returns an array of DAQ list numbers for all DAQ lists defined in the A2L file. |
| u32 | mcPropECU_TimingFactor | Returns the used timing factor, which you can use to increase XCP or CCP command timeout values. For details on the default Command Timeout values, refer to the XCP or CCP Protocol Specification. |
| u16 | mcPropDAQList_MaxLength | Returns the maximum length of the DAQ list. |
| u32 | mcPropDAQList_CANIdSelectMode | Returns how to select the CAN ID for the specified DAQ list: 0—CAN_ID_FIXED The CAN Identifier is a predefined fixed number. 1—CAN_ID_VARIABLE The CAN Identifier is a variable number. 2—CAN_ID_DTO_ID The CAN Identifier is the same as the DTO identifier. |
| u32 | mcPropDAQList_CANId | Returns the CAN ID for the specified DAQ list if mcPropDAQList_CANIdSelectMode == CAN_ID_FIXED. |
| u8 | mcPropDAQList_FirstPID | Returns the first Packet ID for the specified DAQ list. |
| u32 | mcPropDAQList_NumberOfEventChannels | Returns the number of allowed event channels for the specified DAQ list. |
| [u8] | mcPropDAQList_EventChannels | Returns a list of event channel numbers that can be used with the given DAQ list. The DAQ list is determined by the Name parameter in mcGetProperty containing a string representation of the decimal DAQ list number, e.g., '2.' |
| u32 | mcPropDAQList_ReductionAllowed | Returns whether or not the specified DAQ list allows reduction. |
| u32 | mcPropDAQList_NumberOfExcludedDAQLists | Returns the length of the array containing the numbers of DAQ lists not working together with the current DAQ list. |
| u16 | mcPropDAQList_ExcludedDAQLists | Returns an array containing the numbers of DAQ lists not working together with the current DAQ list. |
| str | mcPropDAQList_Name | Name of the DAQ list (measurement source). Pass the DAQ list number converted to a string in the Name parameter of GetProperty. The available DAQ list number can be obtained by the ECU_DAQListNumbers property. |
| str | mcPropDAQList_Name_Size | Call this property before calling mcPropDAQList_Name to find the amount of storage needed to get the name value. |
| str | mcPropDAQList_DisplayIdentifier | Optional property you can use as a display name as an alternative to the DAQList_Name property. |
| str | mcPropDAQList_DisplayIdentifier_Size | Call this property before calling mcPropDAQList_DisplayIdentifier to find the amount of storage needed to get the display identifier value. |
| u32 | mcPropECU_Name_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_Name. |
| str | mcPropECU_SeedChkDllPath | Determines the directory where the ECU M&C Toolkit expects to find the Seedkey or Checksum DLL. If the property is an empty string (default), the ECU M&C Toolkit expects the DLLs in the same directory as the A2L file. If your DLLs are in a different directory, set this property pointing to this directory. |
| str | mcPropECU_SeedChkDllPath_Size | Returns the required buffer size to read the mcPropECU_SeedChkDllPath property. |
| str | mcPropECU_SeedKey_Cal | Returns the file name of the SeedKey DLL used for Calibration purposes. If SeedKey is configured for remote access, the output is RSK:<server ip address>,<port>. |
| u32 | mcPropECU_SeedKey_Cal_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_SeedKey_Cal. |
| str | mcPropECU_SeedKey_DAQ | Returns the file name of the SeedKey DLL used for DAQ purposes. If SeedKey is configured for remote access, the output is RSK:<server ip address>,<port>. |
| u32 | mcPropECU_SeedKey_DAQ_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_SeedKey_DAQ. |
| str | mcPropECU_SeedKey_Prog | Returns the file name of the SeedKey DLL used for programming purposes. If SeedKey is configured for remote access, the output is RSK:<server ip address>,<port>. |
| u32 | mcPropECU_SeedKey_Prog_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_SeedKey_Prog. |
| str | mcPropECU_SeedKey_XCP | Returns the file name of the SeedKey DLL for XCP. If SeedKey is configured for remote access, the output is RSK:<server ip address>,<port>. |
| str | mcPropECU_LogFileName | Returns the filename (full path) where the XCP or CCP protocol traffic is logged in ASCII format for debugging purposes. An empty path indicates no logging (default). Note that on RT and cRIO systems, the logfile is created on the target system and must be transferred to the host after logging has been completed. Note that no additional CAN port is used for the logging, which makes this method superior to any other method such as running a bus monitor parallel. |
| str | mcPropECU_LogFileName_Size | Returns the size of the buffer needed to retrieve the mcPropECU_LogFileName property. |
| u32 | mcPropECU_SeedKey_XCP_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropECU_SeedKey_XCP. |
| u8 | mcPropECU_Single_Byte_DAQ_Lists | Determines if an ECU supports single-byte or multi-byte DAQ list entries. |
| u32 | mcPropECU_StationAddress | Returns the station address of the slave device. CCP is based on the idea that several ECUs can share the same CAN Arbitration IDs for CCP communication. To avoid communication conflicts, CCP defines a Station Address that has to be unique for all ECUs sharing the same CAN Arbitration IDs. Unless an ECU has been addressed by its Station Address, the ECU must not react to CCP commands sent by the CCP master. |
| u32 | mcPropECU_MeasSplitAllowed | Returns the Boolean property Meas Split Allowed. For measurements in DAQ List mode, the master creates DAQ lists which determines frames with data transmitted by the ECU. The first byte in this frame (ODT) is a PID identifier, the remaining bytes in the frames are used for measurement data (e.g. with CAN 2.0, 7 bytes can be used for data). Depending on the measurements not all bytes in the frame can be used. For example, measuring seven 32-bit values in the ECU requires transmitting seven frames per sampling point as only one 4-byte value can be placed in one frame. The remaining 3 bytes are unused. Setting this property to true (1) allows splitting the measurements across CAN frames, so the seven values can be packed into only four frames (4 frames * 7 bytes = 28 data bytes for DAQ data). The default value is false (0). |
| u16 | mcPropECU_MappingMode | Address mapping mode to be used when accessing the ECU memory by addresses. 0No Mapping: Original addresses from the A2L database are used.1Defined Pages: This mode requires setting the source and target pages. The memory pages are defined in the A2L database in the DEFINED_PAGES section. The source and target pages can be set either by the page name or by the logical page number. If the original address takes place within the source page, it will be re-mapped to the target page with the same offset to the beginning of the page.2ADDR_MAPPING: Use address mapping defined in the A2L database in the ADDR_MAPPING section. |
| 0 | No Mapping: Original addresses from the A2L database are used. |  |
| 1 | Defined Pages: This mode requires setting the source and target pages. The memory pages are defined in the A2L database in the DEFINED_PAGES section. The source and target pages can be set either by the page name or by the logical page number. If the original address takes place within the source page, it will be re-mapped to the target page with the same offset to the beginning of the page. |  |
| 2 | ADDR_MAPPING: Use address mapping defined in the A2L database in the ADDR_MAPPING section. |  |
| str | mcPropECU_MappingSourceName | Name of the source page to be used for the address mapping in Defined Pages mode. |
| u32 | mcPropECU_MappingSourceNameLength | Minimum buffer size required for the name in mcGetProperty:mcPropECU_MappingSourceName. |
| u16 | mcPropECU_MappingSource | Logical page number of the source page to be used for the address mapping in Defined Pages mode. |
| str | mcPropECU_MappingTargetName | Name of the target page to be used for the address mapping in Defined Pages mode. |
| u32 | mcPropECU_MappingTargetNameLength | Minimum buffer size required for the name in mcGetProperty:mcPropECU_MappingTargetName. |
| u16 | mcPropECU_MappingTarget | ogical page number of the source page to be used for the address mapping in Defined Pages mode. |
| u32 | mcPropECU_XCP_Timeout_T1 mcPropECU_XCP_Timeout_T2 mcPropECU_XCP_Timeout_T3 mcPropECU_XCP_Timeout_T4 mcPropECU_XCP_Timeout_T5 mcPropECU_XCP_Timeout_T6 mcPropECU_XCP_Timeout_T7 | Returns one of the seven timeout values (in milliseconds) defined in the XCP standard for the various XCP commands. For details of which timeout applies to a specific command, refer to the XCP standard. The values are typically read from an A2L file, but may be overridden manually. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_std | Returns the timeout value (in milliseconds) for most of the CCP commands. For details of which timeout applies to a specific command, refer to the CCP standard. Default: 40. Standard: 25. The default is chosen slightly higher to allow for slower ECUs. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_pgm | Returns the timeout value (in milliseconds) for the CCP programming commands. For details of which timeout applies to a specific command, refer to the CCP standard. Default: 120. Standard: 100. The default is chosen slightly higher to allow for slower ECUs. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_mem | Returns the timeout value (in milliseconds) for the CCP memory commands. For details of which timeout applies to a specific command, refer to the CCP standard. Default and Standard: 30000. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_diag | Returns the timeout value (in milliseconds) for the CCP DIAG_SERVICE command. Default and Standard: 500. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_act | Returns the timeout value (in milliseconds) for the CCP ACTION_SERVICE command. Default: 500. Standard: 5000. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropGen_Version_Build | Returns the build number of the ECU M&C software. This number applies to Development, Alpha, and Beta phase only, and should be ignored for Release phase. |
| str | mcPropGen_Version_Comment | Returns a comment string for the ECU M&C software. If you received a custom release of ECU M&C from NI, this comment often describes special features of the release. |
| u32 | mcPropGen_Version_Comment_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropGen_Version_Comment. |
| u32 | mcPropGen_Version_Major | Returns the major version of the ECU M&C software, such as the 1 in version 1.2.5. |
| u32 | mcPropGen_Version_Minor | Returns the minor version of the ECU M&C software, such as the 2 in version 1.2.5. |
| u32 | mcPropGen_Version_Update | Returns the update version of the ECU M&C software, such as the 5 in version 1.2.5. |
| str | mcPropIPAddress | Returns the IP address of the slave device for XCP on Ethernet (TCP or UDP) as a string. |
| u32 | mcPropIPAddress_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropIPAddress. |
| u16 | mcPropIPPort | Returns the IP port for XCP on Ethernet (TCP or UDP). |
| str | mcPropIPSourceAddress | Returns the IP address of the host Ethernet interface for XCP on Ethernet (TCP or UDP) as a string. Empty string (default) indicates the using of the host primary Ethernet interface. |
| u32 | mcPropIPSourceAddress_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropIPSourceAddress. |
| i32 | mcPropIPSourcePort | Returns the source port (XCP master port) used for Ethernet communication. The default value is -1, which indicates that the source port will be chosen by the operating system. Valid port values are 0 to 65535. Note that port 0 is reserved and typically should not be used. |
| str | mcPropIPXnetStackName | Returns the name of the XNET IP Stack to be used. If this parameter is empty string (default), the native operating system IP stack will be used. |
| u32 | mcPropIPXnetStackName_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropIPXnetStackName. |
| str | mcPropIPXnetLocalInterface | Returns the name of the local interface that is used with the specified XNET IP Stack for this session. This property is ignored for the native operating system IP stack. |
| u32 | mcPropIPXnetLocalInterface_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropIPXnetLocalInterface. |
| u32 | mcPropMeas_Address | Returns the address of the selected Measurement in the memory of the control unit. |
| u32 | mcPropMeas_ByteOrder | Returns the specified byte order: 0—Intel format Bytes are in little-endian order, with least-significant bit first. 1—Motorola format Bytes are in big-endian order, with most-significant bit first. |
| u8 | mcPropMeas_Datatype | Returns the data type of the Measurement task. |
| u8 | mcPropMeas_Extension | Returns the address extension of the ECU address. This optional parameter may contain additional address information defined in the A2L database. For instance it can be used, to distinguish different address spaces of an ECU (multi-microcontroller devices). |
| u32 | mcPropMeas_IsVirtual | Returns whether the Measurement is virtual. Virtual Measurements are not transmitted by the ECU but are calculated in the application. They return an error when opened in a DAQ list. |
| f64 | mcPropMeas_Maximum | Returns the maximum value of the Measurement. |
| f64 | mcPropMeas_Minimum | Returns the minimum value of the Measurement. |
| u32 | mcPropMeas_ReadOnly | Returns TRUE if the selected Measurement is read only and can only be accessed through mcMeasurementRead, or returns FALSE if the Measurement can be accessed through mcMeasurementWrite as well. |
| str | mcPropMeas_Unit | Returns the unit string defined for this Measurement in the A2L database. |
| u32 | mcPropMeas_Unit_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropMeas_Unit. |
| u16 | mcPropMeas_Comment | Returns the comment of this Measurement defined in the A2L database. |
| f64 | mcPropMeas_Comment_Size | Returns the required buffer size for the measurement comment when using mcPropMeas_Comment property. |
| f64 | mcPropMeas_Scale_Factor | Returns the scaling factor defined for this Measurement in the A2L database. |
| f64 | mcPropMeas_Scale_Offset | Returns the scaling offset defined for this Measurement in the A2L database. |
| u32 | mcPropMeas_Scale_Type | Returns the scaling type defined for this Measurement in the A2L database. 0: Unknown The type of the scaling could not be derived from the A2L file content. 1: Rational Function The related scaling is based on a rational function of second order. This covers also the linear scaling, given by factor and offset. 2: Enumeration Text The related scaling is based on the COMPU_VTAB keyword within the A2L file. Read functions return nonscaled, numeric values.Write functions accept nonscaled, numeric values.It is possible to use mcDoubleToText and mcTextToDouble to convert between enumeration text values and double values. 3: Range Text The related scaling is based on the COMPU_VTAB_RANGE keyword within the A2L file. Read functions return nonscaled, numeric values.Write functions accept nonscaled, numeric values.It is possible to use mcDoubleToText and mcTextToDouble to convert between range text values and double values. 4: Formula The related scaling is based on the FORMULA keyword within the A2L file, using a free formula to calculate the values. 5: Table (Using Interpolation) The related scaling is based on the TAB_INTP keyword within the A2L file, using interpolation between x-y pairs. 6: Table (Without Interpolation) The related scaling is based on the TAB_NOINTP keyword within the A2L file, using x-y pairs without interpolation. |
| u32 | mcPropMeas_Scale_TextValues_Size | If the scaling type is 2 = Enumeration Text or 3 = Range Text, you can use this property to request the length needed to store the comma-separated list of text values that can be converted into raw values (refer to the mcPropMeas_Scale_TextValues property). |
| str | mcPropMeas_Scale_TextValues | If the scaling type is 2 = Enumeration Text or 3 = Range Text, you can use this property to request the comma-separated list of text values which can be converted into raw values. |
| u32 | mcPropOptCmd_ACTION_SERVICE | Returns whether the ECU supports the optional CCP Command ACTION_SERVICE. |
| u32 | mcPropOptCmd_BUILD_CHKSUM | Returns whether the ECU supports the optional CCP Command BUILD_CHKSUM. |
| u32 | mcPropOptCmd_CLEAR_MEMORY | Returns whether the ECU supports the optional CCP Command CLEAR_MEMORY. |
| u32 | mcPropOptCmd_DIAG_SERVICE | Returns whether the ECU supports the optional CCP Command DIAG_SERVICE. |
| u32 | mcPropOptCmd_DNLOAD_6 | Returns whether the ECU supports the optional CCP Command DNLOAD_6. |
| u32 | mcPropOptCmd_GET_ACTIVE_CAL_PAGE | Returns whether the ECU supports the optional CCP Command GET_ACTIVE_CAL_PAGE. |
| u32 | mcPropOptCmd_GET_S_STATUS | Returns whether the ECU supports the optional CCP Command GET_S_STATUS. |
| u32 | mcPropOptCmd_GET_SEED | Returns whether the ECU supports the optional CCP Command GET_SEED. |
| u32 | mcPropOptCmd_MOVE | Returns whether the ECU supports the optional CCP Command MOVE. |
| u32 | mcPropOptCmd_PROGRAM | Returns whether the ECU supports the optional CCP Command PROGRAM. |
| u32 | mcPropOptCmd_PROGRAM_6 | Returns whether the ECU supports the optional CCP Command PROGRAM_6. |
| u32 | mcPropOptCmd_SELECT_CAL_PAGE | Returns whether the ECU supports the optional CCP Command SELECT_CAL_PAGE. |
| u32 | mcPropOptCmd_SET_S_STATUS | Returns whether the ECU supports the optional CCP Command SET_S_STATUS. |
| u32 | mcPropOptCmd_SHORT_UP | Returns whether the ECU supports the optional CCP Command SHORT_UP. |
| u32 | mcPropOptCmd_START_STOP_ALL | Returns whether the ECU supports the optional CCP Command START_STOP_ALL. |
| u32 | mcPropOptCmd_TEST | Returns whether the ECU supports the optional CCP Command TEST. |
| u32 | mcPropOptCmd_UNLOCK | Returns whether the ECU supports the optional CCP Command UNLOCK. |
| u8 | mcPropPGM_AccessMethod | Returns the selected access mode for mcProgram and mcClearMemory. 0x00—Absolute Access Mode (default). The MTA uses physical addresses. 0x00—Functional Access Mode. The MTA functions as a block sequence number of the new flash content file. 0x80...0xFF—User defined. It is possible to use different access modes for clearing and programming. |
| u8 | mcPropPGM_CompressionMethod | Returns the selected compression method used for mcProgram. 0—Data is uncompressed (default). 0x80...0xFF—User defined. |
| u8 | mcPropPGM_EncryptionMethod | Returns the selected encryption method used for mcProgram. 0—Data is not encrypted (default). 0x80...0xFF—User defined. |
| u8 | mcPropPGM_ProgrammingMethod | Returns the selected programming method used for mcProgram. 0—Sequential programming (default). 0x80...0xFF—User defined. |
| u32 | mcPropGroup_IsRoot | Returns a nonzero value for Groups that are root. |
| str | mcPropGroup_Comment | Returns the comment of the selected Group. |
| u32 | mcPropGroup_Comment_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropGroup_Comment. |
| str | mcPropFunction_Comment | Returns the comment of the selected Function. |
| u32 | mcPropFunction_Comment_Size | Returns the number of bytes to be allocated if you call mcGetProperty with the parameter mcPropFunction_Comment. |

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcmeasurementcreate.html language=enus -->
## TOPIC 00055: mcMeasurementCreate

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcmeasurementcreate.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcmeasurementcreate.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates a Measurement object in memory. Format mcTypeStatus mcMeasurementCreate( mcTypeTaskRef ECURefNum, char *MeasurementName, mcAddress Address, i32 DataType, u8 DataSize, char *ConversionName); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This referenc

### mcMeasurementCreate

Purpose

Creates a Measurement object in memory.
Format

| mcTypeStatus | mcMeasurementCreate( mcTypeTaskRef ECURefNum, char *MeasurementName, mcAddress Address, i32 DataType, u8 DataSize, char *ConversionName); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *MeasurementName, |
| mcAddress | Address, |
| i32 | DataType, |
| u8 | DataSize, |
| char | *ConversionName); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecucreate).

Address

Configures the target address for the programming operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the programming address.

**Extension**

Extension contains the extension part of the address.

DataType

DataType sets the data type of the measurement task.

| DataType | Data Format |
| --- | --- |
| 0 | Unsigned byte |
| 1 | Signed byte |
| 2 | Unsigned word |
| 3 | Signed word |
| 4 | Unsigned long |
| 5 | Signed long |
| 6 | Float 32 |

DataSize

Sets the size of the measurement data and corresponds to the selected DataType.

| Data Format | DataSize |
| --- | --- |
| Unsigned byte | 1 |
| Signed byte | 1 |
| Unsigned word | 2 |
| Signed word | 2 |
| Unsigned long | 4 |
| Signed long | 4 |
| Float 32 | 4 |

ConversionName

ConversionName identifies the referred conversion object that [mcConversionCreate](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcconversioncreate) defines.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

Use mcMeasurementCreate to create a measurement object in memory instead of referring to a predefined measurement in the A2L database.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcmeasurementread.html language=enus -->
## TOPIC 00056: mcMeasurementRead

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcmeasurementread.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcmeasurementread.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads a single scaled Measurement value from the ECU. Format mcTypeStatus mcMeasurementRead( mcTypeTaskRef RefNum, char *MeasurementName, f64 *Value); Input RefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . MeasurementName Me

### mcMeasurementRead

Purpose

Reads a single scaled Measurement value from the ECU.
Format

| mcTypeStatus | mcMeasurementRead( mcTypeTaskRef RefNum, char *MeasurementName, f64 *Value); |
| --- | --- |
| mcTypeTaskRef | RefNum, |
| char | *MeasurementName, |
| f64 | *Value); |

Input

RefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

MeasurementName

MeasurementName is the name of a Measurement channel stored in the A2L database file from which a Measurement value is to be read.
Output

Value

Returns a single sample for the Measurement channel initialized in MeasurementName.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcMeasurementRead performs a single point read (upload) of a single scaled Measurement from the selected ECU without opening a Measurement task.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcmeasurementreadraw.html language=enus -->
## TOPIC 00057: mcMeasurementReadRaw

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcmeasurementreadraw.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcmeasurementreadraw.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Reads a single raw (unscaled) Measurement value from the ECU. Format mcTypeStatus mcMeasurementReadRaw( mcTypeTaskRef ECURefNum, char *MeasurementName, u64 *Value); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from mcE

### mcMeasurementReadRaw

Purpose

Reads a single raw (unscaled) Measurement value from the ECU.
Format

| mcTypeStatus | mcMeasurementReadRaw( mcTypeTaskRef ECURefNum, char *MeasurementName, u64 *Value); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *MeasurementName, |
| u64 | *Value); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

MeasurementName

MeasurementName is the name of a Measurement channel stored in the A2L database file from which a Measurement value is to be read.
Output

Value

Returns a single sample for the Measurement channel initialized in MeasurementName.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcMeasurementReadRaw performs a single point read (upload) of a single raw Measurement from the selected ECU without opening a Measurement task.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcmeasurementwrite.html language=enus -->
## TOPIC 00058: mcMeasurementWrite

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcmeasurementwrite.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcmeasurementwrite.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes a single scaled Measurement value to the ECU. Format mcTypeStatus mcMeasurementWrite( mcTypeTaskRef RefNum, char *MeasurementName, f64 Values); Input RefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . MeasurementName Me

### mcMeasurementWrite

Purpose

Writes a single scaled Measurement value to the ECU.
Format

| mcTypeStatus | mcMeasurementWrite( mcTypeTaskRef RefNum, char *MeasurementName, f64 Values); |
| --- | --- |
| mcTypeTaskRef | RefNum, |
| char | *MeasurementName, |
| f64 | Values); |

Input

RefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

MeasurementName

MeasurementName is the name of a Measurement channel stored in the A2L database file to which a Measurement value is to be written.

Values

Writes a single sample for the Measurement channel initialized in MeasurementName.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcMeasurementWrite performs a single point write (download) of a scaled Measurement into the selected ECU without opening a Measurement task. mcMeasurementWrite can only be performed if the Measurement channel is not set to read only. To query if an ECU Measurement channel can be accessed by mcMeasurementWrite, call [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcgetproperty) with the parameter mcPropMeas_ReadOnly.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcmeasurementwriteraw.html language=enus -->
## TOPIC 00059: mcMeasurementWriteRaw

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcmeasurementwriteraw.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcmeasurementwriteraw.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Writes a single raw (unscaled) Measurement value to the ECU. Format mcTypeStatus mcMeasurementWriteRaw( mcTypeTaskRef ECURefNum, char *MeasurementName, u64 Values); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from mcE

### mcMeasurementWriteRaw

Purpose

Writes a single raw (unscaled) Measurement value to the ECU.
Format

| mcTypeStatus | mcMeasurementWriteRaw( mcTypeTaskRef ECURefNum, char *MeasurementName, u64 Values); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| char | *MeasurementName, |
| u64 | Values); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

MeasurementName

MeasurementName is the name of a Measurement channel stored in the A2L database file to which a Measurement value is to be written.

Values

Writes a single sample for the Measurement channel initialized in MeasurementName.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcMeasurementWriteRaw performs a single point write (download) of a raw Measurement into the selected ECU without opening a Measurement task. mcMeasurementWriteRaw can only be performed if the Measurement channel is not set to read only. To query if an ECU Measurement channel can be accessed by mcMeasurementWriteRaw, call mcGetProperty with the parameter mcPropMeas_ReadOnly.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcprogram.html language=enus -->
## TOPIC 00060: mcProgram

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcprogram.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcprogram.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Programs a memory block on the ECU. Format mcTypeStatus mcProgram( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *Data); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Address Configures the target

### mcProgram

Purpose

Programs a memory block on the ECU.
Format

| mcTypeStatus | mcProgram( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *Data); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address, |
| u32 | BlockSize, |
| u8 | *Data); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Configures the target address for the programming operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the programming address.

**Extension**

Extension contains the extension part of the address.

BlockSize

BlockSize determines the size of the data block which is transferred to the ECU and used for programming from the MTA0 target.

Data

data contains the byte array that is transmitted to the ECU.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If you are using the CCP protocol, mcProgram implements the CCP command PROGRAM. The command is used to program the specified data into non-volatile ECU memory (Flash, EEPROM, etc.). Programming starts at the selected MTA0 address and extension defined in the **Address** struct. The mcProgram function auto-increments the ECU MTA0 address.

If you are using the XCP protocol, mcProgram implements the XCP command PROGRAM. The command is used to program a non-volatile memory segment inside the ECU slave. Depending on the access mode (defined by PROGRAM_FORMAT), two different concepts are supported. The end of the memory segment is indicated when BlockSize is set to 0. The end of the overall programming sequence is indicated by a using the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset) command which executes the XCP command PROGRAM_RESET, causing the slave device to move into a disconnected state. Usually a hardware reset of the slave device is executed. This command may support block transfer similar to the commands DOWNLOAD and DOWNLOAD_NEXT. For further information on how to use mcProgram and details on block mode transfers refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcprogramreset.html language=enus -->
## TOPIC 00061: mcProgramReset

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcprogramreset.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcprogramreset.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Indicates the end of a programming sequence. Format mcTypeStatus mcProgramReset( mcTypeTaskRef ECURefNum); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Output Return ValueThe return value indicates the status of

### mcProgramReset

Purpose

Indicates the end of a programming sequence.
Format

| mcTypeStatus | mcProgramReset( mcTypeTaskRef ECURefNum); |
| --- | --- |
| mcTypeTaskRef | ECURefNum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If you are using the XCP protocol, [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset) implements the XCP command PROGRAM_RESET. This optional command indicates the end of a non-volatile memory programming sequence and may or may not have a response from the ECU. In either case, the slave device will go into a disconnected state.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset) may be used to reset a slave device for other purposes. For further information on how to use program ECU memory and to use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset) command refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcprogramstart.html language=enus -->
## TOPIC 00062: mcProgramStart

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcprogramstart.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcprogramstart.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Indicates the start of a programming sequence. Format mcTypeStatus mcProgramStart( mcTypeTaskRef ECURefNum); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Output Return ValueThe return value indicates the status

### mcProgramStart

Purpose

Indicates the start of a programming sequence.
Format

| mcTypeStatus | mcProgramStart( mcTypeTaskRef ECURefNum); |
| --- | --- |
| mcTypeTaskRef | ECURefNum); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If you are using the XCP protocol, [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramstart](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramstart) implements the XCP command PROGRAM_START. This optional command the beginning of a programming sequence into a non-volatile memory area. If the slave device is not in a state which permits programming, an error is returned. The memory programming commands The end of a non-volatile memory programming sequence is indicated by using the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramreset) function.

For further information on how to use program ECU memory and to use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramstart](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcprogramstart) command refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcsetproperty.html language=enus -->
## TOPIC 00063: mcSetProperty

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcsetproperty.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcsetproperty.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets a property of the driver, the database, the ECU, a characteristic, a Measurement, or a Measurement task. Format mcTypeStatus mcSetProperty( mcTypeTaskRef RefNum, cstr Name, u32 PropertyID, u32 SizeOfValue, void *Value); Input RefNum RefNum is any ECU M&C task reference which consists of

### mcSetProperty

Purpose

Sets a property of the driver, the database, the ECU, a characteristic, a Measurement, or a Measurement task.
Format

| mcTypeStatus | mcSetProperty( mcTypeTaskRef RefNum, cstr Name, u32 PropertyID, u32 SizeOfValue, void *Value); |
| --- | --- |
| mcTypeTaskRef | RefNum, |
| cstr | Name, |
| u32 | PropertyID, |
| u32 | SizeOfValue, |
| void | *Value); |

Input

RefNum

RefNum is any ECU M&C task reference which consists of a valid link to the opened A2L database (DBRefNum), a selected ECU (ECURefNum) or a Measurement task (DAQRefNum). RefNum has to be valid for the related PropertyID type.

Name

Name is not used and can be set to NULL. This parameter may be used for further extensions.

PropertyID

Selects the property to set. The PropertyID is represented by a property name as defined in the niemc.h header file. Refer to the Properties section for PropertyID data type, name, and description.

SizeOfValue

Number of bytes allocated for the Value output. This size normally depends on the data type listed in the description of the property.

Value

Provides the property value. PropertyId determines the data type of the value.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [mcStatusToString](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

There are four types of properties which can be modified in the poly input value: ECU-specific properties, DAQ-specific properties, Characteristic-specific properties, and Measurement-specific properties.

#### ECU-Specific Properties

You cannot set an ECU property while the application is connected to the ECU. If you need to change a ECU property prior to connecting, call [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex), followed by mcSetProperty, and then [mcECUConnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect). After you connect to the ECU, you also can change a property by calling [mcECUDisconnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecudisconnect), followed by mcSetProperty, and then [mcECUConnect](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuconnect) to restart the task. Refer to the ECU-Specific Properties table below for a list of ECU-specific values for PropertyID.

#### DAQ-Specific Properties

You cannot set a DAQ property while a Measurement task is running. If you need to change a property prior to starting a Measurement task call [mcDAQInitialize](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqinitialize), followed by mcSetProperty, and then [mcDAQStartStop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop). After you start the Measurement task, you also can change a property by calling [mcDAQStartStop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop), followed by mcSetProperty, and then [mcDAQStartStop](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdaqstartstop) to restart the task. Refer to the DAQ-Specific Properties table below for a list of DAQ-specific values for PropertyID.

#### Properties

#### ECU-Specific Properties

| Data Type | Name | Description |
| --- | --- | --- |
| u32 | mcPropCANBaudrate | Sets the CAN Baud rate for XCP or CCP on CAN which is used to send commands and data from the host to the slave device. |
| u32 | mcPropCANTermination | For all XNET devices, the termination is software selectable. XNET provides the option of 120 Ω between Bus Plus and Bus Minus or no termination. The Termination property configures the onboard termination of the NI-XNET interface CAN connector (port). The Boolean property supports two values: TRUE = Termination ON and FALSE = Termination Off. However, different CAN hardware has different termination requirements, and the termination values have different meanings. Refer to the Termination attribute in the XNET API for more details. (This property is supported for NI-XNET devices only.) 0 — FALSE (termination off) 1 — TRUE (termination on) |
| u64 | mcPropCANBaudrate64 | Set the Baud Rate in use by the CAN Interface with XCP protocol. Basic baud rates such as 125000 and 500000 are specified as numeric values. Advanced (or custom) baud rates are specific to the CAN interface in use and the description can be found in the NI-XNET documentation. The default value for the property is the baud rate set in the A2L database used for the application. If NI-XNET is used and the A2L file specifies a sampling point for the baud rate which differs from the sampling point used internally in NI-XNET, ECUMC replaces the standard baud rate value by a custom 64-bit baud rate which uses the sampling point as close as possible to the sampling point in A2L database. You can find the documentation of the NI-XNET custom baud rate in NI-XNET Hardware and Software Help under Interface:64bit Baud Rate. |
| u64 | mcPropCANFDBaudrate64 | Set the CAN FD baud rate value (used for the data part of transmission). If CAN FD is used, 64bit Baud Rate specifies the baud rate for the arbitration part of the CAN message, while this property specifies the baud rate for the data part of the CAN message. CAN FD is only supported by NI-XNET interfaces for XCP protocol. Basic baud rates such as 500000 and 2000000 are specified as numeric values. Information about the advanced (or custom) baud rates can be found in the NI-XNET Hardware and Software Help under Interface:CAN:64bit FD Baud Rate. The default value for the property is the baud rate set in the CAN_FD section of the A2L database used for the application. You can set the property to use any other baud rate or custom baud rate according to NI-XNET specification. If the A2L file specifies a sampling point for the CAN FD baud rate which differs from the sampling point used internally in NI-XNET, ECUMC replaces the standard baud rate value by a custom 64-bit baud rate which uses the sampling point as close as possible to the sampling point in A2L database. Refer to information about the custom baud rates in the NI-XNET Hardware and Software Help under Interface:64bit FD Baud Rate. Transceiver Delay Compensation defined by the A2L database is not used while calculating the custom baud rate value, as the value is hardware implementation specific and the value found in the database may not match the NI-XNET specification. If you need very specific values for the CAN FD baud rate, you need to follow the NI-XNET documentation and set a custom baud |
| u32 | mcPropCANIOmode | Set the CAN I/O Mode of the specified interface. The CAN I/O mode is only supported with XNET interfaces. It determines if the interface is running in CAN 2.0 mode (supports frames with payload up to 8 bytes), CAN FD mode (supports frames up to 64 bytes), or CAN FD+BRS mode (CAN FD with baud rate switching). The default value is determined by the A2L database used by the application. In ECU Determined mode, the master can communicate with ECUs using either traditional CAN or CAN FD frames. The master starts the communication with a traditional CAN 2.0 frame; if the ECU responds in any mode, this mode is selected for further communication. If the ECU does not respond to the CAN 2.0 frame, the master repeats (after timeout) the first command using a CAN FD frame. In ECU Determined mode, the NI-XNET interface runs in CAN FD BRS mode, so the CAN FD baud rate must be set before using this mode. In CAN FD+BRS mode, the NI-XNET interface can receive and transmit CAN 2.0, CAN FD, and CAN FD+BRS frames. 0—mcCANioMode_CAN 1—mcCANioMode_CAN_FD 2—mcCANioMode_CAN_FD_BRS 3—mcCANioMode_ECU_Determined Note CAN FD is only supported with NI-XNET version 17.0.1 or later. |
| u32 | mcPropCANUseMaxDLC | This Boolean property determines if the master in CAN 2.0 mode transmits frames with the actual used payload length or always transmits the maximum number of bytes (8 bytes). The default value of this property is being retrieved from the A2L database based on the MAX_DLC_REQUIRED keyword within the XCP_ON_CAN section. 0—FALSE 1—TRUE |
| u32 | mcPropCANFDMaxDLC | This property determines the payload length which should be used if the mcPropCANFDUseMaxDLC setting is TRUE. The default value of this property is being retrieved from the A2L database based on the MAX_DLC keyword within the CAN_FD section. The max value of this property is 64. |
| u32 | mcPropCANFDUseMaxDLC | This Boolean property determines if the master in CAN FD mode transmits frames with the actual used payload length or always transmits the maximum number of bytes, defined by the mcPropCANFDMaxDLC DLC setting (8…64 bytes). The default value of this property is being retrieved from the A2L database based on the MAX_DLC_REQUIRED keyword within the CAN_FD section. 0—FALSE 1—TRUE |
| u32 | mcPropCmd_EXCHANGE_ID | Sets whether or not the EXCHANGE_ID command should be suppressed during connection to the ECU. |
| u32 | mcPropCROID | Sets the CRO CAN Identifier for XCP or CCP on CAN used to send commands and data from the host to the slave device. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| u32 | mcPropDTOID | Sets the DTO CAN Identifier for XCP or CCP on CAN used to send commands and data from the slave device to the host. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| u32 | mcPropECU_BaudRate | Sets the Baud rate in use by the selected interface. This property applies to all tasks initialized with the NI-CAN interface. You can specify the following basic baud rates as the numeric rate: 33333, 83333, 100000, 125000, 200000, 250000, 400000, 500000, 800000, and 1000000. You can specify advanced baud rates as 8000XXYY hex, where YY is the value of Bit Timing Register 0 (BTR0), and XX is the value of Bit Timing Register 1 (BTR1). For more information, refer to the Interface Properties dialog in MAX. The value of this property is originally set within MAX, but it can be changed using mcSetProperty. |
| u32 | mcPropECU_ByteOrder | Sets the byte order of the slave device. 0—MSB_LAST The Slave device uses the MSB_LAST (Intel) byte ordering. 1—MSB_FIRST The Slave device uses the MSB_FIRST (Motorola) byte ordering. |
| str | mcPropECU_Checksum | Sets the file name of the Checksum DLL used for verifying the checksum. |
| u32 | mcPropECU_CmdByteOrder | Sets the byte order for multi-byte command parameters. 0—MSB_LAST The CCP Slave device uses the MSB_LAST (Intel) byte ordering. 1—MSB_FIRST The CCP Slave device uses the MSB_FIRST (Motorola) byte ordering. |
| u32 | mcPropECU_CRO_ID | Sets the CAN identifier for the CRO ID, which is used to send commands and data from the host to the slave device. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| u32 | mcPropECU_DTO_ID | Sets the DTO ID, which is used by the ECU to respond to CCP commands and send data and status information to the CCP master. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| u32 | mcPropECU_MasterID | Sets CCP master ID information. This ID information is optional and specific to the ECU implementation. For more information about the CCP master ID information refer to the documentation for the ECU. |
| str | mcPropECU_SeedChkDllPath | Determines the directory where the ECU M&C Toolkit expects to find the Seedkey or Checksum DLL. If the property is an empty string (default), the ECU M&C Toolkit expects the DLLs in the same directory as the A2L file. If your DLLs are in a different directory, set this property pointing to this directory. |
| str | mcPropECU_SeedKey_Cal | Sets the filename of the SeedKey DLL used for Calibration purposes. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
| str | mcPropECU_SeedKey_DAQ | Sets the filename of the SeedKey DLL used for DAQ purposes. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
| str | mcPropECU_SeedKey_Prog | Sets the filename of the SeedKey DLL used for programming purposes. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
| str | mcPropECU_SeedKey_XCP | Sets the filename of the SeedKey DLL for XCP. For Remote Seedkey access (refer to the LabVIEW examples), set the name to RSK:<server ip address>,<port>. |
| str | mcPropECU_LogFileName | Sets a filename (full path) where the XCP or CCP protocol traffic is logged in ASCII format for debugging purposes. Setting this value to an empty path (NULL or empty string) disables logging (default). Note that on RT and cRIO systems, the logfile is created on the target system and must be transferred to the host after logging has been completed. Note that no additional CAN port is used for the logging, which makes this method superior to any other method such as running a bus monitor parallel. |
| u8 | mcPropECU_Single_Byte_DAQ_Lists | Sets the ECU to support single-byte or multi-byte DAQ list entries. |
| u32 | mcPropECU_StationAddress | Sets the station address of the slave device. CCP is based on the idea that several ECUs can share the same CAN Arbitration IDs for CCP communication. To avoid communication conflicts, CCP defines a Station Address that has to be unique for all ECUs sharing the same CAN Arbitration IDs. Unless an ECU has been addressed by its Station Address, the ECU must not react to CCP commands sent by the CCP master. |
| u32 | mcPropECU_MeasSplitAllowed | Sets the Boolean property Meas Split Allowed. For measurements in DAQ List mode, the master creates DAQ lists which determines frames with data transmitted by the ECU. The first byte in this frame (ODT) is a PID identifier, the remaining bytes in the frames are used for measurement data (e.g., with CAN 2.0, seven bytes can be used for data). Depending on the measurements not all bytes in the frame can be used. For example, measuring seven 32-bit values in the ECU requires transmitting seven frames per sampling point, as only one 4-byte value can be placed in one frame. The other three bytes remain unused. Setting this property to true (1) allows splitting the measurements across CAN frames, so the seven values can be packed into four frames only (4 frames * 7 bytes = 28 data bytes for DAQ data). The default value is false (0). |
| u16 | mcPropECU_MappingMode | Address mapping mode to be used when accessing the ECU memory by addresses. 0No Mapping: Original addresses from the A2L database are used.1Defined Pages: This mode requires setting the source and target pages. The memory pages are defined in the A2L database in the DEFINED_PAGES section. The source and target pages can be set either by the page name or by the logical page number (the last Set Property call defines the page). If the original address takes place within the source page, it will be re-mapped to the target page with the same offset to the beginning of the page.2ADDR_MAPPING: Use address mapping defined in the A2L database in the ADDR_MAPPING section. |
| 0 | No Mapping: Original addresses from the A2L database are used. |  |
| 1 | Defined Pages: This mode requires setting the source and target pages. The memory pages are defined in the A2L database in the DEFINED_PAGES section. The source and target pages can be set either by the page name or by the logical page number (the last Set Property call defines the page). If the original address takes place within the source page, it will be re-mapped to the target page with the same offset to the beginning of the page. |  |
| 2 | ADDR_MAPPING: Use address mapping defined in the A2L database in the ADDR_MAPPING section. |  |
| str | mcPropECU_MappingSourceName | Name of the source page to be used for the address mapping in Defined Pages mode. |
| u16 | mcPropECU_MappingSource | Logical page number of the source page to be used for the address mapping in Defined Pages mode. |
| str | mcPropECU_MappingTargetName | Name of the target page to be used for the address mapping in Defined Pages mode. |
| u16 | mcPropECU_MappingTarget | Logical page number of the source page to be used for the address mapping in Defined Pages mode. |
| u32 | mcPropECU_TimingFactor | Sets the timing factor, which you can use to increase XCP or CCP command timeout values. For details on the default Command Timeout values, refer to the XCP or CCP Protocol Specification. |
| str | mcPropECU_TransportLayerInstance | Sets the transport layer instance. Empty string will select either a single unnamed transport layer instance in the IF_DATA XCPplus or XCP block. Use mcGetNames to identify valid values. Note that setting this property triggers a reinitialization. Most properties will be reverted to the default values read from the database. This property cannot be set while there is an active connection to the ECU. |
| u32 | mcPropECU_XCP_Timeout_T1 mcPropECU_XCP_Timeout_T2 mcPropECU_XCP_Timeout_T3 mcPropECU_XCP_Timeout_T4 mcPropECU_XCP_Timeout_T5 mcPropECU_XCP_Timeout_T6 mcPropECU_XCP_Timeout_T7 | Sets one of the seven timeout values (in milliseconds) defined in the XCP standard for the various XCP commands. For details of which timeout applies to a specific command, refer to the XCP standard. The values are typically read from an A2L file, but may be overridden manually. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_std | Sets the timeout value (in milliseconds) for most of the CCP commands. For details of which timeout applies to a specific command, refer to the CCP standard. Default: 40. Standard: 25. The default is chosen slightly higher to allow for slower ECUs. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_pgm | Sets the timeout value (in milliseconds) for the CCP programming commands. For details of which timeout applies to a specific command, refer to the CCP standard. Default: 120. Standard: 100. The default is chosen slightly higher to allow for slower ECUs. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_mem | Sets the timeout value (in milliseconds) for the CCP memory commands. For details of which timeout applies to a specific command, refer to the CCP standard. Default and Standard: 30000. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_diag | Sets the timeout value (in milliseconds) for the CCP DIAG_SERVICE command. Default and Standard: 500. Note that the mcPropECU_TimingFactor property might modify this value. |
| u32 | mcPropECU_CCP_Timeout_T_act | Sets the timeout value (in milliseconds) for the CCP ACTION_SERVICE command. Default: 500. Standard: 5000. Note that the mcPropECU_TimingFactor property might modify this value. |
| str | mcPropIPAddress | Sets the IP address for XCP on Ethernet (TCP or UDP) as a string. |
| u16 | mcPropIPPort | Sets the IP port for XCP on Ethernet (TCP or UDP). |
| str | mcPropIPSourceAddress | Sets the IP address of the host Ethernet interface for XCP on Ethernet (TCP or UDP). Use this property if your system has more than one Ethernet interface and you want to use a non-primary interface. Empty string (default) indicates using of the primary interface. |
| i32 | mcPropIPSourcePort | Sets the source port (XCP master port) used for Ethernet communication. The default value is -1, which indicates that the source port will be chosen by the operating system. Valid port values are 0 to 65535. Note that port 0 is reserved and typically should not be used. |
| str | mcPropIPXnetStackName | Sets the name of the XNET IP Stack for this session. The XNET IP stack must already exist. Refer to NI-XNET Hardware and Software Help for information about creating and configuring an XNET IP stack. If this parameter is empty string (default), the native operating system IP stack will be used. |
| str | mcPropIPXnetLocalInterface | Sets the name of the local interface used with the specified XNET IP Stack for this session; the XNET IP stack can contain multiple virtual interfaces. Refer to NI-XNET Hardware and Software Help for more information on this parameter. This property is ignored for the native operating system IP stack. |
| u32 | mcPropOptCmd_ACTION_SERVICE | Sets whether the ECU supports the optional CCP Command ACTION_SERVICE. |
| u32 | mcPropOptCmd_BUILD_CHKSUM | Sets whether the ECU supports the optional CCP Command BUILD_CHKSUM. |
| u32 | mcPropOptCmd_CLEAR_MEMORY | Sets whether the ECU supports the optional CCP Command CLEAR_MEMORY. |
| u32 | mcPropOptCmd_DIAG_SERVICE | Sets whether the ECU supports the optional CCP Command DIAG_SERVICE. |
| u32 | mcPropOptCmd_DNLOAD_6 | Sets whether the ECU supports the optional CCP Command DNLOAD_6. |
| u32 | mcPropOptCmd_GET_ACTIVE_CAL_PAGE | Sets whether the ECU supports the optional CCP Command GET_ACTIVE_CAL_PAGE. |
| u32 | mcPropOptCmd_GET_S_STATUS | Sets whether the ECU supports the optional CCP Command GET_S_STATUS. |
| u32 | mcPropOptCmd_GET_SEED | Sets whether the ECU supports the optional CCP Command GET_SEED. |
| u32 | mcPropOptCmd_MOVE | Sets whether the ECU supports the optional CCP Command MOVE. |
| u32 | mcPropOptCmd_PROGRAM | Sets whether the ECU supports the optional CCP Command PROGRAM. |
| u32 | mcPropOptCmd_PROGRAM_6 | Sets whether the ECU supports the optional CCP Command PROGRAM_6. |
| u32 | mcPropOptCmd_SELECT_CAL_PAGE | Sets whether the ECU supports the optional CCP Command SELECT_CAL_PAGE. |
| u32 | mcPropOptCmd_SET_S_STATUS | Sets whether the ECU supports the optional CCP Command SET_S_STATUS. |
| u32 | mcPropOptCmd_SHORT_UP | Sets whether the ECU supports the optional CCP Command SHORT_UP. |
| u32 | mcPropOptCmd_START_STOP_ALL | Sets whether the ECU supports the optional CCP Command START_STOP_ALL. |
| u32 | mcPropOptCmd_TEST | Sets whether the ECU supports the optional CCP Command TEST. |
| u32 | mcPropOptCmd_UNLOCK | Sets whether the ECU supports the optional CCP Command UNLOCK. |
| u8 | mcPropPGM_AccessMethod | Selects the selected access mode for mcProgram and mcClearMemory. 0x00—Absolute Access Mode (default). The MTA uses physical addresses. 0x00—Functional Access Mode. The MTA functions as a block sequence number of the new flash content file. 0x80...0xFF—User defined. It is possible to use different access modes for clearing and programming. |
| u8 | mcPropPGM_CompressionMethod | Selects the selected compression method used for mcProgram. 0—Data is uncompressed (default). 0x80...0xFF—User defined. |
| u8 | mcPropPGM_EncryptionMethod | Selects the selected encryption method used for mcProgram. 0—Data is not encrypted (default). 0x80...0xFF—User defined. |
| u8 | mcPropPGM_ProgrammingMethod | Selects the selected programming method used for mcProgram. 0—Sequential programming (default). 0x80...0xFF—User defined. |

#### DAQ-Specific Properties

| Data Type | Name | Description |
| --- | --- | --- |
| u32 | mcPropDAQ_DTO_ID | Sets the DTO ID, which is used by the ECU to respond to send data from the DAQ lists to the CCP master. If bit 31 (hex 0x80000000) of the value is set, the value is considered an extended CAN identifier (29-bit). |
| str | mcPropDAQ_EventChannelName | Sets the event channel name to which the Measurement task is assigned. If there is no event channel name defined in the A2L file, you can set the Event Channel Number manually by passing a decimal number as a string. |
| i32 | mcPropDAQ_Mode | Sets the mode of an M&C Measurement task. 0—DAQ List The data is transmitted from the ECU in equidistant time intervals as defined in the A2L database. The data can be read back with mcDAQRead as Single point data using sample rate = 0, or as waveform using a sample rate > 0. Input channel data is received from the DAQ messages. Use mcDAQRead to obtain input samples as single-point, array, or waveform. 1—Polling In this mode the data from the Measurement task is uploaded from the ECU whenever mcDAQRead is called. |
| u16 | mcPropDAQ_Prescaler | Sets the Prescaler, which reduces the desired transmission frequency of the associated DAQ list. |
| f64 | mcPropDAQ_SampleRate | Defines the sample rate in Hz for the M&C Measurement task. The sample rate is defined in mcDAQInitialize, mcDAQInitializeEx, mcDAQListInitialize, and mcDAQListInitializeEx functions or by mcSetProperty. |
| u32 | mcPropDAQ_TimingSource | Sets the timing source used for DAQ measurements. The default is Automatic. Values are: 0AutomaticThe default method (1, 2, or 3, below) is selected.1Host TimingTimestamps are generated from the host system time whenever a frame arrives.This mode is always available.This is the default for XCP on TCP/UDP if the ECU does not support timestamps.2CAN TimingTimestamps are generated from the network interface hardware (e.g. NI-XNET hardware).This mode is available only if the network hardware generates timestamps.This is the default for XCP on CAN if the ECU does not support timestamps.3ECU TimingTimestamps are taken from the ECU data. The Start Time is taken from the host, and increments are taken from the ECU.This mode is only available if the ECU generates timestamps; in this case, it is default. |
| 0 | AutomaticThe default method (1, 2, or 3, below) is selected. |  |
| 1 | Host TimingTimestamps are generated from the host system time whenever a frame arrives.This mode is always available.This is the default for XCP on TCP/UDP if the ECU does not support timestamps. |  |
| 2 | CAN TimingTimestamps are generated from the network interface hardware (e.g. NI-XNET hardware).This mode is available only if the network hardware generates timestamps.This is the default for XCP on CAN if the ECU does not support timestamps. |  |
| 3 | ECU TimingTimestamps are taken from the ECU data. The Start Time is taken from the host, and increments are taken from the ECU.This mode is only available if the ECU generates timestamps; in this case, it is default. |  |

#### Characteristic-Specific Properties

| Data Type | Name | Description |
| --- | --- | --- |
| double[] | mcPropChar_X_Axis | Sets the X-axis values on which the Characteristic is defined. The Characteristic dimension must be at least 1. |
| double[] | mcPropChar_Y_Axis | Sets the Y-axis values on which the Characteristic is defined. The Characteristic dimension must be 2. |
| u32 | mcPropChar_ByteOrder | Sets the specified byte order of the selected Characteristic: 0—Intel format Bytes are in little-endian order, with least-significant bit first. 1—Motorola format Bytes are in big-endian order, with most-significant bit first. |

#### Measurement-Specific Properties

| Data Type | Name | Description |
| --- | --- | --- |
| u32 | mcPropMeas_ByteOrder | Sets the specified byte order of the selected Measurement: 0—Intel format Bytes are in little-endian order, with least-significant bit first. 1—Motorola format Bytes are in big-endian order, with most-significant bit first. |

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcstatustostring.html language=enus -->
## TOPIC 00064: mcStatusToString

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcstatustostring.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcstatustostring.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts a status code into a descriptive string. Format mcTypeStatus mcStatusToString( mcTypeTaskRef Status, u32 SizeOfString, str ErrorString); Input Status Nonzero status code returned from an ECU M&C function. SizeOfString SizeofString buffer (in bytes). Output ErrorString ASCII string t

### mcStatusToString

Purpose

Converts a status code into a descriptive string.
Format

| mcTypeStatus | mcStatusToString( mcTypeTaskRef Status, u32 SizeOfString, str ErrorString); |
| --- | --- |
| mcTypeTaskRef | Status, |
| u32 | SizeOfString, |
| str | ErrorString); |

Input

Status

Nonzero status code returned from an ECU M&C function.

SizeOfString

SizeofString buffer (in bytes).
Output

ErrorString

ASCII string that describes Status.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

When the status code returned from an ECU M&C function is nonzero, an error or warning is indicated. This function is used to obtain a description of the error/warning for debugging purposes.

The return code is passed into the Status parameter. The SizeofString parameter indicates the number of bytes available in the string for the description. The description is truncated to size SizeofString if needed, but a size of 300 characters is large enough to hold any description. The text returned in ErrorString is null-terminated, so it can be used with ANSI C functions such as printf. For applications written in C or C++, each ECU M&C function returns a status code as a signed 32-bit integer. The following table summarizes the ECU M&C use of this status.

#### Status Code Use

| Status Code | Definition |
| --- | --- |
| Negative | Error—Function did not perform expected behavior. |
| Positive | Warning—Function performed as expected, but a condition arose that may require attention. |
| Zero | Success—Function completed successfully. |

The application code should check the status returned from every ECU M&C function. If an error is detected, you should close all ECU M&C handles and exit the application. If a warning is detected, you can display a message for debugging purposes or simply ignore the warning.

The following piece of code shows an example of handling ECU M&C status during application debugging.

status= ncDatabaseOpen ("TestDataBase.A2L", &MyDbHandle);

PrintStat (status, "mcOpenDatabase");

where the function PrintStat has been defined at the top of the program as:

void PrintStat(mcTypeStatus status, char *source)

{

char statusString[300];

if(status !=0)

{

mcStatusToString(status, sizeof(statusString), statusString);

printf("\n%s\nSource = %s\n", statusString, source);

if (status < 0)

{

mcDatabaseClose(MyDbHandle);

exit(1);

}

}

}

In some situations, you may want to check for specific errors in the code. For example, when [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mccharacteristicread](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mccharacteristicread) times out, you may want to continue communication, rather than exit the application. To check for specific errors, use the constants defined in niemc.h. These constants have the same names as described in this help file. For example, to check for a function timeout, use:

if (status == mcErrorTimeout)

...

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mctexttodouble.html language=enus -->
## TOPIC 00065: mcTextToDouble

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mctexttodouble.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mctexttodouble.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts a text string to a numerical value using an enumeration or range text scaling. Format mcTypeStatus mcTextToDouble( mcTypeTaskRef ECURefNum, u32 ObjectType, cstr ObjectName, cstr TextValue, double *Value); Input ECURefNum The task reference that links to the selected ECU. This refere

### mcTextToDouble

Purpose

Converts a text string to a numerical value using an enumeration or range text scaling.
Format

```text
        mcTypeStatus  mcTextToDouble(
                 mcTypeTaskRef ECURefNum,
                 u32 ObjectType,
                 cstr ObjectName,
                 cstr TextValue,
                 double *Value);
      
```

Input

ECURefNum

The task reference that links to the selected ECU.

This reference is originally returned from [mcECUSelectEx](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

ObjectType

Indicates the type of the object named in ObjectName. Valid values are:

1 Measurement Name

2 Characteristic Name

ObjectName

Indicates the object (measurement or characteristic) for which the enumeration or range text scaling is performed.

TextValue

The text that you want to turn into the numeric representation.
Output

Value

Returns the converted value.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

mcTextToDouble performs text to double conversion for measurement or characteristic values.

Especially if the measurement or characteristic has an associated enumeration or range text type scaling, the text input will be converted into the numeric representation, using the related COMPU_VTAB or COMPU_VTAB_RANGE table.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcupload.html language=enus -->
## TOPIC 00066: mcUpload

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcupload.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcupload.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Uploads data from an ECU. Format mcTypeStatus mcUpload( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *Data); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Address Configures the source address fo

### mcUpload

Purpose

Uploads data from an ECU.
Format

| mcTypeStatus | mcUpload( mcTypeTaskRef ECURefNum, mcAddress Address, u32 BlockSize, u8 *Data); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address, |
| u32 | BlockSize, |
| u8 | *Data); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Configures the source address for the upload operation in the ECU. mcAddress is a C struct consisting of:

**Address**

Specifies the address part of the source address.

**Extension**

Extension contains the extension part of the address.

BlockSize

BlockSize is the size of the data block in bytes to be uploaded.
Output

Data

Data is a byte array which receives the uploaded data information from the ECU.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

If you are using the CCP protocol, mcUpload implements the CCP command UPLOAD. A data block of the specified length starting at the specified address is uploaded from the ECU. This function sets the Memory Transfer Address pointer MTA0 to the appropriate value as defined in the **Address** struct.

If you are using the XCP protocol, mcUpload implements the XCP command UPLOAD. A data block of the specified length starting at the specified address is uploaded from the ECU. The Memory Transfer Address pointer MTA0 is post-incremented by the given number of data elements. If the slave device does not support block transfer mode, all uploaded data is transferred in a single response packet. If block transfer mode is supported, the uploaded data is transferred in multiple responses on the same request packet. There are no limitations allowed concerning the maximum block size for the master.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to upload data and to use the mcUpload command.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpcopycalpage.html language=enus -->
## TOPIC 00067: mcXCPCopyCalPage

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpcopycalpage.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpcopycalpage.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Forces a copy transaction of one calibration page to another. Format mcTypeStatus mcXCPCopyCalPage( mcTypeTaskRef ECURefNum, u8 SourceSegment, u8 SourcePage, u8 DestinationSegment, u8 DestinationPage); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This refe

### mcXCPCopyCalPage

Purpose

Forces a copy transaction of one calibration page to another.
Format

| mcTypeStatus | mcXCPCopyCalPage( mcTypeTaskRef ECURefNum, u8 SourceSegment, u8 SourcePage, u8 DestinationSegment, u8 DestinationPage); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | SourceSegment, |
| u8 | SourcePage, |
| u8 | DestinationSegment, |
| u8 | DestinationPage); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

SourceSegment

SourceSegment specifies the logical data segment number source.

SourcePage

SourcePage specifies the logical page number source.

DestinationSegment

DestinationSegment specifies the logical data segment number destination.

DestinationPage

DestinationPage specifies the logical page number destination.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpcopycalpage](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpcopycalpage) implements the XCP command COPY_CAL_PAGE and forces the slave to copy one calibration page to another. This command is only available if more than one calibration page is defined. In principal, any page of any segment can be copied to any page of any other segment but there may be restrictions.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpgetcalpage.html language=enus -->
## TOPIC 00068: mcXCPGetCalPage

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpgetcalpage.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpgetcalpage.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Queries a calibration page setting. Format mcTypeStatus mcXCPGetCalPage( mcTypeTaskRef ECURefNum, u8 Mode, u8 Segment, u8 *Page); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Mode Mode specifies the access mode:

### mcXCPGetCalPage

Purpose

Queries a calibration page setting.
Format

| mcTypeStatus | mcXCPGetCalPage( mcTypeTaskRef ECURefNum, u8 Mode, u8 Segment, u8 *Page); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Mode, |
| u8 | Segment, |
| u8 | *Page); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Mode

Mode specifies the access mode:

Mode = 1

The given page is used by the slave device application.

Mode = 2

The slave device XCP driver will access the given page.

Segment

Segment specifies the selected logical data segment number.
Output

*Page

Page returns the logical data page number.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpgetcalpage](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpgetcalpage) implements the XCP command GET_CAL_PAGE and queries the logical number for the calibration data page that is currently activated for the specified access mode and data segment.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpgetid.html language=enus -->
## TOPIC 00069: mcXCPGetId

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpgetid.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpgetid.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Queries session configuration or slave device identification. Format mcTypeStatus mcXCPGetId( mcTypeTaskRef ECURefNum, u8 Type, u32 *Length, char *Id); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Type Type spec

### mcXCPGetId

Purpose

Queries session configuration or slave device identification.
Format

| mcTypeStatus | mcXCPGetId( mcTypeTaskRef ECURefNum, u8 Type, u32 *Length, char *Id); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Type, |
| u32 | *Length, |
| char | *Id); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Type

Type specifies the type of the requested identification:

| Type | Description |
| --- | --- |
| 0 | ASCII text |
| 1 | ASAM-MC2 filename without path and extension |
| 2 | ASAM-MC2 filename with path and extension |
| 3 | URL where the ASAM-MC2 file can be found |
| 4 | ASAM-MC2 file to upload |
| 128..255 | User defined |

Output

Length

Length returns the string length of the Id string.

Id

Id contains the queried identification string.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpgetid](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpgetid) implements the XCP command GET_ID and returns session configuration or slave device identification information of the selected ECU slave device. The supported types are implementation specific of the ECU slave device. The identification string is ASCII text format.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpgetstatus.html language=enus -->
## TOPIC 00070: mcXCPGetStatus

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpgetstatus.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpgetstatus.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Queries the current session status from an ECU slave device. Format mcTypeStatus mcXCPGetStatus( mcTypeTaskRef ECURefNum, u8 *SessionStatus, u8 *ResourceMask, u16 *SessionId); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally return

### mcXCPGetStatus

Purpose

Queries the current session status from an ECU slave device.
Format

| mcTypeStatus | mcXCPGetStatus( mcTypeTaskRef ECURefNum, u8 *SessionStatus, u8 *ResourceMask, u16 *SessionId); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | *SessionStatus, |
| u8 | *ResourceMask, |
| u16 | *SessionId); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).
Output

SessionStatus

SessionStatus returns the current status of the selected ECU.

ResourceMask

ResourceMask is the current resource protection status of the selected ECU.

SessionId

SessionId returns the defined session configuration ID.

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpgetstatus](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpgetstatus) implements the XCP command GET_STATUS and returns all current status information of the selected ECU slave device, including the status of the resource protection, pending store requests and the general status of data acquisition and stimulation.

#### Current Session Status

SessionStatus contains a bit mask which is described below:

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

ResourceMask contains the current resource protection status as a bit mask described below:

| Bit Number | Flag | Description |
| --- | --- | --- |
| 0 | CAL/PAG | REQuest to STORE CALibration data: 0—STORE_CAL_REQ mode is reset. 1—STORE_CAL_REQ mode is set. |
| 1 | Unused | — |
| 2 | DAQ | DAQ list commands (DIRECTION = DAQ): 0—DAQ list commands are not protected with SEED & Key mechanism. 1—DAQ list commands are protected with SEED & Key mechanism. |
| 3 | STIM | DAQ list commands (DIRECTION = STIM): 0—DAQ list commands are not protected with SEED & Key mechanism. 1—DAQ list commands are protected with SEED & Key mechanism. |
| 4 | PGM | ProGraMming commands: 0—ProGraMming commands are not protected with SEED & Key mechanism. 1—ProGraMming commands are protected with SEED & Keyamp; mechanism |
| 5 | Unused | — |
| 6 | Unused | — |
| 7 | Unused | — |

The CAL/PAG flags indicates that all commands of the CALibration/PAGing group are protected and will return an ERR_ACCESS_LOCKED upon an attempt to execute the command without a previous successful GET_SEED/UNLOCK sequence.

The PGM flags indicates that all the commands of the ProGraMming group are protected and will return a ERR_ACCESS_LOCKED upon an attempt to execute the command without a previous successful GET_SEED/UNLOCK sequence.

The parameter SessionId contains the Session configuration ID. The session configuration ID must be set by a prior [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetrequest](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetrequest) call with STORE_DAQ_REQ set. This allows the master device to verify that automatically started DAQ lists contain the expected data transfer configuration.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpprogramprepare.html language=enus -->
## TOPIC 00071: mcXCPProgramPrepare

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpprogramprepare.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpprogramprepare.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Prepares the programming of non volatile memory. Format mcTypeStatus mcXCPProgramPrepare( mcTypeTaskRef ECURefNum, mcAddress Address, u16 CodeSize); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Address Address C

### mcXCPProgramPrepare

Purpose

Prepares the programming of non volatile memory.
Format

| mcTypeStatus | mcXCPProgramPrepare( mcTypeTaskRef ECURefNum, mcAddress Address, u16 CodeSize); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| mcAddress | Address, |
| u16 | CodeSize); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Address

Address Configures the target address to be cleared in the ECU. mcAddress is a C struct consisting of:

Address

Specifies the address part of the target address.

Extension

Contains the extension part of the target address.

CodeSize

CodeSize determines the size of data to be downloaded.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramprepare](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramprepare) may be used to indicate a data download as a pre-condition for non-volatile memory reprogramming. The Memory Transfer address (MTA) pointer is set to the volatile memory location specified by the parameters Address and Extension. The download itself is done by using subsequent standard commands like [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdownload](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcdownload). The slave device must ensure that the target memory area is available and it is in an operational state which permits the download of code. If not, an error will be returned.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramprepare](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramprepare) implements the optional XCP PROGRAM_PREPARE command defined by the XCP specification. For further information on how to program non-volatile ECU memory refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpprogramverify.html language=enus -->
## TOPIC 00072: mcXCPProgramVerify

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpprogramverify.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpprogramverify.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Performs a non-volatile memory certification task on the ECU device. Format mcTypeStatus mcXCPProgramVerify( mcTypeTaskRef ECURefNum, u8 Mode, u16 VerType, u32 VerValue); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned fr

### mcXCPProgramVerify

Purpose

Performs a non-volatile memory certification task on the ECU device.
Format

| mcTypeStatus | mcXCPProgramVerify( mcTypeTaskRef ECURefNum, u8 Mode, u16 VerType, u32 VerValue); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Mode, |
| u16 | VerType, |
| u32 | VerValue); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Mode

Mode specifies the verification mode and can be defined as:

00=request to start internal routine

01=transmit a Verification Value

VerType

VerType determines the verification type and is a bit mask described below:

0x0001—calibration area(s) of the flash

0x0002—code area(s) of the flash

0x0004—complete flash content

0x0008...0x0080—reserved

0x0100...0xFF00—user defined

VerValue

VerValue verification value is project specific.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramverify](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramverify) can be used to verify the success of non-volatile memory reprogramming.

With Mode set to 00 the master can request the slave to start internal test routines to check whether the new flash contents fits to the rest of the flash. Only the result is of interest. With Mode set to 01, the master can tell the slave that he will be sending a Verification value to the slave. The definition of the Verification mode is project-specific. The master receives the Verification Mode from the project-specific programming flow control and passes it to the slave.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramverify](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpprogramverify) implements the optional XCP PROGRAM_VERIFY command defined by the XCP specification. For further information on how to program non-volatile ECU memory refer to the ASAM XCP Part 2 Protocol Layer Specification.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpsetcalpage.html language=enus -->
## TOPIC 00073: mcXCPSetCalPage

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpsetcalpage.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpsetcalpage.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets a calibration page. Format mcTypeStatus mcXCPSetCalPage( mcTypeTaskRef ECURefNum, u8 Mode, u8 Segment, u8 Page); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Mode Mode is a bit mask described below: Bit Des

### mcXCPSetCalPage

Purpose

Sets a calibration page.
Format

| mcTypeStatus | mcXCPSetCalPage( mcTypeTaskRef ECURefNum, u8 Mode, u8 Segment, u8 Page); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Mode, |
| u8 | Segment, |
| u8 | Page); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Mode

Mode is a bit mask described below:

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

Segment

Segment specifies the selected logical data segment number.

Page

Page specifies the logical data page number.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetcalpage](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetcalpage) implements the XCP command SET_CAL_PAGE and sets the access mode for a calibration data segment, if the slave device supports calibration data page switching. A calibration data segment and its pages are specified by logical numbers.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpsetrequest.html language=enus -->
## TOPIC 00074: mcXCPSetRequest

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpsetrequest.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpsetrequest.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Performs a request to save session and device information to non-volatile memory. Format mcTypeStatus mcXCPSetRequest( mcTypeTaskRef ECURefNum, u8 Mode, u16 SessionID); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from

### mcXCPSetRequest

Purpose

Performs a request to save session and device information to non-volatile memory.
Format

| mcTypeStatus | mcXCPSetRequest( mcTypeTaskRef ECURefNum, u8 Mode, u16 SessionID); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Mode, |
| u16 | SessionID); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Mode

Mode is a bit mask described below:

| Bit | Description |
| --- | --- |
| 0 | Request to store calibration data in non-volatile memory. |
| 1 | Unused. |
| 2 | Request to save all DAQ lists, which have been selected with START_STOP_DAQ_LIST(Select) into non-volatile memory. The slave also must store the session configuration ID in non-volatile memory. Upon saving, the slave first must clear any DAQ list configuration that might already be stored in non-volatile memory. |
| 3 | Request to clear all DAQ lists in non-volatile memory. All ODT entries reset to address=0, extension=0, size=0 and bit_offset=FF. Session configuration ID reset to 0. |
| 4 | Unused. |
| 5 | Unused. |
| 6 | Unused. |
| 7 | Unused. |

SessionID

SessionID is a session configuration ID that is stored in non-volatile memory together with the information requested by the Mode parameter.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetrequest](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetrequest) implements the XCP command SET_REQUEST and is used to save session configuration information into non-volatile memory in the ECU.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to setup a request.

Parent topic:

ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit-c-api-ref path=mcxcpsetsegmentmode.html language=enus -->
## TOPIC 00075: mcXCPSetSegmentMode

- bundle_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- source_path: `mcxcpsetsegmentmode.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit-c-api-ref/raw/resource/enus/mcxcpsetsegmentmode.html
- document_id: `ecu-measurement-calibration-toolkit-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets the mode of a specified segment. Format mcTypeStatus mcXCPSetSegmentMode( mcTypeTaskRef ECURefNum, u8 Segment, u8 Mode); Input ECURefNum ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from . Segment Segment specifies the logical da

### mcXCPSetSegmentMode

Purpose

Sets the mode of a specified segment.
Format

| mcTypeStatus | mcXCPSetSegmentMode( mcTypeTaskRef ECURefNum, u8 Segment, u8 Mode); |
| --- | --- |
| mcTypeTaskRef | ECURefNum, |
| u8 | Segment, |
| u8 | Mode); |

Input

ECURefNum

ECURefNum is the task reference which links to the selected ECU. This reference is originally returned from [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcecuselectex).

Segment

Segment specifies the logical data segment number.

Mode

Mode specifies the mode for the segment.
Output

#### Return Value

The return value indicates the status of the function call as a signed 32-bit integer. Zero means the function executed successfully. A negative value specifies an error, which means the function did not perform the expected behavior. A positive value specifies a warning, which means the function performed as expected, but a condition arose that may require attention.

Use the [/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcstatustostring) function of the ECU M&C API to obtain a descriptive string for the return value.

[/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetsegmentmode](/csh?context=ecu-measurement-calibration-toolkit_niecumchelp_mcxcpsetsegmentmode) implements the XCP command SET_SEGMENT_MODE and sets the selected segment into the specified mode. If Mode=0 the segment disables the FREEZE mode, if Mode=1 the segment is set to FREEZE mode through an XCP STORE_CAL_REQ operation.

Refer to the ASAM XCP Part 2 Protocol Layer Specification for more information on how to set up a request.

Parent topic:

ECU M&C API for C
