# NI DOCUMENT BUNDLE: automotive-diagnostic-command-set-toolkit-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref start=1 end=122 -->
<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=adcs_intro.html language=enus -->
## TOPIC 00001: Automotive Diagnostic Command Set Toolkit Programming Reference Manual

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `adcs_intro.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/adcs_intro.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Automotive Diagnostic Command Set Toolkit Programming Reference Manual provides information about the Automotive Diagnostic Command Set Toolkit VIs and error codes. For information not found in the User Manual, like installation, configuration, and programming, browse Related Topics. Related Top

### Automotive Diagnostic Command Set Toolkit Programming Reference Manual

The Automotive Diagnostic Command Set Toolkit Programming Reference Manual provides information about the Automotive Diagnostic Command Set Toolkit VIs and error codes.

#### Related Topics:

For information not found in the User Manual, like installation, configuration, and programming, browse Related Topics.

- Hardware and Software Requirements
- Installation

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=application-development.html language=enus -->
## TOPIC 00002: Application Development

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `application-development.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/application-development.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following topics explain how to develop an application using the Automotive Diagnostic Command Set API. Choosing the Programming Language LabVIEW LabWindows™/CVI™ (Windows only) Visual C++ 6 (Windows only) Other Programming Languages on Windows Other Programming Languages on Linux Application De

### Application Development

The following topics explain how to develop an application using the Automotive Diagnostic Command Set API.

[Choosing the Programming Language](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_choosingtheprogramminglanguage)

[LabVIEW](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_labview)

[LabWindows™/CVI™ (Windows only)](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_labwindowscvi)

[Visual C++ 6 (Windows only)](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_visualc6)

[Other Programming Languages on Windows](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_otherprogramminglanguages)

[Other Programming Languages on Linux](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_otherprogramminglanguagesonlinux)

[Application Development on CompactRIO or R Series Using an NI 985](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_applicationdevelopmentoncompactrioorrseries)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=automotive-diagnostic-command-set-api-for-lab.html language=enus -->
## TOPIC 00003: Automotive Diagnostic Command Set API for LabVIEW

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `automotive-diagnostic-command-set-api-for-lab.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/automotive-diagnostic-command-set-api-for-lab.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Automotive Diagnostic Command Set API for LabVIEW topics describe the format, purpose, and parameters of the Automotive Diagnostic Command Set LabVIEW VIs. The VIs are listed alphabetically in four categories: general functions, KWP2000 services, UDS (DiagOnCAN) services, and OBD (On-Board Diagn

### Automotive Diagnostic Command Set API for LabVIEW

The Automotive Diagnostic Command Set API for LabVIEW topics describe the format, purpose, and parameters of the Automotive Diagnostic Command Set LabVIEW VIs. The VIs are listed alphabetically in four categories: general functions, KWP2000 services, UDS (DiagOnCAN) services, and OBD (On-Board Diagnostics) services.

[Section Headings](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_lvsectionheadings)

[List of VIs](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_listofvis)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=cleardiagnosticinformation-vi.html language=enus -->
## TOPIC 00004: ClearDiagnosticInformation.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `cleardiagnosticinformation-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/cleardiagnosticinformation-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ClearDiagnosticInformation service and clears selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byt

### ClearDiagnosticInformation.vi

Purpose

Executes the ClearDiagnosticInformation service and clears selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/ClearDiagnosticInformationVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The DTC descriptor is given here as a parameter basically to convert the group of DTC parameter to a binary representation according to DTC Byte Length and Byte Order. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | group of DTC specifies the group of Diagnostic Trouble Codes to be cleared. The following values have a special meaning, and you can specify them through a ring control: 0x0000All powertrain DTCs0x4000All chassis DTCs0x8000All body DTCs0xC000All network-related DTCs0xFF00All DTCs |
| 0x0000 | All powertrain DTCs |
| 0x4000 | All chassis DTCs |
| 0x8000 | All body DTCs |
| 0xC000 | All network-related DTCs |
| 0xFF00 | All DTCs |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI clears the diagnostic information on the ECU memory. If the **group of DTC** parameter is present, the ECU is requested to clear all memory including the DTCs.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=close-diagnostic-vi.html language=enus -->
## TOPIC 00005: Close Diagnostic.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `close-diagnostic-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/close-diagnostic-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Closes a diagnostic session. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. error in is a cluster that

### Close Diagnostic.vi

Purpose

Closes a diagnostic session.
Format

[IMAGE alt='image' src='images/CloseDiagnosticVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
| --- | --- |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The diagnostic session specified by **diag ref in** is closed, and you can no longer use it for communication to an ECU. Note that this command does not communicate the closing to the ECU before terminating; if this is necessary, you must manually do so (for example, by calling [StopDiagnosticSession.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_stopdiagnosticsessionvi)) before calling **Close Diagnostic.vi**.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=connect-disconnect.html language=enus -->
## TOPIC 00006: Connect/Disconnect

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `connect-disconnect.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/connect-disconnect.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: KWP2000 expects a diagnostic session to be started with StartDiagnosticSession and terminated with StopDiagnosticSession. However, StartDiagnosticSession has a DiagnosticMode parameter that determines the diagnostic session type. Depending on this type, the ECU may or may not support other diagnosti

### Connect/Disconnect

KWP2000 expects a diagnostic session to be started with StartDiagnosticSession and terminated with StopDiagnosticSession. However, StartDiagnosticSession has a DiagnosticMode parameter that determines the diagnostic session type. Depending on this type, the ECU may or may not support other diagnostic services, or operate in a restricted mode where not all ECU functions are available. The DiagnosticMode parameter values are manufacturer specific and not defined in the standard.

For a diagnostic session to remain active, it must execute the TesterPresent service periodically if no other service is executed. If the TesterPresent service is missing for a certain period of time, the diagnostic session is terminated, and the ECU returns to normal operation mode.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=controldtcsetting-vi.html language=enus -->
## TOPIC 00007: ControlDTCSetting.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `controldtcsetting-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/controldtcsetting-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ControlDTCSetting service and modifies the generation behavior of selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The def

### ControlDTCSetting.vi

Purpose

Executes the ControlDTCSetting service and modifies the generation behavior of selected
Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/ControlDTCSettingVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The DTC descriptor is given here as a parameter basically to convert the group of DTC parameter to a binary representation according to DTC Byte Length and Byte Order. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | data in specifies application-specific data that control DTC generation. |
|  | group of DTC specifies the group of Diagnostic Trouble Codes to be cleared. The following values have a special meaning, and you can specify them through a ring control: 0x0000All powertrain DTCs0x4000All chassis DTCs0x8000All body DTCs0xC000All network-related DTCs0xFF00All DTCs |
| 0x0000 | All powertrain DTCs |
| 0x4000 | All chassis DTCs |
| 0x8000 | All body DTCs |
| 0xC000 | All network-related DTCs |
| 0xFF00 | All DTCs |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=convert-from-phys-vi.html language=enus -->
## TOPIC 00008: Convert from Phys.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `convert-from-phys-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/convert-from-phys-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts a physical data value into a binary representation using a type descriptor. Format Input type descriptor is a cluster that specifies the conversion of the physical value to its binary representation: Start Byte gives the start byte of the binary representation. For Convert from Phys

### Convert from Phys.vi

Purpose

Converts a physical data value into a binary representation using a type descriptor.
Format

[IMAGE alt='image' src='images/ConvertfromPhysVI.gif']
Input

|  | type descriptor is a cluster that specifies the conversion of the physical value to its binary representation: Start Byte gives the start byte of the binary representation. For Convert from Phys.vi, this value is ignored and always assumed to be 0.Byte Length is the binary representation byte length.Byte Order is the byte ordering of the data in the binary representation:0: MSB_FIRST (Motorola)1: LSB_FIRST (Intel)Data Type is the binary representation format:0: Unsigned. Only byte lengths of 1–4 are allowed.1: Signed. Only byte lengths of 1–4 are allowed.2: Float. Only byte lengths of 4 or 8 are allowed.Scale Factor defines the physical value scaling:Phys = (Scale Factor) * (binary representation) + (Scale Offset)Scale Offset (refer to Scale Factor) |
| --- | --- |
|  | Start Byte gives the start byte of the binary representation. For Convert from Phys.vi, this value is ignored and always assumed to be 0. |
|  | Byte Length is the binary representation byte length. |
|  | Byte Order is the byte ordering of the data in the binary representation: |
|  | 0: MSB_FIRST (Motorola) |
|  | 1: LSB_FIRST (Intel) |
|  | Data Type is the binary representation format: |
|  | 0: Unsigned. Only byte lengths of 1–4 are allowed. |
|  | 1: Signed. Only byte lengths of 1–4 are allowed. |
|  | 2: Float. Only byte lengths of 4 or 8 are allowed. |
|  | Scale Factor defines the physical value scaling: |
|  | Phys = (Scale Factor) * (binary representation) + (Scale Offset) |
|  | Scale Offset (refer to Scale Factor) |
|  | value is the physical value to be converted. |

Output

|  | data out is the binary representation of the physical value. If you build a record of multiple values, you can concatenate the outputs of several instances of Convert from Phys.vi. |
| --- | --- |

Description

Data input to diagnostic services (for example, [WriteDataByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_writedatabylocalidentifiervi)) is usually a byte stream of binary data. If you have a description of the data input (for example, byte 3 and 4 are engine RPM scaled as .25 * x RPM in Motorola representation), you can use **Convert from Phys.vi** to convert the physical value to the byte stream by filling an appropriate type descriptor cluster.

**Convert from Phys.vi** converts only the portion specified by one type descriptor to a binary representation. If your data input consists of several values, you can use **Convert from Phys.vi** multiple times and concatenate their outputs.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=convert-to-phys-vi.html language=enus -->
## TOPIC 00009: Convert to Phys.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `convert-to-phys-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/convert-to-phys-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts a binary representation of a value into its physical value using a type descriptor. Format Input type descriptor is a cluster that specifies the conversion of the physical value to its binary representation: Start Byte gives the start byte of the binary representation.Byte Length is

### Convert to Phys.vi

Purpose

Converts a binary representation of a value into its physical value using a type descriptor.
Format

[IMAGE alt='image' src='images/ConverttoPhysVI.gif']
Input

|  | type descriptor is a cluster that specifies the conversion of the physical value to its binary representation: Start Byte gives the start byte of the binary representation.Byte Length is the binary representation byte length.Byte Order is the byte ordering of the data in the binary representation:0: MSB_FIRST (Motorola)1: LSB_FIRST (Intel)Data Type is the binary representation format:0: Unsigned. Only byte lengths of 1–4 are allowed.1: Signed. Only byte lengths of 1–4 are allowed.2: Float. Only byte lengths of 4 or 8 are allowed.Scale Factor defines the physical value scaling:Phys = (Scale Factor) * (binary representation) + (Scale Offset)Scale Offset (refer to Scale Factor) |
| --- | --- |
|  | Start Byte gives the start byte of the binary representation. |
|  | Byte Length is the binary representation byte length. |
|  | Byte Order is the byte ordering of the data in the binary representation: |
|  | 0: MSB_FIRST (Motorola) |
|  | 1: LSB_FIRST (Intel) |
|  | Data Type is the binary representation format: |
|  | 0: Unsigned. Only byte lengths of 1–4 are allowed. |
|  | 1: Signed. Only byte lengths of 1–4 are allowed. |
|  | 2: Float. Only byte lengths of 4 or 8 are allowed. |
|  | Scale Factor defines the physical value scaling: |
|  | Phys = (Scale Factor) * (binary representation) + (Scale Offset) |
|  | Scale Offset (refer to Scale Factor) |
|  | data in is the data record from which physical values are to be extracted. |

Output

|  | value is the physical value extracted from the record. |
| --- | --- |

Description

Data output from diagnostic services (for example, [ReadDataByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_readdatabylocalidentifiervi)) is usually a byte stream of binary data. If you have a description of the data output (for example, byte 3 and 4 are engine RPM scaled as .25 * x RPM in Motorola representation), you can use **Convert to Phys.vi** to extract the physical value from the byte stream by filling an appropriate type descriptor cluster.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=create-extended-can-ids-vi.html language=enus -->
## TOPIC 00010: Create Extended CAN IDs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `create-extended-can-ids-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/create-extended-can-ids-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates diagnostic CAN IDs according to ISO 15765-2. Format Input addressing mode specifies whether the ECU is physically or functionally addressed. transport protocol specifies whether normal or mixed mode addressing is used. source address is the logical address of the host (diagnostic tes

### Create Extended CAN IDs.vi

Purpose

Creates diagnostic CAN IDs according to ISO 15765-2.
Format

[IMAGE alt='image' src='images/CreateExtendedCANIDsVI.gif']
Input

|  | addressing mode specifies whether the ECU is physically or functionally addressed. |
| --- | --- |
|  | transport protocol specifies whether normal or mixed mode addressing is used. |
|  | source address is the logical address of the host (diagnostic tester). |
|  | target address is the ECU logical address. |

Output

|  | transmit ID is the generated CAN identifier for sending diagnostic request messages from the host to the ECU. |
| --- | --- |
|  | receive ID is the generated CAN identifier for sending diagnostic response messages from the ECU to the host. |

Description

ISO 15765-2 specifies a method (extended/29 bit) of creating CAN identifiers for diagnostic applications given the addressing mode (physical/functional), the transport protocol (normal/mixed), and the 8-bit source and target addresses. This VI implements the construction of these CAN identifiers. You can use them directly in [Open Diagnostic on CAN FD.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_opendiagnosticoncanfdvi).

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diag-get-property-vi.html language=enus -->
## TOPIC 00011: Diag Get Property.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diag-get-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diag-get-property-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Gets a diagnostic global internal parameter. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. property I

### Diag Get Property.vi

Purpose

Gets a diagnostic global internal parameter.
Format

[IMAGE alt='image' src='images/DiagGetPropertyVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | property ID defines the parameter whose value is to be retrieved. You can create the values using an Enum control. 0Timeout Diag Command is the timeout in milliseconds the master waits for the response to or DoIP acknowledgement of a diagnostic request message. The default is 1000Â ms. This is the P2 timeout from the ISO 15765-3 specification.1Timeout FC (Bs) is the timeout in milliseconds the master waits for a Flow Control frame after sending a First Frame or the last Consecutive Frame of a block. The default is 250Â ms.2Timeout CF (Cr) is the timeout in milliseconds the master waits for a Consecutive Frame in a multiframe response. The default is 250Â ms for CAN and 1000 ms for LIN.3Receive Block Size (BS) is the number of Consecutive Frames the slave sends in one block before waiting for the next Flow Control frame. A value of 0 (default) means all Consecutive Frames are sent in one run without interruption.4Wait Time CF (STmin) defines the minimum time for the slave to wait between sending two Consecutive Frames of a block. Values from 0 to 127 are wait times in milliseconds. Values 241 to 249 (Hex F1 to F9) mean wait times of 100 Âµs to 900 Âµs, respectively. All other values are reserved. The default is 5Â ms for CAN.5Max Wait Frames (N_WFTmax) is the maximum number of WAIT frames the master accepts before terminating the connection. The default is 10.6Wait Frames to Send (N_WAIT) is the number of WAIT frames the master sends every time before a CTS frame is sent. If this value is set to a negative number (for example, 0xFFFFFFFF = –1), the master sends an OVERLOAD frame instead of a WAIT, and reception is aborted. The default is 0 for maximum speed.7Time between Waits (T_W) is the number of milliseconds the master waits after sending a WAIT frame. The default is 25.8Fill CAN Frames returns whether ISO-TP CAN frames are padded. 0:Sends CAN frames with the minimum valid length, padded with Fill Byte if necessary. This setting allows for maximum performance of the CAN bus.1:CAN frames shorter than 8Â bytes are padded with Fill Byte to 8Â bytes. Longer CAN frames are padded with Fill Byte to the minimum valid length (default).2:All CAN frames are padded with Fill Byte to the length set as the Max DLC input of Open Diagnostic on CAN FD.vi or OBD Open on CAN FD.vi. 9Fill Byte returns the CAN frame content if filled with defined data or random data bytes. 0–255:Byte is used optionally to fill short CAN frames.256:CAN frames are filled optionally with random bytes. The default is 255 (0xFF).10Invalid Response as Error returns how the toolkit handles an invalid ECU response. 0:Invalid response is indicated by success? = FALSE only (default).1:Invalid response is returned as an error in addition.11Max RspPending Count is the number of times a ReqCorrectlyRcvd-RspPending (0x78) Negative Response Message will be accepted to extend the command timeout (default 5). If this message is sent more often in response to a request, an error –8120 is returned. If the ECU implements commands with a long duration (for example, flash commands), you may need to extend this number.12VWTP Command Time Out is the time in milliseconds the host waits for a VWTP 2.0 command to be executed (default 50 ms). The specification states this as 50 ms plus the network latency, but some ECUs may require higher values.13STmin is the minimum time in seconds between the end of transmission of a frame in a diagnostic request message and the start of transmission of the next frame in the diagnostic request message for LIN-based diagnostic communication. The default is 0.14P2min is the minimum time in seconds between reception of the last frame of the diagnostic request and the response sent by the node for LIN-based diagnostic communication. The default is 0.05.15Termination reads the NI-XNET Termination property. Reflections on the CAN and LIN bus can cause communication failures. To prevent reflections, termination can be present as external resistance or resistance the XNET CAN or LIN board applies internally. This property determines whether the XNET board uses termination to the bus. For further information about appropriate terminations of a CAN or LIN network, refer to the NI-XNET Hardware and Software Manual. The default is 0.16Timeout RspPending is the timeout in milliseconds the master waits for the response to a diagnostic request message after receiving an RspPending Negative Response Message (0x78). The default is 1000Â ms. This is the P2* timeout from the ISO 15765-3 specification.17LIN Sleep is available for LIN only and controls the sleep state of the LIN bus. Allowed values are: 0:Remote Sleep. The complete LIN bus is sent to the Sleep state.1:Remote Wakeup. The LIN bus is woken up.18Actual CAN IO Mode returns the CAN IO Mode used for communication to the ECU. This is typically the same as the IO Mode parameter of Open Diagnostic on CAN FD.vi. However, if ECU Determined is chosen, then Actual CAN IO Mode returns the mode actually used.19Response Plausibility Check defines whether the first byte of the diagnostic response is checked to contain the + 0x40 offset (positive response) or whether the first byte is 0x7F (negative response). 0:Response Plausibility Check is disabled.1:Response Plausibility Check is enabled (default). The default is 1, which is compatible with previous versions of the Automotive Diagnostic Command Set. Set this property to 0 only if you use non-standard diagnostic services.20Session-based properties specifies whether the following ISO TP (15765-2) and DoIP properties are shared globally or apply only to the specific diagnostic session: Timeout Diag CommandTimeout FC (Bs)Timeout CF (Cr)Receive Block Size (BS)Wait Time CD (STmin)Max Wait Frames (N_WFTmax)Wait Frames to Send (N_WAIT)Time between Waits (T_W)Fill CAN FramesFill ByteInvalid Response as ErrorMax RespPending CountVWTP Command Time OutTimeout RspPending 0:These properties are shared between sessions that are in the same application instance (default).1:These properties apply only to the specific session. To prevent influencing other sessions, set this property immediately after opening the diagnostic session. 21DoIP Acknowledge Mode returns the DoIP Diagnostic Message Acknowledgement behavior. 0:ADCS acknowledges diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages (default).1:ADCS does not acknowledge diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages.2:ADCS acknowledges diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command.3:ADCS does not acknowledge diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
| 0 | Timeout Diag Command is the timeout in milliseconds the master waits for the response to or DoIP acknowledgement of a diagnostic request message. The default is 1000Â ms. This is the P2 timeout from the ISO 15765-3 specification. |
| 1 | Timeout FC (Bs) is the timeout in milliseconds the master waits for a Flow Control frame after sending a First Frame or the last Consecutive Frame of a block. The default is 250Â ms. |
| 2 | Timeout CF (Cr) is the timeout in milliseconds the master waits for a Consecutive Frame in a multiframe response. The default is 250Â ms for CAN and 1000 ms for LIN. |
| 3 | Receive Block Size (BS) is the number of Consecutive Frames the slave sends in one block before waiting for the next Flow Control frame. A value of 0 (default) means all Consecutive Frames are sent in one run without interruption. |
| 4 | Wait Time CF (STmin) defines the minimum time for the slave to wait between sending two Consecutive Frames of a block. Values from 0 to 127 are wait times in milliseconds. Values 241 to 249 (Hex F1 to F9) mean wait times of 100 Âµs to 900 Âµs, respectively. All other values are reserved. The default is 5Â ms for CAN. |
| 5 | Max Wait Frames (N_WFTmax) is the maximum number of WAIT frames the master accepts before terminating the connection. The default is 10. |
| 6 | Wait Frames to Send (N_WAIT) is the number of WAIT frames the master sends every time before a CTS frame is sent. If this value is set to a negative number (for example, 0xFFFFFFFF = –1), the master sends an OVERLOAD frame instead of a WAIT, and reception is aborted. The default is 0 for maximum speed. |
| 7 | Time between Waits (T_W) is the number of milliseconds the master waits after sending a WAIT frame. The default is 25. |
| 8 | Fill CAN Frames returns whether ISO-TP CAN frames are padded. 0:Sends CAN frames with the minimum valid length, padded with Fill Byte if necessary. This setting allows for maximum performance of the CAN bus.1:CAN frames shorter than 8Â bytes are padded with Fill Byte to 8Â bytes. Longer CAN frames are padded with Fill Byte to the minimum valid length (default).2:All CAN frames are padded with Fill Byte to the length set as the Max DLC input of Open Diagnostic on CAN FD.vi or OBD Open on CAN FD.vi. |
| 0: | Sends CAN frames with the minimum valid length, padded with Fill Byte if necessary. This setting allows for maximum performance of the CAN bus. |
| 1: | CAN frames shorter than 8Â bytes are padded with Fill Byte to 8Â bytes. Longer CAN frames are padded with Fill Byte to the minimum valid length (default). |
| 2: | All CAN frames are padded with Fill Byte to the length set as the Max DLC input of Open Diagnostic on CAN FD.vi or OBD Open on CAN FD.vi. |
| 9 | Fill Byte returns the CAN frame content if filled with defined data or random data bytes. 0–255:Byte is used optionally to fill short CAN frames.256:CAN frames are filled optionally with random bytes. The default is 255 (0xFF). |
| 0–255: | Byte is used optionally to fill short CAN frames. |
| 256: | CAN frames are filled optionally with random bytes. |
| 10 | Invalid Response as Error returns how the toolkit handles an invalid ECU response. 0:Invalid response is indicated by success? = FALSE only (default).1:Invalid response is returned as an error in addition. |
| 0: | Invalid response is indicated by success? = FALSE only (default). |
| 1: | Invalid response is returned as an error in addition. |
| 11 | Max RspPending Count is the number of times a ReqCorrectlyRcvd-RspPending (0x78) Negative Response Message will be accepted to extend the command timeout (default 5). If this message is sent more often in response to a request, an error –8120 is returned. If the ECU implements commands with a long duration (for example, flash commands), you may need to extend this number. |
| 12 | VWTP Command Time Out is the time in milliseconds the host waits for a VWTP 2.0 command to be executed (default 50 ms). The specification states this as 50 ms plus the network latency, but some ECUs may require higher values. |
| 13 | STmin is the minimum time in seconds between the end of transmission of a frame in a diagnostic request message and the start of transmission of the next frame in the diagnostic request message for LIN-based diagnostic communication. The default is 0. |
| 14 | P2min is the minimum time in seconds between reception of the last frame of the diagnostic request and the response sent by the node for LIN-based diagnostic communication. The default is 0.05. |
| 15 | Termination reads the NI-XNET Termination property. Reflections on the CAN and LIN bus can cause communication failures. To prevent reflections, termination can be present as external resistance or resistance the XNET CAN or LIN board applies internally. This property determines whether the XNET board uses termination to the bus. For further information about appropriate terminations of a CAN or LIN network, refer to the NI-XNET Hardware and Software Manual. The default is 0. |
| 16 | Timeout RspPending is the timeout in milliseconds the master waits for the response to a diagnostic request message after receiving an RspPending Negative Response Message (0x78). The default is 1000Â ms. This is the P2* timeout from the ISO 15765-3 specification. |
| 17 | LIN Sleep is available for LIN only and controls the sleep state of the LIN bus. Allowed values are: 0:Remote Sleep. The complete LIN bus is sent to the Sleep state.1:Remote Wakeup. The LIN bus is woken up. |
| 0: | Remote Sleep. The complete LIN bus is sent to the Sleep state. |
| 1: | Remote Wakeup. The LIN bus is woken up. |
| 18 | Actual CAN IO Mode returns the CAN IO Mode used for communication to the ECU. This is typically the same as the IO Mode parameter of Open Diagnostic on CAN FD.vi. However, if ECU Determined is chosen, then Actual CAN IO Mode returns the mode actually used. |
| 19 | Response Plausibility Check defines whether the first byte of the diagnostic response is checked to contain the + 0x40 offset (positive response) or whether the first byte is 0x7F (negative response). 0:Response Plausibility Check is disabled.1:Response Plausibility Check is enabled (default). The default is 1, which is compatible with previous versions of the Automotive Diagnostic Command Set. Set this property to 0 only if you use non-standard diagnostic services. |
| 0: | Response Plausibility Check is disabled. |
| 1: | Response Plausibility Check is enabled (default). |
| 20 | Session-based properties specifies whether the following ISO TP (15765-2) and DoIP properties are shared globally or apply only to the specific diagnostic session: Timeout Diag CommandTimeout FC (Bs)Timeout CF (Cr)Receive Block Size (BS)Wait Time CD (STmin)Max Wait Frames (N_WFTmax)Wait Frames to Send (N_WAIT)Time between Waits (T_W)Fill CAN FramesFill ByteInvalid Response as ErrorMax RespPending CountVWTP Command Time OutTimeout RspPending 0:These properties are shared between sessions that are in the same application instance (default).1:These properties apply only to the specific session. To prevent influencing other sessions, set this property immediately after opening the diagnostic session. |
| 0: | These properties are shared between sessions that are in the same application instance (default). |
| 1: | These properties apply only to the specific session. To prevent influencing other sessions, set this property immediately after opening the diagnostic session. |
| 21 | DoIP Acknowledge Mode returns the DoIP Diagnostic Message Acknowledgement behavior. 0:ADCS acknowledges diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages (default).1:ADCS does not acknowledge diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages.2:ADCS acknowledges diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command.3:ADCS does not acknowledge diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
| 0: | ADCS acknowledges diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages (default). |
| 1: | ADCS does not acknowledge diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages. |
| 2: | ADCS acknowledges diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
| 3: | ADCS does not acknowledge diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. It is copied unchanged to error out and has no other effect on the VI. It is provided for sequencing purposes only. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | property value is the requested property value. |
|  | error out describes error conditions. It is copied unchanged from the error in cluster. It is provided for sequencing purposes only. |

Description

Use this VI to request several internal diagnostic parameters, such as timeouts for the transport protocol. Use [Diag Set Property.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diagsetpropertyvi) to modify them.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diag-set-property-vi.html language=enus -->
## TOPIC 00012: Diag Set Property.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diag-set-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diag-set-property-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sets a diagnostic global internal parameter. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. property I

### Diag Set Property.vi

Purpose

Sets a diagnostic global internal parameter.
Format

[IMAGE alt='image' src='images/DiagSetPropertyVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | property ID defines the parameter whose value is to be retrieved. You can create the values using an Enum control. 0Timeout Diag Command is the timeout in milliseconds the master waits for the response to or DoIP acknowledgement of a diagnostic request message. The default is 1000Â ms. This is the P2 timeout from the ISO 15765-3 specification.1Timeout FC (Bs) is the timeout in milliseconds the master waits for a Flow Control frame after sending a First Frame or the last Consecutive Frame of a block. The default is 250 ms.2Timeout CF (Cr) is the timeout in milliseconds the master waits for a Consecutive Frame in a multiframe response. The default is 250 ms for CAN and 1000 ms for LIN.3Receive Block Size (BS) is the number of Consecutive Frames the slave sends in one block before waiting for the next Flow Control frame. A value of 0 (default) means all Consecutive Frames are sent in one run without interruption.4Wait Time CF (STmin) defines the minimum time for the slave to wait between sending two Consecutive Frames of a block. Values from 0 to 127 are wait times in milliseconds. Values 241 to 249 (Hex F1 to F9) mean wait times of 100 Âµs to 900 Âµs, respectively. All other values are reserved. The default is 5 ms.5Max Wait Frames (N_WFTmax) is the maximum number of WAIT frames the master accepts before terminating the connection. The default is 10.6Wait Frames to Send (N_WAIT) is the number of WAIT frames the master sends every time before a CTS frame is sent. If this value is set to a negative number (for example, 0xFFFFFFFF = –1), the master sends an OVERLOAD frame instead of a WAIT, and reception is aborted. The default is 0 for maximum speed.7Time between Waits (T_W) is the number of milliseconds the master waits after sending a WAIT frame. The default is 25.8Fill CAN Frames specifies how ISO-TP CAN frames are padded. 0:Sends CAN frames with the minimum valid length, padded with Fill Byte if necessary. This setting allows for maximum performance of the CAN bus.1:CAN frames shorter than 8Â bytes are padded with Fill Byte to 8Â bytes. Longer CAN frames are padded with Fill Byte to the minimum valid length (default).2:All CAN frames are padded with Fill Byte to the length set as the Max DLC input of Open Diagnostic on CAN FD.vi or OBD Open on CAN FD.vi. 9Fill Byte specifies the CAN frame content, filled with defined data or random data. 0–255:Byte is used optionally to fill short CAN frames.256:Short CAN frames are filled optionally with random bytes. The default is 255 (0xFF).10Invalid Response as Error specifies how the toolkit handles an invalid ECU response. 0:Invalid response is indicated by success? = FALSE only (default).1:Invalid response is returned as an error in addition.11Max RspPending Count defines the number of times a ReqCorrectlyRcvd-RspPending (0x78) Negative Response Message will be accepted to extend the command timeout (default 5). If this message is sent more often in response to a request, an error –8120 is returned. If the ECU implements commands with a long duration (for example, flash commands), you may need to extend this number.12VWTP Command Time Out sets the time in milliseconds the host waits for a VWTP 2.0 command to be executed (default 50 ms). The specification states this as 50 ms plus the network latency, but some ECUs may require higher values.13STmin sets the minimum time in seconds between the end of transmission of a frame in a diagnostic request message and the start of transmission of the next frame in the diagnostic request message for LIN-based diagnostic communication. The default is 0.14P2min sets the minimum time in seconds between reception of the last frame of the diagnostic request and the response sent by the node for LIN-based diagnostic communication. The default is 0.05.15Termination sets the NI-XNET Termination property. Reflections on the CAN and LIN bus can cause communication failures. To prevent reflections, termination can be present as external resistance or resistance the XNET CAN or LIN board applies internally. This property determines whether the XNET board uses termination to the bus. For further information about appropriate terminations of a CAN or LIN network, refer to the NI-XNET Hardware and Software Manual. The default is 0.16Timeout RspPending is the timeout in milliseconds the master waits for the response to a diagnostic request message after receiving an RspPending Negative Response Message (0x78). The default is 1000 ms. This is the P2* timeout from the ISO 15765-3 specification.17LIN Sleep is available for LIN only and controls the sleep state of the LIN bus. Allowed values are: 0:Remote Sleep. The complete LIN bus is sent to the Sleep state.1:Remote Wakeup. The LIN bus is woken up.18Actual CAN IO Mode is a read-only property. Diag Set Property.vi with this parameter value has no effect.19Response Plausibility Check defines whether the first byte of the diagnostic response is checked to contain the + 0x40 offset (positive response) or whether the first byte is 0x7F (negative response). 0:Response Plausibility Check is disabled.1:Response Plausibility Check is enabled (default). The default is 1, which is compatible with previous versions of the Automotive Diagnostic Command Set. Set this property to 0 only if you use non-standard diagnostic services.20Session-based properties specifies whether the following ISO TP (15765-2) and DoIP properties are shared globally or apply only to the specific diagnostic session: Timeout Diag CommandTimeout FC (Bs)Timeout CF (Cr)Receive Block Size (BS)Wait Time CD (STmin)Max Wait Frames (N_WFTmax)Wait Frames to Send (N_WAIT)Time between Waits (T_W)Fill CAN FramesFill ByteInvalid Response as ErrorMax RespPending CountVWTP Command Time OutTimeout RspPending 0:These properties are shared between sessions that are in the same application instance (default).1:These properties apply only to the specific session. To prevent influencing other sessions, set this property immediately after opening the diagnostic session. 21DoIP Acknowledge Mode returns the DoIP Diagnostic Message Acknowledgement behavior. 0:ADCS acknowledges diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages (default).1:ADCS does not acknowledge diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages.2:ADCS acknowledges diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command.3:ADCS does not acknowledge diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
| 0 | Timeout Diag Command is the timeout in milliseconds the master waits for the response to or DoIP acknowledgement of a diagnostic request message. The default is 1000Â ms. This is the P2 timeout from the ISO 15765-3 specification. |
| 1 | Timeout FC (Bs) is the timeout in milliseconds the master waits for a Flow Control frame after sending a First Frame or the last Consecutive Frame of a block. The default is 250 ms. |
| 2 | Timeout CF (Cr) is the timeout in milliseconds the master waits for a Consecutive Frame in a multiframe response. The default is 250 ms for CAN and 1000 ms for LIN. |
| 3 | Receive Block Size (BS) is the number of Consecutive Frames the slave sends in one block before waiting for the next Flow Control frame. A value of 0 (default) means all Consecutive Frames are sent in one run without interruption. |
| 4 | Wait Time CF (STmin) defines the minimum time for the slave to wait between sending two Consecutive Frames of a block. Values from 0 to 127 are wait times in milliseconds. Values 241 to 249 (Hex F1 to F9) mean wait times of 100 Âµs to 900 Âµs, respectively. All other values are reserved. The default is 5 ms. |
| 5 | Max Wait Frames (N_WFTmax) is the maximum number of WAIT frames the master accepts before terminating the connection. The default is 10. |
| 6 | Wait Frames to Send (N_WAIT) is the number of WAIT frames the master sends every time before a CTS frame is sent. If this value is set to a negative number (for example, 0xFFFFFFFF = –1), the master sends an OVERLOAD frame instead of a WAIT, and reception is aborted. The default is 0 for maximum speed. |
| 7 | Time between Waits (T_W) is the number of milliseconds the master waits after sending a WAIT frame. The default is 25. |
| 8 | Fill CAN Frames specifies how ISO-TP CAN frames are padded. 0:Sends CAN frames with the minimum valid length, padded with Fill Byte if necessary. This setting allows for maximum performance of the CAN bus.1:CAN frames shorter than 8Â bytes are padded with Fill Byte to 8Â bytes. Longer CAN frames are padded with Fill Byte to the minimum valid length (default).2:All CAN frames are padded with Fill Byte to the length set as the Max DLC input of Open Diagnostic on CAN FD.vi or OBD Open on CAN FD.vi. |
| 0: | Sends CAN frames with the minimum valid length, padded with Fill Byte if necessary. This setting allows for maximum performance of the CAN bus. |
| 1: | CAN frames shorter than 8Â bytes are padded with Fill Byte to 8Â bytes. Longer CAN frames are padded with Fill Byte to the minimum valid length (default). |
| 2: | All CAN frames are padded with Fill Byte to the length set as the Max DLC input of Open Diagnostic on CAN FD.vi or OBD Open on CAN FD.vi. |
| 9 | Fill Byte specifies the CAN frame content, filled with defined data or random data. 0–255:Byte is used optionally to fill short CAN frames.256:Short CAN frames are filled optionally with random bytes. The default is 255 (0xFF). |
| 0–255: | Byte is used optionally to fill short CAN frames. |
| 256: | Short CAN frames are filled optionally with random bytes. |
| 10 | Invalid Response as Error specifies how the toolkit handles an invalid ECU response. 0:Invalid response is indicated by success? = FALSE only (default).1:Invalid response is returned as an error in addition. |
| 0: | Invalid response is indicated by success? = FALSE only (default). |
| 1: | Invalid response is returned as an error in addition. |
| 11 | Max RspPending Count defines the number of times a ReqCorrectlyRcvd-RspPending (0x78) Negative Response Message will be accepted to extend the command timeout (default 5). If this message is sent more often in response to a request, an error –8120 is returned. If the ECU implements commands with a long duration (for example, flash commands), you may need to extend this number. |
| 12 | VWTP Command Time Out sets the time in milliseconds the host waits for a VWTP 2.0 command to be executed (default 50 ms). The specification states this as 50 ms plus the network latency, but some ECUs may require higher values. |
| 13 | STmin sets the minimum time in seconds between the end of transmission of a frame in a diagnostic request message and the start of transmission of the next frame in the diagnostic request message for LIN-based diagnostic communication. The default is 0. |
| 14 | P2min sets the minimum time in seconds between reception of the last frame of the diagnostic request and the response sent by the node for LIN-based diagnostic communication. The default is 0.05. |
| 15 | Termination sets the NI-XNET Termination property. Reflections on the CAN and LIN bus can cause communication failures. To prevent reflections, termination can be present as external resistance or resistance the XNET CAN or LIN board applies internally. This property determines whether the XNET board uses termination to the bus. For further information about appropriate terminations of a CAN or LIN network, refer to the NI-XNET Hardware and Software Manual. The default is 0. |
| 16 | Timeout RspPending is the timeout in milliseconds the master waits for the response to a diagnostic request message after receiving an RspPending Negative Response Message (0x78). The default is 1000 ms. This is the P2* timeout from the ISO 15765-3 specification. |
| 17 | LIN Sleep is available for LIN only and controls the sleep state of the LIN bus. Allowed values are: 0:Remote Sleep. The complete LIN bus is sent to the Sleep state.1:Remote Wakeup. The LIN bus is woken up. |
| 0: | Remote Sleep. The complete LIN bus is sent to the Sleep state. |
| 1: | Remote Wakeup. The LIN bus is woken up. |
| 18 | Actual CAN IO Mode is a read-only property. Diag Set Property.vi with this parameter value has no effect. |
| 19 | Response Plausibility Check defines whether the first byte of the diagnostic response is checked to contain the + 0x40 offset (positive response) or whether the first byte is 0x7F (negative response). 0:Response Plausibility Check is disabled.1:Response Plausibility Check is enabled (default). The default is 1, which is compatible with previous versions of the Automotive Diagnostic Command Set. Set this property to 0 only if you use non-standard diagnostic services. |
| 0: | Response Plausibility Check is disabled. |
| 1: | Response Plausibility Check is enabled (default). |
| 20 | Session-based properties specifies whether the following ISO TP (15765-2) and DoIP properties are shared globally or apply only to the specific diagnostic session: Timeout Diag CommandTimeout FC (Bs)Timeout CF (Cr)Receive Block Size (BS)Wait Time CD (STmin)Max Wait Frames (N_WFTmax)Wait Frames to Send (N_WAIT)Time between Waits (T_W)Fill CAN FramesFill ByteInvalid Response as ErrorMax RespPending CountVWTP Command Time OutTimeout RspPending 0:These properties are shared between sessions that are in the same application instance (default).1:These properties apply only to the specific session. To prevent influencing other sessions, set this property immediately after opening the diagnostic session. |
| 0: | These properties are shared between sessions that are in the same application instance (default). |
| 1: | These properties apply only to the specific session. To prevent influencing other sessions, set this property immediately after opening the diagnostic session. |
| 21 | DoIP Acknowledge Mode returns the DoIP Diagnostic Message Acknowledgement behavior. 0:ADCS acknowledges diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages (default).1:ADCS does not acknowledge diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages.2:ADCS acknowledges diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command.3:ADCS does not acknowledge diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
| 0: | ADCS acknowledges diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages (default). |
| 1: | ADCS does not acknowledge diagnostic messages. ADCS reports timeouts of ECU diagnostic acknowledge messages. |
| 2: | ADCS acknowledges diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
| 3: | ADCS does not acknowledge diagnostic messages. ADCS ignores timeouts of ECU diagnostic acknowledge messages, but will still wait for an acknowledgement for the time specified in Timeout Diag Command. |
|  | property value is the value of the property to be set. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. It is copied unchanged to error out and has no other effect on the VI. It is provided for sequencing purposes only. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. It is copied unchanged from the error in cluster. It is provided for sequencing purposes only. |

Description

Use this VI to set several internal diagnostic parameters such as timeouts for the transport protocol. Use [Diag Get Property.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diaggetpropertyvi) to read them out.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-frame-recv-vi.html language=enus -->
## TOPIC 00013: Diagnostic Frame Recv.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-frame-recv-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-frame-recv-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Receives a raw CAN frame on the diagnostic CAN ID to check for errors in the transport protocol implementation of an ECU. Format Input timeout specifies the time in milliseconds to wait for a frame on the diagnostic identifier. If no frame arrives within this time, a timeout error is returne

### Diagnostic Frame Recv.vi

Purpose

Receives a raw CAN frame on the diagnostic CAN ID to check for errors in the transport protocol implementation of an ECU.
Format

[IMAGE alt='image' src='images/DiagnosticFrameRecvVI.gif']
Input

|  | timeout specifies the time in milliseconds to wait for a frame on the diagnostic identifier. If no frame arrives within this time, a timeout error is returned. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns an array of up to 8Â bytes of payload data from a CAN frame, or up to 64Â bytes of payload data from a CAN FD frame, received as CAN payload on the diagnostic identifier. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**Diagnostic Frame Recv.vi** receives an arbitrary raw CAN frame on the diagnostic CAN identifier. For example, you can check the transport protocol implementation of an ECU for correct responses if erroneous protocol requests are issued.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-frame-send-vi.html language=enus -->
## TOPIC 00014: Diagnostic Frame Send.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-frame-send-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-frame-send-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sends a raw CAN frame on the diagnostic CAN ID to check for errors in the transport protocol implementation of an ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not

### Diagnostic Frame Send.vi

Purpose

Sends a raw CAN frame on the diagnostic CAN ID to check for errors in the transport protocol implementation of an ECU.
Format

[IMAGE alt='image' src='images/DiagnosticFrameSendVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | data in is an array of up to 8Â bytes for standard CAN, or up to 64Â bytes for CAN FD, sent as CAN payload on the diagnostic identifier. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**Diagnostic Frame Send.vi** transmits an arbitrary raw CAN frame on the diagnostic CAN identifier. For example, you can check the transport protocol implementation of an ECU for robustness if erroneous protocol requests are issued.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-service-format.html language=enus -->
## TOPIC 00015: Diagnostic Service Format

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-service-format.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-service-format.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Diagnostic services have a common message format. Each service defines a Request Message, Positive Response Message, and Negative Response Message. The Request Message has the ServiceId as first byte, plus additional service-defined parameters. The Positive Response Message has an echo of the Servic

### Diagnostic Service Format

Diagnostic services have a common message format. Each service defines a Request Message, Positive Response Message, and Negative Response Message.

The Request Message has the ServiceId as first byte, plus additional service-defined parameters. The Positive Response Message has an echo of the ServiceId with bit 6 set as first byte, plus the service-defined response parameters.

The Negative Response Message is usually a three-byte message: it has the Negative Response ServiceId as first byte, an echo of the original ServiceId as second byte, and a ResponseCode as third byte. The only exception to this format is the negative response to an EscapeCode service; here, the third byte is an echo of the user-defined service code, and the fourth byte is the ResponseCode. The KWP2000 standard partly defines the ResponseCodes, but there is room left for manufacturer-specific extensions. For some of the ResponseCodes, KWP2000 defines an error handling procedure. Because both positive and negative responses have an echo of the requested service, you can always assign the responses to their corresponding request.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-service-format2.html language=enus -->
## TOPIC 00016: Diagnostic Service Format

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-service-format2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-service-format2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Diagnostic services have a common message format. Each service defines a Request Message, a Positive Response Message, and a Negative Response Message. The general format of the diagnostic services complies with the KWP2000 definition; most of the Service Ids also comply with KWP2000. The Request Me

### Diagnostic Service Format

Note

The Negative Response Message is usually a three-byte message: it has the Negative Response ServiceId (0x7F) as first byte, an echo of the original ServiceId as second byte, and a ResponseCode as third byte. The UDS standard partly defines the ResponseCodes, but there is room left for manufacturer-specific extensions. For some of the ResponseCodes, UDS defines an error handling procedure.

Because both positive and negative responses have an echo of the requested service, you always can assign the responses to their corresponding request.

Parent topic:

UDS (Unified Diagnostic Services)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-service-vi.html language=enus -->
## TOPIC 00017: Diagnostic Service.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-service-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-service-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes a generic diagnostic service. If a special service is not available through the KWP2000, UDS, or OBD service functions, you can build it using this VI. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subs

### Diagnostic Service.vi

Purpose

Executes a generic diagnostic service. If a special service is not available through the KWP2000, UDS, or OBD service functions, you can build it using this VI.
Format

[IMAGE alt='image' src='images/DiagnosticServiceVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | require response? indicates whether a diagnostic service expects a response (TRUE) or not (FALSE). In the latter case, error code is returned as 0, and data out as an empty array. |
|  | data in defines the diagnostic service request message sent to the ECU as a stream of bytes. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error code is the error code sent with a negative response message. In addition, the error cluster indicates an error and gives a more detailed description. If no negative response message occurred, 0 is returned. |
|  | data out returns the diagnostic service response message (positive or negative) the ECU sends as a stream of bytes. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**Diagnostic Service.vi** is a generic routine to execute any diagnostic service. The request and response messages are fed unmodified to the **data in** input and retrieved from the **data out** output, respectively. No interpretation of the contents is done, with one exception: the error number is retrieved from a negative response, if one occurs. In this case, an error also is communicated through the **error out** cluster.

All specialized diagnostic services call **Diagnostic Service.vi** internally.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-services.html language=enus -->
## TOPIC 00018: Diagnostic Services

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-services.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-services.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The diagnostic services available in KWP2000 are grouped in functional units and identified by a one-byte code (ServiceId). The standard does not define all codes; for some codes, the standard refers to other SAE or ISO standards, and some are reserved for manufacturer-specific extensions. The Autom

### Diagnostic Services

The diagnostic services available in KWP2000 are grouped in functional units and identified by a one-byte code (ServiceId). The standard does not define all codes; for some codes, the standard refers to other SAE or ISO standards, and some are reserved for manufacturer-specific extensions. The Automotive Diagnostic Command Set supports the following services:

- Diagnostic Management
- Data Transmission
- Stored Data Transmission (Diagnostic Trouble Codes)
- Input/Output Control
- Remote Activation of Routine

Note

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-services2.html language=enus -->
## TOPIC 00019: Diagnostic Services

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-services2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-services2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The diagnostic services available in UDS are grouped in functional units and identified by a one-byte code (ServiceId). Not all codes are defined in the standard; for some codes, the standard refers to other standards, and some are reserved for manufacturer-specific extensions. The Automotive Diagno

### Diagnostic Services

The diagnostic services available in UDS are grouped in functional units and identified by a one-byte code (ServiceId). Not all codes are defined in the standard; for some codes, the standard refers to other standards, and some are reserved for manufacturer-specific extensions. The Automotive Diagnostic Command Set supports the following services:

- Diagnostic Management
- Data Transmission
- Stored Data Transmission (Diagnostic Trouble Codes)
- Input/Output Control
- Remote Activation of Routine

For UDS on LIN, a slave node must support a set of ISO 14229-1 diagnostic services such as:

- Node identification (reading hardware and software version, hardware part number, and diagnostic version)
- Reading data parameters (reading ECU internal values such as oil temperature and vehicle speed)
- Writing parameter values if applicable

Note

LIN Specification Package

Parent topic:

UDS (Unified Diagnostic Services)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=diagnostic-trouble-codes.html language=enus -->
## TOPIC 00020: Diagnostic Trouble Codes

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `diagnostic-trouble-codes.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/diagnostic-trouble-codes.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A major diagnostic feature is the readout of Diagnostic Trouble Codes (DTCs). KWP2000 defines several services that access DTCs based on their group or status.

### Diagnostic Trouble Codes

A major diagnostic feature is the readout of Diagnostic Trouble Codes (DTCs). KWP2000 defines several services that access DTCs based on their group or status.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=disablenormalmessagetransmission-vi.html language=enus -->
## TOPIC 00021: DisableNormalMessageTransmission.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `disablenormalmessagetransmission-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/disablenormalmessagetransmission-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the DisableNormalMessageTransmission service. The ECU no longer transmits its regular communication messages (usually CAN messages). Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired thr

### DisableNormalMessageTransmission.vi

Purpose

Executes the DisableNormalMessageTransmission service. The ECU no longer transmits its
regular communication messages (usually CAN messages).
Format

[IMAGE alt='image' src='images/DisableNormalMessageTransmissionVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | response required? indicates whether the ECU answers this service (TRUE, default) or not (FALSE). In the latter case, success? is TRUE. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-activate-routing-vi.html language=enus -->
## TOPIC 00022: DoIP Activate Routing.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-activate-routing-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-activate-routing-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Defines the source and target addresses for a DoIP TCP/IP connection. Format Input Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements

### DoIP Activate Routing.vi

Purpose

Defines the source and target addresses for a DoIP TCP/IP connection.
Format

[IMAGE alt='image' src='images/DoIPActivateRoutingVI.gif']
Input

|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | Source Address is the DoIP source address of the tester that starts the communication. |
|  | Activation Type indicates the specific type of routing activation that may require different types of authentication and/or confirmation. Defined values are: 0Default.1WWH-OBD (worldwide harmonized onboard diagnostic).0xE0Use an OEM-specific central security approach. Values 2 to 0xDF are reserved. Values 0xE0 to 0xFF are OEM specific. |
| 0 | Default. |
| 1 | WWH-OBD (worldwide harmonized onboard diagnostic). |
| 0xE0 | Use an OEM-specific central security approach. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | Target address of responding entity is the logical address of the responding DoIP entity. This address is contained inside the routing activation response. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Activate Routing.vi** establishes a route for the DoIP messages and assigns an endpoint **Target Address**. After successfully establishing a route, diagnostic messages can be exchanged with the target DoIP entity using any diagnostic service VI.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-connect-vi.html language=enus -->
## TOPIC 00023: DoIP Connect.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-connect-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-connect-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Creates a TCP/IP connection to a DoIP entity identified by its IP address. Format Input remote port defines the ECU's TCP port to connect to. Default is 13400. local port defines the source TCP port to use. Default is 0, which will select an available port randomly. TCP ports may be kept in

### DoIP Connect.vi

Purpose

Creates a TCP/IP connection to a DoIP entity identified by its IP address.
Format

[IMAGE alt='image' src='images/DoIPConnectVI.gif']
Input

|  | remote port defines the ECU's TCP port to connect to. Default is 13400. |
| --- | --- |
|  | local port defines the source TCP port to use. Default is 0, which will select an available port randomly. TCP ports may be kept in a wait state for an operating system specific time after the connection was closed, which prevents reusing that port until that time has passed. Consult your operating system's documentation on how to configure this timeout. |
|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | address is the IP address of the DoIP entity to connect to (zero-terminated string in a.b.c.d notation). |
|  | protocol version is the protocol version of the DoIP packets. Choices are: 12010 â Initial draft version DoIP ISO/DIS 13400-2:2010 22012 â Official released version DoIP ISO 13400-2:2012 If protocol version is set to 2010, the protocol version byte of the Generic DoIP header is set to 1. If protocol version is set to 2012, the protocol version byte of the Generic DoIP header is set to 2. If the input is not connected or set to 0, the protocol version specified in Open Diagnostic on IP.vi is used. The protocol versions used by the ECU and Automotive Diagnostic Command Set application must match or a Generic Header error will be issued. |
| 1 | 2010 â Initial draft version DoIP ISO/DIS 13400-2:2010 |
| 2 | 2012 â Official released version DoIP ISO 13400-2:2012 |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | Source Address is the DoIP source address of the tester that starts the communication. You can leave this input unwired if you are activating a route through DoIP Activate Routing.vi. Note Â Â If you use DoIP Activate Routing.vi at a later point to activate a route, then you must specify the source address of the tester using that VI. |
|  | Target Address is the DoIP target address of the device under test. When you are connecting directly to the device under test without using a DoIP gateway, you can leave this input unwired if you activate a route through DoIP Activate Routing.vi. If you are connecting to the device under test through a DoIP gateway, you must specify the target address of the device under test using this input. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

DoIP Connect.vi creates a unique TCP/IP data connection to a certain DoIP entity identified by its IP **address**. The IP address might be retrieved from [DoIP Get Entities.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi). The TCP/IP data connection is needed to exchange diagnostic service requests.

When you connect directly to the device under test without using a DoIP gateway, you can either specify the **Source Address** and **Target Address** or leave them blank if a route is activated later using [DoIP Activate Routing.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipactivateroutingvi). However, if you connect to the device under test through a DoIP gateway, you must specify the **Target Address** of the device under test in this VI.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-disconnect-vi.html language=enus -->
## TOPIC 00024: DoIP Disconnect.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-disconnect-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-disconnect-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Disconnects the TCP/IP connection to a DoIP entity. Format Input Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. e

### DoIP Disconnect.vi

Purpose

Disconnects the TCP/IP connection to a DoIP entity.
Format

[IMAGE alt='image' src='images/DoIPDisconnectVI.gif']
Input

|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Disconnect.vi** terminates the TCP/IP connection to the connected DoIP entity. After executing this VI, diagnostic services no longer can be executed on that DoIP entity. You can reconnect with [DoIP Connect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipconnectvi).

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-functions.html language=enus -->
## TOPIC 00025: DoIP Functions

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-functions.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-functions.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: DoIP Activate Routing.vi DoIP Connect.vi DoIP Disconnect.vi DoIP Get Diagnostic Power Mode.vi DoIP Get DoIP Entity Status.vi DoIP Get Entities.vi DoIP Send Vehicle Identification Request.vi DoIP Send Vehicle Identification Request w EID.vi DoIP Send Vehicle Identification Request w VIN.vi

### DoIP Functions

[DoIP Activate Routing.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipactivateroutingvi)

[DoIP Connect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipconnectvi)

[DoIP Disconnect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipdisconnectvi)

[DoIP Get Diagnostic Power Mode.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetdiagnosticpowermodevi)

[DoIP Get DoIP Entity Status.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetdoipentitystatusvi)

[DoIP Get Entities.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi)

[DoIP Send Vehicle Identification Request.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipsendvehicleidentificationrequestvi)

[DoIP Send Vehicle Identification Request w EID.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipsendvehicleidentificationrequestweidvi)

[DoIP Send Vehicle Identification Request w VIN.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipsendvehicleidentificationrequestwvinvi)

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-get-diagnostic-power-mode-vi.html language=enus -->
## TOPIC 00026: DoIP Get Diagnostic Power Mode.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-get-diagnostic-power-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-get-diagnostic-power-mode-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Gets information about the DoIP entity power state. Format Input Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. e

### DoIP Get Diagnostic Power Mode.vi

Purpose

Gets information about the DoIP entity power state.
Format

[IMAGE alt='image' src='images/DoIPGetDiagnosticPowerModeVI.gif']
Input

|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | power mode identifies whether the vehicle is in Diagnostic Power Mode and ready to perform reliable diagnostics. Possible values are: 0Not ready1Ready All other values are reserved. |
| 0 | Not ready |
| 1 | Ready |
|  | ok? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Get Diagnostic Power Mode.vi** retrieves the Diagnostic Power Mode of a vehicle. For example, test equipment can use this information to verify whether the vehicle is in Diagnostic Power Mode, which allows for performing reliable diagnostics on the vehicle's components.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-get-doip-entity-status-vi.html language=enus -->
## TOPIC 00027: DoIP Get DoIP Entity Status.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-get-doip-entity-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-get-doip-entity-status-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Gets status information from a DoIP entity. Format Input Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. error in

### DoIP Get DoIP Entity Status.vi

Purpose

Gets status information from a DoIP entity.
Format

[IMAGE alt='image' src='images/DoIPGetDoIPEntityStatusVI.gif']
Input

|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | node type is a U8 ring that indicates the type of DoIP entity. Possible values are: 0DoIP gateway1DoIP node All other values are reserved. |
| 0 | DoIP gateway |
| 1 | DoIP node |
|  | ok? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | max sockets represents the maximum number of concurrent TCP/IP sockets allowed with this DoIP entity excluding the reserve socket required for socket handling. |
|  | cur sockets is the number of currently established TCP/IP sockets. |

Description

**DoIP Get DoIP Entity Status.vi** identifies certain operating conditions of the responding DoIP entity. For example, this allows for test equipment to detect existing diagnostic communication sessions as well as the capabilities of a DoIP entity.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-get-entities-vi.html language=enus -->
## TOPIC 00028: DoIP Get Entities.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-get-entities-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-get-entities-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Returns a table of all DoIP entities (vehicles) on the local subnet, possibly restricted to EID or VIN. Format Input Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), but can be overridden t

### DoIP Get Entities.vi

Purpose

Returns a table of all DoIP entities (vehicles) on the local subnet, possibly restricted to EID or VIN.
Format

[IMAGE alt='image' src='images/DoIPGetEntitiesVI.gif']
Input

|  | Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), but can be overridden to specify a specific broadcast address, e.g. on a specific Network Interface Controller). |
| --- | --- |
|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | DoIP Open Type is a U16 ring. It defines which DoIP entities this command queries and lists. Allowed values are VIN, EID, and All. |
|  | VIN or EID depends on the DoIP Open Type: DoIP Open TypeVIN or EID ValueVINVIN or EID is a 17-character Vehicle Identification Number. Only DoIP entities for this VIN are listed.EIDVIN or EID is an Entity ID (usually a MAC address). Only the DoIP entity with this ID is listed. Specify the EID as xx-xx-xx-xx-xx-xx, where each x is a hexadecimal digit.AllVIN or EID is ignored. |
| DoIP Open Type | VIN or EID Value |
| VIN | VIN or EID is a 17-character Vehicle Identification Number. Only DoIP entities for this VIN are listed. |
| EID | VIN or EID is an Entity ID (usually a MAC address). Only the DoIP entity with this ID is listed. Specify the EID as xx-xx-xx-xx-xx-xx, where each x is a hexadecimal digit. |
| All | VIN or EID is ignored. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | All Versions specifies whether the request is sent with 0xFF as the protocol version in the Generic DoIP header. The default is TRUE. If the protocol version in Open Diagnostic on IP.vi is set to 2010, this flag is ignored and the request is always sent with the protocol version byte of the header set to 1. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DoIP Entities is an array of clusters, each of which contains the description of one DoIP entity that responded to the command: VIN is the 17-character Vehicle Identification Number of the DoIP entity. It can be blank if the DoIP entity does not yet belong to a vehicle.Source Address is the 16-bit DoIP address of this entity. This address can distinguish multiple DoIP entities within a vehicle.EID is a 6-byte array of the Entity ID, which is usually the DoIP device MAC address.GID is a unique 6-byte group identification of DoIP entities that belong to the same vehicle. It is used as long as a VIN is not yet defined.IP Address is the IP Address of this DoIP entity in a.b.c.d notation. Use this IP address to connect to the DoIP entity using DoIP Connect.vi. |
|  | VIN is the 17-character Vehicle Identification Number of the DoIP entity. It can be blank if the DoIP entity does not yet belong to a vehicle. |
|  | Source Address is the 16-bit DoIP address of this entity. This address can distinguish multiple DoIP entities within a vehicle. |
|  | EID is a 6-byte array of the Entity ID, which is usually the DoIP device MAC address. |
|  | GID is a unique 6-byte group identification of DoIP entities that belong to the same vehicle. It is used as long as a VIN is not yet defined. |
|  | IP Address is the IP Address of this DoIP entity in a.b.c.d notation. Use this IP address to connect to the DoIP entity using DoIP Connect.vi. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Get Entities.vi** uses a UDP broadcast to identify all DoIP entities in the local subnet matching a certain condition. The entities responding are returned in the **DoIP Entities** cluster array.

The conditions are either a common VIN or EID or simply all entities connected. Refer to the **DoIP Open Type** and **VIN or EID** descriptions.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-send-vehicle-identification-request-vi.html language=enus -->
## TOPIC 00029: DoIP Send Vehicle Identification Request.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-send-vehicle-identification-request-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-send-vehicle-identification-request-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sends a UDP request to all DoIP-capable vehicles in the local subnet to identify themselves. Format Input Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), but can be overridden to specify a

### DoIP Send Vehicle Identification Request.vi

Purpose

Sends a UDP request to all DoIP-capable vehicles in the local subnet to identify themselves.
Format

[IMAGE alt='image' src='images/DoIPSendVehicleIdentificationRequestVI.gif']
Input

|  | Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), but can be overridden to specify a specific broadcast address, e.g. on a specific Network Interface Controller). |
| --- | --- |
|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | All Versions specifies whether the request is sent with 0xFF as the protocol version in the Generic DoIP header. The default is TRUE. If the protocol version in Open Diagnostic on IP.vi is set to 2010, this flag is ignored and the request is always sent with the protocol version byte of the header set to 1. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Send Vehicle Identification Request.vi** sends a Vehicle Identification Request to all DoIP entities in the local subnet.

Usually, this is done as part of [/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi) and does not need to be executed separately.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-send-vehicle-identification-request-w-ei.html language=enus -->
## TOPIC 00030: DoIP Send Vehicle Identification Request w EID.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-send-vehicle-identification-request-w-ei.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-send-vehicle-identification-request-w-ei.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sends a UDP request to all DoIP-capable vehicles with a certain EID (MAC address) in the local subnet to identify themselves. Format Input Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), b

### DoIP Send Vehicle Identification Request w EID.vi

Purpose

Sends a UDP request to all DoIP-capable vehicles with a certain EID (MAC address) in the local subnet to identify themselves.
Format

[IMAGE alt='image' src='images/DoIPSendVehicleIdentificationRequestwEIDVI.gif']
Input

|  | Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), but can be overridden to specify a specific broadcast address, e.g. on a specific Network Interface Controller). |
| --- | --- |
|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | EID is the Entity ID (usually the MAC address) of the DoIP entity assumed to respond. Specify the EID as xx-xx-xx-xx-xx-xx, where each x stands for a hexadecimal digit. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | All versions specifies whether the request is sent with 0xFF as the protocol version in the Generic DoIP header. The default is TRUE. If the protocol version in Open Diagnostic on IP.vi is set to 2010, this flag is ignored and the request is always sent with the protocol version byte of the header set to 1. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Send Vehicle Identification Request w EID.vi** sends a Vehicle Identification Request to all DoIP entities in the local subnet identified by the given **EID**.

Usually, this is done as part of [/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi) and does not need to be executed separately.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=doip-send-vehicle-identification-request-w-vi.html language=enus -->
## TOPIC 00031: DoIP Send Vehicle Identification Request w VIN.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `doip-send-vehicle-identification-request-w-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/doip-send-vehicle-identification-request-w-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Sends a UDP request to all DoIP-capable vehicles with a certain VIN (Vehicle Identification Number) in the local subnet to identify themselves. Format Input Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interf

### DoIP Send Vehicle Identification Request w VIN.vi

Purpose

Sends a UDP request to all DoIP-capable vehicles with a certain VIN (Vehicle Identification Number) in the local subnet to identify themselves.
Format

[IMAGE alt='image' src='images/DoIPSendVehicleIdentificationRequestwVINVI.gif']
Input

|  | Broadcast Address is the subnet address to send the request to. It defaults to 255.255.255.255 (broadcast on the default Network Interface Controller), but can be overridden to specify a specific broadcast address, e.g. on a specific Network Interface Controller). |
| --- | --- |
|  | Diag reference in specifies the diagnostic session handle, obtained from Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | VIN is the 17-character Vehicle Identification Number of the DoIP entity assumed to respond. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | All Versions specifies whether the request is sent with 0xFF as the protocol version in the Generic DoIP header. The default is TRUE. If the protocol version in Open Diagnostic on IP.vi is set to 2010, this flag is ignored and the request is always sent with the protocol version byte of the header set to 1. |

Output

|  | Diag reference out is a copy of Diag reference in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**DoIP Send Vehicle Identification Request w VIN.vi** sends a Vehicle Identification Request to all DoIP entities in the local subnet identified by the given **VIN**.

Usually, this is done as part of [/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi) and does not need to be executed separately.

Parent topic:

DoIP Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=dtc-to-string-vi.html language=enus -->
## TOPIC 00032: DTC to String.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `dtc-to-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/dtc-to-string-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Returns a string representation (such as P1234) for a 2-byte Diagnostic Trouble Code (DTC). Format Input DTC (num) is the DTC number as returned in the following clusters: ReadDTCByStatus.viReadStatusOfDTC.viUDS ReportDTCBySeverityMaskRecord.viUDS ReportDTCByStatusMask.viUDS ReportSeverityIn

### DTC to String.vi

Purpose

Returns a string representation (such as P1234) for a 2-byte Diagnostic Trouble Code (DTC).
Format

[IMAGE alt='image' src='images/DTCtoStringVI.gif']
Input

|  | DTC (num) is the DTC number as returned in the following clusters: ReadDTCByStatus.viReadStatusOfDTC.viUDS ReportDTCBySeverityMaskRecord.viUDS ReportDTCByStatusMask.viUDS ReportSeverityInformationOfDTC.viUDS ReportSupportedDTCs.viOBD Request Emission Related DTCs.viOBD Request Emission Related DTCs During Current Drive Cycle.vi |
| --- | --- |

Note

|  | DTC (string) is the DTC string representation. |
| --- | --- |

Description

The SAE J2012 standard specifies a naming scheme for 2-byte DTCs consisting of one letter and four digits. Use **DTC to String.vi** to convert a DTC numerical representation to this name.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=ecureset-vi.html language=enus -->
## TOPIC 00033: ECUReset.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `ecureset-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/ecureset-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ECUReset service. Resets the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elemen

### ECUReset.vi

Purpose

Executes the ECUReset service. Resets the ECU.
Format

[IMAGE alt='image' src='images/ECUResetVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | mode indicates the reset mode: HexDescription01PowerOn This value identifies the PowerOn ResetMode, a simulated PowerOn reset that most ECUs perform after the ignition OFF/ON cycle. When the ECU performs the reset, the client (tester) re-establishes communication.02PowerOnWhileMaintainingCommunication This value identifies the PowerOn ResetMode, a simulated PowerOn reset that most ECUs perform after the ignition OFF/ON cycle. When the ECU performs the reset, the server (ECU) maintains communication with the client (tester).03–7FReserved80–FFManufacturerSpecific This range of values is reserved for vehicle manufacturer-specific use. |
| Hex | Description |
| 01 | PowerOn This value identifies the PowerOn ResetMode, a simulated PowerOn reset that most ECUs perform after the ignition OFF/ON cycle. When the ECU performs the reset, the client (tester) re-establishes communication. |
| 02 | PowerOnWhileMaintainingCommunication This value identifies the PowerOn ResetMode, a simulated PowerOn reset that most ECUs perform after the ignition OFF/ON cycle. When the ECU performs the reset, the server (ECU) maintains communication with the client (tester). |
| 03–7F | Reserved |
| 80–FF | ManufacturerSpecific This range of values is reserved for vehicle manufacturer-specific use. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests the ECU to perform an ECU reset effectively based on the **mode** parameter value content. The vehicle manufacturer determines when the positive response message is sent.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=enablenormalmessagetransmission-vi.html language=enus -->
## TOPIC 00034: EnableNormalMessageTransmission.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `enablenormalmessagetransmission-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/enablenormalmessagetransmission-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the EnableNormalMessageTransmission service. The ECU starts transmitting its regular communication messages (usually CAN messages). Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired thro

### EnableNormalMessageTransmission.vi

Purpose

Executes the EnableNormalMessageTransmission service. The ECU starts transmitting its
regular communication messages (usually CAN messages).
Format

[IMAGE alt='image' src='images/EnableNormalMessageTransmissionVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | response required? indicates whether the ECU answers this service (TRUE, default) or not (FALSE). In the latter case, success? is TRUE. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=external-references.html language=enus -->
## TOPIC 00035: External References

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `external-references.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/external-references.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For more information about the KWP2000 Standard, refer to the ISO 14230-3 standard.

### External References

For more information about the KWP2000 Standard, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=external-references2.html language=enus -->
## TOPIC 00036: External References

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `external-references2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/external-references2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For more information about the UDS Standard, refer to the ISO 15765-3 standard.

### External References

For more information about the UDS Standard, refer to the ISO 15765-3 standard.

Parent topic:

UDS (Unified Diagnostic Services)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=general-functions.html language=enus -->
## TOPIC 00037: General Functions

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `general-functions.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/general-functions.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Close Diagnostic.vi Convert from Phys.vi Convert to Phys.vi Create Extended CAN IDs.vi Diag Get Property.vi Diagnostic Frame Recv.vi Diagnostic Frame Send.vi Diagnostic Service.vi Diag Set Property.vi DTC to String.vi Get Time Stamp.vi OBD Open on CAN FD.vi Open Diagnostic on CAN FD.vi Open Diagnost

### General Functions

[Close Diagnostic.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_closediagnosticvi)

[Convert from Phys.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_convertfromphysvi)

[Convert to Phys.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_converttophysvi)

[Create Extended CAN IDs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_createextendedcanidsvi)

[Diag Get Property.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diaggetpropertyvi)

[Diagnostic Frame Recv.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diagnosticframerecvvi)

[Diagnostic Frame Send.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diagnosticframesendvi)

[Diagnostic Service.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diagnosticservicevi)

[Diag Set Property.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_diagsetpropertyvi)

[DTC to String.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_dtctostringvi)

[Get Time Stamp.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_gettimestampvi)

[OBD Open on CAN FD.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdopenoncanfdvi)

[Open Diagnostic on CAN FD.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_opendiagnosticoncanfdvi)

[Open Diagnostic on IP.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_opendiagnosticonipvi)

[Open Diagnostic on LIN.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_opendiagnosticonlinvi)

[Start Periodic TesterPresent.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_startperiodictesterpresentvi)

[Stop Periodic TesterPresent.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_stopperiodictesterpresentvi)

[VWTP Connection Test.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_vwtpconnectiontestvi)

[VWTP Connect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_vwtpconnectvi)

[VWTP Disconnect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_vwtpdisconnectvi)

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=get-time-stamp-vi.html language=enus -->
## TOPIC 00038: Get Time Stamp.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `get-time-stamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/get-time-stamp-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Gets timestamp information about the first/last send/received frame of the ISO TP for CAN and LIN. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on LIN.vi and wired through subsequent diagnostic VIs. Normally,

### Get Time Stamp.vi

Purpose

Gets timestamp information about the first/last send/received frame of the ISO TP for CAN and LIN.
Format

[IMAGE alt='image' src='images/GetTimeStampVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on LIN.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. It is copied unchanged to error out and has no other effect on the VI. It is provided for sequencing purposes only. |

Output

|  | Time Stamp write first contains the timestamp of the first write frame. This is usually the FF or SF of the ISO TP. |
| --- | --- |
|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
|  | Time Stamp write last contains the timestamp of the last write frame. This is usually the last CF or SF of the ISO TP. |
|  | Time Stamp read first contains the timestamp of the first read frame. This is usually the FF or SF of the ISO TP. |
|  | Time Stamp read last contains the timestamp of the last read frame. This is usually the CF or SF of the ISO TP. |
|  | error out describes error conditions. It is copied unchanged from the error in cluster. It is provided for sequencing purposes only. |

Description

Get Time Stamp.vi

Note

The UDS Read ECU Information example includes an example for getting the timestamp.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=getseed-unlock.html language=enus -->
## TOPIC 00039: GetSeed/Unlock

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `getseed-unlock.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/getseed-unlock.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A GetSeed/Unlock mechanism may protect some diagnostic services. However, the applicable services are left to the manufacturer and not defined by the standard. You can execute the GetSeed/Unlock mechanism through the SecurityAccess service. This defines several levels of security, but the manufactur

### GetSeed/Unlock

A GetSeed/Unlock mechanism may protect some diagnostic services. However, the applicable services are left to the manufacturer and not defined by the standard.

You can execute the GetSeed/Unlock mechanism through the SecurityAccess service. This defines several levels of security, but the manufacturer assigns these levels to certain services.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=input-output-control.html language=enus -->
## TOPIC 00040: Input/Output Control

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `input-output-control.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/input-output-control.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: KWP2000 defines services to modify internal or external ECU signals. One example is redirecting ECU sensor inputs to stimulated signals. The control parameters of these commands are manufacturer specific and not defined in the standard.

### Input/Output Control

KWP2000 defines services to modify internal or external ECU signals. One example is redirecting ECU sensor inputs to stimulated signals. The control parameters of these commands are manufacturer specific and not defined in the standard.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=inputoutputcontrolbylocalidentifier-vi.html language=enus -->
## TOPIC 00041: InputOutputControlByLocalIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `inputoutputcontrolbylocalidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/inputoutputcontrolbylocalidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the InputOutputControlByLocalIdentifier service. Modifies ECU I/O port behavior. Format Input data in defines application-specific data for this service. diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and w

### InputOutputControlByLocalIdentifier.vi

Purpose

Executes the InputOutputControlByLocalIdentifier service. Modifies ECU I/O port behavior.
Format

[IMAGE alt='image' src='images/InputOutputControlByLocalIdentifierVI.gif']
Input

|  | data in defines application-specific data for this service. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | local ID defines the local identifier of the I/O to be manipulated. The values are application specific. |
|  | mode defines the type of I/O control. The values are application specific. The usual values are: 0: ReturnControlToECU1: ReportCurrentState4: ResetToDefault5: FreezeCurrentState7: ShortTermAdjustment8: LongTermAdjustment |
| 0: ReturnControlToECU |  |
| 1: ReportCurrentState |  |
| 4: ResetToDefault |  |
| 5: FreezeCurrentState |  |
| 7: ShortTermAdjustment |  |
| 8: LongTermAdjustment |  |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific data for this service. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI substitutes a value for an input signal or internal ECU function. It also controls an output (actuator) of an electronic system referenced by the **local ID** parameter.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=kwp2000-key-word-protocol-2000.html language=enus -->
## TOPIC 00042: KWP2000 (Key Word Protocol 2000)

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `kwp2000-key-word-protocol-2000.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/kwp2000-key-word-protocol-2000.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The KWP2000 protocol has become a de facto standard in automotive diagnostic applications. It is standardized as ISO 14230-3. KWP2000 describes the implementation of various diagnostic services you can access through the protocol. You can run KWP2000 on several transport layers such as K-line (seria

### KWP2000 (Key Word Protocol 2000)

The KWP2000 protocol has become a de facto standard in automotive diagnostic applications. It is standardized as ISO 14230-3. KWP2000 describes the implementation of various diagnostic services you can access through the protocol. You can run KWP2000 on several transport layers such as K-line (serial) or CAN.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=kwp2000-services.html language=enus -->
## TOPIC 00043: KWP2000 Services

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `kwp2000-services.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/kwp2000-services.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClearDiagnosticInformation.vi ControlDTCSetting.vi DisableNormalMessageTransmission.vi ECUReset.vi EnableNormalMessageTransmission.vi InputOutputControlByLocalIdentifier.vi ReadDataByLocalIdentifier.vi ReadDTCByStatus.vi ReadECUIdentification.vi ReadMemoryByAddress.vi ReadStatusOfDTC.vi RequestRouti

### KWP2000 Services

[ClearDiagnosticInformation.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_cleardiagnosticinformationvi)

[ControlDTCSetting.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_controldtcsettingvi)

[DisableNormalMessageTransmission.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_disablenormalmessagetransmissionvi)

[ECUReset.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_ecuresetvi)

[EnableNormalMessageTransmission.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_enablenormalmessagetransmissionvi)

[InputOutputControlByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_inputoutputcontrolbylocalidentifiervi)

[ReadDataByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_readdatabylocalidentifiervi)

[ReadDTCByStatus.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_readdtcbystatusvi)

[ReadECUIdentification.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_readecuidentificationvi)

[ReadMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_readmemorybyaddressvi)

[ReadStatusOfDTC.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_readstatusofdtcvi)

[RequestRoutineResultsByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_requestroutineresultsbylocalidentifiervi)

[RequestSeed.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_requestseedvi)

[SendKey.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_sendkeyvi)

[StartDiagnosticSession.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_startdiagnosticsessionvi)

[StartRoutineByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_startroutinebylocalidentifiervi)

[StopDiagnosticSession.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_stopdiagnosticsessionvi)

[StopRoutineByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_stoproutinebylocalidentifiervi)

[TesterPresent.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_testerpresentvi)

[WriteDataByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_writedatabylocalidentifiervi)

[WriteMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_writememorybyaddressvi)

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=list-of-vis.html language=enus -->
## TOPIC 00044: List of VIs

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `list-of-vis.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/list-of-vis.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table is an alphabetical list of the Automotive Diagnostic Command Set VIs. Automotive Diagnostic Command Set API VIs for LabVIEW Function Purpose ClearDiagnosticInformation.vi Executes the ClearDiagnosticInformation service and clears selected Diagnostic Trouble Codes (DTCs). Close Di

### List of VIs

The following table is an alphabetical list of the Automotive Diagnostic Command Set VIs.

#### Automotive Diagnostic Command Set API VIs for LabVIEW

| Function | Purpose |
| --- | --- |
| ClearDiagnosticInformation.vi | Executes the ClearDiagnosticInformation service and clears selected Diagnostic Trouble Codes (DTCs). |
| Close Diagnostic.vi | Closes a diagnostic session. |
| ControlDTCSetting.vi | Executes the ControlDTCSetting service and modifies the generation behavior of selected Diagnostic Trouble Codes (DTCs). |
| Convert from Phys.vi | Converts a physical data value into a binary representation using a type descriptor. |
| Convert to Phys.vi | Converts a binary representation of a value into its physical value using a type descriptor. |
| Create Extended CAN IDs.vi | Creates diagnostic CAN IDs according to ISO 15765-2. |
| Diag Get Property.vi | Gets a diagnostic global internal parameter. |
| Diag Set Property.vi | Sets a diagnostic global internal parameter. |
| Diagnostic Frame Recv.vi | Receives a raw CAN frame on the diagnostic CAN ID to check for errors in the transport protocol implementation of an ECU. |
|  | Sends a raw CAN frame on the diagnostic CAN ID to check for errors in the transport protocol implementation of an ECU. |
| Diagnostic Service.vi | Executes a generic diagnostic service. If a special service is not available through the KWP2000, UDS, or OBD service functions, you can build it using this VI. |
| DisableNormalMessageTransmission.vi | Executes the DisableNormalMessageTransmission service. The ECU no longer transmits its regular communication messages (usually CAN messages). |
| DoIP Activate Routing.vi | Defines the source and target addresses for a DoIP TCP/IP connection. |
| DoIP Connect.vi | Creates a TCP/IP connection to a DoIP entity identified by its IP address. |
| DoIP Disconnect.vi | Disconnects the TCP/IP connection to a DoIP entity. |
| DoIP Get Diagnostic Power Mode.vi | Gets information on the DoIP entity power state. |
| DoIP Get DoIP Entity Status.vi | Gets status information from a DoIP entity. |
| DoIP Get Entities.vi | Returns a table of all DoIP entities (vehicles) on the local subnet, possibly restricted to EID or VIN. |
| DoIP Send Vehicle Identification Request.vi | Sends a UDP request to all DoIP-capable vehicles in the local subnet to identify themselves. |
| DoIP Send Vehicle Identification Request w EID.vi | Sends a UDP request to all DoIP-capable vehicles with a certain EID (MAC address) in the local subnet to identify themselves. |
| DoIP Send Vehicle Identification Request w VIN.vi | Sends a UDP request to all DoIP-capable vehicles with a certain VIN (Vehicle Identification Number) in the local subnet to identify themselves. |
| DTC to String.vi | Returns a string representation (such as P1234) for a 2-byte Diagnostic Trouble Code (DTC). |
| Get Time Stamp.vi | Gets timestamp information about the first/last send/received frame of the ISO TP for CAN and LIN. |
| ECUReset.vi | Executes the ECUReset service and resets the ECU. |
| EnableNormalMessageTransmission.vi | Executes the EnableNormalMessageTransmission service. The ECU starts transmitting its regular communication messages (usually CAN messages). |
| InputOutputControlByLocalIdentifier.vi | Executes the InputOutputControlByLocalIdentifier service. Modifies the ECU I/O port behavior. |
| OBD Clear Emission Related Diagnostic Information.vi | Executes the OBD Clear Emission Related Diagnostic Information service. Clears emission-related Diagnostic Trouble Codes (DTCs) in the ECU. |
| OBD Open on CAN FD.vi | Opens an OBD-II diagnostic session on a CAN port. |
| OBD Request Control Of On-Board Device.vi | Executes the OBD Request Control Of On-Board Device service. Use this VI to modify ECU I/O port behavior. |
| OBD Request Current Powertrain Diagnostic Data.vi | Executes the OBD Request Current Powertrain Diagnostic Data service. Reads a data record from the ECU. |
| OBD Request Emission Related DTCs.vi | Executes the OBD Request Emission Related DTCs service. Reads all emission-related Diagnostic Trouble Codes (DTCs). |
| OBD Request Emission Related DTCs During Current Drive Cycle.vi | Executes the OBD Request Emission Related DTCs During Current Drive Cycle service. Reads the emission-related Diagnostic Trouble Codes (DTCs) that occurred during the current (or last completed) drive cycle. |
| OBD Request On-Board Monitoring Test Results.vi | Executes the OBD Request On-Board Monitoring Test Results service. Reads a test data record from the ECU. |
| OBD Request Permanent Fault Codes.vi | Executes the OBD Request Permanent Fault Codes service. All permanent Diagnostic Trouble Codes (DTCs) are read. |
| OBD Request Powertrain Freeze Frame Data.vi | Executes the OBD Request Powertrain Freeze Frame Data service. Reads a data record from the ECU that has been stored while a Diagnostic Trouble Code occurred. |
| OBD Request Supported PIDs.vi | Executes the OBD Request Current Powertrain Diagnostic Data service to retrieve the valid PID values for this service. |
| OBD Request Vehicle Information.vi | Executes the OBD Request Vehicle Information service. Reads a set of information data from the ECU. |
| Open Diagnostic on CAN FD.vi | Opens a diagnostic session on a CAN port. Communication to the ECU is not yet started. |
| Open Diagnostic on IP.vi | Opens a diagnostic session on an IP port. Communication to the ECU is not yet started. |
| Open Diagnostic on LIN.vi | Opens a diagnostic session on an NI-XNET LIN port. Communication to the ECU is not yet started. |
| ReadDataByLocalIdentifier.vi | Executes the ReadDataByLocalIdentifier service. Reads a data record from the ECU. |
| ReadDTCByStatus.vi | Executes the ReadDiagnosticTroubleCodesByStatus service. Reads selected Diagnostic Trouble Codes (DTCs). |
| ReadECUIdentification.vi | Executes the ReadECUIdentification service. Returns ECU identification data from the ECU. |
| ReadMemoryByAddress.vi | Executes the ReadMemoryByAddress service. Reads data from the ECU memory. |
| ReadStatusOfDTC.vi | Executes the ReadStatusOfDiagnosticTroubleCodes service. Reads selected Diagnostic Trouble Codes (DTCs). |
| RequestRoutineResultsByLocalIdentifier.vi | Executes the RequestRoutineResultsByLocalIdentifier service. Returns results from a routine on the ECU. |
| RequestSeed.vi | Executes the SecurityAccess service to retrieve a seed from the ECU. |
| SendKey.vi | Executes the SecurityAccess service to send a key to the ECU. |
| StartDiagnosticSession.vi | Executes the StartDiagnosticSession service. Sets up the ECU in a specific diagnostic mode. |
| Start Periodic TesterPresent.vi | Starts a background thread for the current diagnostic session that periodically transmits a TesterPresent message. |
| StartRoutineByLocalIdentifier.vi | Executes the StartRoutineByLocalIdentifier service. Executes a routine on the ECU. |
| StopDiagnosticSession.vi | Executes the StopDiagnosticSession service. Brings the ECU back in normal mode. |
| Stop Periodic TesterPresent.vi | Terminates automatic transmission of a periodic TesterPresent message. |
| StopRoutineByLocalIdentifier.vi | Executes the StopRoutineByLocalIdentifier service. Stops a routine on the ECU. |
| TesterPresent.vi | Executes the TesterPresent service. Keeps the ECU in diagnostic mode. |
| UDS ClearDiagnosticInformation.vi | Executes the UDS ClearDiagnosticInformation service. Clears selected Diagnostic Trouble Codes (DTCs). |
| UDS CommunicationControl.vi | Executes the UDS CommunicationControl service. Use this VI to switch on or off transmission and/or reception of the normal communication messages (usually CAN messages). |
| UDS ControlDTCSetting.vi | Executes the UDS ControlDTCSetting service. Modifies Diagnostic Trouble Code (DTC) generation behavior. |
| UDS DiagnosticSessionControl.vi | Executes the UDS DiagnosticSessionControl service. Sets up the ECU in a specific diagnostic mode. |
| UDS ECUReset.vi | Executes the UDS ECUReset service. Resets the ECU. |
| UDS InputOutputControlByIdentifier.vi | Executes the UDS InputOutputControlByIdentifier service. Use this VI to modify ECU I/O port behavior. |
| UDS ReadDataByIdentifier.vi | Executes the UDS ReadDataByIdentifier service. Reads a data record from the ECU. |
| UDS ReadMemoryByAddress.vi | Executes the UDS ReadMemoryByAddress service. Reads data from the ECU memory. |
| UDS ReportDTCBySeverityMaskRecord.vi | Executes the ReportDTCBySeverityMaskRecord subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs). |
| UDS ReportDTCByStatusMask.vi | Executes the ReportDTCByStatusMask subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs). |
| UDS ReportSeverityInformationOfDTC.vi | Executes the ReportSeverityInformationOfDTC subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs). |
| UDS ReportSupportedDTCs.vi | Executes the ReportSupportedDTCs subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads all supported Diagnostic Trouble Codes (DTCs). |
| UDS RequestDownload.vi | Initiates a download of data to the ECU. |
| UDS RequestSeed.vi | Executes the UDS SecurityAccess service to retrieve a seed from the ECU. |
| UDS RequestTransferExit.vi | Terminates a download/upload process. |
| UDS RequestUpload.vi | Initiates an upload of data from the ECU. |
| UDS RoutineControl.vi | Executes the UDS RoutineControl service. Executes a routine on the ECU. |
| UDS SendKey.vi | Executes the SecurityAccess service to send a key to the ECU. |
| UDS TesterPresent.vi | Executes the UDS TesterPresent service. Keeps the ECU in diagnostic mode. |
| UDS TransferData.vi | Transfers data to/from the ECU in a download/upload process. |
| UDS WriteDataByIdentifier.vi | Executes the UDS WriteDataByIdentifier service. Writes a data record to the ECU. |
| UDS WriteMemoryByAddress.vi | Executes the UDS WriteMemoryByAddress service. Writes data to the ECU memory. |
| UDS06 ReadMemoryByAddress.vi | Executes the UDS ReadMemoryByAddress service. Reads data from the ECU memory. |
| UDS06 WriteMemoryByAddress.vi | Executes the UDS WriteMemoryByAddress service. Writes data to the ECU memory. |
| VWTP Connect.vi | Establishes a connection channel to an ECU using the VW TP 2.0. |
| VWTP Connection Test.vi | Maintains a connection channel to an ECU using the VW TP 2.0. |
| VWTP Disconnect.vi | Terminates a connection channel to an ECU using the VW TP 2.0. |
| WriteDataByLocalIdentifier.vi | Executes the WriteDataByLocalIdentifier service. Writes a data record to the ECU. |
| WriteMemoryByAddress.vi | Executes the WriteMemoryByAddress service. Writes data to the ECU memory. |
| WWH-OBD Clear Emission Related DTCs.vi | Executes the WWH-OBD ClearDiagnosticInformation service. Clears selected Diagnostic Trouble Codes (DTCs). |
| WWH-OBD Convert DTCs to J1939.vi | Converts DTCs to the J1939 DTC format. |
| WWH-OBD Convert DTCs to J2012.vi | Converts DTCs to the J2012 DTC format. |
| WWH-OBD Request DID.vi | Executes the WWH-OBD ReadDataByIdentifier service. Reads a data record from the ECU. |
| WWH-OBD Request DTC Extended Data Record.vi | Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs). |
| WWH-OBD Request Emission Related DTCs.vi | Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs). |
| WWH-OBD Request Freeze Frame Information.vi | Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs). |
| WWH-OBD Request RID.vi | Executes the WWH-OBD RoutineControl service. Reads a data record from the ECU. |
| WWH-OBD Request Supported DIDs.vi | Executes the WWH-OBD ReadDataByIdentifier service to retrieve the valid DID values for this service. |
| WWH-OBD Request Supported RIDs.vi | Executes the WWH-OBD RoutineControl service to retrieve the valid RID values for this service. |

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=measurements.html language=enus -->
## TOPIC 00045: Measurements

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `measurements.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/measurements.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the ReadDataByLocal/CommonIdentifier services to access ECU data in a way similar to a DAQ list. A Local/CommonIdentifier describes a list of ECU quantities that are then transferred from the ECU to the tester. The transfer can be either single value or periodic, with a slow, medium, or fast tra

### Measurements

Note

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-clear-emission-related-diagnostic-informa.html language=enus -->
## TOPIC 00046: OBD Clear Emission Related Diagnostic Information.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-clear-emission-related-diagnostic-informa.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-clear-emission-related-diagnostic-informa.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Clear Emission Related Diagnostic Information service. Clears emission-related Diagnostic Trouble Codes (DTCs) in the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs

### OBD Clear Emission Related Diagnostic Information.vi

Purpose

Executes the OBD Clear Emission Related Diagnostic Information service. Clears
emission-related Diagnostic Trouble Codes (DTCs) in the ECU.
Format

[IMAGE alt='image' src='images/OBDClearEmissionRelatedDiagnosticInformationVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-on-board-diagnostic-services2.html language=enus -->
## TOPIC 00047: OBD (On-Board Diagnostic) Services

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-on-board-diagnostic-services2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-on-board-diagnostic-services2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: OBD Clear Emission Related Diagnostic Information.vi OBD Request Control Of On-Board Device.vi OBD Request Current Powertrain Diagnostic Data.vi OBD Request Emission Related DTCs During Current Drive Cycle.vi OBD Request Emission Related DTCs.vi OBD Request On-Board Monitoring Test Results.vi OBD Re

### OBD (On-Board Diagnostic) Services

[OBD Clear Emission Related Diagnostic Information.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdclearemissionrelateddiagnosticinformationvi)

[OBD Request Control Of On-Board Device.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestcontrolofonboarddevicevi)

[OBD Request Current Powertrain Diagnostic Data.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestcurrentpowertraindiagnosticdatavi)

[OBD Request Emission Related DTCs During Current Drive Cycle.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestemissionrelateddtcsduringcurrentdrivecyclevi)

[OBD Request Emission Related DTCs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestemissionrelateddtcsvi)

[OBD Request On-Board Monitoring Test Results.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestonboardmonitoringtestresultsvi)

[OBD Request Permanent Fault Codes.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestpermanentfaultcodesvi)

[OBD Request Powertrain Freeze Frame Data.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestpowertrainfreezeframedatavi)

[OBD Request Supported PIDs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestsupportedpidsvi)

[OBD Request Vehicle Information.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_obdrequestvehicleinformationvi)

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-on-board-diagnostic.html language=enus -->
## TOPIC 00048: OBD (On-Board Diagnostic)

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-on-board-diagnostic.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-on-board-diagnostic.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: On-Board Diagnostic (OBD) systems are present in most cars and light trucks on the road today. On-Board Diagnostics refer to the vehicle's self-diagnostic and reporting capability, which the vehicle owner or a repair technician can use to query status information for various vehicle subsystems. The

### OBD (On-Board Diagnostic)

On-Board Diagnostic (OBD) systems are present in most cars and light trucks on the road today. On-Board Diagnostics refer to the vehicle's self-diagnostic and reporting capability, which the vehicle owner or a repair technician can use to query status information for various vehicle subsystems.

The amount of diagnostic information available via OBD has increased since the introduction of on-board vehicle computers in the early 1980s. Modern OBD implementations use a CAN communication port to provide real-time data and a standardized series of diagnostic trouble codes (DTCs), which identify and remedy malfunctions within the vehicle. In the 1970s and early 1980s, manufacturers began using electronic means to control engine functions and diagnose engine problems. This was primarily to meet EPA emission standards. Through the years, on-board diagnostic systems have become more sophisticated. OBD-II, a standard introduced in the mid 1990s, provides almost complete engine control and also monitors parts of the chassis, body, and accessory devices, as well as the car's diagnostic control network. The newest standard was introduced in 2012 as WWH-OBD.

The On-Board Diagnostic (OBD) standard defines a minimum set of diagnostic information for passenger cars and light and medium-duty trucks, which must be exchanged with any off-board test equipment.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-open-on-can-fd-vi.html language=enus -->
## TOPIC 00049: OBD Open on CAN FD.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-open-on-can-fd-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-open-on-can-fd-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Opens an OBD-II diagnostic session on a CAN or CAN FD port. Format Input Max DLC is the maximum CAN frame length to be used in CAN FD diagnostic communication. Allowed values are 8, 12, 16, 20, 24, 32, 48, and 64. For an IO Mode of CAN 2.0, this setting is ignored and a value of 8 is used. F

### OBD Open on CAN FD.vi

Purpose

Opens an OBD-II diagnostic session on a CAN or CAN FD port.
Format

[IMAGE alt='image' src='images/OBDOpenOnCANFDVI.gif']
Input

|  | Max DLC is the maximum CAN frame length to be used in CAN FD diagnostic communication. Allowed values are 8, 12, 16, 20, 24, 32, 48, and 64. For an IO Mode of CAN 2.0, this setting is ignored and a value of 8 is used. For the CAN FD settings of the IO Mode, this limits the frame size for transmission of diagnostic requests. The receive data length is determined from the incoming messages and not limited by this value. |  |
| --- | --- | --- |
|  | CAN interface specifies the CAN interface on which the diagnostic communication should take place. NI-CAN The CAN interface is the name of the NI-CAN Network Interface Object to configure. This name uses the syntax CANx, where x is a decimal number starting at 0 that indicates the CAN network interface (CAN0, CAN1, up to CAN63). CAN network interface names are associated with physical CAN ports using Measurement and Automation Explorer (MAX). NI-XNET By default, the Automotive Diagnostic Command Set uses NI-CAN for CAN communication. This means you must define an NI-CAN interface for your NI-XNET hardware (NI-CAN compatibility mode) to use your XNET hardware for CAN communication. However, to use your NI-XNET interface in the native NI-XNET mode (meaning it does not use the NI-XNET Compatibility Layer), you must define your interface under NI-XNET Devices in MAX and pass the NI-XNET interface name that the Automotive Diagnostic Command Set will use. To do this, add @nixnet to the protocol string (for example, CAN1@nixnet). The interface name is related to the NI-XNET hardware naming under Devices and Interfaces in MAX. Note Â Â By selecting nixnet as the interface string, the Automotive Diagnostic Command Set uses the Frame Input and Output Queued sessions. To force the use of Frame Input and Output Stream sessions instead, select ni_genie_nixnet as the interface string (for example, CAN1@ni_genie_nixnet). An application instance can use only one Frame Input Stream Session and one Frame Output Stream Session at a time, so use the default name nixnet as the interface string, so that multiple NI-XNET Frame Queued Sessions can coexist on a single interface, and the Frame Input and Output Stream Sessions may be used, for example, for a Frame logging/replay use case. CompactRIO or R Series If using CompactRIO or R Series hardware, you must provide a bitfile that handles the CAN communication between the host system and FPGA. To access the CAN module on the FPGA, you must specify the bitfile name after the @ (for example, CAN1@MyBitfile.lvbitx). To specify a special RIO target, you can specify that target by its name followed by the bitfile name (for example, CAN1@RIO1,MyBitfile.lvbitx). RIO1 defines the RIO target name as defined in your LabVIEW Project definition. The lvbitx filename represents the filename and location of the bitfile on the host if using RIO or on a CompactRIO target. This implies that you must download the bitfile to the CompactRIO target before you can run your application. You may specify an absolute path or a path relative to the root of your target for the bitfile. |  |
|  | baudrate is the diagnostic communication baud rate. You can wire standard baud rates as well as custom 64-bit baud rates to this control. For more information on 64-bit nonstandard baud rates, refer to the NI-XNET Hardware and Software Help. You can use the NI-XNET Bus Monitor and NI-XNET Database Editor utilities to create a custom baud rate. Refer to NI-XNET Tools and Utilities Help and NI-XNET Hardware and Software Help for more information about creating a custom baud rate. |  |
|  | FD baudrate is the diagnostic communication FD baud rate for the CAN FD+BRS IO Mode. You can wire standard FD baud rates as well as custom 64-bit baud rates to this control. For more information on 64-bit nonstandard FD baud rates, refer to the NI-XNET Hardware and Software Help. You can use the NI-XNET Bus Monitor and NI-XNET Database Editor utilities to create a custom FD baud rate. Refer to NI-XNET Tools and Utilities Help and NI-XNET Hardware and Software Help for more information about creating a custom FD baud rate. |  |
|  | IO Mode is the CAN I/O Mode to be used for the diagnostic communication. Choices are: 0CAN 2.0Traditional 8 byte CAN 2.0 frames.1CAN FDCAN FD frames with up to 64 bytes.2CAN FD+BRSCAN FD frames with up to 64 bytes, but with a higher baud rate used for transferring the data and checksum bytes.3ECU DeterminedThe IO Mode that is actually used is determined from the first response of the ECU. The first request to the ECU is sent in CAN 2.0 mode; if the ECU responds in any mode, this mode is selected for further communication. If the ECU does not respond (timeout), ADCS retries the request in the other modes. If none succeeds, the timeout error is returned to the user. After the communication has started, the IO Mode that is actually used can be determined from reading the Actual CAN IO Mode property. Note Â Â The CAN FD features are only supported with NI-XNET version 17.0.1 or later. |  |
| 0 | CAN 2.0 | Traditional 8 byte CAN 2.0 frames. |
| 1 | CAN FD | CAN FD frames with up to 64 bytes. |
| 2 | CAN FD+BRS | CAN FD frames with up to 64 bytes, but with a higher baud rate used for transferring the data and checksum bytes. |
| 3 | ECU Determined | The IO Mode that is actually used is determined from the first response of the ECU. The first request to the ECU is sent in CAN 2.0 mode; if the ECU responds in any mode, this mode is selected for further communication. If the ECU does not respond (timeout), ADCS retries the request in the other modes. If none succeeds, the timeout error is returned to the user. After the communication has started, the IO Mode that is actually used can be determined from reading the Actual CAN IO Mode property. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |  |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |  |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |  |
|  | source identifies the VI where the error occurred. |  |
|  | transmit ID is the CAN identifier for sending diagnostic request messages from the host to the ECU. To specify an extended (29-bit) ID, OR the value with 0x20000000. The default setting is -1 which tries out the legislated OBD 11-bit and 29-bit CAN identifiers and opens the first matching setting. |  |
|  | receive ID is the CAN identifier or sending diagnostic response messages from the ECU to the host. To specify an extended (29-bit) ID, OR the value with 0x20000000. The default setting is -1 which tries out the legislated OBD 11-bit and 29-bit CAN identifiers and opens the first matching setting. |  |

Output

|  | diag ref out is a cluster containing all necessary diagnostic session information. Wire this cluster as a handle to all subsequent diagnostic VIs and close it using Close Diagnostic.vi. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

Use this VI to open a diagnostic communication channel to an ECU for OBD-II. The CAN port specified as input is initialized and a handle to it is stored (among other internal data) in the **diag ref out** cluster, which serves as reference for further diagnostic functions.

Possible examples of selections for the interface parameter for the various hardware targets are as follows.

Using NI-CAN hardware:

- CAN0 âuses CAN interface 0.
- CAN1 âuses CAN interface 1 and so on with the form CANx .
- CAN256 âuses virtual NI-CAN interface 256.

Using NI-XNET hardware with NI-XNET Frame Input/Output-based sessions:

- CAN1@nixnet âuses CAN interface 1 of an NI-XNET device.
- CAN2@nixnet âuses CAN interface 2 of an NI-XNET device and so on with the form CANx .

Using NI-XNET hardware with NI-XNET Stream Input/Output-based sessions:

- CAN1@ni_genie_nixnet âuses CAN interface 1 of an NI-XNET device.
- CAN2@ni_genie_nixnet âuses CAN interface 2 of an NI-XNET device and so on with the form CANx .

Using R Series:

- CAN1@RIO1, c:\temp\MyFpgaBitfile.lvbitx âuses a named target RIO1 as compiled into the bitfile at location c:\temp\MyFpgaBitfile.lvbitx .

Using CompactRIO

- CAN1@/MyFpgaBitfile.lvbitx âuses compiled bitfile MyFpgaBitfile.lvbitx , which must be FTP copied to the root of the CompactRIO target.

First, communication to the ECU is tried on the default 11-bit OBD CAN identifiers; if that fails, the default 29-bit OBD CAN identifiers are tried. If that also fails, the VI returns an error.

You can overwrite the default OBD CAN identifiers optionally with any other identifiers.

In general, it is not necessary to manipulate the **diag ref out** cluster contents.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-control-of-on-board-device-vi.html language=enus -->
## TOPIC 00050: OBD Request Control Of On-Board Device.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-control-of-on-board-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-control-of-on-board-device-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Control Of On-Board Device service. Modifies ECU I/O port behavior. Format Input data in defines application-specific data for this service. diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent d

### OBD Request Control Of On-Board Device.vi

Purpose

Executes the OBD Request Control Of On-Board Device service. Modifies ECU I/O port
behavior.
Format

[IMAGE alt='image' src='images/OBDRequestControlofOnBoardDeviceVI.gif']
Input

|  | data in defines application-specific data for this service. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | TID defines the test identifier of the I/O to be manipulated. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific data for this service. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-current-powertrain-diagnostic-dat.html language=enus -->
## TOPIC 00051: OBD Request Current Powertrain Diagnostic Data.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-current-powertrain-diagnostic-dat.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-current-powertrain-diagnostic-dat.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Current Powertrain Diagnostic Data service. Reads a data record from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to ma

### OBD Request Current Powertrain Diagnostic Data.vi

Purpose

Executes the OBD Request Current Powertrain Diagnostic Data service. Reads a data record
from the ECU.
Format

[IMAGE alt='image' src='images/OBDRequestCurrentPowertrainDiagnosticDataVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | PID defines the parameter identifier of the data to be read. The SAE J1979 standard defines the values. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU data record. If you know the record data description, you can use Convert from Phys.vi to generate this record. You can obtain the description from the SAE J1979 standard. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-emission-related-dtcs-during-curr.html language=enus -->
## TOPIC 00052: OBD Request Emission Related DTCs During Current Drive Cycle.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-emission-related-dtcs-during-curr.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-emission-related-dtcs-during-curr.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Emission Related DTCs During Current Drive Cycle service. Reads the emission-related Diagnostic Trouble Codes (DTCs) that occurred during the current (or last completed) drive cycle. Format Input DTC descriptor is a cluster that describes the DTC records the ECU deli

### OBD Request Emission Related DTCs During Current Drive Cycle.vi

Purpose

Executes the OBD Request Emission Related DTCs During Current Drive Cycle service. Reads the emission-related Diagnostic Trouble Codes (DTCs) that occurred during the current (or last completed) drive cycle.
Format

[IMAGE alt='image' src='images/OBDRequestEmissionRelatedDTCsDuringCurrentDriveCycleVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 0 for OBD.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 0 for OBD. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information.Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information. |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-emission-related-dtcs-vi.html language=enus -->
## TOPIC 00053: OBD Request Emission Related DTCs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-emission-related-dtcs-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-emission-related-dtcs-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Emission Related DTCs service. Reads all emission-related Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default

### OBD Request Emission Related DTCs.vi

Purpose

Executes the OBD Request Emission Related DTCs service. Reads all emission-related
Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/OBDRequestEmissionRelatedDTCsVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 0 for OBD.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 0 for OBD. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information.Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information. |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-on-board-monitoring-test-results.html language=enus -->
## TOPIC 00054: OBD Request On-Board Monitoring Test Results.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-on-board-monitoring-test-results.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-on-board-monitoring-test-results.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request On-Board Monitoring Test Results service. Reads a test data record from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to

### OBD Request On-Board Monitoring Test Results.vi

Purpose

Executes the OBD Request On-Board Monitoring Test Results service. Reads a test data
record from the ECU.
Format

[IMAGE alt='image' src='images/OBDRequestOnBoardMonitoringTestResultsVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | OBDMID defines the parameter identifier of the data to be read. The SAE J1979 standard defines the values. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU data record. If you know the record data description, you can use Convert from Phys.vi to generate this record. You can obtain the description from the SAE J1979 standard. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-permanent-fault-codes-vi.html language=enus -->
## TOPIC 00055: OBD Request Permanent Fault Codes.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-permanent-fault-codes-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-permanent-fault-codes-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Permanent Fault Codes service. All permanent Diagnostic Trouble Codes (DTCs) are read. Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2

### OBD Request Permanent Fault Codes.vi

Purpose

Executes the OBD Request Permanent Fault Codes service. All permanent Diagnostic Trouble Codes (DTCs) are read.
Format

[IMAGE alt='image' src='images/OBDRequestPermanentFaultCodesVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 0 for OBD.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 0 for OBD. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information.Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information. |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-powertrain-freeze-frame-data-vi.html language=enus -->
## TOPIC 00056: OBD Request Powertrain Freeze Frame Data.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-powertrain-freeze-frame-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-powertrain-freeze-frame-data-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Powertrain Freeze Frame Data service. Reads an ECU data record stored while a Diagnostic Trouble Code occurred. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. N

### OBD Request Powertrain Freeze Frame Data.vi

Purpose

Executes the OBD Request Powertrain Freeze Frame Data service. Reads an ECU data record
stored while a Diagnostic Trouble Code occurred.
Format

[IMAGE alt='image' src='images/OBDRequestPowertrainFreezeFrameDataVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | PID defines the parameter identifier of the data to be read. The SAE J1979 standard defines the values. |
|  | # frame is the number of the freeze frame from which the data are to be retrieved. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU data record. If you know the record data description, you can use Convert from Phys.vi to generate this record. You can obtain the description from the SAE J1979 standard. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-supported-pids-vi.html language=enus -->
## TOPIC 00057: OBD Request Supported PIDs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-supported-pids-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-supported-pids-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Current Powertrain Diagnostic Data service to retrieve the valid PID values for this service. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not

### OBD Request Supported PIDs.vi

Purpose

Executes the OBD Request Current Powertrain Diagnostic Data service to retrieve the valid PID values for this service.
Format

[IMAGE alt='image' src='images/OBDRequestSupportedPIDsVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | PIDs out returns an array of valid PIDs for the OBD Request Current Powertrain Diagnostic Data service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=obd-request-vehicle-information-vi.html language=enus -->
## TOPIC 00058: OBD Request Vehicle Information.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `obd-request-vehicle-information-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/obd-request-vehicle-information-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the OBD Request Vehicle Information service. Reads a set of information data from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manua

### OBD Request Vehicle Information.vi

Purpose

Executes the OBD Request Vehicle Information service. Reads a set of information data from the ECU.
Format

[IMAGE alt='image' src='images/OBDRequestVehicleInformationVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | info type defines the type of information to be read. The values are defined in the SAE J1979 standard. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the vehicle information from the ECU. You can obtain the description from the SAE J1979 standard. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | # items is the number of data tiems (not bytes) this service returns. |

Parent topic:

OBD (On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=open-diagnostic-on-can-fd-vi.html language=enus -->
## TOPIC 00059: Open Diagnostic on CAN FD.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `open-diagnostic-on-can-fd-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/open-diagnostic-on-can-fd-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Opens a diagnostic session on a CAN or CAN FD port. Communication to the ECU is not yet started. Format Input Max DLC is the maximum CAN frame length to be used in CAN FD diagnostic communication. Allowed values are 8, 12, 16, 20, 24, 32, 48, and 64. For an IO Mode of CAN 2.0, this setting i

### Open Diagnostic on CAN FD.vi

Purpose

Opens a diagnostic session on a CAN or CAN FD port. Communication to the ECU is not yet started.
Format

[IMAGE alt='image' src='images/OpenDiagnosticOnCANFDVI.gif']
Input

|  | Max DLC is the maximum CAN frame length to be used in CAN FD diagnostic communication. Allowed values are 8, 12, 16, 20, 24, 32, 48, and 64. For an IO Mode of CAN 2.0, this setting is ignored and a value of 8 is used. For the CAN FD settings of the IO Mode, this limits the frame size for transmission of diagnostic requests. The receive data length is determined from the incoming messages and not limited by this value. |  |
| --- | --- | --- |
|  | CAN interface specifies the CAN interface on which the diagnostic communication should take place. NI-CAN The CAN interface is the name of the NI-CAN Network Interface Object to configure. This name uses the syntax CANx, where x is a decimal number starting at 0 that indicates the CAN network interface (CAN0, CAN1, up to CAN63). CAN network interface names are associated with physical CAN ports using Measurement and Automation Explorer (MAX). NI-XNET By default, the Automotive Diagnostic Command Set uses NI-CAN for CAN communication. This means you must define an NI-CAN interface for your NI-XNET hardware (NI-CAN compatibility mode) to use your XNET hardware for CAN communication. However, to use your NI-XNET interface in the native NI-XNET mode (meaning it does not use the NI-XNET Compatibility Layer), you must define your interface under NI-XNET Devices in MAX and pass the NI-XNET interface name that the Automotive Diagnostic Command Set will use. To do this, add @nixnet to the protocol string (for example, CAN1@nixnet). The interface name is related to the NI-XNET hardware naming under Devices and Interfaces in MAX. Note Â Â By selecting nixnet as the interface string, the Automotive Diagnostic Command Set uses the Frame Input and Output Queued sessions. To force the use of Frame Input and Output Stream sessions instead, select ni_genie_nixnet as the interface string (for example, CAN1@ni_genie_nixnet). An application instance can use only one Frame Input Stream Session and one Frame Output Stream Session at a time, so use the default name nixnet as the interface string, so that multiple NI-XNET Frame Queued Sessions can coexist on a single interface, and the Frame Input and Output Stream Sessions may be used, for example, for a Frame logging/replay use case. CompactRIO or R Series If using CompactRIO or R Series hardware, you must provide a bitfile that handles the CAN communication between the host system and FPGA. To access the CAN module on the FPGA, you must specify the bitfile name after the @ (for example, CAN1@MyBitfile.lvbitx). To specify a special RIO target, you can specify that target by its name followed by the bitfile name (for example, CAN1@RIO1,MyBitfile.lvbitx). RIO1 defines the RIO target name as defined in your LabVIEW Project definition. The lvbitx filename represents the filename and location of the bitfile on the host if using RIO or on a CompactRIO target. This implies that you must download the bitfile to the CompactRIO target before you can run your application. You may specify an absolute path or a path relative to the root of your target for the bitfile. |  |
|  | baudrate is the diagnostic communication baud rate. You can wire standard baud rates as well as custom 64-bit baud rates to this control. For more information on 64-bit nonstandard baud rates, refer to the NI-XNET Hardware and Software Help. You can use the NI-XNET Bus Monitor and NI-XNET Database Editor utilities to create a custom baud rate. Refer to NI-XNET Tools and Utilities Help and NI-XNET Hardware and Software Help for more information about creating a custom baud rate. |  |
|  | FD baudrate is the diagnostic communication FD baud rate for the CAN FD+BRS IO Mode. You can wire standard FD baud rates as well as custom 64-bit baud rates to this control. For more information on 64-bit nonstandard FD baud rates, refer to the NI-XNET Hardware and Software Help. You can use the NI-XNET Bus Monitor and NI-XNET Database Editor utilities to create a custom FD baud rate. Refer to NI-XNET Tools and Utilities Help and NI-XNET Hardware and Software Help for more information about creating a custom FD baud rate. |  |
|  | IO Mode is the CAN I/O Mode to be used for the diagnostic communication. Choices are: 0CAN 2.0Traditional 8 byte CAN 2.0 frames.1CAN FDCAN FD frames with up to 64 bytes.2CAN FD+BRSCAN FD frames with up to 64 bytes, but with a higher baud rate used for transferring the data and checksum bytes.3ECU DeterminedThe IO Mode that is actually used is determined from the first response of the ECU. The first request to the ECU is sent in CAN 2.0 mode; if the ECU responds in any mode, this mode is selected for further communication. If the ECU does not respond (timeout), ADCS retries the request in the other modes. If none succeeds, the timeout error is returned to the user. After the communication has started, the IO Mode that is actually used can be determined from reading the Actual CAN IO Mode property. Note Â Â The CAN FD features are only supported with NI-XNET version 17.0.1 or later. |  |
| 0 | CAN 2.0 | Traditional 8 byte CAN 2.0 frames. |
| 1 | CAN FD | CAN FD frames with up to 64 bytes. |
| 2 | CAN FD+BRS | CAN FD frames with up to 64 bytes, but with a higher baud rate used for transferring the data and checksum bytes. |
| 3 | ECU Determined | The IO Mode that is actually used is determined from the first response of the ECU. The first request to the ECU is sent in CAN 2.0 mode; if the ECU responds in any mode, this mode is selected for further communication. If the ECU does not respond (timeout), ADCS retries the request in the other modes. If none succeeds, the timeout error is returned to the user. After the communication has started, the IO Mode that is actually used can be determined from reading the Actual CAN IO Mode property. |
|  | transport protocol specifies the transport protocol for transferring the diagnostic service messages over the CAN network. The following values are valid and can be obtained through an enum control: 0ISO TPâNormal Mode: The ISO TP as specified in ISO 15765-2 is used; all eight data bytes of the CAN messages are used for data transfer.1ISO TPâMixed Mode: The ISO TP as specified in ISO 15765-2 is used; the first data byte is used as address extension.2VW TP 2.0 |  |
| 0 | ISO TPâNormal Mode: The ISO TP as specified in ISO 15765-2 is used; all eight data bytes of the CAN messages are used for data transfer. |  |
| 1 | ISO TPâMixed Mode: The ISO TP as specified in ISO 15765-2 is used; the first data byte is used as address extension. |  |
| 2 | VW TP 2.0 |  |
|  | transmit ID is the CAN identifier for sending diagnostic request messages from the host to the ECU. To specify an extended (29-bit) ID, OR the value with 0x20000000. |  |
|  | receive ID is the CAN identifier or sending diagnostic response messages from the ECU to the host. To specify an extended (29-bit) ID, OR the value with 0x20000000. |  |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |  |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |  |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |  |
|  | source identifies the VI where the error occurred. |  |

Output

|  | diag ref out is a cluster containing all necessary diagnostic session information. Wire this cluster as a handle to all subsequent diagnostic VIs and close it using Close Diagnostic.vi. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**Open Diagnostic on CAN FD.vi** opens a diagnostic communication channel to an ECU. The CAN port specified as input is initialized, and a handle to it is stored (among other internal data) in the **diag ref out** cluster, which serves as reference for further diagnostic functions.

Possible examples of selections for the interface parameter for the various hardware targets are as follows.

Using NI-CAN hardware:

- CAN0 âuses CAN interface 0.
- CAN1 âuses CAN interface 1 and so on with the form CANx .
- CAN256 âuses virtual NI-CAN interface 256.
- CAN257 âuses virtual NI-CAN interface 257.

Using NI-XNET hardware with NI-XNET Frame Input/Output-based sessions:

- CAN1@nixnet âuses CAN interface 1 of an NI-XNET device.
- CAN2@nixnet âuses CAN interface 2 of an NI-XNET device and so on with the form CANx .

Using NI-XNET hardware with NI-XNET Stream Input/Output-based sessions:

- CAN1@ni_genie_nixnet âuses CAN interface 1 of an NI-XNET device.
- CAN2@ni_genie_nixnet âuses CAN interface 2 of an NI-XNET device and so on with the form CANx .

Using R Series:

- CAN1@RIO1, c:\temp\MyFpgaBitfile.lvbitx âuses a named target RIO1 as compiled into the bitfile at c:\temp\MyFpgaBitfile.lvbitx .

Using CompactRIO

- CAN1@/MyFpgaBitfile.lvbitx âuses compiled bitfile MyFpgaBitfile.lvbitx , which must be FTP copied to the root of the CompactRIO target.

Note

StartDiagnosticSession.vi

UDS DiagnosticSessionControl.vi

In general, it is not necessary to manipulate the **diag ref out** cluster contents, with one notable exception: If you use the **ISO TPâMixed Mode** transport protocol, you must store the address extensions for transmit and receive in the appropriate cluster members.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=open-diagnostic-on-ip-vi.html language=enus -->
## TOPIC 00060: Open Diagnostic on IP.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `open-diagnostic-on-ip-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/open-diagnostic-on-ip-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Opens a diagnostic session on an IP port. Communication to the ECU is not yet started. Format Input protocol version is the protocol version of the DoIP packets: 12010 — Initial draft version DoIP ISO/DIS 13400:2:201022012 — Official released version DoIP ISO 13400-2:2012 If protocol version

### Open Diagnostic on IP.vi

Purpose

Opens a diagnostic session on an IP port. Communication to the ECU is not yet started.
Format

[IMAGE alt='image' src='images/OpenDiagnosticonIPVI.gif']
Input

|  | protocol version is the protocol version of the DoIP packets: 12010 — Initial draft version DoIP ISO/DIS 13400:2:201022012 — Official released version DoIP ISO 13400-2:2012 If protocol version is set to 2010, the protocol version byte of the Generic DoIP header is set to 1. If protocol version is set to 2012, the protocol version byte of the Generic DoIP header is set to 2. The default is 2010. The protocol versions used by the ECU and Automotive Diagnostic Command Set applications must match or a Generic Header error will be issued. |
| --- | --- |
| 1 | 2010 — Initial draft version DoIP ISO/DIS 13400:2:2010 |
| 2 | 2012 — Official released version DoIP ISO 13400-2:2012 |
|  | dynamic port defines whether a dynamically assigned UDP source port is used (TRUE, default). If set to FALSE, the port set as local static port will be used. |
|  | local static port defines the source UDP port to use when dynamic port is set to FALSE. Default is 13401. |
|  | XNET IP stack name specifies the name of the XNET IP Stack to use for IP communication by this diagnostic session. This IP stack must be started beforehand, refer to NI-XNET Hardware and Software Help for information about creating and configuring an XNET IP Stack. You can wire the XNET IP Stack reference directly to this input. This VI will wait for the IP stack and all of its virtual interfaces to become ready. If this parameter is not set, the native operating system IP stack will be used. |
|  | XNET local interface specifies the local interface to use for this diagnostic session on the specified XNET IP Stack; used when the XNET IP Stack contains multiple virtual interfaces. This optional parameter can be omitted if the IP Stack has only one local interface. This property is ignored if the XNET IP stack name parameter is not set. Refer to NI-XNET Hardware and Software Help for more information on this parameter. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | Diag reference out is a cluster containing all necessary information about the diagnostic session. Wire this output as a handle through all subsequent diagnostic VIs, and always close it using Close Diagnostic.vi to disconnect from the ECU and close the diagnostic session's XNET IP Stack reference. Do not abort a running VI using ADCS functions, as this may not properly clear all resources. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**Open Diagnostic on IP.vi** opens a Diagnostic on Internet Protocol (DoIP) communication channel to an ECU. The UDP port specified as input is initialized, and a handle to it is stored (among other internal data) in the **Diag reference out** cluster, which serves as reference for further diagnostic functions.

Note that no communication to an ECU takes place at this point. To open a diagnostic session on an ECU, you can optionally call [DoIP Get Entities.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipgetentitiesvi) to find out which DoIP entities (DoIP-capable ECUs) exist in the network. Then, open a TCP/IP connection to a DoIP entity using [DoIP Connect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_doipconnectvi). After that, you can execute diagnostic services on the TCP/IP connection.

This VI replaces the standard (CAN-based) [Open Diagnostic on CAN FD.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_opendiagnosticoncanfdvi), because the CAN parameters are no longer relevant for IP-based diagnostics.

In general, you do not need to manipulate the **Diag reference out** cluster contents.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=open-diagnostic-on-lin-vi.html language=enus -->
## TOPIC 00061: Open Diagnostic on LIN.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `open-diagnostic-on-lin-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/open-diagnostic-on-lin-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Opens a diagnostic session on an NI-XNET LIN port. Communication to the ECU is not yet started. Format Input Interface specifies the LIN interface on which the diagnostic communication should take place, and points to the corresponding database cluster. The values for the XNET hardware inter

### Open Diagnostic on LIN.vi

Purpose

Opens a diagnostic session on an NI-XNET LIN port. Communication to the ECU is not yet started.
Format

[IMAGE alt='image' src='images/OpenDiagnosticonLINVI.gif']
Input

|  | Interface specifies the LIN interface on which the diagnostic communication should take place, and points to the corresponding database cluster. The values for the XNET hardware interface names are LIN1, LIN2, and so on. The Automotive Diagnostic Command Set supports NI-XNET LIN devices for LIN communication only. To use your NI-XNET interface, define your interface under NI-XNET Devices in MAX and pass the NI-XNET interface name that the Automotive Diagnostic Command Set will use. To do this, add @nixnet to the protocol string (for example, LIN1@nixnet). The interface name is related to the NI-XNET hardware naming under Devices and Interfaces in MAX. The Automotive Diagnostic Command Set requires valid assignments to a LIN database such as LDF or FIBEX. To communicate with hardware products on the external network, applications must understand how that hardware communicates in the actual embedded system, such as the vehicle. This embedded communication is described within a standardized file, such as FIBEX (.xml) or LDF (.ldf) for LIN. Within NI-XNET, this file is referred to as a database. The database contains many object classes, each of which describes a distinct entity in the embedded system. For LIN, select a LIN database and cluster to assign all settings from the selected cluster automatically, such as the LIN Baudrate, Master Request Frame, Slave Response Frame, or LIN Diagnostic Schedule. Using NI-XNET hardware, the Interface string should look like the following examples: LIN1@nixnet:XNET_LIN_DatabaseâUses LIN interface 1 of an NI-XNET device and assigns properties such as baudrate automatically from the XNET alias XNET_LIN_Database.LIN2@nixnet:XNET_LIN_DatabaseâUses LIN interface 2 of an NI-XNET device and so on, with the form LINx. Refer to the NI-XNET Hardware and Software Manual to assign a database cluster alias. |
| --- | --- |
|  | MasterReqFrame selects the Master Request Frame from an LDF or FIBEX database. If you assign an empty string (default) as MasterReqFrame, the name as defined in the LIN MasterReq standard is used. |
|  | SlaveRespFrame selects the Slave Response Frame from an LDF or FIBEX database. If you assign an empty string (default) as SlaveRespFrame, the name as defined in the LIN SlaveResp standard is used. |
|  | Baud Rate is the diagnostic communication baud rate. The default is –1, which reuses the baudrate of the selected LIN cluster from the assigned FIBEX or LDF database. To change the baudrate from the database, select a valid LIN baudrate. |
|  | NAD is the address of the slave node being addressed in a request. NAD also indicates the source of a response. NAD values are 1–127 (0x7F), while 0 (zero) and 128 (0x80)–255 (0xFF) are reserved for other purposes. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | Diag Ref Out is a cluster containing all necessary information about the diagnostic session. Wire this output as a handle to all subsequent diagnostic VIs, and close it using Close Diagnostic.vi. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**Open Diagnostic on LIN.vi** opens a diagnostic LIN communication channel to an ECU. The LIN port specified as input is initialized, and a handle to it is stored (among other internal data) in the **diag ref out** cluster, which serves as reference for further diagnostic functions.

A possible example of selections for the interface parameter for the NI-XNET hardware targets is:

- LIN1@nixnet:[LIN Cluster]â Uses LIN interface 1 of an NI-XNET device and settings of the LIN database of [LIN Cluster] alias as defined by NI-XNET.

Note

StartDiagnosticSession.vi

UDS DiagnosticSessionControl.vi

Open Diagnostic on LIN.vi

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=read-write-memory.html language=enus -->
## TOPIC 00062: Read/Write Memory

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `read-write-memory.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/read-write-memory.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Read/WriteMemoryByAddress services to upload/download data to certain memory addresses on an ECU. The address is a three-byte quantity in KWP2000 and a five-byte quantity (four-byte address and one-byte extension) in the calibration protocols. The Upload/Download functional unit services are

### Read/Write Memory

Use the Read/WriteMemoryByAddress services to upload/download data to certain memory addresses on an ECU. The address is a three-byte quantity in KWP2000 and a five-byte quantity (four-byte address and one-byte extension) in the calibration protocols.

The Upload/Download functional unit services are highly manufacturer specific and not well defined in the standard, so they are not a good way to provide a general upload/download mechanism.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=readdatabylocalidentifier-vi.html language=enus -->
## TOPIC 00063: ReadDataByLocalIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `readdatabylocalidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/readdatabylocalidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReadDataByLocalIdentifier service. Reads a data record from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessar

### ReadDataByLocalIdentifier.vi

Purpose

Executes the ReadDataByLocalIdentifier service. Reads a data record from the ECU.
Format

[IMAGE alt='image' src='images/ReadDataByLocalIdentifierVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | local ID defines the local identifier of the data to be read. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the data record from the ECU. If you know the record data description, you can interpret this record using Convert from Phys.vi. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests data record values from the ECU identified by the **local ID** parameter.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=readdtcbystatus-vi.html language=enus -->
## TOPIC 00064: ReadDTCByStatus.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `readdtcbystatus-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/readdtcbystatus-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReadDiagnosticTroubleCodesByStatus service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status

### ReadDTCByStatus.vi

Purpose

Executes the ReadDiagnosticTroubleCodesByStatus service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/ReadDTCByStatusVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) This VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | mode defines the type of DTCs to be read. The values are application specific. The usual values are: 2:AllIdentified3:AllSupported |
| 2: | AllIdentified |
| 3: | AllSupported |
|  | group of DTC specifies the group of Diagnostic Trouble Codes to be cleared. The following values have a special meaning, and you can specify them through a ring control: 0x0000All powertrain DTCs0x4000All chassis DTCs0x8000All body DTCs0xC000All network-related DTCs0xFF00All DTCs |
| 0x0000 | All powertrain DTCs |
| 0x4000 | All chassis DTCs |
| 0x8000 | All body DTCs |
| 0xC000 | All network-related DTCs |
| 0xFF00 | All DTCs |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequestedAdd Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI reads DTCs by status from the ECU memory. If you use the optional **group of DTC** parameter, the ECU reports DTCs only with status information based on the functional group selected by **group of DTC**.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=readecuidentification-vi.html language=enus -->
## TOPIC 00065: ReadECUIdentification.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `readecuidentification-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/readecuidentification-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReadECUIdentification service. Returns ECU identification data. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to

### ReadECUIdentification.vi

Purpose

Executes the ReadECUIdentification service. Returns ECU identification data.
Format

[IMAGE alt='image' src='images/ReadECUIdentificationVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | mode indicates the type of identification information to be returned. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU identification data. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests identification data from the ECU. The **mode** parameter identifies the type of identification data requested. The ECU returns identification data that the **data out** parameter can access. The **data out** format and definition are vehicle manufacturer specific.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=readmemorybyaddress-vi.html language=enus -->
## TOPIC 00066: ReadMemoryByAddress.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `readmemorybyaddress-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/readmemorybyaddress-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReadMemoryByAddress service. Reads data from the ECU memory. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to man

### ReadMemoryByAddress.vi

Purpose

Executes the ReadMemoryByAddress service. Reads data from the ECU memory.
Format

[IMAGE alt='image' src='images/ReadMemoryByAddressVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | address defines the memory address from which data are to be read. Notice that only three bytes are sent to the ECU, so the address must be in the range 0–FFFFFF (hex). |
|  | size defines the length of the memory block to be read. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the memory data from the ECU. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests memory data from the ECU identified by the **address** and **size** parameters. The **data out** format and definition are vehicle manufacturer specific. **data out** includes analog input and output signals, digital input and output signals, internal data, and system status information if the ECU supports them.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=readstatusofdtc-vi.html language=enus -->
## TOPIC 00067: ReadStatusOfDTC.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `readstatusofdtc-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/readstatusofdtc-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReadStatusOfDiagnosticTroubleCodes service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status

### ReadStatusOfDTC.vi

Purpose

Executes the ReadStatusOfDiagnosticTroubleCodes service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/ReadStatusOfDTCVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) This VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | group of DTC specifies the group of Diagnostic Trouble Codes to be cleared. The following values have a special meaning, and you can specify them through a ring control: 0x0000All powertrain DTCs0x4000All chassis DTCs0x8000All body DTCs0xC000All network-related DTCs0xFF00All DTCs |
| 0x0000 | All powertrain DTCs |
| 0x4000 | All chassis DTCs |
| 0x8000 | All body DTCs |
| 0xC000 | All network-related DTCs |
| 0xFF00 | All DTCs |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequestedAdd Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | DTC is the resulting Diagnostic Trouble Code. For the default 2-byte DTCs, you can use DTC to String.vi to convert this to readable format as defined by SAE J2012. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI reads diagnostic trouble codes from the ECU memory. If you use the optional **group of DTC** parameter, the ECU reports DTCs based only on the functional group selected by **group of DTC**.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=remote-activation-of-a-routine.html language=enus -->
## TOPIC 00068: Remote Activation of a Routine

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `remote-activation-of-a-routine.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/remote-activation-of-a-routine.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: These services are similar to the ActionService and DiagService functions of CCP. You can invoke an ECU internal routine identified by a Local/CommonIdentifier or a memory address. Contrary to the CCP case, execution of this routine can be asynchronous; that is, there are separate Start, Stop, and R

### Remote Activation of a Routine

These services are similar to the ActionService and DiagService functions of CCP. You can invoke an ECU internal routine identified by a Local/CommonIdentifier or a memory address. Contrary to the CCP case, execution of this routine can be asynchronous; that is, there are separate Start, Stop, and RequestResult services.

The control parameters of these commands are manufacturer specific and not defined in the standard.

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=requestroutineresultsbylocalidentifier-vi.html language=enus -->
## TOPIC 00069: RequestRoutineResultsByLocalIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `requestroutineresultsbylocalidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/requestroutineresultsbylocalidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the RequestRoutineResultsByLocalIdentifier service. Returns results from a routine on the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normal

### RequestRoutineResultsByLocalIdentifier.vi

Purpose

Executes the RequestRoutineResultsByLocalIdentifier service. Returns results from a routine
on the ECU.
Format

[IMAGE alt='image' src='images/RequestRoutineResultsByLocalIdentifierVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | local ID defines the local identifier of the routine from which this VI retrieves results. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific output parameters from the routine. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests results (for example, exit status information) referenced by **local ID** and generated by the routine executed in the ECU memory.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=requestseed-vi.html language=enus -->
## TOPIC 00070: RequestSeed.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `requestseed-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/requestseed-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the SecurityAccess service to retrieve a seed from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually

### RequestSeed.vi

Purpose

Executes the SecurityAccess service to retrieve a seed from the ECU.
Format

[IMAGE alt='image' src='images/RequestSeedVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | access mode indicates the security level to be granted. The values are application specific. This is an odd number, usually 1. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | seed out returns the seed from the ECU. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The usual procedure for getting a security access to the ECU is as follows:

1. Request a seed from the ECU using RequestSeed.vi with access mode = n .
2. From the seed, compute a key for the ECU on the host.
3. Send the key to the ECU using SendKey.vi with access mode = n + 1.
4. The security access is granted if the ECU validates the key sent. Otherwise, an error is returned.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=section-headings2.html language=enus -->
## TOPIC 00071: Section Headings

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `section-headings2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/section-headings2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following are section headings found in the Automotive Diagnostic Command Set API for LabVIEW VIs. Purpose Each VI description briefly describes the VI purpose. Format The format section describes the VI format. Input and Output The input and output sections list the VI parameters. Description T

### Section Headings

The following are section headings found in the Automotive Diagnostic Command Set API for LabVIEW VIs.
Purpose

Each VI description briefly describes the VI purpose.
Format

The format section describes the VI format.
Input and Output

The input and output sections list the VI parameters.
Description

The description section gives details about the VI purpose and effect.

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=sendkey-vi.html language=enus -->
## TOPIC 00072: SendKey.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `sendkey-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/sendkey-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the SecurityAccess service to send a key to the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipu

### SendKey.vi

Purpose

Executes the SecurityAccess service to send a key to the ECU.
Format

[IMAGE alt='image' src='images/SendKeyVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | access mode indicates the security level to be granted. The values are application specific. This is an even number, usually 2. |
|  | key in defines the key data to be sent to the ECU. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The usual procedure for getting a security access to the ECU is as follows:

1. Request a seed from the ECU using RequestSeed.vi with access mode = n .
2. From the seed, compute a key for the ECU on the host.
3. Send the key to the ECU using SendKey.vi with access mode = n + 1.
4. The security access is granted if the ECU validates the key sent. Otherwise, an error is returned.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=start-periodic-testerpresent-vi.html language=enus -->
## TOPIC 00073: Start Periodic TesterPresent.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `start-periodic-testerpresent-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/start-periodic-testerpresent-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Starts a background thread for the current diagnostic session that periodically transmits a TesterPresent message. Format Input period [sec] is the transmit period of the periodic message. Note that the periodic message is inhibited while the user sends regular messages. diag ref in specifie

### Start Periodic TesterPresent.vi

Purpose

Starts a background thread for the current diagnostic session that periodically transmits a TesterPresent message.
Format

[IMAGE alt='image' src='images/StartPeriodicTesterPresentVI.gif']
Input

|  | period [sec] is the transmit period of the periodic message. Note that the periodic message is inhibited while the user sends regular messages. |  |
| --- | --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Typically, it is not necessary to manipulate the elements of this cluster manually. |  |
|  | message type defines the periodic message to be sent. Choices are: KWP2000 TesterPresent0A TesterPresent service request according to the KWP2000 protocol as defined in ISO 14230-3. The response required? parameter determines whether the message is configured to have a response.UDS TesterPresent1A TesterPresent service request according to the UDS protocol as defined in ISO 14229-1. The response required? parameter determines whether the message is configured to have a response.User Defined2Any user defined request message can be transmitted periodically. Specify the message with the user message parameter. The response required? parameter determines whether the message is configured to have a response. If the response required? parameter does not match the behavior of the message given, the behavior is undefined. |  |
| KWP2000 TesterPresent | 0 | A TesterPresent service request according to the KWP2000 protocol as defined in ISO 14230-3. The response required? parameter determines whether the message is configured to have a response. |
| UDS TesterPresent | 1 | A TesterPresent service request according to the UDS protocol as defined in ISO 14229-1. The response required? parameter determines whether the message is configured to have a response. |
| User Defined | 2 | Any user defined request message can be transmitted periodically. Specify the message with the user message parameter. The response required? parameter determines whether the message is configured to have a response. If the response required? parameter does not match the behavior of the message given, the behavior is undefined. |
|  | response required? specifies whether the periodic message will have a response. |  |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when the status is TRUE.code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |  |
|  | status is TRUE if an error occurred. This VI is not executed when the status is TRUE. |  |
|  | code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |  |
|  | source identifies the VI where the error occurred. |  |
|  | user message defines the periodic service request message to be sent to the ECU as a stream of bytes for the User Defined message type. |  |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicates an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

Often it is necessary to transmit a TesterPresent service to keep a diagnostic session alive in the ECU. This VI automatically transmits a periodic TesterPresent message in the context of the current diagnostic session, as long as no other communication takes place. The automatic transmissions do not interfere with the regular diagnostic communication the user initiates.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=startdiagnosticsession-vi.html language=enus -->
## TOPIC 00074: StartDiagnosticSession.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `startdiagnosticsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/startdiagnosticsession-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the StartDiagnosticSession service. Sets up the ECU in a specific diagnostic mode. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is no

### StartDiagnosticSession.vi

Purpose

Executes the StartDiagnosticSession service. Sets up the ECU in a specific diagnostic mode.
Format

[IMAGE alt='image' src='images/StartDiagnosticSessionVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | mode indicates the diagnostic mode into which the ECU is brought. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI enables different diagnostic modes in the ECU. The possible diagnostic modes are not defined in the ISO 14230 standard and are application specific. A diagnostic session starts only if communication with the ECU is established. For more details about starting communication, refer to the ISO 14230-2 standard. If no diagnostic session has been requested after [Open Diagnostic on CAN FD.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_opendiagnosticoncanfdvi), a default session is automatically enabled in the ECU. The default session supports at least the following services:

- The StopCommunication service (refer to Close Diagnostic.vi and the ISO 14230-2 standard).
- The TesterPresent service (refer to TesterPresent.vi and the ISO 14230-3 standard).

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=startroutinebylocalidentifier-vi.html language=enus -->
## TOPIC 00075: StartRoutineByLocalIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `startroutinebylocalidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/startroutinebylocalidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the StartRoutineByLocalIdentifier service. Executes a routine on the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessa

### StartRoutineByLocalIdentifier.vi

Purpose

Executes the StartRoutineByLocalIdentifier service. Executes a routine on the ECU.
Format

[IMAGE alt='image' src='images/StartRoutineByLocalIdentifierVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | local ID defines the local identifier of the routine to be started. The values are application specific. |
|  | data in defines application-specific input parameters for the routine. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific output parameters from the routine. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI starts a routine in the ECU memory. The routine in the ECU starts after the positive response message is sent. The routine stops until [StopRoutineByLocalIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_stoproutinebylocalidentifiervi) is issued. The routines could be either tests run instead of normal operating code or routines enabled and executed with the normal operating code running. In the first case, you may need to switch the ECU to a specific diagnostic mode using [StartDiagnosticSession.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_startdiagnosticsessionvi) or unlock the ECU using the SecurityAccess service prior to using **StartRoutineByLocalIdentifier.vi**.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=stop-periodic-testerpresent-vi.html language=enus -->
## TOPIC 00076: Stop Periodic TesterPresent.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `stop-periodic-testerpresent-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/stop-periodic-testerpresent-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Terminates automatic transmission of a periodic TesterPresent message. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Typically, it is not necessary to manipulate the elements of this c

### Stop Periodic TesterPresent.vi

Purpose

Terminates automatic transmission of a periodic TesterPresent message.
Format

[IMAGE alt='image' src='images/StopPeriodicTesterPresentVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Typically, it is not necessary to manipulate the elements of this cluster manually. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when the status is TRUE.code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when the status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicates an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 indicates success. A negative value indicates an error; the VI did not execute the intended operation. A positive value indicates a warning; the VI executed the intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The automatic periodic transmission of a TesterPresent service initiated with [Start Periodic TesterPresent.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_startperiodictesterpresentvi) is terminated. If this VI is not called explicitly, the transmission is stopped when the diagnostic session is terminated with [Close Diagnostic.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_closediagnosticvi). When using the VW TP 2.0 transport protocol, calling [VWTP Disconnect.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_vwtpdisconnectvi) also stops the periodic TesterPresent transmission.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=stopdiagnosticsession-vi.html language=enus -->
## TOPIC 00077: StopDiagnosticSession.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `stopdiagnosticsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/stopdiagnosticsession-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the StopDiagnosticSession service. Returns the ECU to normal mode. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to m

### StopDiagnosticSession.vi

Purpose

Executes the StopDiagnosticSession service. Returns the ECU to normal mode.
Format

[IMAGE alt='image' src='images/StopDiagnosticSessionVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI disables the current ECU diagnostic mode. A diagnostic session stops only if communication is established with the ECU and a diagnostic session is running. If no diagnostic session is running, the default session is active. **StopDiagnosticSession.vi** cannot disable the default session. If the ECU has stopped the current diagnostic session, it performs the necessary action to restore its normal operating conditions. Restoring the normal operating conditions of the ECU may include resetting all controlled actuators if they were activated during the diagnostic session being stopped, and resuming all normal ECU algorithms. You should call **StopDiagnosticSession.vi** before disabling communication with [Close Diagnostic.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_closediagnosticvi), but only if you previously used [StartDiagnosticSession.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_startdiagnosticsessionvi).

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=stoproutinebylocalidentifier-vi.html language=enus -->
## TOPIC 00078: StopRoutineByLocalIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `stoproutinebylocalidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/stoproutinebylocalidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the StopRoutineByLocalIdentifier service. Stops a routine on the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary t

### StopRoutineByLocalIdentifier.vi

Purpose

Executes the StopRoutineByLocalIdentifier service. Stops a routine on the ECU.
Format

[IMAGE alt='image' src='images/StopRoutineByLocalIdentifierVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | local ID defines the local identifier of the routine to be started. The values are application specific. |
|  | data in defines application-specific input parameters for the routine. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific parameters from the routine. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI stops a routine in the ECU memory referenced by the **local ID** parameter.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=testerpresent-vi.html language=enus -->
## TOPIC 00079: TesterPresent.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `testerpresent-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/testerpresent-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the TesterPresent service. Keeps the ECU in diagnostic mode. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manuall

### TesterPresent.vi

Purpose

Executes the TesterPresent service. Keeps the ECU in diagnostic mode.
Format

[IMAGE alt='image' src='images/TesterPresentVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | response required? indicates whether the ECU answers this service (TRUE, default) or not (FALSE). In the latter case, success? is TRUE. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

To ensure proper ECU operation, you may need to keep the ECU informed that a diagnostic session is still in progress. If you do not send this information (for example, because the communication is broken), the ECU returns to normal mode from diagnostic mode after a while.

The TesterPresent service is this "keep alive" signal. It does not affect any other ECU operation.

Keep calling **TesterPresent.vi** within the ECU timeout period if no other service is executed.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=transport-protocol.html language=enus -->
## TOPIC 00080: Transport Protocol

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `transport-protocol.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/transport-protocol.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: As KWP2000 uses messages of variable byte lengths, a transport protocol is necessary on layers with only a well defined (short) message length, such as CAN. The transport protocol splits a long KWP2000 message into pieces that can be transferred over the network and reassembles those pieces to recov

### Transport Protocol

As KWP2000 uses messages of variable byte lengths, a transport protocol is necessary on layers with only a well defined (short) message length, such as CAN. The transport protocol splits a long KWP2000 message into pieces that can be transferred over the network and reassembles those pieces to recover the original message.

Note

Parent topic:

KWP2000 (Key Word Protocol 2000)

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-cleardiagnosticinformation-vi.html language=enus -->
## TOPIC 00081: UDS ClearDiagnosticInformation.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-cleardiagnosticinformation-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-cleardiagnosticinformation-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS ClearDiagnosticInformation service. Clears selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status By

### UDS ClearDiagnosticInformation.vi

Purpose

Executes the UDS ClearDiagnosticInformation service. Clears selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/UDSClearDiagnosticInformationVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The DTC descriptor is given here as a parameter basically to convert the group of DTC parameter to a binary representation according to DTC Byte Length and Byte Order. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 2. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | group of DTC specifies the group of Diagnostic Trouble Codes to be cleared. The following value has a special meaning, and you can specify it through a ring control: 0xFFFFFFAll DTCs |
| 0xFFFFFF | All DTCs |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI clears the diagnostic information on the ECU memory. If the **group of DTC** parameter is present, the ECU is requested to clear all memory including the DTCs.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-communicationcontrol-vi.html language=enus -->
## TOPIC 00082: UDS CommunicationControl.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-communicationcontrol-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-communicationcontrol-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS CommunicationControl service. Use this VI to switch transmission and/or reception of the normal communication messages (usually CAN messages) on or off. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagn

### UDS CommunicationControl.vi

Purpose

Executes the UDS CommunicationControl service. Use this VI to switch transmission and/or
reception of the normal communication messages (usually CAN messages) on or off.
Format

[IMAGE alt='image' src='images/UDSCommunicationControlVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | type indicates whether transmission/reception is to be switched on/off. The usual values are: 00:enableRxAndTx01:enableRxAndDisableTx02:disableRxAndEnableTx03:disableRxAndTx |
| 00: | enableRxAndTx |
| 01: | enableRxAndDisableTx |
| 02: | disableRxAndEnableTx |
| 03: | disableRxAndTx |
|  | communication type is a bitfield indicating the application level to change. The usual values are: 01:application02:networkManagement You can change more than one level at a time. |
| 01: | application |
| 02: | networkManagement |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI executes the UDS CommunicationControl service and switches transmission and/or reception of the normal communication messages (usually CAN messages) on or off. The **type** and **communication type** parameters are vehicle manufacturer specific (one OEM may disable the transmission only, while another OEM may disable the transmission and the reception based on vehicle manufacturer specific needs). The request is either transmitted functionally addressed to all ECUs with a single request message, or transmitted physically addressed to each ECU in a separate request message.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-controldtcsetting-vi.html language=enus -->
## TOPIC 00083: UDS ControlDTCSetting.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-controldtcsetting-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-controldtcsetting-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS ControlDTCSetting service. Modifies Diagnostic Trouble Code (DTC) generation behavior. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normal

### UDS ControlDTCSetting.vi

Purpose

Executes the UDS ControlDTCSetting service. Modifies Diagnostic Trouble Code (DTC) generation behavior.
Format

[IMAGE alt='image' src='images/UDSControlDTCSettingVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | data in defines application-specific data that control DTC generation. |
|  | type specifies the control mode: 1:on2:off |
| 1: | on |
| 2: | off |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-diagnosticsessioncontrol-vi.html language=enus -->
## TOPIC 00084: UDS DiagnosticSessionControl.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-diagnosticsessioncontrol-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-diagnosticsessioncontrol-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS DiagnosticSessionControl service. Sets up the ECU in a specific diagnostic mode. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it

### UDS DiagnosticSessionControl.vi

Purpose

Executes the UDS DiagnosticSessionControl service. Sets up the ECU in a specific diagnostic mode.
Format

[IMAGE alt='image' src='images/UDSDiagnosticSessionControlVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | mode indicates the diagnostic mode into which the ECU is brought. The values are application specific. The usual values are: 01:defaultSession02:ECUProgrammingSession03:ECUExtendedDiagnosticSession |
| 01: | defaultSession |
| 02: | ECUProgrammingSession |
| 03: | ECUExtendedDiagnosticSession |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | session parameter record returns implementation-dependent data from the ECU. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-diagoncan-services2.html language=enus -->
## TOPIC 00085: UDS (DiagOnCAN) Services

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-diagoncan-services2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-diagoncan-services2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: UDS ClearDiagnosticInformation.vi UDS CommunicationControl.vi UDS ControlDTCSetting.vi UDS DiagnosticSessionControl.vi UDS ECUReset.vi UDS InputOutputControlByIdentifier.vi UDS ReadDataByIdentifier.vi UDS ReadMemoryByAddress.vi UDS ReportDTCBySeverityMaskRecord.vi UDS ReportDTCByStatusMask.vi UDS Re

### UDS (DiagOnCAN) Services

[UDS ClearDiagnosticInformation.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udscleardiagnosticinformationvi)

[UDS CommunicationControl.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udscommunicationcontrolvi)

[UDS ControlDTCSetting.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udscontroldtcsettingvi)

[UDS DiagnosticSessionControl.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsdiagnosticsessioncontrolvi)

[UDS ECUReset.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsecuresetvi)

[UDS InputOutputControlByIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsinputoutputcontrolbyidentifiervi)

[UDS ReadDataByIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreaddatabyidentifiervi)

[UDS ReadMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreadmemorybyaddressvi)

[UDS ReportDTCBySeverityMaskRecord.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreportdtcbyseveritymaskrecordvi)

[UDS ReportDTCByStatusMask.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreportdtcbystatusmaskvi)

[UDS ReportSeverityInformationOfDTC.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreportseverityinformationofdtcvi)

[UDS ReportSupportedDTCs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreportsupporteddtcsvi)

[UDS RequestDownload.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestdownloadvi)

[UDS RequestSeed.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestseedvi)

[UDS RequestTransferExit.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequesttransferexitvi)

[UDS RequestUpload.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestuploadvi)

[UDS RoutineControl.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsroutinecontrolvi)

[UDS SendKey.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udssendkeyvi)

[UDS TesterPresent.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udstesterpresentvi)

[UDS TransferData.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udstransferdatavi)

[UDS WriteDataByIdentifier.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udswritedatabyidentifiervi)

[UDS WriteMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udswritememorybyaddressvi)

[UDS 06ReadMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_uds06readmemorybyaddressvi)

[UDS 06WriteMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_uds06writememorybyaddressvi)

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-ecureset-vi.html language=enus -->
## TOPIC 00086: UDS ECUReset.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-ecureset-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-ecureset-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS ECUReset service. Resets the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the el

### UDS ECUReset.vi

Purpose

Executes the UDS ECUReset service. Resets the ECU.
Format

[IMAGE alt='image' src='images/UDSECUResetVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | mode indicates the reset mode: HexDescription01hardReset02keyOffOnReset03softReset04enableRapidPowerShutDown05disableRapidPowerShutDown |
| Hex | Description |
| 01 | hardReset |
| 02 | keyOffOnReset |
| 03 | softReset |
| 04 | enableRapidPowerShutDown |
| 05 | disableRapidPowerShutDown |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | power down time returns the minimum standby sequence time that the server remains in the power-down sequence in seconds. A value of FF hex indicates a failure or time not available. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests the ECU to perform an ECU reset effectively based on the **mode** parameter value content. The vehicle manufacturer determines when the positive response message is sent.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-inputoutputcontrolbyidentifier-vi.html language=enus -->
## TOPIC 00087: UDS InputOutputControlByIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-inputoutputcontrolbyidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-inputoutputcontrolbyidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS InputOutputControlByIdentifier service. Modifies ECU I/O port behavior. Format Input data in defines application-specific data for this service. diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wi

### UDS InputOutputControlByIdentifier.vi

Purpose

Executes the UDS InputOutputControlByIdentifier service. Modifies ECU I/O port behavior.
Format

[IMAGE alt='image' src='images/UDSInputOutputControlByIdentifierVI.gif']
Input

|  | data in defines application-specific data for this service. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | ID defines the identifier of the I/O to be manipulated. The values are application specific. |
|  | mode defines the I/O control type. The values are application specific. The usual values are: 0:ReturnControlToECU1:ResetToDefault2:FreezeCurrentState3:ShortTermAdjustment |
| 0: | ReturnControlToECU |
| 1: | ResetToDefault |
| 2: | FreezeCurrentState |
| 3: | ShortTermAdjustment |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific data for this service. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI substitutes a value for an input signal or internal ECU function. It also controls an output (actuator) of an electronic system referenced by the **local ID** parameter.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-readdatabyidentifier-vi.html language=enus -->
## TOPIC 00088: UDS ReadDataByIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-readdatabyidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-readdatabyidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS ReadDataByIdentifier service. Reads a data record from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary

### UDS ReadDataByIdentifier.vi

Purpose

Executes the UDS ReadDataByIdentifier service. Reads a data record from the ECU.
Format

[IMAGE alt='image' src='images/UDSReadDataByIdentifierVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | ID defines the identifier of the data to be read. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the data record from the ECU. If you know the record data description, you can use Convert to Phys.vi to generate this record. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests data record values from the ECU identified by the **ID** parameter.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-readmemorybyaddress-vi.html language=enus -->
## TOPIC 00089: UDS ReadMemoryByAddress.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-readmemorybyaddress-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-readmemorybyaddress-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS ReadMemoryByAddress service. Reads data from the ECU memory. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to

### UDS ReadMemoryByAddress.vi

Purpose

Executes the UDS ReadMemoryByAddress service. Reads data from the ECU memory.
Format

[IMAGE alt='image' src='images/UDSReadMemoryByAddressVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | address defines the memory address from which data are to be read. Only three bytes are sent to the ECU, so the address must be in the range 0–FFFFFF (hex). |
|  | size defines the length of the memory block to be read. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU memory data. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI requests ECU memory data identified by the **address** and **size** parameters. The **data out** format and definition are vehicle manufacturer specific. **data out** includes analog input and output signals, digital input and output signals, internal data, and system status information if the ECU supports them.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-reportdtcbyseveritymaskrecord-vi.html language=enus -->
## TOPIC 00090: UDS ReportDTCBySeverityMaskRecord.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-reportdtcbyseveritymaskrecord-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-reportdtcbyseveritymaskrecord-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReportDTCBySeverityMaskRecord subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of by

### UDS ReportDTCBySeverityMaskRecord.vi

Purpose

Executes the ReportDTCBySeverityMaskRecord subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/UDSReportDTCBySeverityMaskRecordVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. For this subfunction, the default is 2.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) This VI interprests the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. For this subfunction, the default is 2. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | severity mask defines the status of DTCs to be read. The values are application specific. |
|  | status defines the status of DTCs to be read. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequestedAdd Data contains optional additional data for this DTC. |
|  | DTC is the resulting Diagnostic Trouble Code. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | status avail mask is an application-specific value returned for all DTCs. |

Description

This VI executes the ReportDTCBySeverityMaskRecord subfunction of the UDS ReadDiagnosticTroubleCodeInformation service and reads the selected DTCs.

For further details about this service, refer to the ISO 14229-1 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-reportdtcbystatusmask-vi.html language=enus -->
## TOPIC 00091: UDS ReportDTCByStatusMask.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-reportdtcbystatusmask-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-reportdtcbystatusmask-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReportDTCByStatusMask subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the

### UDS ReportDTCByStatusMask.vi

Purpose

Executes the ReportDTCByStatusMask subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/UDSReportDTCByStatusMaskVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) This VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | status mask defines the status of DTCs to be read. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequestedAdd Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | DTC is the resulting Diagnostic Trouble Code. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | status avail mask is an application-specific value returned for all DTCs. |

Description

This VI executes the ReportDTCByStatusMask subfunction of the UDS ReadDiagnosticTroubleCodeInformation service and reads the selected DTCs from the ECU.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-reportseverityinformationofdtc-vi.html language=enus -->
## TOPIC 00092: UDS ReportSeverityInformationOfDTC.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-reportseverityinformationofdtc-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-reportseverityinformationofdtc-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReportSeverityInformationOfDTC subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of b

### UDS ReportSeverityInformationOfDTC.vi

Purpose

Executes the ReportSeverityInformationOfDTC subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/UDSReportSeverityInformationofDTCVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. For this subfunction, the default is 2.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) This VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. For this subfunction, the default is 2. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | DTC mask record defines the status of DTCs to be read. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequestedAdd Data contains optional additional data for this DTC. |
|  | DTC is the resulting Diagnostic Trouble Code. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | status avail mask is an application-specific value returned for all DTCs. |

Description

This VI executes the ReportSeverityInformationOfDTC subfunction of the UDS ReadDiagnosticTroubleCodeInformation service and reads the selected DTCs from the ECU memory.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-reportsupporteddtcs-vi.html language=enus -->
## TOPIC 00093: UDS ReportSupportedDTCs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-reportsupporteddtcs-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-reportsupporteddtcs-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the ReportSupportedDTCs subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads all supported Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes t

### UDS ReportSupportedDTCs.vi

Purpose

Executes the ReportSupportedDTCs subfunction of the UDS ReadDiagnosticTroubleCodeInformation service. Reads all supported Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/UDSReportSupportedDTCsVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) This VI interprets the response byte stream according to this description and returns the resulting DTC records in the DTCs cluster array. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3 for UDS. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequestedAdd Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | DTC is the resulting Diagnostic Trouble Code. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor). |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | status avail mask is an application-specific value returned for all DTCs. |

Description

This VI executes the ReportSupportedDTCs subfunction of the UDS ReadDiagnosticTroubleCodeInformation service and reads all supported DTCs from the ECU memory.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-requestdownload-vi.html language=enus -->
## TOPIC 00094: UDS RequestDownload.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-requestdownload-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-requestdownload-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Initiates a download of data to the ECU. Format Input data format identifier defines the compression and encryption scheme to be used for the data blocks written to the ECU. A value of 0 means no compression/no encryption. Nonzero values are not standardized and implementation dependent. dia

### UDS RequestDownload.vi

Purpose

Initiates a download of data to the ECU.
Format

[IMAGE alt='image' src='images/UDSRequestDownloadVI.gif']
Input

|  | data format identifier defines the compression and encryption scheme to be used for the data blocks written to the ECU. A value of 0 means no compression/no encryption. Nonzero values are not standardized and implementation dependent. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | memory address defines the memory address to which data are written. |
|  | memory size defines the size of the data to be written. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | memory address length defines the number of bytes of the memory address parameter that are written to the ECU. This value is implementation dependent and must be in the range of 1–4. For example, if this value is 2, only the two lowest bytes of the address are written to the ECU. |
|  | memory size length defines the number of bytes of the memory size parameter that are written to the ECU. This value is implementation dependent and must be in the range of 1–4. For example, if this value is 2, only the two lowest bytes of the size are written to the ECU. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | block size returns the number of data bytes to be transferred to the ECU in subsequent UDS TransferData.vi requests. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**UDS RequestDownload.vi** initiates the download of a data block to the ECU. This is required to set up the download process; the actual data transfer occurs with subsequent [UDS TransferData.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udstransferdatavi) requests. The transfer must occur in blocks of the size that this service returns (the **block size** parameter). After the download completes, use the [UDS RequestTransferExit.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequesttransferexitvi) service to terminate the process.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-requestseed-vi.html language=enus -->
## TOPIC 00095: UDS RequestSeed.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-requestseed-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-requestseed-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS SecurityAccess service to retrieve a seed from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manu

### UDS RequestSeed.vi

Purpose

Executes the UDS SecurityAccess service to retrieve a seed from the ECU.
Format

[IMAGE alt='image' src='images/UDSRequestSeedVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | access mode indicates the security level to be granted. The values are application specific. This is an odd number, usually 1. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | seed out returns the seed from the ECU. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The usual procedure for getting a security access to the ECU is as follows:

1. Request a seed from the ECU using UDS RequestSeed.vi with access mode = n .
2. From the seed, compute a key for the ECU on the host.
3. Send the key to the ECU using UDS SendKey.vi with access mode = n + 1.
4. The security access is granted if the ECU validates the key sent. Otherwise, an error is returned.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-requesttransferexit-vi.html language=enus -->
## TOPIC 00096: UDS RequestTransferExit.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-requesttransferexit-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-requesttransferexit-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Terminates a download/upload process. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of thi

### UDS RequestTransferExit.vi

Purpose

Terminates a download/upload process.
Format

[IMAGE alt='image' src='images/UDSRequestTransferExitVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | data in defines a data record to be written to the ECU as part of the termination process. The meaning is implementation dependent; this might be a checksum or a similar verification instrument. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns a memory data block from the ECU as part of the termination process. The meaning is implementation dependent; this might be a checksum or a similar verification instrument. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**UDS RequestTransferExit.vi** terminates a download or upload process initialized with [UDS RequestDownload.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestdownloadvi) or [UDS RequestUpload.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestuploadvi).

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-requestupload-vi.html language=enus -->
## TOPIC 00097: UDS RequestUpload.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-requestupload-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-requestupload-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Initiates an upload of data from the ECU. Format Input data format identifier defines the compression and encryption scheme to be used for the data blocks read from the ECU. A value of 0 means no compression/no encryption. Nonzero values are not standardized and implementation dependent. dia

### UDS RequestUpload.vi

Purpose

Initiates an upload of data from the ECU.
Format

[IMAGE alt='image' src='images/UDSRequestUploadVI.gif']
Input

|  | data format identifier defines the compression and encryption scheme to be used for the data blocks read from the ECU. A value of 0 means no compression/no encryption. Nonzero values are not standardized and implementation dependent. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | memory address defines the memory address from which data are read. |
|  | memory size defines the size of the data to be read. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | memory address length defines the number of bytes of the memory address parameter that are written to the ECU. This value is implementation dependent and must be in the range of 1–4. For example, if this value is 2, only the two lowest bytes of the address are written to the ECU. |
|  | memory size length defines the number of bytes of the memory size parameter that are written to the ECU. This value is implementation dependent and must be in the range of 1–4. For example, if this value is 2, only the two lowest bytes of the size are written to the ECU. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | block size returns the number of data bytes to be transferred from the ECU in subsequent UDS TransferData.vi requests. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**UDS RequestDownload.vi** initiates the upload of a data block from the ECU. This is required to set up the upload process; the actual data transfer occurs with subsequent [UDS TransferData.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udstransferdatavi) requests. The transfer must occur in blocks of the size that this service returns (the **block size** parameter). After the upload completes, use the [UDS RequestTransferExit.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequesttransferexitvi) service to terminate the process.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-routinecontrol-vi.html language=enus -->
## TOPIC 00098: UDS RoutineControl.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-routinecontrol-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-routinecontrol-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS RoutineControl service. Executes a routine on the ECU. Format Input mode defines the service operation mode. You can obtain the values from a ring control: 1:Start Routine2:Stop Routine3:Request Routine Results Other values are application specific. diag ref in specifies the

### UDS RoutineControl.vi

Purpose

Executes the UDS RoutineControl service. Executes a routine on the ECU.
Format

[IMAGE alt='image' src='images/UDSRoutineControlVI.gif']
Input

|  | mode defines the service operation mode. You can obtain the values from a ring control: 1:Start Routine2:Stop Routine3:Request Routine Results Other values are application specific. |
| --- | --- |
| 1: | Start Routine |
| 2: | Stop Routine |
| 3: | Request Routine Results |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | ID defines the identifier of the routine to be started. The values are application specific. |
|  | data in defines application-specific input parameters for the routine. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific output parameters from the routine. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI executes the UDS RoutineControl service and launches an ECU routine, stops an ECU routine, or requests ECU routine results from the ECU.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-sendkey-vi.html language=enus -->
## TOPIC 00099: UDS SendKey.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-sendkey-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-sendkey-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the SecurityAccess service to send a key to the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipu

### UDS SendKey.vi

Purpose

Executes the SecurityAccess service to send a key to the ECU.
Format

[IMAGE alt='image' src='images/UDSSendKeyVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | access mode indicates the security level to be granted. The values are application specific. This is an even number, usually 2. |
|  | key in defines the key data to be sent to the ECU. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The usual procedure for getting a security access to the ECU is as follows:

1. Request a seed from the ECU using UDS RequestSeed.vi with access mode = n .
2. From the seed, compute a key for the ECU on the host.
3. Send the key to the ECU using UDS SendKey.vi with access mode = n + 1.
4. The security access is granted if the ECU validates the key sent. Otherwise, an error is returned.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-testerpresent-vi.html language=enus -->
## TOPIC 00100: UDS TesterPresent.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-testerpresent-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-testerpresent-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS TesterPresent service. Keeps the ECU in diagnostic mode. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to man

### UDS TesterPresent.vi

Purpose

Executes the UDS TesterPresent service. Keeps the ECU in diagnostic mode.
Format

[IMAGE alt='image' src='images/UDSTesterPresentVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | response required? indicates whether the ECU answers this service (TRUE, default) or not (FALSE). In the latter case, success? is TRUE. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

To ensure proper ECU operation, you may need to keep the ECU informed that a diagnostic session is still in progress. If you do not send this information (for example, because the communication is broken), the ECU returns to normal mode from diagnostic mode after a while.

The TesterPresent service is this "keep alive" signal. It does not affect any other ECU operation.

Keep calling **UDS TesterPresent.vi** within the ECU timeout period if no other service is executed.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-transferdata-vi.html language=enus -->
## TOPIC 00101: UDS TransferData.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-transferdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-transferdata-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Transfers data to/from the ECU in a download/upload process. Format Input block sequence counter in is used to number the data blocks to be transferred to/from the ECU. The block sequence counter value starts at 01 hex with the first UDS TransferData.vi request that follows the UDS RequestDo

### UDS TransferData.vi

Purpose

Transfers data to/from the ECU in a download/upload process.
Format

[IMAGE alt='image' src='images/UDSTransferDataVI.gif']
Input

|  | block sequence counter in is used to number the data blocks to be transferred to/from the ECU. The block sequence counter value starts at 01 hex with the first UDS TransferData.vi request that follows the UDS RequestDownload.vi or UDS RequestUpload.vi service. Its value is incremented by 1 for each subsequent UDS TransferData.vi request. At the value of FF hex, the block sequence counter rolls over and starts at 00 hex with the next UDS TransferData.vi request. The block sequence counter is updated automatically and returned in the block sequence counter out parameter. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | data in defines the data block to be written to the ECU. For a download, this is a memory data block to be downloaded to the ECU. For an upload, the meaning is implementation dependent; in most cases, it is sufficient to leave the parameter empty (default). |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | block sequence counter out returns the updated value of the block sequence counter. |
| --- | --- |
|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
|  | data out returns the memory data from the ECU. For a download, this might contain a checksum or similar verification instrument; the meaning is implementation dependent. For an upload, this is a memory data block uploaded from the ECU. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

**UDS TransferData.vi** executes the data transfer of a download process (initiated with a previous [UDS RequestDownload.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestdownloadvi) request) or an upload process (initiated with a previous [UDS RequestUpload.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequestuploadvi) request). The data transfer must occur in blocks of the size returned in the **block size** parameter of the respective request service. After the data transfer has completed, terminate the operation by calling the [UDS RequestTransferExit.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsrequesttransferexitvi) service.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-unified-diagnostic-services.html language=enus -->
## TOPIC 00102: UDS (Unified Diagnostic Services)

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-unified-diagnostic-services.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-unified-diagnostic-services.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The UDS protocol has become a de facto standard in automotive diagnostic applications. It is standardized as ISO 14229. UDS describes the implementation of various diagnostic services you can access through the protocol. As UDS uses messages of variable byte lengths, a transport protocol is necessar

### UDS (Unified Diagnostic Services)

The UDS protocol has become a de facto standard in automotive diagnostic applications. It is standardized as ISO 14229. UDS describes the implementation of various diagnostic services you can access through the protocol.

As UDS uses messages of variable byte lengths, a transport protocol is necessary on layers with only a well defined (short) message length, such as CAN or LIN. The transport protocol splits a long UDS message into pieces that can be transferred over the network and reassembles those pieces to recover the original message.

Note

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-writedatabyidentifier-vi.html language=enus -->
## TOPIC 00103: UDS WriteDataByIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-writedatabyidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-writedatabyidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS WriteDataByIdentifier service. Writes a data record to the ECU. Format Input data in defines the data record written to the ECU. If you know the record data description, you can use Convert from Phys.vi to generate this record. diag ref in specifies the diagnostic session ha

### UDS WriteDataByIdentifier.vi

Purpose

Executes the UDS WriteDataByIdentifier service. Writes a data record to the ECU.
Format

[IMAGE alt='image' src='images/UDSWriteDataByIdentifierVI.gif']
Input

|  | data in defines the data record written to the ECU. If you know the record data description, you can use Convert from Phys.vi to generate this record. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | ID defines the identifier of the data to be written. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI performs the UDS service WriteDataByIdentifier and writes RecordValues (data values) to the ECU. **data in** identifies the data. The vehicle manufacturer must ensure the ECU conditions are met when performing this service. Typical use cases are clearing nonvolatile memory, resetting learned values, setting option content, setting the Vehicle Identification Number, or changing calibration values.

For further details about this service, refer to the 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds-writememorybyaddress-vi.html language=enus -->
## TOPIC 00104: UDS WriteMemoryByAddress.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds-writememorybyaddress-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds-writememorybyaddress-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS WriteMemoryByAddress service. Writes data to the ECU memory. Format Input data in defines the memory block to be written to the ECU. diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through

### UDS WriteMemoryByAddress.vi

Purpose

Executes the UDS WriteMemoryByAddress service. Writes data to the ECU memory.
Format

[IMAGE alt='image' src='images/UDSWriteMemoryByAddressVI.gif']
Input

|  | data in defines the memory block to be written to the ECU. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | address defines the memory address to which data are to be written. Only three bytes are sent to the ECU, so the address must be in the range 0–FFFFFF (hex). |
|  | size defines the length of the memory block to be written. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI performs the UDS service WriteMemoryByAddress and writes RecordValues (data values) to the ECU. **address** and **size** identify the data. The vehicle manufacturer must ensure the ECU conditions are met when performing this service. Typical use cases are clearing nonvolatile memory, resetting learned values, setting option content, setting the Vehicle Identification Number, or changing calibration values.

For further details about this service, refer to the ISO 15765-3 standard.

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds06-readmemorybyaddress-vi.html language=enus -->
## TOPIC 00105: UDS06 ReadMemoryByAddress.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds06-readmemorybyaddress-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds06-readmemorybyaddress-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS ReadMemoryByAddress service. Reads data from the ECU memory. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to

### UDS06 ReadMemoryByAddress.vi

Purpose

Executes the UDS ReadMemoryByAddress service. Reads data from the ECU memory.
Format

[IMAGE alt='image' src='images/UDS06ReadMemoryByAddressVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | memory address defines the memory address from which data are to be read. Note that memory address length specifies how many bytes of the address are sent to the ECU. This defines the maximum address you can use. |
|  | memory size defines the length of the memory block to be read. Note that memory size length specifies how many bytes of the size are sent to the ECU. This defines the maximum size you can use. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | memory address length specifies how many bytes of the address are sent to the ECU. The default is 4. |
|  | memory size length specifies how many bytes of the size are sent to the ECU. The default is 4. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the memory data from the ECU. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

Similar to [UDS ReadMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udsreadmemorybyaddressvi). You can define the size in bytes of the **address** and **size** parameters (the default is 4).

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=uds06-writememorybyaddress-vi.html language=enus -->
## TOPIC 00106: UDS06 WriteMemoryByAddress.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `uds06-writememorybyaddress-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/uds06-writememorybyaddress-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the UDS WriteMemoryByAddress service. Writes data to the ECU memory. Format Input data in defines the memory block to be written to the ECU. diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through

### UDS06 WriteMemoryByAddress.vi

Purpose

Executes the UDS WriteMemoryByAddress service. Writes data to the ECU memory.
Format

[IMAGE alt='image' src='images/UDS06WriteMemoryByAddressVI.gif']
Input

|  | data in defines the memory block to be written to the ECU. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | memory address defines the memory address to which data are to be sent. Note that memory address length specifies how many bytes of the address are sent to the ECU. This defines the maximum address you can use. |
|  | memory size defines the length of the memory block to be sent. Note that memory size length specifies how many bytes of the size are sent to the ECU. This defines the maximum size you can use. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |
|  | memory address length specifies how many bytes of the address are sent to the ECU. The default is 4. |
|  | memory size length specifies how many bytes of the size are sent to the ECU. The default is 4. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

Similar to [UDS WriteMemoryByAddress.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_udswritememorybyaddressvi). You can define the size in bytes of the **address** and **size** parameters (the default is 4).

Parent topic:

UDS (DiagOnCAN) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=vwtp-connect-vi.html language=enus -->
## TOPIC 00107: VWTP Connect.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `vwtp-connect-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/vwtp-connect-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Establishes a connection channel to an ECU using the VW TP 2.0. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this

### VWTP Connect.vi

Purpose

Establishes a connection channel to an ECU using the VW TP 2.0.
Format

[IMAGE alt='image' src='images/VWTPConnectVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | channel ID defines the CAN identifier on which the ECU responds for this connection. The ECU defines the ID on which the host transmits. |
|  | application type specifies the type of communication that takes place on the communication channel. For diagnostic applications, specify KWP2000 (1). The other values are for manufacturer-specific purposes. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

Note

VWTP Connection Test.vi

There is no equivalent for the ISO TP (ISO 15765-2), as the ISO TP does not use a special
communication link.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=vwtp-connection-test-vi.html language=enus -->
## TOPIC 00108: VWTP Connection Test.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `vwtp-connection-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/vwtp-connection-test-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Maintains a connection channel to an ECU using the VW TP 2.0. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cl

### VWTP Connection Test.vi

Purpose

Maintains a connection channel to an ECU using the VW TP 2.0.
Format

[IMAGE alt='image' src='images/VWTPConnectionTestVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

For the VW TP 2.0, you must periodically maintain the connection link to the ECU so that
the ECU does not terminate it.

This VI sends a Connection Test message to the ECU and evaluates its response, performing
the steps necessary to maintain the connection.

There is no equivalent for the ISO TP (ISO 15765-2), as the ISO TP does not use a special
communication link.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=vwtp-disconnect-vi.html language=enus -->
## TOPIC 00109: VWTP Disconnect.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `vwtp-disconnect-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/vwtp-disconnect-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Terminates a connection channel to an ECU using the VW TP 2.0. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this c

### VWTP Disconnect.vi

Purpose

Terminates a connection channel to an ECU using the VW TP 2.0.
Format

[IMAGE alt='image' src='images/VWTPDisconnectVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

Note

VWTP Connect.vi

There is no equivalent for the ISO TP (ISO 15765-2), as the ISO TP does not use a special
communication link.

Parent topic:

General Functions

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=writedatabylocalidentifier-vi.html language=enus -->
## TOPIC 00110: WriteDataByLocalIdentifier.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `writedatabylocalidentifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/writedatabylocalidentifier-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WriteDataByLocalIdentifier service. Writes a data record to the ECU. Format Input data in defines the data record written to the ECU. If you know the record data description, you can use Convert from Phys.vi to generate this record. diag ref in specifies the diagnostic session h

### WriteDataByLocalIdentifier.vi

Purpose

Executes the WriteDataByLocalIdentifier service. Writes a data record to the ECU.
Format

[IMAGE alt='image' src='images/WriteDataByLocalIdentifierVI.gif']
Input

|  | data in defines the data record written to the ECU. If you know the record data description, you can use Convert from Phys.vi to generate this record. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | local ID defines the local identifier of the data to be written. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI performs the KWP2000 WriteDataByLocalIdentifier service and writes RecordValues (data values) to the ECU. **data in** identifies the data. The vehicle manufacturer must ensure the ECU conditions are met when performing this service. Typical use cases are clearing nonvolatile memory, resetting learned values, setting option content, setting the Vehicle Identification Number, or changing calibration values.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=writememorybyaddress-vi.html language=enus -->
## TOPIC 00111: WriteMemoryByAddress.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `writememorybyaddress-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/writememorybyaddress-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WriteMemoryByAddress service. Writes data to the ECU memory. Format Input data in defines the memory block to be written to the ECU. diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subs

### WriteMemoryByAddress.vi

Purpose

Executes the WriteMemoryByAddress service. Writes data to the ECU memory.
Format

[IMAGE alt='image' src='images/WriteMemoryByAddressVI.gif']
Input

|  | data in defines the memory block to be written to the ECU. |
| --- | --- |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | address defines the memory address to which data are written. Notice that only three bytes are sent to the ECU, so the address must be in the range 0–FFFFFF (hex). |
|  | size defines the length of the memory block to be written. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

This VI performs the KWP2000 WriteDataByAddress service and writes RecordValues (data values) to the ECU. **address** and **size** identify the data. The vehicle manufacturer must ensure the ECU conditions are met when performing this service. Typical use cases are clearing nonvolatile memory, resetting learned values, setting option content, setting the Vehicle Identification Number, or changing calibration values.

For further details about this service, refer to the ISO 14230-3 standard.

Parent topic:

KWP2000 Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-clear-emission-related-dtcs-vi.html language=enus -->
## TOPIC 00112: WWH-OBD Clear Emission Related DTCs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-clear-emission-related-dtcs-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-clear-emission-related-dtcs-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD ClearDiagnosticInformation service. Clears selected Diagnostic Trouble Codes (DTCs). Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Norm

### WWH-OBD Clear Emission Related DTCs.vi

Purpose

Executes the WWH-OBD ClearDiagnosticInformation service. Clears selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/WWHOBDClearEmissionRelatedDTCsVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD ClearDiagnosticInformation service is based on the UDS ClearDiagnosticInformation service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-convert-dtcs-to-j1939-vi.html language=enus -->
## TOPIC 00113: WWH-OBD Convert DTCs to J1939.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-convert-dtcs-to-j1939-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-convert-dtcs-to-j1939-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts DTCs to the J1939 DTC format. Format Input DTCs is a cluster that contains diagnostic trouble codes (DTCs). error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to e

### WWH-OBD Convert DTCs to J1939.vi

Purpose

Converts DTCs to the J1939 DTC format.
Format

[IMAGE alt='image' src='images/WWHOBDConvertDTCstoJ1939VI.gif']
Input

|  | DTCs is a cluster that contains diagnostic trouble codes (DTCs). |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE. code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | DTCs J1939 contains the DTCs converted to the J1939 format. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred. code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-convert-dtcs-to-j1939-vi2.html language=enus -->
## TOPIC 00114: WWH-OBD Convert DTCs to J1939.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-convert-dtcs-to-j1939-vi2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-convert-dtcs-to-j1939-vi2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Converts DTCs to the J2012 DTC format. Format Input DTCs is a cluster that contains diagnostic trouble codes (DTCs). error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to e

### WWH-OBD Convert DTCs to J1939.vi

Purpose

Converts DTCs to the J2012 DTC format.
Format

[IMAGE alt='image' src='images/WWHOBDConvertDTCstoJ2012VI.gif']
Input

|  | DTCs is a cluster that contains diagnostic trouble codes (DTCs). |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE. code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | DTCs J2012 contains the DTCs converted to the J2012 format. |
| --- | --- |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred. code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-did-vi.html language=enus -->
## TOPIC 00115: WWH-OBD Request DID.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-did-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-did-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD ReadDataByIdentifier service. Reads a data record from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not neces

### WWH-OBD Request DID.vi

Purpose

Executes the WWH-OBD ReadDataByIdentifier service. Reads a data record from the ECU.
Format

[IMAGE alt='image' src='images/WWHOBDRequestDIDVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | data identifier defines the data identifier of the data to be read. The SAE J1979DA standard defines the values. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU data record. If you know the record data description, you can use Convert from Phys.vi to interpret this record. You can obtain the description from the SAE J1979DA standard. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD ReadDataByIdentifier service is based on the UDS ReadDataByIdentifier service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-dtc-extended-data-record-vi.html language=enus -->
## TOPIC 00116: WWH-OBD Request DTC Extended Data Record.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-dtc-extended-data-record-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-dtc-extended-data-record-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it

### WWH-OBD Request DTC Extended Data Record.vi

Purpose

Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/WWHOBDRequestDTCExtendedDataRecordVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | DTC mask record specifies the DTC mask record. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU data record. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD ReadDTCInformation service is based on the UDS ReaDTCInformation service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-emission-related-dtcs-vi.html language=enus -->
## TOPIC 00117: WWH-OBD Request Emission Related DTCs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-emission-related-dtcs-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-emission-related-dtcs-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3.Status Byte Le

### WWH-OBD Request Emission Related DTCs.vi

Purpose

Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/WWHOBDRequestEmissionRelatedDTCsVI.gif']
Input

|  | DTC descriptor is a cluster that describes the DTC records the ECU delivers: DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3.Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1.Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0.Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) The DTC descriptor is given here as a parameter to convert the group of DTC parameters to a binary representation according to DTC Byte Length and Byte Order. |
| --- | --- |
|  | DTC Byte Length indicates the number of bytes the ECU sends for each DTC. The default is 3. |
|  | Status Byte Length indicates the number of bytes the ECU sends for each DTC's status. The default is 1. |
|  | Add Data Byte Length indicates the number of bytes the ECU sends for each DTC's additional data. Usually, there is no additional data, so the default is 0. |
|  | Byte Order indicates the byte ordering for multibyte items: 0:MSB_FIRST (Motorola) (default)1:LSB_FIRST (Intel) |
| 0: | MSB_FIRST (Motorola) (default) |
| 1: | LSB_FIRST (Intel) |
|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
|  | DTC status mask defines the status of DTCs to be read. The values are application specific. |
|  | DTC severity mask defines the severity information of DTCs to be read. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | DTCs returns the resulting DTCs as an array of clusters: DTC is the resulting Diagnostic Trouble Code. You can use or to convert this to readable format as SAE J1939 and SAE J2012 define.Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information.Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
| --- | --- |
|  | DTC is the resulting Diagnostic Trouble Code. You can use or to convert this to readable format as SAE J1939 and SAE J2012 define. |
|  | Status is the DTC status. Usually, this is a bit field with the following meaning: BitMeaning0testFailed1testFailedThisMonitoringCycle2pendingDTC3confirmedDTC4testNotCompletedSinceLastClear5testFailedSinceLastClear6testNotCompletedThisMonitoringCycle7warningIndicatorRequested For OBD, this field usually does not contain valid information. |
| Bit | Meaning |
| 0 | testFailed |
| 1 | testFailedThisMonitoringCycle |
| 2 | pendingDTC |
| 3 | confirmedDTC |
| 4 | testNotCompletedSinceLastClear |
| 5 | testFailedSinceLastClear |
| 6 | testNotCompletedThisMonitoringCycle |
| 7 | warningIndicatorRequested |
|  | Add Data contains optional additional data for this DTC. Usually, this does not contain valid information (refer to DTC descriptor) |
|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
|  | DTC status availability mask is an application-specific value returned for all DTCs. |
|  | DTC severity availability mask is an application-specific value returned for all DTCs. |
|  | DTC format identifier is an application-specific value returned for all DTCs. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD ReadDTCInformation service is based on the UDS ReaDTCInformation service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-freeze-frame-information-vi.html language=enus -->
## TOPIC 00118: WWH-OBD Request Freeze Frame Information.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-freeze-frame-information-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-freeze-frame-information-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs). Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it

### WWH-OBD Request Freeze Frame Information.vi

Purpose

Executes the WWH-OBD ReadDTCInformation service. Reads selected Diagnostic Trouble Codes (DTCs).
Format

[IMAGE alt='image' src='images/WWHOBDRequestFreezeFrameInformationVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | DTC mask record defines the DTC to be read. The values are application specific. |
|  | DTC record number specifies the snapshot record number. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns the ECU data record. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD ReadDTCInformation service is based on the UDS ReaDTCInformation service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-rid-vi.html language=enus -->
## TOPIC 00119: WWH-OBD Request RID.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-rid-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-rid-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD RoutineControl service. Reads a data record from the ECU. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary t

### WWH-OBD Request RID.vi

Purpose

Executes the WWH-OBD RoutineControl service. Reads a data record from the ECU.
Format

[IMAGE alt='image' src='images/WWHOBDRequestRIDVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | mode defines the service operation mode. You can obtain the values from a ring control: 1:Start Routine2:Stop Routine3:Request Routine Results Other values are application specific. |
| 1: | Start Routine |
| 2: | Stop Routine |
| 3: | Request Routine Results |
|  | routine identifier defines the identifier of the routine to be started. The values are application specific. |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | data out returns application-specific output parameters from the routine. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD RoutineControl service is based on the UDS RoutineControl service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-supported-dids-vi.html language=enus -->
## TOPIC 00120: WWH-OBD Request Supported DIDs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-supported-dids-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-supported-dids-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD ReadDataByIdentifier service to retrieve the valid DID values for this service. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally,

### WWH-OBD Request Supported DIDs.vi

Purpose

Executes the WWH-OBD ReadDataByIdentifier service to retrieve the valid DID values for this service.
Format

[IMAGE alt='image' src='images/WWHOBDRequestSupportedDIDsVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | DID specifies the diagnostic data identifier for this service. The following values are valid and can be obtained through an enum control: 0:PID: parameter identifier1:MID: monitor identifier2:ITID: info type identifier |
| 0: | PID: parameter identifier |
| 1: | MID: monitor identifier |
| 2: | ITID: info type identifier |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | DIDs out returns an array of valid DIDs. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD ReadDataByIdentifier service is based on the UDS ReadDataByIdentifier service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-request-supported-rids-vi.html language=enus -->
## TOPIC 00121: WWH-OBD Request Supported RIDs.vi

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-request-supported-rids-vi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-request-supported-rids-vi.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Purpose Executes the WWH-OBD RoutineControl service to retrieve the valid RID values for this service. Format Input diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is

### WWH-OBD Request Supported RIDs.vi

Purpose

Executes the WWH-OBD RoutineControl service to retrieve the valid RID values for this service.
Format

[IMAGE alt='image' src='images/WWHOBDRequestSupportedRIDsVI.gif']
Input

|  | diag ref in specifies the diagnostic session handle, obtained from Open Diagnostic on CAN FD.vi or Open Diagnostic on IP.vi and wired through subsequent diagnostic VIs. Normally, it is not necessary to manually manipulate the elements of this cluster. |
| --- | --- |
|  | error in is a cluster that describes error conditions occurring before the VI executes. If an error has already occurred, the VI returns the value of the error in cluster to error out. status is TRUE if an error occurred. This VI is not executed when status is TRUE.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. This VI is not executed when status is TRUE. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Output

|  | diag ref out is a copy of diag ref in. You can wire it to subsequent diagnostic VIs. |
| --- | --- |
|  | RIDs out returns an array of valid RIDs. |
|  | success? indicates successful receipt of a positive response message for this diagnostic service. |
|  | error out describes error conditions. If the error in cluster indicated an error, the error out cluster contains the same information. Otherwise, error out describes the error status of this VI. status is TRUE if an error occurred.code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler.source identifies the VI where the error occurred. |
|  | status is TRUE if an error occurred. |
|  | code is the error code number identifying an error. A value of 0 means success. A negative value means error: the VI did not execute the intended operation. A positive value means warning: the VI executed intended operation, but an informational warning is returned. For a description of the code, wire the error cluster to a LabVIEW error-handling VI, such as the Simple Error Handler. |
|  | source identifies the VI where the error occurred. |

Description

The WWH-OBD RoutineControl service is based on the UDS RoutineControl service (ISO 14229-1).

Parent topic:

WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit-labview-api-ref path=wwh-obd-world-wide-harmonized-on-board-diagno2.html language=enus -->
## TOPIC 00122: WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

- bundle_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- source_path: `wwh-obd-world-wide-harmonized-on-board-diagno2.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit-labview-api-ref/raw/resource/enus/wwh-obd-world-wide-harmonized-on-board-diagno2.html
- document_id: `automotive-diagnostic-command-set-toolkit-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: WWH-OBD Clear Emission Related DTCs.vi WWH-OBD Convert DTCs to J1939.vi WWH-OBD Convert DTCs to J2012.vi WWH-OBD Request DID.vi WWH-OBD Request DTC Extended Data Record.vi WWH-OBD Request Emission Related DTCs.vi WWH-OBD Request Freeze Frame Information.vi WWH-OBD Request RID.vi WWH-OBD Request Supp

### WWH-OBD (World Wide Harmonized On-Board Diagnostic) Services

[WWH-OBD Clear Emission Related DTCs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdclearemissionrelateddtcsvi)

[WWH-OBD Convert DTCs to J1939.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdconvertdtcstoj2012vi)

[WWH-OBD Convert DTCs to J2012.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdconvertdtcstoj2012vi)

[WWH-OBD Request DID.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestdidvi)

[WWH-OBD Request DTC Extended Data Record.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestdtcextendeddatarecordvi)

[WWH-OBD Request Emission Related DTCs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestemissionrelateddtcsvi)

[WWH-OBD Request Freeze Frame Information.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestfreezeframeinformationvi)

[WWH-OBD Request RID.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestridvi)

[WWH-OBD Request Supported DIDs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestsupporteddidsvi)

[WWH-OBD Request Supported RIDs.vi](/csh?context=automotive-diagnostic-command-set-toolkit_adcs_wwhobdrequestsupportedridsvi)

Parent topic:

Automotive Diagnostic Command Set API for LabVIEW
